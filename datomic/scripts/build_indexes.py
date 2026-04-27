#!/usr/bin/env python3
"""Generate lookup indexes for the clojure-datomic skill."""

from __future__ import annotations

import argparse
import difflib
import re
import sys
from pathlib import Path


SKILL = Path(__file__).resolve().parents[1]
REFS = SKILL / "references"
DOCS = REFS / "docs"

HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*#*\s*$")
EXPLICIT_ANCHOR_RE = re.compile(r"\s+\{#([A-Za-z0-9_.:-]+)\}\s*$")

API_DOCS = [
    "04-apis/01-peer-api-clojuredoc/peer-api-clojuredoc.md",
    "04-apis/03-client-api-clojuredoc/client-api-clojuredoc.md",
    "04-apis/04-client-api/client-api.md",
    "04-apis/05-datomic-local-api/datomic-local-api.md",
    "04-apis/06-index-pull/index-pull.md",
    "04-apis/07-index-apis/index-apis.md",
    "04-apis/08-log-api/log-api.md",
    "04-apis/10-io-stats/io-stats.md",
    "04-apis/11-query-stats/query-stats.md",
    "04-apis/12-tx-stats/tx-stats.md",
    "04-apis/13-error-handling/error-handling.md",
]


def slug(text: str) -> str:
    text = re.sub(r"(?<!\\)<[^>]+>", "", text)
    text = text.replace("\\<", "<").replace("\\>", ">")
    text = re.sub(r"`([^`]*)`", r"\1", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"[*~]", "", text)
    text = text.strip().lower()
    text = re.sub(r"[^a-z0-9_\s-]", "", text)
    text = re.sub(r"\s+", "-", text)
    return text.strip("-")


def headings(path: Path) -> list[tuple[int, str, str]]:
    seen: dict[str, int] = {}
    result: list[tuple[int, str, str]] = []
    for line in path.read_text().splitlines():
        match = HEADING_RE.match(line)
        if not match:
            continue
        level = len(match.group(1))
        title = match.group(2).strip()
        explicit = EXPLICIT_ANCHOR_RE.search(title)
        if explicit:
            title = EXPLICIT_ANCHOR_RE.sub("", title).strip()
            result.append((level, title, explicit.group(1)))
            continue
        base = slug(title)
        count = seen.get(base, 0)
        seen[base] = count + 1
        anchor = base if count == 0 else f"{base}-{count}"
        result.append((level, title, anchor))
    return result


def title_for(path: Path) -> str:
    for level, title, _anchor in headings(path):
        if level == 1:
            return title
    return path.stem.replace("-", " ").title()


def generate_full_doc_index() -> str:
    lines = [
        "# Full Documentation Index",
        "",
        "Generated from bundled Markdown docs. Use this when curated lookup files do not identify a specific source.",
        "",
    ]
    for path in sorted(DOCS.rglob("*.md")):
        rel = path.relative_to(DOCS)
        lines.append(f"## {rel}")
        lines.append("")
        lines.append(f"- Title: {title_for(path)}")
        h = headings(path)
        if h:
            lines.append("- Headings:")
            for level, title, anchor in h:
                indent = "  " * max(level - 1, 0)
                lines.append(f"  - {indent}[{title}](docs/{rel}#{anchor})")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def generate_api_symbol_index() -> str:
    lines = [
        "# API Symbol Index",
        "",
        "Generated from bundled API docs. Use this to jump to API functions and API reference sections.",
        "",
    ]
    for rel_text in API_DOCS:
        path = DOCS / rel_text
        if not path.exists():
            continue
        rel = Path(rel_text)
        lines.append(f"## {title_for(path)}")
        lines.append("")
        for level, title, anchor in headings(path):
            if level >= 2:
                lines.append(f"- [{title}](docs/{rel}#{anchor})")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def generate_glossary_index() -> str:
    path = DOCS / "12-glossary" / "glossary.md"
    lines = [
        "# Glossary Index",
        "",
        "Generated from the bundled Datomic glossary.",
        "",
    ]
    if path.exists():
        rel = path.relative_to(DOCS)
        for level, title, anchor in headings(path):
            if level == 2:
                lines.append(f"- [{title}](docs/{rel}#{anchor})")
    return "\n".join(lines).rstrip() + "\n"


GENERATORS = {
    REFS / "full-doc-index.md": generate_full_doc_index,
    REFS / "api-symbol-index.md": generate_api_symbol_index,
    REFS / "glossary-index.md": generate_glossary_index,
}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="verify generated indexes are current")
    args = parser.parse_args()

    failures = 0
    for path, generator in GENERATORS.items():
        content = generator()
        if args.check:
            old = path.read_text() if path.exists() else ""
            if old != content:
                failures += 1
                print(f"stale {path.relative_to(SKILL)}")
                diff = difflib.unified_diff(
                    old.splitlines(),
                    content.splitlines(),
                    fromfile=str(path),
                    tofile=f"{path} (generated)",
                    lineterm="",
                )
                for line in list(diff)[:80]:
                    print(line)
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content)
            print(f"wrote {path.relative_to(SKILL)}")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
