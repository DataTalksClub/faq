---
id: a83f047f52
question: How to troubleshoot issues and ask good questions
sort_order: 6
---

## Try to solve it yourself first

- Read the error message carefully — it usually includes a line number, a stack trace, and a description of what went wrong.
- Search the message: copy the most specific part of the error (not the whole stack trace) into Google. The format `<tool> <error message>` works well, e.g. `pgcli error column c.relhasoids does not exist`.
- Check the official documentation of the tool you're using.
- Use Ctrl+F in this FAQ and in Slack channel pinned messages.
- Restart the process / container / shell / VM and try once more — many transient errors resolve this way.
- If you suspect the install is broken, uninstall first, then reinstall. Reinstalling on top of a broken install rarely helps.

## Asking for help in Slack / forums

When the troubleshooting steps don't help and you need another pair of eyes, include enough info that someone can actually help without going back and forth:

- Operating system and version (e.g. Windows 11 + WSL Ubuntu 24.04, Mac M2, Linux Ubuntu 22.04).
- Which lesson / video you're following, and which command failed.
- The exact command and the exact error — paste both as text inside triple-backtick code blocks. Don't paste screenshots of text.
- What you've already tried. If you skip this, helpers' first suggestions will be the things you already tried.
- Stay in one thread. Reply to your own question; don't open a new post for a follow-up.

If the same problem recurs, post in the same thread with what changed in your environment since last time.

## Help others by contributing back

If your problem isn't yet covered in this FAQ, consider [opening a PR](https://github.com/DataTalksClub/faq) so the next student doesn't have to debug it from scratch.
