---
course: data-engineering-zoomcamp
id: 542abbcb6a
question: 'wget - ERROR: cannot verify <website> certificate  (MacOS)'
section: 'Module 1: Docker and Terraform'
sort_order: 530
---

Firstly, make sure that you add “!” before wget if you’re running your command in a Jupyter Notebook or CLI. Then, you can check one of this 2 things (from CLI):

Using the Python library wget you installed with pip, try python -m wget <url>

Write the usual command and add --no-check-certificate at the end. So it should be:

!wget<website_url> --no-check-certificate

