# DataTalks.Club FAQ

A static site generator for DataTalks.Club course FAQs with automated AI-powered FAQ maintenance.

## Features

- **Static Site Generation**: Converts markdown FAQs to a beautiful, searchable HTML site
- **Automated FAQ Management**: AI-powered bot that processes new FAQ proposals
- **Intelligent Triage**: Automatically determines if proposals should create new entries, update existing ones, or are duplicates
- **GitHub Integration**: Seamless workflow via GitHub Issues and Pull Requests

## Project Structure

```
datatalksclub-faq/
├── _questions/              # FAQ content organized by course
│   ├── machine-learning-zoomcamp/
│   │   ├── _metadata.yaml   # Course configuration
│   │   ├── general/         # General course questions
│   │   ├── module-1/        # Module-specific questions
│   │   └── ...
│   ├── data-engineering-zoomcamp/
│   └── ...
├── _layouts/                # Jinja2 HTML templates
│   ├── base.html
│   ├── course.html
│   └── index.html
├── assets/                  # CSS and static assets
├── faq_automation/          # FAQ automation module
│   ├── core.py             # Core FAQ processing functions
│   ├── rag_agent.py        # AI-powered decision agent
│   ├── actions.py          # GitHub Actions integration
│   └── cli.py              # Command-line interface
├── tests/                   # Test suite
├── generate_website.py      # Main site generator
└── Makefile                # Build commands
```

## Contributing FAQ Entries

We welcome FAQ contributions! There are two ways to contribute:

### 1. Automated (Recommended)

Simply [create a new issue](https://github.com/DataTalksClub/faq/issues/new?template=faq-proposal.yml) using the "FAQ Proposal" template. Our FAQ Bot will:

1. Analyze your proposal against existing FAQs
2. Decide the best action (NEW, UPDATE, or DUPLICATE)
3. Either create a PR with your changes or provide feedback

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed instructions.

### 2. Manual Pull Request

1. Fork this repository
2. Add/modify FAQ files in `_questions/{course}/{section}/`
3. Follow the frontmatter format (see below)
4. Create a Pull Request

## FAQ File Format

Each FAQ entry is a markdown file with YAML frontmatter:

```markdown
---
id: abc1234567
question: 'How do I install the dependencies?'
sort_order: 10
---

Your answer content here.
```

### Frontmatter Fields

- **id**: Unique 10-character identifier (auto-generated)
- **question**: The FAQ question text
- **sort_order**: Integer controlling order within section
- **images** (optional): Array of image metadata for embedded images

## FAQ Automation

The FAQ automation system uses:

- **minsearch**: Lightweight text search to find similar existing FAQs
- **OpenAI GPT-5**: LLM-based decision making for triage
- **Pydantic**: Structured output validation
- **GitHub Actions**: Automated workflow orchestration

### How It Works

1. **Proposal Submission**: User creates GitHub issue with FAQ proposal
2. **Retrieval**: System searches existing FAQs for similar content
3. **LLM Analysis**: GPT-5 analyzes proposal + search results and decides:
   - **NEW**: Question not covered → create new FAQ file
   - **UPDATE**: Adds valuable context → merge with existing FAQ
   - **DUPLICATE**: Already fully answered → close with explanation
4. **Action Execution**:
   - NEW/UPDATE: Create PR with file changes (issue auto-closes when PR is merged)
   - DUPLICATE: Comment on issue and close immediately

### Configuration

The workflow requires:

- **OPENAI_API_KEY**: Set as repository secret for GitHub Actions
- **GitHub permissions**: `contents: write`, `issues: write`, `pull-requests: write`

## Development

### Setup

```bash
# Install dependencies
uv sync --dev
```

For testing the FAQ automation locally, you'll need to set your OpenAI API key:

```bash
export OPENAI_API_KEY='your-api-key-here'
```

Or add it to your shell configuration file (e.g., `~/.bashrc`, `~/.zshrc`).

### Running Locally

To test the FAQ automation locally, create a `test_issue.txt` file:

```bash
cat > test_issue.txt << 'EOF'
### Course
machine-learning-zoomcamp

### Question
How do I check my Python version?

### Answer
Run `python --version` in your terminal.
EOF
```

Then process the FAQ proposal:

```bash
uv run python -m faq_automation.cli \
  --issue-body "$(cat test_issue.txt)" \
  --issue-number 42
```

### Testing

```bash
# Generate static website
make website

# Run all tests
make test

# Run unit tests only
make test-unit

# Run integration tests only
make test-int
```

See [testing documentation](tests/README.md) for detailed information about the test suite, including how to run specific test files or methods, test coverage details, and guidelines for adding new tests.

## Architecture

### Site Generation Pipeline

1. **Collection** (`collect_questions()`):
   - Reads all markdown files from `_questions/`
   - Parses YAML frontmatter
   - Loads course metadata for section ordering

2. **Processing** (`process_markdown()`):
   - Converts markdown to HTML
   - Applies syntax highlighting (Pygments)
   - Auto-links plain text URLs
   - Handles image placeholders

3. **Sorting** (`sort_sections_and_questions()`):
   - Orders sections per `_metadata.yaml`
   - Sorts questions by `sort_order` field

4. **Rendering** (`generate_site()`):
   - Applies Jinja2 templates
   - Generates course pages and index
   - Copies assets to `_site/`

### FAQ Automation Pipeline

1. **Issue Parsing**: Extract question/answer from GitHub issue
2. **Index Building**: Create search index from existing FAQs
3. **Retrieval**: Find top 5 similar FAQs
4. **LLM Decision**: GPT-5 analyzes and decides action
5. **Execution**: Create PR or comment based on decision

## Dependencies

### Core
- **jinja2**: Template rendering
- **mistune**: Markdown parsing
- **pygments**: Syntax highlighting
- **pyyaml**: YAML parsing

### Automation
- **minsearch**: FAQ search/retrieval
- **openai**: LLM integration
- **pydantic**: Data validation

### Development
- **pytest**: Testing framework

## License

[Add license information]

## Support

- **Issues**: Report bugs or request features via [GitHub Issues](https://github.com/DataTalksClub/faq/issues)
- **Contributing**: See [CONTRIBUTING.md](CONTRIBUTING.md)

## Acknowledgments

Built with ❤️ for the DataTalks.Club community.
