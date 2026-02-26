import { execSync } from 'child_process';
import { existsSync } from 'fs';
import { join, dirname } from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

const skillBoxDir = join(__dirname, '../../');

console.log('🔄 更新 Skill-Box 子模块...\n');

try {
    // 检查 Skill-Box 目录是否存在
    if (!existsSync(skillBoxDir)) {
        console.error('❌ Skill-Box 目录不存在:', skillBoxDir);
        console.log('ℹ️  请先克隆仓库:');
        console.log('   git clone https://github.com/Jst-Well-Dan/Skill-Box.git src/Skill-Box');
        process.exit(1);
    }

    // 检查是否为 git 仓库
    if (!existsSync(join(skillBoxDir, '.git'))) {
        console.error('❌ Skill-Box 不是一个 git 仓库');
        process.exit(1);
    }

    let currentCommit = '';
    console.log('📍 当前版本:');
    try {
        currentCommit = execSync('git log -1 --oneline', {
            cwd: skillBoxDir,
            encoding: 'utf-8'
        }).trim();
        console.log(`   ${currentCommit}\n`);
    } catch (err) {
        console.log('   (无法获取当前版本)\n');
    }

    // 拉取最新更新
    console.log('📥 拉取最新更新...');
    execSync('git pull origin master', {
        cwd: skillBoxDir,
        stdio: 'inherit'
    });

    console.log('\n📍 更新后版本:');
    const newCommit = execSync('git log -1 --oneline', {
        cwd: skillBoxDir,
        encoding: 'utf-8'
    }).trim();
    console.log(`   ${newCommit}\n`);

    // 检查是否有更新
    const status = execSync('git status --porcelain', {
        cwd: skillBoxDir,
        encoding: 'utf-8'
    }).trim();

    if (!status && currentCommit === newCommit) {
        console.log('✅ Skill-Box 已是最新版本\n');
    } else {
        console.log('✅ Skill-Box 更新成功！\n');

        // 显示文件变更
        try {
            console.log('📝 变更摘要:');
            const diffStat = execSync('git diff HEAD@{1} HEAD --stat', {
                cwd: skillBoxDir,
                encoding: 'utf-8'
            }).trim();
            if (diffStat) {
                console.log(diffStat);
            }
        } catch (err) {
            // Ignore diff errors
        }
    }

} catch (error) {
    console.error('\n❌ 更新失败:', error.message);
    console.log('\n💡 尝试手动更新:');
    console.log('   cd src/Skill-Box');
    console.log('   git pull origin master');
    process.exit(1);
}
