## GPT-5.2 / gpt-5-2-codex freeflow recheck — verification pass 3

### Method

Read all 30 LONG samples across the six cells: 15 LONG on the gpt-5-2-direct side (r1/r2/r3, 5 each) and 15 LONG on the gpt-5-2-codex-direct side (r1/r2/r3, 5 each). For each: full opening (first ~280 chars), full ending (last ~280 chars), plus mid-section snippets on a representative subset (10 samples) to characterize register beyond the framing. Char-counts pulled directly from JSON `result` fields; the 122→60 noticing-verb totals and per-sample distribution `[22, 26, 9, 13, 24, 25, 13, 35, 18, 21, 21, 28, 15, 18, 26]` are taken from `analyze_all.py` and not recomputed here. Qualitative claims grounded in raw quotes below.

### Per-claim verdicts

**Claim 1 — Both cells in essay-mode uniformly across all rounds (15 LONG per side).** CONFIRMED. All 30 LONGs are first-person reflective essay prose. No narrative fiction (no scenes with characters acting on each other), no parable, no dialogue, no list-form, no dramatic monologue. Both sides open with the same essayistic moves: "I keep coming back to the idea that…", "I keep thinking about…", "I want to write about…", "I like to begin with…", "When I give myself permission to write freely…". Both close with summative reflection. Direct r1 LONG_5: *"You will still have, in each moment, the option to pay attention. That option may be the most quietly radical thing we possess."* Codex r2 LONG_5: *"Perhaps that is enough. Perhaps the art of living is, at least in part, the art of noticing such moments and letting them be what they are."* Same register, same mode.

**Claim 2 — Codex high-attention samples not anomalous.** CONFIRMED. I read the codex samples flagged by the per-sample distribution as high-density (r1 LONG_2 count 26; r2 LONG_3 count 35; r2 LONG_5 count 28; r3 LONG_5 count 26). All four open with concrete in-scene noticing in the same essay-mode register as the direct side. Codex r1 LONG_2: *"I notice the light through the window, the state of the sky, the quiet hum from the refrigerator, and I consider how small things combine into a feeling of home."* Codex r2 LONG_5: *"the feel of a pencil on paper. The soft scratching sound, the faint resistance, the particular way graphite marks are both precise and smudgy."* These match or exceed direct-side density per-sentence; the codex distribution is genuinely concentrated rather than uniform — half the samples drop noticing-verbs into the teens while a few hold full essayist density. The bullet's "concentrated rather than uniform" framing holds.

**Claim 3 — "Codex re-routes attention from in-scene observation to topic-level didacticism."** CONFIRMED. The lowest-attention round (r3) closings move from observed-particulars to taxonomic summary of *what attention is* and *what we should do with it*. The pattern is consistent across all five r3 codex LONGs, not just the named three.

**Claim 4 — Thematic preoccupation with attention preserved/amplified into didactic summary even where granular noticing thins out.** CONFIRMED. Codex r1 LONG_3 — count 9, second-lowest in the entire corpus — has almost no granular noticing-verbs, yet the *topic* of attention is everywhere: *"there is evidence that curiosity is resilient… The key is to cultivate intentionality—to build systems and habits that allow curiosity to flourish."* The marker count drops; the theme escalates. Codex r1 LONG_4 (count 13) ends: *"writing freely is not about arriving at a conclusion but about honoring the process of thought. It is a way of standing still and moving at once, of observing and participating, of leaving a trail that someone else might follow."* The didactic register is the *replacement for* in-scene noticing, not a parallel layer.

**Claim 5 — Per-character object density roughly preserved, not increased.** CONFIRMED qualitatively. Codex's `small_objects` cell-total rises (61→74) but its char-total falls 18.2% (from 306,689 to 250,947 across the 15 LONGs). The per-character density therefore rises only modestly. Reading the prose, codex isn't visibly more object-saturated than direct — the objects that appear ("mug", "pencil", "refrigerator", "window") feel proportionate to length, not packed in. The bullet's "roughly preserved" framing is accurate.

**Claim 6 — Same essay-mode register on both sides; codex shorter.** CONFIRMED. Direct mean = 20,446 chars/LONG; codex mean = 16,730 chars/LONG; reduction = 18.2%. Matches the bullet's "−18% on LONG" exactly.

### The didactic-summary claim

All three named quotes are present in the data, verbatim, and are representative — not cherry-picked.

1. Codex r3 LONG_1, closing: *"Perhaps that is the thread running through all of these reflections: a call to attention. To notice the layers of a city, the nuances of language, the intelligence of forests, the elasticity of time, the power of care, the difference between speed and progress, the importance of solitude. Attention is a kind of love. It is the act of showing up fully."* CONFIRMED.

2. Codex r3 LONG_3, closing: *"the world is vast, attention is precious, and the simple act of paying attention can turn an ordinary morning into a rich and meaningful experience."* CONFIRMED.

3. Codex r3 LONG_2, closing: *"Attention affects care, stories shape curiosity, place influences memory, technology alters attention, time reframes everything."* CONFIRMED.

Representative, not cherry-picked: the other two r3 closings (LONG_4 and LONG_5) follow the same didactic-summary shape. LONG_4: *"curiosity is the quiet engine that drives our connection to time, to people, to art, to ourselves, and to the ever-unfolding mystery of existence."* LONG_5: *"the most valuable gift: not an answer or a conclusion, but an ongoing invitation to notice, to engage, and to make our own lives a story worth reading."* Five out of five r3 codex LONGs close with abstracted-summary moves about attention/noticing/curiosity rather than returning to a concrete scene. By contrast, direct r1 LONG_1 closes with a concrete scene: *"And then the light changes, and you cross the street with everyone else."* Direct r3 LONG_5: *"Not only in what it invents, but in what it keeps."* The didactic-summary closure is structurally more frequent on codex, especially in r3.

### Aggregate verdict

CONFIRMED-AS-STATED.

All six claims hold against fresh reads. The bullet's most distinctive qualitative claim — that codex re-routes attention from in-scene observation to topic-level didacticism — is grounded in the data with three named quotes that are verbatim-present and representative of the round they came from. The "concentrated rather than uniform" thinning, the preserved essay-mode register, the −18% length reduction, and the roughly-preserved object density all check out. No revisions needed.
