---
course: machine-learning-zoomcamp
id: 34d0aaa13e
question: Running out of storage after building many docker images
section: 10. Kubernetes and TensorFlow Serving
sort_order: 3550
---

Problem description

Due to experimenting back and forth so much without care for storage, I just ran out of it on my 30-GB AWS instance.

My first reflex was to remove some zoomcamp directories, but of course those are mostly code so it didn’t help much.

Solution description

> docker images

revealed that I had over 20 GBs worth of superseded / duplicate models lying around, so I proceeded to > docker rmi

a bunch of those — but to no avail!

It turns out that deleting docker images does not actually free up any space as you might expect. After removing images, you also need to run

> docker system prune

See also: [[Stack Overflow](https://stackoverflow.com/questions/36799718/why-removing-docker-containers-and-images-does-not-free-up-storage-space-on-wind)](https://stackoverflow.com/questions/36799718/why-removing-docker-containers-and-images-does-not-free-up-storage-space-on-wind)

Added by Konrad Mühlberg

