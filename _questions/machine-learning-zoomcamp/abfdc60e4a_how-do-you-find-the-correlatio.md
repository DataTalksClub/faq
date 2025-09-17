---
course: machine-learning-zoomcamp
id: abfdc60e4a
question: How do you find the correlation matrix?
section: 3. Machine Learning for Classification
sort_order: 1030
---

First, you have to consider whether the data is numerical or categorical. If it’s numerical, you can correlate it directly - if it’s categorial you can find the correlations for the data indirectly by vectorizing the data using One-Hot encoding or other similar method.

To find if it’s numerical, check the dtypes() of the dataframe you’re looking at. Anything that’s integer, float, etc is numerical, while data types such as objects are categorical. You can correlate the numerical data by specifying which columns are numerical and using that as input to a correlation matrix.

numerical = ['tenure', 'monthlycharges', 'totalcharges']

df[numerical].corr()

Added by Michael Friske

