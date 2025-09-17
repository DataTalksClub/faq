---
course: mlops-zoomcamp
id: 13559b737e
question: The chart in Grafana doesn’t get updates
section: 'Module 5: Monitoring'
sort_order: 2010
---

Problem description. While my metric generation script was still running, I noticed that the charts in Grafana don’t get updated.

Solution description. There are two things to pay attention to:

Refresh interval: set it to a small value: 5-10-30 seconds

Use your local timezone in a call to `pytz.timezone` – I couldn’t get updates before changing this from the original value “Europe/London” to my own zone

