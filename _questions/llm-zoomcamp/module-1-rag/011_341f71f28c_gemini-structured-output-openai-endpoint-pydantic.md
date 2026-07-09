---
id: 341f71f28c
question: How can I get structured output (Pydantic objects) from Gemini via the OpenAI-compatible
  endpoint when responses.parse isn't available?
sort_order: 11
---

To get parsed structured output, use the OpenAI SDK’s chat-completions parsing flow instead of the newer Responses API. This is the right choice when you want to stay on the OpenAI SDK but call a chat-completions-compatible model like Gemini through the OpenAI-compatible endpoint.

Example code:

```python
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

response = client.chat.completions.parse(
    model="gemini-3.1-flash-lite",
    messages=messages,
    response_format=Questions
)

result = response.choices[0].message.parsed
print(result.questions)
```

Notes:
- This approach keeps using the OpenAI SDK while leveraging Gemini through Google's endpoint.
- The parsed output (e.g., `result.questions`) is available directly without manual JSON parsing.