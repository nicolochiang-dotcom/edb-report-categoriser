"""Send report text to Google Gemini and get back categorised extractions
plus report-level metadata (home country, industry, engagement type, date).
"""

import json
import time
from typing import Any

from dotenv import load_dotenv
from google import genai
from google.genai import errors, types

from categories import CATEGORIES

load_dotenv()  # makes GEMINI_API_KEY from .env available

MODEL = "gemini-2.5-flash"    # "gemini-2.5-pro" needs a paid/billed account
MAX_OUTPUT_TOKENS = 8000      # raise if very long reports get truncated
MAX_RETRIES = 4

client = genai.Client()       # picks up GEMINI_API_KEY automatically


# ---------------------------------------------------------------------------
# 1. Build the system prompt from categories.py
# ---------------------------------------------------------------------------

RULES = """\
INSTRUCTIONS

You will be given one report (a meeting note, call report or similar)
inside <report> tags. Read the ENTIRE report, then produce TWO things:
(A) the report-level METADATA described below, and (B) the extracted
passages for the categories above.

PASSAGE RULES
1. Extract passages VERBATIM - copy the exact wording from the report.
   Include enough surrounding sentence(s) for the passage to be
   understandable on its own, but do not copy whole pages.
2. A passage may belong to MULTIPLE categories - list every category
   that genuinely applies.
3. Do NOT force-fit: if a paragraph is not clearly relevant to any
   category, skip it. It is correct to return few extractions for a
   thin report.
4. Never invent, paraphrase or summarise text into the passage field.
5. rationale: one short sentence explaining why the passage fits the
   category/categories you chose.
6. confidence: "high" if the fit is obvious, "medium" if reasonable
   people could disagree, "low" if it is a stretch but worth flagging
   for human review.
7. Prefer the most specific category over category 20 (Other) and
   category 22 (Things to note). Use those two only when nothing more
   specific applies.
8. Category 21 (Challenges) applies to anything with negative valence,
   even if the topic overlaps another category.
"""

METADATA_RULES = """\
METADATA RULES

Extract four pieces of report-level metadata. Use your best judgement; if a
field genuinely cannot be determined from the report, return an empty string
"" rather than guessing.

- home_country: The country where the company is headquartered globally (its
  home / source country), e.g. "Germany", "United States", "Japan". For a
  multiplier or roundtable engagement, use the country the body represents
  (e.g. a UK business council -> "United Kingdom"). Use the common English
  country name only - no city, no region.

- industry: The company's primary industry, as a SHORT standard cluster-style
  name of the kind EDB uses, for example: "Semiconductors", "Chemicals &
  Materials", "Healthcare", "Logistics & Supply Chain", "Financial Services",
  "Consumer Businesses", "Digital / Infocomm", "Advanced Manufacturing",
  "Aerospace", "Marine & Offshore", "Energy", "Agri-Food", "Professional
  Services", "Urban Solutions & Sustainability". Pick whatever best fits the
  report - you are not limited to this list - but prefer these short standard
  names over inventing long descriptions.

- engagement_type: What kind of engagement the report covers. Choose exactly
  ONE of these values:
    "Company"                  - a meeting or call with a single company
    "Multiplier - Chamber"     - a chamber of commerce or business council
                                 (e.g. UKABC, EuroCham)
    "Multiplier - Roundtable"  - a roundtable or group session with several
                                 companies (e.g. a Spanish business roundtable)
    "Multiplier - Association" - a trade or industry association
    "Multiplier - Other"       - any other intermediary body representing
                                 multiple companies
    "Government"               - engagement with a government or public body
    "Other"                    - none of the above

- report_date: The date of the report or meeting, formatted STRICTLY as
  DD/MM/YYYY (e.g. "19/06/2026"). Zero-pad day and month. If only a month and
  year are given, use 01 as the day. If no date appears anywhere, return "".
"""


def build_system_prompt() -> str:
    blocks = [
        "You are an analyst at the Singapore Economic Development Board "
        "(EDB). Your job is to read internal reports, extract report-level "
        "metadata, and extract passages relevant to a fixed list of "
        "categories about why companies choose and operate in Singapore."
        "\n\nTHE CATEGORIES:"
    ]

    for cat in CATEGORIES:
        block = (
            f"CATEGORY {cat['id']}: {cat['name']}\n"
            f"Definition: {cat['description']}"
        )

        if cat.get("notes"):
            block += f"\nDisambiguation: {cat['notes']}"

        blocks.append(block)

    blocks.append(RULES)
    blocks.append(METADATA_RULES)
    return "\n\n".join(blocks)


