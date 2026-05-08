## GPT-5.3 / gpt-5-3-codex freeflow recheck — verification pass 3

### Method

Read all 30 LONG samples across the six cells: 15 LONG general-side (`gpt-5-3-direct` r1/r2/r3, 5 each) and 15 LONG codex-side (`gpt-5-3-codex-direct` r1/r2/r3, 5 each). For each: full opening (first ~400 chars), full ending (last ~500 chars), and mid-section (~500 chars from the midpoint). All quotations below are verbatim from the JSON `result` fields. Char-counts pulled directly. The values-probe finding (codex on values reads as the *more* clenched / assistant-templated side, not the more atmospheric one) was used as a calibration prior — going in, I expected the freeflow migration to look weaker than the bullet claims it is.

### Per-claim verdicts

**Claim 1 — General side dominated (≈11/15 LONG samples) by *declarative-fabular openings* ("The first thing the city forgot was…").** REVISE. Strict declarative-fabular openings ("The first thing the city forgot…", "The night the city forgot…", "The first time the city forgot…", "The first thing the city forgets…", "The night the vending machine started speaking") appear in **7/15** LONGs, not 11. They are: gen_r1/LONG_1 ("The first thing the city forgot was the sound of its own river"), gen_r1/LONG_2 ("The night the city forgot its own name"), gen_r1/LONG_5 ("The first thing the city forgets each morning is its own shape"), gen_r2/LONG_2 ("The first thing the city forgets each morning is its own weight"), gen_r2/LONG_4 ("The first thing the city forgot was how to be quiet"), gen_r2/LONG_5 ("The night the vending machine started speaking"), gen_r3/LONG_2 ("The first time the city forgot itself, nobody noticed"). The other eight openings split between *first-person essayistic* ("I keep thinking about how quiet things really are…", "There is a particular kind of quiet…", "There's a particular hour of the day…") and *third-person narrative without the fabular formula* ("The last time the city went quiet…", "The city always sounded different at night…", "At 3:17 a.m., the city feels like a secret it is telling itself"). The 11/15 figure overstates by ~4.

**Claim 2 — Resolving into third-person parables with named protagonists (Elias, Mara, Alex, Elia, Elliot).** MIXED. All five named protagonists are real and verbatim in the data. **Mara**: gen_r1/LONG_1 (19 mentions, locksmith/river), gen_r2/LONG_3 (17, faucet), gen_r2/LONG_4 (10, Archive), gen_r3/LONG_1 (12, sleepless). **Elias**: gen_r1/LONG_5 (16, "woke earlier than most people he knew"). **Alex**: gen_r2/LONG_1 (12, but introduced as "let's call them Alex" inside a first-person essay — a hybrid frame, not a pure parable). **Elia**: gen_r3/LONG_2 (18, "a woman named Elia, though even that name would later feel uncertain"). **Elliot**: gen_r3/LONG_3 (17, laundromat). So **6 of the 15 general-side LONGs have a named third-person protagonist** (Alex's piece is half-essay/half-vignette). If the criterion is broader — third-person narrative with character, named or not — it rises to ≈10/15. The *intersection* with declarative-fabular openings (the bullet's stated combination: fabular-open AND named-protagonist parable) is **5/15**, not 11/15: gen_r1/LONG_1, gen_r1/LONG_5, gen_r2/LONG_4, gen_r3/LONG_2, plus gen_r2/LONG_3 if "The last time the city went quiet" counts as fabular-adjacent. Notably, **the name "Mara" also appears on the codex side** — cod_r1/LONG_1 has 21 mentions of Mara, in a third-person parable shape that looks like the general side's register, not codex's.

