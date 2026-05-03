---
id: 778635395f
question: 'DBT: Running `dbt run --models stg_green_tripdata --var ''is_test_run:
  false''` is not returning anything:'
sort_order: 43
---

Use the syntax below instead if the code in the tutorial is not working.

```bash
dbt run --select stg_green_tripdata --vars '{"is_test_run": false}'
```