---
id: a1469eef57
question: How does the project evaluation work for you as a peer reviewer?
section: Projects (Midterm and Capstone)
course: machine-learning-zoomcamp
sort_order: 3800
---

I am not sure how the project evaluate assignment works? Where do I find this? I have access to all the capstone 2 project, perhaps, I can randomly pick any to review.

Answer:

The link provided for example (2023/Capstone link ):  contains a list of all submitted projects to be evaluated. More specific, you are to review 3 assigned peer projects. In the spreadsheet are 3 hash values of your assigned peer projects. However, you need to derive the your hash value of your email address and find the value on the spreadsheet under the (reviewer_hash) heading.

To calculate your hash value run the python code below:

from hashlib import sha1

def compute_hash(email):

return sha1(email.lower().encode('utf-8')).hexdigest()

# Example usage **** enter your email below (Example1@gmail.com)****

email = "Example1@gmail.com"

hashed_email = compute_hash(email)

print("Original Email:", email)

print("Hashed Email (SHA-1):", hashed_email)

Edit the above code to replace  as your email address

Store and run the above python code from your terminal. See below as the Hashed Email (SHA-1) value

![Image](images/machine-learning-zoomcamp/image_5d15610e.png)

You then go to the link:

Lastly, copy the “Hashed Email (SHA-1): bd9770be022dede87419068aa1acd7a2ab441675” value and search for 3 identical entries. There you should see your peer project to be reviewed.

![Image](images/machine-learning-zoomcamp/image_ca88b4f9.png)

By Emmanuel Ayeni

