---
id: eecebb4f2f
question: How to select column by dtype
sort_order: 14
---

To select columns by data type, you can use the following methods:

- To get columns with numeric data:

  ```python
  df.select_dtypes(include=np.number).columns.tolist()
  ```
  
- To get columns with object (string) data:

  ```python
  df.select_dtypes(include='object').columns.tolist()
  ```