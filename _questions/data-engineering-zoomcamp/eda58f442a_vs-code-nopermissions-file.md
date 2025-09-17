---
course: data-engineering-zoomcamp
id: eda58f442a
question: '​​VS Code: NoPermissions (FileSystemError): Error: EACCES: permission denied
  (linux)'
section: 'Module 4: analytics engineering with dbt'
sort_order: 3050
---

If you have problems editing dbt_project.yml when using Docker after ‘docker-compose run dbt-bq-dtc init’, to change profile ‘taxi_rides_ny’ to 'bq-dbt-workshop’, just run:

sudo chown -R username path

DBT - Internal Error: Profile should not be None if loading is completed

When  running dbt debug, change the directory to the newly created subdirectory (e.g: the newly created `taxi_rides_ny` directory, which contains the dbt project).

