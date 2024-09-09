[](){#macos-windows-docker}
# Docker for macOS, Windows & Linux


On macOS and Windows, you can to run the Engine in a Docker container. We are working on providing native support for them in the near future.

Setup the [Python API][python-api-concepts] and the [Engine][engine-install] of the [getML Community edition](https://github.com/getml/getml-community) as follows.

## Python API

Use Python's pip package manager to install the API:

```py
pip install getml
```

## Engine {#engine-install}

Make sure that Docker is [installed](https://docs.docker.com/get-docker/). For Linux, follow these [post-installation steps](https://docs.docker.com/engine/install/linux-postinstall/) to run Docker without root rights.

!!! enterprise-adm "Enterprise Edition"
    Need the highest models accuracy in commercial prediction applications and enterprise grade support?

    [Choose getML Enterprise][enterprise-benefits]{ .md-button }

    Once you have obtained the getML Enterprise edition, you can install it as follows:

    - Install the [Python API][python-api-concepts]: `pip install getml`
    - Install the [Engine][engine-install] by following the same instructions as below. Just replace the URL with that of the Enterprise `docker-compose.yml` file you have been provided with.


Run the following command in your terminal (macOS & Linux) or PowerShell (Windows):

```bash
curl https://raw.githubusercontent.com/getml/getml-community/1.5.0/runtime/docker-compose.yml | docker-compose up -f -
```

This will download `docker-compose.yml` configuration file and use `docker compose` to run a getML service.

In addition, a docker volume `getml` will be created and mounted into the container. This volume will contain the files of projects. The ports required for the Python API to communicate with the Engine will be mapped to the host system.

To shut down the service after you are done, press `Ctrl+c`.


## Where to go next

To get started with getML, you may check out:

- [User Guide][user-guide-index], which provides a comprehensive introduction to getML at varying levels of detail
- [Examples][examples-index], where we demonstrate practical examples inside Jupyter Notebooks