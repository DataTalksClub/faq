---
course: data-engineering-zoomcamp
id: 6c9785b291
question: Orchestrating dbt cloud with Mage
section: Project
sort_order: 4270
---

You can trigger your dbt job in Mage pipeline. For this get your dbt cloud api key under settings/Api tokens/personal tokens. Add it safely to  your .env

For example

dbt_api_trigger=dbt_**

Navigate to job page and find api trigger  link

Then create a custom mage Python block with a simple http request like

![Image](images/data-engineering-zoomcamp/image_981381c8.png)

![Image](images/data-engineering-zoomcamp/image_ebc771b3.png)

from dotenv import load_dotenv
from pathlib import Path
dotenv_path = Path('/home/src/.env')
load_dotenv(dotenv_path=dotenv_path)
dbt_api_trigger= os.getenv(dbt_api_trigger)

url = f"https://cloud.getdbt.com/api/v2/accounts/{dbt_account_id}/jobs/<job_id>/run/"

headers = {
        "Authorization": f"Token {dbt_api_trigger}",
        "Content-Type": "application/json" }

body = {
        "cause": "Triggered via API"
    }
    response = requests.post(url, headers=headers, json=body)

voila! You triggered dbt job form your mage pipeline.

