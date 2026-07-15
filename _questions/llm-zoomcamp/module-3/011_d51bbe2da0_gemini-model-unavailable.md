---
id: d51bbe2da0
question: "Kestra: Gemini model returns 404 or is unavailable. What do I do?"
sort_order: 11
---

Model availability changes over time and can vary by account. If a course workflow returns a `404 NOT_FOUND` saying that its Gemini model is unavailable, replace the model id in the affected YAML file with one currently available to you. For example, in a Kestra flow:

```yaml
provider:
  type: io.kestra.plugin.ai.provider.GoogleGemini
  modelName: gemini-3.5-flash
  apiKey: "{{ secret('GEMINI_API_KEY') }}"
```

In `docker-compose.yml`, update the equivalent `model-name` setting. Then rerun the flow, or restart the Docker Compose services if you changed their configuration.

Check the [official Gemini model list](https://ai.google.dev/gemini-api/docs/models) for current model ids. Do not assume the original model was permanently shut down based on a temporary `404`; select a model that the API makes available to your account.
