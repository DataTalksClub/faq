---
id: 2c24ec504d
question: Why do I get different answers for the same question even though my RAG
  index hasn't changed?
sort_order: 32
---

It’s normal for an LLM to produce slightly different answers to the same question even when the retrieved documents are identical.

Common reasons include:
- The model is using a non-zero `temperature`, which introduces randomness.
- The hosted/provider model may change over time (optimizations, updates, or routing).
- The retrieved context can come back in a different order when multiple chunks/documents have very similar relevance scores.
- Small prompt changes or formatting differences can affect the final response.

If you need reproducible outputs (for testing or evaluation):
- Set `temperature=0`.
- Keep retrieval deterministic (same query, same index, and stable tie-breaking when scores are close).
- Ensure the prompt template and formatting stay unchanged.
- Use the same model version/provider for every run.

This is expected behavior and doesn’t necessarily mean your RAG pipeline is incorrect.