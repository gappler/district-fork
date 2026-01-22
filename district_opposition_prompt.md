# district_opposition_prompt

**Version:** 1.1
**Date:** January 21, 2026
**Purpose:** To generate a strictly forensic **Vulnerability Dossier** on a specific federal candidate (U.S. House, U.S. Senate, or Presidential). This report identifies specific structural weaknesses, contradictions, and liabilities.
**Primary Deliverable:** The **Vulnerability Summary Matrix** (Section VI) is the primary product. All prior sections exist to populate and justify that matrix.
**Audience:** Senior "Red Team" Strategists and Campaign Managers.

---

## Naming Convention

Follow the conventions in the attached `district_naming_prompt.md` file for output filename and header.

**Output filename:** `[district]_opposition_[candidate].md`
Example: `TX-28_opposition_henry_cuellar.md`

**CRITICAL: Document H1 header must match the filename (without `.md`):**
Example: `# TX-28_opposition_henry_cuellar`

**YAML metadata block (immediately after H1):**
```yaml
---
district: [district code]
type: opposition
candidate: [first_last]
date: [YYYY-MM-DD]
prompt: district_opposition_prompt.md
prompt_version: 1.1
---
```

---

## Race Type Configuration (Required)

Select the race type and complete the configuration fields before beginning research.

**Race Type:** [ ] U.S. House | [ ] U.S. Senate | [ ] Presidential

| Field | U.S. House | U.S. Senate | Presidential |
| :--- | :--- | :--- | :--- |
| **Geographic Unit** | District | State | National |
| **Truancy Benchmark** | House median (~2.1%) | Senate median (~2.8%) | Record in prior legislative office (if applicable) |
| **Fundraising Geography** | In-District vs. Out-of-District | In-State vs. Out-of-State | Small-Dollar vs. Large-Dollar; Grassroots concentration |
| **Constituent Services** | District office responsiveness | State office responsiveness (multiple locations) | Record in prior executive/legislative office |
| **Committee Relevance** | House committee assignments | Senate committee assignments | Prior committee assignments or executive agency oversight |

**Candidate Information:**
- **Candidate Name:** _______________
- **Party:** _______________
- **State/District:** _______________
- **Incumbent/Challenger/Open Seat:** _______________
- **Prior Office Held (if any):** _______________

---

## Grading Standards (Required for All Findings)

Every finding in this report must be assigned two ratings. Do not include findings that cannot be graded.

**1. Severity Rating**
* **CRITICAL:** A career-ending vulnerability (e.g., criminal conviction, documented corruption, fatal hypocrisy on core base issue, staff criminal charges).
* **HIGH:** A major narrative liability that dominates a news cycle (e.g., industry capture >50%, missed votes >10%, contradictory video, staff lawsuit, severely detached fundraising).
* **MEDIUM:** A useful hit for mailers or digital ads (e.g., out-of-state funding, flip-flop with weak explanation, constituent complaints pattern).
* **LOW:** Background noise or "nuance" (e.g., ancient tweets, minor technical fines, isolated incidents).

**2. Confidence Rating**
* **HIGH:** Primary source document (Court filing, FEC report, C-SPAN video, official government record).
* **MEDIUM:** Corroborated by at least two reputable news outlets.
* **LOW:** Single source (verified) or archived social media without context.

---

## Section I: The Hypocrisy Audit (Policy & Record)

**Goal:** Identify contradictions between current branding and past actions.

### I.A The "Flip-Flop" Check (Nuance Required)

* Compare the candidate's *current* platform to public statements from >4 years ago.
* **Constraint:** Distinguish *evolution* from *contradiction*.
    * If the candidate publicly explained the shift at the time, include the explanation verbatim in the "Known Defense" field.
    * If no explanation exists, flag as **Unexplained Reversal**.
* *Tools:* Internet Archive (Wayback Machine), Google Advanced Search, C-SPAN Video Library.

### I.B The Party Loyalty Check

* Has the candidate switched parties or endorsed the opposition?
* **Instruction:** Log specific dates and the target of the endorsement.
* **Note:** A party switch can cut both ways—flag but assess whether it reinforces or undermines candidate's current narrative.

### I.C The Truancy Record (Incumbents/Former Legislators Only)

* Compare lifetime missed votes to the chamber median.
* **Thresholds:**

| Chamber | Median | >5% Severity | >10% Severity |
| :--- | :--- | :--- | :--- |
| U.S. House | ~2.1% | MEDIUM | HIGH |
| U.S. Senate | ~2.8% | MEDIUM | HIGH |

