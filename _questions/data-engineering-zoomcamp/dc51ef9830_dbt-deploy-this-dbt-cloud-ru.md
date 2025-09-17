---
id: dc51ef9830
question: DBT Deploy - This dbt Cloud run was cancelled because a valid dbt project was not found.
section: Module 4: analytics engineering with dbt
course: data-engineering-zoomcamp
sort_order: 3070
---

This happens because we have moved the dbt project to another directory on our repo.

Or might be that you’re on a different branch than is expected to be merged from / to.

Solution:

Go to the projects window on dbt cloud -> settings -> edit -> and add directory (the extra path to the dbt project)

For example:

/week5/taxi_rides_ny

Make sure your file explorer path and this Project settings path matches and there’s no files waiting to be committed to github if you’re running the job to deploy to PROD.

![Image](images/data-engineering-zoomcamp/image_c27ecb8e.png)

![Image](images/data-engineering-zoomcamp/image_8b6478c1.png)

And that you had setup the PROD environment to check in the main branch, or whichever you specified.

In the picture below, I had set it to ella2024 to be checked as “production-ready” by the “freshness” check mark at the PROD environment settings. So each time I merge a branch from something else into ella2024 and then trigger the PR, the CI check job would kick-in. But we still do need to Merge and close the PR manually, I believe, that part is not automated.

![Image](images/data-engineering-zoomcamp/image_80992235.png)

You set up the PROD custom branch (if not default main) in the Environment setup screen.

![Image](images/data-engineering-zoomcamp/image_cd924928.png)

