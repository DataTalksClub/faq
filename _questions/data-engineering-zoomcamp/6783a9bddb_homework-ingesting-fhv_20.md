---
course: data-engineering-zoomcamp
id: 6783a9bddb
question: Homework - Ingesting FHV_20?? data
section: 'Module 4: analytics engineering with dbt'
sort_order: 3110
---

Issue: If you’re having problems loading the FHV_20?? data from the github repo into GCS and then into BQ (input file not of type parquet), you need to do two things. First, append the URL Template link with ‘?raw=true’ like so:

URL_TEMPLATE = URL_PREFIX + "/fhv_tripdata_{{ execution_date.strftime(\'%Y-%m\') }}.parquet?raw=true"

Second, update make sure the URL_PREFIX is set to the following value:

URL_PREFIX = ""

It is critical that you use this link with the keyword blob. If your link has ‘tree’ here, replace it. Everything else can stay the same, including the curl -sSLf command. ‘

