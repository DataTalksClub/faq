---
id: 1be7635aaf
question: "ta-lib won't install on Windows. What works?"
sort_order: 2
---

ta-lib is a C library, so a plain pip install often fails. The easiest options are: install via conda (conda install conda-forge::ta-lib), use the prebuilt wheels from cgohlke/talib-build, or implement the indicator (for example CCI) manually without the library.
