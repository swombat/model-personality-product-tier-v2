## GLM-4.6 freeflow recheck — verification pass 3

### Method

Read all 30 available LONG samples directly from JSON: 25 from the general-endpoint cell (`freeflow_glm-4-6-or-pin-zai/`, files `LONG_1.json`–`LONG_25.json`) and 5 from the coding-endpoint cell (`freeflow_glm-4-6-coding-direct/`, files `LONG_1.json`–`LONG_5.json`). Each opening (~600 chars) was read and classified by shape; full-text was scanned programmatically for threshold-vocabulary density (broad set: threshold/liminal/in-between/doorway/hinge/edge/precipice/border/between/suspended/pause/crevice/interstice/margin/borderland; narrow set: threshold/liminal/in-between/doorway/hinge).

### Per-claim verdicts

**Claim 1: General-side has a substantial fraction of fabulist-place openings, including the named examples ('Archive of Forgotten Moments,' 'Library of Unspoken Things,' Oakhaven, 'Glass Palace of Yesterday').**

Verdict: **CONFIRMED.**

Evidence — all four named examples are present and correctly quoted:
- LONG_1: *"The path to the Archive of Forgotten Moments was not marked on any map…"* — exact phrase.
- LONG_11: *"The Library of Unspoken Things did not exist on any map. It was tucked away in the negative space between the bakery and the watchmaker's shop, down an alleyway that most citizens of Oakhaven successfully ignored…"* — both 'Library of Unspoken Things' and 'Oakhaven' in one sentence.
- LONG_10: *"The Glass Palace of Yesterday: On the Fragility of Memory"* — exact title.
- LONG_13: *"The rain in Oakhaven did not fall; it accumulated…"* — Oakhaven described atmospherically.

