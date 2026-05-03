---
id: dec5edee6a
question: 'Terraform: Could not reach provider registry in restricted region (e.g.,
  Iraq) – Invalid provider registry host / Could not query available provider packages'
sort_order: 1
---

This error can occur when Terraform cannot access the online provider registry, which may happen in restricted regions where registry.terraform.io is blocked. The error messages may include things like "Invalid provider registry host" and "Could not query available versions for provider hashicorp/google".

Fix:

- Install and activate a system-wide VPN software (e.g., Proton VPN). Ensure that all traffic from your terminal (where `terraform init` runs) is routed through the VPN.
- Important: A VPN browser extension is usually not sufficient. Extensions proxy traffic only within the web browser and do not affect terminal/VS Code connections.

After the VPN is active, run `terraform init` again to retry fetching provider packages.