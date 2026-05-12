---
id: d6dd8c7f90
question: 'Pandas ParserError: Expected 1 fields in line N, saw M when reading a CSV downloaded with wget'
sort_order: 38
---

`wget` saved an HTML page (the GitHub web view), not the actual CSV. Use the **raw** GitHub URL:

```
https://raw.githubusercontent.com/<user>/<repo>/<branch>/<path>.csv
```

NOT `https://github.com/<user>/<repo>/blob/...` — that serves an HTML page. Verify with `head data.csv` — if you see HTML tags, you have the wrong URL.
