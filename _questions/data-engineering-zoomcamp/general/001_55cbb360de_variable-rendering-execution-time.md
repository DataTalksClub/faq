---
id: 55cbb360de
question: Why is variable rendering only visible at execution time?
sort_order: 1
---

Variable rendering depends on runtime inputs and execution context. Until the workflow is executed with specific parameters, Kestra cannot resolve templates into concrete values. Rendered results are therefore only observable during or after execution.