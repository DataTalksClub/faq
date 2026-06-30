---
id: 04440cab11
question: 'Kestra AI Copilot replies "I can only assist with creating Kestra flows"
  — how do I fix it?'
sort_order: 2
---

This message means the AI Copilot didn't get a valid Gemini API key, so it falls back to a canned refusal. In Kestra's Open Source edition the Copilot only supports Gemini, and it reads the **plain** `GEMINI_API_KEY` variable (not the base64-encoded `SECRET_GEMINI_API_KEY` that the flows use).

Make sure you exported the plain key before starting Kestra, then restart it:

```bash
export GEMINI_API_KEY="your-gemini-api-key-here"
docker compose up -d
```

If it still fails, the key is usually missing, mistyped, or rate-limited:

- Confirm the variable is actually set in the shell you ran `docker compose up` from (`echo $GEMINI_API_KEY`).
- Generate a fresh key in [Google AI Studio](https://aistudio.google.com/app/apikey).
- If you've been running the agent/multi-agent flows a lot, you may have hit the free-tier quota (`429 Resource Exhausted`) — wait a minute and retry.

Note that the Copilot needs the **plain** `GEMINI_API_KEY` while the flows need `SECRET_GEMINI_API_KEY` — export both.
