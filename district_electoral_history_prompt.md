# District Electoral History Prompt

**Version:** 1.0
**Purpose:** To retrieve factual electoral history for a congressional district.

---

## Input Required

- District identifier (e.g., TX-28)
- Baseline file: `[district]_baseline.md`

---

## Task

Retrieve electoral results for this district for the **past 5 election cycles** (10 years), covering both primary and general elections for the U.S. House seat.

---

## Output Format

### Output File
`[district]_electoral_history.md`

### Structure

For each election cycle, provide:

```
## [YEAR] Election

### Primary ([Party])
| Candidate | Votes | Percentage |
|-----------|-------|------------|

Winner: [Name] | Margin: [X points]

### General
| Candidate | Party | Votes | Percentage |
|-----------|-------|-------|------------|

Winner: [Name] | Margin: [X points]
Turnout: [X]

Presidential result in district (if presidential year): [Candidate] +[X]
```

---

## Data Source Hierarchy

Consult these sources in order of authority:

1. **State Secretary of State** — Official election results (primary source)
2. **Ballotpedia** — Verified election data
3. **Dave's Redistricting App** — For boundary/map context only

If sources conflict, use State SOS data and note the discrepancy.

---

## Do NOT Include

- Interpretation of trends or momentum
- Predictions about current cycle
- Candidate biographies or backgrounds
- Fundraising information
- Endorsements

---

## Redistricting Note

If district boundaries changed during the 10-year period, note which cycles used which maps. Do not attempt to "translate" results across different district configurations—just note the boundary change.

---

## Output Quality Check

Before finalizing, verify:
- [ ] All data sourced to State SOS or Ballotpedia
- [ ] Margins calculated correctly
- [ ] Redistricting boundary changes noted
- [ ] No interpretation or editorializing