* **Presidential Note:** If candidate is a current or former legislator, apply the relevant chamber benchmark. If candidate has no legislative record, mark N/A.
* *Source:* GovTrack.us, Congress.gov

### I.D The "Voted Against Your Constituents" Check
* Identify 3-5 votes or positions that directly harmed constituents in the relevant geographic unit.

| Race Type | Geographic Unit | Focus Areas |
| :--- | :--- | :--- |
| U.S. House | District | District-specific industries, military bases, hospitals, infrastructure |
| U.S. Senate | State | Statewide industries, federal installations, state funding, disaster relief |
| Presidential | National / Home State | National policy impact; also examine home state record if applicable |

* **Instruction:** Cross-reference candidate's committee assignments and voting record with economic profile:
    * Major industries (agriculture, manufacturing, energy, healthcare, tech)
    * Military bases or defense employers
    * Healthcare facilities (rural hospitals, VA centers)
    * Infrastructure needs (ports, highways, broadband, water)
    * Disaster relief votes (if applicable to region)
* **Example (House):** "Voted against farm bill provision that would have benefited [X] agricultural workers in [District]."
* **Example (Senate):** "Voted against disaster relief funding after [State] hurricane."
* **Example (Presidential):** "As Senator, voted against auto industry bailout that saved [X] jobs in Michigan."
* *Severity:* **HIGH** if vote directly cost jobs/funding; **MEDIUM** if indirect impact.
* *Source:* Congress.gov (voting record), Census Bureau, BLS, state/district economic data

---

## Section II: The Financial Audit (Money vs. Brand)

**Goal:** Identify structural capture and donor conflicts.

### II.A Cycle Currency Requirement

* **All campaign finance analysis must include BOTH:**
    1. The most recent completed cycle, AND
    2. The current cycle (if Q3+ data is available)
* **Instruction:** If current cycle data shows a significant shift from prior patterns (e.g., in-district/in-state percentage improved or worsened by >10 points), flag explicitly.
* **Constraint:** Do not rely solely on prior cycle data if current cycle filings are available.

### II.B The "Industry Capture" Test

* Compare the candidate's Committee Assignments (or executive agency oversight, for Presidential) to their Top 5 Donor Industries.
* **Instruction:** Flag if **>25%** of donations come from industries directly under the candidate's legislative/executive jurisdiction.
* *Severity:* **HIGH** if >25%; **CRITICAL** if >50%.
* *Source:* OpenSecrets.org, FEC.gov

### II.C The "Carpetbagger" Tiers

* Calculate fundraising by geographic origin.

| Race Type | Metric | Severely Detached (HIGH) | Structurally Detached (MED) | Weak Local Base (LOW) |
| :--- | :--- | :--- | :--- | :--- |
| U.S. House | In-District % | <10% | 10–20% | 20–35% |
| U.S. Senate | In-State % | <15% | 15–30% | 30–45% |
| Presidential | Small-Dollar % | <10% | 10–25% | 25–40% |

* **Presidential Note:** For Presidential races, the "Carpetbagger" metric shifts to small-dollar vs. large-dollar fundraising and grassroots geographic concentration. A candidate heavily reliant on large-dollar coastal donors in a populist primary faces a structural vulnerability.
* *Source:* OpenSecrets.org (Geographic breakdown), FEC.gov

### II.D The "Burn Rate" Warning

* Flag if Burn Rate >120% or COH below threshold.
* *Source:* FEC.gov

### II.E Self-Funding Analysis

* Flag if candidate has self-funded >40% of campaign while claiming grassroots support.
* *Severity:* **MEDIUM** if >40%; **HIGH** if >60% while claiming grassroots.

### II.F Data Reconciliation Requirement

* **Instruction:** If financial data from different sources (e.g., OpenSecrets vs. FEC) shows discrepancies >5%, note both figures and explain the likely source of the discrepancy (timing, methodology, etc.).

---

## Section III: The Digital Conduct Audit

**Goal:** Identify statements or behavior that contradict current positioning.

### III.A The Deleted Tweet Audit

* Search for deleted tweets via ProPublica Politwoops or Internet Archive.
* **Instruction:** Flag only tweets that contradict current positioning or reveal conduct the candidate has disavowed.
* *Severity:* **HIGH** if tweet contradicts core campaign message; **MEDIUM** if merely embarrassing.

### III.B The "Hot Mic" / Gaffe Audit

* Search for video of unguarded moments or gaffes.
* **Threshold:** Only include if the gaffe was covered by at least one major outlet OR if the video itself is highly damaging and undercovered.
* *Source:* C-SPAN, YouTube, news archives.

### III.C Conspiracy & Extremism Documentation

