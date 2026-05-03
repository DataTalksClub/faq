---
id: 25f96d0b34
question: 'dbt: Command ''dbt'' not found after installing dbt—how can I fix it?'
sort_order: 9
---

These steps fix the 'dbt' command not found error when dbt is installed inside a virtual environment:

1. Activate your virtual environment:
```
source ~/venvs/zoomcamp/bin/activate
```

2. Verify dbt is installed inside it:
```
which dbt
```

It should return something like:
```
~/venvs/zoomcamp/bin/dbt
```

3. If dbt is not installed, install it inside the activated environment:
```
pip install dbt-bigquery
```

4. Confirm installation:
```
dbt --version
```

If you want dbt available globally (not recommended), ensure the installation path is added to your PATH variable.