---
id: 5b54567e89
question: Opening an HTML file with a Windows browser from Linux running on WSL
section: Course Management Platform for Homeworks, Project and Certificate
course: data-engineering-zoomcamp
sort_order: 460
---

If you’re running Linux on Windows Subsystem for Linux (WSL) 2, you can open HTML files from the guest (Linux) with whatever Internet Browser you have installed on the host (Windows). Just install  and open the page with wslview <file>, for example:

wslview index.html

You can customise which browser to use by setting the BROWSER environment variable first. For example:

export BROWSER='/mnt/c/Program Files/Firefox/firefox.exe'

