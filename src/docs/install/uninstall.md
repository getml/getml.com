# Uninstall

## Python API (all platforms)

!!! warning "Project data might be deleted"

    If you have not [installed the engine separately][separate-installation-of-engine] and have not set the home directory to a custom location on the engine launch, projects data will be deleted when you uninstall the Python API.

To uninstall the Python API, execute the following command in a terminal:

```bash
pip uninstall getml
```

## Linux 

!!! warning "Project data might be deleted"

    If you have not set the home directory to a custom location on the engine launch, projects data will be deleted when you remove the `.getML` directory.

You will have to remove the folder `.getML` from your home directory. In a terminal, execute: 
```bash
rm -r $HOME/.getML
```

## Docker

To remove the resources defined in the `docker-compose.yml` file, you can follow these steps:


### Docker Image

Remove the Docker image `getml/getml` from your local Docker repository as follows:

```sh
docker rmi getml/getml
```

Note that if there are any containers using this image, you must remove those containers first.

### Named Volumes

Remove the `getml` volume as follows:

```sh
docker volume rm getml
```

Ensure that the volume is not in use by any other containers.

### `getml` directory

Remove your local directory `getml` as follows:

!!! warning "Project data will be deleted"

    Your projects data will be deleted when you delete the `getml` directory.

```bash
rm -r getml
```