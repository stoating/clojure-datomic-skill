#!/usr/bin/env python3
"""Search bundled Datomic Markdown docs."""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path


SKILL = Path(__file__).resolve().parents[1]
DOCS = SKILL / "references" / "docs"
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*#*\s*$")


@dataclass
class Hit:
    score: int
    path: Path
    line_no: int
    heading: str
    text: str


def terms(query: str) -> list[str]:
    result: list[str] = []
    for raw in re.findall(r"[a-zA-Z0-9_:/?.-]+", query):
        term = raw.lower()
        if len(term) <= 1:
            continue
        result.append(term)
        if term.endswith("s") and len(term) > 3:
            result.append(term[:-1])
        elif term.isalpha() and len(term) > 2:
            result.append(f"{term}s")
    return list(dict.fromkeys(result))


def title_for(lines: list[str], path: Path) -> str:
    for line in lines:
        m = HEADING_RE.match(line)
        if m and len(m.group(1)) == 1:
            return m.group(2).strip()
    return path.stem.replace("-", " ").title()


def search(query: str, limit: int) -> list[Hit]:
    qs = terms(query)
    hits: list[Hit] = []
    for path in sorted(DOCS.rglob("*.md")):
        lines = path.read_text(errors="replace").splitlines()
        title = title_for(lines, path)
        current_heading = title
        for idx, line in enumerate(lines, start=1):
            heading = HEADING_RE.match(line)
            if heading:
                current_heading = heading.group(2).strip()
            hay = f"{path.relative_to(DOCS)} {current_heading} {line}".lower()
            matched = [term for term in qs if term in hay]
            if not matched:
                continue
            score = len(matched)
            if heading:
                score += 5
            if any(term in title.lower() for term in qs):
                score += 4
            if any(term in str(path).lower() for term in qs):
                score += 3
            hits.append(Hit(score, path, idx, current_heading, line.strip()))
    hits.sort(key=lambda h: (-h.score, str(h.path), h.line_no))
    return hits[:limit]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("query", help="search query")
    parser.add_argument("--limit", type=int, default=20)
    args = parser.parse_args()
    for hit in search(args.query, args.limit):
        rel = hit.path.relative_to(DOCS)
        print(f"{rel}:{hit.line_no}: {hit.heading} :: {hit.text}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
