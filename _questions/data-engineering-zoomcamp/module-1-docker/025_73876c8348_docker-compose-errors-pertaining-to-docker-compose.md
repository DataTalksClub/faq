---
id: 73876c8348
images:
question: 'Docker-Compose: Errors pertaining to docker-compose.yml and pgadmin setup'
sort_order: 25
---

For those experiencing problems with Docker Compose, getting data in PostgreSQL, and similar issues, follow these steps:

- **Create a new volume** on Docker, either using the command line or Docker Desktop app.
- **Modify your `docker-compose.yml` file** as needed to fix any setup issues.
- **Set `low_memory=False`** when importing the CSV file using pandas:
  
```python
df = pd.read_csv('yellow_tripdata_2021-01.csv', nrows=1000, low_memory=False)
```

- Use the specified function in your `upload-data.ipynb` for better tracking of the ingestion process.

```python
from time import time

counter = 0
time_counter = 0

while True:
    t_start = time()

    df = next(df_iter)

    df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
    df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)

    df.to_sql(name='yellow_taxi_data', con=engine, if_exists='append')

    t_end = time()

    t_elapsed = t_end - t_start

    print('Chunk Insertion Done! Time taken: %.2f seconds' %(t_elapsed))

    counter += 1
    time_counter += t_elapsed

    if counter == 14:
        print('All Chunks Inserted! Total Time Taken: %.2f seconds' %(time_counter))
        break
```

### Order of Execution:

1. Open the terminal in the `2_docker_sql` folder and run: `docker compose up`
2. Ensure no other containers are running except the ones you just executed (pgAdmin and pgdatabase).
3. Open Jupyter Notebook and begin the data ingestion.
4. Open pgAdmin and set up a server. Make sure you use the same configurations as your `docker-compose.yml` file, such as the same name (`pgdatabase`), port, and database name (`ny_taxi`).