---
course: mlops-zoomcamp
id: 1e05eabc5c
question: Mage data_exporter block not taking all outputs from previous transformer
  block
section: 'Module 3: Orchestration'
sort_order: 1360
---

I encountered this issue while trying to run the data_export block that saves the dict vectorizer and the logs of the linear regression model into mlflow. My two distinct outputs, while they were clearly created by the previous transformer block where the linear regression model is trained and the dict vectorizer fitted to the training dataset.

Thus, I had this error while trying to run my export code:

Exception: Block mlflow_model_registry may be missing upstream dependencies. It expected to have 2 arguments, but only received 1. Confirm that the @data_exporter method declaration has the correct number of arguments.

The outputs are stored in a list and this list is the input with the two outputs as the two elements. I had to modify my code in the data_exporter function to take only one argument and to define the two variables after that:

Dv = output[0]

Lr = output[1]

Added by Mélanie Fouesnard

