---
id: 5e953f0e8e
question: Read-in the File in Windows OS
sort_order: 6
---

How do I read the dataset with Pandas in Windows?

I used the code below but it's not working:

```python
df = pd.read_csv('C:\Users\username\Downloads\data.csv')
```

Unlike Linux/Mac OS, Windows uses the backslash (`\`) to navigate the files, which causes a conflict with Python. In Python, the `\` is used for escape sequences, e.g., `\n` for a new line or `\t` for a tab. To avoid this issue, add an `r` before the file path to treat it as a raw string:

```python
df = pd.read_csv(r'C:\Users\username\Downloads\data.csv')
```