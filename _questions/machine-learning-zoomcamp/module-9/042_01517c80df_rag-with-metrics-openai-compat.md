---
id: 01517c80df
question: How do I adapt the RAGWithMetrics class to work with OpenAI-compatible endpoints
  like Google Gemini?
sort_order: 42
---

To use RAGWithMetrics with OpenAI-compatible endpoints (e.g., Gemini) you switch the internal LLM call to the standard chat completions workflow and adjust how you extract content and usage metrics.

```python
import time

class RAGWithMetrics(RAGBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.last_call: LLMCallRecord = None

    def llm(self, prompt):
        start_time = time.time()
        response = self._call_llm(prompt)
        response_time = time.time() - start_time
        self._log_response(prompt, response, response_time)
        return response.choices[0].message.content

    def _call_llm(self, prompt):
        input_messages = [
            {"role": "developer", "content": self.instructions},
            {"role": "user", "content": prompt},
        ]

        # Switched from the OpenAI-specific Responses API to chat completions
        response = self.llm_client.chat.completions.create(
            model=self.model,
            messages=input_messages,
        )
        return response

    def _log_response(self, prompt, response, response_time):
        usage = response.usage
        cost = calculate_cost(self.model, usage)

        call_record = LLMCallRecord(
            model=self.model,
            prompt=prompt,
            instructions=self.instructions,
            answer=response.choices[0].message.content,
            prompt_tokens=usage.prompt_tokens,
            completion_tokens=usage.completion_tokens,
            total_tokens=usage.total_tokens,
            response_time=response_time,
            cost=cost,
        )
        print(call_record)
        self.last_call = call_record
```

Notes:
- The LLM call path uses `client.chat.completions.create` instead of `client.responses.create`.
- Extraction now reads `response.choices[0].message.content` and `response.usage` for token counts and cost.
- Ensure your `llm_client` is configured for the OpenAI-compatible interface provided by Gemini or other providers.