---
id: a32ed35da6
question: Dim_zones.sql Dataset was not found in location US When Running fact_trips.sql
sort_order: 2300
---

To solve this error mention the location = US when creating the dim_zones table

{{ config(

materialized='table',

location='US'

) }}

Just Update this part to solve the issue and run the dim_zones again and then run the fact_trips

