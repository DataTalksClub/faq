---
course: machine-learning-zoomcamp
id: ba250275a3
images:
- description: 'image #1'
  id: image_1
  path: images/machine-learning-zoomcamp/image_16b33640.png
question: 'wget: unable to resolve host address ''raw.githubusercontent.com'''
section: 1. Introduction to Machine Learning
sort_order: 360
---

In Kaggle, when you are trying to !wget a dataset from github (or any other public repository/location), you get the following error:

Getting  this error while trying to import data- !wget[ [raw.githubusercontent.com](https://raw.githubusercontent.com/alexeygrigorev/datasets/master/housing.cs)v](https://raw.githubusercontent.com/alexeygrigorev/datasets/master/housing.csv)

--2022-09-17 16:55:24-- [ [raw.githubusercontent.com](https://raw.githubusercontent.com/alexeygrigorev/datasets/master/housing.cs)v](https://raw.githubusercontent.com/alexeygrigorev/datasets/master/housing.csv)

Resolving raw.githubusercontent.com (raw.githubusercontent.com)... failed: Temporary failure in name resolution.

wget: unable to resolve host address 'raw.githubusercontent.com'

Solution:

In your Kaggle notebook settings, turn on the Internet for your session. It's on the settings panel, on the right hand side of the Kaggle screen. You'll be asked to verify your phone number so Kaggle knows you are not a bot.

<{IMAGE:image_1}>

