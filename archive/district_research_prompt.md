# district_research_prompt

---
version: 1.0
date: 2026-01-21
purpose: Produce a comprehensive, neutral, and strictly forensic research document on a U.S. House district
tool: Manus AI or similar research tools with web search capability
legacy_version: U.S. House District Research Prompt v4.5
---

## Naming Convention

**Follow the conventions in the attached `district_naming_prompt.md` file.**

Output filename pattern: `[district]_overview.md`

Example: `NJ-11_overview.md`

**CRITICAL: Document H1 header must match the filename (without `.md`):**

Example: `# NJ-11_overview`

**YAML metadata block (immediately after H1):**

```yaml
---
district: NJ-11
type: overview
date: 2026-01-21
prompt: district_research_prompt.md
prompt_version: 1.0
status: Research Complete
---
```

---

## Document Header (Required — Top of Report)

Every research report must begin with a condensed document header containing the following fields in a single horizontal text block, after the YAML metadata. This format maximizes information density.

**Format:**

`[State] [District] ([Stage]) | Ratings: [Cook]/[Inside Elections] | PVI: [Score] | Incumbent: [Name] | Map: [Link]`

**Example:**

`New Jersey 11th Congressional District (NJ-11) (Primary) | Ratings: Lean D/Tilt D | PVI: D+2 | Incumbent: Mikie Sherrill (D) - First elected 2018 | Map: [Official District Map]`

**Additional Administrative Fields (Below Header):**

- **Report Type:** U.S. House District Research Report
- **Last Updated:** [Month Day, Year, Time, Timezone] (if different from Date Compiled)
- **Next Anticipated Update Trigger:** [Event and date]
  - Common trigger events include:
    - FEC filing deadlines (quarterly reports)
    - Primary or general election results
    - Filing deadlines for candidate entry
    - Court rulings on redistricting, ballot access, or candidate eligibility
    - Major endorsements or candidate withdrawals
  - If multiple triggers are plausible, list the earliest one.
- **Author/Source:** (Optional: e.g., "Manus AI" or analyst name)
- **Commissioned By:** (Optional: if applicable)

---

## Section 0: Administrative & Election Context

This section provides a high-level overview of the race and its key parameters. It should be presented as a table with the following fields:

- **Race Ratings:** Cook Political Report, Inside Elections, Sabato's Crystal Ball
- **Filing Deadline:** Date
- **Primary Date:** Date
- **Primary Type:** Open, closed, semi-closed, etc.
- **Runoff Threshold:** Percentage of vote required to avoid a runoff
- **Runoff Date:** Date (if applicable)
- **General Election:** Date
- **Incumbent:** Name (Party) - First elected year
- **District PVI:** Partisan Voter Index (e.g., R+5, D+2)
- **2024 Presidential Result:** Margin (e.g., Trump +10.2)
- **Map References:** Links to official district map, prior map reference, and Google Maps overlay (if available)
- **Primary System Citation:** Provide the statutory citation for the state's primary election mechanics (e.g., N.C. Gen. Stat. § 163-111). Source: National Conference of State Legislatures (NCSL).

---

## Section I: District Profile and Demographics

### I.A Geographic Overview

- **Counties:** List all counties (full or partial) in the district
- **Major Population Centers:** List major cities and towns
- **Economic Character:** Describe the district's economy (major industries, economic challenges)

### I.B Redistricting Analysis

If redistricting occurred, provide a detailed analysis:

- **Redistricting Delta Table:** [Prior Year] vs. [Current Year]
  - **Partisan Lean (PVI):** Change in PVI
  - **Presidential Margin:** Change in presidential vote margin
  - **Counties Added/Removed:** Net partisan impact
  - **Racial/Ethnic Composition:** Change in voting-age population by race
  - **Total Population:** Change in total population
  - **Computation Method Note:** Explain how the partisan lean was calculated (e.g., Cook PVI methodology).

