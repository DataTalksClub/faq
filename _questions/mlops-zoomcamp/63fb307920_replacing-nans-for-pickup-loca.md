---
id: 63fb307920
question: Replacing NaNs for pickup location and drop off location with -1 for One-Hot Encoding
section: Module 1: Introduction
course: mlops-zoomcamp
sort_order: 590
---

pd.get_dummies and DictVectorizer both create a one-hot encoding on string values. Therefore you need to convert the values in PUlocationID and DOlocationID to string.

If you convert the values in PUlocationID and DOlocationID from numeric to string, the NaN values get converted to the string "nan".  With DictVectorizer the RMSE is the same whether you use "nan" or "-1" as string representation for the NaN values. Therefore the representation doesn't have to be "-1" specifically, it could also be some other string.

