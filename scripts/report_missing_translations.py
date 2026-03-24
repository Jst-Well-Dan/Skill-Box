import os

root_dir = r'E:\Python_Doc\My_Github\Skillbox-Workspace\Skill Box'
i18n_root = os.path.join(root_dir, 'i18n', 'skills')

categories = [
    'ai-meta', 'business-analyst', 'content-pipeline', 'dev-tools',
    'obsidian', 'productivity', 'visual-creative'
]

report = []

for cat in categories:
    cat_path = os.path.join(root_dir, cat)
    if not os.path.exists(cat_path):
        continue
    
    # Special handling for obsidian-toolkit (nested structure)
    if cat == 'obsidian':
        toolkit_path = os.path.join(cat_path, 'obsidian-toolkit')
        if os.path.exists(toolkit_path):
            for sub in os.listdir(toolkit_path):
                sub_path = os.path.join(toolkit_path, sub)
                if os.path.isdir(sub_path):
                    # Check in i18n
                    i18n_sub_path = os.path.join(i18n_root, 'obsidian', 'obsidian-toolkit', sub)
                    has_md = os.path.exists(os.path.join(i18n_sub_path, 'SKILL.md'))
                    has_zh_md = os.path.exists(os.path.join(i18n_sub_path, 'SKILL.zh.md'))
                    
                    if not (has_md or has_zh_md):
                        report.append(f"Missing: obsidian/obsidian-toolkit/{sub}")
    
    # Normal skills
    for skill in os.listdir(cat_path):
        skill_path = os.path.join(cat_path, skill)
        if not os.path.isdir(skill_path):
            continue
        if skill == 'obsidian-toolkit' and cat == 'obsidian':
            continue
            
        # Check if the root skill has a SKILL.md (to ensure it's actually a skill)
        if not os.path.exists(os.path.join(skill_path, 'SKILL.md')):
            # Some might be utility folders, but usually in this repo they are skills
            # report.append(f"Note: {cat}/{skill} has no root SKILL.md")
            pass
            
        i18n_skill_path = os.path.join(i18n_root, cat, skill)
        has_md = os.path.exists(os.path.join(i18n_skill_path, 'SKILL.md'))
        has_zh_md = os.path.exists(os.path.join(i18n_skill_path, 'SKILL.zh.md'))
        
        if not (has_md or has_zh_md):
            report.append(f"Missing: {cat}/{skill}")

print("\n".join(report))
if not report:
    print("All skills have a translation file in i18n/skills.")