* Document any instances of the candidate promoting conspiracy theories or associating with extremist movements.
* **Instruction:** Include specific quotes, dates, and context. Flag whether the candidate has since disavowed.
* *Severity:* **CRITICAL** if ongoing; **HIGH** if disavowed but documented.

### III.D Praise for Disgraced Figures

* Flag any documented instances of the candidate publicly praising individuals who were later disgraced (convicted, resigned in scandal, etc.).
* **Instruction:** Include the date of the praise and the date of the disgrace. Assess whether the candidate has since distanced themselves.
* *Severity:* **HIGH** if praise was effusive and no distancing has occurred; **MEDIUM** if distancing is documented.

---

## Section IV: The Personal Conduct Audit

**Goal:** Identify personal conduct issues that create political liability.

### IV.A Financial Disclosure Conflicts

* Review candidate's personal financial disclosures for conflicts of interest.
* **Instruction:** Flag any assets or income sources that conflict with committee assignments or policy positions.
* *Source:* Clerk of the House, Secretary of the Senate, OGE (Presidential)

### IV.B Family Financial Conflicts

* Flag any immediate family members with financial interests that conflict with the candidate's official duties.
* **Instruction:** Include only if documented in financial disclosures or credible reporting.
* *Severity:* **HIGH** if family member has lobbied or contracted with entities under candidate's jurisdiction.

### IV.C Staff & Associates Audit

#### IV.C.1 Staff Scandal Check

* Flag any:
    * Resignations under controversy
    * Lawsuits or criminal charges (before or after hire)
    * Documented complaints (HR, legal, media)

#### IV.C.2 The "Revolving Door" Check

* Flag if senior staff have recently lobbied for industries under the candidate's committee jurisdiction.
* *Source:* OpenSecrets.org (Lobbying Revolving Door)

### IV.D Constituent Services Record

* Review local news archives, Google/Yelp reviews for district/state offices, and social media for patterns of constituent complaints.
* **Instruction:** Flag documented patterns of non-responsiveness, case mismanagement, or poor service.
* *Severity:* **MEDIUM** if a clear pattern is documented by local media.

### IV.E Campaigning Violations

* Flag any documented instances of:
    * Improper use of official resources for campaign purposes (franking violations, etc.)
    * Campaigning in churches or other non-political venues in a manner that violates their tax-exempt status.
* *Source:* FEC complaints, news reports, watchdog groups.

---

## Section V: Prior Attack Efficacy

**Goal:** Determine which attacks have been tried and whether they landed.

### V.A Prior Cycle Attack Inventory

* Document attacks used against the candidate in prior cycles (primary and general).
* **Instruction:** Review TV ads, mailers, and debate transcripts from previous campaigns.
* *Source:* Political TV Ad Archive, local news coverage, debate recordings.

### V.B Efficacy Assessment

* For each prior attack, assess its efficacy:
    * **Landed:** Attack was widely covered and forced a response from the candidate.
    * **Misfire:** Attack was ignored, easily rebutted, or backfired.
    * **Underexploited:** Attack was used in a limited fashion (e.g., one mailer) but has potential.

### V.C Surrogate & Endorser Liability (Presidential Only)

* Identify 3-5 of the candidate's most prominent public surrogates or endorsers.
* **Instruction:** Conduct a mini-vulnerability check on each surrogate, flagging any major liabilities (criminal records, extreme statements, business scandals) that could create a damaging "friends of" narrative.
* *Severity:* **HIGH** if surrogate is a household name with a major scandal.

---

## Section VI: Vulnerability Summary Matrix

**Goal:** To provide a single, at-a-glance summary of the candidate's most significant liabilities, sorted by strategic importance.

**CRITICAL INSTRUCTION: Matrix Completeness Check**
* The Summary Matrix **MUST** include all findings rated **HIGH** or **CRITICAL** severity from Sections I-V. Before finalizing, cross-reference each section to ensure no HIGH/CRITICAL findings are omitted.

**Instruction:** Sort table first by **Severity** (Critical to Low), then by **Confidence** (High to Low).

