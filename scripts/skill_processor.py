"""
Skill processor module for validating and normalizing skills.
"""
import logging
from pathlib import Path
from typing import Optional, Dict, List
import frontmatter


def validate_skill(skill_path: str) -> Dict[str, any]:
    """
    Validate a skill directory.

    Checks:
    - SKILL.md file exists
    - SKILL.md has valid frontmatter
    - Required fields present (name, description)

    Args:
        skill_path: Path to skill directory

    Returns:
        Dict with validation results:
        {
            'valid': bool,
            'errors': List[str],
            'warnings': List[str],
            'metadata': Dict or None
        }
    """
    result = {
        'valid': False,
        'errors': [],
        'warnings': [],
        'metadata': None
    }

    skill_dir = Path(skill_path)

    # Check if directory exists
    if not skill_dir.exists():
        result['errors'].append(f"Directory does not exist: {skill_path}")
        return result

    if not skill_dir.is_dir():
        result['errors'].append(f"Path is not a directory: {skill_path}")
        return result

    # Check for SKILL.md
    skill_md = skill_dir / 'SKILL.md'
    if not skill_md.exists():
        result['errors'].append(f"SKILL.md not found in {skill_path}")
        return result

    # Parse frontmatter
    try:
        metadata = parse_skill_frontmatter(str(skill_md))
        result['metadata'] = metadata

        # Check required fields
        if not metadata.get('name'):
            result['warnings'].append("Missing 'name' in frontmatter")

        if not metadata.get('description'):
            result['warnings'].append("Missing 'description' in frontmatter")

        # Check file size
        file_size = skill_md.stat().st_size
        if file_size == 0:
            result['errors'].append("SKILL.md is empty")
            return result
        elif file_size < 50:
            result['warnings'].append(f"SKILL.md is very small ({file_size} bytes)")

        # Validation passed
        result['valid'] = True

    except Exception as e:
        result['errors'].append(f"Failed to parse SKILL.md: {e}")

    return result


def parse_skill_frontmatter(skill_md_path: str) -> Dict:
    """
    Parse YAML frontmatter from SKILL.md file.

    Args:
        skill_md_path: Path to SKILL.md file

    Returns:
        Dict with frontmatter metadata
    """
    try:
        with open(skill_md_path, 'r', encoding='utf-8') as f:
            post = frontmatter.load(f)
            return dict(post.metadata)
    except Exception as e:
        logging.error(f"Failed to parse frontmatter from {skill_md_path}: {e}")
        return {}


def check_name_conflicts(
    target_name: str,
    base_dir: str
) -> Optional[str]:
    """
    Check if a skill folder name conflicts with existing directories.

    Args:
        target_name: Target folder name to check
        base_dir: Base directory to check in

    Returns:
        Conflicting path if exists, None otherwise
    """
    target_path = Path(base_dir) / target_name

    if target_path.exists():
        return str(target_path)

    return None


def get_existing_skills(base_dir: str) -> List[str]:
    """
    Get list of existing skill directory names.

    Args:
        base_dir: Base directory containing skills

    Returns:
        List of skill folder names
    """
    base_path = Path(base_dir)
    if not base_path.exists():
        return []

    skills = []
    for item in base_path.iterdir():
        if item.is_dir() and not item.name.startswith('.'):
            # Check if it's a skill (has SKILL.md)
            if (item / 'SKILL.md').exists():
                skills.append(item.name)

    return skills


def normalize_skill_metadata(
    skill_config: Dict,
    parsed_metadata: Optional[Dict] = None
) -> Dict:
    """
    Normalize skill metadata for marketplace entry.

    Combines config data with parsed frontmatter, preferring frontmatter
    when available.

    Args:
        skill_config: Skill configuration from config file
        parsed_metadata: Parsed frontmatter from SKILL.md (optional)

    Returns:
        Normalized metadata dict
    """
    metadata = {}

    # Start with config data
    metadata['name'] = skill_config.get('id')
    metadata['description'] = skill_config.get('description', '')
    metadata['category'] = skill_config.get('category', '')

    # Override with frontmatter if available
    if parsed_metadata:
        if parsed_metadata.get('name'):
            # Use frontmatter name if it exists
            pass  # We'll keep the id as name for consistency
        if parsed_metadata.get('description'):
            metadata['description'] = parsed_metadata['description']

    return metadata


def validate_all_skills(
    skills_dir: str,
    skill_names: Optional[List[str]] = None
) -> Dict[str, Dict]:
    """
    Validate multiple skills.

    Args:
        skills_dir: Base directory containing skills
        skill_names: List of specific skill names to validate (None = all)

    Returns:
        Dict mapping skill names to validation results
    """
    results = {}

    if skill_names is None:
        skill_names = get_existing_skills(skills_dir)

    for skill_name in skill_names:
        skill_path = Path(skills_dir) / skill_name
        results[skill_name] = validate_skill(str(skill_path))

    return results


def generate_validation_report(validation_results: Dict[str, Dict]) -> str:
    """
    Generate human-readable validation report.

    Args:
        validation_results: Dict of validation results from validate_all_skills

    Returns:
        Formatted report string
    """
    lines = []
    lines.append("=" * 70)
    lines.append("Skill Validation Report")
    lines.append("=" * 70)
    lines.append("")

    total = len(validation_results)
    valid = sum(1 for r in validation_results.values() if r['valid'])
    invalid = total - valid

    lines.append(f"Total skills: {total}")
    lines.append(f"Valid: {valid}")
    lines.append(f"Invalid: {invalid}")
    lines.append("")

    # Group by status
    valid_skills = []
    invalid_skills = []
    skills_with_warnings = []

    for skill_name, result in validation_results.items():
        if result['valid']:
            valid_skills.append(skill_name)
            if result['warnings']:
                skills_with_warnings.append((skill_name, result['warnings']))
        else:
            invalid_skills.append((skill_name, result['errors']))

    # Report invalid skills
    if invalid_skills:
        lines.append("INVALID SKILLS:")
        lines.append("-" * 70)
        for skill_name, errors in invalid_skills:
            lines.append(f"  {skill_name}:")
            for error in errors:
                lines.append(f"    ERROR: {error}")
        lines.append("")

    # Report warnings
    if skills_with_warnings:
        lines.append("SKILLS WITH WARNINGS:")
        lines.append("-" * 70)
        for skill_name, warnings in skills_with_warnings:
            lines.append(f"  {skill_name}:")
            for warning in warnings:
                lines.append(f"    WARNING: {warning}")
        lines.append("")

    # Report valid skills
    if valid_skills:
        lines.append("VALID SKILLS:")
        lines.append("-" * 70)
        for skill_name in sorted(valid_skills):
            lines.append(f"  ✓ {skill_name}")
        lines.append("")

    lines.append("=" * 70)

    return '\n'.join(lines)
