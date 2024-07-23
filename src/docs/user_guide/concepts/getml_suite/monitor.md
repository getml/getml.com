---
status: enterprise
---
[](){#monitor}

# The getML Monitor

!!! info "Enterprise Feature"
    This is an enterprise feature and not available in the community edition. Learn more about the [benefits](/enterprise/benefits) and see the [comparion of features](/enterprise/feature-list) between the community and enterprise edition.

The monitor provides information on the data imported into the engine, as well as on the trained pipelines and their performance. It is written in Go and compiled into a binary separate from the getML engine.

## Accessing the Monitor

The monitor runs on the same machine as the engine, using sockets for communication. By default, it opens an HTTP port (1709) for browser access. To view the monitor, enter the following address in your browser's navigation bar:

[http://localhost:1709](http://localhost:1709){: style="text-align: center; display: block"}

Please note, the HTTP port is only accessible from within the host machine running the getML suite.

The main purpose of the monitor is to provide visual feedback to support your data science projects.

!!! note "Tip"
    
    If you experience issues opening the monitor, try the following steps:
    
    - Manually shut down and restart the engine using `getml.engine.shutdown()` and `getml.engine.launch()`.
    - Kill the associated background process in the terminal and restart the engine.
    - Close all tabs and windows where the monitor was previously running and try again.

