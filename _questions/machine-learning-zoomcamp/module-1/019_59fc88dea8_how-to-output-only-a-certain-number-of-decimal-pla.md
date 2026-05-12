---
id: 59fc88dea8
question: How to output only a certain number of decimal places
sort_order: 19
---

You can use the `round()` function or f-strings:

- **Using `round()` function:**
  ```python
  round(number, 4)  # This will round number up to 4 decimal places
  ```

- **Using f-strings:**
  ```python
  print(f'Average mark for the Homework is {avg:.3f}')  # Formats the number to 3 decimal places
  ```

- **Using `pandas.Series.round` if you need to round values in a whole Series:**
  
  See the documentation for more information:
  [pandas.Series.round](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.round.html#pandas.Series.round)

