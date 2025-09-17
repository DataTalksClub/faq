---
id: 4d08d35199
question: AttributeError: 'MlflowClient' object has no attribute 'list_run_infos'
section: Module 2: Experiment tracking
course: mlops-zoomcamp
sort_order: 1230
---

Problem: In scenario 2 notebook, an error AttributeError: 'MlflowClient' object has no attribute 'list_run_infos',

Is thrown when one runs “run_id = client.list_run_infos(experiment_id='1')[0].run_id”

Solution: Use “run_id = client.search_runs(experiment_ids='1')[0].info.run_id” instead.

Scenario: For reference, this works for mflow version 2.12.2, but might work for other recent versions as of May, 2024

Added by Oluwadara Adedeji

