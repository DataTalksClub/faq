---
course: data-engineering-zoomcamp
id: 5b4c133384
question: iPython - Pandas parsing dates with ‘read_csv’
section: 'Module 1: Docker and Terraform'
sort_order: 1320
---

Pandas can interpret “string” column values as “datetime” directly when reading the CSV file using “pd.read_csv” using the parameter “parse_dates”, which for example can contain a list of column names or column indices. Then the conversion afterwards is not required anymore.

Example from week 1

import pandas as pd

df = pd.read_csv(

'yellow_tripdata_2021-01.csv',

nrows=100,

parse_dates=['tpep_pickup_datetime', 'tpep_dropoff_datetime'])

df.info()

which will output

<class 'pandas.core.frame.DataFrame'>

RangeIndex: 100 entries, 0 to 99

Data columns (total 18 columns):

#   Column                 Non-Null Count  Dtype

---  ------                 --------------  -----

0   VendorID               100 non-null    int64

1   tpep_pickup_datetime   100 non-null    datetime64[ns]

2   tpep_dropoff_datetime  100 non-null    datetime64[ns]

3   passenger_count        100 non-null    int64

4   trip_distance          100 non-null    float64

5   RatecodeID             100 non-null    int64

6   store_and_fwd_flag     100 non-null    object

7   PULocationID           100 non-null    int64

8   DOLocationID           100 non-null    int64

9   payment_type           100 non-null    int64

10  fare_amount            100 non-null    float64

11  extra                  100 non-null    float64

12  mta_tax                100 non-null    float64

13  tip_amount             100 non-null    float64

14  tolls_amount           100 non-null    float64

15  improvement_surcharge  100 non-null    float64

16  total_amount           100 non-null    float64

17  congestion_surcharge   100 non-null    float64

dtypes: datetime64[ns](2), float64(9), int64(6), object(1)

memory usage: 14.2+ KB

