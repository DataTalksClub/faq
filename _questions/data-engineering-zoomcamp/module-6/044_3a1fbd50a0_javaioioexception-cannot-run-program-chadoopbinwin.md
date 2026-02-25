---
id: 3a1fbd50a0
question: Java.io.IOException. Cannot run program “C:\hadoop\bin\winutils.exe”. CreateProcess
  error=216, This version of 1% is not compatible with the version of Windows you
  are using.
sort_order: 44
---

To resolve the issue, follow these steps:

1. Change the Hadoop version to 3.0.1.
2. Replace all the files in the local Hadoop `bin` folder with the files from this repository: [winutils/hadoop-3.0.1/bin at master · cdarlint/winutils](https://github.com/cdarlint/winutils/tree/master/hadoop-3.0.1/bin).
3. If this does not work, try other versions available in the repository.

For more information, refer to the following issue discussion: [This version of %1 is not compatible with the version of Windows you're running · Issue #20 · cdarlint/winutils](https://github.com/cdarlint/winutils/issues/20)