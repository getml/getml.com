[](){#project-management}
# Managing projects

When working with getML, all data is bundled into *projects.* getML's projects are managed through the [`getml.project`][getml.project] module.

## The relationship between projects and engine processes
Each project is tied to a specific instance of the [getML engine][engine] running as a global process (independent of your python session). In this way, it is possible to share one getML instance with multiple users to work on different projects. When switching projects through [`getml.project.switch()`][getml.project.attrs.switch], the python API spawns a new process and establishes a connection to this process, while the currently loaded project remains in memory and its process is delegated to the background (until you explicitly [`getml.project.suspend()`][getml.project.attrs.suspend] the project). You can also work on multiple projects simultaneously from different python sessions. This comes in particularly handy if you use [Jupyter Lab](https://jupyter.org/) to open multiple notebooks and manage multiple python kernels simultaneously.

To load an existing project or create a new one, you can do so from the 'Projects' view in the monitor or use the API ([`getml.engine.set_project()`][getml.engine.set_project]).

If you want to shut down the engine process associated with the current project, you 
can call [`getml.project.suspend()`][getml.project.attrs.suspend]. When you suspend 
the project, the memory of the engine is flushed and all unsaved changes to the data 
frames are lost (see [lifecycles and synchronization between engine and API][python-api-lifecycles] for details). All pipelines of the new project are automatically loaded into memory. You can retrieve all of your project's pipelines through [`getml.project.pipelines`][getml.project.Pipelines]. 

Projects can be deleted by clicking the trash can icon in the 'Projects' tab of the getML monitor or by calling [`getml.engine.delete_project()`][getml.engine.delete_project] (to delete a project by name) or [`getml.project.delete()`][getml.project.attrs.delete] (to suspend and delete the project currently loaded).

## Managing data using projects

Every project has its own folder in `~/.getML/getml-VERSION/projects` (for Linux and macOS) in which all of its data and pipelines are stored. On Windows, the projects folder is in the same location as `getML.exe`. These folders can be easily shared between different instances of getML; even between different operating systems. However, individual pipelines or data frames cannot be simply copied to another project folder – they are tied to the project. Projects can be bundled and exported/imported.

## Using the project module to manage your project

The [`getml.project`][getml.project] module is the entry point to your projects. 
From here, you can: query project-specific data ([`pipelines`][getml.project.Pipelines], 
[`data_frames`][getml.project.DataFrames], 
[`hyperopts`][getml.project.Hyperopts]), manage the state of the current project (
[`delete()`][getml.project.attrs.delete], [`restart()`][getml.project.attrs.restart], [`switch()`][getml.project.attrs.switch], [`suspend()`][getml.project.attrs.suspend]), and import projects from or export projects as a `.getml` bundle to disk ([`load()`][getml.project.attrs.load], [`save()`][getml.project.attrs.save]).

