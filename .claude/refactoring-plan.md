# Refactoring Plan: Separate Independent Projects

## Current State Analysis

The repository has **NO shared code** between components:

| Component | Dependencies | Purpose |
|-----------|--------------|---------|
| **Website Generator** (`generate_website.py`) | jinja2, mistune, pygments, python-docx, pyyaml, requests | Reads FAQ `.md` files → generates HTML website |
| **FAQ Automation** (`faq_automation/`) | minsearch, openai, pydantic, pyyaml | Reads GitHub issues → creates FAQ `.md` files |

**No code imports between them.** They are completely independent.

---

## Proposed Structure

```
faq/
├── _questions/                    # FAQ content (shared data)
├── _layouts/                      # Website layouts (shared)
├── assets/                        # Website assets (shared)
├── images/                        # Website images (shared)
│
├── website/                       # Website generator project
│   ├── generate_website.py        # Main script
│   ├── pyproject.toml             # Website dependencies
│   ├── pyproject.lock
│   ├── tests/                     # Unit tests
│   │   ├── test_frontmatter.py
│   │   ├── test_url_conversion.py
│   │   ├── test_markdown.py
│   │   ├── test_renderer.py
│   │   ├── test_course_processing.py
│   │   ├── test_jinja_setup.py
│   │   └── test_sorting.py
│   └── tests_integration/         # Integration tests
│       ├── test_site_generation.py
│       └── test_real_world.py
│
└── faq_automation/                # FAQ automation project
    ├── __init__.py
    ├── core.py
    ├── rag_agent.py
    ├── actions.py
    ├── cli.py
    ├── github_actions.py
    ├── pyproject.toml             # FAQ dependencies
    ├── pyproject.lock
    ├── tests/                     # Unit tests
    │   ├── test_faq_automation.py
    │   ├── test_cli_parsing.py
    │   ├── test_faq_actions.py
    │   └── test_github_actions.py
    └── tests_integration/         # Integration tests
        └── test_faq_automation_workflow.py
```

---

## Step-by-Step Implementation

### Step 1: Create `website/` project

```bash
mkdir -p website/tests website/tests_integration

# Move generate_website.py
mv generate_website.py website/

cat > website/pyproject.toml << 'EOF'
[project]
name = "website-generator"
version = "0.1.0"
requires-python = ">=3.13"
dependencies = [
    "jinja2>=3.1.6",
    "mistune>=3.0.0",
    "pygments>=2.19.2",
    "python-docx>=1.2.0",
    "pyyaml>=6.0.2",
    "requests>=2.32.5",
]

[dependency-groups]
dev = [
    "pytest>=8.4.2",
]

[tool.pytest.ini_options]
testpaths = ["tests", "tests_integration"]
python_files = ["test_*.py"]
python_classes = ["Test*"]
python_functions = ["test_*"]
addopts = "-v --tb=short"
markers = [
    "integration: Integration tests that build the full site"
]
EOF

cd website && uv lock && cd ..
```

### Step 2: Restructure `faq_automation/` as a complete project

```bash
mkdir -p faq_automation/tests faq_automation/tests_integration

# Move tests into faq_automation
mv tests/unit/test_faq_automation.py faq_automation/tests/
mv tests/unit/test_cli_parsing.py faq_automation/tests/
mv tests/unit/test_faq_actions.py faq_automation/tests/
mv tests/unit/test_github_actions.py faq_automation/tests/
mv tests/integration/test_faq_automation_workflow.py faq_automation/tests_integration/

cat > faq_automation/pyproject.toml << 'EOF'
[project]
name = "faq-automation"
version = "0.1.0"
requires-python = ">=3.13"
dependencies = [
    "minsearch>=0.0.7",
    "openai>=1.0.0",
    "pydantic>=2.0.0",
    "pyyaml>=6.0.2",
]

[dependency-groups]
dev = [
    "pytest>=8.4.2",
    "pytest-mock>=3.10.0",
]

[tool.pytest.ini_options]
testpaths = ["tests", "tests_integration"]
python_files = ["test_*.py"]
python_classes = ["Test*"]
python_functions = ["test_*"]
addopts = "-v --tb=short"
markers = [
    "integration: Integration tests for FAQ workflows"
]

[project.scripts]
faq-bot = "faq_automation.cli:main"
EOF

cd faq_automation && uv lock && cd ..
```

