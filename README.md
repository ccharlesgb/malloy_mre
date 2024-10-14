
# Run with docker compose:

`docker compose run --build base`

You should see a failure relating to the node service

# Run outside of docker

`poetry install`
`poetry shell`
`python3 -m malloy_mre`

You will see an error (But that's ok because this project isn't real but the service is working):

```
ERROR:absl:404 GET https://bigquery.googleapis.com/bigquery/v2/projects/proj/datasets/dataset/tables/my_data?prettyPrint=false: Project proj is not found. Make sure it references valid GCP project that hasn't been deleted.; Project id: proj
```