---
id: a5a8a6ac39
question: Setting JAVA_HOME with Homebrew on Apple Silicon (M1/M2/M3 Macs)
sort_order: 25
---

Apple Silicon Macs install Homebrew under `/opt/homebrew/` instead of `/usr/local/`. Generic instructions written for Intel Macs won't find the JDK. Set `JAVA_HOME` explicitly in `~/.zshrc` (or `~/.bashrc`):

```bash
brew install openjdk@17

export JAVA_HOME="/opt/homebrew/opt/openjdk@17"
export PATH="${JAVA_HOME}/bin:${PATH}"
```

Reload your shell (`source ~/.zshrc` or open a new terminal) and verify:

```bash
which java
java --version
```

`which java` should print a path under `/opt/homebrew/...` and `java --version` should show JDK 17.

Spark 4.x supports Java 17 and 21; pick whichever is available via Homebrew (`brew install openjdk@21` works the same way).