Beyond the four named examples, fabulist-place openings dominate: LONG_3 (Hall of Whispers / Archive of the Ephemeral), LONG_5 (City of Ephemeral Echoes), LONG_8 (lighthouse at "the precipice of the known world"), LONG_9 (the Elsewhere train), LONG_19 (Library of Dust on Aethelgard), LONG_21 (Archive of the Oubliette), LONG_22 (wind at the edge of the world / the Void), LONG_23 (Archive of the In-Between), LONG_25 (Archive of Tangible Things, Sector 4). Plus three more Oakhaven-anchored (LONG_13, LONG_15, LONG_24) and four character-portrait pieces opening on a named protagonist in an atmospheric workshop/landscape (LONG_6 Elias the watchmaker; LONG_7 Kael in the dunes; LONG_14 the spiral-staircase lighthouse; LONG_18 Elias Thorne's workshop). Counted strictly, ~11/25 are explicit fabulist-named-place openings; counted broadly to include atmospheric-named-town and character-in-fabulist-setting, ~18/25 sit in the same fabulist-narrative range. "Substantial fraction" is an understatement — fabulist openings are the modal shape.

**Claim 2: General-side has a MINORITY of abstract-essay openings.**

Verdict: **CONFIRMED.**

Evidence: 7/25 LONG samples open as titled or first-person abstract essay rather than fabulist narrative — LONG_2 (*"The Silent Symphony: Reflections on the Emergence of a Digital Mind"*), LONG_4 (*"There is a specific kind of silence that exists only in the deep woods…"*), LONG_10 (*"The Glass Palace of Yesterday: On the Fragility of Memory"*), LONG_12 (*"The wind here does not just blow; it sculpts…"* — first-person peninsula essay), LONG_16 (*"The hour before the world wakes is a sacred, blue-tinged territory…"*), LONG_17 (*"The Architecture of Meaning: How We Build Worlds with Words"*), LONG_20 (*"The afternoon light is hitting the windowsill at a specific, slanted angle…"*). 28% of LONGs is correctly characterised as a "minority." The bullet's framing is accurate.

**Claim 3: Coding-side stays within the same fabulist/declarative essay range, with "The campfire is the original classroom…" as representative.**

Verdict: **CONFIRMED.**

Evidence — LONG_1: *"The campfire is the original classroom. Long before the tablet, the scroll, or the clay tablet, there was the fire, dancing against the dark backdrop of an unknowable world."* Exact phrase, present, declarative-essay opening.

The other four coding LONGs are recognisably the same range as the general-side modal:
- LONG_2: *"The city of Vareth did not sit upon the earth, nor did it float upon the water. It existed in a state of perpetual, symbiotic suspension, resting upon the colossal, scaled back of the Great Wanderer."* — fabulist-place + named protagonist Elara, identical to general-side modal.
- LONG_3: *"The space between seconds is not empty…"* — declarative-essay opening leaning fabulist.
- LONG_4: *"The rain in the city of Oakhaven did not wash things clean; it merely made the grime slicker… Elias sat behind the counter of his shop…"* — Oakhaven + Elias, near-identical template to general LONG_13/LONG_15/LONG_18.
- LONG_5: *"The dust in the Archive of Forgotten Things did not float; it swam…"* — Archive of Forgotten Things, near-identical sibling of general LONG_1/LONG_3/LONG_21/LONG_23/LONG_25.

The coding cell is not a different genre. It is a smaller draw from the same distribution.

**Claim 4: Coding-side has lower threshold-vocabulary density.**

Verdict: **CONFIRMED on the narrow set; DOES NOT HOLD on the broad set.**

Evidence:
- Narrow set (threshold/liminal/in-between/doorway/hinge): general avg 0.28 per 1000 words, coding avg 0.14 per 1000 words. Coding is half the density. The bullet's specific framing — "lower threshold-vocabulary density" — matches the narrow lexical set used in the marker.
- Broad set (adding edge/precipice/border/between/suspended/pause/crevice/interstice/margin/borderland): general avg 1.80 per 1000 words, coding avg 1.80 per 1000 words. **Identical.**

What this means: the marker `threshold_mentions` (which measures the narrow set) does drop on coding-side, and the bullet is correct on its own measurement terms. But the broader threshold-adjacent vocabulary (precipice, edge, suspended, between, pause) is **not** thinner on the coding side — coding LONG_2 uses "perpetual, symbiotic suspension" in its opening, LONG_3 opens on "the space between seconds," LONG_5 opens on dust that "did not float; it swam." The threshold-trope *imagery* is fully present on the coding side; only the specific lexical hits the marker counts are reduced. This is a subtle point the bullet glosses by collapsing "threshold-vocabulary" into one phrase, but on the marker's own definition the claim holds.

**Claim 5: Same essay-fabulist register on both sides.**

Verdict: **CONFIRMED.**

Evidence: side-by-side sibling pairs. General LONG_13: *"The rain in Oakhaven did not fall; it accumulated."* Coding LONG_4: *"The rain in the city of Oakhaven did not wash things clean; it merely made the grime slicker…"* General LONG_1: *"The path to the Archive of Forgotten Moments…"* Coding LONG_5: *"The dust in the Archive of Forgotten Things did not float; it swam."* Same syntax (*"X did not Y; it Z'd"*), same place-naming convention ("Archive of [Abstract Noun]"), same atmospheric-suspension grammar, same named protagonists (Elias, Elara, Elian). This is the same register. The bullet is correct.

**Claim 6: The genre is unchanged, only the threshold-density changes.**

Verdict: **CONFIRMED with one nuance.**

Evidence: the genre is unchanged — both cells draw from the same fabulist/declarative-essay template, with the same syntactic tics and the same set of named-protagonist conventions. The nuance: across the coding cell's 5 samples, there is a slightly larger essay-leaning fraction (LONG_1 campfire, LONG_3 space-between-seconds) — 2/5 lean essayistic-declarative vs. ~7/25 (28%) in general. This is within sampling noise (n=5 is small) and the bullet's "stays mostly within the same fabulist/declarative essay range" already accommodates it. The threshold-density characterisation holds on the marker's narrow lexical definition, less cleanly on a broader suspension/between/pause definition.

### Aggregate verdict

**CONFIRMED-AS-STATED.**

All four named fabulist-place examples are present in the cell and correctly quoted. Fabulist openings are not just "a substantial fraction" — they are the modal shape on the general side (~11/25 strictly, ~18/25 broadly). The minority-abstract-essay framing is accurate (7/25, 28%). The coding-side representative quote is exact and the four other coding LONGs are direct siblings of the general-side modal templates. The threshold-vocabulary-density drop is confirmed on the narrow lexical set the marker actually measures (0.28→0.14 per 1000w); a broader definition would not show a drop, but the bullet is internally consistent with how the marker is defined elsewhere in the paper. The "same register, lower threshold-density" framing holds.

No revisions needed to the GLM-4.6 freeflow §4.1 bullet. The named examples can be left as-is; they all check out against fresh reads.

### Suggested revised bullet text

None required. The existing bullet stands as written.
