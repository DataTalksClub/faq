---
course: data-engineering-zoomcamp
id: 55fac499b0
question: Build - Why do my Fact_trips only contain a few days of data?
section: 'Module 4: analytics engineering with dbt'
sort_order: 2640
---

Make sure you use:

dbt run --var ‘is_test_run: false’ or

dbt build --var ‘is_test_run: false’

(watch out for formatted text from this document: re-type the single quotes). If that does not work, use --vars '{'is_test_run': 'false'}' with each phrase separately quoted.

