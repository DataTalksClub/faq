---
id: adaf994857
question: Replace: 
{{ dbt_utils.surrogate_key([ 
     field_a, 
     field_b, 
     field_c,
     …,
     field_z     
]) }}
section: Module 4: analytics engineering with dbt
course: data-engineering-zoomcamp
sort_order: 2670
---

For this instead:
{{ dbt_utils.generate_surrogate_key([ 
     field_a, 
     field_b, 
     field_c,
     …,
     field_z
]) }}

add a global variable in dbt_project.yml(...)

