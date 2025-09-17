---
course: data-engineering-zoomcamp
id: d677df9ccb
question: Taxi Data - How to handle taxi data files, now that the files are available
  as *.csv.gz?
section: 'Module 1: Docker and Terraform'
sort_order: 490
---

In [this video](https://www.youtube.com/watch?v=B1WwATwf-vY&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb), we store the data file as “output.csv”. The data file won’t store correctly if the file extension is csv.gz instead of csv. One alternative is to replace csv_name = “output.cs -v” with the file name given at the end of the URL. Notice that the URL for the yellow taxi data is: [https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/](https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_2021-01.csv.gz)[yellow_tripdata_2021-01.csv.gz](https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_2021-01.csv.gz) where the highlighted part is the name of the file. We can parse this file name from the URL and use it as csv_name. That is, we can replace csv_name = “output.csv” withcsv_name = url.split(“/”)[-1] . Then when we use csv_name to using pd.read_csv, there won’t be an issue even though the file name really has the extension csv.gz instead of csv since the pandas read_csv function can read csv.gz files directly.

