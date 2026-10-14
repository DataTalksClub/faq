---
id: 517f093406
question: "My provisioned Grafana alert stays Normal even though the dashboard shows 5xx errors. What's wrong?"
sort_order: 3
---

Check the Grafana logs first:

```bash
docker compose logs grafana --since 10m | grep -i "rule evaluator"
```

If you see `Failed to build rule evaluator` repeating every evaluation interval, the rule never actually evaluates. A common cause in provisioned YAML is that the expression nodes don't name their input. The `reduce` node needs `expression: <query refId>` and the `threshold` node needs `expression: <reduce refId>`:

```yaml
- refId: B
  datasourceUid: __expr__
  model:
    refId: B
    type: reduce
    reducer: last
    expression: A   # input: the Prometheus query
- refId: C
  datasourceUid: __expr__
  model:
    refId: C
    type: threshold
    expression: B   # input: the reduce node
    conditions:
      - evaluator: {type: gt, params: [0]}
```

If the rule sets `execErrState: OK`, evaluation errors are shown as **Normal**, which looks exactly like a quiet period. While debugging, use `execErrState: Error` so failures are visible.

After fixing the file, run `docker compose restart grafana`, because provisioning is read at startup.

Tip: build the rule once in the UI, then use **Export** on the rule to get YAML that Grafana accepts, and use that as your provisioning file.
