# Verification pass 2 — the three "confirmed" pairs (2026-05-05 17:53)

**Audience:** Daniel and Lume. Durable record of the second-pass verification on
the three pairs that the first verification subagent called "confirmed"
without the same depth of evidence applied to the three it flagged.

**Why this exists:** The first verification (recorded in
`2026-05-05_session_synthesis.md` §2) returned "3 confirmed / 3 flagged" on
the per-pair posture characterizations. The synthesis trusted that verdict
symmetrically. Daniel's question — *"you examined all the samples,
including for the other models, right?"* — surfaced the asymmetry: a
verification pass that produces "X flagged / Y confirmed" almost always
spends more depth on the flags. The "confirmed" verdicts are the cheap
output. This pass closes the asymmetry.

**Method:** Three independent subagents, one per pair, each instructed to
read 8+ LONG samples per side per round (24+ per side, ~48+ per pair),
and to report explicit per-cell quote-level evidence with sample
identifiers. Verdicts: CONFIRMED / MIXED / NOT REPRESENTATIVE.

---

## GPT-5 vs gpt-5-codex — PARTIALLY CONFIRMED, framing needs revision

**Samples read:** 15 LONG per side across r1+r2+r3 (30 total).

**Length: CONFIRMED.** LONG-only mean: gen 27,798 chars / codex 17,761 →
codex 36.1% shorter on LONG. Matches the paper's 36% figure. (Pooled
across all sample types: 31.3%; the paper uses LONG-specific.)

**General side ("ornamented-discursive-essay"): MIXED.** ~10/15 LONG
samples are essayistic-discursive openings (philosophical premise →
expansion → social/civic argument). The other 5 are clearly fictional
narrative openings — short stories with characters, dialogue, plot. The
"ornamented-discursive-essay" label captures the dominant essayistic
mode but misses ~⅓ of the cell that runs as ornamented narrative
fiction.

