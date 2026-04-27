# Troubleshooting and Releases Lookup

Use for errors, exceptions, support reports, failed setup/deploys, release compatibility, changelogs, and notices.

## Primary Docs

- Error handling: `references/docs/04-apis/13-error-handling/error-handling.md`
- Cloud troubleshooting: `references/docs/05-operation/02-cloud/13-cloud-troubleshooting/cloud-troubleshooting.md`
- Datomic deployment troubleshooting: `references/docs/05-operation/01-pro/03-datomic-deployment/datomic-deployment.md`
- Analytics troubleshooting: `references/docs/08-analytics/06-troubleshooting/troubleshooting.md`
- Writing a problem report: `references/docs/09-tech-notes/05-write-a-problem-report/write-a-problem-report.md`
- Releases index: `references/docs/11-releases/releases.md`
- Pro releases: `references/docs/11-releases/01-datomic-pro/01-pro-releases/pro-releases.md`
- Pro changelog: `references/docs/11-releases/01-datomic-pro/02-pro-change-log/pro-change-log.md`
- Pro release notices: `references/docs/11-releases/01-datomic-pro/03-pro-release-notices/pro-release-notices.md`
- Cloud releases: `references/docs/11-releases/02-datomic-cloud/01-cloud-releases/cloud-releases.md`
- Cloud changelog: `references/docs/11-releases/02-datomic-cloud/02-cloud-change-log/cloud-change-log.md`
- Local changelog: `references/docs/11-releases/03-datomic-local-change-log/datomic-local-change-log.md`
- Override settings: `references/docs/09-tech-notes/11-override-settings/override-settings.md`

## Best-Practice Checks

- Ask for exact error text, edition, version, API, and deployment model when troubleshooting is under-specified.
- For Datomic exceptions, check anomaly category and wrapped cause chain.
- For Cloud forbidden/access errors, check access control and credential docs before application code.
- For release questions, check release notices as well as changelogs.
- For support-bound advice, point users to problem-report guidance and avoid unsupported override recommendations.

