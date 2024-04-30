[](){#engine}
# The getML engine 



The getML engine is a standalone program written in C++ that does the actual work of feature engineering and prediction.

[](){#engine-start-engine}
## Starting the engine

The engine can be started using the dedicated launcher icon or by using the getML command line interface (CLI). For more information, check out the [installation instructions](#installation) for your operating system.

## Shutting down the engine

There are several ways to shut down the getML engine:

- Click the 'Shutdown' tab in the sidebar of the monitor
- Press `Ctrl-C` (if started via the command line)
- Run the getML command-line interface (CLI) (see [installation](#installation)) using the `-stop` option
- macOS only: Right-click the getML icon in the status bar and click 'Quit' (if started via the launchpad)

## Logging

The engine keeps a log about what it is currently doing.

The easiest way to view the log is to click the 'Log' tab in the sidebar of the getML monitor. The engine will also output its log to the command line when it is started using the command-line interface.
