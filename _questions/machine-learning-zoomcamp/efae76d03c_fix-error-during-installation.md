---
id: efae76d03c
question: Fix error during installation of Pipfile inside Docker container
section: 5. Deploying Machine Learning Models
course: machine-learning-zoomcamp
sort_order: 2040
---

![Image](images/machine-learning-zoomcamp/image_a22bc45c.png)

I tried the first solution on Stackoverflow which recommended running `pipenv lock` to update the Pipfile.lock. However, this didn’t resolve it. But the following switch to the pipenv installation worked

RUN pipenv install --system --deploy --ignore-pipfile

