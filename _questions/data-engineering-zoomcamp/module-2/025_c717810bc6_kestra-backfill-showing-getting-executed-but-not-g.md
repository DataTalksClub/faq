---
id: c717810bc6
question: 'Kestra: Backfill showing getting executed but not getting results or showing
  up in executions'
sort_order: 25
---

It seems to be a bug. The current fix is to remove the timezone from triggers in the script. More on this bug is [here](https://github.com/kestra-io/kestra/issues/7227).