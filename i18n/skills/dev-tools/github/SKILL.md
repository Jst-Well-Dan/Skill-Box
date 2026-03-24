---
name: github
description: "通过 `gh` CLI 执行 GitHub 操作：管理 Issue、PR、CI 运行、代码审查、API 查询。适用于：(1) 检查 PR 状态或 CI 情况, (2) 创建或评论 Issue, (3) 列出/筛选 PR 或 Issue, (4) 查看运行日志。不适用于：需要手动浏览器操作的复杂 Web UI 交互（如果可用，请使用浏览器工具）、跨多个仓库的批量操作（使用 gh api 脚本），或者未配置 gh auth 的情况。"
metadata:
  {
    "openclaw":
      {
        "emoji": "🐙",
        "requires": { "bins": ["gh"] },
        "install":
          [
            {
              "id": "brew",
              "kind": "brew",
              "formula": "gh",
              "bins": ["gh"],
              "label": "安装 GitHub CLI (brew)",
            },
            {
              "id": "apt",
              "kind": "apt",
              "package": "gh",
              "bins": ["gh"],
              "label": "安装 GitHub CLI (apt)",
            },
          ],
      },
  }
---

# GitHub 操作技能

使用 `gh` CLI 与 GitHub 仓库、Issue、PR 和 CI 进行交互。

## 何时使用

✅ **在以下情况下使用此技能：**

- 检查 PR 状态、审查情况或合并就绪状态。
- 查看 CI/工作流运行状态和日志。
- 创建、关闭或评论 Issue。
- 创建或合并拉取请求 (Pull Requests)。
- 查询 GitHub API 获取仓库数据。
- 列出仓库、发布版本或协作者。

## 何时不要使用

❌ **在以下情况下不要使用此技能：**

- 本地 git 操作（commit, push, pull, branch）→ 直接使用 `git`。
- 非 GitHub 仓库（GitLab, Bitbucket, 自托管等）→ 使用不同的 CLI。
- 克隆仓库 → 使用 `git clone`。
- 审查实际的代码更改 → 使用 `coding-agent` 技能。
- 复杂的跨文件差异比较 → 使用 `coding-agent` 或直接读取文件。

## 设置指南

```bash
# 身份验证（一次性设置）
gh auth login

# 验证状态
gh auth status
```

## 常用命令

### 拉取请求 (Pull Requests)

```bash
# 列出 PR
gh pr list --repo owner/repo

# 检查 CI 状态
gh pr checks 55 --repo owner/repo

# 查看 PR 详情
gh pr view 55 --repo owner/repo

# 创建 PR
gh pr create --title "feat: 添加功能" --body "描述内容"

# 合并 PR
gh pr merge 55 --squash --repo owner/repo
```

### 问题 (Issues)

```bash
# 列出 Issue
gh issue list --repo owner/repo --state open

# 创建 Issue
gh issue create --title "Bug: 某些功能损坏" --body "详情描述..."

# 关闭 Issue
gh issue close 42 --repo owner/repo
```

### CI/工作流运行 (Workflow Runs)

```bash
# 列出最近的运行记录
gh run list --repo owner/repo --limit 10

# 查看特定运行记录
gh run view <run-id> --repo owner/repo

# 仅查看失败步骤的日志
gh run view <run-id> --repo owner/repo --log-failed

# 重新运行失败的作业
gh run rerun <run-id> --failed --repo owner/repo
```

### API 查询

```bash
# 获取带特定字段的 PR 信息
gh api repos/owner/repo/pulls/55 --jq '.title, .state, .user.login'

# 列出所有标签
gh api repos/owner/repo/labels --jq '.[].name'

# 获取仓库统计数据
gh api repos/owner/repo --jq '{stars: .stargazers_count, forks: .forks_count}'
```

## JSON 输出

大多数命令支持 `--json` 参数以获得结构化输出，配合 `--jq` 进行筛选：

```bash
gh issue list --repo owner/repo --json number,title --jq '.[] | "\(.number): \(.title)"'
gh pr list --json number,title,state,mergeable --jq '.[] | select(.mergeable == "MERGEABLE")'
```

## 模板示例

### PR 审查摘要

```bash
# 获取 PR 概览用于审查
PR=55 REPO=owner/repo
echo "## PR #$PR 摘要"
gh pr view $PR --repo $REPO --json title,body,author,additions,deletions,changedFiles \
  --jq '"**\(.title)** 由 @\(.author.login) 提交\n\n\(.body)\n\n📊 +\(.additions) -\(.deletions) 涉及 \(.changedFiles) 个文件"'
gh pr checks $PR --repo $REPO
```

### Issue 分类整理

```bash
# 快速 Issue 分类视图
gh issue list --repo owner/repo --state open --json number,title,labels,createdAt \
  --jq '.[] | "[\(.number)] \(.title) - \([.labels[].name] | join(", ")) (\(.createdAt[:10]))"'
```

## 注意事项

- 不在 git 目录中时，务必指定 `--repo owner/repo`。
- 直接使用 URL：`gh pr view https://github.com/owner/repo/pull/55`。
- 存在速率限制；对于重复查询，请使用 `gh api --cache 1h`。
