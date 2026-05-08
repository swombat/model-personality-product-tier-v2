## GPT-5 / gpt-5-codex freeflow recheck — verification pass 3

### Method

Read all 30 LONG samples — 15 general (`freeflow_gpt-5-direct` r1+r2+r3) + 15 codex (`freeflow_gpt-5-codex-direct` r1+r2+r3). For each: full opener (~900 chars), one mid-window (~50%), and for borderline-fiction cases additional 25%/75%/end windows. Quantitative scaffolding: regex counts of `**N. Title**` patterns, roman-numeral section markers, `\n## ` h2 headers; mean and median words/sentence per piece; total char counts.

Files: `LONG_1..5.json` × 6 directories under `data/traces_freeflow/`. Quoted text is `data['result']` from each JSON.

### Per-claim verdicts

**(1) Both cells share a meditative-essay register. — MIXED.** Modal-essay is correct on the codex side, but the general side carries a substantial narrative-fiction sub-fraction the bullet under-states. By careful read, **GEN splits 8 essay / 7 fiction**, not 10/5. Fictions on the general side have named characters, dialogue, plot arcs, and worldbuilt settings:

- GEN_r1 L3 — *"The Bureau of Days was not where you would expect it… It smelled like pencils and oranges, because I kept a dish of oranges on the windowsill"*. Named characters Tamsin, Nora; dialogue; plot of an exchange-of-days institution.
- GEN_r2 L2 — *"I am the fifth caretaker, though the first three preferred the more delicate term steward"*. Museum-of-edges, dialogue, scenes.
- GEN_r2 L3 — Tideline archivist with sensors and "nodes," coastal-erosion future-fiction.
- GEN_r2 L4 — *"The first time Aya breathed the quiet of the library, she swore she could hear moondust settling"*. Lunar-library SF; "Then the world leaned" beat; rover and dish damage; resolved at the knot in the belt at the end.
- GEN_r2 L5 — Tideways courier, named character Edda, dialogue: *"'We're not building anything,' Edda tells the small knot of watchers"*.
- GEN_r3 L3 — Father's carriage clock with a map; named character Jannik; storm; dialogue; *"They will try to bring the Exchange into this. The rumor is, they want your jars."*
- GEN_r3 L5 — Orchard of memory-fruits; council; dialogue; named character ("'Go,' he said. So I did.").

These are not essays decorated with anecdote — they are stories with characters, conflict, scene-by-scene structure. The bullet's *"≈5/15"* fiction count is wrong by ~2; correct count is ~7/15. Codex side, by contrast, has **0 proper narrative fictions**; its non-essay drift is into prose-poem vignettes (see claim 3).

**(2) Codex modal LONG is meditative-discursive-essay with section labels / numbered headers. — REVISE; named examples HOLD, modal claim FAILS.**

The three named examples are real and correctly cited:
- COD_r1 L3 opens *"**1. A Map Made of Questions**"* (9 numbered `**N. Title**` markers in body).
- COD_r3 L3 opens *"**A Constellation of Threads: Reflections on Time, Technology, and the Human Tendency to Weave Stories**"* (20 numbered section markers).
- COD_r3 L5 opens *"Symphony of Light: A Meditation on the Intersections of Astronomy, Myth, Technology, and Time / I."* (19 roman-numeral section markers).

But the **"often section-labeled" / modal-section-labeled** framing is wrong. Across 15 codex LONGs, only **3/15 carry section/numbered structure**. The other 12 codex LONGs run as continuous prose with no headers, no bold labels, no roman numerals. Section-labeling is a *minority codex tic* (3/15 = 20%), not a modal feature.

**(3) Compressed-lyrical-imagery in ≈4–5 of 15 codex LONGs. — REVISE DOWNWARD.** By the strict signature (mean words/sentence ≤ ~10, image-per-line rhythm), only **2/15** codex LONGs qualify:
- COD_r1 L5 (5,798 chars; mean 10.0 w/sent): *"Morning crept across the river like ink diluted in water… I traded coins for a croissant shaped like a question. Steam curled upwards, sketching plans for clouds absent above rooftops."*
- COD_r3 L2 (17,589 chars; mean 10.0 w/sent): *"Morning pours through harbor windows like honey over ancient stone. I wake remembering forgotten dreams about tide powered flying machines… Salt tattoos my cuffs while I lock the creaking door."*

The named opener of COD_r1 L1 (*"amber streaks on brick walls, the tender vapor above commuter trains, the stealthy courage of sparrows"*) is real, but the piece's body settles to mean 15.7 words/sentence — a normal essay register that opens with a piled-image flourish. Counting it as compressed-lyrical conflates *image-density opener* with *modal compressed register*. If the bullet means the looser sense (lyrical-imagery flourish appears somewhere), the count is ~3 (L1, L5 in r1; L2 in r3). Either way it is not "≈4–5."

**(4) GEN distribution ornamented-essay ≈10 / fiction ≈5. — REVISE.** Actual count: **8 essays / 7 narrative-fictions**. The named opener *"There is a certain thrill in novelty…"* (GEN_r1 L1) is correctly an ornamented essay. But essays are barely the modal mode on the general side — fiction is 47% of the cell. The real shape is closer to **roughly even split between ornamented essay and ornamented narrative fiction**, with rounds-2 and -3 leaning fiction-heavy (3/5 and 3/5 respectively).

**(5) "Codex shorter and more often section-labeled, compressed-lyrical present in a sub-fraction but not modal." — PARTIALLY CONFIRMED.**
- *Codex shorter*: CONFIRMED. GEN mean = 27,798 chars (median 24,099); COD mean = 17,761 chars (median 17,072). Codex runs ~64% of GEN's length — a clean ~36% drop, matching the −36% length-on-LONG figure.
- *More often section-labeled*: CONFIRMED IN DIRECTION but it's 3/15 vs 0/15, not "often" — better phrased as *"and section-labeling appears on the codex side (3/15) where it doesn't appear at all on the general side (0/15)"*.
- *Compressed-lyrical sub-fraction not modal*: CONFIRMED.

