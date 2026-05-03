---
id: acd25600d1
question: How to configure and run a Python script in Kestra Docker on Windows 11
  without the 'Could not find or install 'Python 3.13' path' error?
sort_order: 13
---

```yaml
type: io.kestra.plugin.scripts.python.Commands
commands:
  - pip install requests kestra
  - python your_script.py
InputFiles:
  your_script.py: |
    # Python script content from before
```

To use, replace `your_script.py` with your actual script filename and paste the Python code under `InputFiles`.