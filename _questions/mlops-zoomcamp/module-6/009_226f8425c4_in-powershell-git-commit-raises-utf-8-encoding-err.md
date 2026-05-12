---
id: 226f8425c4
question: In Powershell, Git commit raises utf-8 encoding error after creating pre-commit
  yaml file
sort_order: 9
---

When executing the following command in PowerShell, an error occurs:

```bash
git commit -m 'Updated xxxxxx'
```

The error message is:

```bash
An error has occurred: InvalidConfigError:

==> File .pre-commit-config.yaml

=====> 'utf-8' codec can't decode byte 0xff in position 0: invalid start byte
```

Set UTF-8 encoding when creating the pre-commit YAML file:

```powershell
pre-commit sample-config | out-file .pre-commit-config.yaml -encoding utf8
```