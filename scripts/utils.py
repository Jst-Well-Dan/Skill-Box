"""
Utility functions for fetching external Claude skills.
"""
import re
import logging
import shutil
from pathlib import Path
from urllib.parse import urlparse
from typing import Optional, Tuple


def setup_logging(log_file: str = "fetch_skills.log", level: int = logging.INFO):
    """
    Setup logging configuration with both file and console handlers.

    Args:
        log_file: Path to log file
        level: Logging level
    """
    # Create formatters
    formatter = logging.Formatter(
        '%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    # Setup file handler
    file_handler = logging.FileHandler(log_file, encoding='utf-8')
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    # Setup console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(level)
    console_handler.setFormatter(formatter)

    # Configure root logger
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger


def to_kebab_case(name: str) -> str:
    """
    Convert a string to kebab-case.

    Rules:
    1. Convert to lowercase
    2. Replace spaces with hyphens
    3. Replace underscores with hyphens
    4. Remove special characters (except hyphens)
    5. Collapse multiple hyphens to single
    6. Strip leading/trailing hyphens

    Examples:
        "Markdown to EPUB Converter" → "markdown-to-epub-converter"
        "csv_data_summarizer_claude_skill" → "csv-data-summarizer-claude-skill"
        "iOS Simulator" → "ios-simulator"
        "D3.js Visualization" → "d3js-visualization"

    Args:
        name: String to convert

    Returns:
        Kebab-case string
    """
    # Convert to lowercase
    name = name.lower()

    # Replace spaces and underscores with hyphens
    name = name.replace(' ', '-').replace('_', '-')

    # Remove special characters except hyphens and alphanumerics
    name = re.sub(r'[^a-z0-9-]', '', name)

    # Collapse multiple hyphens to single
    name = re.sub(r'-+', '-', name)

    # Strip leading/trailing hyphens
    name = name.strip('-')

    return name


def parse_github_url(url: str) -> Tuple[str, str, str, Optional[str]]:
    """
    Parse GitHub URL to extract owner, repo, branch, and path.

    Examples:
        "https://github.com/smerchek/claude-epub-skill"
        → ("smerchek", "claude-epub-skill", "main", None)

        "https://github.com/obra/superpowers/tree/main/skills/brainstorming"
        → ("obra", "superpowers", "main", "skills/brainstorming")

    Args:
        url: GitHub URL

    Returns:
        Tuple of (owner, repo, branch, path)
    """
    parsed = urlparse(url)
    path_parts = [p for p in parsed.path.split('/') if p]

    if len(path_parts) < 2:
        raise ValueError(f"Invalid GitHub URL: {url}")

    owner = path_parts[0]
    repo = path_parts[1]

    # Default branch (will be determined by API if not specified)
    branch = "main"
    subfolder_path = None

    # Check if URL contains tree/branch/path structure
    if len(path_parts) > 3 and path_parts[2] == "tree":
        branch = path_parts[3]
        if len(path_parts) > 4:
            subfolder_path = '/'.join(path_parts[4:])

    return owner, repo, branch, subfolder_path


def backup_file(file_path: str) -> Optional[str]:
    """
    Create a backup of a file.

    Args:
        file_path: Path to file to backup

    Returns:
        Path to backup file, or None if file doesn't exist
    """
    path = Path(file_path)
    if not path.exists():
        return None

    backup_path = path.with_suffix(path.suffix + '.backup')
    shutil.copy2(path, backup_path)
    logging.info(f"Created backup: {backup_path}")

    return str(backup_path)


def create_directory(path: str) -> bool:
    """
    Create a directory if it doesn't exist.

    Args:
        path: Directory path to create

    Returns:
        True if created or already exists, False on error
    """
    try:
        Path(path).mkdir(parents=True, exist_ok=True)
        return True
    except Exception as e:
        logging.error(f"Failed to create directory {path}: {e}")
        return False


def remove_directory(path: str, ignore_errors: bool = False) -> bool:
    """
    Remove a directory and all its contents.

    Args:
        path: Directory path to remove
        ignore_errors: Whether to ignore errors

    Returns:
        True if removed successfully, False otherwise
    """
    try:
        dir_path = Path(path)
        if dir_path.exists():
            shutil.rmtree(dir_path, ignore_errors=ignore_errors)
            logging.debug(f"Removed directory: {path}")
        return True
    except Exception as e:
        logging.error(f"Failed to remove directory {path}: {e}")
        return False
