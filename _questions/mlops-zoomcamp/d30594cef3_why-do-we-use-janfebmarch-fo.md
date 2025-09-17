---
id: d30594cef3
question: Why do we use Jan/Feb/March for Train/Test/Validation Purposes?
section: Module 2: Experiment tracking
course: mlops-zoomcamp
sort_order: 1200
---

Problem: Someone asked why we are using this type of split approach instead of just a random split.

Solution: For example, I have some models at work that train on Jan 1 2020 — Aug 1 2021 time period, and then test on Aug 1 - Dec 31 2021, and finally validate on Jan - March or something

We do these “out of time”  validations to do a few things:

Check for seasonality of our data

We know if the RMSE for Test is 5 say, and then RMSE for validation is 20, then there’s serious seasonality to the data we are looking at, and now we might change to Time Series approaches

If I’m predicting on Mar 30 2023 the outcomes for the next 3 months, the “random sample” in our train/test would have caused data leakage, overfitting, and poor model performance in production. We mustn’t take information about the future and apply it to the present when we are predicting in a model context.

These are two of, I think, the biggest points for why we are doing jan/feb/march. I wouldn’t do it any other way.

Train: Jan

Test: Feb

Validate: March

The point of validation is to report out model metrics to leadership, regulators, auditors, and record the models performance to then later analyze target drift

Added by Sam LaFell

