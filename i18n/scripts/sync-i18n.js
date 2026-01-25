import { readFileSync, writeFileSync } from 'fs';
import { join, dirname } from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

const marketplaceFile = join(__dirname, '../../.claude-plugin/marketplace.json');
const zhCNFile = join(__dirname, '../locales/marketplace.zh.json');
const enFile = join(__dirname, '../locales/marketplace.en.json');

console.log('🔄 Syncing i18n translations...\n');

try {
  // Read data/marketplace.json
  const marketplace = JSON.parse(readFileSync(marketplaceFile, 'utf8'));

  // Read i18n files
  const zhCN = JSON.parse(readFileSync(zhCNFile, 'utf8'));
  const en = JSON.parse(readFileSync(enFile, 'utf8'));

  // Ensure skills object exists
  if (!zhCN.skills) zhCN.skills = {};
  if (!en.skills) en.skills = {};

  let addedCount = 0;
  const addedSkills = [];

  // Process each plugin in marketplace
  for (const plugin of marketplace.plugins) {
    const skillId = plugin.name;

    // Check if translation exists
    if (!zhCN.skills[skillId]) {
      // Add English translation (use original description)
      en.skills[skillId] = {
        name: formatSkillName(skillId),
        description: plugin.description
      };

      // Add Chinese placeholder (needs manual translation)
      zhCN.skills[skillId] = {
        name: `[待翻译] ${formatSkillName(skillId)}`,
        description: `[需要翻译] ${plugin.description}`
      };

      addedSkills.push(skillId);
      addedCount++;
    }
  }

  // Sort skills alphabetically
  zhCN.skills = sortObject(zhCN.skills);
  en.skills = sortObject(en.skills);

  // Write back to files
  writeFileSync(zhCNFile, JSON.stringify(zhCN, null, 2) + '\n', 'utf8');
  writeFileSync(enFile, JSON.stringify(en, null, 2) + '\n', 'utf8');

  if (addedCount > 0) {
    console.log(`✅ Added ${addedCount} new skill(s) to i18n:\n`);
    addedSkills.forEach(skill => console.log(`   - ${skill}`));
    console.log('\n⚠️  Please translate the Chinese placeholders marked with [待翻译] and [需要翻译]');
  } else {
    console.log('✅ All skills are already translated');
  }

  console.log(`\n📊 Total skills: ${marketplace.plugins.length}`);

} catch (error) {
  console.error('❌ Failed to sync i18n:', error.message);
  process.exit(1);
}

/**
 * Format skill ID to readable name
 * Example: "algorithmic-art" -> "Algorithmic Art"
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
