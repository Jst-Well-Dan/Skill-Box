import { existsSync } from 'fs';
import { dirname, join } from 'path';
import { fileURLToPath } from 'url';
import { execSync } from 'child_process';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

const skillBoxDir = join(__dirname, '../../');
const marketplaceFile = join(skillBoxDir, '.claude-plugin/marketplace.json');

async function syncMarketplace() {
  try {
    // Check if Skill-Box directory exists
    if (!existsSync(skillBoxDir)) {
      console.error('❌ Skill-Box directory not found at:', skillBoxDir);
      console.log('ℹ️  Please run: git clone https://github.com/Jst-Well-Dan/Skill-Box.git src/Skill-Box');
      process.exit(1);
    }

    // Check if marketplace.json exists
    if (!existsSync(marketplaceFile)) {
      console.error('❌ marketplace.json not found in Skill-Box/.claude-plugin/');
      process.exit(1);
    }

    console.log('🔄 Updating Skill-Box subproject from GitHub...');

    // Pull latest changes from Skill-Box repository
    execSync('git pull', {
      cwd: skillBoxDir,
      stdio: 'inherit'
    });

    console.log('✅ Skill-Box marketplace data synced successfully');

  } catch (error) {
    console.error('❌ Failed to sync Skill-Box:', error.message);

    // Check if marketplace file exists as fallback
    if (existsSync(marketplaceFile)) {
      console.log('ℹ️  Using existing local marketplace.json from Skill-Box');
    } else {
      console.error('❌ No local marketplace.json available');
      process.exit(1);
    }
  }
}

syncMarketplace();
