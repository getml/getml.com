[](){#project-management}
# Managing Projects

When working with getML, all data is organized into *projects.* These projects are managed through the [`getml.project`][getml.project] module.

## Relationship between Projects and Engine Processes
Each project is linked to a specific instance of the [getML Engine][engine], which runs as a global process, independent of your Python session. This setup allows multiple users to share a single getML instance and work on different projects. When switching projects using [`getml.project.switch()`][getml.project.attrs.switch], the Python API spawns a new process and connects to it, while the current project's process moves to the background (unless explicitly suspended via [`getml.project.suspend()`][getml.project.attrs.suspend]). You can also work on multiple projects simultaneously from different Python sessions, which is particularly useful when using [Jupyter Lab](https://jupyter.org/) to manage multiple notebooks and Python kernels concurrently.

To load an existing project or create a new one, use [`getml.engine.set_project()`][getml.engine.set_project].

To shut down the Engine process associated with the current project, call [`getml.project.suspend()`][getml.project.attrs.suspend]. Suspending a project flushes the Engine's memory, and any unsaved changes to data frames are lost (refer to [Dataframes][python-api-lifecycles] for details). All pipelines of the new project are automatically loaded into memory. You can retrieve all your project's pipelines through [`getml.project.pipelines`][getml.project.Pipelines]. 

Projects can be deleted by calling [`getml.engine.delete_project()`][getml.engine.delete_project] to delete a project by name or [`getml.project.delete()`][getml.project.attrs.delete] to suspend and delete the currently loaded project.

## Managing Data Using Projects

Each project has its own folder in `~/.getML/getml-VERSION/projects` (for Linux and macOS) where all its data and pipelines are stored. On Windows, the projects folder is located in the same directory as `getML.exe`. These folders can be easily shared between different getML instances and even across different operating systems. However, individual pipelines or data frames cannot be simply copied to another project folder as they are tied to the project. Projects can be bundled, exported, and imported.

## Using the Project Module to Manage Your Project

The [`getml.project`][getml.project] module is the entry point for managing your projects. From here, you can query project-specific data ([`data_frames`][project-dataframes], [`hyperopts`][project-hyperopts], [`pipelines`][project-pipelines]), manage the state of the current project ([`delete()`][getml.project.attrs.delete], [`restart()`][getml.project.attrs.restart], [`switch()`][getml.project.attrs.switch], [`suspend()`][getml.project.attrs.suspend]), and import or export projects as `.getml` bundles to disk ([`load()`][getml.project.attrs.load], [`save()`][getml.project.attrs.save]).
