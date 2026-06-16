---
id: ea815eb858
question: Can I use something other than Python for homework or the project?
sort_order: 12
---

In most cases, use Python. The course materials, examples, and reviewer expectations are Python-based, so Python is the easiest path.

Using another language or stack is technically possible, but do it only if you have a strong reason. We do not want to restrict your choice of technology, but using a different stack makes reproducibility and review harder.

If you use another language, for example Go, your documentation must be very thorough. Assume the reviewer has no knowledge of that language or ecosystem. Your README should explain how to install dependencies and run the homework or project on Windows, macOS, and Linux.

For Go, include steps at the level of:

```bash
go mod tidy
go run .
```

The submission must still be easy to reproduce and evaluate.
