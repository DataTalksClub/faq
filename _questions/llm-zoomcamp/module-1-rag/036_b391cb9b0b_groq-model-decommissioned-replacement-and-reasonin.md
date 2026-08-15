---
id: b391cb9b0b
question: My Groq model stopped working — I'm getting a GroqError or model_decommissioned
  error. What do I do?
sort_order: 36
---

As of August 2026, `llama-3.3-70b-versatile` and `qwen/qwen3-32b` are being retired by Groq. If you see errors like `GroqError` / `model_decommissioned`, switch to a currently supported model.

Recommended replacement (as of the report):
- `MODEL = "openai/gpt-oss-120b"`

Also check your request parameters:
- `gpt-oss-120b` accepts only `reasoning_effort` values: `"low"`, `"medium"`, or `"high"`.
- If your code uses `reasoning_effort="none"`, update it to `reasoning_effort="low"`.
- Otherwise you can get a validation error on every request.

If you’re still failing after switching models, verify the exact model id you’re sending to Groq matches the new one you intend to use (including case/spelling) and that `reasoning_effort` is set to one of the supported values.