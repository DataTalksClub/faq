---
course: data-engineering-zoomcamp
id: 7bff88dbd7
question: 'Compression Error: zcat output is gibberish, seems like still compressed'
section: 'Module 5: pyspark'
sort_order: 3600
---

In the code along from Video 5.3.3 Alexey downloads the CSV files from the NYT website and gzips them in their bash script. If we now (2023) follow along but download the data from the GH course Repo, it will already be zippes as csv.gz files. Therefore we zip it again if we follow the code from the video exactly. This then leads to gibberish outcome when we then try to cat the contents or count the lines with zcat, because the file is zipped twitch and zcat only unzips it once.

✅solution: do not gzip the files downloaded from the course repo. Just wget them and save them as they are as csv.gz files. Then the zcat command and the showSchema command will also work

URL="${URL_PREFIX}/${TAXI_TYPE}/${TAXI_TYPE}_tripdata_${YEAR}-${FMONTH}.csv.gz"

LOCAL_PREFIX="data/raw/${TAXI_TYPE}/${YEAR}/${FMONTH}"

LOCAL_FILE="${TAXI_TYPE}_tripdata_${YEAR}_${FMONTH}.csv.gz"

LOCAL_PATH="${LOCAL_PREFIX}/${LOCAL_FILE}"

echo "downloading ${URL} to ${LOCAL_PATH}"

mkdir -p ${LOCAL_PREFIX}

wget ${URL} -O ${LOCAL_PATH}

echo "compressing ${LOCAL_PATH}"

# gzip ${LOCAL_PATH} <- uncomment this line

