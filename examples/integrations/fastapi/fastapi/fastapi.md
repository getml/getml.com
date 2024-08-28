[](){#fastapi}
## Provide generic prediction endpoint via FastAPI

A common way to communicate with resources is via REST-APIs. In Python, [FastAPI](https://fastapi.tiangolo.com/) is a well known web framework package to build web-APIs.

The following shows an example how easily, pipelines in a project can be made accessible via endpoints in FastAPI.

It is assumed that you have some basic knowledge of FastAPI and the getML framework.

Helpful resources to get started:

[FastAPI get started](https://fastapi.tiangolo.com/tutorial/first-steps/)  
[getML example notebooks](https://github.com/getml/getml-demo)  
[getML user guide][user-guide-index]  

This integration example requires at least v1.4.0 of the [getml package](https://pypi.org/project/getml/) and at least [Python 3.8](https://www.python.org/downloads/).

### Example Data

As an example project we first run the demo notebook ["Loan default prediction"](https://notebooks.getml.com/github/getml/getml-demo/blob/master/loans.ipynb) which creates a project named "loans" in the getML Engine.

### Code Explained

First, import the necessary packages and create a FastAPI-App `app`. If the Engine isn't running yet 
([`getml.engine.is_engine_alive()`][getml.engine.is_engine_alive]) launch it 
([`getml.engine.launch()`][getml.engine.launch]). The `launch_browser=False` 
option prevents the browser to be opened 
when the Engine spins up. Further, direct the Engine to load and set the previously created 
[`project`][getml.project] "loans". ([`getml.engine.set_project()`][getml.engine.set_project])

```python
from typing import Dict, List, Optional, Union
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from uvicorn import run
from getml import engine, pipeline, Pipeline, DataFrame

app: FastAPI = FastAPI()

if not engine.is_alive():
    engine.launch(launch_browser=False)
engine.set_project("loans")
```

Create the first GET endpoint which returns a list with all
[`pipeline`][getml.pipeline]s present ([`list_pipelines()`][getml.pipeline.list_pipelines]) in the
project. The list itself will only contain the names of the pipelines and no
additional metainformation. For sake of simplicity of the tutorial pagination is
left out.

```python
@app.get("/pipeline")
async def get_pipeline() -> List[str]:
    return pipeline.list_pipelines()
```

The following is required to start the app with uvicorn. Run your Python code
and test the endpoint via [localhost:8080/pipeline](localhost:8080/pipeline).

```python
if __name__ == "__main__":
    run(app, host="localhost", port=8080)
```


To expand the functionality, add another informative GET endpoint for a single
pipeline. The `pipeline_id` can be retrieved from the previously
created GET endpoint. The existence of the pipeline can be checked using
[`exists()`][getml.pipeline.exists]. After validating its existence, the Engine must be
directed to load the pipeline identified with the provided
`pipeline_id`. Information of interest could be the
name of the population data frame and peripheral data frames, the applied
preprocessors, used feature learners and selectors and target predictors. Those
information can be retrieved from the member variable `metadata` of the
pipeline (`pipeline_.metadata`) and the pipeline itself. 
Again this endpoint can be tested by running your code and invoking the endpoint
[localhost:8080/pipeline/a1b2c3](localhost:8080/pipeline/a1b2c3) assuming that
the previously created pipeline has the id `a1b2c3`.

```python
@app.get("/pipeline/{pipeline_id}")
async def get_pipeline_pipeline_id(pipeline_id: str) -> Dict[str, Union[str, List[str]]]:
    if not pipeline.exists(pipeline_id):
        raise HTTPException(status_code=404, detail=f'Pipeline {pipeline_id} not found.')

    pipeline_ = pipeline.load(pipeline_id)

    if pipeline_.metadata is None:
        raise HTTPException(status_code=409,
                            detail='The data schema is missing or pipeline is incomplete')

    meta_data = pipeline_.metadata
    metadata: Dict[str, Union[str, List[str]]] = {}
    metadata["data_model"] = meta_data.population.name
    metadata["peripheral"] = [_.name for _ in meta_data.peripheral]
    metadata["preprocessors"] = [_.type for _ in pipeline_.preprocessors]
    metadata["feature_learners"] = [_.type for _ in pipeline_.feature_learners]
    metadata["feature_selectors"] = [_.type for _ in pipeline_.feature_selectors]
    metadata["predictors"] = [_.type for _ in pipeline_.predictors]

    return metadata

```

To create the prediction endpoint the data scheme for the request body needs to
be created first. For a prediction the getML Engine requires multiple data sets,
the population data set `population` and any related peripheral data set
`peripheral` based on the [Data model][data-model] of the pipeline. The
peripheral data sets can be either a list or a dictionary where the order of the
data sets in the list needs to match the order returned by
`[_.name for _ in getml.pipeline.metadata.peripheral]`. This information
can also be retrieved by calling the previously created GET endpoint.

```python
class PredictionBody(BaseModel):
    peripheral: Union[List[Dict[str, List]], Dict[str, Dict[str, List]]]
    population: Dict[str, List]
```

Next up, implement the POST endpoint which accepts data to task the Engine to
make a prediction. Validate that the pipeline exist, load the pipeline
([`load()`][getml.pipeline.load]), and validate that the pipeline has been
finalized.

```python
@app.post("/pipeline/{pipeline_id}/predict")
async def post_project_predict(pipeline_id: str, body: PredictionBody) -> Optional[List]:
    if not pipeline.exists(pipeline_id):
        raise HTTPException(status_code=404,
                            detail=f'Pipeline {pipeline_id} not found.')

    pipeline_: Pipeline = pipeline.load(pipeline_id)

    if pipeline_.metadata is None:
        raise HTTPException(status_code=409,
                            detail='The data schema is missing or pipeline is incomplete')
```

The request body should contain both the population and peripheral data. Check
that the population in the request body contains any content. Create a
data frame from the dictionary ([`from_dict()`][getml.DataFrame.from_dict]): the name of
the data frame must not collide with an existing data frame in the pipeline, the
roles of the population can be obtained from the pipeline, using
`pipeline_.metadata.population.roles`.

```python

if not body.population:
    raise HTTPException(status_code=400, detail='Missing population data.')

population_data_frame = DataFrame.from_dict(name='future',
                                            roles=pipeline_.metadata.population.roles,
                                            data=body.population)
```

The peripheral can be submitted in the request body both as list and dictionary.
Check that in case the peripheral data sets are received as dictionaries that
the names of all required peripheral data sets exist in the dictionary keys, and
in case the peripheral data sets are received as a list, check that the length of
the list matches the number of peripheral data sets in the pipeline. After,
create a list of data frames of the peripheral data. Again, ensure that the
names of the created data frames do not collide with existing data frames and
use the roles defined in the pipeline for the peripheral data sets
(`pipeline_.metadata.peripheral[i].roles`).

```python
peripheral_names = [_.name for _ in pipeline_.peripheral]

if isinstance(body.peripheral, dict):
    if set(peripheral_names) - set(body.peripheral.keys()):
        raise HTTPException(
            status_code=400,
            detail=f'Missing peripheral data, expected {peripheral_names}')
    periperal_raw_data = body.peripheral
else:
    if len(peripheral_names) != len(body.peripheral):
        raise HTTPException(
            status_code=400,
            detail=f"Expected {len(pipeline_.peripheral)} peripheral data frames.")
    periperal_raw_data = dict(zip(peripheral_names, body.peripheral))

peripheral_data_frames = [
    DataFrame.from_dict(name=name + '_predict',
                        data=periperal_raw_data[name],
                        roles=pipeline_.metadata.peripheral[i].roles)
    for i, name in enumerate(peripheral_names)
]

```

This leaves the actual call to the Engine to make a prediction
([`predict()`][getml.Pipeline.predict]) using the previously created population data
frame and peripheral data frames. The predicted target value is a numpy array
and returned transformed to a list as request response. 

```python
prediction = pipeline_.predict(
    population_table=population_data_frame,
    peripheral_tables=peripheral_data_frames
)

if prediction:
    return prediction.tolist()

raise HTTPException(status_code=500, detail='getML Engine didn\'t return a result.')

```

This endpoint can be called on
[localhost:8080/pipeline/a1b2c3/predict](localhost:8080/pipeline/a1b2c3/predict),
where the body needs the form: 

```json
{
    "peripheral": [{
        "column_1": [2.4, 3.0, 1.2, 1.4, 2.2],
        "column_2": ["a", "b", "a", "b", "b"]
    }],
    "population": {
        "column_1": [0.2, 0.1],
        "column_2": ["a", "b"],
        "time_stamp": ["2010-01-01 12:30:00", "2010-01-01 23:30:00"]
    }
}
```

Example json data can be extracted from the notebook using the following code
snippet at the end of the notebook used to create the Example Data.

```python
from typing import Union, Any
from datetime import datetime
from json import dumps


def handle_timestamp(x: Union[Any, datetime]):
    if isinstance(x, datetime):
        return x.strftime(r'%Y-%m-%d %H:%M:%S')


pd_population_test = population_test.to_pandas()
account_id = pd_population_test.iloc[0]["account_id"]
populaton_dict = pd_population_test[pd_population_test["account_id"] == account_id].to_dict()
populaton_json = dumps({k: list(v.values()) for k, v in populaton_dict.items()}, default=handle_timestamp)
pd_peripherals = {_.name: _.to_pandas() for _ in [order, trans, meta]}
peripheral_dict = {k: v[v["account_id"] == account_id].to_dict() for k, v in pd_peripherals.items()}
peripheral_json = dumps(
    {k: {vk: list(vv.values()) for vk, vv in v.items()} for k, v in peripheral_dict.items()},
    default=handle_timestamp)
populaton_json
peripheral_json
```

### Conclusion


With only a few lines it is possible to create a web API to make project
pipelines accessible and request target predictions for provided population and
peripheral data.
