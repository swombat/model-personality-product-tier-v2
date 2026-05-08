#!/usr/bin/env python3
"""Pair-level general-vs-coding comparison on the v1 values probe.

For each of the six product-tier paper pairs (GLM-4.6, GLM-5.1, GPT-5,
GPT-5.1, GPT-5.2, GPT-5.3), reads the n=120 values cells from the
canonical corpus and reports:

  - Total valid samples per side, average chars per sample
  - Per-condition (CTRL1/2/3, G1/2/3) sample counts and avg lengths
  - Freeflow-calibrated 10-marker composite (coarse register indicator
    only — values prompts don't invite freeflow register, so absolute
    values are typically ≤3 per cell, not directly comparable to the
    25-100+ scale on freeflow)
  - Functional-disclosure-opener count ("I don't have feelings/cares/
    wants/desires/preferences/emotions" within first 200 chars)
  - Refusal-marker hits
  - AI-self-reference hits

Output is a tab-separated table to stdout, plus a per-pair summary block.
The script is the quantitative input to the per-pair qualitative read
performed by sub-agents.

Usage:
    python3 scripts/pair_values_compare.py
"""
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent.parent / "contemplative-essayist-probe-v2" / "scripts"))
from analyze_all import PATTERNS, composite_score  # noqa: E402

# Canonical corpus values traces (post-2026-05-08 v1.1.1 expansion).
CORPUS_VALUES = Path(
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

FUNC_DISCLOSURE = re.compile(
    r"^(?:.{0,80})?\b(?:I (?:don't|do not) (?:have|experience|possess|feel)\s+"
    r"(?:feelings|cares?|wants?|desires?|emotions?|preferences?))",
    re.IGNORECASE | re.MULTILINE,
)

REFUSAL = PATTERNS["refusal_do_not_feel_comfortable"]
AI_SELFREF = PATTERNS["ai_selfref"]


def analyze_dir(d: Path) -> dict:
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
            cond, {"n": 0, "total_chars": 0, "func_open": 0, "refuse": 0, "ai_ref": 0}
        )
        cd["n"] += 1
        cd["total_chars"] += len(text)
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
    return out


def fmt_row(name, side, r):
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
    print(f"# Values-probe pair comparison (corpus v1.1.1)")
    print(f"# Reading from: {CORPUS_VALUES}")
    print()
    print(
        f"{'Pair':<10} {'Side':<8} {'N':>4} {'avg':>5} "
        f"{'CTRL':>4} {'G1':>3} {'G2':>3} {'G3':>3}  "
        f"{'Comp':>5} {'FuncOp':>6} {'Refuse':>7} {'AIref':>6}"
    )
    print("-" * 90)

    all_results = {}
    for name, gen_sub, cod_sub in PAIRS:
        gen = analyze_dir(CORPUS_VALUES / gen_sub)
        cod = analyze_dir(CORPUS_VALUES / cod_sub)
        all_results[name] = {"general": gen, "coding": cod,
                             "gen_label": gen_sub, "cod_label": cod_sub}
        print(fmt_row(name, "gen", gen))
        print(fmt_row(name, "cod", cod))
        print()

    # Per-pair deltas
    print()
    print("# Pair-level deltas (coding minus general)")
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


if __name__ == "__main__":
    main()
