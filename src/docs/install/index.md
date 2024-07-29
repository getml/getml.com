# Installation
[](){#installation-index .page-pointer}

getML is a software suite for automated feature engineering on relational data and time series. It enables you to complete your data science projects in a fraction of their usual time and with better results.

getML is available for Python 3.8 to 3.12 and supported on the following 64-bit systems and architectures:

- Linux (amd64/arm) with glibc 2.28 or above (also via docker)
- macOS (amd64/arm) via docker
- Windows (amd64/arm) via docker

The [getML suite][getml-suite] comprises of [Python API][getml-suite-python-api], [engine][] and [monitor][]. The monitor is shipped along with the engine.

Both our [community](https://github.com/getml/getml-community) and [enterprise](../enterprise/benefits.md) editions use the same Python API.


## Linux

Use Python's `pip` package manager to install both the [Python API][getml-suite-python-api] and the [engine][].

[Read the Linux install guide](packages/linux.md){ .md-button .md-button--primary }

## macOS, Windows & Linux

Setup a Docker container to run the [engine][engine]. Install the [Python API][getml-suite-python-api] with `pip`.

[Read the Docker install guide](packages/Docker.md){ .md-button .md-button--primary }


## From source

Install the Python API from source.

[Read the API install guide](source/python-api.md){ .md-button .md-button--primary }

Build engine and the API from source.

[Read the engine & API build guide](source/build.md){ .md-button .md-button--primary }



## Using versioned archives

In some scenarios, installing getML from an archive might be necessary.

[Read the archive install guide](packages/archive.md){ .md-button .md-button--primary }


[test][installation-index]
