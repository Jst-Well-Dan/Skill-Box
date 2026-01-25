#!/usr/bin/env node
/**
 * Unified i18n Sync & Translation Tool
 * 
 * Features:
 * 1. Syncs marketplace.json plugins to en.json/zh-CN.json
 * 2. Translates missing Chinese names and descriptions using GLM API
 */

import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import { execSync } from 'child_process';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

// Simple env loader to avoid dotenv dependency
function loadEnv() {
    const envPath = path.join(__dirname, '..', 'glm-api-caller', '.env');
    if (fs.existsSync(envPath)) {
        const content = fs.readFileSync(envPath, 'utf-8');
        content.split(/\r?\n/).forEach(line => {
            const cleanLine = line.split('#')[0].trim();
            if (cleanLine) {
                const [key, ...valueParts] = cleanLine.split('=');
                if (key) {
                    process.env[key.trim()] = valueParts.join('=').trim();
                }
            }
        });
    }
}
loadEnv();

const CONFIG = {
    marketplaceFile: path.join(__dirname, '..', '..', '.claude-plugin', 'marketplace.json'),
    zhCNFile: path.join(__dirname, '..', 'locales', 'marketplace.zh.json'),
    enFile: path.join(__dirname, '..', 'locales', 'marketplace.en.json'),
    glmScriptsDir: path.join(__dirname, '..', '..', '..', '..', 'glm-api-caller', 'scripts'),
    apiKey: process.env.GLM_API_KEY,
    model: 'glm-4-flash'
};

/**
 * Format skill ID to readable name
 */
function formatSkillName(id) {
    return id
        .split('-')
        .map(word => word.charAt(0).toUpperCase() + word.slice(1))
        .join(' ');
}

/**
 * Sort object keys alphabetically
 */
function sortObject(obj) {
    return Object.keys(obj)
        .sort()
        .reduce((result, key) => {
            result[key] = obj[key];
            return result;
        }, {});
}

