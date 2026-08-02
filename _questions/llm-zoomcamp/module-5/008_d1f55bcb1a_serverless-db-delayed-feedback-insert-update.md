---
id: d1f55bcb1a
question: Does it matter which serverless database I pick for the bonus deployment
  points when user feedback arrives after the interaction is stored?
sort_order: 8
---

Yes—it can matter a lot because your write pattern is typically two-step: (1) an `INSERT` when the interaction happens, then (2) an `UPDATE` later when the user submits thumbs up/down.

Some serverless databases are optimized for streaming/fast inserts but have a “fresh insert” window during which the row cannot be updated (or behaves differently than you’d expect). If your monitoring/feedback pipeline does a delayed feedback update, that can silently break (or effectively fail) the later `UPDATE`.

For example, BigQuery can keep a newly inserted row effectively un-updatable for up to ~90 minutes due to its streaming buffer, which can break delayed feedback updates unless you change the data model.

A serverless Postgres option like Neon supports both the initial `INSERT` and a later `UPDATE` more naturally, so you usually don’t need special casing.

Practical guidance:
- Check whether your chosen serverless database supports “insert now, update later” with no restrictions.
- If your database has an update/consistency window, consider restructuring feedback into a separate table (or otherwise modeling delayed updates) to avoid updating the freshly inserted row directly.