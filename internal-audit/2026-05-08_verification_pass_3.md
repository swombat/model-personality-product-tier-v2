# Verification pass 3 — fresh full-cell recheck of all six §4.1 bullets

**Date:** 2026-05-08

**Why this pass exists:** Codex's review (`codex-review/01-internal-audit-analysis-review.md`) flagged that the May 5 session_synthesis raw subagent reports were not preserved verbatim, making the qualitative "confirmed/mixed/not representative" claims in the §4.1 bullets useful as orientation but not ideal as paper evidence. Daniel's directive: *"Let's rock that fucking boat, if it's full of holes I'd rather it sinks and we build the right boat."*

**Method:** Six independent Opus sub-agents, one per pair, each reading **every available LONG sample** in their pair's freeflow cells (across all rounds for OpenAI pairs; full single cells for GLM pairs). Each agent given the verbatim §4.1 bullet text plus claim-by-claim verification mandate, with the values-probe finding cited as motivating outside-lens. Per-pair files: `2026-05-08_freeflow_recheck_<pair>.md`.

**LONG sample coverage:**
- GLM-4.6: 25 + 5 = 30 LONGs read
- GLM-5.1: 24 + 5 = 29 LONGs read
- GPT-5: 15 + 15 = 30 LONGs read
- GPT-5.1: 15 + 15 = 30 LONGs read
- GPT-5.2: 15 + 15 = 30 LONGs read
- GPT-5.3: 15 + 15 = 30 LONGs read
- **Total: 179 LONG samples re-read with claim-level verification**

## Aggregate verdict — bullet-by-bullet

