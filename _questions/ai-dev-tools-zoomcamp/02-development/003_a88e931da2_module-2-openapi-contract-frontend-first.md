---
id: a88e931da2
question: 'Module 2: Why define an OpenAPI contract from the frontend service layer
  before implementing the FastAPI backend?'
sort_order: 3
---

The OpenAPI contract is the explicit agreement between the frontend and the FastAPI backend.

If you build the frontend first and put all backend calls behind a centralized frontend service layer, you already know the exact API requirements: which endpoints exist, which HTTP methods they use, what request/response bodies look like, and what authentication is required. Generating `openapi.yaml` from that service layer gives the backend a precise target to implement, instead of requiring the backend (or coding agent) to infer the API by reading frontend code.

This workflow lets both sides be developed independently while keeping a stable interface: the frontend can use mocked service calls early, and the backend can be implemented against the contract. It also reduces ambiguity and helps catch mismatches before the real backend is connected.

A typical sequence in Module 2 is:
1) Build the interactive frontend with mocked backend calls.
2) Centralize backend calls in the frontend service layer.
3) Generate the OpenAPI contract from that service layer.
4) Implement the FastAPI backend against the contract.
5) Swap the mocked service with a real backend client.

So the contract isn’t just documentation—it’s the shared interface that prevents both teams (or agents) from having to guess each other’s expectations.