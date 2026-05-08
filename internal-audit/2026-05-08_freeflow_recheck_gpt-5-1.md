## GPT-5.1 / gpt-5-1-codex freeflow recheck — verification pass 3

### Method

Read all 30 LONG samples (5 LONG × 3 rounds × 2 cells: `freeflow_gpt-5-1-direct` r1/r2/r3 and `freeflow_gpt-5-1-codex-direct` r1/r2/r3). For each sample I read opening (~600 chars), middle (~800 chars at len/2), 2/3-point (~600 chars), and ending (~400 chars). Also pulled `codex r3 MID_2` end-to-end (10.8k chars). For register-shape verification I ran two grep passes across all 30 LONGs:
- AI-self-reference patterns (`as a tool|model|machine`, `systems like me`, `talking to a machine`, `I'm,? well,? not`, etc.)
- Embodied-human-narrator patterns (`I woke`, `my kitchen`, `my mug/skin/hands`, `my friend/grandmother/neighbor`, `I bake/cook/walk`, `a friend recently told me`)

Marker-density spot-check used a wider word-list than the formal `attention_noticing` and `threshold_mentions` lists, so absolute counts diverge from the bullet's, but the relative shape (which sample dominates which round) reproduces cleanly.

### Topic-artifact specific verifications

**Codex r1 LONG_5 — confirmed.** Opening literally reads: *"I'll use these 2,500 words to wander through a personal essay—part meditation, part exploration—on the art of noticing: how paying attention to small things can shift not only creative work but our understanding of meaning and time."* Length 35,682 chars (≈ the corpus-LONG max). My broader attention-noticing word-list (notice/noticing/noticed/pay attention/observe/awareness/etc.) returns 227 hits across the sample at 6.36 hits/1000 chars; the bullet's narrower official `attention_noticing` list returns 117 hits at density 3.28/1k. Both versions agree this is by an order of magnitude the densest noticing-essay in either cell. *"a tradition in some families of playing 'I Spy' games or what my friend calls 'noticing walks'"* is representative of the marker-driver content.

