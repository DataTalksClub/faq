---
id: 70072fcf7a
question: Solving dbt-Athena library conflicts
sort_order: 65
---

When working on a dbt-Athena project, do not install `dbt-athena-adapter`. Instead, always use the `dbt-athena-community` package, ensuring it matches the version of `dbt-core` to avoid compatibility conflicts.

### Best Practice

- **Always pin the versions of `dbt-core` and `dbt-athena-community` to the same version.**
  
  ```
  Example: dbt-core~=1.9.3 dbt-athena-community~=1.9.3
  ```

### Why?

- `dbt-athena-adapter` is outdated and no longer maintained.
- `dbt-athena-community` is the actively maintained package and is compatible with the latest versions of `dbt-core`.

### Steps to Avoid Conflicts

1. **Check the compatibility matrix** in the [dbt-athena-community](https://github.com/dbt-labs/dbt-adapters/tree/main/dbt-athena-community) GitHub repository.
2. **Update `requirements.txt`** to use the latest compatible versions of `dbt-core` and `dbt-athena-community`.
3. **Avoid mixing** `dbt-athena-adapter` with `dbt-athena-community` in the same environment.

By following this practice, you can avoid the conflicts we faced previously and ensure a smooth development experience.