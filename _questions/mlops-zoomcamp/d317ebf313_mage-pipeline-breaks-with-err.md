---
course: mlops-zoomcamp
id: d317ebf313
question: 'Mage pipeline breaks with [Errno 2] No such file or directory: ''/home/src/mage_data/{…}
  /.variables/{...}/output_1/object.joblib''"'
section: 'Module 3: Orchestration'
sort_order: 1300
---

Try to export the pipeline as zip file, create a new Mage project and import the pipeline zip to new project

Start by thoroughly checking the logs of the upstream block that was supposed to generate object.joblib. Ensure it completed successfully and that its expected output (often named output_1) was actually created and saved. You might also want to quickly verify in the Mage UI or file system (if accessible) whether the file exists in the .variables directory for that upstream block.