- **Redistricting as a System:**
  - **Who Initiated:** Which party or body initiated redistricting
  - **Legal Authority:** Constitutional or statutory authority
  - **Mechanism:** Legislation, commission, court order, etc.
  - **Stated Rationale:** Official reason for redistricting
  - **Legal Status:** Approved, pending litigation, etc.
  - **Decision Timeline:** Key dates (passage, court rulings, filing deadlines)

- **Legal Challenges (Required if applicable):**
  
  If redistricting is subject to active litigation or legal challenge, provide:
  - **Case Name & Court:** Full case name and jurisdiction
  - **Status:** Active, pending ruling, resolved, etc. (as of report date)
  - **Parties:** Plaintiffs and defendants
  - **Legal Arguments:** Brief summary of each side's core argument (1-2 sentences each)
  - **Timeline:** Key dates (filing, hearing, expected ruling, filing deadlines that could be affected)
  - **Potential Impact:** What happens if plaintiffs prevail (e.g., "District reverts to [Year] boundaries with [PVI]")

  If no legal challenges exist, state: "No active legal challenges to redistricting as of [date]."

### I.C Demographics

- **Population:** Total population
- **Racial/Ethnic Composition:** Voting-age population by race
- **Age Distribution:** Median age, 65+ population
- **Educational Attainment:** Bachelor's degree or higher, high school diploma
- **Voter Registration:** By party (Democratic, Republican, Unaffiliated)
- **Data confidence flag:** Note if data is modeled or estimated.

### I.D Economic Profile

- **Median Household Income:** Compared to state median
- **Poverty Rate:** Compared to state average
- **Unemployment Rate:** Compared to state average
- **Major Industries:** List top 5 industries
- **Economic Challenges:** List key economic challenges

### I.E Electoral History

- **Presidential Performance ([Current Boundaries]):**
  - 2024: Margin
  - 2020: Margin

- **U.S. House Results (Historical Boundaries):**
  - 2024: Result, margin, district PVI
  - 2022: Result, margin, district PVI
  - 2020: Result, margin, district PVI

---

## Section II: Primary System Context, Institutional Power Dynamics, and Candidate Profiles

### II.A Primary System Context

- **Primary Type:** Open, closed, semi-closed
- **Runoff Threshold:** Percentage of vote required to avoid a runoff

- **Decisive Stage Classification (Required):** Classify the decisive stage of the election as one of the following. (Note: The PVI of +/-10 is used as a baseline for a safe seat, as districts with this level of partisan lean rarely flip.)
  - **Party Primary:** The primary winner is the prohibitive favorite due to strong partisan lean (PVI of D+10 or greater / R+10 or greater)
  - **General Election:** The race is competitive between parties; the general election determines the outcome
  - **Same-Party General:** Top-two or jungle primary systems may produce two candidates of the same party in the general election
  - **Indeterminate:** Unusual factors (strong independent, legal challenges, extreme primary fragmentation) make the decisive stage unclear
  - Provide a one-sentence justification citing PVI, recent electoral history, or other structural factors.

- **Unaffiliated Voter Impact (Required):** Assess the practical impact of unaffiliated voter participation as:
  - **Material:** Unaffiliated voters could determine the outcome under plausible turnout scenarios
  - **Marginal:** Unaffiliated voters may influence margins but are unlikely to be decisive
  - **Negligible:** Primary rules, registration patterns, or turnout history make unaffiliated participation insignificant
  - Provide a one-sentence justification based on registration share, historical participation, and primary competitiveness.

### II.B Institutional Power Dynamics (Required)

Identify formal and informal control mechanisms that structure candidate viability and voter behavior in this district. This section must contain only verifiable, observable facts about institutional power structures.

**Required Elements:**

- **Ballot Access / Ballot Position Control:** Does the state or district use a county line system (e.g., "The Line" in New Jersey) that grants organizational endorsements preferential ballot placement? If yes, which organizations control it? Provide statutory or regulatory citation if available.

