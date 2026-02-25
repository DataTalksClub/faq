---
id: d039adfb76
images:
- description: 'image #1'
  id: image_1
  path: images/data-engineering-zoomcamp/image_07f863ec.png
- description: 'image #2'
  id: image_2
  path: images/data-engineering-zoomcamp/image_df52218e.png
- description: 'image #3'
  id: image_3
  path: images/data-engineering-zoomcamp/image_deaf91b1.png
- description: 'image #4'
  id: image_4
  path: images/data-engineering-zoomcamp/image_8584c5ce.png
question: 'Java Kafka: Tests are not picked up in VSCode'
sort_order: 25
---

In VS Code, you might expect to see a triangle icon next to each test method in your Java files. If you don't see it, here are the steps to fix the issue:

1. Open **Explorer** (first icon on the left navigation bar).
2. Navigate to **JAVA PROJECTS** (bottom collapsable section).
3. Click the icon in the rightmost position next to **JAVA PROJECTS** to open the options.
   
   <{IMAGE:image_1}>

   <{IMAGE:image_2}>
   
   <{IMAGE:image_3}>

4. Select **Clean Workspace**.
5. Confirm by clicking **Reload and Delete**.

Following these steps should restore the triangle icons you expect to see next to each test, similar to those visible in Python tests.

Example:

<{IMAGE:image_4}>

Additionally, you can add classes and packages in this window instead of creating files directly in the project directory.