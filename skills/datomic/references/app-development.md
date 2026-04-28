# Application Development Lookup

Use for schema, modeling, identities, transactions, query, pull, entities, EDN, and time/history.

## Primary Docs

- Schema reference: `references/docs/06-reference/01-schema/01-schema-reference/schema-reference.md`
- Changing schema: `references/docs/06-reference/01-schema/02-changing-schema/changing-schema.md`
- Data modeling: `references/docs/06-reference/01-schema/03-data-modeling/data-modeling.md`
- Identity and uniqueness: `references/docs/06-reference/01-schema/04-identity-and-uniqueness/identity-and-uniqueness.md`
- Transactions index: `references/docs/06-reference/02-transactions/transactions.md`
- Transaction data: `references/docs/06-reference/02-transactions/02-transaction-data/transaction-data.md`
- Transaction functions: `references/docs/06-reference/02-transactions/04-transaction-functions/transaction-functions.md`
- Query reference: `references/docs/06-reference/03-query-and-pull/02-query-reference/query-reference.md`
- Executing queries: `references/docs/06-reference/03-query-and-pull/01-executing-queries/executing-queries.md`
- Pull: `references/docs/06-reference/03-query-and-pull/03-pull/pull.md`
- Time filters: `references/docs/06-reference/06-time-in-datomic/time-in-datomic.md`
- Entities: `references/docs/06-reference/07-entities/entities.md`
- Programming with data and EDN: `references/docs/06-reference/05-programming-with-data-and-edn/programming-with-data-and-edn.md`
- Best practices: `references/docs/06-reference/08-best-practices/best-practices.md`
- Outer joins: `references/docs/09-tech-notes/09-outer-joins/outer-joins.md`
- Composing transactions: `references/docs/09-tech-notes/02-composing-transactions-by-example/composing-transactions-by-example.md`

## Common Routes

- Unique identities, lookup refs, external keys: identity/uniqueness plus schema best practices.
- Entity relationships: data modeling plus best practices on relationship direction and component attributes.
- Transaction composition or invariants: transaction data/functions plus composing transactions.
- Query syntax, rules, predicates, aggregates: query reference.
- Optional/missing values: outer joins and query functions like `get-else`, `missing?`.
- Audit/history/as-of/since: time filters, log API, and time best practices.

## Best-Practice Checks

- Always check `06-reference/08-best-practices/best-practices.md` for schema, transaction, query, and time advice.
- Prefer lookup refs for existing entities when transacting external identities.
- Prefer pull for retrieving entity-shaped attribute values.
- Prefer query over raw index access unless the user asks for low-level index APIs or selective time/log access.
- Warn that schema grows over time; do not recommend removing or reusing names.

