---
course: machine-learning-zoomcamp
id: 167b32b84c
question: 'BentoML not working with –production flag at any stage: e.g. with bentoml
  serve and while running the bentoml container'
section: Miscellaneous
sort_order: 3920
---

You might see a long error message with something about sparse matrices, and in the swagger UI, you get a code 500 error with “” (empty string) as output.

Potential reason: Setting DictVectorizer or OHE to sparse while training, and then storing this in a pipeline or custom object in the benotml model saving stage in train.py. This means that when the custom object is called in service.py, it will convert each input to a different sized sparse matrix, and this can't be batched due to inconsistent length. In this case, bentoml model signatures should have batchable set to False for production during saving the bentoml mode in train.py.

(Memoona Tahira)

