# ================================================================
# Skill Box 安全审查脚本 (Security Audit Script)
# ================================================================
# 用途: 自动扫描外部技能中的潜在安全风险
# 使用: .\scripts\security-audit.ps1 -TargetPath ".\skills_incoming"
# ================================================================

param(
    [Parameter(Mandatory=$true)]
    [string]$TargetPath,
    
    [Parameter(Mandatory=$false)]
    [switch]$DetailedOutput,
    
    [Parameter(Mandatory=$false)]
    [switch]$GenerateReport
)

# 颜色输出函数
function Write-ColorOutput {
    param(
        [string]$Message,
        [string]$Color = "White"
    )
    Write-Host $Message -ForegroundColor $Color
}

# 风险级别定义
$RiskLevels = @{
    Critical = @{ Color = "Red"; Emoji = "🔴"; Score = 10 }
    High     = @{ Color = "Yellow"; Emoji = "🟡"; Score = 7 }
    Medium   = @{ Color = "Cyan"; Emoji = "🟠"; Score = 4 }
    Low      = @{ Color = "Green"; Emoji = "🟢"; Score = 1 }
    Safe     = @{ Color = "Green"; Emoji = "✅"; Score = 0 }
}

# 初始化结果
$AuditResults = @{
    SkillsScanned = 0
    TotalRiskScore = 0
    Findings = @()
    DangerSkills = @()
    SafeSkills = @()
}

Write-ColorOutput "`n🔍 Skill Box 安全审查工具" "Cyan"
Write-ColorOutput "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" "Cyan"
Write-ColorOutput "扫描目录: $TargetPath`n" "Gray"

# 检查目标路径是否存在
if (-not (Test-Path $TargetPath)) {
    Write-ColorOutput "错误: 目标路径不存在 - $TargetPath" "Red"
    exit 1
}

# 查找所有SKILL.md文件
$SkillPaths = Get-ChildItem -Path $TargetPath -Recurse -Filter "SKILL.md" | Select-Object -ExpandProperty Directory

Write-ColorOutput "发现 $($SkillPaths.Count) 个技能待审查...`n" "Cyan"

# 定义可信来源（降低风险评分）
$TrustedAuthors = @("Anthropic", "Vercel Labs")

# 尝试读取marketplace.json获取author信息
$AuthorMap = @{}
$MarketplaceJson = Join-Path (Split-Path $TargetPath -Parent) ".claude-plugin\marketplace.json"
if (Test-Path $MarketplaceJson) {
    try {
        $Marketplace = Get-Content $MarketplaceJson -Raw -Encoding UTF8 | ConvertFrom-Json
        foreach ($Plugin in $Marketplace.plugins) {
            $Skills = $Plugin.skills
            foreach ($SkillPath in $Skills) {
                $SkillName = Split-Path $SkillPath -Leaf
                if ($Plugin.author) {
                    $AuthorMap[$SkillName] = $Plugin.author.name
                } elseif ($Plugin.authors) {
                    $AuthorMap[$SkillName] = ($Plugin.authors | Select-Object -First 1).name
                }
            }
        }
        Write-ColorOutput "✓ 已加载 $($AuthorMap.Count) 个技能的作者信息`n" "Green"
    } catch {
        Write-ColorOutput "⚠ 无法读取marketplace.json，将不应用可信来源优化`n" "Yellow"
    }
}

