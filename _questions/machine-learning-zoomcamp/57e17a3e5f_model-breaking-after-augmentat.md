---
id: 57e17a3e5f
question: Model breaking after augmentation – high loss + bad accuracy
section: 8. Neural Networks and Deep Learning
course: machine-learning-zoomcamp
sort_order: 2840
---

Problem:

When resuming training after augmentation, the loss skyrockets (1000+ during first epoch) and accuracy settles around 0.5 – i.e. the model becomes as good as a random coin flip.

Solution:

Check that the augmented ImageDataGenerator still includes the option “rescale” as specified in the preceding step.

Added by Konrad Mühlberg

