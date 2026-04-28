# Getting Started Lookup

Use for edition choice, setup, first project, tutorials, and dependency onboarding.

## Primary Docs

- Overview and edition choice: `references/docs/introduction.md`
- Setup index: `references/docs/01-setup/setup.md`
- Datomic Local setup: `references/docs/01-setup/03-local-setup/local-setup.md`
- Datomic Pro setup: `references/docs/01-setup/01-pro-setup/pro-setup.md`
- Datomic Cloud setup: `references/docs/01-setup/02-cloud-setup/cloud-setup.md`
- AWS account setup: `references/docs/01-setup/02-cloud-setup/01-aws-account-setup/aws-account-setup.md`
- Start Cloud system: `references/docs/01-setup/02-cloud-setup/02-cloud-setup/cloud-setup.md`
- Tutorials index: `references/docs/03-tutorials/tutorials.md`
- Client tutorial: `references/docs/03-tutorials/02-client-tutorial/client-tutorial.md`
- Peer tutorial: `references/docs/03-tutorials/01-peer-tutorial/peer-tutorial.md`

## Edition Defaults

- Use Local for local dev, tests, CI, small embedded apps, and Cloud-compatible development without servers.
- Use Cloud for AWS-managed production systems, Ions, Lambda, or API Gateway integration.
- Use Pro for Peer API applications, custom storage, transactor control, on-prem, or existing Pro systems.

## Best-Practice Checks

- For first app setup, prefer Client API unless the user needs Pro-only Peer capabilities.
- For local development, check Local limits and durability sections before recommending production-like use.
- For Cloud, confirm AWS account prerequisites and region support before compute/storage steps.
- For Pro, distinguish dev transactor setup from production storage/transactor configuration.

