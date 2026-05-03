---
id: 39328a73c7
question: Why must a file be declared again under outputFiles for it to be visible
  or downloadable in Kestra?
sort_order: 19
---

Kestra isolates task execution contexts. Files are only persisted and made available to subsequent tasks or the UI when explicitly declared under outputFiles. Without this declaration, files may exist temporarily during execution but are not surfaced or retained for inspection.