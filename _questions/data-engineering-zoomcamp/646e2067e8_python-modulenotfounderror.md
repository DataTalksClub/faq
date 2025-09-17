---
course: data-engineering-zoomcamp
id: 646e2067e8
question: 'Python - ModuleNotFoundError: No module named ''pysqlite2'''
section: 'Module 1: Docker and Terraform'
sort_order: 1300
---

ImportError: DLL load failed while importing _sqlite3: The specified module could not be found. ModuleNotFoundError: No module named 'pysqlite2'

The issue seems to arise from the missing of sqlite3.dll in path ".\Anaconda\Dlls\".

✅I solved it by simply copying that .dll file from \Anaconda3\Library\bin and put it under the path mentioned above. (if you are using anaconda)

