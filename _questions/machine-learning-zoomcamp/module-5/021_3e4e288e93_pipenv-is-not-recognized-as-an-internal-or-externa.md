---
id: 3e4e288e93
images:
- description: 'image #1'
  id: image_1
  path: images/machine-learning-zoomcamp/image_6db28918.png
- description: 'image #2'
  id: image_2
  path: images/machine-learning-zoomcamp/image_3b4fce52.png
- description: 'image #3'
  id: image_3
  path: images/machine-learning-zoomcamp/image_b2712e9d.png
- description: 'image #4'
  id: image_4
  path: images/machine-learning-zoomcamp/image_a4cd7017.png
question: '''pipenv'' is not recognized as an internal or external command, operable
  program or batch file.'
sort_order: 21
---

This error occurs because `pipenv` is installed but not accessible from the PATH.

You might encounter this error when running:

```bash
pipenv --version
```

or

```bash
pipenv shell
```

**Solution for Windows:**

1. Open this option:
   
   <{IMAGE:image_1}>

2. Click here:
   
   <{IMAGE:image_2}>

3. Click the Edit button:
   
   <{IMAGE:image_3}>

4. Ensure the following locations are included in the PATH. If not, add them:
   
   - `C:\Users\AppData\...\Python\PythonXX\`
   - `C:\Users\AppData\...\Python\PythonXX\Scripts\`
   
   <{IMAGE:image_4}>

**Note:** This solution is for setups without Anaconda. If you use Windows, Anaconda might be a better and less error-prone choice.