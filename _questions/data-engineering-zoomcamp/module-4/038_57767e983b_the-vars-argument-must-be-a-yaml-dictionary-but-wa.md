---
id: 57767e983b
question: The - vars argument must be a YAML dictionary, but was of type str
sort_order: 38
---

Remember to add a space between the variable and the value. Otherwise, it won't be interpreted as a dictionary.

Correct usage:

```bash
dbt run --var 'is_test_run: false'
```

Not able to change Environment Type as it is greyed out and inaccessible. You don't need to change the environment type. If you are following the videos, you are creating a Production Deployment, so the only available option is the correct one.