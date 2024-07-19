
[](){#installation-linux}
Install [getML community edition](https://github.com/getml/getml-community) with Python's pip package manager.

```py
pip install getml
```
The will install both the [Python API][getml-suite-python-api] and the [engine][engine] on your Linux machine.


!!! enterprise-adm "Enterprise Edition"
    Need the highest models accuracy in commercial prediction applications and enterprise grade support?

    [Choose getML enterprise](../../enterprise/benefits.md){ .md-button }

    Once you have obtained the getML enterprise edition, you can install it as follows:

    - Install the [Python API][getml-suite-python-api]: `pip install getml`
    - Install the [engine][engine] by following [instructions for separate installation of it][separate-installation-of-engine] below. Start from step 2 and use the enterprise `tar` file you have been provided with.

[](){#separate-installation-of-engine}
### Separate installation of engine

In some cases it might be preferred to install the engine separately on Linux machines. For example, if you want to use the [enterprise edition](../../enterprise/benefits.md) of the engine.


Please execute the following commands, replacing `ARCH` with either `x64` or `arm64`, depending on your architecture.
If you are unsure, `x64` is probably the right choice.
You can also use `uname -m` to figure out the architecture.
If it says something like `aarch64` or `arm64`, you need to use [`arm64`](https://static.getml.com/download/1.5.0/getml-1.5.0-arm64-community-edition-linux.tar.gz), otherwise go with [`x64`](https://static.getml.com/download/1.5.0/getml-1.5.0-x64-community-edition-linux.tar.gz).

```bash
# 1. Download the tar file of the engine
wget https://static.getml.com/download/1.5.0/getml-1.5.0-ARCH-community-edition-linux.tar.gz

# 2. Extract the tar file
tar -xzf getml-1.5.0-ARCH-community-edition-linux.tar.gz

# 3. Change directory 
cd getml-1.5.0-ARCH-community-edition-linux

# 4. Install the engine
./getML install
```

The output of the `install` command will tell you where the engine has been installed.
It will look something like this:

```bash
getml@laptop src % ./getML install        
Installing getML...
Could not install into '/usr/local': mkdir /usr/local/getML: permission denied
Global installation failed, most likely due to missing root rights. Trying local installation instead.
Installing getML...
Successfully installed getML into '/Users/getml/.getML/getml-1.5.0-arm64-community-edition-linux'.
Installation successful. To be able to call 'getML' from anywhere, add the following path to PATH:
/home/getml/.getML/getml-1.5.0-arm64-community-edition-linux
```

To run the engine, execute:
```bash
./getML
```

If the engine was installed to the user home directory, you can add the installation directory to your PATH if you want to call the getML CLI from anywhere.

```bash
export PATH=$PATH:/path/to/getml-1.5.0-ARCH-community-edition-linux
```

To make the changes permanent, you will have to add the line to your `.bashrc` or `.bash_profile` file. 

