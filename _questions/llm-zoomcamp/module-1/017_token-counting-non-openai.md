---
id: 4d8c1f5b3a
question: 'How do I count tokens for a non-OpenAI model (Gemini, Mistral, HuggingFace)?'
sort_order: 17
---

`tiktoken` only ships tokenizers for OpenAI models. Using `cl100k_base` for other providers gives wrong counts and unreliable cost estimates.

For other providers, use their native tokenizer:

- Gemini:
  ```python
  import google.generativeai as genai
  model = genai.GenerativeModel('gemini-2.0-flash')
  print(model.count_tokens(prompt))
  ```
- Hugging Face / open-source models:
  ```python
  from transformers import AutoTokenizer
  tok = AutoTokenizer.from_pretrained("meta-llama/Llama-3.1-8B")
  print(len(tok.encode(prompt)))
  ```
- Mistral: use the official `mistral-common` tokenizer package.

Don't use `cl100k_base` as a generic fallback — token counts will diverge from what the provider actually bills.
