---
id: 15e931476c
images:
- description: 'image #1'
  id: image_1
  path: images/llm-zoomcamp/image_c9b96ca3.png
question: 'In Windows OS: OSError: [WinError 126] The specified module could not be
  found. Error loading "C:\Users\USER\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\lib\fbgemm.dll"
  or one of its dependencies.'
sort_order: 1
---

- **Solution 1**: Install Visual C++ Redistributable.

- **Solution 2**: Install Visual Studio, not Visual Studio Code. 

  <{IMAGE:image_1}>

  For more details, please follow this link: [discuss.pytorch.org](https://discuss.pytorch.org/t/failed-to-import-pytorch-fbgemm-dll-or-one-of-its-dependencies-is-missing/201969)