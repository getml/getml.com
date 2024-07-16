[](){#installation-linux}
# Install getML on Linux

This installation guide explains all necessary steps to install getML on Linux.
To download the getML suite, go to 

[https://www.getml.com/download](https://www.getml.com/download)

and click the download button. This will download a tarball containing everything you need to use getML: The [getML engine][engine], the [getML monitor][monitor], and the [Python API][python-api].

### System requirements

Your Linux should meet at least the following requirements to successfully install getML:

- **GLIBC** 2.17 or above (check by using `ldd --version`)
  
- If you are using **Fedora 30**, you need *libxcrypt-compat*. Install using `yum install libxcrypt-compat`.

- Python 3.7 or above must be installed on your machine. Furthermore, `numpy` and `pandas` are required dependencies for the getML Python API.

### Install and run the getML engine and monitor

The getML engine is the C++ backend of getML. It comes with a graphical user interface - the getML monitor - that runs in your browser. To install these components, do the following:

1. Extract the tarball using 
   `tar -xzvf getml-VERSION-linux.tar.gz`.

2. `cd` into the resulting folder. Then, type `./getML`.
   This will create a hidden folder called `.getML` in your home directory. If your computer has a desktop environment, you will also have a getML icon in your Applications menu. 
   
3. (optional) You can now install getML command-line interface (getML CLI). See below for further instructions. 
     
4. Open a browser and visit [http://localhost:1709/](http://localhost:1709/) (if launching getML did not point you there automatically). 

### Install the getML Python API

The Python API is a convenient way to interact with and to control the getML engine. There are two options to install the getML Python API:

#### From PyPI 

In a terminal, execute the following command to install the remote version from the Python Package Index:

```bash
pip install getml
```

### Install the getML CLI

getML comes with a [command-line interface][cli] (CLI) that lets you configure the most 
important parameters on startup. The CLI is a standalone Go-binary located in the downloaded bundle.

??? note
    Before you can use the CLI, you have to follow steps 1 and 2 of the installation 
    instructions above.
    
After deflating the tarball, you should find the `getML` binary in the resulting folder.

After you have started getML for the first time, you can move the `getML` binary anywhere you want. We recommend moving the `getML` binary to a location included in the `PATH` environment variable, such as `~/.local/bin`. You can inspect the content of the aforementioned variable in a shell using:

```bash
echo $PATH
```

and check if it can be properly found by executing:

```bash
which getML
```

If this returns the location you moved the binary to, you are ready to go.

For further help on how to use the CLI, just use `getML -h` or `getML -help`.

### Uninstall getML

To uninstall getML from your computer:

1. Remove the folder `.getML` from your home directory. To do so, open a terminal and enter the following command:

```bash
rm -r $HOME/.getML
```

3. Delete `getML` binary from wherever you have put it (if you have decided to install the getML CLI).

### Where to go next

The [Getting started guide][getting-started] provides an overview of the functionality of getML and a basic example of how to use the Python API. In order to get help or provide feedback, please contact our [support][support].
