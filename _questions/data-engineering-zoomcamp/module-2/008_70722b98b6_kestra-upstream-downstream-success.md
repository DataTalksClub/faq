---
id: 70722b98b6
question: Why can a Kestra workflow show successful upstream tasks even when downstream
  tasks fail?
sort_order: 8
---

Kestra executes tasks independently according to defined dependencies. A task is marked successful if its own execution completes without error, regardless of downstream failures. This makes it possible to inspect intermediate outputs and logs (such as file size computation) even if later database or merge steps fail.