What are the main assumptions of Logistic Regression?

1. **Binary or Ordinal Outcome**
   The dependent variable (Y) must be categorical.
2. **Independence of Observations**
   Each observation in the dataset should be independent of all other observations. This means the data should not come from repeated measurements on the same individual or from clustered data. This is a data collection and study design assumption.
3. **Little to No Multicollinearity**
   The independent (predictor) variables (X) should not be highly correlated with each other. If two predictors are strongly correlated, it becomes difficult for the model to determine the individual effect of each one on the outcome.
   Of course. Here is a comprehensive FAQ that covers the main assumptions of logistic regression, with a special focus on how to verify the linearity of the logit assumption.

4. **Linearity of Predictors and Log-Odds**

   It assumes that the predictors are linearly related to the log-odds (or logit) of the outcome.

   $logit(p)=ln(\frac{p}{1−p})=β0​+β1​X$

```python
# Visual inspection of linear relationship
# Define your model
import seaborn as sns
from sklearn.linear_model import LogisticRegression

# After data preparation, define your Logistic Regression model
log_clf = LogisticRegression(solver='liblinear', random_state=42)
log_clf.fit(X_train, y_train)

# logit data
logit_data = X_train.copy()

# logit column
training_probabilities = log_clf.predict_proba(X_train)
logit_data['logit'] = [np.log(prob[1] / prob[0]) for prob in training_probabilities]

# plot a regplot
sns.regplot(
    data=logit_data,
    x='col_name',
    y='logit',
    scatter_kws={'s': 2, 'alpha': 0.5}
        )
```
