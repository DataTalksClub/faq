---
course: data-engineering-zoomcamp
id: 52858dfd98
question: 'Postgres - ModuleNotFoundError: No module named ''psycopg2'''
section: 'Module 1: Docker and Terraform'
sort_order: 1230
---

Issue:

![Image](images/data-engineering-zoomcamp/image_b7e005cb.png)

e…

![Image](images/data-engineering-zoomcamp/image_c56a8539.png)

Solution:

pip install psycopg2-binary

If you already have it, you might need to update it:

pip install psycopg2-binary --upgrade

Other methods, if the above fails:

if you are getting the “ ModuleNotFoundError: No module named 'psycopg2' “ error even after the above installation, then try updating conda using the command conda update -n base -c defaults conda. Or if you are using pip, then try updating it before installing the psycopg packages i.e

First uninstall the psycopg package

Then update conda or pip

Then install psycopg again using pip.

if you are still facing error with r pcycopg2 and showing pg_config not found then you will have to install postgresql. in MAC it is brew install postgresql

