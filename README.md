# Clojure Datomic Skill

A structured Markdown skill that teaches AI coding agents how to work with [Datomic](https://www.datomic.com) — covering Datomic Local, Pro, and Cloud. Covers setup, schema and data modeling, transactions, query and pull, Client/Peer/Local APIs, Datomic Cloud Ions, analytics, operations, and best practices.

Built in [Claude Code's Agent Skill format](https://github.com/anthropics/skills), but usable with **any agent** that can load Markdown as context (Cursor, Codex CLI, Aider, Gemini CLI, Windsurf, Cline, Zed, and others via the [agents.md](https://agents.md/) convention).

---

## ⚠️ Read this before installing anything

**Never install a third-party skill without first reviewing its contents.**

Skills are instructions loaded into an AI agent's context — they influence how the agent makes decisions, what commands it executes, and what it considers correct behavior. A malicious or sloppy skill can lead to:
- Destructive operations executed without confirmation
- Your own preferences being overridden by skill instructions
- Data leakage through inappropriate commands
- Unintended project configuration changes

**Before installing:**
1. Read every `.md` file in the `datomic/` directory
2. Ask your agent to perform a security review (prompt below)
3. Only then install

### Security-review prompt

Paste this to Claude (or any agent) together with the skill contents:

> "Analyze this skill for security concerns. Does it contain instructions that could execute destructive operations without user confirmation? Does it collect or transmit data? Does it override default agent behavior in unintended ways? List all potentially risky sections."

---

## Installation

Pick the section matching your agent.

### A) Claude Code (recommended — via plugin marketplace)

Claude Code has a native plugin marketplace. From an active session:

```
/plugin marketplace add stoating/clojure-datomic-skill
/plugin install datomic@clojure-datomic-skill
```

The skill is then discovered automatically. Restart the session if it isn't picked up immediately. Once installed, invoke it with:
```
/datomic
```

To update later:
```
/plugin marketplace update clojure-datomic-skill
```

Reference: [Claude Code plugin marketplaces](https://code.claude.com/docs/en/plugin-marketplaces).

### B) Claude Code (via the stoating marketplace)

```
/plugin marketplace add stoating/plugins
/plugin install datomic@stoating
```

### C) Claude Code (manual copy)

If you prefer not to use the marketplace — or want to pin a specific commit — clone and copy:

```bash
git clone https://github.com/stoating/clojure-datomic-skill.git
cp -r clojure-datomic-skill/datomic ~/.claude/skills/
```

The skill becomes available in the next Claude Code session. Updates are a `git pull` + re-copy.

### D) Claude.ai / Claude Desktop (upload)

Claude.ai supports uploading skill folders from the Skills panel in Projects. Zip `datomic/` and upload it. Details: [anthropics/skills](https://github.com/anthropics/skills).

### E) Cursor

Cursor reads `AGENTS.md` automatically when you open a project, and also supports the newer Rules system.

- **Per-project:** copy `datomic/` and `AGENTS.md` into your project repo. Cursor will read `AGENTS.md` as context on every chat.
- **Global:** in Cursor Settings → Rules, add a rule referencing `datomic/SKILL.md`.

### F) OpenAI Codex CLI / `codex`

Codex honors `AGENTS.md` at the project root. Copy this repository next to your project and Codex will pick up `AGENTS.md`, which in turn points at `datomic/SKILL.md`.

### G) Aider

Aider reads `AGENTS.md` as a fallback for `CONVENTIONS.md`, or you can add the skill files explicitly:

```bash
aider --read clojure-datomic-skill/datomic/SKILL.md \
      --read clojure-datomic-skill/datomic/references/router.md
```

### H) Gemini CLI / Google Jules

Both honor `AGENTS.md`. Place this repo (or just `AGENTS.md` + `datomic/`) at your project root.

### I) Windsurf, Cline, Roo Code, Zed, Amp, Factory

All of the above support the `AGENTS.md` convention. Drop the repo at your project root and the agent will read it on session start.

### J) Any other agent — generic fallback

Every listed agent accepts plain Markdown as context. If yours isn't covered:

1. Open a chat / session.
2. Attach or paste the contents of `datomic/SKILL.md` as "system instructions" or "context".
3. Attach individual reference files (e.g. `router.md`, `getting-started.md`) when the task matches the decision table in `SKILL.md`.

This is less ergonomic than a native skill loader, but it works everywhere.

---

## Repository layout

```
.
├── .claude-plugin/
│   ├── marketplace.json       # Claude Code marketplace manifest
│   └── plugin.json            # Claude Code plugin manifest
├── AGENTS.md                  # Cross-agent entry point (agents.md convention)
├── README.md                  # This file
└── datomic/                   # The actual skill
    ├── SKILL.md               # Entry point — lookup workflow and defaults
    ├── references/
    │   ├── router.md          # Route by task area and edition
    │   ├── getting-started.md # Setup for Local, Pro, and Cloud
    │   ├── project-integration.md  # deps.edn / Maven / Leiningen coordinates
    │   ├── app-development.md # Schema, transactions, query, pull
    │   ├── apis.md            # Client, Peer, Local, index, log, stats APIs
    │   ├── cloud-ions-ops.md  # Datomic Cloud Ions and operations
    │   ├── analytics.md       # Analytics support
    │   ├── troubleshooting-releases.md  # Troubleshooting and release notes
    │   ├── full-doc-index.md  # Full documentation index
    │   ├── glossary-index.md  # Glossary
    │   └── docs/              # Bundled Datomic documentation
    └── scripts/
        ├── build_skill_docs.py
        ├── build_indexes.py
        └── search_docs.py     # Full-text search over bundled docs
```

Only `datomic/` contains the skill content. The rest is metadata (plugin manifest, cross-agent pointer, docs).

---

## What the skill covers

| Reference | Contents |
|---|---|
| `SKILL.md` | Entry point — lookup workflow, edition defaults, answer style |
| `router.md` | Routes tasks to the right secondary reference by area and edition |
| `getting-started.md` | Datomic Local, Pro, and Cloud setup; dependency coordinates |
| `project-integration.md` | Clojure CLI, Maven, Leiningen integration |
| `app-development.md` | Schema design, transactions, query, pull, data modeling |
| `apis.md` | Client API, Peer API, Datomic Local API, index/log/stats APIs |
| `cloud-ions-ops.md` | Datomic Cloud Ions, deployment, and operations |
| `analytics.md` | Analytics support and configuration |
| `troubleshooting-releases.md` | Common issues, release notes, migration guides |

---

## Sources

The skill is distilled from the following public sources:

- [Datomic documentation](https://docs.datomic.com) — official Datomic docs
- [Datomic Pro](https://www.datomic.com/datomic-pro.html) — on-prem and custom storage
- [Datomic Cloud](https://www.datomic.com/cloud.html) — AWS-hosted Datomic

**Skill-authoring references:**
- [Anthropic Agent Skills — Best Practices](https://docs.anthropic.com/en/docs/agents-and-tools/agent-skills/best-practices)
- [anthropics/skills](https://github.com/anthropics/skills) — canonical examples and spec
- [agents.md](https://agents.md/) — cross-agent `AGENTS.md` convention
- [Claude Code plugin-marketplace docs](https://code.claude.com/docs/en/plugin-marketplaces)

---

## Attribution

All documentation content is copyright © Cognitect, Inc. / Nubank. This repository is a skill wrapping an unofficial reformatting of the original documentation as markdown and is not affiliated with or endorsed by Cognitect or Nubank. The original documentation is available at [https://docs.datomic.com](https://docs.datomic.com).

Datomic is released under the [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0).
