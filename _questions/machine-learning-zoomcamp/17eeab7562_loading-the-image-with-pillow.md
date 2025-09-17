---
id: 17eeab7562
question: Loading the Image with PILLOW library and converting to numpy array
section: Miscellaneous
course: machine-learning-zoomcamp
sort_order: 3840
---

Pip install pillow - install pillow library

from PIL import Image

img = Image.open('aeroplane.png')

From numpy import asarray

numdata=asarray(img)

Krishna Anand

