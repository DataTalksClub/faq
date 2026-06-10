---
id: ebc76c896b
question: 'After merging DataFrames I get Adj Close_x and Adj Close_y instead of Adj Close. Why?'
sort_order: 4
---

Those are pandas merge suffixes (default _x and _y) that appear when both frames share a column name. Pass the suffixes parameter to get clearer names. The _x version is the correct value; ideally drop the merge artifacts and keep a single version of each column.