- **Machine Strength:** Are there specific political machines, labor councils, or clubs that historically control the vote? Provide historical turnout data, documented examples, or vote share analysis from prior cycles.

- **Endorsement Culture / Kingmaker Endorsements:** Which specific local endorsements function as "kingmakers"? Are there formal or informal endorsements that historically determine primary outcomes? (e.g., party committee endorsements, labor council endorsements, influential elected officials)

- **Institutional Veto Points:** Are there structural barriers to entry (e.g., petition signature requirements, party committee approval, financial thresholds) that limit candidate viability?

- **Historical Precedent:** Cite specific examples from prior cycles where these mechanisms determined or significantly influenced outcomes.

**Format:** Present as a structured list or short paragraphs. 

**Minimum Investigation Requirement:** Even if no significant institutional power dynamics currently exist, provide at least 3-4 sentences documenting the investigation. This should include:
- What institutional structures were investigated (e.g., county party organizations, labor councils, political families/networks)
- Historical context if relevant (e.g., "South Texas has a documented history of Democratic political machines, but their influence has diminished since [X]")
- Why the conclusion was reached

Do NOT simply state "No significant institutional power dynamics identified" without this documentation.

### II.C Mechanical Risks & Edge Cases (Factual)

Identify and analyze structural risks that could influence the primary or general election outcome. For each identified risk, provide a relevance weighting (High / Medium / Low) and a one-sentence justification for that weighting. Present risks in descending order of relevance.

- Vote-splitting scenarios
- Runoff probability and timing implications
- Unaffiliated/independent voter participation effects
- Field size dynamics (plurality winner with low vote share)
- Special election timing effects
- Ballot design or access issues

### II.D Candidate Profiles

- **Candidate Classification Rule:** Classify candidates as **Contenders** or **Non-Contenders** based on:
  - Incumbency
  - Fundraising totals and cash on hand
  - Prior electoral performance
  - Media coverage and visibility
  - Endorsements or observable organizational support

- **Equal Depth Requirement:** Only Contenders require full analytical depth.

#### Contenders: Full Profile Required

For each contender, provide:

- **Detailed Background:** Name, party, residence, occupation, relevant biography
- **Electoral History:** Prior runs for office, win/loss record, vote margins
- **Incumbent Governing Record (if applicable):** Legislative record, committee assignments, notable votes, sponsorships
- **2026 Endorsements:** List all endorsements received in the current cycle
- **Coalition Indicators:** Observable support from key demographic or institutional groups
- **Campaign Finance:** Fundraising totals, cash on hand, burn rate, major donors

- **Strengths (Required):** Numbered list of 5-7 factual, verifiable advantages. Each item must be a standalone factual observation.
  
  **Instruction:** List only verifiable structural facts (e.g., "Incumbent with $3M cash on hand," "District voted Trump +10 in 2024," "Endorsed by [Organization] which delivered 15,000 votes in 2022 primary," "Outspent opponent 2:1 in prior cycle"). **Explicitly prohibit subjective adjectives** such as "charismatic," "momentum," "strong retail politician," or "energetic campaigner." Every strength must be a verifiable fact.

- **Constraints (Required):** Numbered list of 5-7 factual, verifiable challenges. Each item must be a standalone factual observation.
  
  **Instruction:** List only verifiable structural facts (e.g., "Has never run for office," "Raised only $50K in Q1," "District lost 10,000 manufacturing jobs since 2020," "Faces opponent with 2:1 cash advantage"). **Explicitly prohibit subjective adjectives** such as "lacks charisma," "disorganized campaign," "weak fundraising operation," or "low energy." Every constraint must be a verifiable fact.

- **Format Requirement:** Strengths and Constraints must be presented as separate numbered lists, not narrative paragraphs. Each item should be a standalone factual observation, not a compound sentence combining multiple points.

