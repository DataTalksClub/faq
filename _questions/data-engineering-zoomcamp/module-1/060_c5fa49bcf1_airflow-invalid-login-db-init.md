---
id: c5fa49bcf1
question: 'Airflow: Invalid login or missing users - how to fix by initializing the
  database?'
sort_order: 60
---

## Airflow: Invalid login or missing users

This usually happens when the Airflow database is not initialized correctly.

Fix

Run the following command inside your container:

```bash
docker exec -it weather-dag-airflow-1 airflow db init
```

then paste this code:

```bash
docker exec -it weather-dag-airflow-1 airflow users create \
--username admin \
--password admin \
--firstname admin \
--lastname user \
--role Admin \
--email admin@example.com
```

After this, type exit and press enter.
You're done the username and password will be admin as shown above