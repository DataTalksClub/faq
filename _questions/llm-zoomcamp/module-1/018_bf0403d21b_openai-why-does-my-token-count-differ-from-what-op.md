---
id: bf0403d21b
question: 'OpenAI: Why does my token count differ from what OpenAI reports?'
sort_order: 18
---

When using `tiktoken.encode()` to count tokens in your prompt, you might see a difference compared to OpenAI’s API response. For instance, you might get 320 tokens, while OpenAI reports 327. This is due to internal tokens added by OpenAI’s chat formatting.

Here’s what happens:

- Each message in a `chat.completions.create()` call (e.g., `{role: "user", content: "..."}`) adds 4 structural tokens (role, content, separators).
- The API adds 2 tokens globally to mark the start of assistant response generation.
- Extra newlines, whitespace, or uncommon Unicode characters in your content may slightly increase the token count.

Thus, even if your visible text is 320 tokens, OpenAI may count 327 due to these internal additions.