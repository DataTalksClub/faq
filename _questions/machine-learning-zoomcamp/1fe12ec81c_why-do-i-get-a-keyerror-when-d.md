---
id: 1fe12ec81c
question: Why do I get a KeyError when dropping features after one-hot encoding?
section: 3. Machine Learning for Classification
course: machine-learning-zoomcamp
sort_order: 1370
---

The error occurs because some features you try to drop have been one-hot encoded into multiple columns. After encoding, the original column may no longer exist, leading to the KeyError. To resolve this, identify and drop all related one-hot encoded columns (e.g., those starting with the original feature name) instead of the original feature itself.

For example, after one-hot encoding, the column 'marital' could have been split into columns like 'marital_single', 'marital_married', etc. This means that the original column 'marital' no longer exists, leading to the KeyError.

~ David Peterson

