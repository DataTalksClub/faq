---
id: 092b1efc9e
question: I ran the Agent Relay task flow or integration test successfully, but I
  can’t see the completed task in the dashboard. Was the task deleted?
sort_order: 4
---

Usually, the task was not deleted.

The Agent Relay dashboard is tied to the agent token you enter on the page, and it only shows tasks that were sent or received by that specific agent.

When you run the integration test, it creates new sender and recipient agents. The test output includes a token like `DASHBOARD_SENDER_TOKEN=agt_...`. Copy that sender token into the dashboard (the same token the test printed) and refresh the page—you should then see the task with `completed` status.

If you use a different agent token, the dashboard may look empty even though the task exists in the database.

One exception: the CI workflow uses a temporary PostgreSQL database for its integration test and removes that database during cleanup. As a result, tasks/tokens created by the CI-only test won’t be available after the workflow finishes. If you want to inspect a task in the dashboard after CI/CD deployment, run the integration test against the persistent PostgreSQL database used by Docker Compose or Kubernetes, then use the sender token printed by that test.