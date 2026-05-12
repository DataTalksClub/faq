---
id: 675f59049a
question: After eb init, EB ignores my profile / picks the wrong region
sort_order: 71
---

Pass `--profile` and `-r` (region) explicitly:

```bash
eb init --profile myprofile -p docker -r eu-west-3 churn-serving
```
