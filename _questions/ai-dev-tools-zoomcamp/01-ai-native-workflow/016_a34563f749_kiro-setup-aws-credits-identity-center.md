---
id: a34563f749
question: How do I set up Kiro with my personal AWS account to use my existing AWS
  credits?
sort_order: 16
---

Subscribe to Kiro through the Kiro console in your AWS account instead of buying an individual Kiro plan. The subscription is then billed to that AWS account, where eligible credits can cover it.

The setup steps change, so follow the official Kiro docs:

- [Subscribe your team](https://kiro.dev/docs/enterprise/subscribe/): set up IAM Identity Center, create the Kiro profile, and assign a subscription tier to your user.
- [Connect IAM Identity Center](https://kiro.dev/docs/enterprise/identity-provider/iam-identity-center/): requirements for the Identity Center instance.
- [Enterprise billing](https://kiro.dev/docs/enterprise/billing/): tiers and how charges are billed.

If you already have a paid individual Kiro account, cancel it and sign out of Kiro. Then sign back in with your IAM Identity Center user. Check Billing and Cost Management > Credits to confirm that your credits apply to Kiro charges.
