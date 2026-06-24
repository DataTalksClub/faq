---
id: ea815eb858
question: Can I use a programming language other than Python (for example JavaScript, TypeScript, Go, Rust, Java, Scala, C#, or R) for homework or the project?
sort_order: 12
---

In most cases, use Python. The course materials, examples, and reviewer expectations are Python-based, so Python is the easiest path. This applies to every homework and to the final/capstone project.

Using another programming language or stack - for example JavaScript, TypeScript, Go, Rust, Java, Scala, C#, or R - is technically possible, but do it only if you have a strong reason. We do not want to restrict your choice of technology, but a non-Python stack makes reproducibility and review harder.

If you use a language other than Python, your documentation must be very thorough. Assume the reviewer has no knowledge of that language or ecosystem. Your README should explain how to install dependencies and run the homework or project on Windows, macOS, and Linux.

For example, a Go project should include steps at the level of:

```bash
go mod tidy
go run .
```

The submission must still be easy to reproduce and evaluate.
