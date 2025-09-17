---
id: 4d94846cbe
question: Requests Error: No connection adapters were found for 'localhost:9696/predict'.
section: 5. Deploying Machine Learning Models
course: machine-learning-zoomcamp
sort_order: 2220
---

You need to include the protocol scheme: ''.

Without the http:// part, requests has no idea how to connect to the remote server.

Note that the protocol scheme must be all lowercase; if your URL starts with HTTP:// for example, it won’t find the http:// connection adapter either.

Added by George Chizhmak

