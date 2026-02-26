import { execSync } from 'child_process';
import { existsSync } from 'fs';
import { join, dirname } from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

console.log('╔════════════════════════════════════════════════════════════╗');
console.log('║     Skill-Box 自动更新 & 翻译工作流                         ║');
console.log('╚════════════════════════════════════════════════════════════╝\n');

const steps = [
    {
        name: '1️⃣  更新 Skill-Box 子模块',
        command: 'node src/Skill-Box/i18n/scripts/update-skillbox.js',
        required: true
    },
    {
        name: '2️⃣  同步 marketplace.json',
        command: 'node src/Skill-Box/i18n/scripts/sync-marketplace.js',
        required: true
    },
    {
        name: '3️⃣  同步 i18n 占位符',
        command: 'node src/Skill-Box/i18n/scripts/sync-i18n.js',
        required: true
    },
    {
        name: '4️⃣  翻译技能名称和描述',
        command: 'node src/Skill-Box/i18n/scripts/translate-i18n.js',
        required: false,
        checkEnv: () => {
            const envFile = process.env.GLM_API_CALLER_DIR 
                ? join(process.env.GLM_API_CALLER_DIR, '.env') 
                : join(__dirname, '../../../Skill Box Website/glm-api-caller/.env');
            if (!existsSync(envFile)) {
                return false;
            }
            return true;
        }
    },
    {
        name: '5️⃣  批量翻译 SKILL.md 文档',
        command: 'node src/Skill-Box/i18n/scripts/translate-skills.js',
        required: false,
        checkEnv: () => {
            const envFile = process.env.GLM_API_CALLER_DIR 
                ? join(process.env.GLM_API_CALLER_DIR, '.env') 
                : join(__dirname, '../../../Skill Box Website/glm-api-caller/.env');
            return existsSync(envFile);
        }
    }
];

async function runStep(step, index) {
    console.log(`\n${step.name}`);
    console.log('─'.repeat(62));

    // Check environment if needed
    if (step.checkEnv && !step.checkEnv()) {
        if (!step.required) {
            console.log('   ⏭️  跳过此步骤\n');
            return true;
        } else {
            console.log('   ❌ 环境检查失败\n');
            return false;
        }
    }

    try {
        execSync(step.command, {
            stdio: 'inherit',
            cwd: join(__dirname, '..')
        });
        console.log(`\n✅ ${step.name} 完成`);
        return true;
    } catch (error) {
        if (step.required) {
            console.error(`\n❌ ${step.name} 失败`);
            throw error;
        } else {
            console.log(`\n⚠️  ${step.name} 失败，但继续执行`);
            return false;
        }
    }
}

async function main() {
    const startTime = Date.now();
    let successCount = 0;
    let skipCount = 0;

    try {
        for (let i = 0; i < steps.length; i++) {
            const success = await runStep(steps[i], i);
            if (success) successCount++;
            else skipCount++;
        }

        const duration = ((Date.now() - startTime) / 1000).toFixed(1);

        console.log('\n╔════════════════════════════════════════════════════════════╗');
        console.log('║                    ✅ 全部完成！                           ║');
        console.log('╚════════════════════════════════════════════════════════════╝');
        console.log(`\n📊 统计:`);
        console.log(`   完成步骤: ${successCount}/${steps.length}`);
        if (skipCount > 0) {
            console.log(`   跳过步骤: ${skipCount}`);
        }
        console.log(`   总耗时: ${duration}s\n`);

        console.log('💡 下一步:');
        console.log('   1. 查看更改: git status');
        console.log('   2. 提交更改: git add . && git commit -m "chore: update skills"');
        console.log('   3. 推送远程: git push\n');

    } catch (error) {
        console.error('\n╔════════════════════════════════════════════════════════════╗');
        console.error('║                    ❌ 执行失败                             ║');
        console.error('╚════════════════════════════════════════════════════════════╝\n');
        console.error('错误:', error.message);
        console.log('\n💡 故障排查:');
        console.log('   1. 检查网络连接');
        console.log('   2. 验证 API Key 配置 (GLM_API_CALLER_DIR/.env 或默认路径)');
        console.log('   3. 查看详细日志');
        console.log('   4. 尝试单独运行失败的步骤\n');
        process.exit(1);
    }
}

main();
