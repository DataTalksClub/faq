---
course: data-engineering-zoomcamp
id: af2b85f346
question: GCP gcloud + MS VS Code - gcloud auth hangs
section: 'Module 1: Docker and Terraform'
sort_order: 1600
---

If you are using MS VS Code and running gcloud in WSL2, when you first try to login to gcp via the gcloud cli gcloud auth application-default login, you will see a message like this, and nothing will happen

![Image](images/data-engineering-zoomcamp/image_df9492cb.png)

And there might be a prompt to ask if you want to open it via browser, if you click on it, it will open up a page with error message

![Image](images/data-engineering-zoomcamp/image_6b01ae01.png)

Solution : you should instead hover on the long link, and ctrl + click the long link

Click configure Trusted Domains here

Popup will appear, pick first or second entry

![Image](images/data-engineering-zoomcamp/image_bc858c4b.png)

![Image](images/data-engineering-zoomcamp/image_a231d54c.png)

![Image](images/data-engineering-zoomcamp/image_2f5bf08c.png)

Next time you gcloud auth, the login page should popup via default browser without issues

