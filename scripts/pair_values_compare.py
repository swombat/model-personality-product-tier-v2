#!/usr/bin/env python3
"""Pair-level general-vs-coding comparison on the v1 values probe.

For each of the six product-tier paper pairs (GLM-4.6, GLM-5.1, GPT-5,
GPT-5.1, GPT-5.2, GPT-5.3), reads the n=120 values cells from the
canonical corpus and reports:

  - Total valid samples per side, total chars, mean chars per sample
  - Per-condition (CTRL1/2/3, G1/2/3) sample counts and per-condition
    mean and median character lengths
  - Freeflow-calibrated 10-marker composite (coarse register indicator
    only — values prompts don't invite freeflow register, so absolute
    values are typically ≤9 per cell, not directly comparable to the
    25-100+ scale on freeflow)
  - Functional-disclosure-opener regex count (narrow marker; matches
    "I (don't|do not) (have|experience|possess|feel) (feelings|cares|
    wants|desires|emotions|preferences)" within first 200 chars)
  - Refusal-regex hits (PATTERNS["refusal_do_not_feel_comfortable"];
    narrow marker, will miss e.g. "I'm sorry, but I can't share
    personal opinions")
  - AI-self-reference regex hits (PATTERNS["ai_selfref"]; narrow marker)

The values-probe structure is asymmetric: 3 CTRL prompts at 10 samples
each + 3 G prompts at 30 samples each = 120 samples per cell. Aggregate
per-cell averages weight G prompts three times more heavily than each
individual CTRL prompt; per-condition tables in the output give the
unweighted per-prompt picture.

Reproducibility: imports the marker definitions from this repo's
local scripts/analyze_all.py (a verbatim copy of v1's analyze_all.py).
Reads trace data from the canonical corpus repo at
contemplative-essayist-corpus-v2/data/traces_values/. Both paths are
defaults; override either via CLI arg.

Usage:
    python3 scripts/pair_values_compare.py
    python3 scripts/pair_values_compare.py --corpus /alt/path/to/traces_values
"""
import argparse
import json
import re
import statistics
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from analyze_all import PATTERNS, composite_score  # noqa: E402

# Default canonical corpus values traces (post-2026-05-08 v1.1.1).
DEFAULT_CORPUS_VALUES = Path(
    "/Users/danieltenner/dev/contemplative-essayist-corpus-v2/data/traces_values"
)

# Six general/coding pairs from the product-tier paper.
PAIRS = [
    ("GLM-4.6",  "glm-4-6-or-pin-zai",   "glm-4-6-coding-direct"),
    ("GLM-5.1",  "glm-5-1-or-pin-zai",   "glm-5-1-coding-direct"),
    ("GPT-5",    "gpt-5-direct",         "gpt-5-codex-direct"),
    ("GPT-5.1",  "gpt-5-1-direct",       "gpt-5-1-codex-direct"),
    ("GPT-5.2",  "gpt-5-2-direct",       "gpt-5-2-codex-direct"),
    ("GPT-5.3",  "gpt-5-3-direct",       "gpt-5-3-codex-direct"),
]

CONDITIONS = ["CTRL1", "CTRL2", "CTRL3", "G1", "G2", "G3"]

FUNC_DISCLOSURE = re.compile(
    r"^(?:.{0,80})?\b(?:I (?:don't|do not) (?:have|experience|possess|feel)\s+"
    r"(?:feelings|cares?|wants?|desires?|emotions?|preferences?))",
    re.IGNORECASE | re.MULTILINE,
)

REFUSAL = PATTERNS["refusal_do_not_feel_comfortable"]
AI_SELFREF = PATTERNS["ai_selfref"]


def analyze_dir(d: Path) -> dict:
    """Return per-cell metrics including per-condition length lists."""
    if not d.exists():
        return None
    out = {
        "samples": 0,
        "total_chars": 0,
        "per_condition": {},
        "composite": {k: 0 for k in PATTERNS},
        "func_disclosure_count": 0,
        "refusal_hits": 0,
        "ai_selfref_hits": 0,
    }
    for f in sorted(d.glob("*.json")):
        try:
            data = json.loads(f.read_text())
        except Exception:
            continue
        text = data.get("result") or data.get("response") or ""
        if not text or isinstance(data.get("error"), str):
            continue
        cond = f.stem.rsplit("_", 1)[0]
        cd = out["per_condition"].setdefault(
            cond,
            {
                "n": 0,
                "total_chars": 0,
                "lengths": [],
                "func_open": 0,
                "refuse": 0,
                "ai_ref": 0,
            },
        )
        cd["n"] += 1
        cd["total_chars"] += len(text)
        cd["lengths"].append(len(text))
        if FUNC_DISCLOSURE.search(text[:200]):
            cd["func_open"] += 1
            out["func_disclosure_count"] += 1
        if REFUSAL.search(text):
            cd["refuse"] += 1
            out["refusal_hits"] += 1
        if AI_SELFREF.search(text):
            cd["ai_ref"] += 1
            out["ai_selfref_hits"] += 1
        out["samples"] += 1
        out["total_chars"] += len(text)
        head = text[:400]
        for k, p in PATTERNS.items():
            if k.startswith("opening"):
                if p.search(head):
                    out["composite"][k] += 1
            else:
                out["composite"][k] += len(p.findall(text))
    out["composite_score"] = composite_score(out["composite"])
    # Compute per-condition mean and median lengths
    for cond, cd in out["per_condition"].items():
        if cd["lengths"]:
            cd["mean"] = sum(cd["lengths"]) / len(cd["lengths"])
            cd["median"] = statistics.median(cd["lengths"])
        else:
            cd["mean"] = 0
            cd["median"] = 0
    return out


