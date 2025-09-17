---
id: fa4068ee43
question: Unable to complete HW 5 due to running Docker on M1 and not using Docker Desktop.
section: 6. Decision Trees and Ensemble Learning
course: machine-learning-zoomcamp
sort_order: 2370
---

Solution: 
If you replaced Docker desktop with ‘lima’, you may be able to create an instance of Lima using the . Follow the instructions listed on the page and create an instance with the template supplied. You’ll have to switch your current (if any) docker context to the context associated with this new (running) image. You should be able to use ‘svizor/zoomcamp-model:3.11.5-slim’ as a base image and run your own built image without issues.

By Alex Khvatov

Simple solution:

specify the platform. try this

docker run --platform linux/amd64 -it --rm -p 9696:9696 <your-docker-image-name>

Added by Till Meineke, solution from Aaron

Q: Why do I get the error TypeError: Expecting a sequence of strings for feature names, got: <class 'numpy.ndarray'> when using xgb.DMatrix?

A: This error occurs because recent versions of xgb.DMatrix expect the feature_names parameter to be a list of strings rather than a NumPy array. If you’re following older tutorial videos, they may use feature_names=dv.get_feature_names_out() directly, which now results in this error.

Solution: To resolve this, convert dv.get_feature_names_out() to a list using .tolist(). Here’s an updated example:

# Convert feature names to a list

feature_names = dv.get_feature_names_out().tolist()

# Create DMatrix objects with the corrected feature names

dfulltrain = xgb.DMatrix(X_full_train,

label=y_full_train,

feature_names=feature_names)

dtest = xgb.DMatrix(X_test,

feature_names=feature_names)

Explanation: The dv.get_feature_names_out() method returns a NumPy array, but xgb.DMatrix now expects feature_names to be a list of strings. Using .tolist() converts the array to a compatible format, allowing the code to run without errors.

