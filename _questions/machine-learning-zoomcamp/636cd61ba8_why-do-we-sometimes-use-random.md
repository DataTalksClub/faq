---
course: machine-learning-zoomcamp
id: 636cd61ba8
question: Why do we sometimes use random_state and not at other times?
section: 4. Evaluation Metrics for Classification
sort_order: 1420
---

Ie particularly in module-04 homework Qn2 vs Qn5. [https://datatalks-club.slack.com/archives/C0288NJ5XSA/p1696760905214979](https://datatalks-club.slack.com/archives/C0288NJ5XSA/p1696760905214979)

Refer to the sklearn docs, random_state is to ensure the “randomness” that is used to shuffle dataset is reproducible, and it usually requires both random_state and shuffle params to be set accordingly.

~~Ella Sahnan~~

