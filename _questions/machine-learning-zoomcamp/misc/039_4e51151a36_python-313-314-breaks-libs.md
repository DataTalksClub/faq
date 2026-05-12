---
id: 4e51151a36
question: Python 3.13 / 3.14 breaks my code (sklearn / numpy / etc.)
sort_order: 39
---

Pin to Python ≤ 3.12 for now. Python 3.13 introduced free-threaded (no-GIL) builds and 3.14 made significant changes that some ML libraries haven't caught up with.

The course officially recommends Python 3.11. If you've already upgraded, the easiest fix is `uv python install 3.11` (or `pyenv install 3.11`) and pin the project to that version.
