# Deployment

The results of the [feature learning][feature-engineering] and the [prediction][predicting] can be retrieved in different ways and formats.

## Transpiling pipelines

- Using [`SQLCode.save()`](getml/pipeline/SQLCode/save), you can transpile Pipelines to SQL code, which can be used without any proprietary components.

## Returning Python objects

- Using the [`Pipeline.transform`](getml/pipeline/Pipeline/transform) and [`Pipeline.predict`](getml/pipeline/Pipeline/predict) methods of a trained [`Pipeline`](getml/pipeline/Pipeline), you can access both the features and the predictions as `numpy.ndarray` via the Python API.

## Writing into a database

- You can also write both features and prediction results back into a new table of the connected database by providing the `table_name` argument in the [`Pipeline.transform`](getml/pipeline/Pipeline/transform) and [`Pipeline.predict`](getml/pipeline/Pipeline/predict) methods. Please refer to the [unified import interface][importing-data-unified-interface] for information on how to connect to a database.

## Responding to a HTTP POST request

- The getML suite contains HTTP endpoints to post new data via a JSON string and retrieve either the resulting features or the predictions.
## Batch prediction

Batch prediction pipelines are the most common way of productionizing machine learning pipelines on relational data. These pipelines are usually set to run regularly (once a month, once a week, once a day...) to create a batch of predictions on the newest data. They are typically inserted into a [Docker](https://www.docker.com/) container and scheduled using tools like [Jenkins](https://www.jenkins.io/) and/or [Airflow](https://airflow.apache.org/).

If you are looking for a pure Python, 100% open-source way to productionize getML's [`Pipeline`](getml/data/Pipeline)s, you can transpile all the features into sqlite3 code. sqlite3 is part of the Python standard library, and you can use getML's 100% open source and pure Python [`sqlite3`](getml/sqlite3) which provides some useful extra functionality not included in Python's standard library.

## HTTP Endpoints

As soon as you have trained a pipeline, whitelisted it for external access using its [`deploy`](getml/pipeline/Pipeline/deploy) method, and configured the getML monitor for [remote access](#remote_access), you can transform new data into features or make predictions on them using these endpoints:

- [Transform endpoint: `http://localhost:1709/transform/PIPELINE_NAME`][deployment-transform]
- [Predict endpoint: `http://localhost:1709/predict/PIPELINE_NAME`][deployment-predict]

To each of them, you must send a POST request containing the new data as a JSON string in a specific [request format][deployment-request-format].

!!! note

    For testing and developing purposes, you can also use the HTTP port of the monitor to query the endpoints. Note that this is only possible within the same host. The corresponding syntax is  [http://localhost:1709/predict/PIPELINE_NAME](http://localhost:1709/predict/PIPELINE_NAME)

[](){#deployment-request-format}
## Request Format

In all POST requests to the endpoints, a JSON string with the following syntax has to be provided in the body:

```json
{
  "peripheral": [{
    "column_1": [],
    "column_2": []
  },{
    "column_1": [],
    "column_2": []
  }],
  "population": {
    "column_1": [],
    "column_2": []
  }
}
```


It has to have exactly two keys in the top level called
`population` and `peripheral`. These will contain the new
input data.

The order of the columns is irrelevant. They will be matched according to their
names. However, the order of the
individual peripheral tables is very important and has to exactly
match the order the corresponding [`Placeholder`](getml/data/Placeholder)
have been provided in the constructor of `pipeline`.

In our example above, we
could post a JSON string like this:

```json
{
  "peripheral": [{
    "column_01": [2.4, 3.0, 1.2, 1.4, 2.2],
    "join_key": ["0", "0", "0", "0", "0"],
    "time_stamp": [0.1, 0.2, 0.3, 0.4, 0.8]
  }],
  "population": {
    "column_01": [2.2, 3.2],
    "join_key": ["0", "0"],
    "time_stamp": [0.65, 0.81]
  }
}
```
# Time stamp formats in requests

You might have noticed that the time stamps in the example above have been
passed as numerical values and not as their string representations
shown in the beginning. Both ways are
supported by the getML monitor. But if you choose to pass the
string representation, you also have to specify the particular format
in order for the getML engine to interpret your data properly.

```json
{
  "peripheral": [{
    "column_01": [2.4, 3.0, 1.2, 1.4, 2.2],
    "join_key": ["0", "0", "0", "0", "0"],
    "time_stamp": ["2010-01-01 00:15:00", "2010-01-01 08:00:00", "2010-01-01 09:30:00", "2010-01-01 13:00:00", "2010-01-01 23:35:00"]
  }],
  "population": {
    "column_01": [2.2, 3.2],
    "join_key": ["0", "0"],
    "time_stamp": ["2010-01-01 12:30:00", "2010-01-01 23:30:00"]
  },
  "timeFormats": ["%Y-%m-%d %H:%M:%S"]
}
```

All special characters available for specifying the format of the time
stamps are listed and described in
e.g. [`read_csv()`](getml/data/DataFrame/read_csv).

# Using an existing [`DataFrame`](getml/data/DataFrame)

You can also use a
[`DataFrame`](getml/data/DataFrame) that already 
exists on the getML engine:

```json
{
  "peripheral": [{
    "df": "peripheral_table"
  }],
  "population": {
    "column_01": [2.2, 3.2],
    "join_key": ["0", "0"],
    "time_stamp": [0.65, 0.81]
  }
}
```

# Using data from a database

You can also read the data from the connected database
(see [unified import interface][importing-data-unified-interface]) 
by passing an arbitrary query to the `query` key:

```json
{
  "peripheral": [{
    "query": "SELECT * FROM PERIPHERAL WHERE join_key = '0';"
  }],
  "population": {
    "column_01": [2.2, 3.2],
    "join_key": ["0", "0"],
    "time_stamp": [0.65, 0.81]
  }
}
```
[](){#deployment-transform}
# Transform Endpoint

The transform endpoint returns the generated features.

[http://localhost:1709/transform/PIPELINE_NAME](http://localhost:1709/transform/PIPELINE_NAME)

Such an HTTP request can be sent in many languages. For
illustration purposes, we will use the command line tool `curl`,
which comes preinstalled on both Linux and macOS. Also, we will use
the HTTP port via localhost (only possible for terminals running on
the same machine as the getML monitor) for better reproducibility.

```bash
curl --header "Content-Type: application/json"           \
     --request POST                                      \
     --data '{"peripheral":[{"column_01":[2.4,3.0,1.2,1.4,2.2],"join_key":["0","0","0","0","0"],"time_stamp":[0.1,0.2,0.3,0.4,0.8]}],"population":{"column_01":[2.2,3.2],"join_key":["0","0"],"time_stamp":[0.65,0.81]}}' \
     http://localhost:1709/transform/PIPELINE_NAME
```
[](){#deployment-predict}
# Predict Endpoint

When using getML as an end-to-end data science pipeline, you can use
the predict endpoint to upload new, unseen data and receive the
resulting predictions as a response via HTTP.

[http://localhost:1709/predict/PIPELINE_NAME](http://localhost:1709/predict/PIPELINE_NAME)

Such an HTTP request can be sent in many languages. For
illustration purposes, we will use the command line tool `curl`,
which comes preinstalled on both Linux and macOS. Also, we will use
the HTTP port via localhost (only possible for terminals running on
the same machine as the getML monitor) for better reproducibility.

```bash
curl --header "Content-Type: application/json"           \
     --request POST                                      \
     --data '{"peripheral":[{"column_01":[2.4,3.0,1.2,1.4,2.2],"join_key":["0","0","0","0","0"],"time_stamp":[0.1,0.2,0.3,0.4,0.8]}],"population":{"column_01":[2.2,3.2],"join_key":["0","0"],"time_stamp":[0.65,0.81]}}' \
     http://localhost:1709/predict/PIPELINE_NAME
```
