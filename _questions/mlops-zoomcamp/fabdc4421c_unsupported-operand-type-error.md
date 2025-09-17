---
course: mlops-zoomcamp
id: fabdc4421c
question: Unsupported Operand Type Error in hpo.py
section: 'Module 2: Experiment tracking'
sort_order: 1060
---

Running “python hpo.py --data_path=./your-path --max_evals=50” for the homework leads to the following error: TypeError: unsupported operand type(s) for -: 'str' and 'int'

Full Traceback:

File "~/repos/mlops/02-experiment-tracking/homework/hpo.py", line 73, in <module>

run(args.data_path, args.max_evals)

File "~/repos/mlops/02-experiment-tracking/homework/hpo.py", line 47, in run

fmin(

File "~/Library/Caches/pypoetry/virtualenvs/mlflow-intro-SyTqwt0D-py3.9/lib/python3.9/site-packages/hyperopt/fmin.py", line 540, in fmin

return trials.fmin(

File "~/Library/Caches/pypoetry/virtualenvs/mlflow-intro-SyTqwt0D-py3.9/lib/python3.9/site-packages/hyperopt/base.py", line 671, in fmin

return fmin(

File "~/Library/Caches/pypoetry/virtualenvs/mlflow-intro-SyTqwt0D-py3.9/lib/python3.9/site-packages/hyperopt/fmin.py", line 586, in fmin

rval.exhaust()

File "~/Library/Caches/pypoetry/virtualenvs/mlflow-intro-SyTqwt0D-py3.9/lib/python3.9/site-packages/hyperopt/fmin.py", line 364, in exhaust

self.run(self.max_evals - n_done, block_until_done=self.asynchronous)

TypeError: unsupported operand type(s) for -: 'str' and 'int'

Solution:

The --max_evals argument in hpo.py has no defined datatype and will therefore implicitly be treated as string. It should be an integer, so that the script can work correctly. Add type=int to the argument definition:

parser.add_argument(

"--max_evals",

type=int,

default=50,

help="the number of parameter evaluations for the optimizer to explore."

)

export

