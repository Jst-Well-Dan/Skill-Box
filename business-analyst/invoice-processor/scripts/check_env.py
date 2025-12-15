#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Quick environment check for invoice processor
"""

import os
import sys
from pathlib import Path

# 获取 .env 文件路径（脚本上级目录）
SCRIPT_DIR = Path(__file__).resolve().parent
ENV_FILE = SCRIPT_DIR.parent / '.env'


def load_env_file():
    """从 .env 文件加载环境变量"""
    if not ENV_FILE.exists():
        return {}

    env_vars = {}
    with open(ENV_FILE, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#') and '=' in line:
                key, value = line.split('=', 1)
                env_vars[key.strip()] = value.strip()
    return env_vars


def check_environment():
    """快速检查环境配置"""
    issues = []

    # 从 .env 文件加载配置
    env_vars = load_env_file()

    # Check .env file exists
    if not ENV_FILE.exists():
        issues.append(f".env file not found at: {ENV_FILE}")
        issues.append("  Create .env file with: GLM_API_KEY=your_api_key")
    elif not env_vars.get('GLM_API_KEY'):
        issues.append("GLM_API_KEY not set in .env file. Get key from: https://open.bigmodel.cn/")

    # Check dependencies
    try:
        import aiohttp
    except ImportError:
        issues.append("Missing: pip install aiohttp")

    try:
        import fitz
    except ImportError:
        issues.append("Missing: pip install PyMuPDF (for PDF support)")

    try:
        import openpyxl
    except ImportError:
        issues.append("Missing: pip install openpyxl")

    # Report results
    if issues:
        print("Environment issues found:")
        for i, issue in enumerate(issues, 1):
            print(f"  {i}. {issue}")
        return 1
    else:
        print("Environment OK - Ready to process invoices")
        return 0

if __name__ == '__main__':
    sys.exit(check_environment())
