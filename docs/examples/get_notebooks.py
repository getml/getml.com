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

import logging
import tarfile
from io import BytesIO
from pathlib import Path

import requests
import yaml

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
            - repo_name: The name of the GitHub repository (e.g., 'getml/getml-community').
            - repo_branch: The branch of the GitHub repository (e.g., 'main').
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
    Check if any Jupyter notebook files are present in the target directory.

    Args:
        target_dir: The directory to check for notebooks.

    Returns:
        bool: True if any '.ipynb' files are found in the target_dir, False otherwise.
    """
    return any(Path(target_dir).glob("*.ipynb"))
    

def fetch_from_github(
    repo_name: str,
    repo_branch: str,
    repo_subdir: str,
    target_dir: str
) -> None:
    """
    Fetch notebooks from a GitHub repository and store them locally.

    Steps:
        1. Construct the URL to download the tarball of the specified repository and branch.
        2. Fetch the tarball using the requests library.
        3. Open the tarball using the tarfile module.
        4. Iterate over the files in the tarball, adjusting paths to remove the top-level directory.
        5. Filter and extract only the '.ipynb' files located in the specified repo_subdir (if any).
        6. Extract the notebooks directly to the target_dir, maintaining the directory structure under repo_subdir.

    Args:
        repo_name: The name of the GitHub repository (e.g., 'getml/getml-community').
        repo_branch: The branch of the GitHub repository (e.g., 'main' or 'master').
        repo_subdir: The subdirectory in the repository where the notebooks are located.
        target_dir: The directory where the notebooks should be stored.
    """
    
    log.info(f"Fetching notebooks from {repo_name}[{repo_branch}] repository...")

    tarball_url = f"https://api.github.com/repos/{repo_name}/tarball/{repo_branch}"

    try:
        response = requests.get(tarball_url, stream=True)
        response.raise_for_status()

        tar_bytes = BytesIO(response.content)

        with tarfile.open(fileobj=tar_bytes, mode="r:gz") as tar:
            members = tar.getmembers()
            for member in members:
                # member.name is the path inside the tarball
                # The first component is the top-level directory
                path_parts = member.name.split('/')
                # Remove the top-level directory
                relative_path = '/'.join(path_parts[1:])
                # If repo_subdir is specified, check if the relative_path starts with repo_subdir
                if repo_subdir:
                    if not relative_path.startswith(repo_subdir + '/'):
                        continue
                    # After matching the repo_subdir, get the path under repo_subdir
                    sub_path = relative_path[len(repo_subdir)+1:]
                else:
                    sub_path = relative_path

                if sub_path.endswith('.ipynb'):
                    # Extract the member to target_dir
                    # Adjust the member's name to remove the leading directories
                    member.name = sub_path  # Set the name to the relative path under repo_subdir
                    tar.extract(member, path=target_dir)

    except requests.HTTPError as e:
        log.error(f"HTTP error occurred: {e}")
    except Exception as e:
        log.error(f"An error occurred: {e}")
    else:
        log.info(f"Notebooks fetched to {target_dir}")
    


def process_repo(
    repo_name: str,
    repo_branch: str,
    repo_subdir: str,
    target_dir: str
) -> None:
    """
    Process a repository by fetching the notebooks.

    Steps:
        1. Check if notebooks are already present in the target directory.
        2. If not, call fetch_from_github() to download and extract the notebooks.

    Args:
        repo_name: The name of the GitHub repository.
        repo_branch: The branch of the repository.
        repo_subdir: The subdirectory in the repository to look for notebooks.
        target_dir: The local directory to store the fetched notebooks.
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
    Hook function called at MkDocs startup.

    Retrieves repository attributes and processes each repository.

    References on hooks and events:
        https://www.mkdocs.org/user-guide/configuration/#hooks
        https://www.mkdocs.org/dev-guide/plugins/#events
    """

    repo_attributes = get_repo_attributes(script_dir)

    for repo in repo_attributes:
        process_repo(**repo)

if __name__ == "__main__":
    on_startup()
