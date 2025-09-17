---
course: machine-learning-zoomcamp
id: 55a29a88a1
question: What if your accuracy and std training loss don’t match HW?
section: 8. Neural Networks and Deep Learning
sort_order: 2900
---

Problem:

I found running the wasp/bee model on my mac laptop had higher reported accuracy and lower std deviation than the HW answers. This may be because of the SGD optimizer. Running this on my mac printed a message about a new and legacy version that could be used.

Solution:

Try running the same code on google collab or another way. The answers were closer for me on collab. Another tip is to change the runtime to use T4 and the model run’s faster than just CPU

Added by Quinn Avila

