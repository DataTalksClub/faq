---
id: 3d4013c118
question: Do you have an example of a Data Engineering Zoomcamp final project built
  on AWS with Airflow, S3, Athena, and a dashboard?
sort_order: 6
---

Yes. Here is an example final project:

Repo:
https://github.com/mlordjames/openpayments-analytics-platform

This project uses:
- Airflow on EC2 for batch workflow orchestration
- Python for ingestion and validation
- Amazon S3 as the raw data lake
- AWS Glue Data Catalog and Athena for the query layer
- a partitioned raw table by year (2023 and 2024)
- Streamlit for dashboarding and comparison views
- Terraform for reproducibility/documentation

It covers an end-to-end batch pipeline for CMS Open Payments General Payments data, including ingestion, upload to S3, Athena querying, and a dashboard showing:
- monthly payment trends by year
- top companies by payment amount
- top payment natures
- 2023 vs 2024 comparison metrics

This may be useful as a reference for students looking for an AWS-based final project structure.