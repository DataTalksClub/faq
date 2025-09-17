---
course: machine-learning-zoomcamp
id: 79b2760cc5
question: How do I interpret precision and recall?
section: 4. Evaluation Metrics for Classification
sort_order: 1720
---

Precision:

Memory tip: Think of Precision as "How Precise Are Our Positive Predictions?". It relates to the accuracy of the positive results. It emphasizes how many of the predicted positive instances are actually correct

Interpretation:

- High Precision:

- Most of the predicted positives are correct.

- This makes the model more reliable.

- Low Precision:

- Indicates a higher rate of false positives.

- This decreases trust in the positive predictions.

When to prioritize precision: In scenarios like email spam detection, where marking a legitimate email as spam (false positive) can lead to missed communications, high precision is preferred to ensure that most flagged emails are indeed spam.

Recall:

Memory tip: Think of Recall as "How Sensitive Are We to the Positives?". It emphasizes capturing all actual positive cases. A high recall means that the model is good at identifying most of the positives.

Interpretation:

- High Recall:

- The model captures most of the true positives.

- This is crucial in situations where missing a positive case is costly.

- Low Recall:

- Many actual positives are overlooked.

- This highlights potential issues in detection.

When to prioritize recall: In medical diagnostics for a severe or highly contagious disease, missing a true positive (an actual case of the disease) can have serious public health implications.

Balancing Precision and Recall:

- Improving one metric may lead to a decrease in the other.

- The choice between precision and recall depends on specific goals and acceptable trade-offs in a given application.

(added by Karina)

