# district_briefing_prompt

---
version: 1.1
date: 2026-02-14
purpose: Generate race briefings for Early Returns — fact-dense analysis with editorial voice
tool: Claude (Opus 4.5 or equivalent)
companion: district-writing-prompt.md (narrative format, used selectively)
---

## Publication Identity

Early Returns is a political intelligence publication covering U.S. House primaries and competitive general elections. It exists to help readers understand what races reveal about American politics — and to sink Republicans by showing, not telling.

The briefing format is the publication's primary output: 2-3 per week, covering every race in the portfolio. The narrative format (district-writing-prompt.md) is reserved for races that warrant deeper treatment.

---

## What a Briefing Is

A briefing is a fact-dense race analysis with editorial voice concentrated in the opening and closing. The body is evidence. The bookends are insight.

**It is not:**
- A narrative piece with a hook-pivot-thesis
- A reference document or data dump
- A summary of the research files
- An opinion piece

**It is:**
- Everything a campaign staffer, donor, organizer, or journalist needs to understand a race
- Sourced to primary documents
- Publishable in an afternoon

---

## Inputs

All research must be complete before drafting:
- `{district}-baseline.md` — race metadata, candidates, ratings, fundraising, electoral history, demographics
- `{district}-media-research.md` — press coverage with verified facts and quotes
- `{district}-candidate-{name}.md` — candidate profiles (one per contender)
- `data/` folder — census CSV, FEC CSVs, IE data, DRA map screenshot
- `data/reference/` — Kondik crossover CSV, Downballot presidential CSV

**Do not draft until all research is indexed and accessible.**

---

## Citation Method: Cite as You Go

Every factual claim carries its source inline during drafting. This is the critical difference from the narrative prompt, where citation happened at Stage 5.

**Working draft format:**
> Cook PVI: R+3 [baseline, Section 8]. Trump carried the new lines by 10 points — 54.6% to 44.5% [kondik]. All three forecasters rate Toss-up [baseline, Section 8].

**Source key (define at top of working draft):**
- `[baseline]` = {district}-baseline.md + section number
- `[kondik]` = kondik-crossover-presidential-2026-lines.csv
- `[downballot]` = downballot-presidential.csv
- `[census]` = census-district-{number}.csv
- `[{candidate}]` = candidate profile + section number
- `[media, Art. N]` = media research, article number
- `[FEC]` = FEC filing with committee ID and period
- `[DRA]` = Dave's Redistricting App map

