[](){#monitor}
# The getML monitor

The getML monitor contains information on the data imported into the engine as well as the trained pipelines and their performance. It is written in Go and compiled into a binary that is separate from the getML engine.

## Accessing the monitor

The monitor is always started on the same machine as the engine. The engine and the monitor use sockets to communicate. The monitor opens an HTTP port - 1709 by default - for you to access it via your favorite internet browser. Entering the following address into the navigation bar will point your browser to the monitor:

[http://localhost:1709](http://localhost:1709){: style="text-align: center; display: block"}

The HTTP port can only be accessed from within the host the getML suite is running on.

The main purpose of the monitor is to help you with your data science project by providing visual feedback.

!!! note "Tip"
    
    If you experience any issues opening the monitor, try any of these steps:
    
    - Manually shutdown the engine and restart it: `getml.engine.shutdown()` and `getml.engine.launch()`
    - Kill the associated background process in the terminal and restart the engine
    - Close all tabs and windows in which the monitor ran previously and try again

