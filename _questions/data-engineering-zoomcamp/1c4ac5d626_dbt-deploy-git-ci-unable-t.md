---
id: 1c4ac5d626
question: Dbt deploy + Git CI - Unable to configure Continuous Integration (CI) with Github
section: Module 4: analytics engineering with dbt
course: data-engineering-zoomcamp
sort_order: 2760
---

If you’re trying to configure CI with Github and on the job’s options you can’t see Run on Pull Requests? on triggers, you have to reconnect with Github using native connection instead clone by SSH. Follow these steps:

On Profile Settings > Linked Accounts connect your Github account with dbt project allowing the permissions asked. More info at

![Image](images/data-engineering-zoomcamp/image_7800f401.png)

Disconnect your current Github’s configuration from Account Settings > Projects (analytics) > Github connection. At the bottom left appears the button Disconnect, press it.

Once we have confirmed the change, we can configure it again. This time, choose Github and it will appear in all repositories which you have allowed to work with dbt. Select your repository and it’s ready.

![Image](images/data-engineering-zoomcamp/image_8efd4f76.png)

Go to the Deploy > job configuration’s page and go down until Triggers and now you can see the option Run on Pull Requests:

![Image](images/data-engineering-zoomcamp/image_4e68416b.png)

