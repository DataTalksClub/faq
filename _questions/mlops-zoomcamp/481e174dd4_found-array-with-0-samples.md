---
course: mlops-zoomcamp
id: 481e174dd4
question: Found array with 0 sample(s)
section: 'Module 5: Monitoring'
sort_order: 1980
---

Problem description

ValueError: Found array with 0 sample(s) (shape=(0, 6)) while a minimum of 1 is required by LinearRegression.

Solution description

This happens because the generated data is based on an early date therefore the training dataset would be empty.

Adjust the following

begin = datetime.datetime(202X, X, X, 0, 0)

Added by Luke