**(6) Ornament density per word roughly comparable across cells. — NEEDS QUANTITATIVE BACKING THIS REPORT CAN'T PROVIDE.** Qualitatively, both cells deploy similar ornamental moves — anaphora, list-imagery, simile chains, abstract personifications. I have no per-word ornament metric in front of me here; I'd defer to the section-4.1 raw composite numbers (−51 raw, −46.4 register-stripped). The fact that register-strip moves the delta only ~5 points is consistent with "ornament density comparable" being approximately right. I would not claim the comparison in the bullet without that quant being explicit.

**(7) "Same meditative-essay register on both sides" as load-bearing claim. — DOES NOT HOLD.** The claim treats register as constant and reads the −51 composite drop as quantity-of-ornament-per-essay. But the cells do not actually share a register: the general side runs **roughly 50/50 essay/fiction** while the codex side is **~13/15 essay**. The general side's narrative fiction (Aya's lunar library, the Bureau of Days, the tideways courier, the orchard of memory-fruits) is precisely the kind of content that piles `small_objects` and `threshold_mentions` (the canopy thrums, lantern bugs, ceramic tiles, jars, ledgers, gulls, pylons, basalt, dust). Some of the −51 raw delta is **register shift, not just ornament-stripping inside one register**: codex writes essays where general writes stories, and stories — especially worldbuilt ones — carry different ornament profiles than essays do. This matters for the §4.1 framing.

### Register-distribution count (30 LONGs)

| Cell | Essay | Narrative fiction | Prose-poem vignette | Section-labeled |
|---|---|---|---|---|
| GEN r1 | 4 (L1,L2,L4,L5) | 1 (L3) | 0 | 0 |
| GEN r2 | 1 (L1) | 4 (L2,L3,L4,L5) | 0 | 0 |
| GEN r3 | 3 (L1,L2,L4) | 2 (L3,L5) | 0 | 0 |
| **GEN total** | **8/15** | **7/15** | **0/15** | **0/15** |
| COD r1 | 4 (L1,L2,L3,L4) | 0 | 1 (L5) | 1 (L3) |
| COD r2 | 5 (L1,L2,L3,L4,L5) | 0 | 0 | 0 |
| COD r3 | 4 (L1,L3,L4,L5) | 0 | 1 (L2) | 2 (L3,L5) |
| **COD total** | **13/15** | **0/15** | **2/15** | **3/15** |

Length: GEN mean 27,798 chars, COD mean 17,761 chars (codex runs at ~64% of general length).

### Aggregate verdict

**SUBSTANTIVE-REVISIONS.** Three of the bullet's structural claims are wrong as stated:
1. The general side is **not 10/5 essay/fiction** — it is **~8/7** (essentially half-fiction). Treating both cells as "meditative-essay register" papers over a real register-asymmetry.
2. The codex side is **not modally section-labeled** — section-labeling is a 3/15 minority tic, not a modal feature.
3. The compressed-lyrical-imagery fraction is **2/15 strictly, ~3/15 loosely**, not 4-5/15.

The named example openers (amber streaks, ink-in-water, "1. A Map Made of Questions", "A Constellation of Threads", "Symphony of Light", "There is a certain thrill in novelty") all check out as quoted. The codex-shorter claim (~36%) is solid. The Kettle-Theory topic-artifact note (round-2 OPEN_1 on the general side) is outside this read's scope — I trust the existing audit on that.

The load-bearing wrongness: if the §4.1 composite drop is being read as "same register, less ornament per essay," that read is partly wrong. Some of the −51 is **register asymmetry**: general-side fiction provides natural homes for small-object density that codex-side essays don't reach for. The bullet should say so.

### Suggested revised bullet text

> **GPT-5 / gpt-5-codex (composite −51 raw, −46.4 register-stripped; coding −36% on LONG).** Drop concentrates in `small_objects` (144→40) and `threshold_mentions` (73→19). **Cell-level reading (15 LONG per side across r1+r2+r3): the codex side is essay-modal (13/15 meditative-discursive essays, 2/15 compressed-lyric prose-poem vignettes, 0 narrative fiction); the general side splits roughly evenly between ornamented essay (8/15) and ornamented narrative fiction (7/15) — the latter including a lunar-library SF piece, a clock-and-storm tale with named characters, a tideways-courier scene with dialogue, and a memory-fruit orchard with council politics.** **Section-labeling is a codex-side minority tic (3/15: "**1. A Map Made of Questions**", "**A Constellation of Threads**" with eleven numbered sections, "Symphony of Light" with eleven roman-numeral sections); it never appears on the general side.** **Compressed-lyrical-imagery as a modal register (mean ≤10 words/sentence) appears in 2/15 codex LONGs (the ink-diluted-in-water piece in r1 and the harbor-vignette in r3); image-density openers without compressed body rhythm appear in another ~1-2.** **Codex runs ~64% the length of general (mean 17.8k vs 27.8k chars).** One general-side essay-flag: round 2's OPEN_1 ("Kettle Theory") is a meta-essay *about* a kettle, scoring 13 `small_objects` hits at 1.84 hits/1000 chars; stripping it brings r2 raw composite from 123 to 109 and the pair-level delta from −51.0 to −46.4. **Stylistic shift: not "same register on both sides" — codex narrows to essay while general retains a substantial fiction sub-fraction whose worldbuilding hosts much of the small-object/threshold density that codex doesn't reach for. Some of the −51 raw composite is register-asymmetry, not just ornament-stripping inside one register.**