| Severity | Confidence | Vulnerability | Attack Vector Example | Known Defense | Source(s) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **CRITICAL** | **HIGH** | *Staff Scandal* | *"Her District Director resigned after a $1M sexual assault lawsuit."* | *"He resigned; we took swift action."* | *[Source]* |
| **CRITICAL** | **HIGH** | *Industry Capture* | *"Takes 60% of cash from industry he regulates."* | *"I support the industry."* | *[OpenSecrets]* |
| **HIGH** | **HIGH** | *Carpetbagger* | *"Only 4% of her money comes from the district."* | *"I have national support."* | *[FEC/OpenSecrets]* |
| **HIGH** | **HIGH** | *Extremism* | *"Spread QAnon conspiracies and called Jan 6 an Antifa attack."* | *"Old posts, I've moved on."* | *[CNN]* |
| **HIGH** | **HIGH** | *Voted Against Constituents* | *"Voted against lowering prescription drug costs."* | *"That bill was wasteful."* | *[Congress.gov]* |
| **MEDIUM** | **HIGH** | *FEC Violation* | *"Paid herself $15K illegally."* | *"Administrative error."* | *[FEC]* |
| **MEDIUM** | **MED** | *Dishonesty* | *"Posted fake photos pretending she cooked the food."* | *"Silly mistake."* | *[News report]* |
| **LOW** | **HIGH** | *Attendance* | *"Missed 4% of votes."* | *"Family illness."* | *[GovTrack]* |

---

## Section VII: Data Source Mapping

**Goal:** To provide a clear map of preferred data sources for each category of research.

**CRITICAL INSTRUCTION: Citation Completeness**
* All citations in the final report must be complete. Incomplete citations are not acceptable.
* **Required Format:** Publication/Agency, "Article Title," Date, URL.

| Data Point | Primary Source (Gold Standard) | Fallback Source |
| :--- | :--- | :--- |
| **Missed Votes** | GovTrack.us | Congress.gov |
| **Voting Record** | Congress.gov | VoteSmart.org |
| **Donor Industries** | OpenSecrets.org | FEC.gov |
| **Geographic Donor Breakdown** | OpenSecrets.org | FEC.gov (itemized contributions) |
| **FEC Violations** | FEC.gov (Enforcement Query System) | News reports |
| **Deleted Tweets** | ProPublica Politwoops | Internet Archive |
| **House Ethics Reports** | Office of Congressional Ethics (OCE) | News reports |
| **Senate Ethics Reports** | Senate Select Committee on Ethics | News reports |
| **Executive Branch Ethics** | Office of Government Ethics (OGE) | News reports |
| **Staff/Associate Issues** | Court records (PACER, state courts) | Local news archives, ProPublica |
| **Constituent Complaints** | Local news archives | Social media searches, Google/Yelp reviews |
| **Prior Attack Efficacy** | Political TV Ad Archive | News coverage of prior races, Factbase |
| **Financial Disclosures (House)** | Clerk of the House | OpenSecrets |
| **Financial Disclosures (Senate)** | Secretary of the Senate | OpenSecrets |
| **Financial Disclosures (Presidential)** | FEC, OGE | OpenSecrets |
| **District/State Economic Profile** | Census Bureau, BLS | Local economic development reports |

---

## Section VIII: Explicit Exclusions
* **No Rumor Mill:** Exclude unverified allegations unless the *allegation itself* has generated significant media coverage (The "Scandal" vs. The "Fact").
* **No Policy Analysis:** Do not explain the *merit* of the vote. Report the political liability.
* **No Strategy:** Do not advise *how* to use this info. Just provide the ammunition.
* **No Guilt-by-Association:** Do not flag casual contact, shared event attendance, or photographs without active promotion by the candidate.
* **No Stale Data:** Do not rely solely on prior cycle data if current cycle data is available.

---

## Section IX: Version History
| Version | Date | Changes |
| :--- | :--- | :--- |
| 1.0 | 2026-01-19 | Renamed to District Fork Opposition Prompt. Added Naming Convention section with output filename and YAML header requirements. Content carried forward from Federal Candidate Opposition Research Prompt v1.4. |
| 1.1 | 2026-01-21 | Updated naming convention references. Removed versions from filenames per `district_naming_prompt.md` v1.1. |

---

## Appendix: Quick Reference Checklist
Before submitting the dossier, verify:
- [ ] Output filename follows naming convention
- [ ] YAML header included at top of output
- [ ] Race Type Configuration completed at top of document
- [ ] All findings have Severity AND Confidence ratings
- [ ] Current cycle FEC data included if available
- [ ] Financial data discrepancies are noted and explained (II.F)
- [ ] Constituent impact analysis uses correct geographic unit (district/state/national)
- [ ] Fundraising geography uses correct benchmark for race type
- [ ] Truancy benchmark matches correct chamber
- [ ] Staff and associates checked for controversies
- [ ] Deleted social media searched via Politwoops/Archive
- [ ] Prior cycle attacks documented with efficacy assessment
- [ ] Surrogate liability checked (Presidential only)
- [ ] Vulnerability Summary Matrix is complete (includes all HIGH/CRITICAL findings)
- [ ] All citations are complete (Publication, Title, Date, URL)
- [ ] No strategy recommendations included
- [ ] No unverified rumors included
