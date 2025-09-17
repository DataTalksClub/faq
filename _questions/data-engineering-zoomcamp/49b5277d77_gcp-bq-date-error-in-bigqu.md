---
id: 49b5277d77
question: GCP BQ - DATE() Error in BigQuery
section: Module 3: Data Warehousing
course: data-engineering-zoomcamp
sort_order: 2220
---

Error Message:

PARTITION BY expression must be DATE(<timestamp_column>), DATE(<datetime_column>), DATETIME_TRUNC(<datetime_column>, DAY/HOUR/MONTH/YEAR), a DATE column, TIMESTAMP_TRUNC(<timestamp_column>, DAY/HOUR/MONTH/YEAR), DATE_TRUNC(<date_column>, MONTH/YEAR), or RANGE_BUCKET(<int64_column>, GENERATE_ARRAY(<int64_value>, <int64_value>[, <int64_value>]))

Solution:

Convert the column to datetime first.

df["pickup_datetime"] = pd.to_datetime(df["pickup_datetime"])

df["dropOff_datetime"] = pd.to_datetime(df["dropOff_datetime"])

