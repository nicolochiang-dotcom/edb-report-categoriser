"""Category definitions for the EDB report categorisation tool.

This file is the "brain" of the categoriser. To improve accuracy, edit the
descriptions and notes below - no other file needs to change.

Each category has:
  id          - the number used in the spreadsheet column
  name        - the column heading
  description - what belongs in this category
  notes       - how to tell it apart from categories it is often confused
                with (set to None if not needed)
"""

CATEGORIES = [
    {
        "id": 1,
        "name": "Role of SG setup (GHQ/RHQ/no HQ)",
        "description": (
            "Factual statements about what role the company's Singapore "
            "entity plays. Look for: global headquarters (GHQ) or global "
            "mandates run from Singapore; regional/APAC headquarters (RHQ); "
            "or an explicitly NON-headquarters presence such as a sales "
            "office, plant, distribution centre or holding entity. Also "
            "covers CHANGES to that role - upgrading an office to an RHQ, "
            "relocating HQ mandates into or out of Singapore, or a company "
            "actively evaluating/considering an HQ move. Statements that a "
            "company is explicitly NOT setting up an HQ, or has no HQ "
            "intention at this stage, belong here too."
        ),
        "notes": (
            "This category is about WHAT the setup is, not WHY it was "
            "chosen. Reasons for choosing Singapore belong in categories "
            "3-20. Distinguish from category 2: category 1 is the STATUS of "
            "the entity (GHQ/RHQ/no HQ); category 2 is the specific "
            "FUNCTIONS placed here. A passage naming both can be tagged "
            "with both."
        ),
    },
    {
        "id": 2,
        "name": "What HQ functions do they place in Singapore?",
        "description": (
            "Statements naming or describing which specific headquarters "
            "functions the company locates in Singapore. Examples of such "
            "functions: group or regional finance, treasury, tax and risk "
            "management; legal and compliance; strategy and corporate "
            "development; business development and commercial leadership; "
            "marketing and brand; supply chain, procurement and logistics "
            "management; HR and people functions; IT, digital and data or "
            "analytics teams; R&D and innovation leadership; and C-suite or "
            "senior leadership roles based in Singapore."
        ),
        "notes": (
            "Tag the FUNCTIONS themselves, not the reasons for placing them "
            "here. If a passage lists functions AND gives a reason, tag "
            "category 2 plus whichever reason category (3-20) applies. See "
            "also the note under category 1."
        ),
    },
    {
        "id": 3,
        "name": (
            "Singapore's long-term thinking and consistency make us a safe "
            "harbour for businesses to weather disruption"
        ),
        "description": (
            "Singapore's long-term planning horizon, policy consistency and "
            "predictability OVER TIME make it a safe harbour where "
            "companies can shelter from external disruption - geopolitical "
            "tension, trade wars and tariffs, supply chain shocks, "
            "pandemics, regional instability, or volatility elsewhere. "
            "Typical signals: the government 'thinks in decades'; policy "
            "does not swing with election cycles; direction is "
            "well-signalled far in advance; Singapore is a stable anchor or "
            "safe pair of hands while the rest of the region or world is "
            "turbulent; the company can plan years ahead with confidence."
        ),
        "notes": (
            "MOST CONFUSED WITH CATEGORY 4. Use category 3 when the "
            "emphasis is on CONSISTENCY OVER TIME and being a REFUGE FROM "
            "EXTERNAL DISRUPTION (long-term planning, predictable policy "
            "direction, weathering turbulence). Use category 4 when the "
            "emphasis is on POLITICAL STABILITY and the LEGAL SYSTEM (rule "
            "of law, contracts, courts, IP, regulatory certainty) as the "
            "assurance behind a specific investment or strategic decision. "
            "Many real passages genuinely cover both ideas - when a speaker "
            "links long-term predictability AND legal/political stability, "
            "tag BOTH 3 and 4 rather than choosing one."
        ),
    },
    {
        "id": 4,
        "name": (
            "Singapore's stability and rule of law give companies the "
            "assurance they need to make long-term strategic decisions and "
            "investments"
        ),
        "description": (
            "Singapore's political stability and strong legal and "
            "regulatory system give companies the confidence to commit to "
            "long-term strategic decisions and capital investment. Typical "
            "signals: rule of law; contract enforceability; a clean, "
            "reliable and independent judiciary; intellectual property "
            "protection; regulatory certainty and clear, consistently "
            "applied rules; low corruption in a legal/governance sense; a "
            "stable political environment that de-risks committing capital "
            "or making a multi-year or multi-decade commitment."
        ),
        "notes": (
            "See the disambiguation under category 3 - read it before "
            "choosing between 3 and 4. Mentions of the LEGAL system, "
            "courts, contracts, IP protection, regulatory certainty or the "
            "phrase 'rule of law' point to category 4. If the passage is "
            "specifically about FINANCIAL regulation, banking or treasury "
            "security, prefer category 5."
        ),
    },
    {
        "id": 5,
        "name": (
            "Our trusted environment and premier financial centre status "
            "enable secure multinational operations"
        ),
        "description": (
            "Singapore's status as a leading, well-regulated financial "
            "centre and a trusted jurisdiction enables companies to run "
            "secure multinational operations. Typical signals: depth and "
            "quality of banking; treasury, cash management and "
            "capital-allocation centres; access to capital, financing, fund "
            "structures and capital markets; sound and respected financial "
            "regulation (e.g. MAS); a deep pool of financial and "
            "professional services expertise; and general institutional "
            "trust that makes Singapore a safe place to hold, move and "
            "manage money across borders."
        ),
        "notes": (
            "Passages specifically about FINANCE - banks, treasury, "
            "fundraising, capital, financial regulation, fund management - "
            "belong here rather than in categories 3, 4 or 20. If the "
            "passage is about the company PLACING a treasury or finance "
            "function in Singapore, also tag category 2."
        ),
    },
    {
        "id": 6,
        "name": "Singapore has no hidden costs; what you see is what you get",
        "description": (
            "The transparency and predictability of the cost of doing "
            "business in Singapore. Typical signals: no corruption, bribes, "
            "facilitation payments or informal costs; transparent, "
            "published fees and rules; costs that can be modelled and "
            "budgeted accurately upfront; no unpleasant surprises. "
            "Companies often acknowledge Singapore looks expensive on paper "
            "while arguing the TOTAL, all-in cost is honest and predictable "
            "compared with cheaper-looking alternatives, and that this "
            "predictability itself has real value."
        ),
        "notes": (
            "The defining element is TRANSPARENCY or PREDICTABILITY of "
            "cost. A complaint that Singapore is simply expensive, with no "
            "transparency angle, belongs in category 21 (Challenges), not "
            "here. A passage that acknowledges high cost BUT praises the "
            "predictability can be tagged with both 6 and 21."
        ),
    },
    {
        "id": 7,
        "name": (
            "Singapore's strong digital infrastructure and business & "
            "research ecosystem enable companies to ascend the value chain, "
            "particularly in innovation and R&D"
        ),
        "description": (
            "Singapore's digital infrastructure and its business and "
            "research ecosystem let companies move up the value chain, "
            "particularly into innovation and R&D, positioning them at the "
            "forefront of their industry. Typical signals: R&D centres, "
            "innovation labs, product development and pilot projects; "
            "collaboration with universities, A*STAR, public research "
            "institutes or government innovation programmes; partnerships "
            "with startups, suppliers or industry peers; IP creation; "
            "strong digital and data infrastructure, connectivity, data "
            "centres and testbeds; and shifting Singapore activity from "
            "routine work toward higher-value, technology-led work."
        ),
        "notes": (
            "'Digital infrastructure' here means DIGITAL and RESEARCH "
            "capability. Physical infrastructure for moving people and "
            "goods (airport, port, logistics) belongs in category 13. If a "
            "passage describes placing an R&D or digital TEAM here, also "
            "tag category 2."
        ),
    },
    {
        "id": 8,
        "name": (
            "Companies can unlock dual benefits of Singapore and our "
            "regional partners with the SG+ model"
        ),
        "description": (
            "Companies pairing Singapore with a nearby location to get the "
            "best of both - Singapore as the global or regional HQ and home "
            "for high-value functions, and the partner location for its "
            "cost-competitive skilled workforce, land and growing "
            "industrial base. Johor and the Johor-Singapore Special "
            "Economic Zone (JS-SEZ) are the primary examples; Batam, "
            "Bintan, Iskandar and similar twinning arrangements also count. "
            "Typical signals: 'HQ in Singapore, operations/manufacturing/ "
            "back-office across the border'; splitting activities between "
            "Singapore and a neighbouring location; asking about or "
            "evaluating the SG+ or JS-SEZ model."
        ),
        "notes": (
            "Requires a TWINNING element - Singapore PLUS another nearby "
            "location working together. A company simply comparing "
            "Singapore against Malaysia and choosing one is not SG+; that "
            "is category 1, 20 or 21 depending on the framing."
        ),
    },
    {
        "id": 9,
        "name": (
            "Companies can build their A-teams in Singapore with a strong "
            "pool of skilled local talent and access to top global talent"
        ),
        "description": (
            "Companies can assemble high-calibre teams in Singapore because "
            "of the strength of the LOCAL talent pool combined with the "
            "ability to attract and bring in TOP GLOBAL talent. Typical "
            "signals: praise for the quality, depth, skills or "
            "professionalism of the workforce; availability of specific "
            "expertise (engineering, digital, finance, maritime, "
            "scientific); being able to hire specialists locally without "
            "relocating them; Singapore as a place where senior "
            "international hires are willing to be based; multilingual or "
            "multicultural teams able to cover the region."
        ),
        "notes": (
            "MOST CONFUSED WITH CATEGORY 10. Category 9 is about the "
            "TALENT ITSELF - skills, availability, calibre, ability to "
            "hire. Category 10 is about the LIVEABILITY that attracts and "
            "retains that talent - schools, safety, healthcare, family "
            "life. A passage about hiring a strong engineering team is 9; a "
            "passage about executives relocating because their families "
            "will be happy is 10. Talent SHORTAGES, wage inflation, losing "
            "candidates to competitors, or work-pass difficulties are "
            "NEGATIVE and belong in category 21 - though a passage praising "
            "the talent pool while also flagging a shortage can be tagged "
            "with both 9 and 21."
        ),
    },
    {
        "id": 10,
        "name": (
            "Singapore provides a high standard of living to attract top "
            "global talent and, importantly, for their children and families"
        ),
        "description": (
            "Singapore's quality of life makes it easy to attract and "
            "retain top global talent, with particular weight on their "
            "children and families. Typical signals: international schools "
            "and education quality; personal safety and low crime; "
            "healthcare; housing and general liveability; cleanliness and "
            "green space; ease and comfort of relocating a family; spouses "
            "and children settling well; executives being personally "
            "willing or keen to move to Singapore; and favourable "
            "comparisons with other regional hubs that staff are reluctant "
            "to relocate their families to."
        ),
        "notes": (
            "See the disambiguation under category 9 - read it before "
            "choosing between 9 and 10. If the passage mentions family, "
            "schools, safety, healthcare or liveability, it points here. "
            "The high cost of living as a COMPLAINT belongs in category 21."
        ),
    },
    {
        "id": 11,
        "name": "Singapore has the optimal time zone for global operations",
        "description": (
            "Singapore's time zone position makes it practical to run "
            "global or regional operations. Typical signals: the working "
            "day overlaps with both Europe and Asia (and can hand off to "
            "the Americas); same-day coordination across markets; "
            "convenient for calls with headquarters in Europe or the US; "
            "supports follow-the-sun operations; sits at a natural midpoint "
            "for a business spanning several continents."
        ),
        "notes": (
            "Requires an actual reference to TIME, time zones, working "
            "hours or scheduling. Geographic centrality without a time "
            "element usually points to category 12, 13 or 19."
        ),
    },
    {
        "id": 12,
        "name": (
            "Singapore serves as a global gateway, enabling companies to "
            "reach world markets from a single strategic location"
        ),
        "description": (
            "Singapore as a base from which companies serve GLOBAL markets "
            "- running worldwide mandates, exporting and selling "
            "internationally, and reaching customers beyond Asia from one "
            "strategic location. Typical signals: serving 'global' or "
            "'worldwide' customers from Singapore; a global mandate run out "
            "of Singapore; using Singapore's trade agreements and open "
            "trading status to access many markets; Singapore as the hinge "
            "between East and West."
        ),
        "notes": (
            "MOST CONFUSED WITH CATEGORIES 13 AND 19. Use the scope of the "
            "market as the test. Category 12 = reaching the WORLD or "
            "markets beyond Asia. Category 19 = reaching SOUTHEAST ASIA or "
            "ASEAN specifically. Category 13 = the PHYSICAL means of "
            "movement (flights, port, logistics, travel). A passage may "
            "genuinely cover more than one - for example, a company using "
            "Changi's network to serve global customers is both 12 and 13 - "
            "in which case tag all that apply."
        ),
    },
    {
        "id": 13,
        "name": (
            "Singapore offers excellent global connectivity that enables "
            "seamless movement of people and goods"
        ),
        "description": (
            "Singapore's physical and logistical connectivity for moving "
            "people and goods. Typical signals: Changi Airport's flight "
            "network and ease of business travel; the seaport, "
            "transshipment volumes and shipping links; air and sea freight "
            "capability; logistics and distribution infrastructure; "
            "efficient customs and cargo handling; and the practical ease "
            "of getting staff, customers or products to and from anywhere."
        ),
        "notes": (
            "See the disambiguation under category 12. This category is "
            "about PHYSICAL movement infrastructure. Digital connectivity "
            "belongs in category 7."
        ),
    },
    {
        "id": 14,
        "name": (
            "Singapore's efficiency means businesses can focus on growing "
            "their business and not navigating bureaucracy"
        ),
        "description": (
            "Singapore's administrative and regulatory efficiency frees "
            "companies to focus on the business itself rather than on "
            "process. Typical signals: fast, simple company incorporation; "
            "quick permits, licences and approvals; responsive, pragmatic, "
            "business-minded government agencies; efficient digital "
            "government services; ease of doing business generally; things "
            "simply working as expected; being operational faster in "
            "Singapore than elsewhere; and time not lost to paperwork or "
            "red tape."
        ),
        "notes": (
            "MOST CONFUSED WITH CATEGORY 15. Category 14 is about TIME, "
            "SPEED and ADMINISTRATIVE EASE. Category 15 is about COST "
            "SAVINGS achieved by consolidating hub activities in Singapore. "
            "If a passage argues efficiency translates into money saved, it "
            "can be tagged with both. Note that PREDICTABILITY of cost is "
            "category 6, and REGULATORY CERTAINTY in a legal sense is "
            "category 4."
        ),
    },
    {
        "id": 15,
        "name": (
            "Companies are setting up HQ hub activities in Singapore to "
            "achieve cost savings"
        ),
        "description": (
            "Companies centralising or consolidating HQ and hub activities "
            "in Singapore in order to save cost. Typical signals: shared "
            "services centres; centralised procurement, treasury, finance "
            "or back-office operations; removing duplicated country-level "
            "functions in favour of one regional hub; economies or "
            "efficiency of scale framed in cost terms; explicit projected "
            "savings or overhead reduction from consolidating into "
            "Singapore."
        ),
        "notes": (
            "See the disambiguation under category 14. The defining "
            "elements are CONSOLIDATION and COST SAVING. If the passage "
            "also names which functions are being consolidated, tag "
            "category 2 as well."
        ),
    },
    {
        "id": 16,
        "name": (
            "Companies stay for long and grow their presence further after "
            "experiencing the benefits of Singapore's trust, certainty and "
            "business-friendly infrastructure"
        ),
        "description": (
            "Evidence that companies remain in Singapore for the long term "
            "and deepen their presence AFTER experiencing what Singapore "
            "offers. Typical signals: long tenure or anniversaries ('we have "
            "been here 20 years'); headcount or footprint growth over time; "
            "repeated reinvestment or successive expansions; adding new "
            "mandates, functions or business lines over the years; "
            "upgrading the Singapore entity's role after a positive "
            "experience; and 'we came for X, but we stayed and grew because "
            "of Y' narratives."
        ),
        "notes": (
            "Requires an element of TENURE or GROWTH OVER TIME - a "
            "retrospective view of an established presence. A first-time "
            "investment decision or a new company evaluating Singapore does "
            "NOT belong here, even if they intend to grow later. If the "
            "passage also names the reason they stayed, tag that reason "
            "category (3-20) as well."
        ),
    },
    {
        "id": 17,
        "name": "HQs create good jobs for Singaporeans",
        "description": (
            "The HQ presence creating good employment for Singaporeans. "
            "Typical signals: numbers hired or headcount growth; the share "
            "or proportion of local employees; the QUALITY of roles created "
            "(professional, managerial, executive and technical / PMET "
            "roles rather than low-skilled ones); high-value functions "
            "staffed locally; and commitments to hire Singaporeans."
        ),
        "notes": (
            "MOST CONFUSED WITH CATEGORY 18. Category 17 is about JOBS "
            "CREATED - the number and quality of positions. Category 18 is "
            "about what happens to Singaporeans IN those jobs over time - "
            "progression, development and advancement. A passage covering "
            "both hiring and progression should be tagged with both."
        ),
    },
    {
        "id": 18,
        "name": "HQs create good career pathways for Singaporeans",
        "description": (
            "The HQ presence creating career development and progression "
            "for Singaporeans. Typical signals: local staff promoted into "
            "regional or global leadership roles; leadership development "
            "and talent programmes; overseas postings, rotations and "
            "secondments; exposure to global mandates and senior "
            "decision-making; skills and technology transfer to local "
            "employees; and Singaporeans rising through the company over "
            "the years."
        ),
        "notes": (
            "See the disambiguation under category 17. The defining element "
            "is PROGRESSION or DEVELOPMENT over time, not the existence of "
            "the job."
        ),
    },
    {
        "id": 19,
        "name": "Singapore is a choice gateway for companies to access SEA",
        "description": (
            "Singapore as the base for accessing SOUTHEAST ASIA and ASEAN "
            "specifically. Typical signals: springboard, launchpad or "
            "beachhead into the region; managing or coordinating Southeast "
            "Asian operations from Singapore; targeting Indonesia, Vietnam, "
            "Thailand, Malaysia, the Philippines and similar markets; "
            "testing or entering the regional market from a Singapore base; "
            "proximity to and familiarity with the region; and ASEAN growth "
            "or trade lanes as the commercial priority."
        ),
        "notes": (
            "See the disambiguation under category 12. The test is the "
            "MARKET SCOPE: Southeast Asia / ASEAN / 'the region' points "
            "here, whereas global or worldwide reach points to category 12. "
            "'Asia-Pacific' broadly can point to either or both - judge "
            "from context."
        ),
    },
    {
        "id": 20,
        "name": "Other points that make companies choose Singapore",
        "description": (
            "Clearly POSITIVE reasons for choosing or valuing Singapore "
            "that do not fit any of categories 3-19. Examples of what can "
            "land here: tax treatment, incentives and grants; the personal "
            "familiarity, history or comfort of company leadership with "
            "Singapore; sustainability and green infrastructure; "
            "geopolitical neutrality or being a trusted bridge between "
            "major powers; the presence of industry peers, customers or "
            "suppliers creating cluster effects; use of English as a "
            "working language; and government support or the quality of the "
            "relationship with agencies such as EDB."
        ),
        "notes": (
            "Use ONLY when no specific category (3-19) fits. This is a "
            "residual category, not a dumping ground - always check "
            "categories 3-19 first, and prefer a specific category even if "
            "the fit is imperfect. Do not use it for negative points "
            "(category 21) or neutral operational information (category 22)."
        ),
    },
    {
        "id": 21,
        "name": "Challenges",
        "description": (
            "Anything raised as a problem, obstacle, risk, concern, "
            "frustration or reason to hesitate about Singapore. Typical "
            "signals: high and rising costs (rent, wages, cost of living, "
            "overall cost base); talent shortages, wage inflation, or "
            "losing candidates to competitors; work-pass, quota or "
            "immigration difficulties; competition from other hubs such as "
            "Hong Kong, Dubai, Kuala Lumpur, Bangkok or Ho Chi Minh City; "
            "regulatory or compliance pain points; land, space or capacity "
            "constraints; small domestic market; and any dissatisfaction, "
            "hesitation or unmet expectation expressed by the company."
        ),
        "notes": (
            "NEGATIVE VALENCE OVERRIDES TOPIC. If a passage is a complaint "
            "or concern, it belongs here even when its subject matter "
            "overlaps another category - for example, a complaint about "
            "port congestion is category 21, not 13, and difficulty getting "
            "work passes is 21, not 9. Where a passage praises something "
            "AND raises a concern about it, tag both the positive category "
            "and 21. Include challenges the company faces in Singapore and "
            "those that would count against choosing Singapore."
        ),
    },
    {
        "id": 22,
        "name": "Things to note",
        "description": (
            "Neutral but noteworthy operational information an officer "
            "should be aware of. Typical signals: follow-up actions, next "
            "steps and asks of EDB; decision timelines and when a decision "
            "is expected; upcoming visits, meetings or leadership changes; "
            "internal company dynamics, reviews or restructuring; "
            "confidentiality or sensitivity flags; funding or investment "
            "status; competitive intelligence about what other "
            "jurisdictions are offering; and background or context useful "
            "for future engagement."
        ),
        "notes": (
            "This is for NEUTRAL, operationally useful information. If the "
            "content is a problem or concern, prefer category 21. If it is "
            "a positive reason for choosing Singapore, prefer categories "
            "3-20. Like category 20, this is a residual category - do not "
            "use it as a dumping ground for anything that does not fit "
            "elsewhere; the passage must be genuinely worth an officer's "
            "attention."
        ),
    },
]