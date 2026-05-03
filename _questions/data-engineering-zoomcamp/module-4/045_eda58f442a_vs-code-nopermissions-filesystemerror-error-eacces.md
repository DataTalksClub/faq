---
id: eda58f442a
question: 'VS Code: NoPermissions (FileSystemError): Error: EACCES: permission denied
  (linux)'
sort_order: 45
---

If you encounter problems editing `dbt_project.yml` when using Docker after running `docker-compose run dbt-bq-dtc init`, to change the profile ‘taxi_rides_ny’ to 'bq-dbt-workshop’, execute the following command:

```bash
sudo chown -R username path
```

If you see the error "DBT - Internal Error: Profile should not be None if loading is completed" when running `dbt debug`, change the directory to the newly created subdirectory, such as the `taxi_rides_ny` directory, which contains the dbt project.