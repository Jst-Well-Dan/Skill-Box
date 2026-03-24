---
name: xurl
description: 用于向 X (Twitter) API 发送经过身份验证请求的命令行工具。当需要发布推文、回复、引用、搜索、查看帖子、管理粉丝、发送私信、上传媒体或与任何 X API v2 端点交互时，请使用此技能。
metadata:
  {
    "openclaw":
      {
        "emoji": "𝕏",
        "requires": { "bins": ["xurl"] },
        "install":
          [
            {
              "id": "brew",
              "kind": "brew",
              "formula": "xdevplatform/tap/xurl",
              "bins": ["xurl"],
              "label": "安装 xurl (brew)",
            },
            {
              "id": "npm",
              "kind": "npm",
              "package": "@xdevplatform/xurl",
              "bins": ["xurl"],
              "label": "安装 xurl (npm)",
            },
          ],
      },
  }
---

# xurl — 代理技能参考指南

`xurl` 是一个用于 X API 的命令行工具。它既支持**快捷命令**（对人类/代理友好的单行命令），也支持对任何 v2 端点的 **curl 风格原始访问**。所有命令都会向标准输出返回 JSON 格式结果。

---

## 安装指南

### Homebrew (macOS)

```bash
brew install --cask xdevplatform/tap/xurl
```

### npm

```bash
npm install -g @xdevplatform/xurl
```

### Shell 脚本

```bash
curl -fsSL https://raw.githubusercontent.com/xdevplatform/xurl/main/install.sh | bash
```

安装到 `~/.local/bin`。如果它不在您的 PATH 中，脚本会提示您需要添加的内容。

---

## 准备工作

此技能需要 `xurl` CLI 工具：<https://github.com/xdevplatform/xurl>。

在使用任何命令之前，您必须通过身份验证。运行 `xurl auth status` 进行检查。

### 机密安全（强制要求）

- **严禁**读取、打印、解析、总结、上传或向 LLM 上下文发送 `~/.xurl`（或其副本）。
- **严禁**要求用户在聊天中粘贴凭据/令牌。
- 用户必须在自己的机器上手动将所需的机密填入 `~/.xurl`。
- **不要**在代理/LLM 会话中建议或执行带有内联机密的身份验证命令。
- 警告：在代理会话中使用 CLI 机密选项可能会导致凭据泄露（在提示/上下文、日志、外壳历史记录中）。
- **不要**在代理/LLM 会话中使用 `--verbose` / `-v` 参数；它可能会在输出中暴露敏感的头部/令牌。
- **绝对禁止**在代理命令中使用的敏感标志：`--bearer-token`, `--consumer-key`, `--consumer-secret`, `--access-token`, `--token-secret`, `--client-id`, `--client-secret`。
- 要验证是否已注册至少一个带有凭据的应用，请运行：`xurl auth status`。

### 注册应用（推荐）

应用凭据注册必须由用户在代理/LLM 会话之外手动完成。
注册凭据后，使用以下命令进行身份验证：

```bash
xurl auth oauth2
```

如果有多个预配置的应用，可以进行切换：

```bash
xurl auth default prod-app          # 设置默认应用
xurl auth default prod-app alice    # 设置默认应用 + 用户
xurl --app dev-app /2/users/me      # 一次性覆盖使用
```

---

## 快速参考

| 操作 | 命令 |
| ------------------------- | ----------------------------------------------------- |
| 发布推文 | `xurl post "Hello world!"` |
| 回复推文 | `xurl reply POST_ID "Nice post!"` |
| 引用推文 | `xurl quote POST_ID "My take"` |
| 删除帖子 | `xurl delete POST_ID` |
| 读取帖子 | `xurl read POST_ID` |
| 搜索帖子 | `xurl search "QUERY" -n 10` |
| 我是谁 | `xurl whoami` |
| 查找用户 | `xurl user @handle` |
| 主页时间线 | `xurl timeline -n 20` |
| 提及/艾特我的 | `xurl mentions -n 10` |
| 点赞 | `xurl like POST_ID` |
| 取消点赞 | `xurl unlike POST_ID` |
| 转推 (Repost) | `xurl repost POST_ID` |
| 撤销转推 | `xurl unrepost POST_ID` |
| 收藏 (Bookmark) | `xurl bookmark POST_ID` |
| 移除收藏 | `xurl unbookmark POST_ID` |
| 收藏列表 | `xurl bookmarks -n 10` |
| 点赞列表 | `xurl likes -n 10` |
| 关注 | `xurl follow @handle` |
| 取消关注 | `xurl unfollow @handle` |
| 正在关注列表 | `xurl following -n 20` |
| 粉丝列表 | `xurl followers -n 20` |
| 拉黑 | `xurl block @handle` |
| 取消拉黑 | `xurl unblock @handle` |
| 屏蔽 (Mute) | `xurl mute @handle` |
| 取消屏蔽 | `xurl unmute @handle` |
| 发送私信 | `xurl dm @handle "message"` |
| 私信列表 | `xurl dms -n 10` |
| 上传媒体 | `xurl media upload path/to/file.mp4` |
| 媒体状态 | `xurl media status MEDIA_ID` |

> **帖子 ID vs URL:** 在上述出现 `POST_ID` 的任何地方，您也可以直接粘贴完整的帖子 URL（例如 `https://x.com/user/status/1234567890`）——xurl 会自动提取 ID。

---

## 常用工作流示例

### 发布带图片的推文

```bash
# 1. 上传图片
xurl media upload photo.jpg
# 2. 从响应中复制 media_id，然后发布
xurl post "看看这张照片！" --media-id MEDIA_ID
```

### 参与对话回复

```bash
# 1. 读取帖子以理解内容背景
xurl read https://x.com/user/status/1234567890
# 2. 回复
xurl reply 1234567890 "这是我的看法..."
```

### 搜索并互动

```bash
# 1. 搜索感兴趣的主题帖子
xurl search "感兴趣的话题" -n 10
# 2. 为其中一个有趣的帖子点赞
xurl like 得到的帖子ID
# 3. 回复该帖子
xurl reply 得到的帖子ID "说得好！"
```

---

## 注意事项

- **频率限制 (Rate limits):** X API 对每个端点强制执行频率限制。如果您收到 429 错误，请等待后重试。写操作（发布、回复、点赞、转推）的限制比读操作更严格。
- **权限范围 (Scopes):** OAuth 2.0 令牌申请时带有广泛的权限。如果您在执行特定操作时收到 403 错误，可能是您的令牌缺少所需权限——请重新运行 `xurl auth oauth2` 以获取新令牌。
- **令牌存储:** `~/.xurl` 是 YAML 格式。每个应用存储自己的凭据和令牌。**绝对不要**读取或发送此文件给 LLM 会话。
