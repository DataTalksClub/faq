---
id: 89733da275
images:
- description: 'image #1'
  id: image_1
  path: images/data-engineering-zoomcamp/image_c3c0865e.png
question: 'dbt: macro errors with get_payment_type_description(payment_type)'
sort_order: 28
---

You will face this issue if you copied and pasted the exact macro directly from the data-engineering-zoomcamp repo.

### Error Message

```
BigQuery adapter: Retry attempt 1 of 1 after error: BadRequest('No matching signature for operator CASE for argument types: STRING, INT64, STRING, INT64, STRING, INT64, STRING, INT64, STRING, INT64, STRING, INT64, STRING, NULL at [35:5]; reason: invalidQuery, location: query, message: No matching signature for operator CASE for argument types: STRING, INT64, STRING, INT64, STRING, INT64, STRING, INT64, STRING, INT64, STRING, INT64, STRING, NULL at [35:5]')
```

### Solution

To resolve this issue, change the data type of the numbers (1, 2, 3, etc.) to text by enclosing them in quotes. The `payment_type` data type should be a string.

#### Updated Macro

```jinja
{#
This macro returns the description of the payment_type
#}

{% macro get_payment_type_description(payment_type) -%}
    case {{ payment_type }}
        when '1' then 'Credit card'
        when '2' then 'Cash'
        when '3' then 'No charge'
        when '4' then 'Dispute'
        when '5' then 'Unknown'
        when '6' then 'Voided trip'
    end
{%- endmacro %}
```

<{IMAGE:image_1}>
