---
id: 27b149393b
question: Can I use Streamlit alone as the deployment for my project?
sort_order: 15
---

No. Streamlit is a UI framework, not a model-serving framework. The deployment criterion requires a service (Flask/FastAPI) wrapped in Docker, optionally on Kubernetes or a cloud platform.

Streamlit can be a nice optional UI layer on top of your service, but it doesn't satisfy the deployment requirement on its own.
