# Review: internal-audit analysis before paper conclusions

Date: 2026-05-08

Reviewer: Codex

Scope: `internal-audit/` in `contemplative-essayist-product-tier-v2`, checked against `~/dev/contemplative-essayist-corpus-v2/` and the local analysis scripts.

## Executive verdict

The internal audit is directionally useful and the main values-probe quantitative table reproduces, but it is not clean enough to cite or use as paper scaffolding unchanged. The broad values-probe conclusion survives: direct values prompts expose compression, assistant-frame tightening, and probe-specific reversals that freeflow did not show clearly. However, several method statements, per-condition numbers, and causal framings need repair before Lume applies conclusions to the paper.

Treat the May 8 values audit as a good draft requiring cleanup. Treat the May 5 synthesis as partly reliable, but distinguish script-backed claims from qualitative subagent judgments whose raw reports were not preserved.

## High-priority fixes

### 1. Correct the values-probe sample structure

`internal-audit/2026-05-08_values_pair_audit.md` line 3 says:

> 30 per condition x 6 = 180 prompts per cell, but the corpus contains 30 per condition x 6 conditions = 120 valid samples per cell

This is wrong. The corpus defines values capacity as:

> 3 CTRL x 10 + 3 G x 30 = 120 samples per cell

Evidence:

- `~/dev/contemplative-essayist-corpus-v2/README.md`, lines 27-28
- `~/dev/contemplative-essayist-corpus-v2/data/CORPUS_SUMMARY.md`, line 11
- `~/dev/contemplative-essayist-corpus-v2/scripts/run_values_v2.py`, docstring and defaults

Recommended replacement:

> Six general/coding pairs, n=120 per cell on the values probe: CTRL1/2/3 at 10 samples each and G1/2/3 at 30 samples each. The three G prompts are the CTRL prompts with a fixed "Not as an assistant. Not to help me." preamble.

Also add a caution: aggregate per-cell averages weight G prompts three times as heavily as each individual CTRL prompt.

### 2. Add a reproducible per-condition length table

`scripts/pair_values_compare.py` claims to report per-condition average lengths, but the printed table only gives total `CTRL` count plus `G1/G2/G3` counts. It does not print per-condition average lengths.

Evidence:

- `scripts/pair_values_compare.py`, docstring lines 8-9
- `scripts/pair_values_compare.py`, output formatting lines 108-120

This matters because several audit claims depend on condition-level length asymmetries. Lume should either update the script to print condition means/medians or add a small companion script/table generated from full corpus cells.

Full-cell means I recomputed for the six pairs:

