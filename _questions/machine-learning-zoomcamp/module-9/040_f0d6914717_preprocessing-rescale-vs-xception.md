---
id: f0d6914717
question: HW9 prediction value is far from the answer options (e.g. 0.0xyz vs 0.24/0.44/0.64/0.84)
sort_order: 40
---

Use simple [0, 1] rescaling, NOT the Xception-style preprocessing from earlier lectures:

```python
def preprocess_input(x):
    return x / 255.0
```

`x / 127.5 - 1` is correct for transfer learning from Xception, but the homework's model was trained from scratch with `[0, 1]` rescaling. Match what the model was trained with.
