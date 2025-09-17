---
id: fee2e5fbda
question: Visualize Feature Importance by using horizontal bar chart
section: 6. Decision Trees and Ensemble Learning
course: machine-learning-zoomcamp
sort_order: 2610
---

To make it easier for us to determine which features are important, we can use a horizontal bar chart to illustrate feature importance sorted by value.

1. # extract the feature importances from the model

feature_importances = list(zip(features_names, rdr_model.feature_importances_))

importance_df = pd.DataFrame(feature_importances, columns=['feature_names', 'feature_importances'])

2. # sort descending the dataframe by using feature_importances value

importance_df = importance_df.sort_values(by='feature_importances', ascending=False)

3. # create a horizontal bar chart

plt.figure(figsize=(8, 6))

sns.barplot(x='feature_importances', y='feature_names', data=importance_df, palette='Blues_r')

plt.xlabel('Feature Importance')

plt.ylabel('Feature Names')

plt.title('Feature Importance Chart')

Radikal Lukafiardi

