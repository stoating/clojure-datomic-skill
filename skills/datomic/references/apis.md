# API Lookup

Use for API selection, function signatures, sync/async behavior, Local API, Peer API, Client API, Java API, and stats/error APIs.

## Primary Docs

- API index: `references/docs/04-apis/apis.md`
- Client API clojuredoc: `references/docs/04-apis/03-client-api-clojuredoc/client-api-clojuredoc.md`
- Client library reference: `references/docs/04-apis/04-client-api/client-api.md`
- Peer API clojuredoc: `references/docs/04-apis/01-peer-api-clojuredoc/peer-api-clojuredoc.md`
- Peer API Javadoc: `references/docs/04-apis/02-peer-api-javadoc/peer-api-javadoc.md`
- Datomic Local API: `references/docs/04-apis/05-datomic-local-api/datomic-local-api.md`
- Index APIs: `references/docs/04-apis/07-index-apis/index-apis.md`
- Index pull: `references/docs/04-apis/06-index-pull/index-pull.md`
- Log API: `references/docs/04-apis/08-log-api/log-api.md`
- REST API: `references/docs/04-apis/09-rest-api/rest-api.md`
- IO stats: `references/docs/04-apis/10-io-stats/io-stats.md`
- Query stats: `references/docs/04-apis/11-query-stats/query-stats.md`
- Tx stats: `references/docs/04-apis/12-tx-stats/tx-stats.md`
- Error handling: `references/docs/04-apis/13-error-handling/error-handling.md`
- Generated API symbols: `api-symbol-index.md`

## API Choice

- Client API: default for Local, Cloud, library code, and broad edition compatibility.
- Peer API: Pro-only applications that need in-process database values, lazy entities, or Pro-specific features.
- Local API: Local-specific helpers such as `divert-system`, `release-db`, and `import-cloud`.
- Java/Javadoc: Peer API Java applications or Java type/member questions.

## Best-Practice Checks

- Choose API by edition and deployment model before giving code.
- For async Client usage, check error handling and channel behavior.
- For performance investigation, pair query/tx/io stats docs with the relevant query or transaction docs.
- For raw index/log use, check whether query/pull would be more appropriate first.