async function translateText(text, type = 'description') {
    if (!CONFIG.apiKey || CONFIG.apiKey === 'your_actual_api_key_here' || CONFIG.apiKey === '') {
        return null;
    }

    console.log(`   🌐 正在通过 AI 翻译 ${type}: "${text.substring(0, 30)}..."`);

    const prompt = type === 'name'
        ? `请将以下 Claude 技能名称翻译成简洁的中文（3-6个字）："${text}"。直接输出翻译结果，不要带引号。`
        : `你是一个专业的技术翻译。请将以下 Claude 技能描述翻译成自然、流畅的中文，保持语气专业：\n\n"${text}"\n\n直接输出翻译后的文本，不要带解释。`;

    try {
        // Use python script to call GLM
        // prompt is a positional argument in call_glm_text.py
        const escapedPrompt = prompt.replace(/"/g, '\\"').replace(/\n/g, '\\n');
        const cmd = `python "${path.join(CONFIG.glmScriptsDir, 'call_glm_text.py')}" --model ${CONFIG.model} "${escapedPrompt}"`;
        const output = execSync(cmd, { encoding: 'utf-8' });

        // We expect the script to output the result as the last line or similar
        // For now, we take the whole trimmed output as result.
        // If the script has logging, we might need to filter it.
        return output.trim();
    } catch (error) {
        console.error(`   ❌ 翻译失败: ${error.message}`);
        return null;
    }
}

async function main() {
    console.log('🔄 开始 i18n 同步与翻译...\n');

    if (!fs.existsSync(CONFIG.marketplaceFile)) {
        console.error('❌ 找不到 marketplace.json');
        process.exit(1);
    }

    const marketplace = JSON.parse(fs.readFileSync(CONFIG.marketplaceFile, 'utf8'));
    const zhCN = JSON.parse(fs.readFileSync(CONFIG.zhCNFile, 'utf8'));
    const en = JSON.parse(fs.readFileSync(CONFIG.enFile, 'utf8'));

    if (!zhCN.skills) zhCN.skills = {};
    if (!en.skills) en.skills = {};

    let updateCount = 0;

    // Build a map of all skills from marketplace
    const allSkillsFromMarketplace = new Map();
    for (const plugin of marketplace.plugins) {
        // Add plugin itself
        allSkillsFromMarketplace.set(plugin.name, {
            name: formatSkillName(plugin.name),
            description: plugin.description
        });

        // Add individual skills
        for (const skillPath of plugin.skills) {
            const skillId = skillPath.split('/').pop();

            // Try to find a more specific description from SKILL.md if possible
            let skillDescription = plugin.description;
            let skillName = formatSkillName(skillId);

            try {
                // Determine path to SKILL.md
                // marketplace paths are like "./category/skill-name"
                const cleanPath = skillPath.replace(/^\.\//, '');
                const skillMdPath = path.join(__dirname, '..', 'src', 'Skill-Box', cleanPath, 'SKILL.md');
                const skillMdFile = path.join(__dirname, '..', 'src', 'Skill-Box', cleanPath + '.md');

                let mdContent = '';
                if (fs.existsSync(skillMdPath)) {
                    mdContent = fs.readFileSync(skillMdPath, 'utf8');
                } else if (fs.existsSync(skillMdFile)) {
                    mdContent = fs.readFileSync(skillMdFile, 'utf8');
                }

                if (mdContent) {
                    // Simple regex to extract name and description from YAML frontmatter
                    const nameMatch = mdContent.match(/^name:\s*(.*)$/m);
                    const descMatch = mdContent.match(/^description:\s*(.*)$/m);

                    if (nameMatch && nameMatch[1]) skillName = nameMatch[1].trim();
                    if (descMatch && descMatch[1]) skillDescription = descMatch[1].trim();
                }
            } catch (e) {
                // Ignore errors reading individual SKILL.md
            }

            allSkillsFromMarketplace.set(skillId, {
                name: skillName,
                description: skillDescription
            });
        }
    }

    // Process all identified skills
    for (const [id, data] of allSkillsFromMarketplace.entries()) {
        if (!en.skills[id]) {
            en.skills[id] = {
                name: data.name,
                description: data.description
            };
        }

        const currentZh = zhCN.skills[id];
        const isPlaceholder = currentZh && (currentZh.name.includes('[待翻译]') || currentZh.description.includes('[需要翻译]'));

        if (!currentZh || isPlaceholder) {
            console.log(`📍 处理项目: ${id}`);

            if (CONFIG.apiKey && CONFIG.apiKey !== 'your_actual_api_key_here' && CONFIG.apiKey !== '') {
                const translatedName = await translateText(data.name, 'name');
                const translatedDesc = await translateText(data.description, 'description');

                if (translatedName && translatedDesc) {
                    zhCN.skills[id] = {
                        name: translatedName,
                        description: translatedDesc
                    };
                    console.log(`   ✅ 翻译成功: ${translatedName}`);
                    updateCount++;
                } else {
                    console.log(`   ⚠️  翻译失败，保留占位符`);
                    if (!currentZh) {
                        zhCN.skills[id] = {
                            name: `[待翻译] ${data.name}`,
                            description: `[需要翻译] ${data.description}`
                        };
                    }
                }
            } else if (!currentZh) {
                zhCN.skills[id] = {
                    name: `[待翻译] ${data.name}`,
                    description: `[需要翻译] ${data.description}`
                };
                updateCount++;
            }
        }
    }

    zhCN.skills = sortObject(zhCN.skills);
    en.skills = sortObject(en.skills);

    fs.writeFileSync(CONFIG.zhCNFile, JSON.stringify(zhCN, null, 2) + '\n', 'utf8');
    fs.writeFileSync(CONFIG.enFile, JSON.stringify(en, null, 2) + '\n', 'utf8');

    console.log(`\n✅ 同步完成！共更新 ${updateCount} 项。`);
    if (!CONFIG.apiKey || CONFIG.apiKey === 'your_actual_api_key_here' || CONFIG.apiKey === '') {
        console.log('⚠️  未检测到有效的 GLM_API_KEY，仅生成占位符。');
    }
}

main().catch(err => {
    console.error('💥 脚本崩溃:', err);
    process.exit(1);
});
