---
id: e839b64165
question: How to run a dbt-core project as an Airflow Task Group on Google Cloud Composer using a service account JSON key
section: Project
course: data-engineering-zoomcamp
sort_order: 4300
---

the  package as a dependency. (see Terraform ).

Make a new folder, dbt/, inside the dags/ folder of your Composer GCP bucket and copy paste your dbt-core project there. (see )

Ensure your profiles.yml is configured to authenticate with a service account key. (see BigQuery )

Create a new DAG using the DbtTaskGroup class and a ProfileConfig specifying a profiles_yml_filepath that points to the location of your JSON key file. (see )

Your dbt lineage graph should now appear as tasks inside a task group like this:

![Image](images/data-engineering-zoomcamp/image_bd4861e1.png)

