---
course: data-engineering-zoomcamp
id: 3e83372387
question: 'Docker - invalid reference format: repository name must be lowercase (Mounting
  volumes with Docker on Windows)'
section: 'Module 1: Docker and Terraform'
sort_order: 690
---

Mapping volumes on Windows could be tricky. The way it was done in the course video doesn’t work for everyone.

First, if you move your data to some folder without spaces. E.g. if your code is in “C:/Users/Alexey Grigorev/git/…”, move it to “C:/git/…”

Try replacing the “-v” part with one of the following options:

-v /c:/some/path/ny_taxi_postgres_data:/var/lib/postgresql/data

-v //c:/some/path/ny_taxi_postgres_data:/var/lib/postgresql/data

-v /c/some/path/ny_taxi_postgres_data:/var/lib/postgresql/data

-v //c/some/path/ny_taxi_postgres_data:/var/lib/postgresql/data

--volume //driveletter/path/ny_taxi_postgres_data/:/var/lib/postgresql/data

Try adding winpty before the whole command:

winpty docker run -it

-e POSTGRES_USER="root"

-e POSTGRES_PASSWORD="root"

-e POSTGRES_DB="ny_taxi"

-v /c:/some/path/ny_taxi_postgres_data:/var/lib/postgresql/data

-p 5432:5432

postgres:1

Try adding quotes:

-v "/c:/some/path/ny_taxi_postgres_data:/var/lib/postgresql/data"

-v "//c:/some/path/ny_taxi_postgres_data:/var/lib/postgresql/data"

-v “/c/some/path/ny_taxi_postgres_data:/var/lib/postgresql/data"

-v "//c/some/path/ny_taxi_postgres_data:/var/lib/postgresql/data"

-v "c:\some\path\ny_taxi_postgres_data":/var/lib/postgresql/data

Note:  (Window) if it automatically creates a folder called “ny_taxi_postgres_data;C” suggests you have problems with volume mapping, try deleting both folders and replacing “-v” part with other options. For me “//c/” works instead of “/c/”. And it will work by automatically creating a correct folder called “ny_taxi_postgres_data”.

A possible solution to this error would be to use /”$(pwd)”/ny_taxi_postgres_data:/var/lib/postgresql/data (with quotes’ position varying as in the above list).

Yes for windows use the command it works perfectly fine

-v /”$(pwd)”/ny_taxi_postgres_data:/var/lib/postgresql/data

Important: note how the quotes are placed.

If none of these options work, you can use a volume name instead of the path:

-v ny_taxi_postgres_data:/var/lib/postgresql/data

For Mac: You can wrap $(pwd) with quotes like the highlighted.

docker run -it \

-e POSTGRES_USER="root" \

-e POSTGRES_PASSWORD="root" \

-e POSTGRES_DB="ny_taxi" \

-v "$(pwd)"/ny_taxi_postgres_data:/var/lib/postgresql/data \

-p 5432:5432 \

Postgres:13

docker run -it \

-e POSTGRES_USER="root" \

-e POSTGRES_PASSWORD="root" \

-e POSTGRES_DB="ny_taxi" \

-v "$(pwd)"/ny_taxi_postgres_data:/var/lib/postgresql/data \

-p 5432:5432 \

postgres:13

Source:

