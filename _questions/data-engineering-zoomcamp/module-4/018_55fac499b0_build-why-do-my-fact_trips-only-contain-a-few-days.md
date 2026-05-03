---
id: 55fac499b0
question: 'Build: Why do my Fact_trips only contain a few days of data?'
sort_order: 18
---

Make sure you use:

```bash
dbt run --var 'is_test_run: false'
```
or

```bash
dbt build --var 'is_test_run: false'
```

Watch out for formatted text from this document: re-type the single quotes. If that does not work, use:

```bash
--vars '{"is_test_run": "false"}'
```

with each phrase separately quoted.