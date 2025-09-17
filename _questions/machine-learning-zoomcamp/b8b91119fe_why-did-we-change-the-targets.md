---
course: machine-learning-zoomcamp
id: b8b91119fe
question: Why did we change the targets to binary format when calculating mutual information
  score in the homework?
section: 3. Machine Learning for Classification
sort_order: 1010
---

Solution: Mutual Information score calculates the relationship between categorical variables or discrete variables. So in the homework, because the target which is median_house_value is continuous, we had to change it to binary format which in other words, makes its values discrete as either 0 or 1. If we allowed it to remain in the continuous variable format, the mutualinformation score could be calculated, but the algorithm would have to divide the continuous variables into bins and that would be highly subjective. That is why continuous variables are not used for mutual information score calculation.

—Odimegwu David—-

