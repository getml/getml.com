# Docker for macOS, Windows & Linux


On macOS and Windows, you can to run the engine in a Docker container. We are working on providing native support for them in the near future.

Setup the [Python API][getml-suite-python-api] and the [engine][engine] of the [getML Community edition](https://github.com/getml/getml-community) as follows.

## Python API

Use Python's pip package manager to install the API:

```py
pip install getml
```
[](){#engine-docker-installation}
## Engine

Make sure that Docker is [installed](https://docs.docker.com/get-docker/). For Linux, follow these [post-installation steps](https://docs.docker.com/engine/install/linux-postinstall/) to run Docker without root rights.

!!! enterprise-adm "Enterprise Edition"
    Need the highest models accuracy in commercial prediction applications and enterprise grade support?

    [Choose getML enterprise](../../enterprise/benefits.md){ .md-button }

    Once you have obtained the getML Enterprise edition, you can install it as follows:

    - Install the [Python API][getml-suite-python-api]: `pip install getml`
    - Install the [engine][engine] by following the same [instructions as below][engine-docker-installation]. Just replace the URL with that of the enterprise `docker-compose.yml` file you have been provided with.


Run the following command in your terminal (macOS & Linux) or PowerShell (Windows):

```bash
curl https://raw.githubusercontent.com/getml/getml-community/1.5.0/runtime/docker-compose.yml | docker-compose up -f -
```

This will download `docker-compose.yml` configuration file and use `docker compose` to run a getML service.

In addition, a local directory `getml` will be created if it doesn't exist and mounted into the container. This directory will contain the files of projects. The ports required for the Python API to communicate with the engine will be mapped to the host system.

To shut down the service after you are done, press `Ctrl+c`.
