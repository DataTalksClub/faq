---
course: mlops-zoomcamp
id: e00253e2df
question: Fix Out of Memory error while orchestrating the workflow on a ML Pipeline
  for a high volume dataset.
section: 'Module 4: Deployment'
sort_order: 1530
---

We come across situations in data transformation & pre-processing as well as model training in a ML pipeline where we need to handle dataset of high dimensionality or/and high cardinality (usually millions). And we often end up with Out of Memory (OOM) errors like below when the flow is running:

![Image](images/mlops-zoomcamp/image_d1d6da8a.png)

If you do not have the option of increasing your RAM, the following 3 approaches can be effective in mitigating this error:

If at all possible, during the data loading step, read only the required features/columns from the dataset, eg.

![Image](images/mlops-zoomcamp/image_23d027f2.png)

Before encoding/vectorizing, when we get our X_train & y_train, we can remove the dataframe, eg.

![Image](images/mlops-zoomcamp/image_09a24598.png)

If you do not have a swap file or have a small one, create a swap file (size as per memory requirement) or replace the existing one with a proper sized one.Eg.

To remove existing swapfile, issue commands:

sudo swapoff /swapfile

sudo rm /swapfile

To create a new proper sized (I’m setting 16 GB in my case) swapfile, issue commands:

sudo fallocate -l 16G /swapfile

sudo chmod 600 /swapfile

sudo mkswap /swapfile

sudo swapon /swapfile

To check the swap file created, issue command:

free -h

Added by Siddhartha Gogoi

