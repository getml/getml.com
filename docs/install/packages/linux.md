
[](){#installation-linux}
Install [getML Community edition](https://github.com/getml/getml-community) with Python's pip package manager.

```py
pip install getml
```
The will install both the [Python API][python-api-concepts] and the [Engine][engine-install] on your Linux machine. You are done.


!!! enterprise-adm "Enterprise Edition"
    Need the highest models accuracy in commercial prediction applications and enterprise grade support?

    [Choose getML Enterprise][enterprise-benefits]{ .md-button }

    Once you have obtained the getML Enterprise edition, you can install it as follows:

    - Install the [Python API][python-api-concepts]: `pip install getml`
    - Install the [Engine][engine-install] by following [instructions for separate installation of it][separate-installation-of-engine] below. Start from step 2 and use the enterprise `tar` file you have been provided with.

## Separate installation of Engine {#separate-installation-of-engine}

In some cases, it might be preferred to install the Engine separately on Linux using [CLI][cli]. For example, if you want to use the [Enterprise edition][enterprise-benefits] of the Engine.


Please execute the following commands, replacing `ARCH` with either `x64` or `arm64`, depending on your architecture.
If you are unsure, `x64` is probably the right choice.
You can also use `uname -m` to figure out the architecture.
If it says something like `aarch64` or `arm64`, you need to use [`arm64`](https://static.getml.com/download/1.5.0/getml-1.5.0-arm64-community-edition-linux.tar.gz), otherwise go with [`x64`](https://static.getml.com/download/1.5.0/getml-1.5.0-x64-community-edition-linux.tar.gz).

```bash
# 1. Download the tar file of the Engine
wget https://static.getml.com/download/1.5.0/getml-1.5.0-ARCH-community-edition-linux.tar.gz

# 2. Extract the tar file
tar -xzf getml-1.5.0-ARCH-community-edition-linux.tar.gz

# 3. Change directory 
cd getml-1.5.0-ARCH-community-edition-linux

# 4. Install the Engine using CLI
./getML install
```

The output of the `install` command will tell you where the Engine has been installed.
It will look something like this:

```bash
getml@laptop src % ./getML install        
Installing getML...
Could not install into '/usr/local': mkdir /usr/local/getML: permission denied
Global installation failed, most likely due to missing root rights. Trying local installation instead.
Installing getML...
Successfully installed getML into '/Users/getml/.getML/getml-1.5.0-arm64-community-edition-linux'.
Installation successful. To be able to call 'getML' from anywhere, add the following path to PATH:
/home/user/.getML/getml-1.5.0-arm64-community-edition-linux
```

### Launching the engine

To run the engine, execute:
```bash
./getML
```

If the Engine was installed to the user home directory, you can add the installation directory to your `PATH` variable if you want to call the getML [CLI][cli] from anywhere.

```bash
export PATH=$PATH:/path/to/getml-1.5.0-ARCH-community-edition-linux
```

To make the changes permanent, you will have to add the line to your `.bashrc` or `.bash_profile` file. 


## Where to go next

To get started with getML, you may check out:

- [User Guide][user-guide-index], which provides a comprehensive introduction to getML at varying levels of detail
- [Examples][examples-index], where we demonstrate practical examples inside Jupyter Notebooks