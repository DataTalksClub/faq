---
id: 334ace3d48
question: "OpenAI Codex models (e.g. gpt-5.1-codex) time out or can't be selected. Why?"
sort_order: 4
---

Your AI coding front-end has to support OpenAI's Responses API. Non-codex models work over the older API, but the codex models need the Responses API - if the client doesn't speak it, you get timeouts. This is the same integration Alexey covers in the "Building a Lovable Clone" material.
