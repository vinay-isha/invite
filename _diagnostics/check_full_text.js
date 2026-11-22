const { chromium } = require('D:/Rea-antigravity/node_modules/playwright-core');

async function main() {
  const browser = await chromium.launch({
    executablePath: 'C:/Program Files/Google/Chrome/Application/chrome.exe',
    headless: true,
    args: ['--no-sandbox']
  });

  const page = await browser.newPage({
    viewport: { width: 1280, height: 800 }
  });

  await page.goto('http://localhost:8080/templates/mangalammoments/v1/preview?draft=1', {
    waitUntil: 'networkidle',
    timeout: 30000
  });

  await page.waitForTimeout(3000);

  // Click door to open
  const doorLocator = page.locator('text=Tap to open the door').first();
  if (await doorLocator.count() > 0) {
    await doorLocator.click();
    await page.waitForTimeout(3000);
  }

  // Scroll all the way to the bottom
  await page.evaluate(async () => {
    for (let i = 0; i < 10; i++) {
      window.scrollBy(0, 1000);
      await new Promise(r => setTimeout(r, 200));
    }
  });
  await page.waitForTimeout(2000);

  const text = await page.innerText('body');
  console.log('--- ALL BODY TEXT ---');
  console.log(text);

  await page.screenshot({ path: 'd:/Clone Website/Second/test_screenshot_4_bottom.png', fullPage: true });

  await browser.close();
}

main().catch(err => {
  console.error(err);
  process.exit(1);
});
