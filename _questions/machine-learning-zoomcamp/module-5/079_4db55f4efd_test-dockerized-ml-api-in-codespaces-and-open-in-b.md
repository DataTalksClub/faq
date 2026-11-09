---
id: 4db55f4efd
question: How can I test a Dockerized ML prediction API in GitHub Codespaces and open
  it in my browser?
sort_order: 79
---

To test a Dockerized ML prediction API in GitHub Codespaces and reach it from your browser, you need to (1) run the container with the app port published and (2) use the Codespaces “forwarded port” URL (not `localhost`) in your browser.

1) Build the Docker image
Run this in the Codespaces terminal from your project directory:
```bash
docker build -t my-ml-api .
```

2) Run the container and publish the API port
If your API listens on port `9696`, run:
```bash
docker run -d --name ml-api -p 9696:9696 my-ml-api
```
Replace `9696` if your app uses a different port.

3) Confirm the container is running
```bash
docker ps
```

4) (Optional) Verify from the terminal using a health endpoint
If you have something like `/healthz`, check:
```bash
curl http://localhost:9696/healthz
```

5) Open it in your browser via Codespaces forwarded ports
- In Codespaces, open the “Ports” tab.
- Find the forwarded port (e.g., `9696`).
- Click the forwarded address/link to open it in the browser.

Important: `localhost` in your browser is your *local computer*, not the Codespace. Use the forwarded port URL provided by Codespaces.

6) Troubleshooting
- Check container logs:
```bash
docker logs ml-api
```
- Make sure your app listens on `0.0.0.0` inside the container (binding to `127.0.0.1` can make the forwarded port unreachable).