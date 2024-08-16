"""
Script for automating the fetching and processing of Jupyter notebooks
from specified GitHub repositories, configured as a MkDocs hook.

This script is defined as a hook in 'mkdocs.yml' by:
    ...
        hooks:
        - docs/examples/get_notebooks.py
    ...

NOTE:
    Notebooks are only converted by mkdocs-jupyter and subsequently included
    in the rendered docs if the environment variable 'NOTEBOOKS_INCLUDE'
    is set to '*.ipynb' or similar.
    
    So, to include the notebooks in the build, start MkDocs with:
        NOTEBOOKS_INCLUDE='*.ipynb' mkdocs serve
        
    Alternatively, set the environment variable before running the serve command:
        export NOTEBOOKS_INCLUDE='*.ipynb'
        mkdocs serve

The script runs functions in the following order:

    on_startup():
        Hook that gets triggered when MkDocs starts.

    get_repo_attributes():
        Retrieves the list of repositories and their attributes from metadata files.

    process_repo():
        Manages the fetching of notebooks for each specified repository.

    fetch_from_github():
        Fetches notebooks from a specified GitHub repository and stores them in a target directory.
"""

import yaml
import logging
import subprocess
from pathlib import Path

log = logging.getLogger("mkdocs")
script_dir = Path(__file__).resolve().parent  # Path to this script


def get_repo_attributes(script_dir: Path) -> list[dict[str, str]]:
    """
    Get the list of repositories and their respective attributes from the metadata files.
    Steps:
        1. List all `.meta.yml` files within the `examples` directory.
        2. Read each metadata file and extract repository details from the `path_repository` key.
        3. Only include files that contain a `path_repository` key.

    Returns:
        list: A list of dictionaries containing the repository details:
            - repo_name: The name of the GitHub repository (e.g. getml/getml-community).
            - repo_branch: The branch of the GitHub repository (e.g. main).
            - repo_subdir: The subdirectory in the repository where the notebooks are located (if any).
            - target_dir: The subdirectory (relative to the script directory) where the notebooks should be stored.
    """
    repo_attributes = []
    
    for meta_file in script_dir.glob("**/.meta.yml"):
        meta_content = meta_file.read_text()
        meta = yaml.safe_load(meta_content)
        
        path_repository = meta.get("path_repository")
        if path_repository:
            # Parse the path_repository string
            parts = path_repository.split('/')
            if len(parts) >= 4:
                repo_name = '/'.join(parts[:2])  # e.g., "getml/getml-community"
                repo_branch = parts[3]  # e.g., "main" or "master"
                repo_subdir = '/'.join(parts[4:]) if len(parts) > 4 else ""  # e.g., "fastprop_benchmark" or ""
                target_dir = str(meta_file.parent) # Default target_dir to the parent directory of .meta.yml

                repo_details = {
                    "repo_name": repo_name,
                    "repo_branch": repo_branch,
                    "repo_subdir": repo_subdir,
                    "target_dir": target_dir
                }
                
                repo_attributes.append(repo_details)

    return repo_attributes
    
    
def is_any_notebook_present(target_dir: str) -> bool:
    """
    Check if notebooks are present in the examples directory.

    Returns:
        bool: True if the notebooks are present, False otherwise.
    """
    return any(Path(target_dir).glob("*.ipynb"))
    
def get_dir_depth(repo_subdir: str) -> int:
    """ 
    Calculate the depth of the directory structure to be extracted from the tarball.
    """
    # Default depth is 1 as GitHub tarballs include a top-level directory.
    dir_depth = 1
    # Add 1 if a single subdirectory is specified.
    dir_depth += 1 if repo_subdir else 0
    # Add the amount of any additional subdirectories there may be.
    dir_depth += repo_subdir.count("/")
    return dir_depth

def fetch_from_github(
    repo_name: str,
    repo_branch: str,
    repo_subdir: str,
    target_dir: str
) -> None:
    """
    Fetches notebooks from a GitHub repository and stores them locally.

    Steps:
        1. Check if notebooks are already present in their respective `target_dir`.
        2. If not: Fetch the tarball from the GitHub repository.
        3. Extract the tarball and store the notebooks in the examples directory.

    Args:
        repo_name: The name of the GitHub repository (e.g. getml/getml-community).
        repo_branch: The branch of the GitHub repository (e.g. main).
        repo_subdir: The subdirectory in the repository where the notebooks are located.
        target_dir: The subdirectory (relative to the script directory) where the notebooks should be stored.
    """
    
    log.info(f"Fetching notebooks from {repo_name} repository...")
    dir_depth = get_dir_depth(repo_subdir)
    
    command = (
        f"curl -L https://api.github.com/repos/{repo_name}/tarball/{repo_branch} | "
        f"tar --wildcards -xz -C {target_dir} --strip-components={dir_depth} "
        f"'*{repo_subdir}/*.ipynb'"
    )

    try:
        subprocess.run(command, shell=True, check=True)

    except subprocess.CalledProcessError as e:
        log.error(f"Fetching unsuccessful: {e}")
    except Exception as e:
        log.error(f"An unexpected error occurred: {type(e).__name__}: {e}")

    else:
        log.info(f"Notebooks fetched to {target_dir}")


def process_repo(
    repo_name: str,
    repo_branch: str,
    repo_subdir: str,
    target_dir: str
) -> None:
    """
    Process a repository by fetching the notebooks and generating the metadata file.
    """
    
    if not is_any_notebook_present(target_dir):
        fetch_from_github(
            repo_name=repo_name,
            repo_branch=repo_branch,
            repo_subdir=repo_subdir,
            target_dir=target_dir
        )


def on_startup(**kwargs) -> None:
    """
    Define the repositories to fetch the notebooks from and process them.

    References on hooks and events:
        https://www.mkdocs.org/user-guide/configuration/#hooks
        https://www.mkdocs.org/dev-guide/plugins/#events
    """

    repo_attributes = get_repo_attributes(script_dir)

    for repo in repo_attributes:
        process_repo(**repo)

if __name__ == "__main__":
    on_startup()