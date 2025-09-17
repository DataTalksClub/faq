---
course: mlops-zoomcamp
id: 0a545e0e4c
question: Viewing SQLite Data Raw & Deleting Experiments Manually
section: 'Module 2: Experiment tracking'
sort_order: 1100
---

All the experiment and other tracking information in mlflow are stored in sqllite database provided while initiating the mlflow ui command. This database can be inspected using Pycharm’s Database tab by using the SQLLite database type. Once the connection is created as below, the tables can be queried and inspected using regular SQL. The same applies for any SQL backed database such as postgres as well.

This is very useful to understand the entity structure of the data being stored within mlflow and useful for any kind of systematic archiving of model tracking for longer periods.

Added by Senthilkumar Gopal

![Image](images/mlops-zoomcamp/image_10815a9d.png)

![Image](images/mlops-zoomcamp/image_e3defff0.png)

