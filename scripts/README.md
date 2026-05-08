# Reproducibility scripts

These four scripts reproduce every numerical claim in the paper from the
released corpus trace data. They are exact copies of the working-repo
versions (kept here to remove the working-repo as a dependency for
reproducing this paper).

| Script | What it does |
|---|---|
| `analyze_all.py` | The v1 freeflow composite-scoring instrument, used unchanged. Computes per-cell composite totals (and the ten per-marker counts) from the released trace data. |
| `run_analysis.py` | Convenience driver that runs `analyze_all.py` over every cell directory and writes `tables/summary.md` and `tables/cells.tsv`. The per-cell row in `tables/cells.tsv` carries the ten-marker counts that produce the per-pair marker-shift figures in §4. |
| `aggregate_n75.py` | Per-sample composite-score aggregation for the OpenAI Group F triple-collected cells. For each gpt-5.x / gpt-5.x-codex cell, computes per-sample composites and aggregates to round-1 alone (n=25) and pooled r1+r2+r3 (n=75): mean and between-round std-dev. Writes `data/n75_composite_summary.tsv`. |
| `run_freeflow_multi.py` | The collection harness used to produce the trace data. Reads API keys from environment variables; documented inline. Not needed for reproducing analyses from the released traces. |

## Reproducing the analysis

The scripts expect the corpus trace data at
`<repo-root>/data/traces_freeflow/`. The canonical location of that
data is the corpus repository:

> *Convergent Form, Divergent Voice II — Corpus.*
> Tenner & Tenner, 2026.
> Concept DOI: [10.5281/zenodo.20013518](https://doi.org/10.5281/zenodo.20013518).
> Version DOI (v1.0.2): [10.5281/zenodo.20022111](https://doi.org/10.5281/zenodo.20022111).
> Source: [github.com/swombat/model-personality-corpus-v2](https://github.com/swombat/model-personality-corpus-v2).

The simplest reproducibility recipe runs the scripts in the corpus
repository directly (the corpus already ships the same scripts):

```bash
git clone https://github.com/swombat/model-personality-corpus-v2.git
cd model-personality-corpus-v2

# Per-cell composite scores and ten-marker counts for every cell
python3 scripts/run_analysis.py

# Pooled n=75 statistics for the OpenAI Group F triple-collected cells
python3 scripts/aggregate_n75.py
```

Outputs are written to `tables/summary.md`, `tables/cells.tsv`, and
`data/n75_composite_summary.tsv`.

If you would prefer to run the scripts from a clone of *this*
repository (the product-tier paper repo), symlink the corpus data:

```bash
git clone https://github.com/swombat/model-personality-product-tier-v2.git
git clone https://github.com/swombat/model-personality-corpus-v2.git
cd model-personality-product-tier-v2
ln -s ../model-personality-corpus-v2/data data
ln -s ../model-personality-corpus-v2/tables tables
python3 scripts/run_analysis.py
python3 scripts/aggregate_n75.py
```

Either workflow produces byte-identical tables.

## Verifying paper claims

The paper's headline findings are reproducible as follows:

- **Z.ai composite-level deltas** (paper Table 1, the four GLM cells):
  read directly from `tables/cells.tsv` rows for `glm-4-6-or`,
  `glm-4-6-coding-direct`, `glm-5-1-or`, `glm-5-1-coding-direct`.
  Composite scores are the `composite` column; the ten per-marker
  counts (TIA, TiQu, TiPP, TiAr, Thr, Attn, Obj, AftL, Cano, Jap)
  are the per-marker columns.

- **OpenAI Group F per-round and pooled n=75 statistics** (paper
  Table 2 and the §4 between-round std-dev discussion): read from
  `data/n75_composite_summary.tsv`, which carries one row per cell
  with r1 mean / sd, r1+r2+r3 pooled mean / sd, and round-level
  composites for r1, r2, r3.

- **Per-pair posture transformations** (paper §4, six per-pair
  marker-level analyses): the marker-shift counts come from
  `tables/cells.tsv` (subtract the per-marker counts of the coding
  cell from the general cell, or vice versa, for each of the six
  pairs). Representative sample quotes are drawn verbatim from
  `data/traces_freeflow/freeflow_<cell>/` in the corpus; cell names
  are listed in the paper's Methods section.

- **Substrate-frame engagement deltas** (paper §4 substrate table):
  read from `data/substrate_classification.tsv` in the corpus, which
  is the per-cell aggregate output of the substrate classification
  pass documented in the companion drift paper. The product-tier
  cells appear with `<cell>` keys matching `tables/cells.tsv`.

## Notes on the collection harness

`run_freeflow_multi.py` is included for transparency about how the
trace data was produced. It is *not* required for reproducing the
paper's numerical analyses — those run entirely from the released
traces. Re-running the probes against the same models will produce
substantively similar but not bit-identical outputs (the underlying
models are stochastic at temperature default, and day-to-day
sampling variance for n=25 freeflow runs is non-trivial; the
triple-collection design for the OpenAI Group F cells is precisely
the empirical handle this paper uses on that variance).
