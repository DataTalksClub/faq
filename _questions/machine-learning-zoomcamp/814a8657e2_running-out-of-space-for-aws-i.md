---
course: machine-learning-zoomcamp
id: 814a8657e2
question: Running out of space for AWS instance.
section: 9. Serverless Deep Learning
sort_order: 3280
---

Due to experimenting back and forth so much without care for storage, I just ran out of it on my 30-GB AWS instance. It turns out that deleting docker images does not actually free up any space as you might expect. After removing images, you also need to run docker system prune

