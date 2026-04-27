# Project Integration Lookup

Use for dependency coordinates, build tools, REPL setup, Java interop, and local/CI workflows.

## Primary Docs

- Accessing index: `references/docs/02-accessing/accessing.md`
- Client library: `references/docs/02-accessing/02-client-library/client-library.md`
- Peer library: `references/docs/02-accessing/01-peer-library/peer-library.md`
- Datomic Local setup: `references/docs/01-setup/03-local-setup/local-setup.md`
- Pro Client getting started: `references/docs/05-operation/01-pro/16-pro-client-getting-started/pro-client-getting-started.md`
- Peer Server: `references/docs/05-operation/01-pro/15-peer-server/peer-server.md`
- Language support: `references/docs/05-operation/01-pro/17-language-support/language-support.md`
- Private Maven hosting: `references/docs/09-tech-notes/03-hosting-private-maven/hosting-private-maven.md`

## Build Tool Routing

- Clojure CLI: use `deps.edn` examples first.
- Maven: use XML dependency snippets from Client/Peer library docs.
- Leiningen: use vector dependency snippets when requested.
- Java: use Javadoc and Peer API Java class docs for Peer applications.

## Best-Practice Checks

- Prefer Datomic Local for repeatable tests and CI unless Pro transactor behavior is required.
- Keep dependency advice edition-specific: `com.datomic/local`, `client-cloud`, `client-pro`, or Peer library are not interchangeable.
- For Pro Peer usage, remind users about transactor/storage requirements.
- For Cloud-compatible local development, point to `divert-system` in the Local API.

