---
id: d4f7c08ea1
question: 'Project: do I need an orchestration tool (Airflow, Mage, Kestra) for the
  capstone?'
sort_order: 8
---

No. A plain Python script that ingests and indexes your data is enough for full points on the "ingestion pipeline" criterion. A Jupyter notebook with the same steps is worth 1 point instead of 2.

Use an orchestrator only if it actually fits your project — for example, recurring ingestion of a feed that updates daily. Don't add one just to score the criterion.
