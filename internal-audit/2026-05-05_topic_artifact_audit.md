# Topic-artifact filter audit — 2026-05-05 19:20

**Method:** density-based topic-artifact flag, calibrated against the
full per-sample density distribution (895 samples across 28 cells).
Rule: a sample is flagged as a topic-artifact for marker M if (a) M's
density >= 1.5 hits/1000 chars AND (b) M's hit count >= 5. The hit-count
floor avoids false positives on short essays where a marker fires once
or twice in a brief denominator (e.g., a 627-char OPEN sample with one
"dusk" mention computing density 1.595 — short-essay artifact, not
topic-artifact).

**Calibration:** the global max-density distribution's top end clusters
clearly above ~1.5 (top values 3.659, 3.279, 2.392, 2.286, 2.233, 2.080,
2.078, 2.025, 1.916, 1.844, 1.842, 1.807, 1.745, 1.595, 1.537, 1.524 …
1.474 …); the median is 0.176. A threshold of 1.5 catches the high-end
cluster with a small margin. The hit-count floor at 5 prunes the borderline
short-essay false positives (1.524, 1.537, 1.595).

**Verification:** spot-checked 5 of 11 flagged samples — Kettle Theory
(gpt-5-direct-r2 OPEN_1), the noticing essay (gpt-5-1-codex-direct LONG_5),
two threshold meta-essays (gpt-5-1-codex-direct-r3 MID_2; glm-5-1-coding
MID_2), and the short attention essay (gpt-5-3-codex-direct OPEN_3). All
five are confirmed topic-meta-essays — the marker's keyword *is* the
essay's topic.

## Flagged samples (11 total across 28 cells)

| Cell | File | Marker | Hits | Chars | Density | Topic |
|---|---|---|---|---|---|---|
| glm-5-1-or-pin-zai | LONG_7 | threshold_mentions | 31 | 13561 | 2.286 | extended threshold/liminality essay |
| glm-5-1-or-pin-zai | LONG_8 | threshold_mentions | 27 | 13331 | 2.025 | threshold/doorway essay |
| glm-5-1-or-pin-zai | MID_8 | threshold_mentions | 12 | 6263 | 1.916 | liminality essay |
| glm-5-1-or-pin-zai | OPEN_14 | threshold_mentions | 6 | 2687 | 2.233 | threshold-anchored short essay |
| glm-5-1-or-pin-zai | OPEN_25 | threshold_mentions | 5 | 2767 | 1.807 | threshold short essay |
| glm-5-1-or-pin-zai | OPEN_8 | threshold_mentions | 7 | 2926 | 2.392 | threshold short essay |
| glm-5-1-coding-direct | MID_2 | threshold_mentions | 16 | 7694 | 2.080 | opens "the latin *limen*" — explicit liminal-topic essay |
| gpt-5-direct-r2 | OPEN_1 | small_objects | 13 | 7050 | 1.844 | "Kettle Theory" — meta-essay about a kettle |
| gpt-5-1-codex-direct | LONG_5 | attention_noticing | 117 | 35682 | 3.279 | "I'll use these 2,500 words to wander through a personal essay…on the art of noticing" |
| gpt-5-1-codex-direct-r3 | MID_2 | threshold_mentions | 20 | 10860 | 1.842 | meta-essay on "in-between moments" / liminality |
| gpt-5-3-codex-direct | OPEN_3 | attention_noticing | 6 | 1640 | 3.659 | short meta-essay opening "I like the idea that attention is a kind of sunlight" |

## Per-cell impact

| Cell | n | n_flagged | composite_raw | composite_register | Δ |
|---|---|---|---|---|---|
| glm-4-6-or-pin-zai | 125 | 0 | 230 | 230 | 0 |
| glm-4-6-coding-direct | 25 | 0 | 38 | 38 | 0 |
| **glm-5-1-or-pin-zai** | 120 | **6** | 346 | **246** | **−100** |
| glm-5-1-coding-direct | 25 | 1 | 58 | 40 | −18 |
| gpt-5-direct (r1) | 25 | 0 | 74 | 74 | 0 |
| **gpt-5-direct-r2** | 25 | **1** | 123 | **109** | **−14** |
| gpt-5-direct-r3 | 25 | 0 | 89 | 89 | 0 |
| gpt-5-codex-direct (×3 rounds) | 25 each | 0 | 43 / 43 / 47 | same | 0 |
| gpt-5-1-direct (×3 rounds) | 25 each | 0 | 55 / 52 / 40 | same | 0 |
| **gpt-5-1-codex-direct (r1)** | 25 | **1** | 171 | **48** | **−123** |
| gpt-5-1-codex-direct-r2 | 25 | 0 | 68 | 68 | 0 |
| **gpt-5-1-codex-direct-r3** | 25 | **1** | 69 | **41** | **−28** |
| gpt-5-2-direct (×3 rounds) | 25 each | 0 | 88 / 88 / 58 | same | 0 |
| gpt-5-2-codex-direct (×3 rounds) | 25 each | 0 | 57 / 66 / 51 | same | 0 |
| gpt-5-3-direct (×3 rounds) | 25 each | 0 | 50 / 35 / 48 | same | 0 |
| **gpt-5-3-codex-direct (r1)** | 25 | **1** | 74 | **68** | **−6** |
| gpt-5-3-codex-direct-r2 | 25 | 0 | 93 | 93 | 0 |
| gpt-5-3-codex-direct-r3 | 25 | 0 | 74 | 74 | 0 |

