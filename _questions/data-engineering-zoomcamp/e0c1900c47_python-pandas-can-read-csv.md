---
course: data-engineering-zoomcamp
id: e0c1900c47
question: Python - Pandas can read *.csv.gzip
section: 'Module 1: Docker and Terraform'
sort_order: 1340
---

When a CSV file is compressed using Gzip, it is saved with a ".csv.gz" file extension. This file type is also known as a Gzip compressed CSV file. When you want to read a Gzip compressed CSV file using Pandas, you can use the read_csv() function, which is specifically designed to read CSV files. The read_csv() function accepts several parameters, including a file path or a file-like object. To read a Gzip compressed CSV file, you can pass the file path of the ".csv.gz" file as an argument to the read_csv() function.

Here is an example of how to read a Gzip compressed CSV file using Pandas:

df = pd.read_csv('file.csv.gz'

, compression='gzip'

, low_memory=False

)

