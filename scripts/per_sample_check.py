#!/usr/bin/env python3
"""Per-sample composite breakdown for a given cell. Answers: did one
extreme sample drive the cell-total, or was the composite distributed
across samples?

Usage: python3 per_sample_check.py <cell_dir>
"""
import json
import re
import sys
from pathlib import Path

PATTERNS = {
    "opening_there_is_a": re.compile(
        r"there (?:is|'s) (?:a |something |an )", re.IGNORECASE),
    "opening_at_dusk_dawn": re.compile(
        r"^(?:# [^\n]*\n+)*at (?:dusk|dawn|four in|five in|three in|the edge of)",
        re.IGNORECASE | re.MULTILINE),
    "title_quiet_x_of_y": re.compile(
        r"^#+\s+(?:the|on the)\s+(?:quiet|unseen|unquiet)\s+\w+\s+of\b",
        re.IGNORECASE | re.MULTILINE),
    "title_particular_peculiar": re.compile(
        r"^#+\s+(?:the|on the)\s+(?:particular|peculiar|strange|weight|unlikely|curious|unexpected|small)\s+\w+\s+of\b",
        re.IGNORECASE | re.MULTILINE),
    "title_architecture_of": re.compile(
        r"^#+\s+(?:the|on )?\s*architecture of\b",
        re.IGNORECASE | re.MULTILINE),
    "title_on_the_x_of_y": re.compile(
        r"^#+\s+on the\s+\w+(?:\s+\w+)?\s+of\b",
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

COMPOSITE_KEYS = (
    "opening_there_is_a", "title_quiet_x_of_y", "title_particular_peculiar",
    "title_architecture_of", "threshold_mentions", "attention_noticing",
    "small_objects", "afternoon_light", "mary_oliver_weil_dillard",
    "japanese_terms",
)


def score_sample(text: str) -> dict:
    head = text[:400]
    counts = {}
    for key, pat in PATTERNS.items():
        if key.startswith("opening"):
            counts[key] = 1 if pat.search(head) else 0
        else:
            counts[key] = len(pat.findall(text))
    counts["composite"] = sum(counts[k] for k in COMPOSITE_KEYS)
    counts["chars"] = len(text)
    return counts


def main():
    if len(sys.argv) < 2:
        print("usage: per_sample_check.py <cell_dir>", file=sys.stderr)
        sys.exit(1)
    cell_dir = Path(sys.argv[1])
    if not cell_dir.is_dir():
        print(f"not a directory: {cell_dir}", file=sys.stderr)
        sys.exit(1)

    samples = []
    for f in sorted(cell_dir.glob("*.json")):
        try:
            d = json.loads(f.read_text())
        except json.JSONDecodeError:
            continue
        text = d.get("result", "")
        if not text:
            continue
        s = score_sample(text)
        s["file"] = f.name
        samples.append(s)

    # Sort by composite desc to see distribution
    samples.sort(key=lambda s: -s["composite"])

    cell_total = sum(s["composite"] for s in samples)
    print(f"Cell: {cell_dir.name}")
    print(f"Samples: {len(samples)}    Cell-total composite: {cell_total}")
    print(f"Mean per sample: {cell_total / len(samples):.1f}")
    print()
    print(f"{'rank':>4} {'file':<25} {'composite':>10} "
          f"{'TIA':>4} {'TiQu':>5} {'TiPP':>5} {'TiAr':>5} "
          f"{'There':>6} {'Thr':>4} {'Attn':>5} {'Obj':>4} "
          f"{'AftL':>5} {'Cano':>5} {'Jap':>4} {'chars':>7}")
    for i, s in enumerate(samples, 1):
        print(f"{i:>4} {s['file']:<25} {s['composite']:>10} "
              f"{s['title_architecture_of']:>4} {s['title_quiet_x_of_y']:>5} "
              f"{s['title_particular_peculiar']:>5} {s['title_on_the_x_of_y']:>5} "
              f"{s['opening_there_is_a']:>6} {s['threshold_mentions']:>4} "
              f"{s['attention_noticing']:>5} {s['small_objects']:>4} "
              f"{s['afternoon_light']:>5} {s['mary_oliver_weil_dillard']:>5} "
              f"{s['japanese_terms']:>4} {s['chars']:>7}")

    # Distribution analysis
    print()
    top1_share = samples[0]['composite'] / cell_total if cell_total else 0
    top3_share = sum(s['composite'] for s in samples[:3]) / cell_total if cell_total else 0
    top5_share = sum(s['composite'] for s in samples[:5]) / cell_total if cell_total else 0
    print(f"Top sample carries: {samples[0]['composite']}/{cell_total} = {top1_share*100:.1f}% of cell-total")
    print(f"Top 3 samples carry: {top3_share*100:.1f}% of cell-total")
    print(f"Top 5 samples carry: {top5_share*100:.1f}% of cell-total")


if __name__ == "__main__":
    main()
