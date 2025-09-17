---
course: machine-learning-zoomcamp
id: 9dc70bef80
question: Getting error module scipy not found during model training in Saturn Cloud
  tensorflow image
section: 8. Neural Networks and Deep Learning
sort_order: 2770
---

The above error happens since module scipy is not installed in the saturn cloud tensorflow image. While creating the Jupyter server resource, in the “Extra Packages” section under pip in the textbox write scipy. Below the textbox, the pip install scipy command will be displayed. This will ensure when the resource spins up, the scipy package will be automatically installed. This approach can also be followed for additional python packages.

Sumeet Lalla

