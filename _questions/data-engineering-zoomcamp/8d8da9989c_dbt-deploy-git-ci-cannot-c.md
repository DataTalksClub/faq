---
id: 8d8da9989c
question: Dbt deploy + Git CI - cannot create CI checks job for deployment to Production. See more discussion in
section: Module 4: analytics engineering with dbt
course: data-engineering-zoomcamp
sort_order: 2750
---

Error:

Triggered by pull requests

This feature is only available for dbt repositories connected through dbt Cloud's native integration with Github, Gitlab, or Azure DevOps

Solution: Contrary to the , don’t use the Git Clone option. Use the Github one instead. Step-by-step guide to UN-LINK Git Clone and RE-LINK with Github in the next entry below

![Image](images/data-engineering-zoomcamp/image_c35c101c.png)