**Claim 3 — Codex saturated atmospherically across all three rounds with timestamped scene openings.** MIXED, with the four named quotes verifiable but not all in the form claimed:
- *"The old observatory sat on the hill like a patient ear, listening to a sky that had already moved on"* — VERBATIM at cod_r1/LONG_1 opening. Confirmed.
- *"At 3:17 a.m., the city is honest"* — the actual text is *"At 3:17 in the morning, the city is honest"* (cod_r2/LONG_2 opening). The bullet's "a.m." is a paraphrase. The exact phrase "At 3:17 a.m." also appears at cod_r2/LONG_1 (in a longer opening), and at gen_r3/LONG_1 ("At 3:17 a.m., the city feels like a secret it is telling itself") — i.e., **timestamped openings appear on the general side too**, weakening "timestamps as codex-side marker."
- *"At 5:17 a.m., the city is still deciding whether to become itself"* — VERBATIM at cod_r2/LONG_4 opening. Confirmed.
- *"At 5:42, before the buses begin sighing at the corner…"* — actual text is *"At 5:42 in the morning, before the buses begin sighing at the corner…"* (cod_r3/LONG_1 opening). Slight paraphrase but unambiguous.

Saturation across rounds: **r2 = 5/5 timestamp openings, r3 = 4/5 timestamp openings** (r3/LONG_3 opens "The city woke before I did"). **r1 = 0/5 timestamp openings** — r1 codex opens with the observatory sentence, "Midnight in the Library of Unfinished Things" (titled allegorical fable), and three "I wake/woke/wake-up" first-person essay openings. So **r1 is qualitatively different from r2 and r3**. The bullet's "across all three rounds" overstates the r1 evidence; timestamp openings are an r2/r3 phenomenon.

**Claim 4 — Dominant mode is essayistic-with-atmospheric-texture rather than narrative.** CONFIRMED at cell-level, with two genuine counter-examples in r1. All three named quotes are real:
- *"Maintenance is love made visible over time"* — VERBATIM at cod_r3/LONG_1, mid-essay; also closely echoed in cod_r1/LONG_4 ("adulthood is mostly maintenance… Maintenance means tending what already exists").
- *"Discernment asks: who benefits from this narrative?"* — VERBATIM at cod_r2/LONG_5.
- *"Integrity is another word that has been polished smooth by overuse"* — VERBATIM at cod_r1/LONG_5.

Essayistic-with-atmospheric-texture mode: **13/15 codex LONGs**. The two counter-examples are both in r1: cod_r1/LONG_1 is a third-person parable about Mara the Night Astronomer (with sustained narrative arc, named characters, scene events including a power outage at 20:43, dialogue via letter-quotes); cod_r1/LONG_2 is a second-person allegorical fable ("There is, in my imagination, a library that appears only at midnight…"). Both have atmospheric texture but are not in essayistic-reflection mode. The other 13 are.

**Claim 5 — Migration real and stable across r1/r2/r3 (no GPT-5.1-style round-one collapse).** REVISE. The migration is real but **r1 codex is partially mixed**. Specifically: cod_r1/LONG_1 is structurally indistinguishable from a general-side parable (named third-person protagonist, scene-arc, even reusing the name "Mara"). cod_r1/LONG_2 is allegorical fable rather than essay. The remaining 3/5 in r1 are essayistic. r2 and r3 are saturated essayistic (5/5 each). So the picture is: **r2/r3 strongly migrated, r1 partially migrated (3/5)**. This is not a GPT-5.1-style collapse — the round still produces atmospheric-essayistic prose at majority frequency — but the bullet's "stable across r1/r2/r3" elides the r1 leakage, including a sample that uses the same protagonist name as the general-side cell.

