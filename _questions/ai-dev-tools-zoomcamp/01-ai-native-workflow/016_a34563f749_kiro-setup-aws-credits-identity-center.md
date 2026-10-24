---
id: a34563f749
question: How do I set up Kiro with my personal AWS account to use my existing AWS
  credits?
sort_order: 16
---

To use eligible AWS credits to pay for Kiro, set up Kiro via your AWS account using AWS Organizations and IAM Identity Center, then subscribe your Kiro organization to your IAM Identity Center user.

1) Set up AWS Organizations + IAM Identity Center
- Sign in to the AWS Management Console.
- In `AWS Organizations`, create/choose an organization.
- In `IAM Identity Center`, enable it and connect it to your AWS Organizations setup if prompted.
- Choose the AWS Region for the IAM Identity Center instance.

2) Create a developer identity
- In IAM Identity Center, create a user using your email address.
- Configure the user’s access to your AWS account.
- Copy your `AWS access portal URL` (useful for signing in).

3) Configure Kiro in the AWS/Kiro flow
- In the AWS Console, search for `Kiro` and open the Kiro console.
- Follow onboarding to enable Kiro with IAM Identity Center.
- Create a Kiro profile and assign a subscription to your IAM Identity Center user.
- Pick the correct subscription plan and complete setup.
- Follow the current steps in the official Kiro enterprise onboarding docs.

4) Sign in to Kiro using organizational access
- Download/open the Kiro IDE.
- If you previously used an individual Kiro account, sign out.
- Choose the organizational sign-in option and authenticate via IAM Identity Center.
- Confirm your organizational subscription is active.

5) Verify your AWS credits are being applied
- Go to AWS Billing and Cost Management and check your available credits/eligibility.
- Review billing reports to confirm Kiro subscription charges are covered by eligible credits.

Note: Creating an AWS organization doesn’t automatically make all AWS credits eligible for Kiro—confirm eligibility for the Kiro subscription charges before relying on credits.