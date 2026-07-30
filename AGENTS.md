use uv for dependency management and running python

periodically commit to git. use double quotes for commit messages, and put the entire message in one line.

## Skills

Skills live in `.claude/skills/` and codify repeatable workflows for this repo:

- **add-faq-record** (`.claude/skills/add-faq-record/SKILL.md`) — Add or update one
  FAQ entry from a question, screenshot, chat thread, issue, or other source; check
  placement and duplicates, assign a collision-free filename and sort order, and validate
  the result.
- **clear-backlog** (`.claude/skills/clear-backlog/SKILL.md`) — Clear open FAQ
  pull requests first and then issues, strictly one item at a time. Check placement,
  duplicates, canonical sources, and content quality; get approval for each resolution;
  and add eval coverage only for meaningful agent regressions.
- **slack-faq-fetch** (`.claude/skills/slack-faq-fetch/SKILL.md`) — Pull recent Slack
  channel discussions for a course into a review export to find missing FAQ entries.
  Run log lives in `.claude/slack-fetch-log.md`.
