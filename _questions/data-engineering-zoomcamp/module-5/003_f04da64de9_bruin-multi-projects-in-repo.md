---
id: f04da64de9
question: Can I have multiple Bruin projects inside the same Git repository?
sort_order: 3
---

Yes, you can have multiple Bruin projects inside the same Git repository. However, bruin init automatically places the **.bruin.yml** config in the Git root, so you need to manually relocate the config file and explicitly tell Bruin where it lives.

Why this happens:
When you run:
```bash
bruin init
```
Bruin detects the nearest `.git` directory in the parent folders and creates the **.bruin.yml** there. So if your repository looks like this:
```bash
repo/
├── .git/
└── data-platforms/
```
the config file will be created in **repo/**, even if you run the command inside **data-platforms/**.