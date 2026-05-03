---
id: f5a8ca34fa
question: Why does the CSV file size shown in the Kestra Outputs tab differ from the value printed by a Python task?
sort_order: 21
---

Kestra displays file sizes in the Outputs tab using human-readable units (e.g., MiB), while a Python task using `os.path.getsize()` returns the raw file size in bytes. For Homework 2, the correct value is the uncompressed file size in bytes (as printed in task logs), not the rounded UI value. The UI size is a convenience display and should not be used for exact comparisons.
