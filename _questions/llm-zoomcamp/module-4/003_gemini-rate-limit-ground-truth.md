---
id: c1e9f4b820
question: 'Evaluation: hitting rate limits while generating the ground-truth dataset'
sort_order: 3
---

Free-tier Gemini limits both per-minute and per-day requests. Adding `time.sleep(4)` only fixes the per-minute side — a long `tqdm` loop can still blow through the per-day quota in one run.

Options when this happens:

- Spend ~$5 on OpenAI and use `gpt-4o-mini`. It's cheap enough to embed/generate the entire ground-truth set and has higher rate limits.
- Use Groq's free tier (`llama-3.3-70b-versatile`) — generous request-per-minute limits.
- Lower concurrency for thread-pool calls. Use a smaller pool size (2–3 workers) instead of pushing the API hard.
- Resume from where you stopped. Save progress periodically (e.g. dump the partial results to a JSONL file) so a hit limit doesn't lose all work.
