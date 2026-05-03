---
id: a4c1f2e983
question: 'dbt: relationships test fails with "depends on a node named ''taxi_zone_lookup.csv''
  which was not found"'
sort_order: 63
---

The warning indicates that dbt is trying to reference a model or seed named `taxi_zone_lookup.csv`, but the `ref()` function takes the *model name*, not the file name — so the `.csv` suffix should not be part of the reference.

Wrong:

```yaml
- relationships:
    to: ref('taxi_zone_lookup.csv')
    field: locationid
```

Correct:

```yaml
- relationships:
    to: ref('taxi_zone_lookup')
    field: locationid
```
