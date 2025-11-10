---
id: 91ff5cb6b6
question: 'ValueError: not enough values to unpack when parsing XGBoost output in
  parse_xg_output; how to fix and switch to evals_result?'
sort_order: 112
---

Check the following outputs:
```python
print(repr(output.stdout))
```
and
```python
print(repr(output.stderr))
```
If they are empty, this means XGBoost does not print training logs to stdout.
One solution is to use the training results returned by the Python API:
```python
evals_result = {}
model = xgb.train(
params=xgb_params,
dtrain=dtrain,
num_boost_round=200,
evals=[(dtrain, 'train'), (dval, 'val')],
evals_result=evals_result,
verbose_eval=True
)
# Convert results to a DataFrame directly
df_results = pd.DataFrame({
'num_iter': range(len(evals_result['train']['auc'])),
'train_auc': evals_result['train']['auc'],
'val_auc': evals_result['val']['auc']
})
df_results.head()
```
This will replace relevant code in parse_xg_output(). Also, the function now does not take any parameters.