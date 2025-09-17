---
course: data-engineering-zoomcamp
id: adaf994857
question: "Replace: \n{{ dbt_utils.surrogate_key([ \n     field_a, \n     field_b,\
  \ \n     field_c,\n     …,\n     field_z     \n]) }}"
section: 'Module 4: analytics engineering with dbt'
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

