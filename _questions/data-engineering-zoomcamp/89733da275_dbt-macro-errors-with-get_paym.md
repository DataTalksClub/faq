---
id: 89733da275
question: dbt macro errors with get_payment_type_description(payment_type)
section: Module 4: analytics engineering with dbt
course: data-engineering-zoomcamp
sort_order: 2790
---

You will face this issue if you copied and pasted the exact macro directly from data-engineering-zoomcamp repo.

BigQuery adapter: Retry attempt 1 of 1 after error: BadRequest('No matching signature for operator CASE for argument types: STRING, INT64, STRING, INT64, STRING, INT64, STRING, INT64, STRING, INT64, STRING, INT64, STRING, NULL at [35:5]; reason: invalidQuery, location: query, message: No matching signature for operator CASE for argument types: STRING, INT64, STRING, INT64, STRING, INT64, STRING, INT64, STRING, INT64, STRING, INT64, STRING, NULL at [35:5]')

What you’d have to do is to change the data type of the numbers (1, 2, 3 etc.) to text by inserting ‘’, as the initial ‘payment_type’ data type should be string (Note: I extracted and loaded the green trips data using Google BQ Marketplace)

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

![Image](images/data-engineering-zoomcamp/image_c3c0865e.png)

