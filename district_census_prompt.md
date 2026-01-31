# district_census_prompt

**Version:** 1.0  
**Date:** January 31, 2026  
**Purpose:** Convert Census.gov "My Congressional District" CSV export to formatted Markdown report

---

## Naming Convention

**REQUIRED:** Before generating output, load and apply all conventions from `district_naming_prompt.md`. This file governs output filenames, H1 headers, and YAML metadata blocks.

Output filename pattern: `[district]_census.md`

Example: `WA-03_census.md`

**CRITICAL: Document H1 header must match the filename (without `.md`):**
Example: `# WA-03_census`

**YAML metadata block (immediately after H1):**
```yaml
---
district: [district code]
type: census
date: [YYYY-MM-DD]
prompt: district_census_prompt.md
prompt_version: 1.0
source: Census.gov My Congressional District
survey_year: [year from CSV source line, e.g., 2024]
---
```

---

## Input Required

- **CSV file:** Downloaded from Census.gov "My Congressional District" tool
  - URL pattern: `https://www.census.gov/mycd/?st=[STATE_FIPS]&cd=[DISTRICT_NUMBER]`
  - Download via the export/download option on the page

---

## Task

1. Parse the provided CSV file
2. Organize data by Topic (People, Workers, Housing, Socioeconomic, Education, Business)
3. Group related Subject areas within each Topic
4. Format values with margins of error where provided
5. Output as structured Markdown report

---

## Output Structure

Organize the report following the Topic hierarchy in the CSV:

### Topics (in order)
1. **People** — Demographics, race, ethnicity, ancestry, veterans, disability, mobility
2. **Workers** — Employment, commuting, occupation, industry
3. **Housing** — Occupancy, tenure, value, costs, rent
4. **Socioeconomic** — Income, health insurance, poverty
5. **Education** — School enrollment, educational attainment
6. **Business** — Employees, payroll, establishments by industry

### Within Each Topic
- Group by Subject (e.g., "Sex and Age", "Race", "Hispanic or Latino and Race")
- Use Subject as H3 subheading
- List data items with values and margins of error

---

## Formatting Rules

### Values
- Report numeric values as shown in CSV
- Include margin of error in parentheses: `802,855 (+/-4,128)`
- For percentages, include MOE: `5.1% (+/-0.7)`
- For medians, label clearly: `Median: $92,354 (+/-2,802)`

### Key Metrics
Highlight these summary statistics at the top of each Topic section:
- **People:** Total population, Median age
- **Workers:** Labor force participation, Unemployment rate
- **Housing:** Total units, Median value, Median rent
- **Socioeconomic:** Median household income, Poverty rate
- **Education:** % High school graduate, % Bachelor's or higher
- **Business:** Total establishments, Total employees

### Tables
Use tables for distribution data (age ranges, income brackets, industry breakdowns).

---

## Output Format

```markdown
# [DISTRICT]_census

---
district: [district code]
type: census
date: [YYYY-MM-DD]
prompt: district_census_prompt.md
prompt_version: 1.0
source: Census.gov My Congressional District
survey_year: [year]
---

## Overview

**Total Population:** [value] (+/-MOE)  
**Median Age:** [value] (+/-MOE)  
**Median Household Income:** [value] (+/-MOE)  
**Unemployment Rate:** [value]% (+/-MOE)

---

## People

### Sex and Age

[Data organized by subject]

### Race

[Data organized by subject]

[Continue for all subjects under People]

---

## Workers

[Continue pattern for each Topic]

---

## Citation

Source: U.S. Census Bureau, [YEAR] American Community Survey 1-Year Estimates  
Retrieved from: Census.gov My Congressional District  
URL: https://www.census.gov/mycd/?st=[FIPS]&cd=[DISTRICT]
```

---

## Do NOT Include

- Interpretation or analysis of the data
- Comparisons to state or national averages (unless adding a comparison column)
- Predictions or implications
- Data not present in the CSV

---

## Quality Standards

Before finalizing, verify:
- [ ] All Topics from CSV are included
- [ ] All Subjects within each Topic are included
- [ ] Values match CSV exactly
- [ ] Margins of error are included where provided
- [ ] Key metrics are highlighted at top of each section
- [ ] Source year is correctly identified from CSV footer

---

## Version History

| Version | Date | Changes |
|:--------|:-----|:--------|
| 1.0 | 2026-01-31 | Initial version. Converts Census.gov MyCD CSV to Markdown. |
