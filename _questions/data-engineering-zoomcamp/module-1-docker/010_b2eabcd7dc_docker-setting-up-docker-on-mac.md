---
id: b2eabcd7dc
question: 'Docker: Setting up Docker on Mac'
sort_order: 10
---

For setting up Docker on macOS, you have two main options:

1. **Download from Docker Website:**
   - Visit the official Docker website and download the Docker Desktop for Mac as a `.dmg` file. This method is generally reliable and avoids issues related to licensing changes.

2. **Using Homebrew:**
   - Be aware that there can be conflicts when installing with Homebrew, especially between Docker Desktop and command-line tools. To avoid issues:
     
     - Install Docker Desktop first.
     - Then install the command line tools.

   - Commands:
     
     ```bash
     brew install --cask docker
     ```
     
     ```bash
     brew install docker docker-compose
     ```

   - For more detailed issues related to `brew install`, refer to this [Issue](https://github.com/Homebrew/brew/issues/16309). 

For more details, you can check the article on [Setting up Docker in macOS](https://medium.com/@vivekslair/setting-up-docker-in-macos-ee36d37b3be2).