import json
import os

marketplace_path = r'E:\Python_Doc\My_Github\Skillbox-Workspace\Skill Box\.claude-plugin\marketplace.json'
i18n_skills_root = r'E:\Python_Doc\My_Github\Skillbox-Workspace\Skill Box\i18n\skills'
root_dir = r'E:\Python_Doc\My_Github\Skillbox-Workspace\Skill Box'

with open(marketplace_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

marketplace_skills = []
for plugin in data['plugins']:
    for skill_path in plugin['skills']:
        # skill_path looks like "./productivity/notion"
        rel_path = skill_path.lstrip('./')
        marketplace_skills.append(rel_path)

print(f"Total skills in marketplace.json: {len(marketplace_skills)}")

missing_in_i18n = []
for skill in marketplace_skills:
    i18n_path = os.path.join(i18n_skills_root, skill)
    if not os.path.isdir(i18n_path):
        missing_in_i18n.append(skill)

print(f"\nMissing folders in i18n/skills ({len(missing_in_i18n)}):")
for s in missing_in_i18n:
    print(f"  - {s}")

# Check if root folders exist for these
missing_in_root = []
for s in marketplace_skills:
    root_path = os.path.join(root_dir, s)
    if not os.path.isdir(root_path):
        missing_in_root.append(s)

if missing_in_root:
    print(f"\nSkills in marketplace.json but missing in root ({len(missing_in_root)}):")
    for s in missing_in_root:
        print(f"  - {s}")

# Check i18n folders that are NOT in marketplace
redundant_in_i18n = []
for root, dirs, files in os.walk(i18n_skills_root):
    # Only check skill-level folders (depth 2 from i18n_skills_root)
    rel_dir = os.path.relpath(root, i18n_skills_root)
    if rel_dir == '.' or rel_dir == '..':
        continue
    
    parts = rel_dir.split(os.sep)
    if len(parts) == 2:
        skill_rel = rel_dir.replace(os.sep, '/')
        if skill_rel not in marketplace_skills:
            redundant_in_i18n.append(skill_rel)

if redundant_in_i18n:
    print(f"\nRedundant folders in i18n/skills ({len(redundant_in_i18n)}):")
    for s in redundant_in_i18n:
        print(f"  - {s}")
