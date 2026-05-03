---
id: bc90da941d
question: 'GCP: The project to be billed is associated with an absent billing account'
sort_order: 4
---

If you receive the error:

```
Error 403: The project to be billed is associated with an absent billing account., accountDisabled
```

It is most likely because you did not enter your project ID correctly. The value you enter should be unique to your project. You can find this value on your GCP Dashboard when you log in.

Another possibility is that you have not linked your billing account to your current project.