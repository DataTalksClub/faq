---
id: a489fb34ac
question: Should I include my .env_encoded file in my .gitignore?
section: Module 2: Workflow Orchestration
course: data-engineering-zoomcamp
sort_order: 1910
---

⚠️ Yes, you should definitely include the .env_encoded file in your .gitignore file. Here's why:

Security: The .env_encoded file contains sensitive information, namely the base64 encoded version of your GCP Service Account key. Even though it's encoded, it's not secure to share this in a public repository as anyone can decode it back to the original JSON.

Best Practices: It's a common practice to not commit environment files or any files containing secrets to version control systems like Git. This prevents accidental exposure of sensitive data.

⚠️ How to do it:
# Add this line to your .gitignore file
.env_encoded

⚠️ More on Security:
Base64 encoding is easily reversible. Base64 is an encoding scheme, not an encryption method. It's designed to encode binary data into ASCII characters that can be safely transmitted over systems that are designed to deal with text. Here's why it's not secure for protecting sensitive information:

Reversibility: Base64 encoding simply translates binary data into a text string using a specific set of 64 characters. Decoding it back to the original data is straightforward and doesn't require any secret key or password.

Public Availability of Tools: Numerous online tools, software libraries, and command-line utilities exist that can decode base64 with just a few clicks or commands.

No Security: Since base64 encoding does not change or hide the actual content of the data, anyone with access to the encoded string can decode it back to the original data.

