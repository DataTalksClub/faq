---
id: 31053272e0
question: 'Terraform: Error: Post "[storage.googleapis.com](https://storage.googleapis.com/storage/v1/b?alt=json&prettyPrint=false&project=coherent-ascent-379901):
  oauth2: cannot fetch token: Post "[oauth2.googleapis.com](https://oauth2.googleapis.com/token):
  dial tcp 172.217.163.42:443: i/o timeout'
sort_order: 2
---

The issue was related to network restrictions, as Google is not accessible in my country. I used a VPN and discovered that the terminal program does not automatically follow the system proxy, requiring separate proxy configuration settings.

**Solution:**

1. Open an Enhanced Mode in your VPN application, such as Clash.
2. Run `terraform apply` again.

If you encounter this issue, consult your VPN provider for assistance with configuration.