---
id: e839b64165
images:
- description: 'image #1'
  id: image_1
  path: images/data-engineering-zoomcamp/image_bd4861e1.png
question: How to run a dbt-core project as an Airflow Task Group on Google Cloud Composer
  using a service account JSON key
sort_order: 9
---

1. Install the [astronomer-cosmos](https://github.com/astronomer/astronomer-cosmos) package as a dependency. Refer to the installation guide [here](https://cloud.google.com/composer/docs/composer-2/install-python-dependencies#install_custom_packages_in_a_environment) and see a Terraform [example](https://github.com/wndrlxx/ca-trademarks-data-pipeline/blob/4e6a0e757495a99e01ff6c8b981a23d6dc421046/terraform/main.tf#L100).

2. Create a new folder, `dbt/`, inside the `dags/` folder of your Composer GCP bucket and copy your dbt-core project there. See the [example](https://github.com/wndrlxx/ca-trademarks-data-pipeline/tree/4e6a0e757495a99e01ff6c8b981a23d6dc421046/dags/dbt/ca_trademarks_dp).

3. Ensure your `profiles.yml` is configured to authenticate with a service account key. Refer to the BigQuery [example](https://docs.getdbt.com/docs/core/connect-data-platform/bigquery-setup#service-account-file).

4. Create a new DAG using the `DbtTaskGroup` class. Use a `ProfileConfig` specifying a `profiles_yml_filepath` that points to the location of your JSON key file. See this [example](https://github.com/wndrlxx/ca-trademarks-data-pipeline/blob/4e6a0e757495a99e01ff6c8b981a23d6dc421046/dags/6_dbt_cosmos_task_group.py#L47).

Your dbt lineage graph should now appear as tasks inside a task group like this:

<{IMAGE:image_1}>
