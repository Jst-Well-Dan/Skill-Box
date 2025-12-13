#!/usr/bin/env python3
"""
Fetch External Claude Skills

This script fetches external Claude skills from GitHub repositories and
integrates them into the awesome-claude-skills marketplace.

Usage:
    python fetch_external_skills.py [options]

Options:
    --dry-run           Simulate fetch without writing files
    --skill SKILL_ID    Fetch only specific skill by ID
    --all               Fetch all skills (default)
    --verbose           Enable verbose logging
    --no-marketplace    Skip marketplace.json update
    --force             Force re-fetch existing skills
"""

import argparse
import json
import logging
import sys
import tempfile
import shutil
from pathlib import Path
from typing import List, Dict, Optional

import utils
import github_fetcher
import skill_processor
import marketplace_updater


class SkillFetcher:
    """Main orchestrator for fetching external skills."""

    def __init__(self, config_path: str, dry_run: bool = False, force: bool = False):
        """
        Initialize skill fetcher.

        Args:
            config_path: Path to external_skills_config.json
            dry_run: If True, simulate without writing files
            force: If True, re-fetch existing skills
        """
        self.config_path = config_path
        self.dry_run = dry_run
        self.force = force
        self.config = None
        self.fetcher = None
        self.base_dir = None

        # Stats
        self.stats = {
            'total': 0,
            'successful': 0,
            'failed': 0,
            'skipped': 0,
            'errors': []
        }

    def load_config(self) -> bool:
        """Load configuration file."""
        try:
            with open(self.config_path, 'r', encoding='utf-8') as f:
                self.config = json.load(f)

            self.base_dir = self.config.get('output_directory', '.')
            logging.info(f"Loaded configuration with {len(self.config['skills'])} skills")
            return True

        except Exception as e:
            logging.error(f"Failed to load configuration: {e}")
            return False

    def validate_environment(self) -> bool:
        """Validate environment and prerequisites."""
        # Check write permissions
        base_path = Path(self.base_dir)
        if not base_path.exists():
            logging.error(f"Output directory does not exist: {self.base_dir}")
            return False

        if not self.dry_run:
            # Test write permissions
            test_file = base_path / '.write_test'
            try:
                test_file.write_text('test')
                test_file.unlink()
            except Exception as e:
                logging.error(f"No write permission in {self.base_dir}: {e}")
                return False

        logging.info("Environment validation passed")
        return True

    def check_conflicts(self, skills: List[Dict]) -> List[str]:
        """Check for name conflicts with existing skills."""
        conflicts = []

        for skill in skills:
            target_folder = skill['target_folder']
            conflict_path = skill_processor.check_name_conflicts(
                target_folder, self.base_dir
            )

            if conflict_path and not self.force:
                conflicts.append(target_folder)
                logging.warning(f"Conflict: {target_folder} already exists")

        return conflicts

    def fetch_skill(self, skill_config: Dict) -> bool:
        """
        Fetch a single skill.

        Args:
            skill_config: Skill configuration dict

        Returns:
            True if successful, False otherwise
        """
        skill_id = skill_config['id']
        target_folder = skill_config['target_folder']
        target_path = Path(self.base_dir) / target_folder

        logging.info(f"Fetching skill: {skill_id}")

        # Check if already exists
        if target_path.exists() and not self.force:
            logging.info(f"Skill already exists, skipping: {target_folder}")
            self.stats['skipped'] += 1
            return True

        if self.dry_run:
            logging.info(f"[DRY RUN] Would fetch {skill_id} to {target_path}")
            return True

        # Create temp directory for fetching
        temp_dir = tempfile.mkdtemp(prefix=f'skill_fetch_{skill_id}_')

        try:
            # Fetch from GitHub
            success = self.fetcher.fetch_skill(
                github_url=skill_config['github_url'],
                repo_type=skill_config['repo_type'],
                target_folder=temp_dir,
                extraction_config=skill_config['extraction_config']
            )

            if not success:
                raise Exception("GitHub fetch failed")

            # Validate skill
            validation = skill_processor.validate_skill(temp_dir)
            if not validation['valid']:
                errors = ', '.join(validation['errors'])
                raise Exception(f"Validation failed: {errors}")

            if validation['warnings']:
                for warning in validation['warnings']:
                    logging.warning(f"  {warning}")

            # Move to target location
            if target_path.exists():
                logging.info(f"Removing existing skill: {target_path}")
                shutil.rmtree(target_path)

            shutil.move(temp_dir, target_path)
            logging.info(f"Successfully fetched: {skill_id} -> {target_path}")

            self.stats['successful'] += 1
            return True

        except Exception as e:
            error_msg = f"Failed to fetch {skill_id}: {e}"
            logging.error(error_msg)
            self.stats['errors'].append(error_msg)
            self.stats['failed'] += 1
            return False

        finally:
            # Cleanup temp directory if it still exists
            if Path(temp_dir).exists():
                try:
                    shutil.rmtree(temp_dir)
                except Exception as e:
                    logging.warning(f"Failed to cleanup temp dir {temp_dir}: {e}")

    def fetch_all_skills(self, skills: List[Dict]) -> Dict[str, Dict]:
        """
        Fetch all skills.

        Args:
            skills: List of skill configurations

        Returns:
            Dict mapping skill IDs to their metadata
        """
        skill_metadata = {}

        self.stats['total'] = len(skills)
        logging.info(f"Starting to fetch {len(skills)} skills...")

        for i, skill_config in enumerate(skills, 1):
            skill_id = skill_config['id']
            logging.info(f"[{i}/{len(skills)}] Processing: {skill_id}")

            success = self.fetch_skill(skill_config)

            if success:
                # Get metadata for marketplace
                target_folder = skill_config['target_folder']
                target_path = Path(self.base_dir) / target_folder

                if target_path.exists():
                    validation = skill_processor.validate_skill(str(target_path))
                    if validation['valid']:
                        metadata = skill_processor.normalize_skill_metadata(
                            skill_config,
                            validation['metadata']
                        )
                        skill_metadata[skill_id] = metadata

        return skill_metadata

    def update_marketplace(self, skill_metadata: Dict[str, Dict]) -> bool:
        """
        Update marketplace.json with fetched skills.

        Args:
            skill_metadata: Dict of skill metadata

        Returns:
            True if successful
        """
        if self.dry_run:
            logging.info("[DRY RUN] Would update marketplace.json")
            return True

        marketplace_path = Path(self.base_dir) / '.claude-plugin' / 'marketplace.json'

        if not marketplace_path.exists():
            logging.error(f"Marketplace not found: {marketplace_path}")
            return False

        # Filter to only successful skills
        successful_skills = [
            skill for skill in self.config['skills']
            if skill['id'] in skill_metadata
        ]

        logging.info(
            f"Updating marketplace with {len(successful_skills)} skills"
        )

        success = marketplace_updater.update_marketplace_with_skills(
            str(marketplace_path),
            successful_skills,
            skill_metadata
        )

        return success

    def generate_report(self) -> str:
        """Generate execution report."""
        lines = []
        lines.append("=" * 70)
        lines.append("External Skills Fetch Report")
        lines.append("=" * 70)
        lines.append("")
        lines.append(f"Total skills:      {self.stats['total']}")
        lines.append(f"Successful:        {self.stats['successful']}")
        lines.append(f"Failed:            {self.stats['failed']}")
        lines.append(f"Skipped (exists):  {self.stats['skipped']}")
        lines.append("")

        if self.stats['errors']:
            lines.append("ERRORS:")
            lines.append("-" * 70)
            for error in self.stats['errors']:
                lines.append(f"  • {error}")
            lines.append("")

        lines.append("=" * 70)

        return '\n'.join(lines)

    def run(self, skill_ids: Optional[List[str]] = None) -> int:
        """
        Run the fetcher.

        Args:
            skill_ids: List of specific skill IDs to fetch (None = all)

        Returns:
            Exit code (0 = success, 1 = failure)
        """
        # Load configuration
        if not self.load_config():
            return 1

        # Validate environment
        if not self.validate_environment():
            return 1

        # Initialize GitHub fetcher
        # GitHubFetcher will read GITHUB_TOKEN from environment automatically
        self.fetcher = github_fetcher.GitHubFetcher(token=None)

        # Filter skills if specific IDs provided
        all_skills = self.config['skills']
        if skill_ids:
            skills_to_fetch = [
                s for s in all_skills if s['id'] in skill_ids
            ]
            if not skills_to_fetch:
                logging.error(f"No skills found matching IDs: {skill_ids}")
                return 1
        else:
            skills_to_fetch = all_skills

        # Check for conflicts
        conflicts = self.check_conflicts(skills_to_fetch)
        if conflicts and not self.force:
            logging.error(
                f"Found {len(conflicts)} conflicting skill names. "
                "Use --force to re-fetch."
            )
            return 1

        # Fetch skills
        skill_metadata = self.fetch_all_skills(skills_to_fetch)

        # Update marketplace
        if skill_metadata and not self.dry_run:
            if not self.update_marketplace(skill_metadata):
                logging.error("Failed to update marketplace.json")
                # Don't fail completely, skills are already fetched

        # Generate report
        report = self.generate_report()
        print("\n" + report)
        logging.info("Fetch completed")

        # Return exit code
        return 0 if self.stats['failed'] == 0 else 1


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description='Fetch external Claude skills from GitHub repositories'
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Simulate fetch without writing files'
    )
    parser.add_argument(
        '--skill',
        metavar='SKILL_ID',
        help='Fetch only specific skill by ID'
    )
    parser.add_argument(
        '--all',
        action='store_true',
        help='Fetch all skills (default)'
    )
    parser.add_argument(
        '--verbose',
        action='store_true',
        help='Enable verbose logging'
    )
    parser.add_argument(
        '--no-marketplace',
        action='store_true',
        help='Skip marketplace.json update'
    )
    parser.add_argument(
        '--force',
        action='store_true',
        help='Force re-fetch existing skills'
    )
    parser.add_argument(
        '--config',
        default='external_skills_config.json',
        help='Path to configuration file (default: external_skills_config.json)'
    )

    args = parser.parse_args()

    # Setup logging
    log_level = logging.DEBUG if args.verbose else logging.INFO
    utils.setup_logging(level=log_level)

    # Determine skill IDs to fetch
    skill_ids = None
    if args.skill:
        skill_ids = [args.skill]

    # Create fetcher and run
    fetcher = SkillFetcher(
        config_path=args.config,
        dry_run=args.dry_run,
        force=args.force
    )

    exit_code = fetcher.run(skill_ids=skill_ids)
    sys.exit(exit_code)


if __name__ == '__main__':
    main()
