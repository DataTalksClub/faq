---
id: e4654d1d0b
question: Export PYTHONPATH command in linux is temporary
section: Module 5: pyspark
course: data-engineering-zoomcamp
sort_order: 3590
---

You can either type the export command every time you run a new session, add it to the .bashrc/ which you can find in /home or run this command at the beginning of your homebook:

import findspark

findspark.init()

