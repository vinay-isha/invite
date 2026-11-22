const { chromium } = require('D:/Rea-antigravity/node_modules/playwright-core');

async function main() {
  const browser = await chromium.launch({
    executablePath: 'C:/Program Files/Google/Chrome/Application/chrome.exe',
    headless: true,
    args: ['--no-sandbox', '--autoplay-policy=no-user-gesture-required']
  });

  const page = await browser.newPage({ viewport: { width: 1280, height: 800 } });
  await page.goto('http://localhost:8080/templates/mangalammoments/v1/preview?draft=1', { waitUntil: 'networkidle' });
  await page.waitForTimeout(2000);

  const btn = page.locator('button:has-text("Tap to open the door")').first();
  if (await btn.count() > 0) await btn.click();
  await page.waitForTimeout(11500);

  // Scroll down
  for (let i = 0; i < 20; i++) {
    await page.evaluate(() => window.scrollBy(0, 800));
    await page.waitForTimeout(100);
  }

  const text = await page.innerText('body');
  console.log('--- ALL UNLOCKED TEXT ---');
  console.log(text);

  await browser.close();
}

main().catch(console.error);
