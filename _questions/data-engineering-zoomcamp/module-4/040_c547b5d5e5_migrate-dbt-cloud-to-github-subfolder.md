---
id: c547b5d5e5
question: How do I migrate from a dbt Cloud managed repository to a GitHub repository?
sort_order: 40
---

1. Save and commit your progress in your dbt projects. This ensures your files are up-to-date before you download them.
2. Go to your profile settings in dbt.
3. Under 'Settings' on the left-hand side, click 'Projects'.
4. Click your project name (e.g., 'taxi_rides_ny').
5. Under 'Repository', click the link (e.g., 'git@github.com:dbt-cloud-managed...').
6. Download the zip file of your repository. Unzip the file, then upload the files/folders for your dbt project to your GitHub repo.
7. After your files are saved in your GitHub repo, go back to the 'Repository details' dbt page. Click 'Disconnect' and 'Confirm Disconnect'. This will remove dbt's managed repo from your project.
8. Follow the instructions on the dbt page to link your GitHub account. You only need to give it access to the repo you are using for this project.
9. The dbt page should prompt you to set up a repo for your project. Connect it to your GitHub repo.
10. After your project is connected to your GitHub repo, go to 'Studio' to view your project. You should see the folders of your GitHub repo.
11. Click 'Initiate project'. This will re-create dbt folders/files in the root (main area) of your repo.

If you want the dbt project to live in a subfolder of your repo (e.g. `Week_4/`), see [the dbt subfolder FAQ](#4f97c0b639).