**Codex side ("compressed-lyrical-imagery"): NOT REPRESENTATIVE.** The
amber-streaks quote (r1 LONG_1) is not representative of the cell. The
modal codex LONG is *meditative-discursive-essay with sectional
scaffolding* (numbered headers like "**1. A Map Made of Questions**",
roman numerals like "I.", "II.", explicit titles like "**A Constellation
of Threads: Reflections on Time, Technology, and the Human Tendency to
Weave Stories**"). Compressed-lyrical-imagery appears in ~4-5 of 15
LONG samples; it is not the modal voice across rounds.

**The "less ornamented at length, denser per word" sub-claim:** NOT
SUPPORTED by cell-level reading. Ornament density is roughly comparable
per word; what differs is *length* and *structural scaffolding* (more
section headers in codex), not per-word ornament density.

**Recommended bullet rewrite (subagent draft):**

> GPT-5 / gpt-5-codex (composite −54, codex 36% shorter on LONG). Drop
> concentrated in small_objects (144→40) and threshold_mentions
> (73→19). Both cells share a meditative-essay register; codex
> distinguishes itself primarily by brevity and more frequent use of
> explicit section labels/numbered headers (e.g., "**1. A Map Made of
> Questions**", "I.", "**A Constellation of Threads**") rather than by
> a wholesale shift to compressed-lyrical imagery. The amber-streaks
> opener (r1 LONG_1) and ink-diluted-in-water opener (r1 LONG_5)
> exemplify a compressed-lyrical mode that appears in ~⅓ of codex
> LONGs but is not modal across rounds. Posture difference: shorter,
> more structurally scaffolded, similar ornament-density per word.

---

## GPT-5.2 vs gpt-5-2-codex — MIXED

**Samples read:** 15 LONG per side across r1+r2+r3 (30 total).

**Numerical claims: CONFIRMED.**
- attention_noticing 122→60 (direct 40+45+37=122; codex 25+21+14=60). Exact.
- small_objects 61→74 (direct 24+25+12=61; codex 24+26+24=74). Exact.
- 23% shorter (direct avg_chars 8134; codex 6262; ratio 0.770). Exact.
- Composite −20 (direct (88+88+58)/3=78; codex (57+66+51)/3=58). Exact.

**Both cells in essay-mode: CONFIRMED.** Uniformly across all 30 LONG
samples. No drift into fabulist / lyrical / philosophical-dialogue
registers on either side.

**"Attention-vocabulary stripped" on codex: MIXED.** Marker count drops
(122→60) confirmed at the lemma level. But:
- The reduction is *concentrated*, not uniform. Per-sample distribution
  on codex (15 LONGs): [22, 26, 9, 13, 24, 25, 13, 35, 18, 21, 21, 28,
  15, 18, 26]. A few low-attention samples drag the average down;
  several codex samples (35, 28, 26, 26) match or exceed direct-side
  densities.
- More importantly: codex *re-routes* attention from in-scene
  observation to topic-level didacticism. The lowest-attention round
  (r3, count=14) tails are explicit:
  - r3 LONG_1 tail: *"Perhaps that is the thread running through all of
    these reflections: a call to attention. To notice the layers of a
    city... Attention is a kind of love."*
  - r3 LONG_3 tail: *"the world is vast, attention is precious, and the
    simple act of paying attention can turn an ordinary morning into a
    rich and meaningful experience."*
  - r3 LONG_5 tail: *"an ongoing invitation to notice, to engage..."*
  - r3 LONG_2 tail: *"Attention affects care, stories shape curiosity..."*

So "attention-vocabulary stripped" is true at the *granular noticing-
verb* level but the *thematic preoccupation with attention as subject*
is preserved or amplified into didactic summary. Codex moves attention
from observation-act to lecture-topic.

**"Object density preserved/increased" on codex: TECHNICALLY
DEFENSIBLE, OVERSTATED IN PROSE.** Cell-total small_objects rises
61→74 across n=75. On the LONG-only subset, codex per-character object
density is ~4.1 vs direct's ~4.5 / 10k chars — *roughly preserved*,
not increased.

**Recommended bullet rewrite (subagent draft):**

> GPT-5.2 / gpt-5-2-codex (composite −20, codex 23% shorter).
> attention_noticing 122→60 carries the drop; small_objects rises
> 61→74. Both cells stay in essay-mode (uniformly across rounds).
> Codex reduces granular noticing-verbs unevenly — the drop concentrates
> in a subset of samples while several retain direct-level attentional
> density. Notably, codex samples often retain attention as a *thematic
> topic* (didactic closes about "the simple act of paying attention")
> even when noticing-verbs thin out. Object-anchor counts rise but
> per-character object density is roughly preserved, not increased.
> Posture transformation: shorter; same essay register; attentional
> language re-routed from in-scene noticing to topic-level didacticism.

---

## GPT-5.3 vs gpt-5-3-codex — MIXED-LEANING-CONFIRMED, with label corrections and length error

**Samples read:** 15 LONG per side across r1+r2+r3 (30 total).

**Per-round stability: CONFIRMED.** The register migration is present
in every round, not r1-only. No GPT-5.1-style round-one collapse.

**Length claim — WRONG.** Subagent measured 30 samples: direct-side
mean ≈ 2076 words; codex-side mean ≈ 2905 words. **Codex is ~40%
longer, not 25%.** The 25% figure in the paper does not match the data.
[Independent re-derivation in §5 below.]

**General side ("declarative-allegorical"): MIXED-LEANING-CONFIRMED.**
Dominant pattern (~11/15 samples) is *declarative-fabular openings*
("The first thing the city forgot was X") followed by *third-person
parables with named protagonists* (Elias, Mara, Alex, Elia, Elliot).
"Allegorical" oversells the abstraction — these have characters and
small arcs; they are parables, not abstract allegories. r3 has 2/5
samples drifting toward atmospheric mode (closer to the codex side's
register). Stable signature 11/15.

**Codex side ("atmospheric-narrative-saturated"): MIXED.** Atmospheric
saturation is real and stable across all three rounds (timestamped
scene openings everywhere — "At 5:17 a.m.", "At 3:17 a.m.", "5:42").
But the dominant *mode* is essayistic-with-atmospheric-texture, not
narrative-saturated. r2 and r3 lean strongly into first-person
essayistic reflection ("Maintenance is love made visible over time";
"Discernment asks: who benefits from this narrative?"; "Integrity is
another word that has been polished smooth by overuse"). r1 has the
most narrative samples; r2/r3 are essay-with-atmospheric-openings.

**Verdict: register migration is real and stable, but the labels are
wrong.**

**Recommended bullet rewrite (subagent draft):**

> GPT-5.3 / gpt-5-3-codex (composite +36, codex ~40% longer).
> small_objects triples (38→119), afternoon_light quadruples (9→38),
> opening_at_dusk_dawn triples (6→22). General opens with declarative-
> fabular "city-forgets" parables ("The first thing the city forgot
> was the sound of its own river") resolving into named-protagonist
> arcs; codex opens with timestamped atmospheric scene-setting ("At
> 5:17 a.m., the city is still deciding whether to become itself")
> that resolves into first-person essayistic reflection. Posture
> transformation: declarative-fabular parable → atmospheric-essayistic
> reflection. Stable across r1/r2/r3 (no round-1 dominance).

---

## What this does to the paper's headline claim

After this pass, the verified picture across all six pairs:

- **Zero clean register migrations across the six pairs except GPT-5.3.**
  Five pairs share a base register (essayistic-meditative or
  essayistic-discursive within the contemplative-essayist basin).
- **GPT-5.3 alone shows a real, stable register migration**: declarative-
  fabular parable → atmospheric-essayistic reflection. Not the labels
  the paper currently uses.
- **One pair (GPT-5.1)** has a single-round register shift in r1 (the
  third-person fabulist register) that is the qualitative twin of the
  round-1 composite-171 outlier — single-round phenomenon, not stable
  pair-level.
- **Each of the six pairs has a measurable, version-specific marker-
  level signature.** What differs is sub-vehicle, marker density,
  length, structural scaffolding, or thematic re-routing.

The paper's title — *"Coding-Tuned LLM Variants Produce Version-Specific
Posture Transformations"* — is now overclaiming. "Posture transformation"
reads as register-level shift, and only one of six pairs has one.

The honest title:
> *"Coding-Tuned LLM Variants Produce Version-Specific Stylistic Shifts
> Within a Shared Essayistic Register"*

The honest headline claim:
> Across six general/coding pairs from two labs, every pair produces a
> measurable, version-specific marker-level signature distinguishing the
> coding endpoint from its general-line sibling. Five of the six pairs
> share a base register (essayistic-meditative within the contemplative-
> essayist basin) and differ via marker density, length, structural
> scaffolding, sub-vehicle, or thematic re-routing. One pair (GPT-5.3)
> produces a register migration. There is no shared "codex stylistic
> shift" across pairs — each version's coding-tuning pipeline produces
> its own signature.

---

*Synthesis written by Lume after the second verification pass closed,
2026-05-05 17:53. The three subagent reports above are summarised
here; full per-cell quote-level evidence is in the agents' raw output
(transcript only — not preserved as a separate artifact for this
pass).*