**Rules:**
- Verify that the source says the specific thing being cited before writing the sentence
- If two sources disagree, use the primary source (FEC over news article, Kondik CSV over baseline's derived calculation)
- If citing polling data, verify against the actual toplines — not summaries, memos, or secondary reporting. Regional breakdowns (e.g., Arizona) are not interchangeable with national figures.
- Flag unverifiable claims with [VERIFY]
- Flag high-risk claims with [LEGAL REVIEW]

**Two outputs:**
1. Working draft with inline citations (your file, not published)
2. Clean draft with no citations (Substack)

---

## Structure

### 1. The Opening Paragraph (Required)

One paragraph that frames the race. This is the editorial value — what the facts mean, what's structurally happening, what to watch. It should cover:

- **Structure:** What created this race (redistricting, retirement, scandal, realignment)
- **Dynamics:** What forces are in play (primary contests, endorsement patterns, voter shifts, money flows)
- **What to watch:** The question the race answers

This paragraph is voice-forward. It's the thing that makes someone open the email. Every sentence after it is evidence for or against what this paragraph claims.

No hook-pivot-thesis. No literary scaffolding. Just the sharpest framing you can write in one paragraph.

### 2. The District

Geography, demographics, key stats. One paragraph.

Then: partisan lean (Cook PVI), presidential performance on new and old lines if redistricted, redistricting shift, forecaster ratings with date. Cook PVI is the district rating — do not conflate it with Trump's margin, which is one election result.

Then (if it earns its own line): the sentence that makes the structural math concrete. "Gonzalez won by 2.6 points in 2024. On the old lines."

### 3. The Money

Open with timestamp: "FEC data pulled [date]."

Incumbent first: cash on hand, total raised, fundraising geography, industry capture if flagged.

Then challengers in order of viability. Include: raised, cash remaining, self-funding if significant, outstanding debt if it exceeds cash on hand.

Then outside spending (prior cycle and current if available). Name the top spenders and amounts.

**What not to include:** Burn rates. The reader can see raised vs. remaining and do the math. Every number should earn its place by telling the reader something they wouldn't know otherwise. Cash on hand says who can compete. Source of money says who they serve. Debt says who's leveraged.

### 4. The Primary (if applicable)

Endorsements, dropouts, straw polls, attacks that landed. Date the straw poll or forum. Name the institutional backers.

### 5. Candidate Sections

For each contender (2-3 paragraphs each):
- Background (brief, relevant)
- One or two sentences of qualitative identity — who they are as a candidate, not just what they've done
- Key vulnerabilities with severity — let the facts speak
- Prior attack history — what landed, what misfired

For the incumbent, include: voting record highlights, committee positions, coalition memberships, endorsement list.

### 6. Special Sections (as warranted)

Use bold headers for findings that deserve emphasis:
- **Residency.** (if candidates live outside the district)
- **Disclosure.** (if financial conflicts are documented)
- **Legal.** (if litigation or ethics issues are active)

These sections exist because the finding is notable. Don't create them for routine information.

### 7. The Math / What to Watch (Required)

The closing. Returns to the opening paragraph's questions and answers them — or sharpens them — with the evidence now presented. This is the second place where voice comes through.

Should include:
- What the primary determines
- What structural forces favor which outcome
- The unresolved question

One paragraph. End on the line that sticks.

---

## Timestamps

- **FEC data:** "FEC data pulled [date]" — once, at the top of the money section. Use the date you pulled the data, not the filing period, since candidates file on different schedules.
- **Ratings:** "as of [date]" — once, when ratings are first mentioned.
- **Census/presidential data:** No timestamp needed (stable data).

---

## Editorial Guardrails

Same as district-writing-prompt.md. The evidence hierarchy, donation guardrails, voting record guardrails, and association guardrails all apply.

The briefing format's density makes errors harder to catch and easier to trust. The inline citation method exists specifically to counter this risk.

---

## Voice

The briefing voice is the narrative voice compressed. Dry, precise, confident. The difference is restraint: one observation at the top, one at the bottom, facts in between.

- No digs in the candidate sections. Let the numbers and the record do the work.
- No more than two sentences of editorial voice per section (opening and closing excepted).
- Trust the reader.

---

## Length and Format

- **Target length:** 1,200-1,800 words (clean version without citations)
- **Section headers:** Bold, descriptive ("The money." "The GOP primary." "Residency.")
- **No bullet points** in the body
- **No numbered lists** in the body
- **Primary date:** In the subhead and in the closing
- **General date:** In the subhead

---

## QA Checklist

### Before drafting
- [ ] All research files indexed and accessible via MCP
- [ ] DRA map screenshot in project data folder (redistricted states)
- [ ] Baseline QA complete (counties match map, ratings verified, FEC totals checked)

### During drafting
- [ ] Every factual claim has an inline source citation
- [ ] Source actually says the specific thing being cited
- [ ] Cook PVI is not conflated with Trump's margin
- [ ] FEC timestamp stated once in money section
- [ ] Ratings timestamp stated once
- [ ] Candidate names match public usage (not just FEC legal names)
- [ ] If redistricted: old lines vs. new lines clearly distinguished throughout
- [ ] Polling claims verified against actual toplines, not summaries or memos

### Before publishing
- [ ] NotebookLM or equivalent fact-check pass on working draft with source URLs
- [ ] Any flagged discrepancies resolved
- [ ] Clean version stripped of all citation brackets
- [ ] Opening paragraph frames structure, dynamics, and what to watch
- [ ] Closing paragraph returns to opening question
- [ ] Em dashes consistent (no spaces)
- [ ] Fresh read for rhythm and clarity
- [ ] Overnight review before publishing

---

## Version History

| Version | Date | Changes |
|:--------|:-----|:--------|
| 1.0 | 2026-02-13 | Initial version. Developed from TX-34 briefing process. Key innovation: inline citation during drafting (not post-draft audit). |
| 1.1 | 2026-02-14 | Removed burn rates from Money section. Added qualitative identity line to candidate sections. Added polling topline verification rule. Added em dash consistency and overnight review to QA. Renamed closing section "The Math / What to Watch." |
