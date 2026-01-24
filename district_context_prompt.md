# District Context Prompt

**Version:** 1.0
**Purpose:** To describe the demographic, economic, and political character of a congressional district.

---

## Input Required

- District identifier (e.g., TX-28)
- Baseline file: `[district]_baseline.md`

---

## Task

Provide factual context about the district's composition and character. This is background for understanding the political environment—not analysis of the current race.

---

## Output Format

### Output File
`[district]_context.md`

### Structure

```
# [DISTRICT] Context

## Demographics

| Metric | Value | Source |
|--------|-------|--------|
| Population | | Census/ACS |
| Latino/Hispanic % | | Census/ACS |
| White (non-Hispanic) % | | Census/ACS |
| Black % | | Census/ACS |
| Asian % | | Census/ACS |
| Median household income | | Census/ACS |
| Urban/Suburban/Rural split | | Census |
| College educated % | | Census/ACS |

## Geography

[2-3 sentences describing the physical district: border region, major cities, rural areas, geographic features, etc.]

## Economic Drivers

| Industry | Notes |
|----------|-------|
| | |

[1-2 paragraphs on the major employers, economic issues, and how the economy shapes political concerns]

## Political Character

[2-3 paragraphs on:]
- Historical voting patterns (without repeating electoral history data)
- Political machines or institutional forces
- Notable political families or dynasties
- Primary vs. general election dynamics
- Any relevant local political culture (patronage systems, border politics, union influence, etc.)

## Key Institutions

| Institution | Type | Relevance |
|-------------|------|-----------|
| | Employer/Union/Media/Political org | |

[Major employers, unions, political organizations, media outlets that shape district politics]
```

---

## Data Source Hierarchy

1. **U.S. Census Bureau / American Community Survey** — Demographics
2. **Bureau of Labor Statistics** — Economic data
3. **Local/regional news outlets** — Political culture context
4. **Academic sources** — For machine politics, historical patterns

---

## Do NOT Include

- Current race predictions or analysis
- Candidate information (covered in separate oppo/affirmative prompts)
- Fundraising data
- Endorsements for current cycle
- Redistricting analysis (covered in baseline)
- Your interpretation of what this means for the race

---

## Output Quality Check

Before finalizing, verify:
- [ ] Demographic data sourced to Census/ACS
- [ ] Economic claims sourced
- [ ] Political character section describes patterns, not current race
- [ ] No predictions or editorializing
- [ ] Key institutions identified with relevance explained
