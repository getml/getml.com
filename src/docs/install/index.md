

# Installation 

GetML is available for Python 3.8 to 3.12 and supported on the following 64-bit systems and architectures:

- Ubuntu 16.04 or later (amd64/arm)
- macOS 10.12.6 or later (amd64/arm)
- Windows 10 19044 or higher (amd64)

From the [getML suite][getml-suite], the same [Python API][getml-suite-python-api] is utilized by our community and enterprise versions.

## Install getML community edition

Download the getML community edition to get started with the most advanced software for relational learning.

### Linux

Use Python's `pip` package manager to install both the [Python API][getml-suite-python-api] and the [engine][engine] on your Linux machine.

[Read the Linux install guide](packages/linux.md){ .md-button .md-button--primary }

### macOS, Windows & Linux

Setup a Docker container to run the [engine][engine]. Install [Python API][getml-suite-python-api] with `pip`. 

[Read the Docker install guide](packages/Docker.md){ .md-button .md-button--primary }

<!-- ## Run a getML container

The [getML Docker images](https://hub.docker.com/r/getml/getml) are already configured to run the getML community edition. A [Docker](https://docs.docker.com/install/) container runs in a virtual environment and is the easiest way to set up a working demo environment.

```bash
docker pull getml/getml:latest  # Download latest stable image
docker run ...
``` -->

### From source

Install the Python API from its source files.

[Read the API install guide](source/python-api.md){ .md-button .md-button--primary }

Build engine and the API from the source.

[Read the engine & API build guide](source/build.md){ .md-button .md-button--primary }



### Using versioned archives

In some scenarios, installing getML from an archive might be necessary. Refer to the guide for details.

[Read the archive install guide](packages/archive.md){ .md-button .md-button--primary }



## Install getML Enterprise

Need the highest models accuracy in commercial prediction applications and enterprise grade support?

[Choose getML enterprise](/enterprise/benefits){ .md-button }

Once you have downloaded the [trial version](/enterprise/book-demo) or [purchased the license](https://www.getml.com/contact) of getML enterprise edition, you can proceed as follows:

- Install the [Python API][getml-suite-python-api]: `pip install getml`
- Install the [engine][engine] by following [instructions for separate installation of it][separate-installation-of-engine]. Start from step 2 and use the `tar` file you have been provided with.