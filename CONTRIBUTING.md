# Contributing to DataTalks.Club FAQ

Thank you for your interest in contributing to the DataTalks.Club FAQ! This guide will help you understand how to propose new FAQ entries or updates.

## Proposing a New FAQ Entry

We have an automated system that helps maintain the FAQ repository. Here's how to propose a new FAQ entry:

### 1. Create a New Issue

1. Go to the [FAQ Proposal form](https://github.com/DataTalksClub/faq/issues/new?template=faq-proposal.yml)
2. Fill out the form:
   - **Course**: Which course this FAQ is for (e.g., `machine-learning-zoomcamp`)
   - **Question**: The FAQ question
   - **Answer**: A clear, helpful answer with examples if applicable
   - Check the validation boxes

### 2. Automated Processing

Once you submit your issue, our FAQ Bot will automatically:

1. **Analyze your proposal** using AI to compare it with existing FAQs
2. **Make a decision**:
   - **NEW**: Create a new FAQ entry if the question isn't covered
   - **UPDATE**: Update an existing FAQ if your proposal adds valuable context
   - **DUPLICATE**: Mark as duplicate if the question is already fully answered

### 3. What Happens Next

#### For NEW or UPDATE Decisions

- A Pull Request will be automatically created with the proposed changes
- The PR will include:
  - The new or modified FAQ file(s)
  - Explanation of why this action was chosen
  - Section placement and reasoning
- A maintainer will review the PR
- Once approved and merged, your FAQ contribution will be live!
- The originating issue will be automatically closed when the PR is merged

#### For DUPLICATE Decisions

- The bot will comment on your issue with:
  - Explanation of why it's considered a duplicate
  - Link to the existing FAQ that covers your question
  - Link to the source file
- The issue will be automatically closed
- If you believe this is incorrect, you can reopen and mention a maintainer

## Writing Good FAQ Entries

### Question Guidelines

- Be specific and clear
- Use the actual words students might search for
- Start with question words (How, What, When, Why, etc.)
- Examples:
  - ✅ "How do I install Python dependencies using uv?"
  - ❌ "Dependencies"

### Answer Guidelines

- Start with a direct answer
- Include code examples when relevant
- Add links to documentation or resources
- Keep it concise but complete
- Use markdown formatting for readability

**Example:**

### Course
machine-learning-zoomcamp

### Question
How do I run the tests for this project?

### Answer
To run all tests, use:

```bash
make test
```

For unit tests only:

```bash
make test-unit
```

For integration tests only:

```bash
make test-int
```

See the [testing documentation](tests/README.md) for more details.

## Manual Contributions

If you prefer to contribute directly via Pull Request:

1. Fork the repository
2. Create a new branch: `git checkout -b faq/your-topic`
3. Add your FAQ file in the appropriate location:
   - `_questions/{course}/{section}/{NNN}_{id}_{slug}.md`
4. Follow the frontmatter format:

```markdown
---
id: abc123
question: 'Your question here?'
sort_order: 10
---

Your answer content here.
```

5. Update `_questions/{course}/_metadata.yaml` if adding a new section
6. Run tests: `make test`
7. Create a Pull Request

## FAQ File Structure

FAQ files are organized as:

```
_questions/
├── machine-learning-zoomcamp/
│   ├── _metadata.yaml          # Course configuration
│   ├── general/
│   │   ├── 001_abc123_when-does-course-start.md
│   │   └── 002_def456_what-are-prerequisites.md
│   └── module-1/
│       ├── 001_xyz789_install-docker.md
│       └── 002_uvw456_docker-errors.md
└── data-engineering-zoomcamp/
    └── ...
```

### Frontmatter Fields

- **id** (required): Unique 10-character identifier
- **question** (required): The FAQ question
- **sort_order** (required): Integer for ordering within section
- **images** (optional): Array of image objects for embedded images

### Markdown Content

- Write the answer in markdown
- Use code blocks with language specifications
- Include links where helpful
- Keep formatting clean and readable

## Questions or Issues?

If you have questions about contributing or encounter issues with the FAQ Bot:

1. Check existing issues for similar questions
2. Create a new issue with the "question" or "bug" label
3. Tag a maintainer if urgent

Thank you for helping improve the DataTalks.Club FAQ! 🎉
