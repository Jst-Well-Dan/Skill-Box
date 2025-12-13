#!/usr/bin/env python3
"""
Skill Scanner and Marketplace Updater

Automatically scans all skill directories in the project, validates them,
and updates marketplace.json with any new or modified skills.

Usage:
    python scripts/scan_and_update_marketplace.py [options]

Options:
    --check         Only check skills, don't update marketplace
    --dry-run       Show what would be changed without writing
    --verbose       Show detailed output
    --force         Force update even if no changes detected
    --category CAT  Only scan a specific category
"""

import argparse
import json
import logging
import os
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import frontmatter

# Project root directory
SCRIPT_DIR = Path(__file__).parent.resolve()
PROJECT_ROOT = SCRIPT_DIR.parent
MARKETPLACE_PATH = PROJECT_ROOT / '.claude-plugin' / 'marketplace.json'

# Categories to scan (directory names)
SKILL_CATEGORIES = [
    'business-marketing',
    'code-development',
    'content-creation',
    'creative-media',
    'data-analysis',
    'learning-research',
    'office-documents',
    'productivity-organization',
]

# Default author for skills without explicit author
DEFAULT_AUTHOR = {
    "name": "Jst-Well-Dan",
    "url": "https://github.com/Jst-Well-Dan/claude-skills-vault"
}


class SkillScanner:
    """Scans and validates skill directories."""

    def __init__(self, verbose: bool = False):
        self.verbose = verbose
        self.setup_logging()

    def setup_logging(self):
        """Configure logging based on verbosity."""
        level = logging.DEBUG if self.verbose else logging.INFO
        logging.basicConfig(
            level=level,
            format='%(levelname)s: %(message)s'
        )
        self.logger = logging.getLogger(__name__)

    def scan_all_skills(self, categories: Optional[List[str]] = None) -> Dict[str, Dict]:
        """
        Scan all skill directories and collect their metadata.

        Args:
            categories: Optional list of specific categories to scan

        Returns:
            Dict mapping skill path to skill info
        """
        skills = {}
        scan_categories = categories or SKILL_CATEGORIES

        for category in scan_categories:
            category_path = PROJECT_ROOT / category
            if not category_path.exists():
                self.logger.warning(f"Category directory not found: {category}")
                continue

            # Scan all subdirectories in this category
            for item in category_path.iterdir():
                if item.is_dir() and not item.name.startswith('.'):
                    skill_md = item / 'SKILL.md'
                    if skill_md.exists():
                        skill_info = self.parse_skill(item, category)
                        if skill_info:
                            rel_path = f"./{category}/{item.name}"
                            skills[rel_path] = skill_info
                    else:
                        self.logger.debug(f"No SKILL.md in {item}")

        return skills

    def parse_skill(self, skill_dir: Path, category: str) -> Optional[Dict]:
        """
        Parse a single skill directory.

        Args:
            skill_dir: Path to skill directory
            category: Category name

        Returns:
            Skill info dict or None if invalid
        """
        skill_md = skill_dir / 'SKILL.md'

        try:
            with open(skill_md, 'r', encoding='utf-8') as f:
                post = frontmatter.load(f)

            metadata = dict(post.metadata)
            content = post.content

            # Extract name (required)
            name = metadata.get('name', skill_dir.name)

            # Extract description (required)
            description = metadata.get('description', '')
            if not description:
                # Try to extract from content (first paragraph after title)
                lines = content.strip().split('\n')
                for line in lines:
                    line = line.strip()
                    if line and not line.startswith('#'):
                        description = line[:500]  # Limit length
                        break

            # Extract author info
            author = self.extract_author(metadata)

            skill_info = {
                'name': name,
                'description': description,
                'category': category,
                'source': f"./{category}/{skill_dir.name}",
                'path': str(skill_dir),
                'has_scripts': (skill_dir / 'scripts').exists(),
                'has_references': (skill_dir / 'references').exists(),
                'has_assets': (skill_dir / 'assets').exists(),
            }

            if author:
                skill_info['author'] = author

            return skill_info

        except Exception as e:
            self.logger.error(f"Failed to parse {skill_md}: {e}")
            return None

    def extract_author(self, metadata: Dict) -> Dict:
        """Extract author information from metadata, use default if not set."""
        author = metadata.get('author')

        if isinstance(author, str):
            return {"name": author}
        elif isinstance(author, dict):
            # Only keep 'name' and 'url', remove 'github' if present
            result = {"name": author.get("name", "")}
            if author.get("url"):
                result["url"] = author["url"]
            if result.get("name"):
                return result

        # Check for GitHub URL to infer author
        github_url = metadata.get('github_url', '')
        if 'github.com/' in github_url:
            parts = github_url.split('github.com/')[1].split('/')
            if parts:
                github_user = parts[0]
                return {
                    "name": github_user,
                    "url": f"https://github.com/{github_user}"
                }

        # Return default author if no author specified
        return DEFAULT_AUTHOR.copy()

    def validate_skill(self, skill_info: Dict) -> Tuple[bool, List[str], List[str]]:
        """
        Validate a skill's metadata.

        Returns:
            Tuple of (is_valid, errors, warnings)
        """
        errors = []
        warnings = []

        # Check required fields
        if not skill_info.get('name'):
            errors.append("Missing 'name' field")

        if not skill_info.get('description'):
            errors.append("Missing 'description' field")
        elif len(skill_info['description']) < 20:
            warnings.append("Description is very short (< 20 chars)")
        elif len(skill_info['description']) > 1000:
            warnings.append("Description is very long (> 1000 chars)")

        if not skill_info.get('category'):
            errors.append("Missing 'category' field")

        # Check path exists
        path = skill_info.get('path')
        if path and not Path(path).exists():
            errors.append(f"Skill directory not found: {path}")

        is_valid = len(errors) == 0
        return is_valid, errors, warnings