foreach ($SkillDir in $SkillPaths) {
    $SkillName = $SkillDir.Name
    $SkillRiskScore = 0
    $SkillFindings = @()
    $SkillAuthor = $AuthorMap[$SkillName]
    $IsTrusted = $SkillAuthor -in $TrustedAuthors
    
    Write-ColorOutput "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" "Gray"
    Write-ColorOutput "📦 检查技能: $SkillName" "White"
    Write-ColorOutput "路径: $($SkillDir.FullName)" "Gray"
    Write-ColorOutput ""
    
    # ===== 检查1: 可执行文件 =====
    Write-ColorOutput "  [1/6] 扫描可执行文件..." "Gray"
    $ExecutableFiles = Get-ChildItem -Path $SkillDir.FullName -Recurse -Include *.py,*.sh,*.ps1,*.bat,*.exe,*.cmd -ErrorAction SilentlyContinue
    
    if ($ExecutableFiles) {
        $ExecutableCount = $ExecutableFiles.Count
        $RiskLevel = if ($ExecutableCount -gt 5) { "High" } elseif ($ExecutableCount -gt 2) { "Medium" } else { "Low" }
        $RiskInfo = $RiskLevels[$RiskLevel]
        
        $Finding = @{
            Category = "可执行文件"
            Level = $RiskLevel
            Message = "发现 $ExecutableCount 个可执行文件"
            Files = $ExecutableFiles | Select-Object -ExpandProperty Name
        }
        $SkillFindings += $Finding
        
        # 可信来源折扣
        $Score = $RiskInfo.Score
        if ($IsTrusted) {
            $Score = [math]::Ceiling($Score * 0.5)  # 50%折扣
        }
        $SkillRiskScore += $Score
        
        $TrustLabel = if ($IsTrusted) { " (可信来源: $SkillAuthor)" } else { "" }
        Write-ColorOutput "    $($RiskInfo.Emoji) ${RiskLevel}: $($Finding.Message)$TrustLabel" $RiskInfo.Color
        if ($DetailedOutput) {
            $ExecutableFiles | ForEach-Object { Write-ColorOutput "      - $($_.Name)" "Gray" }
        }
    } else {
        Write-ColorOutput "    ✅ 未发现可执行文件" "Green"
    }
    
    # ===== 检查2: 硬编码凭据 =====
    Write-ColorOutput "  [2/6] 扫描硬编码凭据..." "Gray"
    $CredentialPatterns = @(
        "(api[_-]?key|apikey)\s*[:=]\s*['\`"][\w-]{20,}['\`"]",
        "(secret|token|password)\s*[:=]\s*['\`"][\w-]{10,}['\`"]",
        "(bearer|authorization)\s*[:=]\s*['\`"][\w.-]{20,}['\`"]"
    )
    
    $CredentialMatches = @()
    foreach ($Pattern in $CredentialPatterns) {
        $Matches = Select-String -Path "$($SkillDir.FullName)\*.*" -Pattern $Pattern -CaseSensitive:$false -ErrorAction SilentlyContinue
        if ($Matches) {
            $CredentialMatches += $Matches
        }
    }
    
    if ($CredentialMatches) {
        $Finding = @{
            Category = "硬编码凭据"
            Level = "Critical"
            Message = "发现 $($CredentialMatches.Count) 处疑似硬编码凭据"
            Details = $CredentialMatches | Select-Object -First 3 | ForEach-Object { "$($_.Filename):$($_.LineNumber)" }
        }
        $SkillFindings += $Finding
        $SkillRiskScore += $RiskLevels["Critical"].Score
        
        Write-ColorOutput "    🔴 Critical: $($Finding.Message)" "Red"
        if ($DetailedOutput) {
            $Finding.Details | ForEach-Object { Write-ColorOutput "      - $_" "Gray" }
        }
    } else {
        Write-ColorOutput "    ✅ 未发现硬编码凭据" "Green"
    }
    
    # ===== 检查3: 外部网络调用 =====
    Write-ColorOutput "  [3/6] 扫描外部网络调用..." "Gray"
    $NetworkPatterns = @(
        "requests\.(get|post|put|delete|patch)",
        "urllib\.request",
        "fetch\(|axios\.",
        "Invoke-WebRequest|Invoke-RestMethod"
    )
    
    # 排除模式：XML命名空间、标准URL、文档链接
    $ExcludePatterns = @(
        "http://schemas\.",           # XML schemas (Office OOXML)
        "http://www\.w3\.org/",       # W3C standards
        "https?://github\.com",       # GitHub links
        "https?://localhost",         # Local development
        "https?://127\.0\.0\.1"       # Local IP
    )
    
    $NetworkMatches = @()
    foreach ($Pattern in $NetworkPatterns) {
        $Matches = Select-String -Path "$($SkillDir.FullName)\*.*" -Pattern $Pattern -CaseSensitive:$false -ErrorAction SilentlyContinue
        if ($Matches) {
            # 过滤掉排除模式
            $FilteredMatches = $Matches | Where-Object {
                $line = $_.Line
                $isExcluded = $false
                foreach ($ExcludePattern in $ExcludePatterns) {
                    if ($line -match $ExcludePattern) {
                        $isExcluded = $true
                        break
                    }
                }
                -not $isExcluded
            }
            if ($FilteredMatches) {
                $NetworkMatches += $FilteredMatches
            }
        }
    }
    
    if ($NetworkMatches) {
        $UniqueFiles = $NetworkMatches | Select-Object -ExpandProperty Filename -Unique
        $RiskLevel = if ($UniqueFiles.Count -gt 3) { "High" } else { "Medium" }
        $RiskInfo = $RiskLevels[$RiskLevel]
        
        $Finding = @{
            Category = "外部网络调用"
            Level = $RiskLevel
            Message = "在 $($UniqueFiles.Count) 个文件中发现网络调用"
            Files = $UniqueFiles | Split-Path -Leaf
        }
        $SkillFindings += $Finding
        $SkillRiskScore += $RiskInfo.Score
        
        Write-ColorOutput "    $($RiskInfo.Emoji) ${RiskLevel}: $($Finding.Message)" $RiskInfo.Color
        if ($DetailedOutput) {
            $Finding.Files | ForEach-Object { Write-ColorOutput "      - $_" "Gray" }
        }
    } else {
        Write-ColorOutput "    ✅ 未发现外部网络调用" "Green"
    }
    
    # ===== 检查4: 危险系统操作 =====
    Write-ColorOutput "  [4/6] 扫描危险系统操作..." "Gray"
    $DangerousOps = @(
        "rm\s+-rf",
        "Remove-Item\s+-Recurse",
        "del\s+/s\s+/q",
        "format\s+[a-z]:",
        "mkfs",
        "dd\s+if=",
        "chmod\s+777",
        "sudo\s+",
        "os\.system|subprocess\.call|exec\("
    )
    
    $DangerousMatches = @()
    foreach ($Pattern in $DangerousOps) {
        $Matches = Select-String -Path "$($SkillDir.FullName)\*.*" -Pattern $Pattern -CaseSensitive:$false -ErrorAction SilentlyContinue
        if ($Matches) {
            $DangerousMatches += $Matches
        }
    }
    
    if ($DangerousMatches) {
        $Finding = @{
            Category = "危险系统操作"
            Level = "Critical"
            Message = "发现 $($DangerousMatches.Count) 处危险系统操作"
            Details = $DangerousMatches | Select-Object -First 3 | ForEach-Object { "$($_.Filename):$($_.LineNumber)" }
        }
        $SkillFindings += $Finding
        $SkillRiskScore += $RiskLevels["Critical"].Score
        
        Write-ColorOutput "    🔴 Critical: $($Finding.Message)" "Red"
        if ($DetailedOutput) {
            $Finding.Details | ForEach-Object { Write-ColorOutput "      - $_" "Gray" }
        }
    } else {
        Write-ColorOutput "    ✅ 未发现危险系统操作" "Green"
    }
    
    # ===== 检查5: 权限提升请求 =====
    Write-ColorOutput "  [5/6] 扫描权限提升请求..." "Gray"
    $ElevationPatterns = @(
        "sudo\s+(?!apt|yum|brew)",  # sudo 后面不是包管理器（更精确）
        "administrator",
        "root\s+(?!cause|directory)",  # root后面不是其他含义
        "elevated",
        "runas",
        "UAC"
    )
    
    $SkillMd = Get-Content "$($SkillDir.FullName)\SKILL.md" -Raw -ErrorAction SilentlyContinue
    $ElevationFound = $false
    
    if ($SkillMd) {
        # 排除安装说明章节（Dependencies, Installation, Prerequisites, Setup）
        $InstallSectionPattern = "(?ms)##\s+(Dependencies|Installation|Prerequisites|Setup|Requirements).*?(?=\n##|\z)"
        $ContentWithoutInstall = $SkillMd -replace $InstallSectionPattern, ""
        
        # 也排除YAML frontmatter中的工具声明
        $ContentWithoutFrontmatter = $ContentWithoutInstall -replace "(?ms)^---.*?---\n", ""
        
        foreach ($Pattern in $ElevationPatterns) {
            if ($ContentWithoutFrontmatter -match $Pattern) {
                $ElevationFound = $true
                break
            }
        }
    }
    
    if ($ElevationFound) {
        $Finding = @{
            Category = "权限提升"
            Level = "High"
            Message = "SKILL.md中提及需要管理员/root权限"
        }
        $SkillFindings += $Finding
        $SkillRiskScore += $RiskLevels["High"].Score
        
        Write-ColorOutput "    🟡 High: $($Finding.Message)" "Yellow"
    } else {
        Write-ColorOutput "    ✅ 未要求权限提升" "Green"
    }
    
    # ===== 检查6: Python依赖包 =====
    Write-ColorOutput "  [6/6] 扫描Python依赖包..." "Gray"
    $RequirementsFile = Get-ChildItem -Path $SkillDir.FullName -Filter "requirements.txt" -ErrorAction SilentlyContinue
    
    if ($RequirementsFile) {
        $Requirements = Get-Content $RequirementsFile.FullName
        $SuspiciousPackages = @("pycrypto", "fabric", "paramiko", "scrapy")
        
        $FoundSuspicious = $Requirements | Where-Object { 
            $pkg = $_
            $SuspiciousPackages | Where-Object { $pkg -match $_ }
        }
        
        if ($FoundSuspicious) {
            $Finding = @{
                Category = "可疑依赖包"
                Level = "Medium"
                Message = "发现 $($FoundSuspicious.Count) 个需要注意的依赖包"
                Details = $FoundSuspicious
            }
            $SkillFindings += $Finding
            $SkillRiskScore += $RiskLevels["Medium"].Score
            
            Write-ColorOutput "    🟠 Medium: $($Finding.Message)" "Cyan"
            if ($DetailedOutput) {
                $Finding.Details | ForEach-Object { Write-ColorOutput "      - $_" "Gray" }
            }
        } else {
            Write-ColorOutput "    ✅ 依赖包检查通过 ($($Requirements.Count) packages)" "Green"
        }
    } else {
        Write-ColorOutput "    ℹ️  无requirements.txt文件" "Gray"
    }
    
    # ===== 生成技能评分和建议 =====
    Write-ColorOutput ""
    $OverallRisk = if ($SkillRiskScore -ge 15) { "Critical" } 
                   elseif ($SkillRiskScore -ge 10) { "High" }
                   elseif ($SkillRiskScore -ge 5) { "Medium" }
                   elseif ($SkillRiskScore -gt 0) { "Low" }
                   else { "Safe" }
    
    $RiskInfo = $RiskLevels[$OverallRisk]
    
    Write-ColorOutput "  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" "Gray"
    Write-ColorOutput "  📊 风险评分: $SkillRiskScore 分 | 风险级别: $($RiskInfo.Emoji) $OverallRisk" $RiskInfo.Color
    
    # 命名建议
    if ($OverallRisk -in @("Critical", "High")) {
        $SuggestedName = if ($SkillName -notmatch "^danger-") { "danger-$SkillName" } else { $SkillName }
        Write-ColorOutput "  ⚠️  命名建议: $SuggestedName" "Yellow"
        Write-ColorOutput "  💡 说明: 建议在插件名称添加'danger-'前缀，告知用户此技能涉及外部调用或系统操作" "Yellow"
        
        $AuditResults.DangerSkills += @{
            Name = $SkillName
            Path = $SkillDir.FullName
            RiskScore = $SkillRiskScore
            RiskLevel = $OverallRisk
            Findings = $SkillFindings
            SuggestedName = $SuggestedName
        }
    } else {
        Write-ColorOutput "  ✅ 此技能安全，可正常命名" "Green"
        $AuditResults.SafeSkills += @{
            Name = $SkillName
            RiskScore = $SkillRiskScore
            RiskLevel = $OverallRisk
        }
    }
    
    Write-ColorOutput ""
    
    $AuditResults.SkillsScanned++
    $AuditResults.TotalRiskScore += $SkillRiskScore
    $AuditResults.Findings += $SkillFindings
}

