---
id: a4adc70f41
question: Why is token usage monitored in Kestra workflows?
sort_order: 5
---

Token usage monitoring in Kestra workflows helps you understand and control the cost and efficiency of LLM-based tasks run in production. The main reasons are:

- Cost awareness: token usage is directly tied to costs charged by LLM providers. Tracking usage lets you budget, forecast, and detect cost anomalies early.
- Prompt optimization and lean outputs: by measuring how many tokens are consumed for prompts and generated outputs, you can iteratively improve prompts to be more concise and reduce unnecessary output without sacrificing quality.
- Production guardrails: monitoring usage enables setting thresholds and alerts if token consumption spikes, helping prevent runaway costs in long-running or looping flows.

How to apply:

- Instrument each LLM call in Kestra tasks to capture usage metrics from the provider's response, such as input_tokens, prompt_tokens, and total_tokens.
- Aggregate these metrics per run and per flow, and push them to your monitoring or observability stack (logs, metrics, dashboards).
- Review token budgets and flow designs regularly to identify optimization opportunities and enforce cost controls.