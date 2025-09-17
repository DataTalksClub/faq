---
id: afdcab5249
question: Running out of memory
sort_order: 650
---

Problem: The output of DictVectorizer was taking up too much memory. So much so, that I couldn’t even fit the linear regression model before running out of memory on my 16 GB machine.

Solution: In the example for DictVectorizer in the scikit-learn [website](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.DictVectorizer.html), they set the parameter “sparse” as False. Although this helps with viewing the results, this results in a lot of memory usage. The solution is to either use “sparse=True” instead, or leave it at the default which is also True.

Ahmed Fahim (afahim03@yahoo.com)

