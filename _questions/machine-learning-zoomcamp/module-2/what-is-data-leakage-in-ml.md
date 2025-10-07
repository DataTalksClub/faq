What is data leakage in machine learning?

Data leakage occurs when information from outside the training dataset is used to create the model, which can lead to overly optimistic performance estimates and a model that fails in the real world.

There are two types of leakage: target leakage and train-test contamination.

- **Target leakage** occurs when your model is trained using information that won't actually be available when making real-world predictions. This gives the model an unfair advantage, causing it to perform exceptionally well during training and testing, but poorly in a live environment because it learned from "future" data.

- **Train-test contamination** happens when data from your validation or test set unintentionally influences the training process, often during preprocessing. For example, if you calculate the mean to impute missing values using the entire dataset before splitting it, information from the test set has already "leaked" into your training data.
