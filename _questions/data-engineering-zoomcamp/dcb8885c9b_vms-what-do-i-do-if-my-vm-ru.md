---
course: data-engineering-zoomcamp
id: dcb8885c9b
question: VMs - What do I do if my VM runs out of space?
section: 'Module 3: Data Warehousing'
sort_order: 2290
---

Try deleting data you’ve saved to your VM locally during ETLs

Kill processes related to deleted files

Download ncdu and look for large files (pay particular attention to files related to Prefect)

If you delete any files related to Prefect, eliminate caching from your flow code

