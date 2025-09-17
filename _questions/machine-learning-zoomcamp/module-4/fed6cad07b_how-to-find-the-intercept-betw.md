---
id: fed6cad07b
question: How to find the intercept between precision and recall curves by using numpy?
sort_order: 1600
---

You can find the intercept between these two curves using numpy diff ([https://numpy.org/doc/stable/reference/generated/numpy.diff.html](https://numpy.org/doc/stable/reference/generated/numpy.diff.html) ) and sign ([https://numpy.org/doc/stable/reference/generated/numpy.sign.html](https://numpy.org/doc/stable/reference/generated/numpy.sign.html)):

I suppose here that you have your df_scores ready with your three columns ‘threshold’, ‘precision’ and ‘recall’:

You want to know at which index (or indices) you have your intercept between precision and recall (namely: where the sign of the difference between precision and recall changes):

idx = np.argwhere(

np.diff(

np.sign(np.array(df_scores["precision"]) - np.array(df_scores["recall"]))

)

).flatten()

You can print the result to easily read it:

print(

f"The precision and recall curves intersect at a threshold equal to {df_scores.loc[idx]['threshold']}."

)

(Mélanie Fouesnard)

