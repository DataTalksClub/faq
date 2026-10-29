---
id: cc4d23c338
question: 'Homework 5 deployment: Why does the /predict API accept invalid categorical
  values and out-of-range numbers (HTTP 200 instead of 422)?'
sort_order: 78
---

In the provided homework service, the API mainly validates types (and sometimes basic Pydantic coercion), not semantic value constraints.

That’s why requests like `lead_source: "Paid_Ads"` (different capitalization) or `lead_source: "tiktok"` can still return HTTP 200: the model’s preprocessing uses a `DictVectorizer`/one-hot encoding fitted on the training categories, and unseen categories are effectively ignored/encoded as zeros, producing a valid probability.

Similarly, `interaction_count: -3` returns 200 when the request model does not include `ge`/`le` constraints for that field. Pydantic will accept an `int` even if it’s negative unless you explicitly constrain allowed ranges.

By contrast, HTTP 422 typically happens when the field type/format can’t be coerced to the declared type. For example, `number_of_courses_viewed: 2.5` fails if the model declares the field as an `int`.

What to do in a real service:
- Add value/range constraints to the Pydantic request model using `Field(...)` (e.g., `ge=0`, `lt=...`).
- Normalize/clean categorical strings (e.g., lowercase and replace spaces with underscores) so `