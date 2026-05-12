---
id: c336d11260
question: 'Problem: ''ls'' is not recognized as an internal or external command, operable
  program or batch file.'
sort_order: 7
---

When trying to run the command `!ls -lh` in a Windows Jupyter Notebook, you may receive an error:

```
'ls' is not recognized as an internal or external command, operable program or batch file.
```

Solution:

Instead of `!ls -lh`, you can use this command:

```bash
!dir
```

This will provide similar output.