class MarketplaceUpdater:
    """Updates marketplace.json with skill information."""

    def __init__(self, marketplace_path: Path, verbose: bool = False):
        self.marketplace_path = marketplace_path
        self.verbose = verbose
        self.logger = logging.getLogger(__name__)

    def load_marketplace(self) -> Optional[Dict]:
        """Load existing marketplace.json."""
        try:
            with open(self.marketplace_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            self.logger.error(f"Failed to load marketplace: {e}")
            return None

    def save_marketplace(self, data: Dict, backup: bool = True) -> bool:
        """Save marketplace.json with optional backup."""
        try:
            # Create backup
            if backup and self.marketplace_path.exists():
                backup_path = self.marketplace_path.with_suffix('.json.bak')
                with open(self.marketplace_path, 'r', encoding='utf-8') as f:
                    backup_data = f.read()
                with open(backup_path, 'w', encoding='utf-8') as f:
                    f.write(backup_data)
                self.logger.info(f"Created backup: {backup_path}")

            # Save new data
            with open(self.marketplace_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
                f.write('\n')

            return True
        except Exception as e:
            self.logger.error(f"Failed to save marketplace: {e}")
            return False

    def skill_to_plugin_entry(self, skill_info: Dict) -> Dict:
        """Convert skill info to marketplace plugin entry."""
        entry = {
            "name": skill_info['name'],
            "description": skill_info['description'],
            "source": skill_info['source'],
            "category": skill_info['category']
        }

        if skill_info.get('author'):
            entry['author'] = skill_info['author']

        return entry

    def compare_entries(self, existing: Dict, new: Dict) -> Tuple[bool, List[str]]:
        """
        Compare two plugin entries and return differences.

        Returns:
            Tuple of (are_same, list of differences)
        """
        differences = []

        # Fields to compare
        fields = ['name', 'description', 'source', 'category']

        for field in fields:
            if existing.get(field) != new.get(field):
                differences.append(f"{field}: '{existing.get(field)}' -> '{new.get(field)}'")

        return len(differences) == 0, differences

    def update_marketplace(
        self,
        skills: Dict[str, Dict],
        dry_run: bool = False,
        force: bool = False
    ) -> Tuple[bool, Dict]:
        """
        Update marketplace with scanned skills.

        Args:
            skills: Dict of skill path to skill info
            dry_run: If True, don't write changes
            force: Force update even if no changes

        Returns:
            Tuple of (success, stats dict)
        """
        stats = {
            'total_scanned': len(skills),
            'added': 0,
            'updated': 0,
            'unchanged': 0,
            'removed': 0,
            'duplicates': 0,
            'errors': []
        }

        # Load existing marketplace
        marketplace = self.load_marketplace()
        if not marketplace:
            stats['errors'].append("Failed to load marketplace.json")
            return False, stats

        # Create lookup by source path
        existing_by_source = {}
        existing_by_name = {}
        for plugin in marketplace.get('plugins', []):
            source = plugin.get('source', '')
            name = plugin.get('name', '')
            existing_by_source[source] = plugin
            existing_by_name[name] = plugin

        # Build new plugin list, tracking seen names to avoid duplicates
        new_plugins = []
        scanned_sources = set()
        seen_names = set()

        for source, skill_info in skills.items():
            scanned_sources.add(source)
            skill_name = skill_info['name']
            new_entry = self.skill_to_plugin_entry(skill_info)

            # Check for duplicate skill names (same name in different directories)
            if skill_name in seen_names:
                stats['duplicates'] += 1
                self.logger.warning(
                    f"Duplicate skill name '{skill_name}' at {source} - skipping"
                )
                continue

            seen_names.add(skill_name)

            # Check if exists
            existing = existing_by_source.get(source) or existing_by_name.get(skill_name)

            if existing:
                same, diffs = self.compare_entries(existing, new_entry)
                if same and not force:
                    # Keep existing entry (preserve author info, etc.)
                    new_plugins.append(existing)
                    stats['unchanged'] += 1
                else:
                    # Update with new info, but preserve author if not in new
                    if 'author' not in new_entry and 'author' in existing:
                        new_entry['author'] = existing['author']
                    new_plugins.append(new_entry)
                    stats['updated'] += 1
                    if diffs:
                        self.logger.info(f"Updating {skill_name}: {', '.join(diffs)}")
            else:
                new_plugins.append(new_entry)
                stats['added'] += 1
                self.logger.info(f"Adding new skill: {skill_name}")

        # Check for plugins that no longer exist on disk
        for source, plugin in existing_by_source.items():
            plugin_name = plugin.get('name', '')
            if source not in scanned_sources:
                # Check if the path actually exists
                full_path = PROJECT_ROOT / source.lstrip('./')
                if not full_path.exists():
                    stats['removed'] += 1
                    self.logger.warning(f"Skill no longer exists: {plugin_name} ({source})")
                elif plugin_name not in seen_names:
                    # Path exists but wasn't scanned (maybe different category structure)
                    new_plugins.append(plugin)
                    seen_names.add(plugin_name)
                    stats['unchanged'] += 1

        # Sort by name
        new_plugins.sort(key=lambda p: p.get('name', '').lower())

        # Update marketplace
        marketplace['plugins'] = new_plugins

        # Summary
        self.logger.info(f"\nScan Results:")
        self.logger.info(f"  Total scanned: {stats['total_scanned']}")
        self.logger.info(f"  Added: {stats['added']}")
        self.logger.info(f"  Updated: {stats['updated']}")
        self.logger.info(f"  Unchanged: {stats['unchanged']}")
        self.logger.info(f"  Duplicates skipped: {stats['duplicates']}")
        self.logger.info(f"  Removed from disk: {stats['removed']}")
        self.logger.info(f"  Total plugins: {len(new_plugins)}")

        if dry_run:
            self.logger.info("\n[DRY RUN] No changes written to disk")
            return True, stats

        # Save if there are changes
        if stats['added'] > 0 or stats['updated'] > 0 or force:
            if self.save_marketplace(marketplace):
                self.logger.info(f"\nSuccessfully updated {self.marketplace_path}")
                return True, stats
            else:
                stats['errors'].append("Failed to save marketplace.json")
                return False, stats
        else:
            self.logger.info("\nNo changes to write")
            return True, stats


def generate_report(
    skills: Dict[str, Dict],
    validation_results: Dict[str, Tuple[bool, List[str], List[str]]],
    stats: Dict
) -> str:
    """Generate a detailed report of the scan."""
    lines = []
    lines.append("=" * 70)
    lines.append("SKILL SCANNER REPORT")
    lines.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append("=" * 70)
    lines.append("")

    # Summary
    lines.append("SUMMARY")
    lines.append("-" * 70)
    lines.append(f"Total skills scanned: {len(skills)}")
    lines.append(f"Valid skills: {sum(1 for v in validation_results.values() if v[0])}")
    lines.append(f"Invalid skills: {sum(1 for v in validation_results.values() if not v[0])}")
    lines.append("")

    # By category
    categories = {}
    for source, info in skills.items():
        cat = info.get('category', 'unknown')
        if cat not in categories:
            categories[cat] = []
        categories[cat].append(info)

    lines.append("BY CATEGORY")
    lines.append("-" * 70)
    for cat in sorted(categories.keys()):
        lines.append(f"  {cat}: {len(categories[cat])} skills")
    lines.append("")

    # Validation issues
    issues = [(path, info, validation_results[path])
              for path, info in skills.items()
              if path in validation_results and (validation_results[path][1] or validation_results[path][2])]

    if issues:
        lines.append("VALIDATION ISSUES")
        lines.append("-" * 70)
        for path, info, (is_valid, errors, warnings) in issues:
            lines.append(f"\n  {info.get('name', path)}:")
            for err in errors:
                lines.append(f"    ERROR: {err}")
            for warn in warnings:
                lines.append(f"    WARNING: {warn}")
        lines.append("")

    # Skills list
    lines.append("ALL SKILLS")
    lines.append("-" * 70)
    for cat in sorted(categories.keys()):
        lines.append(f"\n  [{cat}]")
        for skill in sorted(categories[cat], key=lambda s: s.get('name', '')):
            status = "✓" if validation_results.get(skill['source'], (True, [], []))[0] else "✗"
            lines.append(f"    {status} {skill.get('name')}")
    lines.append("")

    lines.append("=" * 70)
    return "\n".join(lines)


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Scan skills and update marketplace.json",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )
    parser.add_argument('--check', action='store_true',
                        help='Only check skills, don\'t update marketplace')
    parser.add_argument('--dry-run', action='store_true',
                        help='Show what would be changed without writing')
    parser.add_argument('--verbose', '-v', action='store_true',
                        help='Show detailed output')
    parser.add_argument('--force', '-f', action='store_true',
                        help='Force update even if no changes detected')
    parser.add_argument('--category', '-c', type=str,
                        help='Only scan a specific category')
    parser.add_argument('--report', '-r', type=str,
                        help='Save report to file')

    args = parser.parse_args()

    # Setup
    scanner = SkillScanner(verbose=args.verbose)
    updater = MarketplaceUpdater(MARKETPLACE_PATH, verbose=args.verbose)

    print("\n" + "=" * 70)
    print("SKILL SCANNER AND MARKETPLACE UPDATER")
    print("=" * 70 + "\n")

    # Scan skills
    categories = [args.category] if args.category else None
    print(f"Scanning skill directories...")
    skills = scanner.scan_all_skills(categories)
    print(f"Found {len(skills)} skills\n")

    # Validate all skills
    validation_results = {}
    valid_count = 0
    for path, info in skills.items():
        is_valid, errors, warnings = scanner.validate_skill(info)
        validation_results[path] = (is_valid, errors, warnings)
        if is_valid:
            valid_count += 1
        else:
            print(f"Invalid skill: {info.get('name', path)}")
            for err in errors:
                print(f"  ERROR: {err}")

    print(f"\nValidation: {valid_count}/{len(skills)} skills valid")

    # Check only mode
    if args.check:
        report = generate_report(skills, validation_results, {})
        print("\n" + report)

        if args.report:
            with open(args.report, 'w', encoding='utf-8') as f:
                f.write(report)
            print(f"\nReport saved to: {args.report}")

        return 0 if valid_count == len(skills) else 1

    # Update marketplace
    print("\nUpdating marketplace.json...")
    success, stats = updater.update_marketplace(
        skills,
        dry_run=args.dry_run,
        force=args.force
    )

    # Generate and optionally save report
    report = generate_report(skills, validation_results, stats)

    if args.verbose:
        print("\n" + report)

    if args.report:
        with open(args.report, 'w', encoding='utf-8') as f:
            f.write(report)
        print(f"\nReport saved to: {args.report}")

    if not success:
        print("\nERROR: Failed to update marketplace")
        for err in stats.get('errors', []):
            print(f"  - {err}")
        return 1

    print("\nDone!")
    return 0


if __name__ == '__main__':
    sys.exit(main())
