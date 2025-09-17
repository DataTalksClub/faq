---
course: data-engineering-zoomcamp
id: e8fe39dd54
question: DBT - I am having problems with columns datatype while running DBT/BigQuery
section: 'Module 4: analytics engineering with dbt'
sort_order: 2520
---

Issue: If you don’t define the column format while converting from csv to parquet Python will “choose” based on the first rows.

✅Solution: Defined the schema while running web_to_gcp.py pipeline.

Sebastian adapted the script:

Need a quick change to make the file work with gz files, added the following lines (and don’t forget to delete the file at the end of each iteration of the loop to avoid any problem of disk space)

file_name_gz = f"{service}_tripdata_{year}-{month}."

open(file_name_gz, 'wb').write(r.content)

os.system(f"gzip -d {file_name_gz}")

os.system(f"rm {file_name_init}.*")

