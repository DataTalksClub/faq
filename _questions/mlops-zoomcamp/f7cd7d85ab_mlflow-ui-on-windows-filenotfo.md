---
id: f7cd7d85ab
question: mlflow ui on Windows FileNotFoundError: [WinError 2] The system cannot find the file specified
section: Module 2: Experiment tracking
course: mlops-zoomcamp
sort_order: 1050
---

Problem: After successfully installing mlflow using pip install mlflow on my Windows system, I am trying to run the mlflow ui command but it throws the following error:

FileNotFoundError: [WinError 2] The system cannot find the file specified

Solution: Add C:\Users\{User_Name}\AppData\Roaming\Python\Python39\Scripts to the PATH

Added by Alex Litvinov

