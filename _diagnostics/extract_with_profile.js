const { chromium } = require('D:/Rea-antigravity/node_modules/playwright-core');
const fs = require('fs');

async function main() {
  console.log('Launching browser with copied profile...');
  const context = await chromium.launchPersistentContext('d:/Clone Website/temp_profile', {
    executablePath: 'C:/Program Files/Google/Chrome/Application/chrome.exe',
    headless: true,
    args: ['--no-sandbox']
  });

  const page = context.pages().length > 0 ? context.pages()[0] : await context.newPage();
  
  console.log('Navigating to target URL...');
  await page.goto('https://wedinviteglobal.com/templates/mangalammoments/v1/preview?draft=1', {
    waitUntil: 'networkidle',
    timeout: 30000
  });

  // Wait a few seconds for all animations and drafts to settle
  await page.waitForTimeout(5000);

  // Extract localStorage
  const lsData = await page.evaluate(() => {
    const res = {};
    for (let i = 0; i < localStorage.length; i++) {
      const k = localStorage.key(i);
      res[k] = localStorage.getItem(k);
    }
    return res;
  });

  fs.writeFileSync('d:/Clone Website/Second/extracted_local_storage.json', JSON.stringify(lsData, null, 2));
  console.log('Saved localStorage keys:', Object.keys(lsData));

  // Extract settled rendered HTML
  const html = await page.content();
  fs.writeFileSync('d:/Clone Website/Second/settled_user_page.html', html);
  console.log('Saved settled HTML, length:', html.length);

  await context.close();
}

main().catch(err => {
  console.error('Error:', err);
  process.exit(1);
});
