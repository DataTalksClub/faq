---
id: c6f2a2afe5
question: How to fix when %%capture output is not working in Google Collab Notebook
section: 6. Decision Trees and Ensemble Learning
course: machine-learning-zoomcamp
sort_order: 2400
---

I was using Google Collab Notebook for the 2024 cohort HW 06. For the Q6 here, the

![Image](images/machine-learning-zoomcamp/image_03f8bfd8.jpg)

![Image](images/machine-learning-zoomcamp/image_a95d78a7.jpg)

was not working in the Collab Notebook. This led me to find a solution which is as follows:

# import the required libraries

import io

import sys

# Capture output using io.StringIO

output_capture = io.StringIO()

sys.stdout = output_capture  # Redirect stdout to the StringIO buffer

# Train the model with eta=0.3

model_eta_03 = xgb.train(xgb_params, dtrain, num_boost_round=num_rounds, verbose_eval=2, evals=watchlist)

# Reset stdout

sys.stdout = sys.__stdout__

# Retrieve and print the captured output

captured_output = output_capture.getvalue()

And, we need to slightly modify the parser function for only one line:

for line in output.stdout.strip().split('\n'):    # replace this line 3 in Alexey’s parser function with

for line in output.strip().split('\n'):

And  then call the df_score_03 = parse_xgb_output(captured_output)for getting the desired dataframe.

(Added by Siddhartha Gogoi)

