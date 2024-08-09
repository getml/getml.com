---
title: getML Suite
---

[](){#getml-suite}
# The getML Suite

The getML ecosystem comprises three fundamental components:

- [getML Engine][engine]
- [Python API][python-api]
- [getML Monitor][monitor]

[](){#engine}
## Engine

Written in C++, the getML Engine is the core of the Suite and does all the heavy lifting. It is responsible for data management, feature engineering, and machine learning.

### Starting the Engine

After [installing the getML Engine][installation], either via `pip`, `Docker` or `CLI` there are two ways to start the getML Engine:

- Using the [Python API][python-api]
- Using the getML [command-line interface (CLI)][separate-installation-of-engine]

Follow the links to learn more about each method.

### Shutting down the Engine

Depending on how you started the Engine, there are different ways to shut it down:

- In the Python API: `getml.engine.shutdown()`
- Click the ':material-power-standby: Shutdown' tab in the sidebar of the monitor
- On command-line interface (CLI): Press `Ctrl-C` or run `getML -stop`

### Logging

The Engine keeps a log about what it is currently doing.

The easiest way to view the log is to click the '<> Log' tab in the sidebar of the [getML Monitor][Monitor]. The Engine will also output its log to the command line when it is started using the command-line interface.

[](){#getml-suite-python-api}
## Python API

Control the Engine with the getML Python API, which provides handlers to the objects in the Engine and all other necessary tools for end-to-end data science projects. For an in-depth read about its individual classes and methods, check out the [Python API documentation][python-api-reference].

!!! note
    - The classes in the Python API act as handles to objects in the getML Engine.
    - When you connect to or create a project:
        - The API establishes a socket connection to the Engine through a determined port.
        - All subsequent commands are sent to the Engine via this connection.

### Setup new project
Set a project in the getML Engine using [`set_project()`][getml.engine.set_project].

```python
import getml
getml.engine.launch()
getml.engine.set_project("test")
```

!!! note
    If the project name does not match an existing project, a new one will be created.

### Managing projects

To get a list of all available projects, use [`list_projects()`][getml.engine.list_projects].
To remove an entire project, use [`delete_project()`][getml.engine.delete_project].

```python
getml.engine.list_projects()
getml.engine.delete_project("test")
```

For more information, refer to the [Managing projects][project-management] section.

[](){#python-api-lifecycles}
### DataFrames

Create a [`DataFrame`][getml.data.DataFrame] by calling for example:

```python
data = getml.data.DataFrame.from_csv(
    "path/to/my/data.csv", 
    "my_data"
)
```

This creates a data frame object in the getML Engine, imports the provided data, and returns a handler to the object as a [`DataFrame`][getml.data.DataFrame] in the Python API.

!!! note
    There are many other methods to create a [`DataFrame`][getml.data.DataFrame], including [`from_db()`][getml.data.DataFrame.from_db], [`from_json()`][getml.data.DataFrame.from_json], or [`from_pandas()`][getml.data.DataFrame.from_pandas]. For a full list of available methods, refer to the [Importing data][importing-data] section.

**Synchronization**

When you apply any method, like [`add()`][getml.data.DataFrame.add], the changes will be automatically reflected in both the Engine and Python. Under the hood, the Python API sends a command to create a new column to the getML engine. The moment the Engine is done, it informs the Python API and the latter triggers the [`refresh()`][getml.data.DataFrame.refresh] method to update the Python handler.

**Saving**

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

**Loading**

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


### Pipelines

The lifecycle of a [`Pipeline`][getml.pipeline.Pipeline] is straightforward and streamlined by the getML Engine, which automatically saves all changes made to a pipeline and loads all pipelines within a project. Pipelines are created within the Python API using constructors, where they are defined by a set of hyperparameters.

!!! note
    The actual weights of the machine learning algorithms are stored exclusively in the getML Engine and are not transferred to the Python API.

Any changes made through methods such as [`fit()`][getml.pipeline.Pipeline.fit] are automatically updated in both the Engine and the Python API.

By using [`set_project()`][getml.engine.set_project], you can load an existing project, and all associated pipelines will be automatically loaded into memory. To view all pipelines in the current project, access the Pipelines container via [`getml.project.Pipelines`][getml.project.Pipelines].

The function [`list_pipelines()`][getml.pipeline.list_pipelines] lists all available pipelines within a project:
```python
getml.pipeline.list_pipelines()
```

To create a corresponding handle in the Python API, use the [`load()`][getml.pipeline.load] function:
```python
pipe = getml.pipeline.load(NAME_OF_THE_PIPELINE)
```

[](){#monitor}
## Monitor

!!! enterprise-adm "Enterprise edition"
    This feature is exclusive to the Enterprise edition and is not available in the Community edition. Discover the [benefits of the Enterprise edition][enterprise-benefits] and [compare their features][enterprise-feature-list].

    For licensing information and technical support, please [contact us][contact-page].

The Monitor provides information on the data imported into the Engine, as well as on the trained pipelines and their performance. It is written in Go and compiled into a binary separate from the getML Engine.

**Accessing the Monitor**

The Monitor runs on the same machine as the Engine, using sockets for communication. By default, it opens an HTTP port (1709) for browser access. To view the Monitor, enter the following address in your browser's navigation bar:

[http://localhost:1709](http://localhost:1709){: style="text-align: center; display: block"}

Please note, the HTTP port is only accessible from within the host machine running the getML Suite.

The main purpose of the Monitor is to provide visual feedback to support your data science projects.

!!! note "Tip"
    
    If you experience issues opening the Monitor, try the following steps:
    
    - Manually shut down and restart the Engine using `getml.engine.shutdown()` and `getml.engine.launch()`.
    - Kill the associated background process in the terminal and restart the Engine.
    - Close all tabs and windows where the Monitor was previously running and try again.


To get started, head over to the [installation instructions][installation].