- **Conditional Qualifications (Required when applicable):**
  
  When a strength or constraint depends on a disputed or uncertain fact (e.g., redistricting under legal challenge, pending endorsement, unresolved ballot access), explicitly state the condition under which it holds.
  
  **Examples:**
  - "The new district has a more favorable D+2 partisan lean, *if it prevails in court challenge*."
  - "Faces a strong, Trump-endorsed challenger, *if Lincoln advances from the primary*."
  - "Has ballot access in all 50 states, *pending resolution of signature challenges in [State]*."

#### Non-Contenders: Limited Profile

For each non-contender, provide:

- Name, party, residence
- Ballot status
- Any prior runs for office (if applicable)
- Fundraising status (reported / not reported)
- A brief note stating: "No observable indicators of contender status as of [date]."

---

## Section III: Campaign Finance

### III.A Candidate Fundraising (2026 Cycle)

Table of fundraising data for all contenders, including:
- Total raised
- Cash on hand
- Total disbursements
- Burn rate (disbursements as % of receipts, or monthly average if calculable)
- Individual contributions vs. PAC contributions (if available in FEC data)
- Date of most recent filing

### III.B Outside Spending (Prior Cycle - Historical Context)

- **Completion Threshold:** This subsection is complete only if it includes at least one of the following:
  1. A populated historical outside spending table from the most recent comparable cycle, including: Group name, Type (Super PAC, party committee, etc.), Ideology/Side, Amount, Time Window, and Dominant Message Themes.
  2. An explicit absence statement: "No material outside spending was recorded in [cycle] per FEC/OpenSecrets data."
  3. An explicit uncertainty flag: "Historical outside spending data for [cycle] is not available through standard queries; manual review pending."

**NOT ACCEPTABLE:** Vague statements like "Significant outside spending occurred" without actual dollar figures. If spending occurred, quantify it. If you cannot quantify it, use the uncertainty flag.

- If historical data exists, include an **Attribution Summary** with:
  - Total spending by side (pro-Democratic, pro-Republican)
  - Net advantage (e.g., "Net Advantage: D+$2.3M")
  - **Dominant Message Themes** (e.g., "Republican spending focused on inflation and border security; Democratic spending focused on abortion and Social Security")

### III.C Outside Spending (Current Cycle)

State current cycle outside spending status:
- If spending has occurred, provide the same table format as historical.
- If no spending has occurred: "As of [date], no independent expenditures have been reported to the FEC for the [year] cycle."

---

## Section IV: Implications by Actor (Required)

This section outlines the structural implications of the current race dynamics for key actors, based on the factual research presented above. It does not contain strategic recommendations—only factual observations about how the race structure affects different participants.

**Required Subsections:**

- **For Campaigns:** What structural factors (partisan lean, fundraising disparities, primary field composition, turnout patterns) shape the environment each campaign operates in? What are the factual constraints and opportunities?

- **For Parties & Outside Groups:** What does the race structure suggest about likely party and outside group engagement? Which factors (competitiveness, cost, national implications) make this race a priority or non-priority for institutional investment?

- **For Voters & Civic Organizations:** What structural factors affect voter participation? (e.g., primary type, geographic size, registration deadlines, historical turnout patterns) What information gaps exist that civic organizations might address?

**Format:** 3-5 sentences per subsection. Stick to factual observations derived from the research; do not offer strategic advice.

---

## Section V: Open Questions (Required)

List 5-7 genuinely open factual or structural questions that remain unanswered and will be critical to monitor as the race develops. These should be questions that cannot be answered with current information but will materially affect the race dynamics.

**Good Open Questions:**
- "Will [Organization] endorse in the primary, and if so, which candidate?"
- "How will the new district boundaries affect turnout patterns in [County]?"
- "Will outside spending materialize at 2024 levels, or will national groups deprioritize this race?"
- "Can [Candidate] close the fundraising gap before the filing deadline?"

