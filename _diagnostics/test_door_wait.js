const { chromium } = require('D:/Rea-antigravity/node_modules/playwright-core');

async function main() {
  const browser = await chromium.launch({
    executablePath: 'C:/Program Files/Google/Chrome/Application/chrome.exe',
    headless: true,
    args: ['--no-sandbox']
  });

  const page = await browser.newPage({ viewport: { width: 1280, height: 800 } });

  await page.goto('http://localhost:8080/templates/mangalammoments/v1/preview?draft=1', {
    waitUntil: 'networkidle',
    timeout: 30000
  });

  await page.waitForTimeout(3000);

  // Click door
  const doorLocator = page.locator('text=Tap to open the door').first();
  if (await doorLocator.count() > 0) {
    console.log('Clicking door...');
    await doorLocator.click();
  }

  // Wait 7 seconds for door video animation to complete
  console.log('Waiting 7s for doors animation to finish...');
  await page.waitForTimeout(7000);

  // Now check unlocked sections
  const unlocked = await page.$('[class*="_unlockedSections"]');
  console.log('Unlocked sections container present:', !!unlocked);

  // Scroll down to venue and footer
  await page.evaluate(async () => {
    for (let i = 0; i < 15; i++) {
      window.scrollBy(0, 800);
      await new Promise(r => setTimeout(r, 150));
    }
  });
  await page.waitForTimeout(2000);

  const text = await page.innerText('body');
  console.log('Has Vinay & Isha:', text.includes('Vinay') && text.includes('Isha'));
  console.log('Has 16 February 2027:', text.includes('16 February 2027') || text.includes('February 2027'));
  console.log('Has Sangeet:', text.includes('Sangeet'));
  console.log('Has Bika Banquet:', text.includes('Bika Banquet'));
  console.log('Has WedInvite:', /WedInvite/i.test(text));

  await page.screenshot({ path: 'd:/Clone Website/Second/test_screenshot_unlocked.png' });
  console.log('Saved test_screenshot_unlocked.png');

  await browser.close();
}

main().catch(err => {
  console.error(err);
  process.exit(1);
});
