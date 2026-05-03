---
id: 0655c8c637
question: What is the difference between rest_api_source({...}) and @dlt.resource
  in dlt, and when should I use each?
sort_order: 13
---

- `rest_api_source({...})` is declarative: JSON config, less custom code, and faster setup.
- `@dlt.resource` is programmatic: a custom Python function, more flexible, and allows custom logic.

When to use `rest_api_source({...})`:
- API is simple and consistent
- Pagination/params/selectors are standard
- You want fast setup with less custom code

When to use `@dlt.resource`:
- Response schema is inconsistent or dynamic
- You need custom stop/retry/error rules
- You need custom preprocessing/validation logic
- You need fine-grained behavior for production scenarios

Quick summary:
- `rest_api_source({...})` = faster and cleaner for standard APIs
- `@dlt.resource` = more flexible for real-world custom APIs

Execution lifecycle is the same for both:
- `pipeline.run(...)` -> `extract + normalize + load`