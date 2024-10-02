
[](){#installation-linux}
Install [getML Community edition](https://github.com/getml/getml-community) with Python's pip package manager.

```py
pip install getml
```
This will install both the [Python API][python-api-concepts] and the [Engine][engine-concepts] on your Linux machine. And you are done.

!!! enterprise-adm "Enterprise Edition"
    Need the highest models accuracy in commercial prediction applications and enterprise grade support?

    [Choose getML Enterprise][enterprise-benefits]{ .md-button }

    Once you have obtained the getML Enterprise edition, you can install it as follows:

    - Install the [Python API][python-api-concepts]: `pip install getml`
    - Install the [Engine][engine-concepts] by following [instructions for separate installation of it][separate-installation-of-engine] below. Start from step 2 and use the enterprise `tar` file you have been provided with.

## Separate installation of Engine {#separate-installation-of-engine}

In some cases, it might be preferable to install the Engine separately on Linux
using the [CLI][cli], for example, if you just want to run getML in a dedicated
process. You can download the current release's Community edition package from
the [download page][package-download]. Additionally, the [getML Enterprise
edition][enterprise-benefits] is distributed as a separate package and also needs 
to be installed this way.

If you want to download getML from the command line, you can use the following
commands. Replace `<arch>` with either `amd64` or `arm64`, depending on your
architecture. You can use `uname -m` to figure out the architecture. If it
returns `aarch64` or `arm64`, you need to use `arm64`, otherwise go with
`amd64`.

```bash
curl -LO https://static.getml.com/download/<version>/getml-community-<version>-<arch>-linux.tar.gz

# If you want to check the hash:
# curl -LO https://static.getml.com/download/<version>/getml-community-<version>-<arch>-linux.tar.gz.sha256
# if [ "$(sha256sum getml-community-<version>-<arch>-linux.tar.gz)" == "$(cat getml-community-<version>-<arch>-linux.tar.gz.sha256)" ]; then echo "OK"; else echo "NOT OK"; fi

tar -xzf getml-community-<version>-<arch>-linux.tar.gz
cd getml-community-<version>-<arch>-linux
./getML install
```

The output of the `install` command will tell you where the Engine has been installed.
It will look something like this:

```bash
$ src % ./getML install
Installing getML...
Could not install into '/usr/local': mkdir /usr/local/getML: permission denied
Global installation failed, most likely due to missing root rights. Trying local installation instead.
Installing getML...
Successfully installed getML into '/home/user/getml/.getML/getml-1.5.0-arm64-community-edition-linux'.
Installation successful. To be able to call 'getML' from anywhere, add the following path to PATH:
/home/user/.getML/getml-1.5.0-arm64-community-edition-linux
```

### Launching the engine

To run the engine, execute:
```bash
./getML
```

If getML was installed globally, the `getML` executable is placed in the
directory `/usr/local/bin`. This directory is typically included in the `PATH`
environment variable on most major Linux distributions, so you should be able to
run `getML` from any terminal session without any additional configuration.

However, if the getML Engine was installed to your user's home directory rather
than globally, it's stored in a location that isn't automatically included in
the `PATH`. In this case, you can add the installation directory to your `PATH`
environment variable to be able to call the getML CLI from any terminal session.

```bash
export PATH=$PATH:/path/to/getml-1.5.0-ARCH-community-edition-linux
```

To make the changes permanent, you will have to add the line to your `.bashrc` or `.bash_profile` file. 

Afterwards you can call `getML` from anywhere as usual:
```bash
getML
```

## Where to go next

To get started with getML, you may check out:

- [User Guide][user-guide-index], which provides a comprehensive introduction to getML at varying levels of detail
- [Examples][examples-index], where we demonstrate practical examples inside Jupyter Notebooks
