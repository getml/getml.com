## Python API <a name="deinstallation-python-api"></a>

!!! warning "Project data might be deleted"

    If you have not installed the engine separately and have not set the home directory to a custom location on engine launch, the project data will be deleted when you uninstall the Python API.

To uninstall the Python API, execute the following command in a terminal:

```bash
pip uninstall getml
```

## Linux <a name="deinstallation-linux"></a>

!!! warning "Project data might be deleted"

    If you have not set the home directory to a custom location on engine launch, the project data will be deleted when you remove the `.getML` directory.

You will have to remove the folder `.getML` from your home directory. In a terminal, execute: 
```bash
rm -r $HOME/.getML
```