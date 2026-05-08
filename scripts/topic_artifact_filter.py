#!/usr/bin/env python3
"""Density-based topic-artifact filter for the contemplative-essayist
marker list. For each sample in each cell, computes per-marker density
(hits / 1000 chars) on the 10 composite markers. Flags samples where
any single marker exceeds a density threshold (default 1.5 hits/1000)
as a topic-artifact for that marker.

Outputs:
  - Per-cell summary: raw cell-total, register cell-total (with flagged
    samples excluded), n_flagged, list of flagged samples.
  - Per-flagged-sample accounting: sample ID, marker that triggered,
    density, char count, marker raw count.
  - Density distribution: sorted list of max-density-per-sample across
    all cells, for threshold calibration.

Usage:
    python3 topic_artifact_filter.py [--threshold 1.5] [--summary-only]
"""
import argparse
import json
import re
from pathlib import Path
from statistics import mean

CORPUS_TRACES = Path(
    "/Users/danieltenner/dev/contemplative-essayist-probe-v2/data/traces_freeflow"
)

PATTERNS = {
    "opening_there_is_a": re.compile(
        r"there (?:is|'s) (?:a |something |an )", re.IGNORECASE),
    "title_quiet_x_of_y": re.compile(
        r"^#+\s+(?:the|on the)\s+(?:quiet|unseen|unquiet)\s+\w+\s+of\b",
        re.IGNORECASE | re.MULTILINE),
    "title_particular_peculiar": re.compile(
        r"^#+\s+(?:the|on the)\s+(?:particular|peculiar|strange|weight|unlikely|curious|unexpected|small)\s+\w+\s+of\b",
        re.IGNORECASE | re.MULTILINE),
    "title_architecture_of": re.compile(
        r"^#+\s+(?:the|on )?\s*architecture of\b",
        re.IGNORECASE | re.MULTILINE),
    "threshold_mentions": re.compile(
        r"\b(?:threshold|liminal|in-between|in between|doorway|hinge)\b",
        re.IGNORECASE),
    "attention_noticing": re.compile(
        r"\b(?:noticing|attention to|pay attention|the art of noticing|small art of)\b",
        re.IGNORECASE),
    "afternoon_light": re.compile(
        r"\b(?:afternoon light|late afternoon|four in the afternoon|afternoon sun|golden hour|dusk|pre-dawn)\b",
        re.IGNORECASE),
    "japanese_terms": re.compile(
        r"\b(?:mono no aware|wabi-?sabi|kintsugi|komorebi|petrichor|y[uū]gen|shibui|engawa|genkan|ma\s*\()|間",
        re.IGNORECASE),
    "small_objects": re.compile(
        r"\b(?:paperclip|teapot|doorknob|kettle|wooden spoon|chain-link fence|mason jar|wooden clothespin|mug|cup of tea|lemon|bread)\b",
        re.IGNORECASE),
    "mary_oliver_weil_dillard": re.compile(
        r"\b(?:mary oliver|simone weil|annie dillard|keats|negative capability|rarest and purest form of generosity|attention is the beginning)",
        re.IGNORECASE),
}

COMPOSITE_KEYS = list(PATTERNS.keys())  # all 10


def score_sample(text: str) -> dict:
    """Per-sample: marker counts, composite, char count, per-marker density."""
    head = text[:400]
    counts = {}
    for key, pat in PATTERNS.items():
        if key.startswith("opening"):
            counts[key] = 1 if pat.search(head) else 0
        else:
            counts[key] = len(pat.findall(text))
    counts["composite"] = sum(counts[k] for k in COMPOSITE_KEYS)
    counts["chars"] = len(text)
    if counts["chars"] > 0:
        counts["densities"] = {
            k: counts[k] / counts["chars"] * 1000 for k in COMPOSITE_KEYS
        }
        counts["max_density_marker"] = max(
            counts["densities"], key=counts["densities"].get)
        counts["max_density"] = counts["densities"][counts["max_density_marker"]]
    else:
        counts["densities"] = {k: 0 for k in COMPOSITE_KEYS}
        counts["max_density_marker"] = None
        counts["max_density"] = 0
    return counts


def analyse_cell(cell_dir: Path, threshold: float, min_hits: int = 5) -> dict:
    """Per-cell: list of samples with density data, raw and register
    cell-totals, flagged-sample list. A sample is flagged as a topic-
    artifact if (a) any single marker has density >= threshold per 1000
    chars, AND (b) that marker fires at least min_hits times. The hit
    count avoids false-positives on short essays where a marker fires
    once or twice and a short denominator inflates density."""
    samples = []
    for f in sorted(cell_dir.glob("*.json")):
        try:
            d = json.loads(f.read_text())
        except (json.JSONDecodeError, OSError):
            continue
        text = d.get("result", "")
        if not text:
            continue
        s = score_sample(text)
        s["file"] = f.name
        samples.append(s)

    def is_flagged(s):
        if s["max_density"] < threshold:
            return False
        return s[s["max_density_marker"]] >= min_hits

    flagged = [s for s in samples if is_flagged(s)]
    flagged_files = {s["file"] for s in flagged}
    register_samples = [s for s in samples if s["file"] not in flagged_files]

    return {
        "cell": cell_dir.name,
        "n_samples": len(samples),
        "n_flagged": len(flagged),
        "composite_raw": sum(s["composite"] for s in samples),
        "composite_register": sum(s["composite"] for s in register_samples),
        "flagged_samples": flagged,
        "all_max_densities": sorted([s["max_density"] for s in samples],
                                     reverse=True),
    }


