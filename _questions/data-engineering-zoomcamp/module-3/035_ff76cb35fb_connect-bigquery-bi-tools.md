---
id: ff76cb35fb
question: How do you connect BigQuery with BI tools like Looker Studio or Tableau?
sort_order: 35
---

BigQuery can be directly connected to popular BI tools such as Looker Studio (Google Data Studio) and Tableau to build dashboards and reports. Here is a high-level workflow for the two tools:

- Looker Studio:
  1) In Looker Studio, click Create > Data Source.
  2) Choose BigQuery as the data source and authorize access to your Google Cloud project.
  3) Select the project, dataset, and table (or view) you want to report on, then click Connect.
  4) Add the data source to a report and start building your visuals.

- Tableau (Tableau Desktop):
  1) Open Tableau Desktop and choose Google BigQuery as the data connector.
  2) Sign in with your Google account and authorize access to your project.
  3) Browse to your project, dataset, and table, then click Connect and start building visuals.

Notes:
- You may want to create views in BigQuery to simplify the data schema for BI tools.
- For Tableau, consider using extracts if you are working with large datasets or need offline access.
- Ensure proper IAM permissions (BigQuery Data Viewer or Editor) for the service account or user used by the BI tool.