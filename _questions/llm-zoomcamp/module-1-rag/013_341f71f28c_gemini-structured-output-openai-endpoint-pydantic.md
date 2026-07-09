---
id: 341f71f28c
question: How can I get structured output (Pydantic objects) from Gemini via the OpenAI-compatible
  endpoint when responses.parse isn't available?
sort_order: 11
---

To get parsed structured output, use the OpenAI SDK's chat-completions parsing flow instead of the newer Responses API. This is the right choice when you want to stay on the OpenAI SDK but call a chat-completions-compatible model like Gemini through the OpenAI-compatible endpoint.

First, define the structure you want Gemini to return as a Pydantic model:

```python
from pydantic import BaseModel

class Question(BaseModel):
    question: str
    answer: str

class Questions(BaseModel):
    questions: list[Question]
```

Then call `chat.completions.parse` with `response_format=Questions`. Pass the same kind of `messages` you would to any chat completion:

```python
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

messages = [
    {"role": "developer", "content": "Generate three FAQ questions about RAG."},
    {"role": "user", "content": "Topic: structured output with Gemini"}
]

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
- The parsed output (e.g., `result.questions`) is a Pydantic object available directly, with no manual JSON parsing.
- `chat.completions.parse` requires `pydantic` (`uv add pydantic`).
