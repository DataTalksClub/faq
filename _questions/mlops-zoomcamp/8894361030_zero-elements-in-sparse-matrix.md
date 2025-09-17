---
course: mlops-zoomcamp
id: '8894361030'
question: Zero elements in sparse matrix (AKA when dictionary vectorizer / categorical
  X transformation fails )
section: 'Module 1: Introduction'
sort_order: 720
---

Seeing <2855951x515 sparse matrix of type '<class 'numpy.float64'>'

with 0 stored elements in Compressed Sparse Row format>? It could be that your (soon to be vectorized) variables imported as floating point rather than integer. This will result in nonsensical models. Convert with (for dg being your dataframe, and categorical storing names of your variables to be vectorized):

dg[categorical] = dg[categorical].round(0).astype(int).astype(str)