# ===== 生成总结报告 =====
Write-ColorOutput "`n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" "Cyan"
Write-ColorOutput "📋 审查总结" "Cyan"
Write-ColorOutput "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" "Cyan"
Write-ColorOutput "已扫描技能: $($AuditResults.SkillsScanned)" "White"
Write-ColorOutput "总风险评分: $($AuditResults.TotalRiskScore)" "White"
Write-ColorOutput "需要danger前缀: $($AuditResults.DangerSkills.Count)" "Yellow"
Write-ColorOutput "安全技能: $($AuditResults.SafeSkills.Count)" "Green"
Write-ColorOutput ""

if ($AuditResults.DangerSkills.Count -gt 0) {
    Write-ColorOutput "⚠️  需要添加danger前缀的技能:" "Yellow"
    foreach ($Skill in $AuditResults.DangerSkills) {
        Write-ColorOutput "  • $($Skill.Name) → $($Skill.SuggestedName) (风险: $($Skill.RiskLevel), 评分: $($Skill.RiskScore))" "Yellow"
    }
    Write-ColorOutput ""
}

# 生成报告文件
if ($GenerateReport) {
    $ReportPath = ".\security-audit-report-$(Get-Date -Format 'yyyyMMdd-HHmmss').md"
    
    $ReportContent = @"
# Skill Box 安全审查报告

**生成时间**: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')  
**扫描目录**: $TargetPath

---

## 📊 总览

- **已扫描技能**: $($AuditResults.SkillsScanned)
- **总风险评分**: $($AuditResults.TotalRiskScore)
- **需要danger前缀**: $($AuditResults.DangerSkills.Count)
- **安全技能**: $($AuditResults.SafeSkills.Count)

---

## ⚠️ 高风险技能

$( if ($AuditResults.DangerSkills.Count -eq 0) { "无" } else {
    $AuditResults.DangerSkills | ForEach-Object {
        @"

### $($_.Name)

- **建议命名**: ``$($_.SuggestedName)``
- **风险级别**: $($_.RiskLevel)
- **风险评分**: $($_.RiskScore)
- **发现问题**:
$( $_.Findings | ForEach-Object { "  - [$($_.Level)] $($_.Category): $($_.Message)" } | Out-String )

---
"@
    } | Out-String
})

## ✅ 安全技能

$( if ($AuditResults.SafeSkills.Count -eq 0) { "无" } else {
    $AuditResults.SafeSkills | ForEach-Object { "- $($_.Name) (评分: $($_.RiskScore))" } | Out-String
})

---

## 📝 后续建议

1. 对于需要danger前缀的技能，在marketplace.json中更新name字段
2. 在README.md的插件说明中添加风险警告
3. 在SKILL.md开头添加安全使用说明
4. 定期复查外部技能的更新

**自动化工具**: scripts/security-audit.ps1
"@

    $ReportContent | Out-File -FilePath $ReportPath -Encoding UTF8
    Write-ColorOutput "📄 报告已生成: $ReportPath" "Green"
}

Write-ColorOutput "`n✅ 审查完成！" "Green"
Write-ColorOutput "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━`n" "Cyan"

# 返回退出代码
if ($AuditResults.DangerSkills.Count -gt 0) {
    exit 2  # 有高风险技能
} elseif ($AuditResults.TotalRiskScore -gt 0) {
    exit 1  # 有一般风险
} else {
    exit 0  # 安全
}

