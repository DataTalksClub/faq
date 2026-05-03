---
id: c547b5d5e5
question: How do I migrate from a dbt Cloud managed repository to a GitHub repository
  (and can I use a subfolder in my GitHub repo for the dbt project)?
sort_order: 40
---

Steps to migrate from a dbt Cloud managed repository to a GitHub repository:

1. Save and commit your progress in your dbt projects. This ensures your files are up-to-date before you download them.
2. Go to your profile settings in dbt.
3. Under 'Settings' on the left-hand side, click 'Projects'.
4. Click your project name (e.g., 'taxi_rides_ny').
5. Under 'Repository', click the link (e.g., 'git@github.com:dbt-cloud-managed...').
6. Download the zip file of your repository (see instructions here). Unzip the file, then upload the files/folders for your dbt project in your Github repo.
7. After your files are saved in your Github repo, go back to the 'Repository details' dbt page. Click 'Disconnect' and 'Confirm Disconnect'. This will remove dbt's managed repo from your project.
8. Follow the instructions on the dbt page to link your Github account. You only need to give it access to the repo you are using for this project.
9. The dbt page should prompt you to setup a repo for your project. Connect it to your GitHub repo.
10. After your project is connected to your GitHub repo, go to 'Studio' to view your project. You should see the folders of your GitHub repo.
11. Click 'Initiate project'. This will re-create dbt folders/files in the root (main area) of your repo.

If you want to work out of a subfolder of your repo for the dbt project, follow the following instructions. Please note that this is my best guess and is what has worked for me so far...

(For example, I want all my dbt files in the "Week_4" folder of my "DEZoomcamp" repo.)

1. KEEP the 'dbt_project.yml' file in the root of your repo. Go into the file and change the paths to include your subfolder. For example, I added "Week_4/" to the paths below.

```yaml
# These configurations specify where dbt should look for different types of files.
# The `model-paths` config, for example, states that models in this project can be
# found in the "models/" directory. You probably won't need to change these!
model-paths: ["Week_4/models"]
analysis-paths: ["Week_4/analyses"]
test-paths: ["Week_4/tests"]
seed-paths: ["Week_4/seeds"]
macro-paths: ["Week_4/macros"]
snapshot-paths: ["Week_4/snapshots"]
target-path: "Week_4/target"  # directory which will store compiled SQL files
clean-targets:                # directories to be removed by `dbt clean`
- "Week_4/target"
- "Week_4/dbt_packages"
```
2. Save your 'dbt_project.yml' file.
3. Check the .gitignore file in the root of your repo. If it includes changes to account for dbt files, review and save the changes.
4. Delete the duplicative files/folders that dbt created in the root of your repo. You shouldn't need these because you are using the dbt files/folders you already saved in your subfolder. (Note: The 'target' folder might re-appear when you begin to run dbt commands. This is okay -- just keep it.)
5. If you copied an older version of the 'dbt_project.yml' file in your subfolder, delete it. (Make sure you are NOT deleting the version you just updated in the root of your repo.) _This is just to ensure you don't accidentally update the copy in the subfolder, which is not used by dbt._
6. Test run your dbt files from the subfolder to confirm everything works.
