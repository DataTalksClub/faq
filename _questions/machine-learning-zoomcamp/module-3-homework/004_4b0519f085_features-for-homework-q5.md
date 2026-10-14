---
id: 4b0519f085
question: 'Features for homework: Q5'
sort_order: 4
---

Do we need to train the model only with the features: total_rooms, total_bedrooms, population, and households, or with all the available features, then remove each of the previous features one at a time to compare accuracy?

1. Create a list of all features and evaluate the model to obtain the original accuracy.
2. Remove one feature at a time.
3. Train the model each time, calculate the accuracy, and find the difference between the original accuracy and the new accuracy.
4. Identify which feature has the smallest absolute accuracy difference.

While calculating differences between accuracy scores, use the smallest absolute difference. For example, if the differences are -4 and -2, the smallest absolute difference is `abs(-2)`. Use this value to determine the impact of the feature on accuracy.

A difference close to zero (or even negative) is normal: the removed feature may add little information, or its signal may already be captured by other correlated features.