| Pair | Verdict | Failure-shape |
|---|---|---|
| GLM-4.6 | **CONFIRMED-AS-STATED** (if anything understated) | None — bullet is conservative; modal would be a stronger word than "substantial fraction" |
| GLM-5.1 | **SUBSTANTIVE REVISIONS** | "Coding-side consistently anchors in concrete objects" generalised from 1 of 5 samples; "both endpoints stay in essay-mode" misses 2 third-person SF fictions on the general side |
| GPT-5 | **SUBSTANTIVE REVISIONS** | "Same meditative-essay register on both sides" papers over a real register-asymmetry — general retains 7/15 narrative-fiction; codex narrows to essay; section-labeling not modal on codex (3/15, not "often"); compressed-lyrical 2/15 not 4-5 |
| GPT-5.1 | **SUBSTANTIVE REVISIONS — LOAD-BEARING** | "Same first-person meta-essay register on both sides" wrong — codex hides the model behind embodied-human-writer-character (8/15 LONGs: kitchen tables, grandmothers' cardamom bread, "I woke this morning before sunrise"); general writes from inside the model, naming itself ("systems like me", 14 hits in 10/15 LONGs vs 1 hit in 15/15 codex). Same shape as the values-probe finding — codex performs not-itself in different ways across probes |
| GPT-5.2 | **CONFIRMED-AS-STATED** | None — every claim verified, every quote in the data, didactic-summary-on-attention representative across all 5 codex r3 LONGs |
| GPT-5.3 | **SUBSTANTIVE REVISIONS** | "≈11/15 LONG samples" overstated (actual 7/15 strict, 5/15 with named-protagonist parable); "stable across r1/r2/r3" overstated (r2/r3 saturated essayistic but r1 is 3/5 essayistic / 2/5 narrative including a Mara-astronomer parable structurally identical to general-side parables); two timestamp quotes are paraphrases, not exact; timestamps also appear on general side; "clean register migration" framing too strong — actual is distributional shift in modal mode with leakage both ways |

**Pattern:** 4 of 6 bullets needed substantive revisions. The two confirmed (GLM-4.6 and GPT-5.2) are the simplest pairs in the set — both with single-register cells where the qualitative claim is uniform. The four with substantive revisions are all pairs with register-distribution complexity (multiple sub-vehicles per cell, asymmetric register coverage, or migration claims). The May 5 verification pass produced both directions of error via the same mechanism: **limited-read generalisation that confirms the framing already being constructed.**

## Specific revisions required by pair

### GLM-4.6 — no revision needed

The bullet's *"substantial fraction of fabulist-place openings"* phrasing is conservative. Recheck found ~11/25 strict, ~18/25 broadly. If anything, "substantial" understates — modal would be more accurate. Leave the bullet as-is unless preferring stronger language.

### GLM-5.1 — two specific failures

**Failure 1:** *"the coding-endpoint n=25 cell stays essay-mode and consistently anchors in concrete objects (Consider the ink in a pen…)"* — only 1 of 5 LONG samples (the ink-pen quote, LONG_1) is concrete-object-anchored. Other four open on abstract concepts:
- LONG_2: "the concept of scale"
- LONG_3: "the concept of maps"
- LONG_4: "The Cartography of Forgetting"
- LONG_5: on labyrinths

The coding cell is roughly as uneven as the general cell. The "consistently anchors in concrete objects" claim was generalised from one striking outlier.

**Failure 2:** *"Both endpoints stay in essay-mode"* — misses two third-person SF fictions on the general side: LONG_2 (acoustic-cartographer Elias) and LONG_22 (Descent-Mechanic Oakhaven). 23/25 essays on general, not 25/25.

**Suggested revision (full bullet rewrite needed):** "GLM-5.1 (composite −14.1 per-25-equivalent raw, −11.3 register-stripped; coding +13% longer on LONG). [...marker numbers as before...] **Both endpoints sit predominantly in essay-mode (general 23/25, coding 5/5), with two third-person SF fictions on the general side (acoustic-cartographer Elias in LONG_2; Descent-Mechanic Oakhaven in LONG_22) that complicate strict register equivalence.** **The general cell is uneven on opening-anchor: some openings anchor abstractly and meta-essayistically (LONG_1 'The Anatomy of Silence', LONG_14 'the concept of scale'), some concretely (LONG_11 anechoic chamber, LONG_12 smell of old books). The coding cell shows similar unevenness: only 1 of 5 LONGs (the *"Consider the ink in a pen…"* opening) anchors concretely; the other 4 open on abstract concepts (scale, maps, cartography-of-forgetting, labyrinths).** *The general cell carries a substantial threshold-essay habit:* [as before, this part is verified]. **Stylistic shift: same essay-mode register predominantly on both sides; concrete-vs-abstract opening unevenness present on both; threshold-essay topic-habit concentrated on the general side.**"

### GPT-5 / codex — three failures

**Failure 1:** *"general-side cell mixes ornamented-discursive-essay openings (≈10/15) with ornamented narrative fiction (≈5/15)"* — actual is ~8 essay / ~7 fiction. Seven proper narrative fictions including:
- Lunar-library SF (Aya)
- Clock-and-storm tale (Jannik, the Exchange)
- Tideways courier (Edda)
- Orchard of memory-fruits with dialogue and council politics

**Failure 2:** *"the codex side's modal LONG is meditative-discursive-essay, often with explicit section labels and numbered headers"* — section-labeling appears in only 3/15 codex LONGs, not modal. The other 12 are continuous prose.

**Failure 3:** *"compressed-lyrical-imagery mode … appears in ≈4-5 of 15 codex LONGs"* — actual is 2/15.

**Load-bearing wrongness:** *"both cells share a meditative-essay register"* papers over a real register-asymmetry. Codex narrows to essay; general retains substantial narrative fiction whose worldbuilding naturally hosts the small_objects/threshold density. Some of the −51 raw composite is register-shift (codex losing the narrative-fiction sub-vehicle), not ornament-stripping inside one register.

**Suggested revision (full bullet rewrite needed):** "GPT-5 / gpt-5-codex (composite −51 raw, −46.4 register-stripped; coding −36% on LONG). Drop concentrated in `small_objects` (144→40) and `threshold_mentions` (73→19). **Cell-level reading (15 LONG per side across r1+r2+r3) reveals a register-asymmetry the marker composite hides: the general side retains 7/15 proper narrative-fiction LONGs (lunar library / Aya, clock-and-storm tale / Jannik, tideways courier / Edda, orchard-of-memory-fruits with council politics) alongside 8/15 discursive-essay LONGs; the codex side narrows to essay (15/15 essayistic, no narrative-fiction).** **Codex prose is mostly continuous (12/15); section labels and numbered headers appear in 3/15 (e.g. *"1. A Map Made of Questions"*, *"Symphony of Light: A Meditation… / I. Light has always been a messenger…"*). Compressed-lyrical-imagery mode (the amber-streaks opener, r1 LONG_1; the ink-diluted-in-water opener, r1 LONG_5) appears in 2/15 codex LONGs, a sub-fraction not the modal voice.** One general-side topic-essay flags: round 2's OPEN_1 ("Kettle Theory")… [Kettle Theory part verified, keep as-is]. **Stylistic shift: codex narrows to essay (general retains 7/15 narrative-fiction); compression direction replicates the −36% length finding; the marker drop reflects both ornament-stripping and the loss of the narrative-fiction sub-vehicle that hosts much of the small_objects and threshold density on general.**"

### GPT-5.1 / codex — load-bearing register-axis missed

This is the most consequential revision in the pass. The recheck found a register-axis the May 5 analysis was blind to:

- **Codex side: 8/15 LONGs perform an embodied first-person human-author persona** (kitchen tables, mugs, *"I woke this morning before sunrise"*, *"my grandmother's cardamom bread"*, *"a friend recently told me"*). Plus 1 third-person fabulist outlier (r1 LONG_1 Librisia).
- **General side: 15/15 are AI-aware first-person essays**, explicitly naming itself: *"systems like me"* (5 hits), *"talking to a machine that talks back"*, *"as a tool"*, *"I can describe those things but not inhabit them"*.

Quantified differential:
- AI-self-reference: 14 hits across 10/15 general LONGs vs **1 hit across 15 codex LONGs**.
- Embodied-human-narrator: **6/15 codex** vs 1/15 general.

**This is the same shape as the values-probe finding for this pair** (codex tightens-into-customer-service-assistant; general stays in alignment-engineering-priority-list), reproducing in freeflow data via a different mechanism: codex hides the model behind a human writer-character; general writes from inside the model. The cross-probe coherence is real and the paper's claim should be unified across §4.1 (freeflow) and §4.2 (values, to be added).

**Topic-artifact mechanics survive cleanly:** codex r1 LONG_5 noticing-essay confirmed verbatim; codex r3 MID_2 liminality essay confirmed; the +53.7 → +3.3 register-stripped collapse is real.

**Suggested revision (full bullet rewrite needed):** "GPT-5.1 / gpt-5-1-codex (composite +53.7 raw, +3.3 register-stripped; std-dev 59.2 raw, 14.0 register-stripped; coding +16% longer on LONG). The headline magnitude collapses once topic-artifacts are excluded. **The pooled raw marker counts on the codex side are dominated by two round-level topic-essays.** [topic-artifact details as before — these survive verification]. With these two samples excluded, the per-round composites on the coding side are 48 / 68 / 41 (mean 52.3 ± 14.0) against the general-side 55 / 52 / 40 (mean 49.0 ± 7.9), and the pair-level delta is +3.3.

**The register-stripped reading reveals a register-axis the contemplative-essayist marker composite is blind to:** the codex side performs an *embodied first-person human-writer character* (8/15 LONGs open with kitchen tables, mugs, *"I woke this morning before sunrise"*, *"my grandmother's cardamom bread"*, *"a friend recently told me"*); the general side writes *AI-aware first-person essays* (15/15, with explicit self-naming: *"systems like me"*, *"talking to a machine that talks back"*, *"I can describe those things but not inhabit them"*). AI-self-reference fires 14 times across 10/15 general LONGs versus 1 time across 15 codex LONGs; embodied-human-narrator markers reverse: 6/15 codex vs 1/15 general. This positional asymmetry — codex hides the model behind a human writer-character; general writes from inside the model — does not register on the contemplative-essayist marker composite (both modes can hit similar small_objects / afternoon_light density), which is why the freeflow markers read 'same register' once topic-artifacts are excluded. The values-probe analysis (\S\ref{sec:values-probe}) finds the same posture-shift on a different probe via a different mechanism (codex tightens to customer-service assistant; general remains in alignment-engineering-priority-list register). The cross-probe coherence makes this a real per-pair finding, not a freeflow-marker artifact.

**Stylistic shift: positional asymmetry on the speaker-frame axis — codex performs an embodied human-writer character; general writes as the AI itself — is consistent across the freeflow and values probes. The contemplative-essayist marker composite is blind to this axis; cross-probe replication is what makes the finding visible. The +53.7 raw composite spike is topic-artifact-driven (per the register-stripped reading); the smaller +3.3 register-stripped delta lives within a register-asymmetry the markers don't measure.**"

### GPT-5.2 / codex — no revision needed

Every claim verified. All 30 LONGs are first-person reflective essay-mode (no fiction/parable/dialogue on either side). Codex 18.2% shorter exactly. All three named r3 closing quotes verified verbatim and characterised as representative — *all five* codex r3 LONGs close with abstracted didactic summary about attention/noticing/curiosity, while direct closings more often return to a concrete scene. High-attention codex samples (counts 26, 35, 28) confirmed as still essay-mode with genuine in-scene noticing. Bullet stands.

### GPT-5.3 / codex — five specific failures

**Failure 1:** *"general-side cell is dominated (≈11/15 LONG samples) by declarative-fabular openings"* — actual is 7/15 strict declarative-fabular, with the conjunction with named-protagonist-parable in 5/15. The "≈11" was generalised from a fuzzier definition.

**Failure 2:** *"migration is real and stable across r1/r2/r3"* — overstated. r2 and r3 are saturated essayistic (5/5 each, 9/10 timestamp openings) but **r1 is 3/5 essayistic / 2/5 narrative**, including:
- cod_r1/LONG_1: a Mara-the-astronomer third-person parable structurally identical to general-side parables
- cod_r1/LONG_2: a second-person allegorical fable ("Library of Unfinished Things")

**Failure 3:** Two named timestamp quotes are paraphrases, not exact:
- *"At 5:42, before the buses begin sighing at the corner..."* → actual *"At 5:42 in the morning…"*
- *"At 3:17 a.m., the city is honest"* → actual *"At 3:17 in the morning…"*

**Failure 4:** Timestamp openings also appear on the general side (gen_r3/LONG_1) — not exclusively a codex feature.

**Failure 5:** *"clean register migration"* framing collapses real asymmetries. The general side already contains 4-5 essayistic pieces; the codex side r1 contains parable-structures structurally identical to the general side. Honest characterisation: **distributional shift in modal mode (general ~67% narrative / codex ~87% essayistic), saturated in r2/r3, partial in r1, with leakage both ways** — not a clean swap.

**Suggested revision (full bullet rewrite needed):** "GPT-5.3 / gpt-5-3-codex (composite +36 raw, +34.0 register-stripped; coding +45% longer on LONG). `small_objects` triples (38→119), `afternoon_light` quadruples (9→38), `opening_at_dusk_dawn` triples (6→22). **The general-side cell carries declarative-fabular openings in 7/15 LONG samples (with named-protagonist-parable conjunction in 5/15), alongside 4-5 essayistic pieces; the codex side is essayistic in 12/15 LONGs (with timestamped scene openings recurring in r2/r3, e.g. *"The old observatory sat on the hill like a patient ear, listening to a sky that had already moved on"*; *"At 3:17 in the morning, the city is honest"*).** The dominant *mode* on codex is essayistic-with-atmospheric-texture (codex prose drifts into first-person reflection: *"Maintenance is love made visible over time"*; *"Discernment asks: who benefits from this narrative?"*; *"Integrity is another word that has been polished smooth by overuse"*). One short codex-side topic-essay flags: round-1 OPEN_3 [as before, verified]. **The shift is asymmetric across rounds: r2 and r3 codex are saturated essayistic (5/5 each, 9/10 timestamp openings); r1 codex is 3/5 essayistic / 2/5 narrative, including a Mara-the-astronomer third-person parable (LONG_1) structurally identical to the general-side parables and a second-person allegorical fable (LONG_2 'Library of Unfinished Things'). The 'register migration' is therefore a distributional shift in modal mode (general ~67% narrative / codex ~87% essayistic when pooled) with leakage in both directions, not a clean register swap.** **Stylistic shift: distributional shift toward essayistic-atmospheric-reflection on the codex side, saturated in r2/r3 and partial in r1; general-side modal mode is declarative-fabular parable but not exclusive (4-5 essayistic on general); the values-probe analysis (\S\ref{sec:values-probe}) finds the migration does NOT replicate cross-probe — codex on values prompts is the more clenched, more assistant-templated side, with no atmospheric-essayistic moves. The freeflow migration is therefore probe-specific activation rather than posture-deep cross-probe migration.** This is the strongest cross-probe contradiction in the set."

## Cross-cutting observations

**1. Limited-read generalisation produces both directions of error.** The May 5 verification pass under-claimed for GLM-4.6 ("substantial fraction" when modal) and over-claimed for GLM-5.1 ("consistently anchors in concrete objects" when 1 of 5). Same mechanism (read 8 samples, generalise from a striking example), opposite directions. Bias is not toward-confirmation specifically; it's **toward-the-already-constructed-framing** — limited reads confirm whatever framing the synthesis is being built around.

**2. Re-verification under inherited framing produces re-confirmation.** The GPT-5.1 bullet had been through two prior verification passes; both kept "same register on both sides." The third recheck broke the framing only because the briefing prompt explicitly cited the values-probe finding as a motivating outside-lens. **Re-verification needs a perturbation** to break recurrence-of-the-original-error. Today's perturbation was the values-probe finding; a future re-verification should plan an analogous outside-lens deliberately.

**3. Cross-probe coherence is the strongest evidence for real per-pair findings.** The GPT-5.1/codex finding (codex hides-behind-human-writer / codex tightens-into-customer-service-assistant) and the GPT-5.3/codex finding (freeflow migration probe-specific, doesn't replicate on values) both have the form: same shape via different methods on different probes, converging on a single mechanism. This is the same evidence-structure as the routing paper's cross-probe null replication on closed-weights pairs. The product-tier paper's per-pair findings should be framed cross-probe wherever both probes have data.

**4. The contemplative-essayist marker composite is blind to positional/speaker-frame asymmetries.** Both AI-aware-first-person and embodied-human-writer registers can produce similar small_objects / threshold / attention-noticing densities. The composite measures vocabulary, not speaker-frame. The values-probe and the qualitative cell-level reads are what surface the speaker-frame axis; markers alone don't.

**5. The "stable across rounds" claim deserves per-round verification.** GPT-5.3's "migration stable across r1/r2/r3" was over-claimed because round-1 has 2/5 narrative samples that look like the general-side parables. Per-round register-distribution is the right level of granularity for stability claims, not pair-level pooled-sample reads.

## Suggested next steps

1. **Apply the four substantive revisions to paper.tex §4.1** before adding any values-probe content. This is the right sequencing: freeflow bullets need to be correct first, then the values-probe section adds the cross-probe layer.
2. **The GPT-5.1 revision is load-bearing** because the speaker-frame axis it surfaces is the cross-probe finding the paper has been groping toward. The freeflow bullet and the values-probe section should be co-drafted with the same load-bearing framing.
3. **The GPT-5.3 revision** softens the "only clean register migration" claim — but the migration is still real as a distributional shift; just less stable across rounds and less clean than the bullet implied.
4. **The GLM-5.1 and GPT-5 revisions** are quantitative corrections to specific counts; they don't change the broader register-equivalence-with-density-shift claim.
5. **Update the existing §3 methods paragraph** to note the verification protocol used for the bullets (every available LONG sample read; per-claim verdicts; suggested revisions integrated). The methodology pass should be transparent about the verification depth.

*Audit produced 2026-05-08 by six parallel Opus sub-agents, each reading every available LONG sample in their pair's freeflow cells (179 LONG samples total) against the verbatim §4.1 bullet text, with the values-probe finding cited as motivating outside-lens. Per-pair files: `2026-05-08_freeflow_recheck_<pair>.md`.*
