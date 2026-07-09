---
id: a4adc70f41
question: Why is token usage monitored in Kestra workflows?
sort_order: 9
---

Token usage is tracked because it maps directly to what LLM providers charge you for, and Kestra workflows run LLM calls on a schedule or in loops where costs add up fast. The main reasons:

- **Cost control**: tokens are the unit providers bill by, so tracking usage lets you budget, forecast, and spot cost spikes before they get expensive.
- **Prompt optimization**: seeing how many tokens each prompt and response consumes helps you tighten prompts and trim output without losing quality.
- **Guardrails**: in long-running or looping flows, usage monitoring lets you set thresholds and alerts so a runaway task doesn't quietly rack up a large bill.

In practice, each AI task in a Kestra flow can capture usage from the provider's response (for example `usage.total_tokens`), and you can surface those numbers in logs, metrics, or dashboards to keep an eye on spend per run.
