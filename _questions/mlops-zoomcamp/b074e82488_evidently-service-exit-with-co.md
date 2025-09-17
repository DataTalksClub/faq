---
course: mlops-zoomcamp
id: b074e82488
question: Evidently service exit with code 2
section: 'Module 5: Monitoring'
sort_order: 1950
---

Problem description

When I run the command “docker-compose up –build” and send the data to the real-time prediction service. The service will return “Max retries exceeded with url: /api”.

In my case it’s because of my evidently service exit with code 2 due to the “app.py” in evidently service cannot import “from pyarrow import parquet as pq”.

Solution description

The first solution is just install the pyarrow module “pip install pyarrow”

The second solution is to restart your machine.

The third solution is if the first and second one didn’t work with your machine. I found that “app.py” of evidently service didn’t use that module. So comment the pyarrow module out and the problem was solved for me.

Added by Surawut Jirasaktavee

