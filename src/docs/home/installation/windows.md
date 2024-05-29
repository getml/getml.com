[](){#installation-windows}
# Install getML on macOS/Windows/Docker

getML for Docker is the recommended way of running getML on Windows and macOS. However, it can also be used on Linux for a more "out-of-the-box" experience.

This installation guide explains all necessary steps to install getML on Docker. To download the getML suite, go to 

[https://www.getml.com/download](https://www.getml.com/download)

and click the download button. This will download a ZIP archive containing everything you need to use getML for Docker.

## System Requirements

Your system should meet the following requirements to successfully install getML for Docker:

- [Docker](https://www.docker.com/). If you are on Linux, make sure that you can run docker without root rights/sudo.
- [Git Bash](https://gitforwindows.org/). This is pre-installed on Linux and macOS. For Windows users, we recommend.
- [OpenSSL](https://www.openssl.org/). This should be pre-installed on most systems as well.

## Setup and Run getML for Docker

1. Make sure that Docker is running (more precisely, the Docker daemon).
2. Unzip `getml-X.X.X-docker.zip`, where `X.X.X` is a placeholder for the version number.
3. Execute `setup.sh`. This will run the Dockerfile and set up your Docker image. It will also create a Docker volume called 'getml'. On Windows, you can just click on `setup.sh`.

      On macOS and Linux, do the following:
   
      ```bash
      cd getml-X.X.X-docker
      bash setup.sh # or ./setup.sh
      ```
      
      (Please make sure that you actually `cd` into that directory, otherwise `setup.sh` will not find the Dockerfile.)

4. Execute `run.sh`. This will run the Docker image.

On Windows, you can just click on `run.sh`.

On macOS and Linux, do the following:

```bash
cd getml-X.X.X-docker
bash run.sh # or ./run.sh
```

## Uninstall getML

To uninstall getML for Docker, execute `uninstall.sh`. On Windows, you can just click on `uninstall.sh`.

On macOS and Linux, do the following:

```bash
cd getml-X.X.X-docker
bash uninstall.sh # or ./uninstall.sh
```
## Where to Go Next

The [Getting started guide][getting-started] provides an overview of the functionality of getML and a basic example of how to use the Python API. In order to get help or provide feedback, please contact our [support][support].