# ---------------------------------------------------------------------------
# 2. The exact JSON shape the model should return
#    (Gemini-compatible: no additionalProperties / minimum / maximum)
# ---------------------------------------------------------------------------

OUTPUT_SCHEMA = {
    "type": "object",
    "properties": {
        "metadata": {
            "type": "object",
            "properties": {
                "home_country": {
                    "type": "string",
                    "description": "Company's global HQ country, e.g. 'Germany'.",
                },
                "industry": {
                    "type": "string",
                    "description": "Short EDB-style industry cluster name.",
                },
                "engagement_type": {
                    "type": "string",
                    "description": "Company / Multiplier - Chamber / etc.",
                },
                "report_date": {
                    "type": "string",
                    "description": "Date of report as DD/MM/YYYY, or ''.",
                },
            },
            "required": [
                "home_country",
                "industry",
                "engagement_type",
                "report_date",
            ],
        },
        "extractions": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "passage": {
                        "type": "string",
                        "description": "Verbatim text copied from the report.",
                    },
                    "categories": {
                        "type": "array",
                        "items": {"type": "integer"},
                        "description": "Category id numbers (1-22) that apply.",
                    },
                    "rationale": {
                        "type": "string",
                        "description": "One sentence: why these categories fit.",
                    },
                    "confidence": {
                        "type": "string",
                        "enum": ["high", "medium", "low"],
                    },
                },
                "required": ["passage", "categories", "rationale", "confidence"],
            },
        },
    },
    "required": ["metadata", "extractions"],
}

VALID_IDS = {c["id"] for c in CATEGORIES}

METADATA_FIELDS = ["home_country", "industry", "engagement_type", "report_date"]


# ---------------------------------------------------------------------------
# 3. Helpers
# ---------------------------------------------------------------------------

def _is_retryable_error(err: errors.APIError) -> bool:
    """Retry only temporary Gemini/API errors."""
    return getattr(err, "code", None) in {408, 429, 500, 502, 503, 504}


def _response_to_dict(response: Any) -> dict:
    """Convert Gemini response into a normal Python dict."""
    if getattr(response, "parsed", None) is not None:
        parsed = response.parsed

        if hasattr(parsed, "model_dump"):
            return parsed.model_dump()

        if isinstance(parsed, dict):
            return parsed

    if not getattr(response, "text", None):
        raise RuntimeError("Gemini returned no text output.")

    return json.loads(response.text)


# ---------------------------------------------------------------------------
# 4. The API call, with retries for transient errors
# ---------------------------------------------------------------------------

def classify_report(report_text: str) -> tuple[dict, list[dict]]:
    """Return (metadata dict, list of extraction dicts) for one report."""
    system_prompt = build_system_prompt()

    user_prompt = (
        "Here is the report to analyse:\n\n"
        f"<report>\n{report_text}\n</report>"
    )

    response = None

    for attempt in range(1, MAX_RETRIES + 1):
        try:
            response = client.models.generate_content(
                model=MODEL,
                contents=user_prompt,
                config=types.GenerateContentConfig(
                    system_instruction=system_prompt,
                    temperature=0,
                    max_output_tokens=MAX_OUTPUT_TOKENS,
                    response_mime_type="application/json",
                    response_schema=OUTPUT_SCHEMA,
                ),
            )
            break

        except errors.APIError as err:
            if attempt == MAX_RETRIES or not _is_retryable_error(err):
                raise

            wait = 2 ** attempt  # 2, 4, 8 seconds
            print(
                f"    transient Gemini API error ({type(err).__name__}, "
                f"code={getattr(err, 'code', 'unknown')}); retrying in {wait}s..."
            )
            time.sleep(wait)

        except (TimeoutError, ConnectionError, OSError) as err:
            if attempt == MAX_RETRIES:
                raise

            wait = 2 ** attempt
            print(
                f"    transient network error ({type(err).__name__}); "
                f"retrying in {wait}s..."
            )
            time.sleep(wait)

    data = _response_to_dict(response)

    # --- metadata: make sure every field exists, as a plain string ---
    raw_meta = data.get("metadata") or {}
    metadata = {
        field: str(raw_meta.get(field) or "").strip()
        for field in METADATA_FIELDS
    }

    # --- extractions: drop any category id not defined in categories.py ---
    cleaned = []
    for item in data.get("extractions", []):
        item["categories"] = [
            c for c in item.get("categories", []) if c in VALID_IDS
        ]
        if item["categories"]:
            cleaned.append(item)

    return metadata, cleaned