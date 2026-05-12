---
id: af5f29b64f
question: AWS EC2 instance constantly drops SSH connection
sort_order: 15
---

My SSH connection to AWS cannot last more than a few minutes, whether via terminal or VS Code.

My config:

```bash
Host mlops-zoomcamp  # ssh connection calling name
User ubuntu  # username AWS EC2
HostName <instance-public-IPv4-addr>  # Public IP, changes when instance is turned off.
IdentityFile ~/.ssh/name-of-your-private-key-file.pem  # Private SSH key file path
LocalForward 8888 localhost:8888  # Connecting to internal service
StrictHostKeyChecking no
```

The disconnection occurs whether I SSH via WSL2 or via VS Code, often after running some code like `import mlflow`.

To reconnect, I need to stop and restart the instance, which assigns a new IPv4 address.

I've checked the steps at AWS's troubleshooting page: [AWS SSH Connection Errors](https://aws.amazon.com/premiumsupport/knowledge-center/ec2-linux-resolve-ssh-connection-errors/)

Inbound rule should allow all IPs for SSH.

**Expected Behavior:**

- SSH connection should remain active while using the instance.
- Should be able to reconnect if disconnected.

- **Memory Issue**: Disconnections may occur if the instance runs out of memory. Use EC2's screenshot feature to troubleshoot. If it's an OS out-of-memory issue, consider:
  - Using a higher compute VM with more RAM.
  - Adding a swap file, which uses disk as a RAM substitute to prevent OOM errors.
  - Follow Ubuntu's documentation: [Ubuntu Swap FAQ](https://help.ubuntu.com/community/SwapFaq).
  - Alternatively, follow AWS documentation: [AWS Swap File](https://aws.amazon.com/premiumsupport/knowledge-center/ec2-memory-swap-file/).

- **Timeout Issue**: If connections drop due to timeouts, add the following to your local `.ssh/config` file to ping every 50 seconds:

  ```bash
  ServerAliveInterval 50
  ```