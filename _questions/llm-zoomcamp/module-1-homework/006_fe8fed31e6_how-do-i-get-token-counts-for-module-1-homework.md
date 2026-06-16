---
id: fe8fed31e6
question: How do I get token counts for Module 1 homework if I use a different provider?
sort_order: 6
---

For the current Module 1 homework, get the token count from the model response object.

For example, OpenAI-compatible clients usually return usage information on the response, such as `response.usage.input_tokens` or `response.usage.prompt_tokens`, depending on the API style.

If you use a non-OpenAI provider, check the provider's response object for its usage fields and adapt the code. Do not use `tiktoken` or `cl100k_base` as a generic tokenizer for Gemini, Mistral, Hugging Face, Groq, or other providers because tokenization differs by model.

If your provider does not expose token usage, use that provider's native tokenizer as an approximation. For multiple-choice homework questions, choose the closest option.
