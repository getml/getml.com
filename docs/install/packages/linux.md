
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

In some cases, it might be preferred to install the Engine separately on Linux
using [CLI][cli]. For example, if you want to use the [Enterprise
edition][enterprise-benefits] of the Engine. You can download the current
release's package from the [download page][packge-download].

If you want to download getML from the command line, you can use the following
commands. Replace `<arch>` with either `amd64` or `arm64`, depending on your
architecture. You can use `uname -m` to figure out the architecture. If it
returns `aarch64` or `arm64`, you need to use `arm64`, otherwise go with
`amd64`.

```bash
curl -LO https://static.getml.com/download/<version>/getml-community-<version>-<arch>-linux.tar.gz

# If you want to check the hash:
# curl -LO https://static.getml.com/download/<version>/getml-community-<version>-<arch>-linux.tar.gz.sha256
# if [ "$(sha256sum getml-community-<version>-<arch>-linux.tar.gz) == $(cat getml-community-<version>-<arch>-linux.tar.gz.sha256)" ]; then echo "OK"; else echo "NOT OK"; fi

tar -xzf getml-community-<version>-<arch>-linux.tar.gz
getml-community-<version>-<arch>-linux/getML install
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

If a global installation is successful, getML is added to `/usr/local/bin` which
should be on already on `PATH` on every distribution. If the Engine was
installed to the user home directory, you can add the installation directory to
your `PATH` variable if you want to call the getML [CLI][cli] from anywhere.

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
