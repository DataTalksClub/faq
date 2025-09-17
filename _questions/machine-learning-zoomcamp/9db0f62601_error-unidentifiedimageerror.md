---
course: machine-learning-zoomcamp
id: 9db0f62601
question: 'Error UnidentifiedImageError: cannot identify image file'
section: Miscellaneous
sort_order: 3990
---

In deploying model part, I wanted to test my model locally on a test-image data and I had this silly error after the following command:

url = 'https://github.com/bhasarma/kitchenware-classification-project/blob/main/test-image.jpg'

X = preprocessor.from_url(url)

I got the error:

UnidentifiedImageError: cannot identify image file <_io.BytesIO object at 0x7f797010a590>

Solution:

Add ?raw=true after .jpg in url. E.g. as below

url = ‘https://github.com/bhasarma/kitchenware-classification-project/blob/main/test-image.jpg?raw=true’

Bhaskar Sarma

