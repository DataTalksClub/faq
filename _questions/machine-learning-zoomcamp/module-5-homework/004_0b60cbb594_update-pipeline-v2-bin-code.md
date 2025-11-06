---
id: 0b60cbb594
question: The homework instructions say Docker file has a new pipeline. Do I need
  to do any changes in my code to reflect it?
sort_order: 4
---

Yes. Since the homework specifies a new pipeline file, update your code to load pipeline_v2.bin instead of pipeline_v1.bin. Use the following snippet:

```python
with open('pipeline_v2.bin', 'rb') as f_in:
    pipeline = pickle.load(f_in)
```
