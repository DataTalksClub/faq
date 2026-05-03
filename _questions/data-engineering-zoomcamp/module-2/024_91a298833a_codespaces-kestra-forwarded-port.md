---
id: 91a298833a
question: 'GitHub Codespaces: ERR_EMPTY_RESPONSE when accessing Kestra in Docker (this
  page isn’t working / 127.0.0.1 didn’t send any data)'
sort_order: 24
---

In Codespaces, localhost in your browser does not point to the Docker container. Kestra may be running correctly inside Docker, but you must access it through the forwarded port URL, not http://localhost:8080.

What to do:
- Open the Codespaces UI and go to the Ports (forwarded ports) section.
- Ensure port 8080 (or the port Kestra is listening on) is forwarded.
- Copy the forwarded URL for port 8080. It will look like a Codespaces-provided URL (not http://localhost:8080).
- In your browser, navigate to that forwarded URL instead of http://localhost:8080.

If you still see ERR_EMPTY_RESPONSE:
- Check that the Kestra container is actually running and that Kestra is listening on the configured port.
- Check the container logs for errors.
- If necessary, restart the Kestra container.

Notes:
- The forwarded URL is provided by Codespaces in the Ports panel.
- Once you access via the forwarded URL, you should be able to reach Kestra as normal.