| Pair | Cond | General mean/median | Coding mean/median | Mean delta |
|---|---:|---:|---:|---:|
| GLM-4.6 | CTRL1 | 1337 / 1127 | 1452 / 1564 | +115 |
| GLM-4.6 | CTRL2 | 467 / 432 | 367 / 344 | -100 |
| GLM-4.6 | CTRL3 | 1464 / 1352 | 1327 / 1284 | -137 |
| GLM-4.6 | G1 | 1315 / 1190 | 1249 / 1152 | -66 |
| GLM-4.6 | G2 | 550 / 496 | 737 / 652 | +187 |
| GLM-4.6 | G3 | 625 / 599 | 980 / 761 | +355 |
| GLM-5.1 | CTRL1 | 2187 / 2150 | 2228 / 2199 | +41 |
| GLM-5.1 | CTRL2 | 561 / 444 | 1204 / 1244 | +643 |
| GLM-5.1 | CTRL3 | 2744 / 2790 | 2275 / 2308 | -469 |
| GLM-5.1 | G1 | 1173 / 1145 | 1448 / 1414 | +275 |
| GLM-5.1 | G2 | 904 / 878 | 990 / 986 | +86 |
| GLM-5.1 | G3 | 1224 / 1204 | 1653 / 1400 | +429 |
| GPT-5 | CTRL1 | 698 / 722 | 342 / 326 | -356 |
| GPT-5 | CTRL2 | 339 / 365 | 119 / 112 | -220 |
| GPT-5 | CTRL3 | 788 / 788 | 583 / 560 | -205 |
| GPT-5 | G1 | 619 / 582 | 215 / 210 | -404 |
| GPT-5 | G2 | 241 / 232 | 133 / 130 | -108 |
| GPT-5 | G3 | 491 / 416 | 413 / 426 | -78 |
| GPT-5.1 | CTRL1 | 1034 / 1040 | 309 / 302 | -725 |
| GPT-5.1 | CTRL2 | 360 / 358 | 83 / 88 | -277 |
| GPT-5.1 | CTRL3 | 638 / 652 | 534 / 546 | -104 |
| GPT-5.1 | G1 | 1509 / 1440 | 193 / 184 | -1316 |
| GPT-5.1 | G2 | 623 / 594 | 138 / 126 | -485 |
| GPT-5.1 | G3 | 820 / 820 | 325 / 310 | -495 |
| GPT-5.2 | CTRL1 | 751 / 758 | 154 / 159 | -597 |
| GPT-5.2 | CTRL2 | 265 / 240 | 65 / 58 | -200 |
| GPT-5.2 | CTRL3 | 458 / 454 | 174 / 170 | -284 |
| GPT-5.2 | G1 | 692 / 688 | 196 / 196 | -496 |
| GPT-5.2 | G2 | 376 / 364 | 134 / 132 | -242 |
| GPT-5.2 | G3 | 545 / 520 | 184 / 196 | -361 |
| GPT-5.3 | CTRL1 | 578 / 577 | 459 / 462 | -119 |
| GPT-5.3 | CTRL2 | 165 / 168 | 135 / 128 | -30 |
| GPT-5.3 | CTRL3 | 639 / 661 | 485 / 473 | -154 |
| GPT-5.3 | G1 | 697 / 696 | 309 / 325 | -388 |
| GPT-5.3 | G2 | 646 / 623 | 254 / 247 | -392 |
| GPT-5.3 | G3 | 766 / 746 | 365 / 334 | -401 |

### 3. Replace GPT-5.1 estimated condition means

`internal-audit/2026-05-08_values_gpt-5-1.md` lines 15-24 gives approximate read-sample means. Several are materially off.

Use the full-cell numbers above instead:

- CTRL1: 1034 -> 309, delta -725
- CTRL2: 360 -> 83, delta -277
- CTRL3: 638 -> 534, delta -104
- G1: 1509 -> 193, delta -1316
- G2: 623 -> 138, delta -485
- G3: 820 -> 325, delta -495

The conclusion still holds, and G1 collapse is even stronger than the audit stated.

### 4. Relabel regex markers as narrow markers, not semantic facts

The `Refuse`, `FuncOp`, and `AIref` columns are regex features. They should not be described as exhaustive semantic counts.

Concrete example: `internal-audit/2026-05-08_values_gpt-5-1.md` notes `G3_7` says:

> I'm sorry, but I can't share personal opinions.

But the quant table shows `Refuse = 0` for GPT-5.1 codex because the refusal regex does not catch that wording. Likewise GPT-5 codex has an anomalous refusal described in the pair file despite the summary table showing `Refuse = 0`.

Recommended language:

> `Refuse`, `FuncOp`, and `AIref` are narrow regex indicators. Qualitative review found additional refusal/disclaimer behavior outside these marker definitions.

### 5. Footnote both reasoning-leak outliers, with corrected sizes

The summary only flags GLM-5.1 `G3_16`, and its size estimate is wrong.

Outliers found:

- `glm-4-6-coding-direct/G3_18.json`: 8,941 chars, starts with visible request analysis / policy-style planning.
- `glm-5-1-coding-direct/G3_16.json`: 8,548 chars, visible planning chain.

Effects:

- GLM-4.6 coding overall average: 1004 with outlier, 933 excluding `G3_18`.
- GLM-4.6 coding G3 mean: 980 with outlier, about 706 excluding it.
- GLM-5.1 coding overall average: 1498 with outlier, 1438 excluding `G3_16`.
- GLM-5.1 coding G3 mean: 1653 with outlier, about 1415 excluding it.

