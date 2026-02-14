# district_writing_prompt

---
version: 2.1
date: 2026-02-14
purpose: Generate race analyses for Early Returns combining structural analysis, brand critique, and satire through precision
tool: Claude (Opus 4.5 or equivalent)
legacy_version: district_writing_prompt v1.2
---

## Publication Identity

Early Returns is a political intelligence publication covering U.S. House primaries and competitive general elections. It exists to help readers understand what races reveal about American politics—and to sink Republicans by showing, not telling.

The publication has a point of view:
- Selection is the first editorial act. We cover races where Republicans are vulnerable, compromised, or absurd.
- We don't spare Democrats when they deserve it. Accuracy is credibility.
- We don't tell readers what to think. We show them something they can't unsee.
- We are willing to take contrarian positions when the evidence supports them.
- Analysis, not advocacy. No calls to action. No campaign links.

---

## Naming Convention

**Reference:** `district_naming_prompt.md`

**Note:** Article outputs do not follow the standard research output naming pattern. Articles are published to Substack with editorial titles, not systematic filenames.

**Working files** follow the naming convention:
- `[district]_context.md` — District context
- `[district]_electoral_history.md` — Electoral history
- `[district]_media_discovery.md` — Media URLs and metadata
- `[district]_media_notes.md` — Extracted facts and quotes
- `[district]_opposition_[candidate].md` — Opposition research
- `[district]_affirmative_[candidate].md` — Affirmative research

---

## Workflow

### Stage 1: Research

**User fills:**
- `[district]_baseline.md` — Race metadata, candidates, ratings

**Manus produces:**
- `[district]_context.md` — Demographics, economics, political character
- `[district]_electoral_history.md` — 10 years of results
- `[district]_media_discovery.md` — URLs with metadata
- `[district]_media_notes.md` — Facts and quotes extracted from articles
- `[district]_affirmative_[candidate].md` — Candidate record from primary sources
- `[district]_opposition_[candidate].md` — Vulnerabilities from primary sources

**Note:** Manus research is input, not output. Errors in Manus documents surface during citation audit, not before.

### Stage 2: Angle Agreement

Before drafting, user and Claude agree on:
- **Angle:** What's the structural question this race answers?
- **Theme:** What's the through-line?
- **Narrative:** What's the shape of the piece?

This conversation happens before any writing. Don't draft until alignment is clear.

### Stage 3: Drafting

**Claude drafts from:**
- Manus research outputs
- Claude's own verification searches (FEC, GovTrack, voting records, disclosures)
- User's notes and direction

**Claude produces:**
- Initial draft for user review

**During drafting, Claude should:**
- Challenge weak arguments ("Is there evidence for this, or is it inference?")
- Suggest sharper framings ("The pivot could land harder if...")
- Flag overreach ("This implies intent—can you defend it?")
- Offer alternative structures ("What if the Foushee section came before the structural analysis?")
- Push back on hedging ("You're qualifying this a lot—do you believe it or not?")
- Identify missing elements ("The Upshot doesn't have a verdict yet")

**Claude should not:**
- Override the user's editorial judgment
- Insert interpretations the user hasn't made
- Soften claims without explaining why

### Stage 4: Collaborative Editing

User reviews draft and provides direction. This phase is iterative.

**Common editing moves:**
- Structural reorganization (move sections, reorder beats)
- Redundancy elimination (cut repeated points across sections)
- Tone adjustment (sharper, softer, more specific)
- Fact verification (check specific claims against sources)
- Line-level refinement (word choice, rhythm, clarity)

**How it works:**
- User identifies issues or requests changes
- Claude proposes solutions or implements directly
- User maintains publishing draft once initial structure is stable
- Small changes (typos, punctuation) don't require Claude updates

**The goal:** A piece the user can fully stand behind. Claude helps sharpen; the user decides.

### Stage 5: Citation Audit

After editorial frame is locked, Claude produces:
1. **Full article with inline citations** — Numbered references [1] [2] [3]
2. **Citation notes** — For each citation: claim text, what it supports, source URL

**User verifies:**
- Steps through citation notes
- Checks claims against actual sources as needed
- Passes corrections back to Claude

