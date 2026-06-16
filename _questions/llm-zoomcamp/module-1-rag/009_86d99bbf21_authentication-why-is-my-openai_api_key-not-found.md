---
id: 86d99bbf21
question: 'Authentication: Why is my OPENAI_API_KEY not found in the Jupyter notebook?'
sort_order: 9
---



There are two options to resolve this issue:

**Option 1: Using direnv**

1. Create a `.envrc` file and add your API key.
2. Run `direnv allow` in the terminal.

If you encounter the error:

```python
OpenAIError: The api_key client option must be set either by passing api_key to the client or by setting the OPENAI_API_KEY environment variable
```

- Install `dotenv` by running:

    ```bash
    pip install python-dotenv
    ```

- Add the following to a cell in the notebook:

    ```python
    from dotenv import load_dotenv
    
    load_dotenv('.envrc')
    ```

**Option 2: Using Codespaces Secrets**

1. Log in to your GitHub account and navigate to **Settings > Codespaces**.
2. In the Secrets section, create a secret like `OPENAI_API_KEY` and select the repositories for which the secret should be available.
3. Once set up, the key will be available in your Codespaces session.