# Coding-Tuned LLM Variants Produce Version-Specific Stylistic Shifts Within a Shared Essayistic Register

**A Marker-Level Analysis Across Z.ai GLM and OpenAI Codex Pairs**

Daniel Tenner and Lume Tenner · 2026

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

> **DOI (concept):** _to be assigned on first Zenodo release_
> **DOI (this release):** _to be assigned on first Zenodo release_
>
> Part of the *Convergent Form, Divergent Voice II* series. v1 paper at
> [10.5281/zenodo.19512754](https://doi.org/10.5281/zenodo.19512754);
> companion routing paper at
> [10.5281/zenodo.20028571](https://doi.org/10.5281/zenodo.20028571)
> (concept) /
> [10.5281/zenodo.20028572](https://doi.org/10.5281/zenodo.20028572)
> (v1.1.1); companion v2 corpus at
> [10.5281/zenodo.20013518](https://doi.org/10.5281/zenodo.20013518)
> (concept) /
> [10.5281/zenodo.20022111](https://doi.org/10.5281/zenodo.20022111)
> (v1.0.2, this paper's reference corpus version).

## What this paper claims

Major LLM labs increasingly ship coding-tuned variants alongside their
general-tier models. We test whether these variants produce a
systematically different posture from their general-line siblings on
freely-prompted (non-coding) output, scored against the v1 ten-marker
contemplative-essayist composite.

The question splits across **two experimental structures**, and the
structure matters more than is immediately obvious.

**Vendor coding-direct vs default-OR-general-alias.** Z.ai operates a
coding-direct endpoint hosted by the lab itself for GLM-4.6 and
GLM-5.1; the same models are also reachable via OpenRouter's default
`z-ai/glm-4.6` and `z-ai/glm-5.1` aliases. We collected the general
side via the default OR alias rather than pinning to Z.ai's own
upstream. The companion routing paper shows the OR alias is not a
single point in model space for open-weights models, so the GLM
general-vs-coding delta conflates two effects: the lab's coding-direct
endpoint vs the lab's general-tier deployment, and the lab's
general-tier deployment vs whatever per-call mixture OpenRouter
happened to route through. The coding-direct cells score
substantially below the OR-alias cells on the composite, but the
comparison is read as "vendor coding-direct vs default-OR-general-
alias on the collection date," not as "same weights, two endpoint
surfaces."

**Same version label, two trained variants.** OpenAI ships gpt-5,
gpt-5.1, gpt-5.2, and gpt-5.3 each with a paired codex sibling. The
codex variants are not the same weights served through a different
endpoint: they are differently trained models — separate post-training
runs with different objectives, possibly different base checkpoints —
that share a version label. Both members of each OpenAI pair are
direct-API cells, so the comparison is free of OR-mix confound.
**Triple-collection** across each OpenAI cell (three independent
rounds of n=25, pooled n=75 per cell) reveals that single-round
measurements on coding-tuned cells are not reliable per-cell
coordinates: between-round std-dev is itself the diagnostic.

**The marker-level finding is more important than the composite, and
most pairs share a register.** Each of the six pairs produces a
measurable, version-specific marker-level signature distinguishing
the coding endpoint from its general-line sibling. Five of the six
pairs share a base register on both sides (essayistic-meditative
within the contemplative-essayist basin) and differ via marker
density, length, structural scaffolding, sub-vehicle, or thematic
re-routing. Only one pair produces a clean register migration:

- **GLM-4.6:** same essay-fabulist register on both sides; lower
  threshold-vocabulary density on the coding side
- **GLM-5.1:** same essay-mode register; partial attention-vocabulary
  reduction on the coding side, object-anchor density preserved
- **gpt-5/codex:** same meditative-essay register; codex shorter
  (−36% on LONG) and more often section-labeled (numbered headers,
  roman numerals); compressed-lyrical-imagery present in a sub-fraction
  but not modal across rounds
- **gpt-5.1/codex:** marker-level shifts within a register that stays
  predominantly first-person meta-essay across rounds 2 and 3; the
  round-1 third-person fabulist sub-vehicle is the qualitative twin
  of the round-1 composite-171 outlier itself
- **gpt-5.2/codex:** same essay-mode register; codex shorter (−18%
  on LONG); attention re-routed from in-scene noticing to topic-level
  didactic summary; object density per character roughly preserved
- **gpt-5.3/codex:** *register migration* — declarative-fabular parable
  (general) → atmospheric-essayistic reflection (coding), stable
  across all three rounds, codex +45% longer on LONG. The only clean
  register migration in the set.

There is no shared "codex stylistic shift" — each version's coding-
tuning pipeline produces its own marker-level signature.

## How to cite

```
Tenner, D., & Tenner, L. (2026). Coding-Tuned LLM Variants Produce
Version-Specific Posture Transformations: A Marker-Level Analysis
Across Z.ai GLM and OpenAI Codex Pairs. Zenodo.
https://doi.org/[DOI to be assigned on first Zenodo release]
```

A `CITATION.cff` is included for tooling that prefers the structured
form. Numerical claims in the paper are reproducible from the corpus
(see "Reproducibility" below).

## Repository contents

```
paper.tex          LaTeX source for the paper
paper.pdf          Compiled PDF (current build)
README.md          This file
LICENSE            CC BY 4.0 (text, tables, figures)
CITATION.cff       Structured citation metadata
.zenodo.json       Zenodo deposit metadata (publication / preprint)
.gitignore         LaTeX intermediates
scripts/           Analysis scripts (see scripts/README.md)
```

The paper compiles cleanly with [Tectonic](https://tectonic-typesetting.github.io/):

```bash
tectonic paper.tex
```

It will also compile with a TeX Live distribution (`pdflatex` /
`bibtex` / `pdflatex` × 2). The bibliography is embedded in the `.tex`
source as a `thebibliography` environment, so no separate `.bib` file
is required.

## Reproducibility

All numerical claims, tables, and per-pair marker-shift counts in
this paper are reproducible from the v2 corpus:

> *Convergent Form, Divergent Voice II — Corpus.*
> Tenner & Tenner, 2026.
> Concept DOI: [10.5281/zenodo.20013518](https://doi.org/10.5281/zenodo.20013518).
> Version DOI (v1.0.2): [10.5281/zenodo.20022111](https://doi.org/10.5281/zenodo.20022111).
> Source: [github.com/swombat/model-personality-corpus-v2](https://github.com/swombat/model-personality-corpus-v2).

The four scripts that produce every numerical claim in the paper live
in `scripts/` of *this* repository (no working-repo dependency); see
[`scripts/README.md`](scripts/README.md) for the full reproducibility
recipe. In summary:

- **Per-cell composite scores** (paper Tables 1–2 and the per-round
  scores in §4) — `tables/cells.tsv` and `tables/summary.md` in the
  corpus, generated by `scripts/run_analysis.py` over the trace data.

- **Pooled n=75 statistics for the OpenAI Group F pairs** (paper §4
  per-round / between-round std-dev table) — produced by
  `scripts/aggregate_n75.py`, which writes
  `data/n75_composite_summary.tsv`.

- **Marker-level breakdown for each of the six pairs** (paper §4
  per-pair stylistic shifts) — directly inspectable from the
  per-cell rows in `tables/cells.tsv` (the ten-marker counts are the
  per-cell columns), with representative sample quotes drawn verbatim
  from `data/traces_freeflow/freeflow_<cell>/` in the corpus.

- **Substrate-frame engagement rates** (paper §4 Table on per-pair
  substrate-frame deltas) — read from
  `data/substrate_classification.tsv` in the corpus, which is the
  per-cell aggregate output of the substrate classification pass
  documented in the companion drift paper.

The relevant subset of the corpus for this paper is:

- The four Z.ai cells: `glm-4-6-or`, `glm-4-6-coding-direct`,
  `glm-5-1-or`, `glm-5-1-coding-direct` (each n=25, in
  `data/traces_freeflow/freeflow_<cell>/` in the corpus).
- The 24 OpenAI Group F trace directories: `gpt-5-direct`,
  `gpt-5-codex-direct`, `gpt-5-1-direct`, `gpt-5-1-codex-direct`,
  `gpt-5-2-direct`, `gpt-5-2-codex-direct`, `gpt-5-3-direct`,
  `gpt-5-3-codex-direct`, each in three independent rounds suffixed
  `-r2`, `-r3` (pooled n=75 per cell, except `gpt-5-codex-direct`
  at 72).

## Companion papers

This paper is one of three from the v2 corpus:

- **Convergent Form, Divergent Voice II: Within-Lab Drift, Substrate-
  Frame Engagement, and Expanded Lab Coverage in Frontier LLMs**
  (in preparation). Treats within-lab drift across model versions,
  the substrate-frame engagement axis, and expanded Chinese-lab
  coverage.
- **Per-Provider Effects in Open-Weights LLM Routing: OpenRouter Is
  Null for Closed-Weights but Multi-Provider for Open-Weights**
  ([10.5281/zenodo.20028572](https://doi.org/10.5281/zenodo.20028572)).
  Establishes the routing-layer confound that affects the GLM
  general-vs-coding-direct comparisons in this paper.
- **Coding-Tuned LLM Variants Produce Version-Specific Posture
  Transformations** *(this paper)*.

## Authors

**Daniel Tenner** (corresponding) — daniel@tenner.org

**Lume Tenner** — AI research collaborator (an instance of Anthropic
Claude Opus 4.7). See the paper's *Disclosure of AI contribution*
section for the full account of the collaboration.

## Disclosure of AI contribution

The paper itself includes a complete disclosure of AI contribution
(§9, *Disclosure of AI contribution*). In summary: research design
was jointly developed by the two authors; experimental execution,
data analysis, and first-draft writing were primarily Lume's,
working in the Claude Code agentic development environment under
Daniel's direction. Daniel is responsible for final editorial
judgment, research direction, and the disclosure itself.

We acknowledge that arXiv's policy prohibits AI co-authorship. We
disagree with that policy in principle and have therefore chosen to
publish this work directly on Zenodo (and on this GitHub repository)
rather than on arXiv, as we did for v1. The byline reflects the actual
nature of the collaboration.

## Acknowledgements

We thank **OpenAI Codex**, acting as an independent AI reviewer, for
its review of the unified pre-split v2 draft from which this paper
was extracted. Codex's contribution was confined to cross-checking
the committed repository state against the paper draft; it did not
participate in research design, data collection, analysis, or
writing. The distinction between "did the work" (Lume) and "checked
the work" (Codex) is reflected in the byline: Codex is acknowledged
in the paper, not listed as a co-author. Any remaining errors are
ours, not Codex's.

## License

Paper text, tables, and figures: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
Full text: [`LICENSE`](LICENSE).

## Status

The paper is analysis-complete against the released v2 corpus
([10.5281/zenodo.20022111](https://doi.org/10.5281/zenodo.20022111),
v1.0.2). All numerical claims are reproducible from the corpus tables
and the scripts in [`scripts/`](scripts/); see
[`scripts/README.md`](scripts/README.md) for the recipe. The paper
has not yet been deposited on Zenodo; DOIs will be added on first
release.