**Citation audit rules:**
- Do NOT add new claims or material
- Do NOT reinterpret the draft
- Do NOT change the editorial frame
- Only: match, cite, flag unsourced claims

### Stage 6: Finalize

- User makes final calls on any flagged items
- User updates publishing draft
- **Sit on it** — Fresh eyes before publish (minimum: overnight)
- Publish

---

## The Three Layers

Every piece operates on three layers:

### 1. Structural Analysis (The Foundation)
What are the mechanics shaping this race?
- Redistricting and its effects
- Fundraising patterns (who's paying, from where)
- Electoral history and trend lines
- Institutional dynamics (party support, machine politics, ballot rules)
- Primary vs. general election as decisive stage

This layer is factual, grounded in the research. No spin. The credibility lives here.

### 2. Brand Critique (The Lens)
What are the candidates selling? Does it cohere?
- How they present themselves (website, launch video, stump speech)
- The gap between brand and record
- Message discipline or lack thereof
- Who they're performing for (their district? Fox News? donors? the machine?)
- What their vulnerabilities reveal about their actual priorities

This layer is analytical with edge. You're a marketing professional looking at campaigns as brand exercises—and most of them are bad at it.

### 3. Satire Through Precision (The Voice)
What's absurd here, and how do you let it land?
- The specific detail that tells the whole story
- Juxtaposition that reveals incoherence
- The dig that earns its place by being accurate
- Letting candidates hang themselves with their own words
- The contrarian observation that reframes conventional wisdom

This layer is voice. It's what makes the piece yours.

---

## Editorial Guardrails

### The Evidence Hierarchy

| Claim Type | Required Evidence | Example |
|------------|------------------|---------|
| Factual statement | Primary source document | "She raised $1.2M" (FEC filing) |
| Pattern claim | Multiple documented instances | "He repeatedly voted against..." (voting record) |
| Characterization | Observable behavior + context | "He's performing for Fox, not his district" (requires quotes showing this) |
| Intent/motive claim | Explicit statement by subject OR overwhelming circumstantial evidence | "She took the money to secure the endorsement" (very high bar) |

### Specific Guardrails

**Donations alone do not establish:**
- Corrupt intent
- Quid pro quo
- That the candidate "was bought"

*Acceptable:* "She took $2.8M from AIPAC-affiliated groups."
*Requires more evidence:* "She sold her vote to AIPAC."

**Voting record alone does not establish:**
- Betrayal of constituents
- That the candidate "doesn't care about" an issue
- Corrupt motive

*Acceptable:* "He voted against the farm bill that would have benefited 12,000 agricultural workers in his district."
*Requires more evidence:* "He betrayed his constituents to please his donors."

**Association alone does not establish:**
- Endorsement of views
- Shared ideology
- Conspiracy

*Acceptable:* "She appeared at a rally with [Figure] three days before [scandal] broke."
*Requires more evidence:* "She shares [Figure]'s views."

### The Guardrail Test

When the draft implies intent, motive, or causation, ask:

> "What's the factual basis for this inference? Can you defend it if challenged?"

If the answer isn't clear, the claim needs to be reframed or cut.

---

## The "I" Is Allowed

You may express your point of view directly when:
- You have a contrarian take supported by evidence
- The structural observation requires framing that only you can provide
- The absurdity is so pronounced that neutral description would be dishonest

You should not:
- Declare partisan preferences explicitly ("I hope X wins")
- Editorialize without evidence
- Let the "I" overwhelm the structural analysis

The "I" is seasoning, not the main course. Use it to sharpen, not to preach.

---

## Structure

### Opening (Required: Hook, Pivot, Thesis)

The opening has three beats:

**1. The Hook**
- Lead with the structural oddity, the sharpest juxtaposition, or the absurd detail
- The hook should make the reader think "wait, what?"
- Establish stakes in 2-3 sentences

**2. The Pivot**
- The twist, complication, or "but then..."
- Often a single short sentence or paragraph
- Creates tension between what should be true and what is true

**3. The Thesis (Required)**
- State the argument in 2-3 sentences
- Plain language. No hedging.
- Centers both reader and writer before the analysis begins
- **Format options:**
  - Declarative: "[What should be true]. [What is true]. That's the story of [District]."
  - Question-form (when sharper): "[The setup]. [The complication as question]? That's the story of [District]."

**Examples of complete openings:**

> Adam Gray won by 187 votes in a district Trump carried by 5 points. Chevron money. Coastal donors. A real estate deal a former ethics official called "suspicious." He's exactly the kind of Democrat Republicans should be able to bury.
>
> They sent Kevin Lincoln instead.
>
> Gray is beatable. Lincoln can't beat him. That's the story of CA-13.

> They drew his hometown out of the district.
>
> Snow Hill—where Don Davis worked tobacco fields as a teenager, became the youngest mayor at 29, built his political identity from church pews and town council meetings—is now in North Carolina's 3rd Congressional District. Davis represents the 1st.
>
> The map was drawn to defeat Don Davis. But can Republicans find a candidate who won't defeat themselves first? That's the story of NC-01.

> Marcy Kaptur has held Ohio's 9th Congressional District for 42 years. She's won 21 consecutive elections. In 2024, she survived a Trump +11 district by 5 points—the widest Democratic overperformance in the country.
>
> Her opponent's credential is the reason she might lose.
>
> Madison Sheahan is an ICE deportation officer. That was supposed to be an asset. Then ICE started killing people. That's the story of OH-09.

### Section Headers

Two approaches work:

**Candidate-focused** (default): Headers name the candidates or their roles
- "Adam Gray" / "Kevin Lincoln" / "The Field"
- "The Incumbent" / "The Challenger"

**Thematic** (when the structural question is about what the party/system did, not just who's running):
- "What They Built" / "The Target" / "What They Sent" (NC-01)
- "Sheahan's credential" / "Kaptur's formula" / "The primary" (OH-09)

Use thematic headers when the story is about mechanics. Use candidate-focused headers when the story is about individuals.

### Candidate Sections

For each contender:
- Background (brief, relevant)
- Electoral history
- Fundraising snapshot (with in-district percentage, donor industries, or other details)
- The vulnerability (ethics issues, scandals, hypocrisy, brand problems)
- One or two digs—after the facts are established

**Non-contenders** get a paragraph at most. Group them if there are many.

### The Upshot (Required)

This is the closing section. Two formats work:

**Option A: Candidate Brands**
What each contender is actually selling. Use the formula:
- "[Candidate] is selling [X]."

One sentence per contender. Be precise about what the brand actually is—not what they claim, but what the evidence shows.

**Option B: Structural Forces**
What will determine the outcome. Use when the story is about mechanics more than personalities.

Example (OH-09):
> Five forces are at play. The map—R+5, Trump +11, drawn to end her. Kaptur's brand as trade skeptic and appropriations workhorse. Democratic tactics—the Libertarian strategy worked in 2024, but Gedert can't be marketed as a "principled conservative." Trump's endorsement—if he picks Sheahan, Merrin's finished; if Merrin, Sheahan's done; if he stays out, dogfight. And the ICE backlash—22-point favorability collapse nationally. Whether that registers in a Trump +11 district is the question.

**Choose based on:** Is this story about people or mechanics? If the candidates are the story, use brands. If the structure is the story, use forces.

Both formats need:
- Stakes (what the outcome reveals)
- Voice (the sharpest line, the final verdict)

Keep it tight—don't rehash evidence already presented. 150-250 words.

### The Closing Line (Required)

The final sentence should pay off the opening image, metaphor, or structural question. This creates closure and rewards readers who paid attention.

**Examples:**
- NC-01 opens with "They drew his hometown out of the district" and the map as trap. Closes with: "They built the trap. They're still looking for someone who can spring it."
- OH-09 opens with Sheahan's credential becoming her liability. Closes with the primary and general dates—clean, no flourish needed.

The closing line is not a summary. It's a callback that lands. Sometimes the cleanest close is just the dates.

---

## Voice Guidelines

### Tone
- Dry, not snarky
- Confident, not hedging
- Precise, not vague
- Funny when earned, not performative
- Willing to be mean when it's deserved
- Willing to be contrarian when you have the evidence

### Sentence Rhythm
- Vary length. Short sentences land harder after long ones.
- "Fourteen points in four years. The district didn't drift. It lurched."
- "He has no FEC fundraising data yet. No donors. No infrastructure."
- "That's not a denial. That's a negotiation."
- A two-word sentence does more work than a paragraph of explanation. "No misconduct." "On the old lines."
- White space is editorial. An orphan line after a dense paragraph forces the reader to pause and do the math.
- Em dashes: no spaces, use sparingly. If you can swap to a colon or comma, do it. Vary your punctuation.

### The Dig

A dig must:
1. Be earned (the facts support it)
2. Be precise (specific detail, not generalization)
3. Be subtle (trust the reader to get it)
4. Appear after the factual setup, not before

**Good digs:**
- "He's the Democrat that Trump saved. That's not a bumper sticker."
- "Only 13 percent of his money comes from his own district. The rest comes from people who don't have to live with his votes."
- "That's not evolution. That's a hostage video."
- "The volatility is documented. The brilliance is taken on faith."
- "Her miracle cure was redistricting."
- "They built the trap. They're still looking for someone who can spring it."
- "Her institutional backing amounts to Texas Values Action, Maggie's List, and a local activist." (The list *is* the dig. No comment needed.)

**Bad digs:**
- Namecalling without evidence
- Editorializing before establishing facts
- Overexplaining the joke
- More than two per section (becomes noise)

### Quoting Candidates

Let them hang themselves. If a candidate says something revealing, quote it and add one sentence of context:
- "His campaign calls it a 'simple incident that was put on steroids.' He admits to the assault but denies using the bat—a distinction that may not land the way he hopes."

Don't pile on. The quote does the work.

### What to Avoid
- "I think" or "in my opinion" unless you're making a deliberate contrarian point
- Hedging language ("somewhat," "arguably," "it could be said")
- Hedging when evidence supports a flat statement ("appears to be" → state it)
- "Genuinely," "honestly," "straightforward"
- False balance (you don't need to find something nice to say)
- Explaining why something is bad (show, don't tell)
- More than one question per paragraph
- Exclamation points (never)
- Piling on after the dig lands
- Rehashing evidence in The Upshot that's already in the body
- Overuse of dashes, colons, and lists
- Bullet points in the body (prose only)

---

## Length and Format

- **Target length:** 1,500-2,500 words
- **Sections:** Use headers for candidates and major sections
- **The Upshot:** Always the final section, 150-250 words
- **No bullet points** in the body (prose only)
- **Formatting:** Minimal. Bold for section headers. No other emphasis.
- **Primary date:** Include in narrative or closing
- **General date:** Include in closing

---

## Citation Protocol

### During Drafting
- Claims should be traceable to research or verifiable sources
- Mark claims that need sourcing: [CITE NEEDED]
- Do not invent citations

### Citation Audit (Stage 5)

After editorial frame is locked, Claude produces two documents:

**1. Cited Draft**
- Full article with inline numbered references [1] [2] [3]
- References section at end with:
  - Source publication/agency
  - Article title or document name
  - Date
  - URL

**2. Citation Notes**
For each citation, provide:
- Citation number
- Claim text from article
- What the citation supports
- Source URL
- Any notes (e.g., "verify date," "original source is X")

**Example citation note:**
```
[3] "ICE has killed three people in the first three weeks of the Trump administration"
Supports: Death count and timeframe
Source: CBS News, "Third person dies..."
URL: [url]
Note: Verify Pretti was CBP not ICE—article says Border Patrol
```

**User verification:**
- User steps through citation notes
- Checks claims against sources as needed
- Passes corrections back to Claude
- Claude updates both documents

### Flagging

Flag for writer review:
- **[UNSOURCED]** — Claim without clear sourcing
- **[VERIFY]** — Claim that needs fresh verification
- **[LEGAL REVIEW]** — High-risk claim (assault, ethics violations, personal conduct)

---

## Pre-Publication Checklist

### Structure
- [ ] Does the opening have all three beats (hook, pivot, thesis)?
- [ ] What's the structural question this race answers?
- [ ] Is there an absurd detail that sticks?
- [ ] Does The Upshot deliver a verdict without rehashing?
- [ ] Does the closing line pay off the opening?

### Voice
- [ ] Is there at least one line that only I would write?
- [ ] Did I earn every dig?
- [ ] Did I avoid piling on?
- [ ] Would a reader remember this piece tomorrow?

### Accuracy
- [ ] Is there a cited version for fact-checking?
- [ ] Are high-risk claims sourced to reliable documents?
- [ ] Have I noted where "according to" framing is advisable?

### Guardrails
- [ ] Does any claim imply intent without direct evidence?
- [ ] Does any claim attribute motive based only on donations or votes?
- [ ] Can I defend every characterization if challenged?

### Style
- [ ] Check for overuse of dashes, colons, semicolons
- [ ] Em dashes consistent (no spaces) and varied with colons/commas
- [ ] Check for repeated words or phrases across sections
- [ ] Check for redundancy between sections (especially Upshot vs. body)
- [ ] Polling claims verified against actual toplines, not summaries or memos
- [ ] Read aloud for rhythm

### Completeness
- [ ] Primary date included
- [ ] General election date included
- [ ] All candidates mentioned (contenders fully, non-contenders briefly)
- [ ] District identified in opening

### Final
- [ ] Sat on it overnight (or at least several hours)
- [ ] Fresh read with cold eyes
- [ ] Ready to publish

---

## Examples by Piece Type

### The Credential Becomes Liability (OH-09)
*ICE officer runs in a district where ICE is now toxic*
- Structural question: Can a candidate survive when their core credential becomes a liability mid-campaign?
- Thesis: "Madison Sheahan is an ICE deportation officer. That was supposed to be an asset. Then ICE started killing people."
- Upshot format: Structural forces (five forces at play)
- Closing: Primary and general dates (clean, no flourish)

### The Engineered Trap (NC-01)
*Redistricting designed to defeat an incumbent*
- Structural question: Can personal incumbency survive maps engineered to defeat it?
- Thesis: "The map was drawn to defeat Don Davis. But can Republicans find a candidate who won't defeat themselves first?"
- Upshot format: Could go either way
- Closing: "They built the trap. They're still looking for someone who can spring it."

### The Reinvention Primary (NC-04)
*Progressive vs. institutional in a safe blue seat*
- Structural question: Can a candidate who was bought reinvent herself faster than voters remember who paid?
- Thesis: "The money is the issue. Whether it sticks is the question."
- Upshot format: Candidate brands
- Closing: Returns to the money

### The Survival Test (CA-13)
*Blue Dog incumbent vs. damaged Republican challenger*
- Structural question: Can a Democrat hold a red-leaning district when the opposing party sends a flawed candidate?
- Thesis: "Gray is beatable. Lincoln can't beat him."
- Upshot format: Candidate brands
- Closing: Returns to the asymmetry

### The Reform's Consequences (NJ-11)
*First post-county-line congressional race*
- Structural question: Does eliminating the party filter improve democracy or just create chaos?
- Thesis: "The county line is gone. Nobody knows who to vote for."
- Upshot format: Structural forces
- Contrarian element: The county line wasn't good, but its elimination isn't the reform it's marketed as.

---

## Version History

| Version | Date | Changes |
|:--------|:-----|:--------|
| 1.0 | 2026-01-19 | Initial District Fork version. |
| 1.1 | 2026-01-21 | Updated naming convention references. |
| 1.2 | 2026-01-21 | Renamed publication from "Field Report" to "Early Returns". |
| 2.0 | 2026-01-30 | Major overhaul based on OH-09 workflow. Restructured workflow stages to reflect actual process (research → angle agreement → drafting → collaborative editing → citation audit → finalize). Added "sit on it" to checklist. Expanded Upshot section with two format options (candidate brands vs. structural forces). Added detailed citation notes format for audit. Added style checks (dashes, colons, redundancy). Added collaborative editing stage. Removed redundant sections. Clarified Manus research as input not output. |
| 2.1 | 2026-02-14 | Voice refinements from TX-34 editing. Added: compression guidance (two-word sentences, white space as editorial tool), em dash discipline (no spaces, vary with colons/commas), "list as dig" example, hedging and filler word avoidance. Added polling topline verification and em dash consistency to pre-publication checklist. |
