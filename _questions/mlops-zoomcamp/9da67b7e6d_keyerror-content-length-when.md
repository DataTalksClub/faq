---
course: mlops-zoomcamp
id: 9da67b7e6d
question: KeyError ‘content-length’ when running prepare.py
section: 'Module 5: Monitoring'
sort_order: 1940
---

Problem: When running prepare.py getting KeyError: ‘content-length’

Solution: From Emeli Dral:
It seems to me that the link we used in prepare.py to download taxi data does not work anymore. I substituted the instruction:

url = f"

by the

url = f""

in the prepare.py and it worked for me. Hopefully, if you do the same you will be able to get those data.

