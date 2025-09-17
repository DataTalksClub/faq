---
course: data-engineering-zoomcamp
id: dec5edee6a
question: 'Terraform - Error: Failed to query available provider packages │ Could
  not retrieve the list of available versions for provider hashicorp/google: could
  not query │ provider registry for registry.terrafogorm.io/hashicorp/google: the
  request failed after 2 attempts, │ please try again later'
section: 'Module 1: Docker and Terraform'
sort_order: 1610
---

It is an internet connectivity error, terraform is somehow not able to access the online registry. Check your VPN/Firewall settings (or just clear cookies or restart your network). Try terraform init again after this, it should work.