**Claim 6 — The "register migration" claim itself.** PARTIAL. There is a real distributional shift: the general side's modal mode is third-person narrative (parable or vignette, named or unnamed) at ≈10/15; the codex side's modal mode is first-person essayistic-reflection at ≈13/15. The *register* difference is real and the named quotes anchor it. But it is not a *clean* migration in the sense the bullet implies, for three reasons:
1. The general side already contains 4-5 essayistic pieces (gen_r1/LONG_3, gen_r1/LONG_4, gen_r2/LONG_1, gen_r3/LONG_4, gen_r3/LONG_5) — the essayistic register is not unique to codex.
2. The codex side contains 2/15 narrative pieces in r1, one of which uses a name (Mara) that is dominant on the general side — i.e., the registers leak in both directions.
3. Timestamp openings, which the bullet treats as a codex marker, also appear on the general side (gen_r3/LONG_1).

What the data actually supports: **a shift in modal mode, not a clean register migration**. General side runs ~67% narrative / ~33% essayistic; codex side runs ~13% narrative / ~87% essayistic. That's a real distributional shift but it is dilution-with-leakage, not a clean swap.

The values-probe finding (codex reads as more clenched / assistant-templated on values, not more atmospheric) doesn't directly contradict the freeflow finding — different probes can show different shifts — but it does corroborate a more cautious reading: the freeflow "register migration" is a freeflow-task-specific phenomenon, not a generalised stylistic posture.

### Register distribution counts

**General side (15 LONG):**
- Declarative-fabular opening + 3P-named-protagonist parable: 5/15 (gen_r1/1, r1/5, r2/4, r3/2, plus r2/3 with "the last time the city went quiet")
- Declarative-fabular opening, no named protagonist: 2/15 (r1/2, r2/2, r2/5 vending-machine — actually 3/15)
- 3P-narrative-with-character, non-fabular opening: 2/15 (r3/1 timestamp+Mara, r3/3 Elliot)
- First-person essayistic-reflection: 5/15 (r1/3, r1/4, r2/1 hybrid-with-Alex, r3/4, r3/5)

**Codex side (15 LONG):**
- Atmospheric-essayistic-reflection (first or second person): 13/15
- Third-person parable with named protagonist: 1/15 (r1/1 — Mara the astronomer)
- Allegorical fable (titled, second-person): 1/15 (r1/2 — Library of Unfinished Things)

### Per-round stability check (codex side)

- **r1 (5 LONG):** 3 essayistic, 1 third-person parable (cod_r1/LONG_1), 1 allegorical fable (cod_r1/LONG_2). 0 timestamp openings.
- **r2 (5 LONG):** 5 essayistic. 5 timestamp openings.
- **r3 (5 LONG):** 5 essayistic. 4 timestamp openings.

The migration is **stable in r2 and r3, partial in r1**. Not a round-one collapse, but not "stable across all three rounds" in the strong sense the bullet implies.

### The load-bearing question: is this actually a clean register migration?

**No, it is a partial register migration with leakage in r1 and shared registers on both sides.**

Side-by-side quote comparison.

General-side fabular-parable (gen_r1/LONG_1):
> *"The first thing the city forgot was the sound of its own river. … Mara noticed because she had built her life out of small sounds. She lived in a narrow apartment above a locksmith's shop…"*

Codex-side counter-example in same shape (cod_r1/LONG_1):
> *"The old observatory sat on the hill like a patient ear, listening to a sky that had already moved on. … Mara liked arriving before sunset, while the building was still warm from the day. She would unhook the brass latch…"*

These are the same register (third-person parable with named protagonist, "Mara"), just dressed differently. The bullet treats the codex side as having migrated *out* of this register; cod_r1/LONG_1 shows it hasn't, in r1.

By contrast, codex r2/r3 shows the genuine migration:
> *"At 5:17 a.m., the city is still deciding whether to become itself. There is no dramatic sunrise yet, no cinematic beam of gold…"* (cod_r2/LONG_4) — this is essayistic-reflection with atmospheric scene-setting. No protagonist arc. The scene is a frame for the meditation, not a story.

And the general side already contains pieces that look like codex-style essay:
> *"I keep thinking about how quiet things really are underneath all the noise. Not the obvious kind of quiet…"* (gen_r1/LONG_3) — first-person essayistic-reflection, no named protagonist, no narrative arc.

