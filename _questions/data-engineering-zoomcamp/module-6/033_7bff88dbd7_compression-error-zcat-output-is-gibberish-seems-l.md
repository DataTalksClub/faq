---
id: 7bff88dbd7
question: 'Compression Error: zcat output is gibberish, seems like still compressed'
sort_order: 33
---

In the code along from Video 5.3.3, Alexey downloads the CSV files from the NYT website and gzips them in their bash script. Currently (2023), if we download the data from the GH course repo, it is already zipped as `csv.gz` files. Following the video exactly would zip them again, leading to gibberish output when using `zcat`, as it only unzips the file once.

**Solution:** Do not gzip the files downloaded from the course repo. Simply use `wget` to download and save them as `csv.gz` files. Then the `zcat` command and the `showSchema` command will work correctly.

```bash
URL="${URL_PREFIX}/${TAXI_TYPE}/${TAXI_TYPE}_tripdata_${YEAR}-${FMONTH}.csv.gz"

LOCAL_PREFIX="data/raw/${TAXI_TYPE}/${YEAR}/${FMONTH}"

LOCAL_FILE="${TAXI_TYPE}_tripdata_${YEAR}_${FMONTH}.csv.gz"

LOCAL_PATH="${LOCAL_PREFIX}/${LOCAL_FILE}"

echo "downloading ${URL} to ${LOCAL_PATH}"

mkdir -p ${LOCAL_PREFIX}

wget ${URL} -O ${LOCAL_PATH}

echo "compressing ${LOCAL_PATH}"

# gzip ${LOCAL_PATH} <- uncomment this line
```