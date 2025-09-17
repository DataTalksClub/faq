---
id: 7efbf0d444
question: Chart for classes and predictions
section: Miscellaneous
course: machine-learning-zoomcamp
sort_order: 4050
---

How to visualize the predictions per classes after training a neural net

Solution description

classes, predictions = zip(*dict(zip(classes, predictions)).items())

plt.figure(figsize=(12, 3))

plt.bar(classes, predictions)

Luke

