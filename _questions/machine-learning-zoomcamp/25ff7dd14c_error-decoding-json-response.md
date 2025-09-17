---
course: machine-learning-zoomcamp
id: 25ff7dd14c
question: 'Error decoding JSON response: Expecting value: line 1 column 1 (char 0)'
section: Miscellaneous
sort_order: 4020
---

Problem happens when contacting the server waiting to send your predict-test and your data here in the correct shape.
The problem was the format input to the model wasn’t in the right shape. Server receives the data in json format (dict) which is not suitable for the model. U should convert it to like numpy arrays.

Ahmed Okka

