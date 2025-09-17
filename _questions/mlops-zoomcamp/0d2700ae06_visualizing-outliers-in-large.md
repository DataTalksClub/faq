---
id: 0d2700ae06
question: Visualizing outliers in large datasets with Seaborn: Boxplot vs Histplot
section: Module 1: Introduction
course: mlops-zoomcamp
sort_order: 760
---

seaborn.boxplot is generally faster because it uses a smaller set of summary statistics (min, Q1, median, Q3, max) to represent the data, which requires less computational effort, especially for large datasets.

seaborn.histplot can be slower, particularly with large datasets, because it needs to bin the data and compute frequency counts for each bin, which involves more processing.

So, if speed is a concern, especially with large datasets, boxplots are typically faster than histograms.

Added by Alexander Daniel Rios

