"""
Script for automating the fetching and processing of Jupyter notebooks
from specified GitHub repositories.

This script is defined as a hook in 'mkdocs.yml' by:
    ...
        hooks:
        - docs/examples/get_notebooks.py
    ...


NOTE:
    This script / hook is only executed if the environment variable 
    'NOTEBOOKS_INCLUDE' is set to '*.ipynb' or similar.
    
    So, to include the notebooks in the build, start mkdocs with:
        NOTEBOOKS_INCLUDE='*.ipynb' mkdocs serve
        
    or set the environment variable before running the serve command.
        export NOTEBOOKS_INCLUDE='*.ipynb'
        mkdocs serve


The script runs functions in the following order:

    on_startup():
        Hook, that defines the list of repositories.

    process_repo():
        Orchestrates the fetching of notebooks and the generation of metadata for a single repository.

    fetch_from_github():
        Fetches notebooks from the specified GitHub repository and stores them locally.

    gen_meta_yml():
        Generates a .meta.yml file for the notebooks in the specified repository.
"""

import logging
import subprocess
from pathlib import Path

log = logging.getLogger("mkdocs")
script_dir = Path(__file__).resolve().parent  # Path to this script


def gen_meta_yml(
    repo_name: str, repo_branch: str, repo_subdir: str, examples_subdir: str
) -> None:
    """Generates the metadata [.meta.yml file] for a repository folder within the examples directory.

    Args:
        repo_name: The name of the GitHub repository (e.g. getml/getml-community).
        repo_branch: The branch of the GitHub repository (e.g. main).
        repo_subdir: The subdirectory in the repository where the notebooks are located.
        examples_subdir: The subdirectory (relative to the script directory) where the notebooks should be stored.

    Returns:
        str: The metadata for the notebook.
    """

    meta_yml = \
f"""
path_repository: {repo_name}/blob/{repo_branch}{repo_subdir}
"""

    with open(script_dir / examples_subdir / ".meta.yml", "w") as f:
        f.write(meta_yml)


def fetch_from_github(
    repo_name: str,
    repo_branch: str,
    repo_subdir: str,
    examples_subdir: str,
    dir_depth: int,
) -> None:
    """
    Fetches notebooks from a GitHub repository and stores them locally.

    Steps:
        1. Fetch the tarball from the GitHub repository.
        2. Extract the tarball and store the notebooks in the examples directory.

    Condition:
        Check if the target directory exists. If it does not exist, create it.

    Args:
        repo_name: The name of the GitHub repository (e.g. getml/getml-community).
        repo_branch: The branch of the GitHub repository (e.g. main).
        repo_subdir: The subdirectory in the repository where the notebooks are located.
        examples_subdir: The subdirectory (relative to the script directory) where the notebooks should be stored.
        dir_depth: The depth of the subdirectory structure in the repository.
    """
    target_dir = script_dir / examples_subdir

    command = (
        f"curl -L https://api.github.com/repos/{repo_name}/tarball/{repo_branch} | "
        f"tar --wildcards -xz -C {target_dir} --strip-components={dir_depth} "
        f"'*{repo_subdir}/*.ipynb'"
    )

    if not target_dir.exists():
        log.info(f"Fetching notebooks from {repo_name} repository...")

        try:
            target_dir.mkdir(parents=True, exist_ok=False)
            subprocess.run(command, shell=True, check=True)

        except subprocess.CalledProcessError as e:
            log.error(f"Fetching unsuccessful: {e}")
        except Exception as e:
            log.error(f"An unexpected error occurred: {e}")

        else:
            log.info(f"Notebooks fetched to {target_dir}")


def process_repo(
    repo_name: str,
    repo_branch: str,
    repo_subdir: str,
    examples_subdir: str,
    dir_depth: int,
) -> None:
    """
    Process a repository by fetching the notebooks and generating the metadata file.
    """

    fetch_from_github(
        repo_name=repo_name,
        repo_branch=repo_branch,
        repo_subdir=repo_subdir,
        examples_subdir=examples_subdir,
        dir_depth=dir_depth,
    )
    gen_meta_yml(repo_name, repo_branch, repo_subdir, examples_subdir)


def on_startup(**kwargs) -> None:
    """
    Define the repositories to fetch the notebooks from and process them.

    References on hooks and events:
        https://www.mkdocs.org/user-guide/configuration/#hooks
        https://www.mkdocs.org/dev-guide/plugins/#events
    """

    repos = [
        {
            "repo_name": "getml/getml-community",
            "repo_branch": "main",
            "repo_subdir": "/demo-notebooks",
            "examples_subdir": "getml-community",
            "dir_depth": 2,
        },
        {
            "repo_name": "getml/getml-demo",
            "repo_branch": "master",
            "repo_subdir": "",
            "examples_subdir": "getml-demo",
            "dir_depth": 1,
        },
        {
            "repo_name": "getml/getml-demo",
            "repo_branch": "vertexai",
            "repo_subdir": "",
            "examples_subdir": "vertexai",
            "dir_depth": 1,
        },
    ]

    for repo in repos:
        process_repo(**repo)

    # TODO: Add yml for Benchmark nootebooks