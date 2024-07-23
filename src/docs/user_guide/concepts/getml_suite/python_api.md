[](){#getml-suite-python-api}
# The getML Python API

This section provides some general information about the API and how it interacts 
with the engine. For an in-depth read about its individual classes and methods, check out the 
[Python API documentation][python-api].

!!! note
    - The classes in the Python API act as handles to objects in the getML engine.
    - When you connect to or create a project:
        - The API establishes a socket connection to the engine through a determined port.
        - All subsequent commands are sent to the engine via this connection.

## Setup new project
Set a project in the getML engine using [`set_project()`][getml.engine.set_project].

```python
import getml
getml.engine.launch()
getml.engine.set_project("test")
```

!!! note
    If the project name does not match an existing project, a new one will be created.

## Managing projects

To get a list of all available projects, use [`list_projects()`][getml.engine.list_projects].
To remove an entire project, use [`delete_project()`][getml.engine.delete_project].

```python
getml.engine.list_projects()
getml.engine.delete_project("test")
```

For more information, refer to the [Managing projects][project-management] section.

[](){#python-api-lifecycles}
## Lifecycles and Synchronization between Engine and API

Key objects in the API include:

- Data frames ([`DataFrame`][getml.data.DataFrame]), acting as a container for all your data.
- Pipelines ([`Pipeline`][getml.pipeline.Pipeline]), comparable to `models` in other ML libraries.

[](){#lifecycle-dataframe}
### Lifecycle of a DataFrame

Create a [`DataFrame`][getml.data.DataFrame] by calling for example:

```python
data = getml.data.DataFrame.from_csv(
    "path/to/my/data.csv", 
    "my_data"
)
```

This creates a data frame object in the getML engine, imports the provided data, and returns a handler to the object as a [`DataFrame`][getml.data.DataFrame] in the Python API.

!!! note
    There are many other methods to create a [`DataFrame`][getml.data.DataFrame], including [`from_db()`][getml.data.DataFrame.from_db], [`from_json()`][getml.data.DataFrame.from_json], or [`from_pandas()`][getml.data.DataFrame.from_pandas]. For a full list of available methods, refer to the [Importing data][importing-data] section.

#### Synchronization

When you apply any method, like [`add()`][getml.data.DataFrame.add], the changes will be automatically reflected in both the engine and Python. Under the hood, the Python API sends a command to create a new column to the getML engine. The moment the engine is done, it informs the Python API and the latter triggers the [`refresh()`][getml.data.DataFrame.refresh] method to update the Python handler.

#### Saving

!!! warning
    DataFrames are **never saved automatically** and **never loaded automatically**. All unsaved changes to a [`DataFrame`][getml.data.DataFrame] will be lost when restarting the engine. 

To get a list of all your current data_frames, access the container via:

```python
getml.project.data_frames
#or
getml.data.list_data_frames()
```

You can save a specific data frame to disk using [`.save()`][getml.data.DataFrame.save] method on the [`DataFrame`][getml.data.DataFrame]:

```python
# by index
getml.project.data_frames[0].save()
# by name
getml.project.data_frames["my_data"].save()
```

To save all data frames associated with the current project, use the [`.save()`][getml.data.Container.save] method on the [`Container`][getml.data.Container]:

```python
getml.project.data_frames.save()
```

#### Loading

To load a specific [`DataFrame`][getml.data.DataFrame], use [`load_data_frame()`][getml.data.load_data_frame] or [`DataFrame().load()`][getml.data.DataFrame.load]:

```python
df = getml.data.load_data_frame("my_data")
# Forces the API to load the version stored on disk over the one held in memory
df = getml.data.DataFrame("my_data").load()
```

Use [`.load()`][getml.data.DataFrame.load] on the [`Container`][getml.data.Container] to load all data frames associated with the current project:

```python
getml.project.data_frames.load()
```

!!! note
    If a [`DataFrame`][getml.data.DataFrame] is already available in memory (for example "my_data" from above), [`load_data_frame()`][getml.data.load_data_frame] will return a handle to that data frame. If no such [`DataFrame`][getml.data.DataFrame] is held in memory, the function will try to load the data frame from disk and then return a handle. If that is unsuccessful, an exception is thrown.


### Lifecycle of a Pipeline

The lifecycle of a [`Pipeline`][getml.pipeline.Pipeline] is streamlined by the getML engine, which automatically saves all changes made to a pipeline and loads all pipelines within a project.

Pipelines are created within the Python API using constructors, where they are defined by a set of hyperparameters.

!!! note
    The actual weights of the machine learning algorithms are stored exclusively in the getML engine and are not transferred to the Python API.

Any changes made through methods such as [`fit()`][getml.pipeline.Pipeline.fit] are automatically updated in both the engine and the Python API.

By using [`set_project()`][getml.engine.set_project], you can load an existing project, and all associated pipelines will be automatically loaded into memory. To view all pipelines in the current project, access the Pipelines container via [`getml.project.Pipelines`][getml.project.Pipelines].

The function [`list_pipelines()`][getml.pipeline.list_pipelines] lists all available pipelines within a project:
```python
getml.pipeline.list_pipelines()
```

To create a corresponding handle in the Python API, use the [`load()`][getml.pipeline.load] function:
```python
pipe = getml.pipeline.load(NAME_OF_THE_PIPELINE)
```

