---
id: 636cd61ba8
question: Why do we sometimes use random_state and not at other times?
sort_order: 3
---

Refer to the sklearn documentation, `random_state` is used to ensure the "randomness" that is used to shuffle the dataset is reproducible. It typically requires both `random_state` and `shuffle` parameters to be set accordingly.