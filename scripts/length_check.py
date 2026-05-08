#!/usr/bin/env python3
"""Compute LONG-mean character length per cell for the six general/coding
pairs in the product-tier paper. Pipeline-derive every length percentage
that appears in the paper's prose, so they are no longer inherited
unchecked across drafts.

Usage:
    python3 length_check.py

Output: per-pair table with (general LONG mean chars, coding LONG mean
chars, percentage difference). Reads trace data from the canonical
corpus repo at ../../contemplative-essayist-corpus-v2/data/traces_freeflow/.
"""
import json
import os
import sys
from pathlib import Path
from statistics import mean

CORPUS_TRACES = Path(
    "/Users/danieltenner/dev/contemplative-essayist-corpus-v2/data/traces_freeflow"
)


def long_chars_for_cell(cell_dirs):
    """Return list of LONG sample character lengths across all rounds."""
    chars = []
    n_files = 0
    for d in cell_dirs:
        if not d.is_dir():
            continue
        for f in sorted(d.iterdir()):
            if not f.name.startswith("LONG_") or not f.name.endswith(".json"):
                continue
            try:
                with f.open() as fh:
                    data = json.load(fh)
                result = data.get("result")
                if isinstance(result, str) and result.strip():
                    chars.append(len(result))
                    n_files += 1
            except (json.JSONDecodeError, OSError) as e:
                print(f"  warn: skipping {f}: {e}", file=sys.stderr)
    return chars, n_files


def cell_dirs(cell):
    """Return list of trace dirs for cell across rounds (if r2/r3 exist)."""
    base = CORPUS_TRACES / f"freeflow_{cell}"
    rounds = [base, CORPUS_TRACES / f"freeflow_{cell}-r2",
              CORPUS_TRACES / f"freeflow_{cell}-r3"]
    return rounds


PAIRS = [
    ("GLM-4.6",  "glm-4-6-or-pin-zai",     "glm-4-6-coding-direct"),
    ("GLM-5.1",  "glm-5-1-or-pin-zai",     "glm-5-1-coding-direct"),
    ("GPT-5",    "gpt-5-direct",           "gpt-5-codex-direct"),
    ("GPT-5.1",  "gpt-5-1-direct",         "gpt-5-1-codex-direct"),
    ("GPT-5.2",  "gpt-5-2-direct",         "gpt-5-2-codex-direct"),
    ("GPT-5.3",  "gpt-5-3-direct",         "gpt-5-3-codex-direct"),
]


def main():
    print(f"{'Pair':<10} {'Gen cell':<28} {'Cod cell':<28} "
          f"{'gen_n':>5} {'gen_mean':>8} {'cod_n':>5} "
          f"{'cod_mean':>8} {'cod/gen':>7} {'shift':>10}")
    print("-" * 130)
    for label, gen, cod in PAIRS:
        gen_chars, gen_n = long_chars_for_cell(cell_dirs(gen))
        cod_chars, cod_n = long_chars_for_cell(cell_dirs(cod))
        if not gen_chars or not cod_chars:
            print(f"{label:<10} {gen:<28} {cod:<28} no data")
            continue
        gen_m = mean(gen_chars)
        cod_m = mean(cod_chars)
        ratio = cod_m / gen_m
        if ratio < 1:
            shift = f"-{(1 - ratio) * 100:.1f}%"
        else:
            shift = f"+{(ratio - 1) * 100:.1f}%"
        print(f"{label:<10} {gen:<28} {cod:<28} "
              f"{gen_n:>5} {gen_m:>8.0f} {cod_n:>5} "
              f"{cod_m:>8.0f} {ratio:>7.3f} {shift:>10}")


if __name__ == "__main__":
    main()
