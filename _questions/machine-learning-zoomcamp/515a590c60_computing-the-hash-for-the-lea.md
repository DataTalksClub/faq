---
course: machine-learning-zoomcamp
id: 515a590c60
question: Computing the hash for the leaderboard and project review
section: 1. Introduction to Machine Learning
sort_order: 260
---

Leaderboard Links:

2024 -

2023 -

2022 -

Python Code:

from hashlib import sha1

def compute_hash(email):

return sha1(email.lower().encode('utf-8')).hexdigest()

You need to call the function as follows:

print(compute_hash('YOUR_EMAIL_HERE'))

The quotes are required to denote that your email is a string.

(By Wesley Barreto)

You can also use this website directly by entering your email: . Then, you just have to copy and paste your hashed email in the “research” bar of the leaderboard to get your scores.

(Mélanie Fouesnard)

