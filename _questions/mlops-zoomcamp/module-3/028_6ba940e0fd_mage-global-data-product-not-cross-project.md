---
id: 6ba940e0fd
question: "Mage: cannot create a Global Data Product across projects"
sort_order: 28
---

If you try to build a Global Data Product that points at a pipeline in a different Mage project, it fails with:

```
AttributeError: 'NoneType' object has no attribute 'to_dict'
```

Mage's Global Data Products are not cross-project. Create the data preparation pipeline inside the same project that consumes it (e.g. `unit_2_training`) and configure it to build there.
