---
course: machine-learning-zoomcamp
id: 45482efa5e
images:
- description: 'image #1'
  id: image_1
  path: images/machine-learning-zoomcamp/image_852cd1cd.png
- description: 'image #2'
  id: image_2
  path: images/machine-learning-zoomcamp/image_6476267e.png
question: Identifying highly correlated feature pairs easily through unstack
section: 3. Machine Learning for Classification
sort_order: 1050
---

data_corr = pd.DataFrame(data_num.corr().round(3).abs().unstack().sort_values(ascending=False))

data_corr.head(10)

Added by Harish Balasundaram

You can also use seaborn to create a heatmap with the correlation. The code for doing that:

sns.heatmap(df[numerical_features].corr(),

annot=True,

square=True,

fmt=".2g",

cmap="crest")

Added by Cecile Guillot

You can refine your heatmap and plot only a triangle, with a blue to red color gradient, that will show every correlation between your numerical variables without redundant information with this function:

<{IMAGE:image_1}>

Which outputs, in the case of churn dataset:

<{IMAGE:image_2}>

(Mélanie Fouesnard)

