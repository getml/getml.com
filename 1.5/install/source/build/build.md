
[](){#compiling-from-source}

Because getML is complex software, we use [Docker](https://www.docker.com/) for our build environment. If you want to compile our Community edition from source, you can start with cloning its repository:

```bash
git clone https://github.com/getml/getml-community.git
```

We provide a set of wrappers to ease local development. They are located inside the `bin` directory of the repository. You can use them with the `getml` command and the `build` subcommand:

```bash
./bin/getml

Usage:
    getml <subcommand> [options]

Subcommands:
    build   Build utilities
    help    Show help (this message)

Options:
    -h      Show help (this message)
```

## Subcommand `build` 

The `build` subcommand is the entry point for building getML from source. For details about the build process, see [Directly Interacting with Bake](#directly-interacting-with-bake) below.

``` bash
getml build wrapper

Usage:
  build <subcommand> [options]

Subcommands:
  [a]ll       Build all (whole package, [p]ackage + [py]thon API + tar+gz [ar]chive)
  [c]li       Build CLI
  [e]ngine    Build Engine
  [p]ackage   Export runnable [e]ngine + [c]li package
  [py]thon    Package Python API
  [ar]chive   Create tar.gz archive of [p]ackage

Options:
  -b <args>   Specify build args (-b KEY=VALUE); passed to docker build
  -h          Show help (this message)
  -o <path>   Set output path (default: build); passed to docker build
```

Most of the time you probably want to build the (C++) Engine:

```bash
./bin/getml build engine
```

If you are calling `getml build package`, all build artifacts will be packaged inside the specified output folder. With `archive`, a compressed tarball (`getml-<version>-<arch>-linux.tar.gz`) will be created inside the folder.

### Build options

#### `-b <args>`: Build args 
These are [build arguments](https://docs.docker.com/build/guide/build-args/) passed to `docker build`. Build args can be provided as key-value pairs. The following build args are supported:

- `VERSION`: the build version (default: the version specified in the `VERSION` file, present in the root of [getml community repository](https://github.com/getml/getml-community))
- `NJOBS`: the number of threads to use for each compilation step

#### `-h`: Show help
Show the help screen

#### `-o <path>`: Output folder
The [output folder](https://docs.docker.com/build/exporters/) used by Docker's export backend

## Directly Interacting with Bake
The build pipeline is based on multi-stage Docker builds. There are two `Dockerfile`s:

- One for CLI, wheel, and packaging located in the [repository](https://github.com/getml/getml-community)'s root:
  `./Dockerfile`
- One related to the Engine and its dependencies located in the [repository](https://github.com/getml/getml-community)'s `src/engine` subfolder:
  `./src/engine/Dockerfile`

As the second `Dockerfile` is a dependency for the first, we use [bake](https://docs.docker.com/build/bake/) to orchestrate the builds. The bake file (`./docker-bake.hcl`) holds definitions for all build targets and ensures the appropriate build contexts are set.

If you want to interact with Docker directly, you can do so by calling `docker buildx bake`:

``` bash
VERSION=1.5.0 docker buildx bake engine
```

If you want to override build-args, you can do so per build stage via [bake's `--set` overrides](https://docs.docker.com/reference/cli/docker/buildx/bake/#set):

``` bash
docker buildx bake engine --set engine.args.VERSION=1.5.0
```

This way, you can also override some of a target's [default attributes](https://docs.docker.com/reference/cli/docker/buildx/bake/#set):

``` bash
docker buildx bake engine --set engine.output=out
```
