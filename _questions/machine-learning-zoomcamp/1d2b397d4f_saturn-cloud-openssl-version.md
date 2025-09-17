---
id: 1d2b397d4f
question: Saturn Cloud: OpenSSL version mismatch. Built against 30000020, you have 30300020
section: 8. Neural Networks and Deep Learning
course: machine-learning-zoomcamp
sort_order: 3030
---

This error occurs because the OpenSSH client is built against a specific version of OpenSSL (e.g., 3.0.0), but the system tries to use a different version (e.g., 3.0.3). This mismatch prevents the SSH client from working properly.

Solution:
Set the correct OpenSSL library path by running the following line in the terminal:

export LD_LIBRARY_PATH=/usr/lib/x86_64-linux-gnu

Added by Kemal Dahha

