import os
import shutil

root_dir = r'E:\Python_Doc\My_Github\Skillbox-Workspace\Skill Box'
i18n_root = os.path.join(root_dir, 'i18n', 'skills')

categories = [
    'ai-meta', 'business-analyst', 'content-pipeline', 'dev-tools',
    'obsidian', 'productivity', 'visual-creative'
]

for cat in categories:
    cat_path = os.path.join(root_dir, cat)
    if not os.path.exists(cat_path): continue
    
    i18n_cat_path = os.path.join(i18n_root, cat)
    if not os.path.exists(i18n_cat_path):
        os.makedirs(i18n_cat_path)
    
    # Special handle for obsidian-toolkit which has nested folders
    if cat == 'obsidian':
        toolkit_path = os.path.join(cat_path, 'obsidian-toolkit')
        if os.path.exists(toolkit_path):
            i18n_toolkit_path = os.path.join(i18n_cat_path, 'obsidian-toolkit')
            if not os.path.exists(i18n_toolkit_path):
                os.makedirs(i18n_toolkit_path)
            
            for sub in os.listdir(toolkit_path):
                sub_path = os.path.join(toolkit_path, sub)
                if os.path.isdir(sub_path):
                    i18n_sub_path = os.path.join(i18n_toolkit_path, sub)
                    if not os.path.exists(i18n_sub_path):
                        os.makedirs(i18n_sub_path)
    
    for skill in os.listdir(cat_path):
        skill_path = os.path.join(cat_path, skill)
        if not os.path.isdir(skill_path): continue
        if skill == 'obsidian-toolkit': continue # already handled above or special
        
        # Skill-level folder in i18n
        i18n_skill_path = os.path.join(i18n_cat_path, skill)
        if not os.path.exists(i18n_skill_path):
            os.makedirs(i18n_skill_path)
            print(f"Created missing folder: {os.path.relpath(i18n_skill_path, root_dir)}")

print("Done syncing folder structure.")
