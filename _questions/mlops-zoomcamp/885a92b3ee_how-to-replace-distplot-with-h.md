---
course: mlops-zoomcamp
id: 885a92b3ee
question: How to replace distplot with histplot
section: 'Module 1: Introduction'
sort_order: 480
---

sns.distplot(df_train["duration"])

Can be replaced with

sns.histplot(

df_train["duration"] , kde=True,

stat="density", kde_kws=dict(cut=3), bins=50,

alpha=.4, edgecolor=(1, 1, 1, 0.4),

)

To get almost identical result