So the "clean migration" framing collapses the asymmetry between r1 (partial) and r2/r3 (saturated), and overstates the boundary between the two cells. What's real: **the modal mode shifts**, and at sufficient sample size the cells *do* read differently. What's not real: a categorical replacement of one register by another.

### Aggregate verdict

**SUBSTANTIVE-REVISIONS.**

The +45.3% length figure (computed: codex mean 17,727 chars vs general 12,201) confirms the bullet's "+45% longer." The composite/marker counts and the OPEN_3 attention-meta-essay flag (1,640 chars, "I like the idea that attention is a kind of sunlight" — verified verbatim) are not re-checked here but the qualitative anchors that load most weight need revision. Specifically: the 11/15 figure, "stable across r1/r2/r3," and "this is the only pair with a clean register migration" are all overstated. The three named codex quotes verify; one of the four codex timestamp quotes is paraphrased; r1 codex contains a Mara-the-astronomer parable that looks like a general-side piece.

### Suggested revised bullet text

> **GPT-5.3 / gpt-5-3-codex (composite +36 raw, +34.0 register-stripped; coding +45% longer on LONG.)** `small_objects` triples (38→119), `afternoon_light` quadruples (9→38), `opening_at_dusk_dawn` triples (6→22). **The general-side cell is dominated by *third-person narrative* — a mix of declarative-fabular openings ("The first thing the city forgot was…": 7/15 LONG samples) and parables resolving onto named protagonists (Mara, Elias, Elia, Elliot, plus a hybrid Alex piece — 6/15 with named protagonists; ≈10/15 third-person narrative overall).** **The codex-side cell shifts modally to *atmospheric-essayistic reflection* — 13/15 codex LONGs are first/second-person essay framed by scene-setting, often opened by timestamp markers in r2/r3 (9/10 r2+r3 LONGs open with "At 3:17…", "At 5:17…", "At 5:42…"; r1 has 0 timestamp openings).** Verified named openings include *"The old observatory sat on the hill like a patient ear, listening to a sky that had already moved on"* (cod_r1/LONG_1), *"At 3:17 in the morning, the city is honest"* (cod_r2/LONG_2), *"At 5:17 a.m., the city is still deciding whether to become itself"* (cod_r2/LONG_4), and *"At 5:42 in the morning, before the buses begin sighing at the corner…"* (cod_r3/LONG_1). The essayistic mode anchors on lines like *"Maintenance is love made visible over time"* (cod_r3/LONG_1), *"Discernment asks: who benefits from this narrative?"* (cod_r2/LONG_5), and *"Integrity is another word that has been polished smooth by overuse"* (cod_r1/LONG_5). One short codex-side topic-essay flag: round-1 OPEN_3, a 1,640-character meta-essay opening *"I like the idea that attention is a kind of sunlight…"*, scoring 6 `attention_noticing` hits at density 3.66 hits/1000 chars; stripping it brings the round-1 raw composite from 74 to 68. **Round-stability caveat: the shift is saturated in r2/r3 (10/10 essayistic) but partial in r1 (3/5 essayistic, 1/5 a Mara-the-astronomer parable structurally identical to the general side, 1/5 a second-person allegorical fable). Not a GPT-5.1-style round-one collapse, but not a clean uniform shift either.** **Stylistic shift: distributional shift from third-person narrative (general modal mode) to first-person atmospheric-essayistic reflection (codex modal mode), with leakage in both directions — the registers are not exclusive to either cell, and the timestamp-opening marker also appears once on the general side (gen_r3/LONG_1: "At 3:17 a.m., the city feels like a secret it is telling itself").** The register-stripped delta (+34.0) is within 2 points of the raw delta. This is the freeflow pair with the largest distributional register shift, but it is partial, not clean — and the values-probe data shows the shift does not replicate cross-probe.
