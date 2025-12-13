"""
GitHub fetcher module for downloading skills from GitHub repositories.
"""
import os
import time
import logging
import tarfile
import io
from pathlib import Path
from typing import Optional, List, Dict
import requests


class GitHubFetcher:
    """Handle GitHub API interactions and file downloads."""

    def __init__(self, token: Optional[str] = None):
        """
        Initialize GitHub fetcher.

        Args:
            token: GitHub personal access token (optional, for rate limiting)
        """
        self.token = token or os.getenv('GITHUB_TOKEN')
        self.session = requests.Session()

        if self.token:
            self.session.headers.update({
                'Authorization': f'token {self.token}',
                'Accept': 'application/vnd.github.v3+json'
            })
        else:
            self.session.headers.update({
                'Accept': 'application/vnd.github.v3+json'
            })

        self.api_base = 'https://api.github.com'

    def check_rate_limit(self) -> Dict:
        """
        Check GitHub API rate limit status.

        Returns:
            Dict with rate limit info
        """
        try:
            response = self.session.get(f'{self.api_base}/rate_limit')
            response.raise_for_status()
            data = response.json()
            return data['rate']
        except Exception as e:
            logging.warning(f"Failed to check rate limit: {e}")
            return {}

    def wait_for_rate_limit_reset(self):
        """Wait until rate limit resets if approaching limit."""
        rate = self.check_rate_limit()
        if not rate:
            return

        remaining = rate.get('remaining', 100)
        reset_time = rate.get('reset', 0)

        if remaining < 10:
            wait_time = max(0, reset_time - time.time()) + 5
            logging.warning(
                f"Approaching rate limit ({remaining} remaining). "
                f"Waiting {wait_time:.0f} seconds..."
            )
            time.sleep(wait_time)

    def get_default_branch(self, owner: str, repo: str) -> str:
        """
        Get the default branch of a repository.

        Args:
            owner: Repository owner
            repo: Repository name

        Returns:
            Default branch name (e.g., 'main', 'master')
        """
        try:
            url = f'{self.api_base}/repos/{owner}/{repo}'
            response = self.session.get(url)
            response.raise_for_status()
            return response.json()['default_branch']
        except Exception as e:
            logging.warning(
                f"Failed to get default branch for {owner}/{repo}, "
                f"using 'main': {e}"
            )
            return 'main'

    def fetch_standalone_repo(
        self,
        owner: str,
        repo: str,
        branch: str,
        target_dir: str,
        exclude_patterns: Optional[List[str]] = None
    ) -> bool:
        """
        Fetch entire repository as tarball and extract.

        Args:
            owner: Repository owner
            repo: Repository name
            branch: Branch name
            target_dir: Target directory to extract to
            exclude_patterns: Patterns to exclude (e.g., '.git', '.github')

        Returns:
            True if successful, False otherwise
        """
        if exclude_patterns is None:
            exclude_patterns = ['.git', '.github', '__pycache__', '*.pyc']

        try:
            # Check rate limit
            self.wait_for_rate_limit_reset()

            # Download tarball
            tarball_url = f'https://github.com/{owner}/{repo}/archive/refs/heads/{branch}.tar.gz'
            logging.info(f"Downloading {owner}/{repo} from {tarball_url}")

            response = self.session.get(tarball_url, stream=True)
            response.raise_for_status()

            # Extract tarball
            target_path = Path(target_dir)
            target_path.mkdir(parents=True, exist_ok=True)

            with tarfile.open(fileobj=io.BytesIO(response.content), mode='r:gz') as tar:
                # Get the root directory name from tarball
                members = tar.getmembers()
                if not members:
                    logging.error(f"Empty tarball for {owner}/{repo}")
                    return False

                root_dir = members[0].name.split('/')[0]

                # Extract files, excluding patterns
                for member in members:
                    # Skip the root directory itself
                    if member.name == root_dir:
                        continue

                    # Check exclude patterns
                    should_exclude = False
                    for pattern in exclude_patterns:
                        if pattern in member.name:
                            should_exclude = True
                            break

                    if should_exclude:
                        continue

                    # Remove root directory from path
                    member.name = member.name[len(root_dir) + 1:]
                    if member.name:
                        tar.extract(member, target_path)

            logging.info(f"Successfully extracted {owner}/{repo} to {target_dir}")
            return True

        except Exception as e:
            logging.error(f"Failed to fetch standalone repo {owner}/{repo}: {e}")
            return False

    def fetch_subfolder(
        self,
        owner: str,
        repo: str,
        branch: str,
        subfolder_path: str,
        target_dir: str
    ) -> bool:
        """
        Fetch specific subdirectory from repository using Contents API.

        Args:
            owner: Repository owner
            repo: Repository name
            branch: Branch name
            subfolder_path: Path to subfolder in repository
            target_dir: Target directory to save files

        Returns:
            True if successful, False otherwise
        """
        try:
            # Check rate limit
            self.wait_for_rate_limit_reset()

            # Create target directory
            target_path = Path(target_dir)
            target_path.mkdir(parents=True, exist_ok=True)

            # Fetch contents recursively
            return self._fetch_contents_recursive(
                owner, repo, branch, subfolder_path, target_path
            )

        except Exception as e:
            logging.error(
                f"Failed to fetch subfolder {subfolder_path} from "
                f"{owner}/{repo}: {e}"
            )
            return False

    def _fetch_contents_recursive(
        self,
        owner: str,
        repo: str,
        branch: str,
        path: str,
        target_dir: Path
    ) -> bool:
        """
        Recursively fetch directory contents from GitHub.

        Args:
            owner: Repository owner
            repo: Repository name
            branch: Branch name
            path: Path in repository
            target_dir: Target directory

        Returns:
            True if successful
        """
        try:
            url = f'{self.api_base}/repos/{owner}/{repo}/contents/{path}?ref={branch}'
            response = self.session.get(url)
            response.raise_for_status()

            contents = response.json()
            if not isinstance(contents, list):
                contents = [contents]

            for item in contents:
                item_name = item['name']
                item_type = item['type']
                item_path = Path(target_dir) / item_name

                if item_type == 'file':
                    # Download file
                    self.wait_for_rate_limit_reset()
                    download_url = item['download_url']
                    file_response = self.session.get(download_url)
                    file_response.raise_for_status()

                    item_path.write_bytes(file_response.content)
                    logging.debug(f"Downloaded: {item_path}")

                elif item_type == 'dir':
                    # Create directory and recurse
                    item_path.mkdir(exist_ok=True)
                    subpath = f"{path}/{item_name}"
                    self._fetch_contents_recursive(
                        owner, repo, branch, subpath, item_path
                    )

            return True

        except Exception as e:
            logging.error(f"Failed to fetch contents at {path}: {e}")
            return False

    def fetch_skill(
        self,
        github_url: str,
        repo_type: str,
        target_folder: str,
        extraction_config: Dict
    ) -> bool:
        """
        Fetch skill based on repository type and configuration.

        Args:
            github_url: GitHub URL
            repo_type: Type of repository ('standalone', 'multi_skill')
            target_folder: Target folder name
            extraction_config: Extraction configuration dict

        Returns:
            True if successful, False otherwise
        """
        from utils import parse_github_url

        try:
            owner, repo, branch, subfolder_path = parse_github_url(github_url)

            # Get actual default branch if not specified
            if not subfolder_path:
                branch = self.get_default_branch(owner, repo)

            logging.info(
                f"Fetching {target_folder} from {owner}/{repo} "
                f"(branch: {branch}, path: {subfolder_path or 'root'})"
            )

            if repo_type == 'standalone' or not subfolder_path:
                # Fetch entire repository
                exclude_patterns = extraction_config.get(
                    'exclude_patterns',
                    ['.git', '.github', '__pycache__', '*.pyc']
                )
                return self.fetch_standalone_repo(
                    owner, repo, branch, target_folder, exclude_patterns
                )
            else:
                # Fetch specific subfolder
                return self.fetch_subfolder(
                    owner, repo, branch, subfolder_path, target_folder
                )

        except Exception as e:
            logging.error(f"Failed to fetch skill {target_folder}: {e}")
            return False
