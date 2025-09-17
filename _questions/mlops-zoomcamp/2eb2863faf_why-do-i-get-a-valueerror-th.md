---
course: mlops-zoomcamp
id: 2eb2863faf
question: 'Why do I get a “ValueError: The truth value of a DataFrame is ambiguous.
  Use a.empty, a.bool(), a.item(), a.any() or a.all()” error when doing unit test
  that involves comparing two data frames?'
section: 'Module 6: Best practices'
sort_order: 2400
---

Solution: Follow the tip: When you compare two Pandas DataFrames, the result is also a DataFrame. The same is true for Pandas Series. Also, a DataFrame could be turned into a list of dictionaries.

Therefore, do not compare data frames directly, but convert the actual and expected dataframes into list of dictionaries and then use assert to compare the resulting list of dictionaries.

For example:

…

actual_df_list_dicts = actual_df.to_dict('records')

…

expected_df_list_dicts = expected_df.to_dict('records')

…

assert actual_df_list_dicts == expected_df_list_dicts

Added by Victor Emenike

