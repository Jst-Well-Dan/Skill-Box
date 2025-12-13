"""
Marketplace updater module for managing marketplace.json.
"""
import json
import logging
from pathlib import Path
from typing import Dict, List, Optional
from jsonschema import validate, ValidationError


# Marketplace schema
MARKETPLACE_SCHEMA = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "required": ["name", "version", "description", "owner", "plugins"],
    "properties": {
        "name": {"type": "string"},
        "version": {"type": "string"},
        "description": {"type": "string"},
        "owner": {
            "type": "object",
            "required": ["name", "email"],
            "properties": {
                "name": {"type": "string"},
                "email": {"type": "string"}
            }
        },
        "plugins": {
            "type": "array",
            "items": {
                "type": "object",
                "required": ["name", "description", "source", "category"],
                "properties": {
                    "name": {"type": "string"},
                    "description": {"type": "string"},
                    "source": {"type": "string"},
                    "category": {"type": "string"},
                    "author": {
                        "type": "object",
                        "required": ["name"],
                        "properties": {
                            "name": {"type": "string"},
                            "github": {"type": "string"},
                            "url": {"type": "string"}
                        }
                    }
                }
            }
        }
    }
}


def load_marketplace(marketplace_path: str) -> Optional[Dict]:
    """
    Load and parse marketplace.json file.

    Args:
        marketplace_path: Path to marketplace.json

    Returns:
        Parsed marketplace data, or None on error
    """
    try:
        with open(marketplace_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        logging.info(f"Loaded marketplace from {marketplace_path}")
        return data
    except Exception as e:
        logging.error(f"Failed to load marketplace from {marketplace_path}: {e}")
        return None


def save_marketplace(marketplace_path: str, data: Dict, create_backup: bool = True) -> bool:
    """
    Save marketplace data to file.

    Args:
        marketplace_path: Path to marketplace.json
        data: Marketplace data
        create_backup: Whether to create backup before saving

    Returns:
        True if successful, False otherwise
    """
    try:
        from utils import backup_file

        # Create backup if requested
        if create_backup and Path(marketplace_path).exists():
            backup_file(marketplace_path)

        # Write to file with pretty formatting
        with open(marketplace_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
            f.write('\n')  # Add trailing newline

        logging.info(f"Saved marketplace to {marketplace_path}")
        return True
    except Exception as e:
        logging.error(f"Failed to save marketplace to {marketplace_path}: {e}")
        return False


def validate_marketplace_schema(data: Dict) -> bool:
    """
    Validate marketplace data against schema.

    Args:
        data: Marketplace data

    Returns:
        True if valid, False otherwise
    """
    try:
        validate(instance=data, schema=MARKETPLACE_SCHEMA)
        logging.info("Marketplace schema validation passed")
        return True
    except ValidationError as e:
        logging.error(f"Marketplace schema validation failed: {e.message}")
        return False
    except Exception as e:
        logging.error(f"Unexpected error during schema validation: {e}")
        return False


def create_marketplace_entry(
    skill_config: Dict,
    metadata: Optional[Dict] = None
) -> Dict:
    """
    Create a marketplace plugin entry.

    Args:
        skill_config: Skill configuration from config file
        metadata: Optional metadata from SKILL.md frontmatter

    Returns:
        Marketplace plugin entry dict
    """
    entry = {
        "name": skill_config['id'],
        "description": skill_config.get('description', ''),
        "source": f"./{skill_config['target_folder']}",
        "category": skill_config.get('category', 'development')
    }

    # Add author information if available in config
    if 'author' in skill_config:
        author_data = {"name": skill_config['author']}

        # Add GitHub username if available
        if 'github' in skill_config:
            author_data['github'] = skill_config['github']

        # Generate GitHub profile URL if github username is available
        if 'github' in skill_config:
            author_data['url'] = f"https://github.com/{skill_config['github']}"

        entry['author'] = author_data

    # Override with metadata if available
    if metadata:
        if metadata.get('description'):
            entry['description'] = metadata['description']

    return entry


def merge_plugins(
    existing_plugins: List[Dict],
    new_plugins: List[Dict]
) -> List[Dict]:
    """
    Merge existing and new plugin lists, deduplicating by name.

    Existing plugins take precedence over new ones with same name.

    Args:
        existing_plugins: Current plugins from marketplace
        new_plugins: New plugins to add

    Returns:
        Merged and deduplicated plugin list, sorted by name
    """
    # Create dict indexed by plugin name
    plugins_dict = {}

    # Add existing plugins first (they take precedence)
    for plugin in existing_plugins:
        name = plugin.get('name')
        if name:
            plugins_dict[name] = plugin

    # Add new plugins (skip if name already exists)
    added_count = 0
    skipped_count = 0
    for plugin in new_plugins:
        name = plugin.get('name')
        if name:
            if name in plugins_dict:
                logging.warning(f"Skipping duplicate plugin: {name}")
                skipped_count += 1
            else:
                plugins_dict[name] = plugin
                added_count += 1

    logging.info(
        f"Merged plugins: {len(existing_plugins)} existing, "
        f"{added_count} added, {skipped_count} skipped (duplicates)"
    )

    # Convert back to list and sort by name
    merged_plugins = sorted(plugins_dict.values(), key=lambda p: p.get('name', ''))

    return merged_plugins


def update_marketplace_with_skills(
    marketplace_path: str,
    skill_configs: List[Dict],
    skill_metadata: Dict[str, Dict]
) -> bool:
    """
    Update marketplace.json with new skills.

    Args:
        marketplace_path: Path to marketplace.json
        skill_configs: List of skill configurations
        skill_metadata: Dict mapping skill IDs to their metadata

    Returns:
        True if successful, False otherwise
    """
    try:
        # Load existing marketplace
        marketplace = load_marketplace(marketplace_path)
        if not marketplace:
            logging.error("Failed to load marketplace")
            return False

        # Get existing plugins
        existing_plugins = marketplace.get('plugins', [])
        logging.info(f"Found {len(existing_plugins)} existing plugins")

        # Create new plugin entries
        new_plugins = []
        for skill_config in skill_configs:
            skill_id = skill_config['id']
            metadata = skill_metadata.get(skill_id)

            entry = create_marketplace_entry(skill_config, metadata)
            new_plugins.append(entry)

        logging.info(f"Created {len(new_plugins)} new plugin entries")

        # Merge plugins
        merged_plugins = merge_plugins(existing_plugins, new_plugins)

        # Update marketplace
        marketplace['plugins'] = merged_plugins

        # Validate schema
        if not validate_marketplace_schema(marketplace):
            logging.error("Marketplace validation failed after update")
            return False

        # Save marketplace
        if not save_marketplace(marketplace_path, marketplace):
            logging.error("Failed to save updated marketplace")
            return False

        logging.info(
            f"Successfully updated marketplace: "
            f"{len(merged_plugins)} total plugins"
        )
        return True

    except Exception as e:
        logging.error(f"Failed to update marketplace: {e}")
        return False


def get_plugin_by_name(marketplace_path: str, plugin_name: str) -> Optional[Dict]:
    """
    Get a specific plugin by name from marketplace.

    Args:
        marketplace_path: Path to marketplace.json
        plugin_name: Plugin name to search for

    Returns:
        Plugin dict if found, None otherwise
    """
    marketplace = load_marketplace(marketplace_path)
    if not marketplace:
        return None

    plugins = marketplace.get('plugins', [])
    for plugin in plugins:
        if plugin.get('name') == plugin_name:
            return plugin

    return None


def list_marketplace_plugins(marketplace_path: str) -> List[str]:
    """
    Get list of all plugin names in marketplace.

    Args:
        marketplace_path: Path to marketplace.json

    Returns:
        List of plugin names
    """
    marketplace = load_marketplace(marketplace_path)
    if not marketplace:
        return []

    plugins = marketplace.get('plugins', [])
    return [p.get('name') for p in plugins if p.get('name')]