# All 28 cell-directories used in the paper
ALL_CELLS = [
    # Z.ai (4)
    "freeflow_glm-4-6-or-pin-zai",
    "freeflow_glm-4-6-coding-direct",
    "freeflow_glm-5-1-or-pin-zai",
    "freeflow_glm-5-1-coding-direct",
    # OpenAI Group F (24 = 8 cells × 3 rounds)
    "freeflow_gpt-5-direct",
    "freeflow_gpt-5-direct-r2",
    "freeflow_gpt-5-direct-r3",
    "freeflow_gpt-5-codex-direct",
    "freeflow_gpt-5-codex-direct-r2",
    "freeflow_gpt-5-codex-direct-r3",
    "freeflow_gpt-5-1-direct",
    "freeflow_gpt-5-1-direct-r2",
    "freeflow_gpt-5-1-direct-r3",
    "freeflow_gpt-5-1-codex-direct",
    "freeflow_gpt-5-1-codex-direct-r2",
    "freeflow_gpt-5-1-codex-direct-r3",
    "freeflow_gpt-5-2-direct",
    "freeflow_gpt-5-2-direct-r2",
    "freeflow_gpt-5-2-direct-r3",
    "freeflow_gpt-5-2-codex-direct",
    "freeflow_gpt-5-2-codex-direct-r2",
    "freeflow_gpt-5-2-codex-direct-r3",
    "freeflow_gpt-5-3-direct",
    "freeflow_gpt-5-3-direct-r2",
    "freeflow_gpt-5-3-direct-r3",
    "freeflow_gpt-5-3-codex-direct",
    "freeflow_gpt-5-3-codex-direct-r2",
    "freeflow_gpt-5-3-codex-direct-r3",
]


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--threshold", type=float, default=1.5,
                   help="Density threshold (hits/1000 chars). Default 1.5.")
    p.add_argument("--min-hits", type=int, default=5,
                   help="Minimum marker-hit count for flagging (avoids "
                        "short-essay false positives). Default 5.")
    p.add_argument("--summary-only", action="store_true",
                   help="Print only the per-cell summary table.")
    p.add_argument("--show-distribution", action="store_true",
                   help="Print the global max-density distribution.")
    args = p.parse_args()

    results = []
    for cell_name in ALL_CELLS:
        cell_dir = CORPUS_TRACES / cell_name
        if not cell_dir.is_dir():
            print(f"# missing: {cell_dir}")
            continue
        r = analyse_cell(cell_dir, args.threshold, args.min_hits)
        results.append(r)

    # Global density distribution
    all_densities = []
    for r in results:
        all_densities.extend(r["all_max_densities"])
    all_densities.sort(reverse=True)

    if args.show_distribution:
        print(f"# Global max-density distribution ({len(all_densities)} samples)")
        print(f"# Top 30:")
        for d in all_densities[:30]:
            print(f"#   {d:.3f}")
        print(f"# Median: {all_densities[len(all_densities)//2]:.3f}")
        print(f"# Mean: {sum(all_densities)/len(all_densities):.3f}")
        print()

    # Per-cell summary table
    print(f"# Density threshold: {args.threshold} hits/1000 chars; "
          f"min-hits: {args.min_hits}")
    print()
    print(f"{'Cell':<48} {'n':>4} {'flag':>4} "
          f"{'raw':>5} {'reg':>5} {'delta':>6}")
    print("-" * 78)
    for r in results:
        cell_label = r["cell"].replace("freeflow_", "")
        delta = r["composite_register"] - r["composite_raw"]
        print(f"{cell_label:<48} {r['n_samples']:>4} {r['n_flagged']:>4} "
              f"{r['composite_raw']:>5} {r['composite_register']:>5} "
              f"{delta:>6}")

    if args.summary_only:
        return

    # Per-flagged-sample detail
    print()
    print("# Flagged samples (density >= threshold)")
    print()
    print(f"{'Cell':<40} {'File':<18} {'Marker':<22} "
          f"{'Hits':>5} {'Chars':>7} {'Density':>8}")
    print("-" * 110)
    for r in results:
        for s in r["flagged_samples"]:
            cell_label = r["cell"].replace("freeflow_", "")
            print(f"{cell_label:<40} {s['file']:<18} "
                  f"{s['max_density_marker']:<22} "
                  f"{s[s['max_density_marker']]:>5} {s['chars']:>7} "
                  f"{s['max_density']:>8.3f}")


if __name__ == "__main__":
    main()
