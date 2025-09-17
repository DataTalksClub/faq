---
course: machine-learning-zoomcamp
id: 4b0519f085
question: Features for homework Q5
section: 3. Machine Learning for Classification
sort_order: 1190
---

Do we need to train the model only with the features: total_rooms, total_bedrooms, population and households? or with all the available features and then pop once at a time each of the previous features and train the model to make the accuracy comparison?

You need to create a list of all features in this question and evaluate the model one time to obtain the accuracy, this will be the original accuracy, and then remove one feature each time, and in each time, train the model, find the accuracy and the difference between the original accuracy and the found accuracy. Finally, find out which feature has the smallest absolute accuracy difference.

While calculating differences between accuracy scores while training on the whole model, versus dropping one feature at a time and comparing its accuracy to the model to judge impact of the feature on the accuracy of the model, do we take the smallest difference or smallest absolute difference?

Since order of subtraction between the two accuracy scores can result in a negative number, we will take its absolute value as we are interested in the smallest value difference, not the lowest difference value. Case in point, if difference is -4 and -2, the smallest difference is abs(-2), and not abs(-4)

