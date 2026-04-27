#!/usr/bin/env python3
"""Copy repository Markdown docs into the clojure-datomic skill."""

from __future__ import annotations

import argparse
import filecmp
import shutil
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
SKILL = Path(__file__).resolve().parents[1]
DOCS_DEST = SKILL / "references" / "docs"

TOP_LEVEL_DOCS = {
    "01-setup",
    "02-accessing",
    "03-tutorials",
    "04-apis",
    "05-operation",
    "06-reference",
    "07-datomic-cloud-ions",
    "08-analytics",
    "09-tech-notes",
    "10-resources",
    "11-releases",
    "12-glossary",
}

ROOT_FILES = {"introduction.md", "README.md"}


def iter_sources() -> list[Path]:
    paths: list[Path] = []
    for name in sorted(TOP_LEVEL_DOCS):
        base = ROOT / name
        if base.exists():
            paths.extend(sorted(base.rglob("*.md")))
    for name in sorted(ROOT_FILES):
        path = ROOT / name
        if path.exists():
            paths.append(path)
    return paths


def copy_docs(check: bool) -> int:
    sources = iter_sources()
    expected = {DOCS_DEST / path.relative_to(ROOT) for path in sources}
    problems: list[str] = []

    if check:
        for src in sources:
            dest = DOCS_DEST / src.relative_to(ROOT)
            if not dest.exists():
                problems.append(f"missing {dest.relative_to(SKILL)}")
            elif not filecmp.cmp(src, dest, shallow=False):
                problems.append(f"stale {dest.relative_to(SKILL)}")
        for dest in sorted(DOCS_DEST.rglob("*.md")) if DOCS_DEST.exists() else []:
            if dest not in expected:
                problems.append(f"extra {dest.relative_to(SKILL)}")
        for problem in problems:
            print(problem)
        return 1 if problems else 0

    if DOCS_DEST.exists():
        shutil.rmtree(DOCS_DEST)
    for src in sources:
        dest = DOCS_DEST / src.relative_to(ROOT)
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dest)
    print(f"copied {len(sources)} markdown docs to {DOCS_DEST.relative_to(ROOT)}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="verify copied docs are current")
    args = parser.parse_args()
    return copy_docs(args.check)


if __name__ == "__main__":
    sys.exit(main())

