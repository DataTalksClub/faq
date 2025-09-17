---
id: ea4dbd6c83
question: In case you are using mac os and having trouble with WGET
section: 1. Introduction to Machine Learning
course: machine-learning-zoomcamp
sort_order: 540
---

Wget doesn't ship with macOS, so there are other alternatives to use.

No worries, we got curl:

example:

curl -o ./housing.csv https://raw.githubusercontent.com/alexeygrigorev/datasets/master/housing.csv

Explanations:

curl: a utility for retrieving information from the internet.

-o: Tell it to store the result as a file.

filename: You choose the file's name.

Links: Put the web address (URL) here, and cURL will extract data from it and save it under the name you provide.

More about it at:

Added by David Espejo

