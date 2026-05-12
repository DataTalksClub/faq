---
id: 575e56b819
question: What is the difference between label and one-hot encoding?
sort_order: 28
---

Two main encoding approaches are generally used to handle categorical data: label encoding and one-hot encoding.

- **Label Encoding**: Assigns each categorical value an integer based on alphabetical order. Suitable for logical categorical data, such as a rating system or classification.

- **One-Hot Encoding**: Creates new variables using 0s and 1s to represent original categorical data. Useful when there is no inherent order or logic to the categories.

**Tools and Implementation**

- **Sci-kit Learn**:
  - Dictionary Vectorizer: Handles categorical data and generates arrays based on unique instances in a DataFrame or other data structures.
  - `OneHotEncoder` class: Specifically for applying one-hot encoding.

- **Pandas**:
  - `pd.get_dummies()`: Similar functionality for one-hot encoding.

Note: Sometimes resetting a dataset into objects is necessary to apply one-hot encoding, especially when there is logical structuring in the data that could influence label encoding, which can be limiting for some applications.