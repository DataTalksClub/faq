---
id: 91df9f5c6f
question: 'PicklingError: Could not serialise object: IndexError: tuple index out
  of range.'
sort_order: 34
---

This error occurs while running:

```python
spark.createDataFrame(df_pandas).show()
```

### Cause
This issue is usually related to the Python version. As of March 2, 2023, Spark does not support Python 3.11.

### Solution

1. **Create a New Environment with a Supported Python Version:**

   Using Conda, you can create a virtual environment with Python 3.10:
   
   ```bash
   conda create -n myenv python=3.10 anaconda
   ```

2. **Activate the Environment:**

   To use Python 3.10, activate the environment:
   
   ```bash
   conda activate myenv
   ```

3. **Deactivate the Environment:**

   If you need to return to the initial setup, you can deactivate the environment:
   
   ```bash
   conda deactivate
   ```