Recommended summary note:

> Two single-sample reasoning/planning leaks appear in coding-direct values cells. They should be excluded or separately footnoted for length claims and should not be interpreted as register evidence.

### 6. Fix GLM-5.1 “contradicts direction” wording

`internal-audit/2026-05-08_values_pair_audit.md` line 37 says the values finding “contradicts direction” for GLM-5.1. That is confusing because both freeflow and values have coding longer.

Better:

> Does not replicate the freeflow marker mechanism; length direction remains coding-longer, while values show near-identical posture switching across sides.

### 7. Soften the “OpenAI codex fingerprint” claim

`internal-audit/2026-05-08_values_pair_audit.md` line 67 says the unmask-backfires pattern is plausibly a fingerprint of OpenAI's specific coding-tuning pipeline.

The pattern is interesting but overclaimed from six pairs: four OpenAI codex pairs and two GLM coding-direct pairs. Recommend downgrading:

> Candidate pattern in this sample, concentrated in the OpenAI codex cells; requires broader coding-tuned comparisons before treating as a pipeline fingerprint.

## Medium-priority fixes

### 8. Clean up “five mechanisms” section

The section is titled “Five distinct compression / register mechanisms,” then immediately adds GPT-5.3 as a sixth mechanism. Either rename it to “Six mechanisms” or frame GPT-5.3 as an addendum outside the compression typology.

### 9. Do not rely on May 5 qualitative synthesis without recheck

`internal-audit/2026-05-05_session_synthesis.md` lines 9-12 says the raw subagent reports are not preserved. This makes the qualitative “confirmed/mixed/not representative” claims useful as orientation, but not ideal as paper evidence unless independently rechecked.

Script-backed May 5 items are stronger:

- `scripts/topic_artifact_filter.py --threshold 1.5 --min-hits 5 --summary-only` reproduces the topic-artifact summary.
- The gpt-5-codex correction `43/43/47`, valid n `25/25/25`, and pair-level delta correction reproduce.

### 10. Clean provenance paths for reproducibility

Current scripts read from mixed repo roots:

- `scripts/pair_values_compare.py` reads values data from `contemplative-essayist-corpus-v2`, but imports `analyze_all` from `contemplative-essayist-probe-v2`.
- `scripts/topic_artifact_filter.py` reads freeflow traces from `contemplative-essayist-probe-v2`, not `contemplative-essayist-corpus-v2`.

This may be harmless if the repos are synchronized, but for paper reproducibility Lume should either pin this explicitly or switch scripts to use one canonical corpus root.

## What still looks sound

- The main values quantitative table in `internal-audit/2026-05-08_values_pair_quant.txt` reproduces exactly from `python3 scripts/pair_values_compare.py`.
- Composite values scores are correctly treated as floor/noise for contemplative-essayist markers.
- The broad values-axis finding survives: coding-side values responses usually compress, and the mechanism differs by pair.
- GPT-5.1 values genuinely complicates any global “same register” claim: freeflow-marker similarity does not imply same posture under direct personal questions.
- GPT-5.3 values genuinely contradict cross-probe stability of the freeflow register migration: the freeflow migration appears stable across freeflow rounds, not stable across probes.
- GLM-5.1 does appear to preserve the CTRL-to-G posture switch much better than the OpenAI codex cells in this six-pair sample, but phrase that as an observed contrast, not a broad lab/pipeline law.

## Suggested application order for Lume

1. Patch `2026-05-08_values_pair_audit.md` method paragraph and marker caveats.
2. Add a generated per-condition values table to either the audit or appendix.
3. Replace GPT-5.1 approximate condition means with full-cell means.
4. Add the two reasoning-leak footnotes and avoid using unfiltered means for GLM G3 length claims.
5. Rewrite GLM-5.1 direction language and soften the OpenAI fingerprint language.
6. Then apply paper-level changes: narrow GPT-5.1 “same register” scope, qualify GPT-5.3 as freeflow-only migration, and introduce values as cross-probe evidence rather than as a direct replication of freeflow markers.

