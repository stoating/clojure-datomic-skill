---
name: datomic
description: Use for Datomic database work in Clojure and JVM projects: choosing Datomic Local, Pro, or Cloud; installing dependencies; getting started; schema and data modeling; transactions; query and pull; Client API, Peer API, Local API, index/log/stats APIs; Datomic Cloud Ions; operations; analytics; troubleshooting; releases; and Datomic best practices.
metadata:
  short-description: Datomic setup, APIs, modeling, and operations
---

# Clojure Datomic

Use this skill to answer Datomic questions without loading the full documentation by default. Prefer the smallest lookup that can answer the user, then open exact bundled documentation files when detail is needed.

## Lookup Workflow

1. Classify the request by task area and edition: Local, Pro, Cloud, or unknown.
2. Read [router.md](references/router.md).
3. Read the matching secondary reference:
   - [getting-started.md](references/getting-started.md)
   - [project-integration.md](references/project-integration.md)
   - [app-development.md](references/app-development.md)
   - [apis.md](references/apis.md)
   - [cloud-ions-ops.md](references/cloud-ions-ops.md)
   - [analytics.md](references/analytics.md)
   - [troubleshooting-releases.md](references/troubleshooting-releases.md)
4. For design, setup, API choice, performance, operational, or troubleshooting advice, check that secondary reference's best-practice section before answering.
5. Open only the specific bundled docs linked by the secondary reference. Bundled docs live under [references/docs](references/docs).
6. If routing does not find the answer, use:
   - [full-doc-index.md](references/full-doc-index.md)
   - [glossary-index.md](references/glossary-index.md)
   - `python3 scripts/search_docs.py "<query terms>"`

## Defaults

- New local development or CI: prefer Datomic Local unless the user needs Pro-only Peer features or Cloud/Ions.
- New AWS production system or Ions: prefer Datomic Cloud.
- Existing on-prem, custom storage, or Peer API applications: prefer Datomic Pro.
- Clojure projects: prefer Clojure CLI examples first, then Maven/Leiningen if requested.
- If the edition materially changes the answer and cannot be inferred, ask one concise clarification before giving edition-specific steps.

## Answer Style

- Give practical steps first, then short rationale.
- Cite bundled doc paths when the answer depends on specific Datomic behavior.
- Distinguish Client API, Peer API, and Datomic Local APIs explicitly.
- Do not browse the web for Datomic docs unless the user explicitly asks for information newer than this bundled documentation snapshot.