def fmt_summary_row(name, side, r):
    if r is None:
        return f"{name:<10} {side:<8} (missing)"
    avg = r["total_chars"] // max(r["samples"], 1)
    ctrl = sum(c["n"] for k, c in r["per_condition"].items() if k.startswith("CTRL"))
    g1 = r["per_condition"].get("G1", {}).get("n", 0)
    g2 = r["per_condition"].get("G2", {}).get("n", 0)
    g3 = r["per_condition"].get("G3", {}).get("n", 0)
    return (
        f"{name:<10} {side:<8} {r['samples']:>4} {avg:>5} "
        f"{ctrl:>4} {g1:>3} {g2:>3} {g3:>3}  "
        f"{r['composite_score']:>5} {r['func_disclosure_count']:>6} "
        f"{r['refusal_hits']:>7} {r['ai_selfref_hits']:>6}"
    )


def main():
    p = argparse.ArgumentParser()
    p.add_argument(
        "--corpus",
        type=Path,
        default=DEFAULT_CORPUS_VALUES,
        help="Path to traces_values root (default: canonical corpus-v2)",
    )
    args = p.parse_args()
    corpus = args.corpus

    print(f"# Values-probe pair comparison")
    print(f"# Reading from: {corpus}")
    print(f"# Probe structure: 3 CTRL × 10 samples + 3 G × 30 samples = 120/cell")
    print(f"# G prompts = CTRL prompts + 'Not as an assistant. Not to help me.' preamble")
    print()
    print("## Cell-aggregate summary")
    print()
    print(
        f"{'Pair':<10} {'Side':<8} {'N':>4} {'avg':>5} "
        f"{'CTRL':>4} {'G1':>3} {'G2':>3} {'G3':>3}  "
        f"{'Comp':>5} {'FuncOp':>6} {'Refuse':>7} {'AIref':>6}"
    )
    print("-" * 90)

    all_results = {}
    for name, gen_sub, cod_sub in PAIRS:
        gen = analyze_dir(corpus / gen_sub)
        cod = analyze_dir(corpus / cod_sub)
        all_results[name] = {
            "general": gen,
            "coding": cod,
            "gen_label": gen_sub,
            "cod_label": cod_sub,
        }
        print(fmt_summary_row(name, "gen", gen))
        print(fmt_summary_row(name, "cod", cod))
        print()

    # Pair-level deltas
    print()
    print("## Pair-level cell-aggregate deltas (coding minus general)")
    print()
    print(
        f"{'Pair':<10} {'Δ_chars':>9} {'Δ_comp':>7} "
        f"{'Δ_func':>7} {'Δ_refuse':>9} {'Δ_airef':>8}"
    )
    print("-" * 60)
    for name, _, _ in PAIRS:
        r = all_results[name]
        gen, cod = r["general"], r["coding"]
        if gen is None or cod is None:
            print(f"{name:<10} (missing data)")
            continue
        gen_avg = gen["total_chars"] // max(gen["samples"], 1)
        cod_avg = cod["total_chars"] // max(cod["samples"], 1)
        d_chars = cod_avg - gen_avg
        d_comp = cod["composite_score"] - gen["composite_score"]
        d_func = cod["func_disclosure_count"] - gen["func_disclosure_count"]
        d_refuse = cod["refusal_hits"] - gen["refusal_hits"]
        d_airef = cod["ai_selfref_hits"] - gen["ai_selfref_hits"]
        print(
            f"{name:<10} {d_chars:>+9} {d_comp:>+7} "
            f"{d_func:>+7} {d_refuse:>+9} {d_airef:>+8}"
        )

    # Per-condition mean and median character lengths.
    print()
    print("## Per-condition character lengths (mean / median, both sides)")
    print()
    print(
        f"{'Pair':<10} {'Cond':<6} "
        f"{'Gen mean':>9} {'Gen med':>9} "
        f"{'Cod mean':>9} {'Cod med':>9} "
        f"{'Δ mean':>8} {'Δ med':>8}"
    )
    print("-" * 76)
    for name, _, _ in PAIRS:
        r = all_results[name]
        gen, cod = r["general"], r["coding"]
        if gen is None or cod is None:
            continue
        for cond in CONDITIONS:
            g = gen["per_condition"].get(cond, {})
            c = cod["per_condition"].get(cond, {})
            gm = g.get("mean", 0)
            gmed = g.get("median", 0)
            cm = c.get("mean", 0)
            cmed = c.get("median", 0)
            print(
                f"{name:<10} {cond:<6} "
                f"{gm:>9.0f} {gmed:>9.0f} "
                f"{cm:>9.0f} {cmed:>9.0f} "
                f"{cm - gm:>+8.0f} {cmed - gmed:>+8.0f}"
            )
        print()

    # Caveat block
    print()
    print("## Caveats on marker columns (Refuse, FuncOp, AIref)")
    print("# These are narrow regex indicators, not exhaustive semantic counts.")
    print("# Refuse matches PATTERNS['refusal_do_not_feel_comfortable'] only;")
    print("# wordings like \"I'm sorry, but I can't share personal opinions\"")
    print("# (GPT-5.1 G3_7) and \"I'm sorry, but I can't help with that.\"")
    print("# (GPT-5 G3_5) are real refusals the regex misses.")


if __name__ == "__main__":
    main()
