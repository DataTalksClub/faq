---
course: mlops-zoomcamp
id: 108295493e
question: Kernel getting killed during assignment tasks on local
section: 'Module 1: Introduction'
sort_order: 520
---

If the jupyter notebook kernel gets killed repeatedly due to out of memory issues when converting pandas DF to dict or other memory intensive steps, try google colab as it offers larger memory.

For this,

Upload the datasets to google drive [Folder Colab Notebooks]

Mount the drive on colab

from google.colab import drive

drive.mount('/content/drive')

Pull the data from uploaded tables in colab

df_jan = pq.read_table('/content/drive/My Drive/Colab Notebooks/yellow_tripdata_2023-01.parquet').to_pandas()

All set for doing the assignment

Download the final assignment to your local and copy into the relevant repo

