---
id: 52858dfd98
question: 'Postgres - ModuleNotFoundError: No module named ''psycopg2'''
sort_order: 76
---

Issue:

```
ModuleNotFoundError: No module named 'psycopg2'
```

Solution:

1. Install psycopg2-binary:
   
   ```bash
   pip install psycopg2-binary
   ```

2. If psycopg2-binary is already installed, update it:
   
   ```bash
   pip install psycopg2-binary --upgrade
   ```

3. Other methods if the above fails:

   - If the error persists, update conda:
     
     ```bash
     conda update -n base -c defaults conda
     ```

   - Alternatively, update pip:
     
     ```bash
     pip install --upgrade pip
     ```

   - Reinstall psycopg:
     
     - Uninstall the psycopg package.
     - Update conda or pip.
     - Reinstall psycopg using pip.

   - If an error shows about `pg_config` not being found, install PostgreSQL:
     
     - On Mac, use:
       
       ```bash
       brew install postgresql
       ```