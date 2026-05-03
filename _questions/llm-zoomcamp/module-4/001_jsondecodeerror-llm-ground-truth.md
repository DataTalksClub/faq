---
id: a3c7e1b4f9
question: 'Evaluation: "JSONDecodeError: Expecting value" when generating ground-truth
  questions with the LLM'
sort_order: 1
---

The LLM sometimes wraps the JSON in a markdown code fence or adds prose around it, so `json.loads(response)` fails with:

```
JSONDecodeError: Expecting value: line 1 column 1 (char 0)
```

Force JSON output with OpenAI's `response_format`:

```python
response = openai_client.chat.completions.create(
    model='gpt-4o-mini',
    messages=[{"role": "user", "content": prompt}],
    response_format={"type": "json_object"},
)
parsed = json.loads(response.choices[0].message.content)
```

Also be explicit in the prompt about the expected shape:

```
Output a JSON object with a single key "questions" whose value is a list of 5 strings.
Do not include any extra text, explanation, or formatting.
```

Most providers have an equivalent (Gemini's `response_mime_type="application/json"`, Groq's `response_format`, etc.).
