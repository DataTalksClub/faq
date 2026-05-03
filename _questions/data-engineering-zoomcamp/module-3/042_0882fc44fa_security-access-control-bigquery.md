---
id: 0882fc44fa
question: How do I manage security and access control in a BigQuery data warehouse?
sort_order: 42
---

BigQuery uses Identity and Access Management (IAM) to control who can view, query, or modify datasets and tables. You can assign roles at the project, dataset, or table level depending on how granular you want permissions to be.

- Common roles:
- BigQuery Data Viewer → Read-only access to datasets and tables.
- BigQuery Data Editor → Can query and modify data.
- BigQuery Admin → Full control, including managing datasets, tables, and jobs.

- Best practices:
- Apply the principle of least privilege (give users only the access they need).
- Use authorized views to share query results without exposing the underlying raw data.
- Enable column-level security if only certain fields should be visible to specific users.
- Audit usage with INFORMATION_SCHEMA views to track who ran queries and how much data was processed.

This ensures that your BigQuery data warehouse remains secure while still enabling collaboration across teams.