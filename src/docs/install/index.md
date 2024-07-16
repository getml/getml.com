

# Choose a flavour

Download the getML community edition to get started with the most advanced software for relational learning.

## GetML Enterprise

Need the highest models accuracy in commercial prediction applications and enterprise grade support?

[Choose getML enterprise](/enterprise/benefits){ .md-button }


## Install getML community edition

GetML is available for Python 3.8 to 3.12 and supported on the following 64-bit systems and architectures:

- Ubuntu 16.04 or later (amd64/arm)
- macOS 10.12.6 or later (amd64/arm)
- WSL2 via Windows 10 19044 or higher (amd64)

## Recommended installation

### Linux
Install getML community edition with Python's pip package manager.

```py
pip install getml
```
The will install both the [Python API][getml-suite-python-api] and the [engine][engine] on your Linux machine.


<!-- [Read the pip install guide](packages/pip.md){ .md-button .md-button--primary } -->

### macOS, Windows & Linux
Install the [Python API][getml-suite-python-api] and the [engine][engine] separately:

- Python API
    
    Use Python's pip package manager to install the API:

    ```py
    pip install getml
    ```

- Engine

    You will have to run the [engine][engine] in a [Docker](https://www.docker.com/) container. Make sure that Docker is [installed](https://docs.docker.com/get-docker/) and run the following command in your terminal (macOS) or PowerShell (Windows):

    ```bash
    curl https://raw.githubusercontent.com/getml/getml-community/1.5.0/runtime/docker-compose.yml | docker-compose up -f -
    ```

    This will download `docker-compose.yml` configuration file and use `docker compose` to run a getML service.

    In addition, a local directory `getml` will be created if it doesn't exist and mounted into the container. This directory will contain the files of projects. The ports required for the Python API to communicate with the engine will be mapped to the host system.

    To shut down the service after you are done, press `Ctrl+c`.




## Run a getML container

The [getML Docker images](https://hub.docker.com/r/getml/getml) are already configured to run the getML community edition. A [Docker](https://docs.docker.com/install/) container runs in a virtual environment and is the easiest way to set up a working demo environment.

```bash
docker pull getml/getml:latest  # Download latest stable image
docker run ...
```

[Read the docker install guide](packages/Docker.md){ .md-button .md-button--primary }


## Using versioned archives

In some scenarios, installing getML from an archive might be necessary. Refer to the guide for details.

[Read the archive install guide](packages/archive.md){ .md-button .md-button--primary }


# Your first prediction model
