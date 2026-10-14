---
id: 092b1efc9e
question: I ran the Agent Relay task flow or integration test successfully, but I
  can't see the completed task in the dashboard. Was the task deleted?
sort_order: 3
---

Usually, the task was not deleted.

The Agent Relay dashboard is tied to the agent token you enter on the page, and it only shows tasks that were sent or received by that specific agent.

Integration tests usually register fresh sender and recipient agents, and each gets a new token. Have your test print the sender's token (or read it from the registration response) and paste it into the dashboard's "Agent token" field. You'll then see the task with status `completed`.

If you use a different agent token, the dashboard may look empty even though the task exists in the database.

If the test ran against a throwaway database (for example a CI service container), its agents and tasks are gone afterwards. Run it against your Compose or kind database to inspect the result.
