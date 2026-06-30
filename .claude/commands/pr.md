---
description: Review and process open FAQ PRs
---

Go through all open pull requests one by one. For each PR:

## 1. Show Details
- PR number and title
- Course and section (from PR body)
- Related issue number
- **ALWAYS check sort_order**: List files in target section (`ls _questions/<course>/<section>/`) to find highest number, verify PR uses next sequential
- Full diff (use `gh pr diff <number>`)

## 2. Check Against These Rules

### Section Placement
- **Kestra questions** → must be in `module-2` (workflow orchestration), NOT `general` or `module-1`
- **Docker + Kestra** → still `module-2` (Kestra is primary topic)
- **Docker-only** (pgAdmin, Postgres, etc.) → `module-1`

### Relevance (Close If)
- Basic Linux/SQL tutorials (vim installation, SQL JOIN concepts, etc.)
- Generic programming not tied to course content
- Already exists in DE zoomcamp when proposed for ML zoomcamp

### Duplicates (Check Before Creating)
- Search existing FAQs: `grep -r "keyword" _questions/`
- Same content should NOT exist in both DE and ML zoomcamp
- Enhance existing entries instead of duplicating

### Code Quality (Fix Before Merge)
- Python code must have proper indentation
- Check for file corruption (garbage characters at end)
- Code blocks should be syntactically correct

## 3. Ask User
After showing each PR, ask: "Merge, close, or needs changes?"

## 4. Actions
- **Merge**: `gh pr merge <number> --delete-branch --squash --subject "..." --body "..."`
  - The PR body's `Closes #<issue>` auto-closes the related issue on merge — no manual step needed.
- **Close**: put the reasoning on the **issue**, not the PR, since closing a PR (unlike merging) does NOT auto-close its linked issue. Steps:
  1. `gh issue comment <issue> --body "reason..."` — explain why, grounded in the course material.
  2. `gh issue close <issue> --reason "not planned"`
  3. `gh pr close <number>` — close the PR with no comment (or a one-line pointer to the issue).
- **Move section**: Checkout branch, `git mv` file, update sort_order, push, then merge
- **Fix content**: Checkout branch, edit file, commit, push, then merge

## 5. Sort Order Guidelines
- Find highest number in target section: `ls _questions/<course>/<section>/`
- Use next sequential number as sort_order

Get open PRs with:
`gh pr list --state open --json number,title,body,headRefName,baseRefName,url`
