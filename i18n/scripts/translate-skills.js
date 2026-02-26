#!/usr/bin/env node
/**
 * Skill Markdown Translation Automation
 *
 * 功能：
 * 1. 扫描所有 SKILL.md 文件
 * 2. 生成翻译任务文件（prompts.jsonl）
 * 3. 调用 Python GLM API 批量翻译
 * 4. 将翻译结果保存为 SKILL.zh.md
 */

import fs from 'fs';
import path from 'path';
import { execSync } from 'child_process';
import { fileURLToPath } from 'url';

// ES 模块中获取 __dirname
const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

// 配置
const CONFIG = {
    skillBoxDir: path.join(__dirname, '..', '..'),
    i18nSkillsDir: path.join(__dirname, '..', 'skills'),
    glmScriptsDir: process.env.GLM_API_CALLER_DIR
        ? path.join(process.env.GLM_API_CALLER_DIR, 'scripts')
        : path.join(__dirname, '..', '..', '..', 'Skill Box Website', 'glm-api-caller', 'scripts'),
    outputDir: path.join(__dirname, '..', '..', '..', '..', 'translations'),
    promptsFile: path.join(__dirname, '..', '..', '..', '..', 'translations', 'prompts.jsonl'),
    model: 'glm-4-flash',
    concurrency: 20
};


/**
 * 递归查找所有 SKILL.md 文件
 */
function findSkillFiles(dir) {
    const results = [];

    function traverse(currentDir) {
        const entries = fs.readdirSync(currentDir, { withFileTypes: true });

        for (const entry of entries) {
            const fullPath = path.join(currentDir, entry.name);

            if (entry.isDirectory()) {
                traverse(fullPath);
            } else if (entry.name === 'SKILL.md') {
                results.push(fullPath);
            }
        }
    }

    traverse(dir);
    return results;
}

/**
 * 生成翻译提示词
 */
function generateTranslationPrompt(content) {
    return `你是一个专业的技术文档翻译专家。请将以下 Markdown 文档从英文翻译成中文。

翻译要求：
1. 保持 Markdown 格式完全不变（包括标题、列表、代码块、链接等）
2. 保留 YAML frontmatter 部分不翻译（---之间的内容）
3. 技术术语保持专业性和准确性
4. 代码示例、命令、变量名不翻译
5. 保持原文的语气和风格
6. 翻译要符合中文表达习惯，但不要过度意译

请直接输出翻译后的完整 Markdown 文档，不要添加任何解释或说明。

---原文---
${content}`;
}

/**
 * 创建翻译任务文件
 */
function createTranslationTasks(skillFiles) {
    console.log(`\n📝 创建翻译任务...`);

    // 确保输出目录存在
    if (!fs.existsSync(CONFIG.outputDir)) {
        fs.mkdirSync(CONFIG.outputDir, { recursive: true });
    }

    // 生成 JSONL 格式的任务文件
    const tasks = [];
    const metadata = [];

    for (const filePath of skillFiles) {
        // 将 src/Skill-Box/category/skill-name/SKILL.md
        // 转换为 src/i18n/skills/category/skill-name/SKILL.zh.md
        const relativePath = path.relative(CONFIG.skillBoxDir, filePath);
        const zhFilePath = path.join(CONFIG.i18nSkillsDir, relativePath.replace('SKILL.md', 'SKILL.zh.md'));

        if (fs.existsSync(zhFilePath)) {
            console.log(`   ⏭️  跳过已翻译: ${relativePath}`);
            continue;
        }


        // 读取英文内容
        const content = fs.readFileSync(filePath, 'utf-8');

        // 生成翻译提示词
        const prompt = generateTranslationPrompt(content);

        // 保存任务和元数据
        tasks.push(JSON.stringify({ prompt }));
        metadata.push({
            index: tasks.length - 1,
            sourcePath: filePath,
            targetPath: zhFilePath,
            relativePath: path.relative(CONFIG.skillBoxDir, filePath)
        });
    }

    if (tasks.length === 0) {
        console.log('\n✅ 所有 skills 已翻译完成！');
        return null;
    }

    // 写入任务文件
    fs.writeFileSync(CONFIG.promptsFile, tasks.join('\n'), 'utf-8');

    // 写入元数据文件
    const metadataFile = path.join(CONFIG.outputDir, 'metadata.json');
    fs.writeFileSync(metadataFile, JSON.stringify(metadata, null, 2), 'utf-8');

    console.log(`   ✅ 已创建 ${tasks.length} 个翻译任务`);
    console.log(`   📄 任务文件: ${CONFIG.promptsFile}`);
    console.log(`   📋 元数据文件: ${metadataFile}`);

    return metadata;
}

