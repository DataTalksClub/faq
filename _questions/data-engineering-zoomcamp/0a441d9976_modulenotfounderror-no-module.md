---
id: 0a441d9976
question: ModuleNotFoundError: No module named 'avro'
section: Module 6: streaming with kafka
course: data-engineering-zoomcamp
sort_order: 3920
---

✅SOLUTION: pip install confluent-kafka[avro].

For some reason, Conda also doesn't include this when installing confluent-kafka via pip.

More sources on Anaconda and confluent-kafka issues:

