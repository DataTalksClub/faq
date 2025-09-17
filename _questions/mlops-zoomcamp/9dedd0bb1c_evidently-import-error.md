---
course: mlops-zoomcamp
id: 9dedd0bb1c
question: Evidently Import Error
section: 'Module 6: Best practices'
sort_order: 2200
---

Problem description

When I run the command “from evidently import ColumnMapping” I get an import error ImportError: cannot import name 'ColumnMapping' from 'evidently'

Solution description

Uninstall the latest version (Version: 0.7.8) with “pip uninstall evidently -y” then install an older compatible version “pip install evidently==0.4.18” and restart the kernel to reload the environment.

Added by Mohamed Cherif

