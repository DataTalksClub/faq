---
id: a5a8a6ac39
question: Setting JAVA_HOME with Homebrew on Apple Silicon
sort_order: 59
---

The MacOS setup instruction ([here](https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/05-batch/setup/macos.md#installing-java)) for setting the `JAVA_HOME` environment variable is for Intel-based Macs, which have a default install location at `/usr/local/`. If you have an Apple Silicon Mac, you need to set `JAVA_HOME` to `/opt/homebrew/`. Update your `.bashrc` or `.zshrc` file with the following:

```bash
export JAVA_HOME="/opt/homebrew/opt/openjdk/bin"
export PATH="$JAVA_HOME:$PATH"
```

Confirm that your path was correctly set by running the command:

```bash
which java
```

You should expect to see the output:

```
/opt/homebrew/opt/openjdk/bin/java
```

Check the Java version with the following command:

```bash
java -version
```

Reference: [https://docs.brew.sh/Installation](https://docs.brew.sh/Installation)