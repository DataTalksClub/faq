---
course: machine-learning-zoomcamp
id: 5e953f0e8e
question: Read-in the File in Windows OS
section: 1. Introduction to Machine Learning
sort_order: 330
---

How do I read the dataset with Pandas in Windows?

I used the code below but not working

df = pd.read_csv('C:\Users\username\Downloads\data.csv')

Unlike Linux/Mac OS, Windows uses the backslash (\) to navigate the files that cause the conflict with Python. The problem with using the backslash is that in Python, the '\' has a purpose known as an escape sequence. Escape sequences allow us to include special characters in strings, for example, "\n" to add a new line or "\t" to add spaces, etc. To avoid the issue we just need to add "r" before the file path and Python will treat it as a literal string (not an escape sequence).

Here’s how we should be loading the file instead:

df = pd.read_csv(r'C:\Users\username\Downloads\data.csv')

(Muhammad Awon)

