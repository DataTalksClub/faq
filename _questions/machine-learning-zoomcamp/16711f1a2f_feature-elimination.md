---
course: machine-learning-zoomcamp
id: 16711f1a2f
question: Feature elimination
section: 3. Machine Learning for Classification
sort_order: 1080
---

For Q5 in homework, should we calculate the smallest difference in accuracy in real values (i.e. -0.001 is less than -0.0002) or in absolute values (i.e. 0.0002 is less than 0.001)?

We should select the “smallest” difference, and not the “lowest”, meaning we should reason in absolute values.

If the difference is negative, it means that the model actually became better when we removed the feature.

