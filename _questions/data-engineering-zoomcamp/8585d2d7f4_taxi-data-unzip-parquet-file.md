---
id: 8585d2d7f4
question: Taxi Data - Unzip Parquet file
section: Module 1: Docker and Terraform
course: data-engineering-zoomcamp
sort_order: 510
---

You can unzip this downloaded parquet file, in the command line. The result is a csv file which can be imported with pandas using the pd.read_csv() shown in the videos.

‘’’gunzip green_tripdata_2019-09.csv.gz’’’

SOLUTION TO USING PARQUET FILES DIRECTLY IN PYTHON SCRIPT ingest_data.py

In the def main(params) add this line

parquet_name= 'output.parquet'

Then edit the code which downloads the files

os.system(f"wget {url} -O {parquet_name}")

Convert the download .parquet file to csv and rename as csv_name to keep it relevant to the rest of the code

df = pd.read_parquet(parquet_name)

df.to_csv(csv_name, index=False)

