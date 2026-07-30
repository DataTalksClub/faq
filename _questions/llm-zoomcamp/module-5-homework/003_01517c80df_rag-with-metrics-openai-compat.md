---
id: 01517c80df
question: How do I adapt the monitoring homework to a provider such as Groq or
  Gemini that uses Chat Completions?
sort_order: 3
---

Do not give `starter.py` a fake `OPENAI_API_KEY`. Configure its module-level
client for your provider instead. For Groq:

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["GROQ_API_KEY"],
    base_url="https://api.groq.com/openai/v1",
)
rag = RAGBase(
    index=index,
    llm_client=client,
    model="<current-groq-model-id>",
)
```

Use a model ID currently available from your provider; an OpenAI model name
will return a `404` on Groq.

Next, keep the course's `LLMCallRecord` and `RAGBase`, but change the three
`RAGWithMetrics` methods that depend on the OpenAI Responses API. Providers
with an OpenAI-compatible Chat Completions endpoint return the answer and token
counts under different attributes:

```python
class RAGWithMetrics(RAGBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.last_call: LLMCallRecord | None = None

    def llm(self, prompt):
        start_time = time.time()
        response = self._call_llm(prompt)
        response_time = time.time() - start_time
        self._log_response(prompt, response, response_time)
        return response.choices[0].message.content

    def _call_llm(self, prompt):
        return self.llm_client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": self.instructions},
                {"role": "user", "content": prompt},
            ],
        )

    def _log_response(self, prompt, response, response_time):
        usage = response.usage
        self.last_call = LLMCallRecord(
            model=self.model,
            prompt=prompt,
            instructions=self.instructions,
            answer=response.choices[0].message.content,
            prompt_tokens=usage.prompt_tokens,
            completion_tokens=usage.completion_tokens,
            total_tokens=usage.total_tokens,
            response_time=response_time,
            cost=0.0,
        )
```

Configure `llm_client` with the provider's API key and OpenAI-compatible base
URL, and pass its model name to `RAGWithMetrics`. The `0.0` cost is a deliberate
placeholder: the course's `calculate_cost` handles only its OpenAI model. Add
the selected provider's current input and output prices before using cost in a
dashboard or database.

If the provider rejects the first request because it is already larger than
your token limit, retries and delays will not help. Reduce the retrieved
context—for example, change the default `num_results` in `RAGBase.search()` from
`5` to `2`—so each request fits within the limit.
