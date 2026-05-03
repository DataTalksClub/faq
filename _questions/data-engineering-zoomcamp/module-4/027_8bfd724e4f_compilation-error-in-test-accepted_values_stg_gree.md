---
id: 8bfd724e4f
question: Compilation Error in test accepted_values_stg_green_tripdata_Payment_type__False___var_payment_type_values_
  (models/staging/schema.yml)  'NoneType' object is not iterable
sort_order: 27
---

In the macro `test_accepted_values` (found in `tests/generic/builtin.sql`), an error was triggered by the test `accepted_values_stg_green_tripdata_Payment_type__False___var_payment_type_values_` located in `models/staging/schema.yml`.

To resolve this issue, ensure the following variable is added to your `dbt_project.yml` file:

```yaml
vars:
  payment_type_values: [1, 2, 3, 4, 5, 6]
```