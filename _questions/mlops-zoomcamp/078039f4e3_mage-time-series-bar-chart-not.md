---
course: mlops-zoomcamp
id: 078039f4e3
question: Mage Time Series Bar Chart Not Showing
section: 'Module 3: Orchestration'
sort_order: 1350
---

import requests

from io import BytesIO

from typing import List

import numpy as np

import pandas as pd

if 'data_loader' not in globals():

from mage_ai.data_preparation.decorators import data_loader

@data_loader

def ingest_files(**kwargs) -> pd.DataFrame:

dfs: List[pd.DataFrame] = []

for year, months in [(2024, (1, 3))]:

for i in range(*months):

response = requests.get(

'https://github.com/mage-ai/datasets/raw/master/taxi/green'f'/{year}/{i:02d}.parquet'

)

if response.status_code != 200:

raise Exception(response.text)

df = pd.read_parquet(BytesIO(response.content))

# if time series chart on mage error, add code below

df['lpep_pickup_datetime_cleaned'] = df['lpep_pickup_datetime'].astype(np.int64) // 10**9

dfs.append(df)

return pd.concat(dfs)

Added by Rohmat S

