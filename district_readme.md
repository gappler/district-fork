# District Fork

**A modular system for political intelligence on U.S. House races.**

District Fork produces standardized research and analysis for campaign strategy. The system uses AI tools for research and discovery, with human editorial judgment controlling the narrative.

---

## Current Components

### Prompts

| Prompt | Status | Description |
|:-------|:-------|:------------|
| `district_opposition_prompt.md` | ✓ Ready | Vulnerability dossier on a candidate |
| `district_research_prompt.md` | Pending | District-level structural analysis |
| `district_affirmative_prompt.md` | ✓ Ready | Candidate performance record |
| `district_media_discovery_prompt.md` | ✓ Ready | Find relevant media coverage |
| `district_media_triage_prompt.md` | ✓ Ready | Index media without interpreting |
| `district_writing_prompt.md` | Pending | Draft the final article |

### Modules

| Module | Status | Description |
|:-------|:-------|:------------|
| `district_naming_prompt.md` | ✓ Ready | File naming, YAML headers, versioning |

---

## How to Run a Prompt

### Setup

1. **Attach the prompt file** (e.g., `district_opposition_prompt.md`)
2. **Attach the naming convention** (`district_naming_prompt.md`)
3. **Provide the required inputs** (see table below)
4. **Tell Manus what to do** (see example phrases)

### Quick Reference

| Prompt | Attach | Provide | Say |
|:-------|:-------|:--------|:----|
| Opposition Research | `district_opposition_prompt.md` + naming convention | District, candidate name | "Run opposition research on Henry Cuellar, TX-28" |
| Affirmative Research | `district_affirmative_prompt.md` + naming convention | District, candidate name | "Run affirmative research on Henry Cuellar, TX-28" |
| District Research | `district_research_prompt.md` + naming convention | District code | "Run district research on TX-28" |
| Media Discovery | `district_media_discovery_prompt.md` + naming convention | District, all candidate names, primary date | "Run media discovery for TX-28. Candidates: Cuellar, Tijerina. Primary: March 3, 2026" |
| Media Triage | `district_media_triage_prompt.md` + naming convention | District, attach media discovery output | "Triage the media for TX-28" |

---

## Output Naming

All outputs follow this pattern:

**Filename:** `[district]_[type]_[candidate].md`

**Example:** `TX-28_opposition_henry_cuellar.md`

**Critical:** The document's H1 header must match the filename (without `.md`). This is how Manus names the output file.

```markdown
# TX-28_opposition_henry_cuellar

---
district: TX-28
type: opposition
candidate: henry_cuellar
date: 2026-01-19
prompt: district_opposition_prompt.md
prompt_version: 1.1
---

[Content follows]
```

---

## Versioning

Versions are tracked **inside files**, not in filenames. GitHub commit history provides granular change tracking.

**Prompts and modules:**
- Patch (minor tweak): v1.0 → v1.0.1
- Minor (new capability): v1.0.1 → v1.1
- Major (restructure): v1.1 → v2.0

**Output re-runs:**
- First run: `TX-28_opposition_henry_cuellar.md`
- Second run: `TX-28_opposition_henry_cuellar_run2.md`

---

## Workflow

The full workflow for producing an article:

1. **District Research** — Structural foundation (run once per district)
2. **Opposition Research** — Vulnerabilities for each contender
3. **Affirmative Research** — Performance record for incumbents/key candidates
4. **Media Discovery** — Find relevant coverage
5. **Media Triage** — Index articles without interpreting
6. **Writer reads priority media** — Human editorial judgment
7. **Writing** — Draft with AI assistance, human controls narrative
8. **Citation pass** — Match claims to sources

---

## Tips and Gotchas

- **Always attach the naming convention** with every prompt
- **H1 must match filename** — Manus uses the H1 to name the output file
- **Check YAML header** — Ensure all fields are filled correctly
- **Re-runs get `_run2` suffix** — Don't overwrite previous outputs
- **Versions live inside files** — YAML header and version history table, not filename

---

## Future Development

Planned modules to extract from prompts:
- `module_grading_standards.md` — Severity/Confidence ratings (used in opposition, affirmative)
- `module_race_type_config.md` — House/Senate/Presidential configuration

---

*Version 1.1 | January 21, 2026*
