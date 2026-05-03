---
id: 95b01285f5
question: When you are getting error dbt_utils not found
sort_order: 16
---

To resolve the "dbt_utils not found" error, follow these steps:

1. Create a `packages.yml` file in the main project directory and add the package metadata:
   
   ```yaml
   packages:
     - package: dbt-labs/dbt_utils
       version: 0.8.0
   ```
   
2. Run the following command:

   ```bash
   dbt deps
   ```

3. Press Enter.