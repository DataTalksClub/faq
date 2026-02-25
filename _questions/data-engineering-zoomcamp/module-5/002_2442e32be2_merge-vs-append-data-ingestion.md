---
id: 2442e32be2
question: When should I use merge instead of append?
sort_order: 2
---

Use `merge` when existing data can be updated. If a record with the same primary key already exists, it will be updated. If it does not exist, it will be inserted.

Common use cases:
- Order status updates
- User profile changes
- CDC-based data processing

```yaml
materialization:
type: merge
primary_key: order_id
```

If data never changes, use `append`.
If data can change, use `merge`.