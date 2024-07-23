[](){#engine}
# The getML engine 

The getML engine is a standalone program written in C++ that does the actual work of feature engineering and prediction.

!!! note
    If you are using the Python API, there is no need to separately install or manage the engine. It will be installed automatically via `pip install getml`.

[](){#engine-start-engine}
## Starting the engine

The engine can be started using the dedicated launcher icon or by using the getML 
command line interface (CLI). For more information, check out the [installation 
instructions][installation] for your operating system.

## Shutting down the engine

There are several ways to shut down the getML engine:

- Click the ':material-power-standby: Shutdown' tab in the sidebar of the monitor
- Press `Ctrl-C` (if started via the command line)
- Run the getML command-line interface (CLI) (see [installation][installation]) using 
  the `-stop` 
  option

## Logging

The engine keeps a log about what it is currently doing.

The easiest way to view the log is to click the '<> Log' tab in the sidebar of the getML monitor. The engine will also output its log to the command line when it is started using the command-line interface.
