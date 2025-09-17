---
course: data-engineering-zoomcamp
id: 1d2222e38a
question: CREATE TABLE has columns with duplicate name locationid.
section: 'Module 4: analytics engineering with dbt'
sort_order: 2920
---

This error could result if you are using some select * query without mentioning the name of table for ex:

with dim_zones as (

select * from `engaged-cosine-374921`.`dbt_victoria_mola`.`dim_zones`

where borough != 'Unknown'

),

fhv as (

select * from `engaged-cosine-374921`.`dbt_victoria_mola`.`stg_fhv_tripdata`

)

select * from fhv

inner join dim_zones as pickup_zone

on fhv.PUlocationID = pickup_zone.locationid

inner join dim_zones as dropoff_zone

on fhv.DOlocationID = dropoff_zone.locationid

);

To resolve just replace use : select fhv.* from fhv