### Step 3: Move remaining tests to `website/`

```bash
mv tests/unit/test_frontmatter.py website/tests/
mv tests/unit/test_url_conversion.py website/tests/
mv tests/unit/test_markdown.py website/tests/
mv tests/unit/test_renderer.py website/tests/
mv tests/unit/test_course_processing.py website/tests/
mv tests/unit/test_jinja_setup.py website/tests/
mv tests/unit/test_sorting.py website/tests/
mv tests/integration/test_site_generation.py website/tests_integration/
mv tests/integration/test_real_world.py website/tests_integration/
```

### Step 4: Create conftest.py files

```bash
# website/tests/conftest.py
cat > website/tests/conftest.py << 'EOF'
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
EOF

cp website/tests/conftest.py website/tests_integration/conftest.py

# faq_automation/tests/conftest.py
cat > faq_automation/tests/conftest.py << 'EOF'
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
EOF

cp faq_automation/tests/conftest.py faq_automation/tests_integration/conftest.py
```

### Step 5: Clean up

```bash
rm -rf tests/
rm utils/  # These are old scripts, no longer needed
```

### Step 6: Update Makefile

```makefile
.PHONY: test test-website test-faq-automation

test-website:
	cd website && uv run pytest tests/ tests_integration/ -v

test-faq-automation:
	cd faq_automation && uv run pytest tests/ tests_integration/ -v

test: test-website test-faq-automation
```

### Step 7: Create convenience scripts

```bash
# website/test.sh
cat > website/test.sh << 'EOF'
#!/bin/bash
cd "$(dirname "$0")"
uv run pytest tests/ tests_integration/ -v "$@"
EOF

# faq_automation/test.sh
cat > faq_automation/test.sh << 'EOF'
#!/bin/bash
cd "$(dirname "$0")"
uv run pytest tests/ tests_integration/ -v "$@"
EOF

chmod +x website/test.sh faq_automation/test.sh
```

### Step 8: Update root README.md

Update to reflect new structure:
```bash
# Run website generator
cd website && uv run python generate_website.py

# Run FAQ bot
cd faq_automation && uv run faq-bot --issue-body "$(cat issue.txt)"

# Run tests
cd website && uv run pytest
cd faq_automation && uv run pytest
```

---

## Migration Checklist

- [ ] Create `website/` directory with `pyproject.toml`
- [ ] Move `generate_website.py` to `website/`
- [ ] Add `pyproject.toml` to `faq_automation/`
- [ ] Run `uv lock` in both projects
- [ ] Move website tests to `website/tests/` and `website/tests_integration/`
- [ ] Move FAQ tests to `faq_automation/tests/` and `faq_automation/tests_integration/`
- [ ] Create `conftest.py` files
- [ ] Delete old `tests/`, `utils/` directories
- [ ] Update Makefile
- [ ] Update CI/CD workflows
- [ ] Update documentation
- [ ] Run all tests to verify

---

## Test Categorization

### Website (`website/`)
| Type | Files |
|------|-------|
| **Unit** (`tests/`) | frontmatter, url_conversion, markdown, renderer, course_processing, jinja_setup, sorting |
| **Integration** (`tests_integration/`) | site_generation, real_world |

### FAQ Automation (`faq_automation/`)
| Type | Files |
|------|-------|
| **Unit** (`tests/`) | faq_automation, cli_parsing, faq_actions, github_actions |
| **Integration** (`tests_integration/`) | faq_automation_workflow |
