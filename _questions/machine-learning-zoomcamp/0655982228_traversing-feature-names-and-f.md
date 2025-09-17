---
id: 0655982228
question: Traversing feature names and feature importance values
section: 6. Decision Trees and Ensemble Learning
course: machine-learning-zoomcamp
sort_order: 2690
---

To pair feature names with their importance values, use dv.get_feature_names_out() to retrieve the feature names and rf.feature_importances_ for the importances. Then, combine them with zip(feature_names, importances) to view or sort by importance.

Just as shown below:

# Assuming rf is your RandomForest model and dv is your DictVectorizer

feature_names = dv.get_feature_names_out()

feature_importances = rf.feature_importances_

# Pair feature names with their importance values

feature_importance_dict = dict(zip(feature_names, feature_importances))

# Sort by importance (optional)

sorted_feature_importance = sorted(feature_importance_dict.items(), key=lambda x: x[1], reverse=True)

# Display results

for feature, importance in sorted_feature_importance:

print(f"{feature}: {importance}")

(added by Jon Areas)

