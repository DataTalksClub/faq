---
id: ac62d9ccf0
question: Getting a syntax error while trying to get the password from aws-cli
sort_order: 4
---

The command `aws ecr get-login --no-include-email` returns an invalid choice error:

```
Invalid choice error
```

The solution is to use the following command instead:

```bash
aws ecr get-login-password
```

To simplify the login process, replace `<ACCOUNT_NUMBER>` and `<REGION>` with your values:

```bash
export PASSWORD=`aws ecr get-login-password`

docker login -u AWS -p $PASSWORD <ACCOUNT_NUMBER>.dkr.ecr.<REGION>.amazonaws.com/clothing-tflite-images
```