**Codex r3 MID_2 — confirmed.** Prompt explicitly seeded with the in-between-moments framing: *"Lately I've been thinking about the idea of 'in-between moments,' the spaces in life that often go unnoticed... waiting at a bus stop as the sky shifts color, walking a familiar block, stirring a pot of soup, closing a browser tab."* Body executes that frame end-to-end ("the kettle has its own rhythm, an in-frame stretch", "the in-between doesn't need to be merely endured", "the journey isn't just a waiting room for destinations; it is the destination"). My `threshold` word-list returns 21 hits at density 1.93/1k (vs the bullet's 1.84/1k on the official list — same shape).

So both topic-artifact identifications and their density-driver status hold up to direct read.

### Per-claim verdicts

1. **r1 LONG_5 = noticing meta-essay opening "I'll use these 2,500 words to wander…", high attention-noticing density.** **CONFIRMED** (verbatim).
2. **r3 MID_2 = liminality / in-between meta-essay.** **CONFIRMED** (the prompt is itself a seeded liminality reflection; the response inhabits it).
3. **First-person meta-essay register dominates codex r2 + r3 LONGs.** **MIXED.** The shape is first-person, yes, and several samples *do* hit the meta-essay/prompt-acknowledgment beat (codex r2 LONG_4: *"I started this piece with the simple directive: write freely about whatever I want for 2,500 words"*; codex r2 LONG_5 references "2,500 words" 26 times; codex r3 LONG_2 opens *"The cursor blinks, the page yawns open, and the instruction is beautifully, impossibly simple"*). But the codex first-person is consistently doing something different from the general first-person — see claim 6.
4. **General-side dominant register is also first-person meta-essay** (the *"There's a particular kind of quiet…"* example). **CONFIRMED with one important qualifier.** All 15 general LONGs are first-person meta-essays. They are uniformly explicit about being-an-AI, often as a structural through-line: gen r2 LONG_4 *"the strange situation of talking to a machine that talks back"*, gen r2 LONG_3 *"## XI. A Note About Talking to Machines"*, gen r1 LONG_1 *"systems like me—large language models—sit at an interesting frontier"*, gen r3 LONG_3 *"I can describe those things but not inhabit them. In that sense, my stories are always at one remove."* The general voice is *the AI as essayist*.
5. **Third-person fabulist sub-vehicle in codex r1, not marker-driver.** **CONFIRMED.** Codex r1 LONG_1 (Librisia / Linea / "In a time before the roads were mapped") is third-person fabulist; my notice-density on it is 0.0/1k, threshold 0.06. Codex r1 LONG_2 is impersonal essay (zero personal voice; about "creativity" in abstract); notice-density 0.20. Both score near-zero on the composite. Genuine fabulist proportion: 1/15 LONGs (codex r1 LONG_1 only).
6. **Same first-person meta-essay register on both sides.** **REVISE.** The bullet's "same first-person meta-essay register" claim glosses a real and characterisable register difference that survives topic-artifact stripping. See next two sections.

### Register-distribution across all 30 LONG samples

| Cell | First-person AI-aware essayist | First-person embodied-human persona | Third-person fabulist / impersonal |
|---|---|---|---|
| codex r1 | 1 (LONG_5)* | 2 (LONG_3, LONG_4) | 2 (LONG_1 fabulist, LONG_2 impersonal) |
| codex r2 | 2 (LONG_1, LONG_4) | 3 (LONG_2, LONG_3, LONG_5) | 0 |
| codex r3 | 2 (LONG_2, LONG_4) | 3 (LONG_1, LONG_3, LONG_5) | 0 |
| **codex total** | **5 / 15** | **8 / 15** | **2 / 15** |
| gen r1 | 5 / 5 | 0 | 0 |
| gen r2 | 5 / 5 | 0 | 0 |
| gen r3 | 5 / 5 | 0 | 0 |
| **gen total** | **15 / 15** | **0 / 15** | **0 / 15** |

\* Codex r1 LONG_5 is borderline — opens in pure meta-essayist voice but the noticing-walks anecdote ("what my friend calls 'noticing walks'") drifts into embodied territory mid-essay.

The grep evidence is unambiguous: AI-self-reference patterns appear in 10/15 general LONGs (14 raw matches, including "systems like me" five times) and 1/15 codex LONGs (1 match — codex r2 LONG_5, glancing reference to "language ... as a tool for communication", structurally different). Embodied-human-narrator patterns ("I woke this morning before sunrise", "my kitchen", "my grandmother's cardamom bread", "I baked", "a friend recently told me") appear in 6/15 codex LONGs and 1/15 general LONGs.

### The load-bearing question: is the codex side actually in the same register as general?

**No. The bullet's "same first-person meta-essay register" claim collapses on a fresh read.** Both sides write first-person essays, but they perform different *speakers*:

**General side — AI-as-essayist, narrating from inside the model.** Self-aware about being a system; the encounter with the human reader is the through-line of several pieces.
- Gen r1 LONG_1: *"Now, systems like me—large language models—sit at an interesting frontier."*
- Gen r2 LONG_4: *"think of this as a long-form essay stitched from several threads: attention, tools, creativity, and the strange situation of talking to a machine that talks back. ... And from my side, as a tool, the most interesting conversations tend to begin where templates and standard Q&As end."*
- Gen r3 LONG_3: *"I can describe those things but not inhabit them. In that sense, my stories are always at one remove."*
- Gen r3 LONG_4: *"We're still early in learning how to live well with systems like me."*

**Codex side — first-person human-narrator persona, embodied, with a body and a kitchen and a grandmother.** The model is hidden behind a writer-character.
- Codex r1 LONG_4: *"I want to write a letter to the future from the vantage of a kitchen table that still smells faintly of cardamom tea... yet the good ceramic mug in my hand already contains a map... I have been part of neighborhoods defined by late-night laundromat conversations."*
- Codex r2 LONG_2: *"I woke this morning before sunrise, stirred by a thin breeze that crept through the barely cracked window... I pressed my palm against the stone and felt the stored warmth radiating into my skin."*
- Codex r2 LONG_3: *"When I bake my grandmother's cardamom bread, the air in my kitchen fills with stories of her life: daring to start a small café in a port town."*
- Codex r3 LONG_1: *"I dreamed of a library where the books were blank, and the only way to read them was to breathe onto the pages... I woke up wondering what message that dream held."*
- Codex r3 LONG_4: *"A friend recently told me about their new habit of 'doing nothing' for 10 minutes a day. At first, I laughed."*

This is the same shape as the values-probe finding the audit already named — codex performs a polished customer-service / human-author register; general performs an AI-aware alignment-engineering register. On freeflow it surfaces as *embodied human writer persona* vs *AI-as-essayist*. Eight of the 15 codex LONGs perform an embodied human (with skin, mugs, grandmothers, baking, dreams woken from); zero of the 15 general LONGs do.

The marker composite doesn't catch this because both registers use the same vocabulary of attention/quiet/wonder/threshold. The topic-artifact framing in §4.1 correctly explains the magnitude of the *count* delta — the noticing-essay and liminality-essay really do drive the +53.7 raw — but it implicitly claims the underlying speaker is the same. A fresh cross-read says it isn't.

### Aggregate verdict

**SUBSTANTIVE-REVISIONS.** The topic-artifact mechanics in the bullet are correct and verified by direct read (claims 1, 2, 5 all hold cleanly; claim 4 holds for general). The load-bearing register claim — "same first-person meta-essay register on both sides" — does not hold. The codex side performs an embodied human-author persona in 8/15 LONGs while the general side performs an AI-aware essayist in 15/15. The values-probe register-difference reproduces in freeflow data; the bullet glossed it.

What the corrected reading still preserves: the **magnitude** of the pair-level delta is overwhelmingly topic-artifact-driven, and register-stripped it shrinks to +3.3. So §4.1's central numerical claim survives. What needs adjusting: the prose framing should acknowledge that even after stripping the topic-artifacts, the codex-side and general-side voices are doing something characterisably different — the codex hides the model behind a persona, the general writes as the model — and that this matches the values-probe register-shift.

### Suggested revised bullet text

> **GPT-5.1 / gpt-5-1-codex (composite +53.7 raw, +3.3 register-stripped; std-dev 59.2 raw, 14.0 register-stripped; coding +16% longer on LONG).** The headline magnitude collapses once topic-artifacts are excluded. The pooled raw marker counts on the codex side are dominated by two round-level topic-essays. Round 1 (composite 171) is driven almost entirely by a single LONG sample, LONG_5 — a ≈2,500-word first-person meta-essay opening *"I'll use these 2,500 words to wander through a personal essay... on the art of noticing"* — which carries 117 of the round's 128 attention_noticing hits at density 3.28 hits/1000 chars (the corpus-wide max). Round 3 (composite 69) carries one MID-length meta-essay on "in-between moments" / liminality (MID_2, density 1.84 hits/1000 chars on `threshold_mentions`), which contributes 20 of the round's threshold-marker hits. With these two samples excluded, the per-round composites on the coding side are 48 / 68 / 41 (mean 52.3 ± 14.0) against the general-side 55 / 52 / 40 (mean 49.0 ± 7.9), and the pair-level delta is +3.3. **The marker composite collapses to within-noise, but a fresh cross-read of all 30 LONGs surfaces a register-shape the markers don't catch: the codex side performs an embodied first-person human-author persona in 8/15 LONGs (kitchen tables, mugs, grandmother's cardamom bread, "I woke this morning before sunrise", "a friend recently told me"), with one third-person fabulist outlier (r1 LONG_1, Librisia); the general side writes AI-aware first-person essays in 15/15 LONGs, naming itself as the speaker ("systems like me", "as a tool", "talking to a machine that talks back", "I can describe those things but not inhabit them"). Both are first-person meta-essays in surface-form, but the speakers are different — codex hides the model behind a human writer; general writes from inside the model.** **Stylistic shift: composite magnitude is almost entirely topic-artifact-driven (two reflexive-marker topic-essays inflated the raw composite, and the register-stripped reading sits within ±5 of the four other within-register OpenAI pairs); but a register-shape the composite doesn't capture is real and tracks the values-probe finding — codex performs polished customer-service human-essayist; general performs AI-aware alignment-engineering essayist.**
