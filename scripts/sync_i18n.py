import os
import json
import shutil

def main():
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    i18n_root = os.path.join(root_dir, 'i18n', 'skills')
    
    categories = [
        'ai-meta', 'business-analyst', 'content-pipeline', 'dev-tools',
        'obsidian', 'productivity', 'visual-creative'
    ]
    
    print("🔄 开始同步 i18n 目录结构...")
    
    for cat in categories:
        cat_path = os.path.join(root_dir, cat)
        if not os.path.exists(cat_path):
            continue
        
        i18n_cat_path = os.path.join(i18n_root, cat)
        if not os.path.exists(i18n_cat_path):
            os.makedirs(i18n_cat_path)
        
        # 处理 obsidian-toolkit 特殊嵌套
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
            if not os.path.isdir(skill_path):
                continue
            if skill == 'obsidian-toolkit':
                continue
            
            i18n_skill_path = os.path.join(i18n_cat_path, skill)
            if not os.path.exists(i18n_skill_path) or not os.path.isdir(i18n_skill_path):
                os.makedirs(i18n_skill_path, exist_ok=True)
                print(f"   ✅ 创建目录: {os.path.relpath(i18n_skill_path, root_dir)}")

    print("\n✅ 目录结构同步完成。")

if __name__ == "__main__":
    main()
