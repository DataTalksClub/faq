---
course: mlops-zoomcamp
id: 47c771de0d
question: wget not working
section: 'Module 2: Experiment tracking'
sort_order: 1180
---

Problem

Using wget command to download either data or python scripts on Windows, I am using the notebook provided by Visual Studio and despite having a python virtual env, it did not recognize the pip command.

Solution: Use python -m pip, this same for any other command. Ie. python -m wget

Added by Erick Calderin

