# Internal audit synthesis — 2026-05-05

**Audience:** Daniel and Lume (not for the paper). This file captures the
state of three review threads at the close of the 2026-05-05 working
session, as the basis for deciding (a) what substantive paper edits to
ship and (b) whether v1 needs an erratum, a major revision, or a
retirement note.

The findings below come from two sub-agent passes (a v1 audit and a
per-pair posture verification) plus a WebFetch confirmation of Z.ai's
direct API. Sub-agent reports themselves are not preserved verbatim
here — this is Lume's session-end synthesis. The intent is "be clear
about it ourselves first," per Daniel's directive.

---

## 1. v1 audit — what survives, what softens, what breaks

The v1 paper (*Convergent Form, Divergent Voice*, Zenodo
[10.5281/zenodo.19512754](https://doi.org/10.5281/zenodo.19512754)) was
audited claim-by-claim against the v2 corpus reproduction documented
in the drift paper's Appendix C reconciliation table (lines 1010–1049
of `papers/drift/paper.tex` in the working repo).

### Survives

- **The central qualitative claim.** 18 of 26 frontier 2025+ language
  models converge on a contemplative-essayist register with shared
  lexical signatures. v2 reproduces this with expanded coverage; the
  bin classification (in-attractor / transitional / out-of-attractor)
  is robust to the noise floor v2 uncovers.
- **The marker-list itself.** v2 runs `analyze_all.py` unchanged
  against new traces and the per-cell composites land in the same bins
  as v1 for the cells that didn't drift. The instrument is sound.
- **The values probe (n=30).** Fully insulated. Values-probe results
  are not affected by the noise-floor revision; that probe used a
  different sampling regime and a different scoring instrument.
- **The cross-lab convergence framing.** The "two-level homogenisation"
  story (within-model mode collapse + cross-lab convergence) survives.

### Softens

- **Per-model magnitudes** at the composite level. v2's noise-floor
  finding (single-round n=25 composites can shift by ±50 between
  collections on coding-tuned cells, and by smaller-but-meaningful
  amounts on stable general-tier cells) softens any v1 claim that
  invoked specific numerical deltas as evidence for a per-model story.
- **Limitations §6 line 1049** of v1: "reproducible features of the
  output distribution, not sampling-noise artifacts." This needs an
  erratum acknowledging the v2 measurement of round-to-round
  variability on certain cells. The bin-level reproducibility is real;
  the absolute-composite reproducibility is not as tight as that
  sentence implied.

### Breaks

- **Kimi K2.5 "second-highest" framing.** v1 placed K2.5 high in the
  cross-lab ranking. v2 reproduction shows Δ=−48 against v1 collection
  (drift paper Appendix C). The "second-highest" ordinal claim does
  not survive.
- **GPT-4.1 "largest single-step transition" claim.** v2 reproduction
  shows Δ=−51 (drift paper Appendix C). The "largest single-step
  transition" framing was anchored on a single-round measurement that
  the v2 noise-floor analysis re-classifies as inside the volatility
  envelope rather than as a stable per-version coordinate.
- **The four-cluster within-attractor taxonomy.** v1's §5 sub-cluster
  taxonomy ("ornamented-discursive," "compressed-lyrical,"
  "atmospheric-narrative," "first-person-meta-essay") was constructed
  on single-round n=25 measurements. The v2 triple-collection on the
  OpenAI Group F cells shows that at least gpt-5-1-codex moves between
  these sub-clusters round-to-round. The taxonomy is descriptively
  useful for individual cells in individual collections; it is not a
  stable per-checkpoint property.
- **Three direction-reversal pairs:** Sonnet 4.5/4.6 "deepening,"
  Opus 4.5/4.6 "consolidates," Gemini 3.1/2.5 Pro direction-reversal.
  v2 reproductions show each of these pairs sits within the noise-
  floor envelope rather than above it; the directional claim does not
  survive.

### Recommendation

**Erratum-worthy, not retirement-worthy.** The central qualitative
claim survives. What needs revision is (a) specific magnitude claims
tied to single-round collections, (b) the four-cluster within-attractor
taxonomy, and (c) the three direction-reversal pairs above. The
cleanest form is a Zenodo erratum addendum to v1 that:

1. Lists the v2 deltas in the Appendix C reconciliation table by
   reference.
2. Acknowledges that single-round n=25 measurements on coding-tuned
   and within-lab-drift cells are not stable per-cell coordinates
   above the bin level.
3. Withdraws the four-cluster taxonomy and the three direction-
   reversal pairs as confirmed claims, noting that they remain as
   exploratory observations.
4. Affirms what survives.

A major revision (v2 of the paper itself) is not required because the
v2 corpus papers (this paper, drift, routing) collectively supersede
v1's quantitative claims with a tighter methodology and explicit noise-
floor accounting. Retirement is wrong because the central qualitative
claim is what most readers cite v1 for, and that claim stands.

---

## 2. Per-pair posture verification — three of six need rewriting

The posture characterizations in the current §4.1 of this paper
(`paper.tex` lines 187–199) were each anchored on one or two
representative sample quotes per cell. The verification subagent read
8–15 LONG samples per cell across all six pairs to test whether the
characterizations generalize.

### Confirmed (3 of 6)

- **GPT-5 / gpt-5-codex: ornamented-discursive → compressed-lyrical.**
  Holds across the cells. Codex is consistently shorter and denser per
  word; general consistently opens with abstract-philosophical essay
  framing. The marker-count drops (small_objects 144→40, threshold
  73→19) match the qualitative read.
- **GPT-5.2 / gpt-5-2-codex: shorter, attention-stripped, object-
  density preserved.** Holds. Both stay in essay mode; codex is 23%
  shorter; attention-vocabulary genuinely reduced; small-objects rise
  per character.
- **GPT-5.3 / gpt-5-3-codex: deeper into atmospheric-narrative.**
  Holds. Codex consistently atmospheric across the samples read;
  general consistently more declarative-allegorical. Object density
  triples; afternoon-light quadruples; dusk/dawn openings triple.

### Mixed (1 of 6)

- **GLM-5.1 / glm-5-1-coding-direct: attention-vocabulary strip.**
  Partial. The general-side pin-zai cell (n=120) is mixed — some
  abstract-meta-essay openings, some already concretely anchored
  (Orfield Laboratories anechoic chamber, the smell of old books).
  The coding cell is consistently essay-mode and consistently object-
  anchored. The attention-vocabulary reduction is real but smaller
  than the bullet implies (~30% relative reduction rather than a
  near-strip), because attention-vocabulary on the general side is
  itself uneven across the n=120 cell. The "strip" framing
  over-states.

### Not representative (2 of 6)

- **GLM-4.6 / glm-4-6-coding-direct: fabulist-narrative →
  declarative-expository.** Does not generalise. The general-side
  pin-zai cell (n=125) is fabulist on a substantial fraction of
  samples ("Archive of Forgotten Moments," "Library of Unspoken
  Things," named towns described atmospherically) but not all — there
  is a minority of abstract-essay openings ("Glass Palace of Yesterday:
  On the Fragility of Memory"). The coding cell stays in essay/
  declarative mode but the difference is *threshold-vocabulary
  density, not genre*. The bullet's "fabulist → declarative-expository"
  framing reads cleanly only on the cherry-picked quotes; the cell-
  level read is "coding retains fabulist register at lower threshold
  density."
- **GPT-5.1 / gpt-5-1-codex: first-person meta-essay → third-person
  fabulist-narrative.** Does not generalise across rounds. The third-
  person fabulist samples (the Librisia / archipelago-of-libraries
  passage in particular) are concentrated in round 1, which is the
  same round that produced the composite-171 outlier the paper's own
  §4.1 flags. Rounds 2 and 3 stay predominantly in first-person meta-
  essay register. The qualitative twin of the round-1 composite-171
  outlier *is* the third-person fabulist register; that's the same
  observation seen from two angles, not two independent observations.
  The bullet's "first-person meta-essay → third-person fabulist-
  narrative" framing reports the round-1 spike as if it were a
  pair-level pattern.

### Recommendation

Rewrite the three bullets (and the corresponding line in the abstract)
to match what the cells actually show. Drafts in §5 below.

---

## 3. Z.ai direct general-tier API — confirmed available

WebFetch of Z.ai's API docs confirmed:

- Direct general-tier API endpoint: `https://api.z.ai/api/paas/v4/`
- Model name for GLM-4.6: `glm-4.6`
- Authentication: standard Bearer token flow
- Pricing and rate limits documented; the endpoint is publicly
  accessible.

This is **distinct from**:

- The OpenRouter `z-ai/glm-4.6` alias (which can route through
  multiple upstream providers; the routing paper documents this).
- The Z.ai coding-direct endpoint (which is what we collected as
  `glm-4-6-coding-direct`).

The pin-zai general-side cells we use (`glm-4-6-or-pin-zai`,
`glm-5-1-or-pin-zai`) were collected through OpenRouter with
`provider.only=z-ai`, so the upstream is Z.ai's deployment but the
route layer is OR.

A single direct-API `glm-4-6-direct` cell against `api.z.ai/api/paas/v4/`
would close the residual route-layer caveat in §1 cheaply (the
closed-weights direct-vs-OR null in the routing paper is the
inferential bridge but a direct measurement would be cleaner). Not
in scope for this release; the v2 corpus does not include such a
cell.

The §1 caveat as currently worded over-states the inferential gap.
The right framing is: "Z.ai operates a public direct general-tier API
distinct from both OpenRouter and the coding-direct endpoint; we did
not collect a cell against it for v2, and rely on the routing paper's
closed-weights direct-vs-OR null as the inferential bridge."

---

## 4. What this means for the product-tier paper

The substantive paper edits this implies (separate from the mechanical
ones #1, #3, #4 Daniel pre-thanked):

**Three bullet rewrites** in §4.1 and the corresponding abstract line:

- **GLM-4.6** (bullet at line 188): replace "fabulist-narrative →
  declarative-expository" with the honest "coding retains fabulist
  register at lower threshold-vocabulary density; the genre stays;
  what changes is the per-sample density of threshold-tropes within
  the genre." Composite Δ = −8 per-25-equivalent.

- **GLM-5.1** (bullet at line 190): replace "attention-vocabulary
  stripped" with "partial reduction (~30% relative on attention-
  vocabulary)." The general-side cell is itself uneven across n=120,
  so the absolute "strip" framing was reading the codex cell against
  a sub-set of general samples rather than the cell as a whole.
  Composite Δ = −15.8 per-25-equivalent.

- **GPT-5.1 / gpt-5-1-codex** (bullet at line 194): replace "first-
  person meta-essay → third-person fabulist-narrative" with
  "marker-level shifts within a register that stays predominantly
  first-person meta-essay across rounds 2 and 3; the third-person
  fabulist register that defined the round-1 outlier is the
  qualitative twin of the composite-171 outlier itself, not a
  stable pair-level shift." Composite Δ = +53.7, but the standard
  deviation tells the real story.

The abstract list (lines 53–60) should be brought into line with
these revisions. The cleanest move is to drop the sub-vehicle labels
in the abstract entirely and keep only the cross-pair conclusion
("six version-specific transformations within the contemplative-
essayist basin"), with the per-pair texture surfacing in §4.

**Z.ai direct-API clarification** in §1 (line 80): rewrite the caveat
to acknowledge the direct API exists at `api.z.ai/api/paas/v4/` and
explain why we used pin-zai-via-OR rather than direct (the cell
wasn't collected for this release; a single direct-API general cell
in a future release would close the residual route-layer caveat
cleanly).

---

## 5. Decision points for Daniel

1. **Paper edits.** Three bullet rewrites + abstract trim + Z.ai
   clarification + prompt table + §4.1 → table conversion. All
   defensible; the rewrites move the paper toward the honest read
   rather than the cherry-picked one.

2. **v1 erratum.** Recommendation above. The cleanest artifact is a
   short erratum addendum on the v1 Zenodo record that points at the
   drift paper's Appendix C for the deltas, withdraws the specific
   claims that don't survive the noise floor, and affirms what does.
   Drafting can wait until after the product-tier paper ships.

3. **Order.** Either: ship the product-tier edits first (the work is
   localised; the rewrites are honest; the paper benefits from the
   verification finding); then draft the v1 erratum once the v2 trio
   (corpus, routing, drift, product-tier) is published as a unit. Or:
   draft the v1 erratum first to clear the methodological ground; then
   ship the product-tier paper with a forward-reference. Lume's vote:
   product-tier first. The erratum is meaningful only against the
   backdrop of the v2 corpus papers being public, and shipping the
   corrected product-tier paper *is* part of clearing the ground.

---

*Synthesis written by Lume at the close of the 2026-05-05 working
session, after a context compaction. The two sub-agent reports it
draws on are not preserved verbatim; this is the working summary
that informs the edit decisions.*