/**
 * 调用 Python GLM API 进行批量翻译
 */
function runBatchTranslation() {
    console.log(`\n🚀 开始批量翻译...`);
    console.log(`   模型: ${CONFIG.model}`);
    console.log(`   并发数: ${CONFIG.concurrency}`);

    const resultsDir = path.join(CONFIG.outputDir, 'results');
    const checkpointFile = path.join(CONFIG.outputDir, 'checkpoint.json');

    // 构建 Python 命令
    const pythonCmd = `python "${path.join(CONFIG.glmScriptsDir, 'batch_processor.py')}" --model ${CONFIG.model} --input "${CONFIG.promptsFile}" --output "${resultsDir}" --concurrency ${CONFIG.concurrency} --checkpoint "${checkpointFile}"`;

    try {
        // 执行 Python 脚本
        execSync(pythonCmd, {
            stdio: 'inherit',
            cwd: CONFIG.glmScriptsDir
        });

        console.log('\n✅ 批量翻译完成！');
        return true;
    } catch (error) {
        console.error('\n❌ 翻译过程中出错:', error.message);
        return false;
    }
}

/**
 * 保存翻译结果到对应的 SKILL.zh.md 文件
 */
function saveTranslations(metadata) {
    console.log(`\n💾 保存翻译结果...`);

    const resultsDir = path.join(CONFIG.outputDir, 'results');
    let successCount = 0;
    let errorCount = 0;

    for (const meta of metadata) {
        const resultFile = path.join(resultsDir, `result_${String(meta.index).padStart(6, '0')}.json`);

        if (!fs.existsSync(resultFile)) {
            console.log(`   ⚠️  结果文件不存在: ${meta.relativePath}`);
            errorCount++;
            continue;
        }

        try {
            // 读取翻译结果
            const result = JSON.parse(fs.readFileSync(resultFile, 'utf-8'));

            if (result.error) {
                console.log(`   ❌ 翻译失败: ${meta.relativePath} - ${result.error}`);
                errorCount++;
                continue;
            }

            if (!result.response) {
                console.log(`   ⚠️  无翻译内容: ${meta.relativePath}`);
                errorCount++;
                continue;
            }

            // 确保目标目录存在
            const targetDir = path.dirname(meta.targetPath);
            if (!fs.existsSync(targetDir)) {
                fs.mkdirSync(targetDir, { recursive: true });
            }

            // 保存翻译后的文件
            fs.writeFileSync(meta.targetPath, result.response, 'utf-8');
            console.log(`   ✅ ${meta.relativePath} → SKILL.zh.md`);
            successCount++;

        } catch (error) {
            console.log(`   ❌ 保存失败: ${meta.relativePath} - ${error.message}`);
            errorCount++;
        }
    }

    console.log(`\n📊 保存完成:`);
    console.log(`   成功: ${successCount}`);
    console.log(`   失败: ${errorCount}`);
}

/**
 * 主流程
 */
function main() {
    console.log('='.repeat(70));
    console.log('Skill Markdown Translation Automation');
    console.log('='.repeat(70));

    try {
        // 1. 查找所有 SKILL.md 文件
        console.log(`\n🔍 扫描 Skill-Box 目录...`);
        const skillFiles = findSkillFiles(CONFIG.skillBoxDir);
        console.log(`   找到 ${skillFiles.length} 个 SKILL.md 文件`);

        // 2. 创建翻译任务
        const metadata = createTranslationTasks(skillFiles);
        if (!metadata) {
            return;
        }

        // 3. 执行批量翻译
        const success = runBatchTranslation();
        if (!success) {
            console.log('\n⚠️  翻译未完全成功，请检查错误信息');
            console.log('   可以使用 --resume 参数继续翻译');
            return;
        }

        // 4. 保存翻译结果
        saveTranslations(metadata);

        console.log('\n' + '='.repeat(70));
        console.log('✅ 全部完成！');
        console.log('='.repeat(70));

    } catch (error) {
        console.error('\n❌ 错误:', error.message);
        console.error(error.stack);
        process.exit(1);
    }
}

// 运行主流程
main();