**Bad Open Questions (avoid):**
- Rhetorical questions ("Can anyone stop [Candidate]?")
- Questions already answered in the report
- Questions that are predictions in disguise ("Will [Candidate] win?")

---

## Section VI: Data Source Mapping

This section provides explicit guidance on where to find each type of data required for the research report. Use the **Primary Source (Gold Standard)** first; if unavailable, use the **Fallback Source**.

| Data Point | Primary Source (Gold Standard) | Fallback Source |
|------------|--------------------------------|-----------------|
| Campaign Finance | FEC.gov (Candidate/Committee Search) | OpenSecrets.org |
| Election Results | State Board of Elections (Official) | CNN / AP / Clerk of the House |
| Pres. Results by CD | Dave's Redistricting App (DRA) or Daily Kos Elections | The Downballot / Cook Political Report |
| Filing Deadlines | State Board of Elections / SOS | Ballotpedia |
| Redistricting Maps | Official State Legislature Site | Redistricting Data Hub / DRA |
| Demographics | Census Reporter (ACS 1-Year) | Census.gov |
| Voter Registration | State Board of Elections (Official Report) | L2 Data (via news reports) |
| Race Ratings | Cook Political Report (Official) | Inside Elections / Sabato |
| Primary/Runoff Dates | State Board of Elections (Official Calendar) | Ballotpedia / SOS Press Releases |
| Primary Type/Rules | NCSL (Statutory Citation) | State Party Bylaws / Ballotpedia |
| Outside Spending | FEC.gov (Independent Expenditures) | OpenSecrets.org |

### Search Heuristics

**Vintage Warning:**

When using map-based tools (like DRA or ArcGIS), explicitly verify that the dataset matches the 2026 district boundaries. Mismatched boundaries will produce incorrect partisan lean calculations.

**Institutional Power Search Operators:**

- **To find Ballot Rules:** `site:[state].gov "ballot placement" primary` OR `filetype:pdf "county committee" bylaws`
- **To find Machine Influence:** `"[District]" "endorsement" "kingmaker" -site:wikipedia.org`
- **To find Historical Machine Context:** `"[Region/County]" "political machine" OR "Democratic establishment" OR "political family"`

---

## Section VII: Explicit Exclusions

This research document must explicitly prohibit the following:

- **Predictions or Forecasts:** Do not predict election outcomes or future events.
- **Strategy Recommendations:** Do not provide strategic advice to campaigns, parties, or voters.
- **Strategic Advice for Candidates:** Do not outline what candidates should do to win.
- **"Path to Victory" Framing:** Do not outline scenarios for how a candidate could win.
- **Normative or Moral Judgments:** Do not make value judgments about candidates, policies, or voters.
- **Speculation on Future Outcomes:** Do not speculate about what might happen in the future.
- **Broken or Hallucinated URLs:** All URLs must be verified as functional before inclusion.
- **Vague Quantitative Statements:** Do not use phrases like "significant spending occurred" without actual figures.
- **Media Interpretation:** Do not include media coverage analysis. Media research is handled in a separate document.

All interpretation, strategy, and forecasting belong in downstream analysis documents, not in this research report.

---

## Section VIII: Version History (Required)

Record all versions, including initial creation (1.0). Change descriptions should be specific and auditable.

| Version | Date | Time (if same-day revision) | Changes |
|---------|------|------------------------------|---------|
| 1.0 | [Date] | | Initial report creation. |

---

## Consistency Flag (Quality Control)

If this report is part of a series covering multiple districts, verify that section structure, terminology, and formatting conventions match other reports in the series. Note any intentional deviations and justify.

---

## Version History

| Version | Date | Changes |
|:--------|:-----|:--------|
| 1.0 | 2026-01-21 | Initial District Fork version. Converted from legacy `U.S. House District Research Prompt v4.5`. Added naming convention integration, YAML headers, output format requirements. Removed Version Management section (versioning now handled per `district_naming_prompt.md`). All research sections unchanged from v4.5. |
