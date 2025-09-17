---
id: 4693802714
question: Getting: Allocator ran out of memory errors?
section: 10. Kubernetes and TensorFlow Serving
course: machine-learning-zoomcamp
sort_order: 3430
---

If you are running tensorflow on your own machine and you start getting the following errors:

Allocator (GPU_0_bfc) ran out of memory trying to allocate 6.88GiB with freed_by_count=0. The caller indicates that this is not a failure, but this may mean that there could be performance gains if more memory were available.

Try adding this code in a cell at the beginning of your notebook:

config = tf.compat.v1.ConfigProto()

config.gpu_options.allow_growth = True

session = tf.compat.v1.Session(config=config)

After doing this most of my issues went away. I say most because there was one instance when I still got the error once more, but only during one epoch. I ran the code again, right after it finished, and I never saw the error again.

Added by Martin Uribe

Problem with downloading    file

The following old link is not valid anymore :




====>	The new link to download the file is :

Added by Sam

