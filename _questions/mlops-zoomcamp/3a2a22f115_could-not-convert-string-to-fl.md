---
course: mlops-zoomcamp
id: 3a2a22f115
question: Could not convert string to float - ValueError
section: 'Module 2: Experiment tracking'
sort_order: 820
---

Running python register_model.py results in the following error:

ValueError: could not convert string to float: '0 int\n1   float\n2     hyperopt_param\n3       Literal{n_estimators}\n4       quniform\n5         Literal{10}\n6         Literal{50}\n7         Literal{1}'

Full Traceback:

Traceback (most recent call last):

File "/Users/name/Desktop/Programming/DataTalksClub/MLOps-Zoomcamp/2. Experiment tracking and model management/homework/scripts/register_model.py", line 101, in <module>

run(args.data_path, args.top_n)

File "/Users/name/Desktop/Programming/DataTalksClub/MLOps-Zoomcamp/2. Experiment tracking and model management/homework/scripts/register_model.py", line 67, in run

train_and_log_model(data_path=data_path, params=run.data.params)

File "/Users/name/Desktop/Programming/DataTalksClub/MLOps-Zoomcamp/2. Experiment tracking and model management/xfsub/scripts/register_model.py", line 41, in train_and_log_model

params = space_eval(SPACE, params)

File "/Users/name/miniconda3/envs/mlops-zoomcamp/lib/python3.9/site-packages/hyperopt/fmin.py", line 618, in space_eval

rval = pyll.rec_eval(space, memo=memo)

File "/Users/name/miniconda3/envs/mlops-zoomcamp/lib/python3.9/site-packages/hyperopt/pyll/base.py", line 902, in rec_eval

rval = scope._impls[node.name](*args, **kwargs)

ValueError: could not convert string to float: '0 int\n1   float\n2     hyperopt_param\n3       Literal{n_estimators}\n4       quniform\n5         Literal{10}\n6         Literal{50}\n7         Literal{1}'

Solution: There are two plausible errors to this. Both are in the hpo.py file where the hyper-parameter tuning is run. The objective function should look like this.

   def objective(params):

# It's important to set the "with" statement and the "log_params" function here

# in order to properly log all the runs and parameters.

with mlflow.start_run():

# Log the parameters

mlflow.log_params(params)

rf = RandomForestRegressor(**params)

rf.fit(X_train, y_train)

y_pred = rf.predict(X_valid)

# Calculate and log rmse

rmse = mean_squared_error(y_valid, y_pred, squared=False)

mlflow.log_metric('rmse', rmse)

If you add the with statement before this function, and just after the following line

X_valid, y_valid = load_pickle(os.path.join(data_path, "valid.pkl"))

and you log the parameters just after the search_space dictionary is defined, like this

search_space = {....}

# Log the parameters

mlflow.log_params(search_space)

Then there is a risk that the parameters will be logged in group. As a result, the

params = space_eval(SPACE, params)

register_model.py file will receive the parameters in group, while in fact it expects to receive them one by one. Thus, make sure that the objective function looks as above.

Added by Jakob Salomonsson

