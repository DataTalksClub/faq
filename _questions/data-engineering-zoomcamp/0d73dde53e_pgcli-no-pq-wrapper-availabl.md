---
course: data-engineering-zoomcamp
id: 0d73dde53e
question: PGCLI - no pq wrapper available.
section: 'Module 1: Docker and Terraform'
sort_order: 1100
---

ImportError: no pq wrapper available.

Attempts made:

- couldn't import \dt

opg 'c' implementation: No module named 'psycopg_c'

- couldn't import psycopg 'binary' implementation: No module named 'psycopg_binary'

- couldn't import psycopg 'python' implementation: libpq library not found

Solution:

First, make sure your Python is set to 3.9, at least.

And the reason for that is we have had cases of 'psycopg2-binary' failing to install because of an old version of Python (3.7.3). 

0. You can check your current python version with: 
$ python -V (the V must be capital)

1. Based on the previous output, if you've got a 3.9, skip to Step #2
   Otherwise better off with a new environment with 3.9

$ conda create --name de-zoomcamp python=3.9
$ conda activate de-zoomcamp

2. Next, you should be able to install the lib for postgres like this:

```

$ pip install psycopg2-binary

$ pip install psycopg_binary

```

3. If above steps do not work, try:

```

$

pip install --upgrade pgcli

```

4. Finally, make sure you're also installing pgcli, but use conda for that:
```
$ pgcli -h localhost -U root -d ny_taxisudo

```

There, you should be good to go now!

Another solution:

Run this

