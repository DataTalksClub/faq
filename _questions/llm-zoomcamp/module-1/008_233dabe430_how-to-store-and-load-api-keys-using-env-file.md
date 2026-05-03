---
id: 233dabe430
question: How to store and load API keys using .env file
sort_order: 8
---

Store the API key in a `.env` file, then use the following steps to load it:

1. Import the necessary modules:
   
   ```python
   import os
   from dotenv import load_dotenv
   ```

2. Load the `.env` file:
   
   ```python
   load_dotenv(os.path.abspath("<path-to-.env>"))
   ```

3. Retrieve the API key:
   
   ```python
   os.getenv("API_KEY_abc")
   ```

- Ensure to add the `.env` file to your `.gitignore` to prevent it from being checked into version control.