[](){#cli}
# Command Line Interface

!!! note

      You do not need to launch getML Engine with the command line if you installed getML Suite using `pip` on Linux. You can execute [getml.engine.launch()][getml.engine.launch] inside Python code to launch the Engine.

On Linux, getML Engine can also [installed and used via the command line interface (CLI)][separate-installation-of-engine] called `getML`.


Some parameters can be set via command line flags. If you do not explicitly set them,
the values from your *config.json* are taken instead. The *config.json* is located 
in `$HOME/.getML/getml-VERSION`. For [Enterprise edition][enterprise-benefits] users, 
the most elegant way to edit your config.json is via 
the configuration view in the getML [monitor][monitor]. Community edition users can edit 
the file via a text editor.

The help menu can also be displayed by passing the flag `-help` or `-h`. The default values displayed in the help menu are the values in the *config.json* (therefore, they are not hard-coded).

```
usage: ./getML <command> [<args>] or ./getML [<args>].
```

```
Possible commands are:
 run        Runs getML. Type "./getML -h" or "./getML run -h" to display the arguments. "run" is executed by default.
 install    Installs getML.
 stop       Stops a running instance of getML. Type "./getML stop -h" to display the arguments.
 uninstall  Uninstalls getML
 version    Prints the version of getML (getml-VERSION-ARCH-PLATFORM)
```

```
Usage of run:
  -allow-push-notifications
    	Whether you want to allow the getML monitor to send push notifications to your desktop. (default true)
  -allow-remote-ips
    	Whether you want to allow remote IPs to access the http-port.
  -home-directory string
    	The directory which should be treated as the home directory by getML. getML will create a hidden folder named '.getML' in said directory. This is where the binaries are installed, if the install process does not have root rights. (default "/root")
  -http-port int
    	The local port of the getML monitor. This port can only be accessed from your local computer, unless you set allow-remote-ips=True. (default 1709)
  -in-memory
    	Whether you want the Engine to process everything in memory. (default true)
  -install
    	Installs getML, even if it is already installed. (default true)
  -launch-browser
    	Whether you want to automatically launch your browser. (default true)
  -log
    	Whether you want the Engine log to appear in the command line. The Engine log also appears in the 'Log' page of the monitor.
  -project-directory string
    	The directory in which to store all of your projects. (default "/root/.getML/projects")
  -proxy-url string
    	The URL of any proxy server that that redirects to the getML monitor.
  -tcp-port int
    	Local TCP port which serves as the communication point for the Engine. This port can only be accessed from your local computer. (default 1711)
  -token string
    	The token used for authentication. Authentication is required when remote IPs are allowed to access the monitor. If authentication is required and no token is passed, a random hexcode will be generated as the token.
```
```
Usage of stop:
  -tcp-port int
      The TCP port of the getML instance you would like to stop. (default 1711)
```