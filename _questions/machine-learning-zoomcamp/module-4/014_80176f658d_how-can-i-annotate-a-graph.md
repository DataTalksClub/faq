---
id: 80176f658d
question: How can I annotate a graph?
sort_order: 14
---

Matplotlib has a cool method to [annotate](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.annotate.html) where you can provide an X,Y point and annotate with an arrow and text. For example, this will show an arrow pointing to the x,y point optimal threshold.

```python
plt.annotate(f'Optimal Threshold: {optimal_threshold:.2f}\nOptimal F1 Score: {optimal_f1_score:.2f}',

xy=(optimal_threshold, optimal_f1_score),

xytext=(0.3, 0.5),

textcoords='axes fraction',

arrowprops=dict(facecolor='black', shrink=0.05))
```