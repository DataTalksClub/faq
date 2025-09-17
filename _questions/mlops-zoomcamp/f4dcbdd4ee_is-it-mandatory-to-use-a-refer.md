---
course: mlops-zoomcamp
id: f4dcbdd4ee
question: Is it mandatory to use a reference dataset when generating a report with
  Evidently?
section: 'Module 5: Monitoring'
sort_order: 2180
---

Answer:

No. While Evidently is designed to compare a reference dataset with a current one, it can also be used without a reference dataset.

In such cases, you can pass reference_data=None when creating the report. This is useful for generating descriptive statistics or univariate analyses on a single dataset (e.g., using ColumnSummaryMetric, DatasetMissingValuesMetric, etc.).

Added by José Luis Martínez

