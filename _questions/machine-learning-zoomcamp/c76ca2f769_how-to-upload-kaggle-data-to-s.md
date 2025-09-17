---
course: machine-learning-zoomcamp
id: c76ca2f769
question: How to upload kaggle data to Saturn Cloud?
section: 8. Neural Networks and Deep Learning
sort_order: 2780
---

Problem description: Uploading the data to saturn cloud from kaggle can be time saving, specially if the dataset is large.

You can just download to your local machine and then upload to a folder on saturn cloud, but there is a better solution that needs to be set once and you have access to all kaggle datasets in saturn cloud.

On your notebook run:

!pip install -q kaggle

Go to Kaggle website (you need to have an account for this):

Click on your profile image -> Account

Scroll down to the API box

Click on Create New API token

It will download a json file with the name kaggle.json store on your local computer. We need to upload this file in the .kaggle folder

On the notebook click on folder icon on the left upper corner

This will take you to the root folder

Click on the .kaggle folder

Once inside of the .kaggle folder upload the kaggle.json file that you downloaded

Run this command on your notebook:

!chmod 600 /home/jovyan/.kaggle/kaggle.json

Download the data using this command:

!kaggle datasets download -d agrigorev/dino-or-dragon

Create a folder to unzip your files:

!mkdir data

Unzip your files inside that folder

!unzip dino-or-dragon.zip -d data

Pastor Soto

