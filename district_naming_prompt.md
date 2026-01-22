# District Fork Naming Convention

Standard naming for all prompts and outputs in District Fork. Attach this file to prompts or load into project files.

---

## Prompt File Naming

**Pattern:** `district_[function]_prompt.md`

| Prompt | Filename |
|:---|:---|
| District Research | `district_research_prompt.md` |
| Opposition Research | `district_opposition_prompt.md` |
| Affirmative Research | `district_affirmative_prompt.md` |
| Media Discovery | `district_media_discovery_prompt.md` |
| Media Triage | `district_media_triage_prompt.md` |
| Writing | `district_writing_prompt.md` |
| Naming Convention | `district_naming_prompt.md` |

---

## Output File Naming

**Pattern:** `[district]_[type]_[candidate if applicable].md`

| Output Type | Code | Example |
|:---|:---|:---|
| District Research | `overview` | `TX-28_overview.md` |
| Opposition Research | `opposition` | `TX-28_opposition_henry_cuellar.md` |
| Affirmative Research | `affirmative` | `TX-28_affirmative_henry_cuellar.md` |
| Media Discovery | `media_discovery` | `TX-28_media_discovery.md` |
| Media Triage | `media_triage` | `TX-28_media_triage.md` |

**Candidate names:** lowercase, underscore between first and last: `henry_cuellar`

---

## Output Header

**CRITICAL:** The document's first heading (H1) must match the output filename (without the `.md` extension). This ensures consistent file naming when the document is saved.

**Example H1:** `# TX-28_opposition_henry_cuellar`

Include YAML metadata block immediately after the H1:

```yaml
---
district: TX-28
type: opposition
candidate: henry_cuellar
date: 2026-01-19
prompt: district_opposition_prompt.md
prompt_version: 1.0
---
```

| Field | Required | Notes |
|:---|:---|:---|
| district | Yes | Standard code (TX-28, NC-01) |
| type | Yes | overview, opposition, affirmative, media_discovery, media_triage |
| candidate | If applicable | For opposition/affirmative only |
| date | Yes | YYYY-MM-DD |
| prompt | Yes | Filename of prompt that created this |
| prompt_version | Yes | Current version of prompt (from prompt's YAML or version table) |

---

## Version Tracking

Versions are tracked **inside files**, not in filenames. GitHub commit history provides granular change tracking.

### Version Scheme

| Change Type | Example | When to Use |
|:---|:---|:---|
| Major | v1.0 → v2.0 | Significant restructure |
| Minor | v1.0 → v1.1 | New section or capability |
| Patch | v1.0 → v1.0.1 | Minor tweak or fix |

### Where Versions Live

**Prompts:** YAML header at top + version history table at bottom

**Outputs:** YAML header includes `prompt_version` field reflecting the prompt version used

### Multiple Runs

If you rerun the same prompt on the same district/candidate, append a date or run number:

- `TX-28_opposition_henry_cuellar.md` (first run)
- `TX-28_opposition_henry_cuellar_2026-01-21.md` (rerun on different date)
- `TX-28_opposition_henry_cuellar_run2.md` (second run same day)

---

## Integration

Add this line to each prompt:

> **Naming:** Follow the conventions in the attached `district_naming_prompt.md` file.

---

## Quick Reference

```
PROMPTS:  district_[function]_prompt.md
OUTPUTS:  [district]_[type]_[candidate].md

TYPES:    overview, opposition, affirmative, media_discovery, media_triage
NAMES:    first_last (lowercase, underscore)
HEADER:   YAML with district, type, candidate, date, prompt, prompt_version
VERSION:  Tracked in YAML header + version history table, not filename
```

---

## Version History

| Version | Date | Changes |
|:---|:---|:---|
| 1.0 | 2026-01-19 | Initial version |
| 1.1 | 2026-01-21 | Removed versions from filenames. Version tracking now lives in YAML headers and version history tables. GitHub commit history handles granular changes. |
