---
course: machine-learning-zoomcamp
id: 9fbb36bb16
question: Alternative way to load the data using requests
section: 2. Machine Learning for Regression
sort_order: 670
---

Above users showed how to load the dataset directly from github. Here is another useful way of doing this using the `requests` library:

# Get data for homework

import requests

url = 'https://raw.githubusercontent.com/alexeygrigorev/datasets/master/housing.csv'

response = requests.get(url)

if response.status_code == 200:

with open('housing.csv', 'wb') as file:

file.write(response.content)

else:

print("Download failed.")

Tyler Simpson

