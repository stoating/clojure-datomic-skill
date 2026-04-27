# Datomic Skill Router

Start here after reading `SKILL.md`. Pick one primary route, then use secondary routes only when the user asks for cross-cutting help.

## Route by User Intent

- **Install, choose edition, create first project, dependency coordinates, tutorials**: read `getting-started.md`, then `project-integration.md` for build tool details.
- **Clojure CLI, Maven, Leiningen, Java interop, REPL, CI, local dev workflow**: read `project-integration.md`.
- **Schema, data modeling, identity, uniqueness, transactions, query, pull, entities, history/time, EDN**: read `app-development.md`.
- **Client API, Peer API, Local API, Javadoc, index APIs, log API, stats, error handling**: read `apis.md`.
- **Datomic Cloud, Ions, entry points, Cognito, Cloud setup, monitoring, deployment, Pro/Cloud operations**: read `cloud-ions-ops.md`.
- **Analytics, SQL, Trino, JDBC, Python, R, Metabase, Superset, Jupyter**: read `analytics.md`.
- **Errors, exceptions, forbidden/busy, failed deploys, problem reports, release compatibility, changelogs**: read `troubleshooting-releases.md`.
- **Term definition**: check `glossary-index.md`, then `references/docs/12-glossary/glossary.md`.

## Edition Signals

- **Local**: local dev, CI, embedded, no server, in-memory, `:server-type :datomic-local`, `com.datomic/local`.
- **Cloud**: AWS, Ion, Lambda, API Gateway, compute group, storage stack, query group, `client-cloud`, `:server-type :ion`.
- **Pro**: transactor, Peer API, storage services, database URI, peer server, `datomic.api`, on-prem, custom storage.

## Fallback

If no route fits, search generated indexes first:

```sh
python3 skills/clojure-datomic/scripts/search_docs.py "terms from the user request"
```

Open only the most relevant hits under `skills/clojure-datomic/references/docs`.

