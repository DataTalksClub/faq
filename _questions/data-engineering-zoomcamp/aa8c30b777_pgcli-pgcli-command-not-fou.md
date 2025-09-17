---
course: data-engineering-zoomcamp
id: aa8c30b777
question: 'PGCLI - pgcli: command not found'
section: 'Module 1: Docker and Terraform'
sort_order: 1130
---

Problem: If you have already installed pgcli but bash doesn't recognize pgcli

On Git bash: bash: pgcli: command not found

On Windows Terminal: pgcli: The term 'pgcli' is not recognized…

Solution: Try adding a Python path C:\Users\...\AppData\Roaming\Python\Python39\Scripts to Windows PATH

For details:

Get the location: pip list -v

Copy C:\Users\...\AppData\Roaming\Python\Python39\site-packages

3. Replace site-packages with Scripts: C:\Users\...\AppData\Roaming\Python\Python39\Scripts

It can also be that you have Python installed elsewhere.

For me it was under c:\python310\lib\site-packages

So I had to add c:\python310\lib\Scripts to PATH, as shown below.

Put the above path in "Path" (or "PATH") in System Variables

![Image](images/data-engineering-zoomcamp/image_b33cbd22.png)

Reference:

