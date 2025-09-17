---
course: mlops-zoomcamp
id: 460343cb44
question: When using Autologging, do I need to set a training parameter to track it
  on Mlflow UI?
section: 'Module 2: Experiment tracking'
sort_order: 1240
---

No, in the official documentation it’s mentioned that autologging keep track of the parameters even when you do not explicitly set them when calling .fit.

You can run the training, only setting the parameters you want, but you can check all the parameters in mlflow UI.

Added by Eduardo Munoz

