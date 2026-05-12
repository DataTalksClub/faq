---
id: f6dbc97ce3
question: 'eb create fails: ''Creating Auto Scaling launch configuration failed ... Use launch templates'''
sort_order: 69
---

AWS deprecated launch configurations in October 2024. Easiest fix: pass `--enable-spot`, which forces EB to use launch templates:

```bash
eb create churn-serving-env --enable-spot
```

Alternatively, run the interactive `eb create` wizard and answer YES to "Spot fleet requests".
