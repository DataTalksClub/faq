---
course: data-engineering-zoomcamp
id: a250f11737
question: What is the fastest way to upload taxi data to dbt-postgres?
section: 'Module 4: analytics engineering with dbt'
sort_order: 3220
---

Use the PostgreSQL COPY FROM feature that is compatible with csv files

First create the table like (as an example):

CREATE TABLE taxis (

…

);

And then use copy functionality (as an example):

COPY taxis FROM PROGRAM

‘url'

WITH (

FORMAT csv,

HEADER true,

ENCODING utf8

);

COPY table_name [ ( column_name [, ...] ) ]

FROM { 'filename' | PROGRAM 'command' | STDIN }

[ [ WITH ] ( option [, ...] ) ]

[ WHERE condition ]

