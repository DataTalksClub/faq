---
id: 78fda262c6
question: How does dbt handle dependencies between models?
sort_order: 54
---

Dbt provides a mechanism called `ref` to manage dependencies between models. By referencing other models using the `ref` keyword in SQL, dbt automatically understands the dependencies and ensures the correct execution order.