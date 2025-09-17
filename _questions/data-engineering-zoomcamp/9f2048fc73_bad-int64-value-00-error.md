---
id: 9f2048fc73
question: Bad int64 value: 0.0 error
section: Module 4: analytics engineering with dbt
course: data-engineering-zoomcamp
sort_order: 2930
---

Some ehail fees are null and casting them to integer gives Bad int64 value: 0.0 error,

Solution:

Using safe_cast returns NULL instead of throwing an error. So use safe_cast from dbt_utils function in the jinja code for casting into integer as follows:

{{ dbt_utils.safe_cast('ehail_fee',  api.Column.translate_type("integer"))}} as ehail_fee,

Can also just use safe_cast(ehail_fee as integer) without relying on dbt_utils.

