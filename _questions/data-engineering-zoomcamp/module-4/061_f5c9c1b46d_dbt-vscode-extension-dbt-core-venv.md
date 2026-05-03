---
id: f5c9c1b46d
question: Power user for dbt vscode extension keeps asking to install dbt core even
  though dbt is installed in a virtual environment
sort_order: 61
---

## Problem
Power user for the dbt VS Code extension keeps prompting to install dbt core even though dbt is already installed in your virtual environment.

## Steps to resolve
- Activate your virtual environment:

```
# Unix/macOS
source <path-to-venv>/bin/activate

# Windows
<path-to-venv>\Scripts\activate
```

- In your dbt project folder (the one containing `dbt_project.yml`), run:

```
dbt debug
```

- Copy the Python interpreter path shown by `dbt debug` (the path to the Python executable inside your virtual environment).

- Configure VS Code to use that interpreter:

```
Ctrl/Cmd+Shift+P  ->  Python: Select Interpreter  ->  Enter interpreter path
```

- Paste the copied path and press Enter. Then check the bottom-left corner of VS Code to confirm that dbt core shows with a checkmark, indicating it is using the selected interpreter.

If the prompt persists, ensure there are no conflicting Python environments and consider restarting VS Code.