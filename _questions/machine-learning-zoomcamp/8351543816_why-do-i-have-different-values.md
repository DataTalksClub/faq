---
id: 8351543816
question: Why do I have different values of accuracy than the options in the homework?
section: 4. Evaluation Metrics for Classification
course: machine-learning-zoomcamp
sort_order: 1590
---

One main reason behind that, is the way of splitting data. For example, we want to split data into train/validation/test with the ratios 60%/20%/20% respectively.

Although the following two options end up with the same ratio, the data itself is a bit different and not 100% matching in each case.

1)

df_train, df_temp = train_test_split(df, test_size=0.4, random_state=42)

df_val, df_test = train_test_split(df_temp, test_size=0.5, random_state=42)

2)

df_full_train, df_test = train_test_split(df, test_size=0.2, random_state=42)

df_train, df_val = train_test_split(df_full_train, test_size=0.25, random_state=42)

Therefore, I would recommend using the second method which is more consistent with the lessons and thus the homeworks.

Ibraheem Taha

