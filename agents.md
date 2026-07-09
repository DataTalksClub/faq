use uv for dependency management and running python

periodically commit to git. use double quotes for commit messages, and put the entire message in one line.

## Skills

Skills live in `.claude/skills/` and codify repeatable workflows for this repo:

- **pr** (`.claude/skills/pr/SKILL.md`) — Review and process open FAQ pull requests:
  check section placement, duplicates, sort_order collisions, and content quality, then
  merge or close with the related issue cleaned up.
- **slack-faq-fetch** (`.claude/skills/slack-faq-fetch/SKILL.md`) — Pull recent Slack
  channel discussions for a course into a review export to find missing FAQ entries.
  Run log lives in `.claude/slack-fetch-log.md`.
