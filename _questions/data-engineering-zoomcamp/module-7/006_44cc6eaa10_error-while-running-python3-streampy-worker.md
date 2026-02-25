---
id: 44cc6eaa10
question: Error while running python3 stream.py worker
sort_order: 6
---

If you get an error while running the command `python3 stream.py worker`, follow these steps:

1. Uninstall the current `kafka-python` package:
   
   ```bash
   pip uninstall kafka-python
   ```

2. Install the specific version of `kafka-python`:

   ```bash
   pip install kafka-python==1.4.6
   ```