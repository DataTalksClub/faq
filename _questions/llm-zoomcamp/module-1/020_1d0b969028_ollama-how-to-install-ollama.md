---
id: 1d0b969028
question: 'Ollama: How to install Ollama?'
sort_order: 20
---

First, install Ollama by visiting [https://ollama.com/download](https://ollama.com/download) and choosing your operating system:

- **macOS**: Download the `.pkg` and install it.
- **Windows**: Download the `.msi` and install it.
- **Linux**: Run the following command in the terminal:

  ```bash
  curl -fsSL https://ollama.com/install.sh | sh
  ```

Once installed, open a terminal and type:

```bash
ollama run llama3
```

This command will:

- Download the LLaMA 3 model (~4GB).
- Start the model locally.
- Open a chat-like interface where you can type questions.

To test the Ollama local server, run the following command:

```bash
curl http://localhost:11434
```

You should receive a response similar to:

```json
{"models": [...]}  
```

Then, install the Python client with:

```bash
pip install ollama
```

Here is a minimal Python example:

```python
import ollama

response = ollama.chat(
    model='llama3',
    messages=[{"role": "user", "content": your_prompt}]
)

print(response['message']['content'])
```