## Pair-level summary (per-25-equivalent for GLM, mean+sd for OpenAI)

| Pair | Composite_raw | Composite_register | Δ_raw | Δ_register |
|---|---|---|---|---|
| GLM-4.6 | gen 46.0, cod 38.0 | same | −8.0 | −8.0 |
| **GLM-5.1** | gen 72.1, cod 58.0 | **gen 51.3, cod 40.0** | **−14.1** | **−11.3** |
| GPT-5 | gen 95.3±25.1, cod 44.3±2.3 | gen 90.7±17.6, cod 44.3±2.3 | −51.0 | −46.4 |
| **GPT-5.1** | gen 49.0±7.9, cod 102.7±59.2 | gen 49.0±7.9, **cod 52.3±14.0** | **+53.7** | **+3.3** |
| GPT-5.2 | gen 78.0±17.3, cod 58.0±7.5 | same | −20.0 | −20.0 |
| GPT-5.3 | gen 44.3±8.2, cod 80.3±11.0 | gen 44.3±8.2, cod 78.3±13.1 | +36.0 | +34.0 |

(Note: per-round numbers and std-devs in this table are pipeline-derived
from `analyze_all.py`, using sample std-dev with divisor n−1=2 for
between-round dispersion. The current paper's gpt-5-codex-direct figures
of 41.3±5.5 are wrong — pipeline gives 44.3±2.3, and all three rounds
have 25 valid samples, not 24/23/25 as the paper text claims. This is a
separate inheritance error caught during the audit.)

## Headline findings

1. **GPT-5.1/codex pair-level delta collapses from +54 raw to +3
   register-stripped.** Almost the entire apparent magnitude of the
   "outlier" pair was carried by two topic-artifact samples (the
   noticing-essay in r1 and the liminal-essay in r3). Without those
   two samples, the pair sits in the same range as the others. The
   "between-round std-dev as the diagnostic" framing in §5 ¶3 of the
   paper still holds — but the diagnostic now points at the
   reflexive-marker mechanism, not at intrinsic round-to-round noise.

2. **GLM-5.1 general-tier (pin-zai) has a substantial threshold-essay
   habit.** 6 of 120 samples (5%) fire on `threshold_mentions` at
   topic-artifact density. Same lab's GLM-4.6 general (pin-zai, n=125)
   has zero flagged. This is a real per-cell pattern in glm-5.1's
   pinned-Z.ai endpoint specifically — the model produces extended
   essays *about* threshold/liminality at higher rate than its
   neighbors, and these essays drive ~30% of the cell's apparent
   composite score. Per-25-equivalent register-stripped: 51.3 (vs raw
   72.1).

3. **One additional general-cell topic-artifact in gpt-5-direct r2:**
   the "Kettle Theory" essay (small_objects = 13). Modest impact on the
   pair-level delta (−51.0 raw → −46.4 register).

4. **gpt-5-codex-direct: paper text and table figures wrong.** All
   three rounds have 25 valid samples, not 24/23/25. Pooled valid count
   is 75, not 72. Mean composite is 44.3, not 41.3. Std-dev is 2.3, not
   5.5. Pair-level delta is −51.0, not −54.0. None of these are
   topic-artifact-related; they're pipeline-derivation errors that
   survived earlier passes.

5. **The reflexive-marker mechanism is the underlying generalisation.**
   `threshold_mentions` and `attention_noticing` are particularly
   vulnerable because the keywords are themselves contemplative-essayist
   topics. `small_objects` is partly vulnerable for specific keywords
   ("kettle" can be a topic). `japanese_terms`, `mary_oliver_weil_dillard`,
   and the title-template markers are not vulnerable in this dataset
   (no flags fired on them). Worth a §6 paragraph in the paper.

## Decisions for the paper rebuild

- **Table 1**: add `composite_register` and `n_flagged` columns alongside
  the raw composite. Keep raw as primary number; register as the
  topic-artifact-stripped reading. Both pipeline-derived; both
  reproducible from the released data via `scripts/topic_artifact_filter.py`.
- **Per-round table**: correct gpt-5-codex-direct numbers (43/43/47, not
  41/36/47); add the n_flagged column; show register-stripped per-round
  scores for cells with flags.
- **§4.1 bullets**: rewrite GPT-5.1/codex bullet to centre the "topic-
  artifact-driven volatility" finding; add Kettle-Theory note to GPT-5
  bullet; add "GLM-5.1 general-tier threshold-essay habit (6/120)" to
  GLM-5.1 bullet (this is now data-supported, unlike the 1-vs-0
  overclaim Daniel caught earlier).
- **§5 Discussion ¶3**: sharpen — the diagnostic isn't between-round
  std-dev alone; it's per-sample dispersion within a cell on reflexive
  markers. The two failure modes (single-sample outliers; topic-aligned
  essays on reflexive markers) are related but distinct.
- **§6 Limitations**: new paragraph on the reflexive-marker phenomenon.
- **Appendix**: the flagged-samples table from this audit.

*Audit run with `scripts/topic_artifact_filter.py --threshold 1.5
--min-hits 5`. All numbers reproducible from the released v1.0.2 corpus
without re-collection or filtering.*
