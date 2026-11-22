const { chromium } = require('D:/Rea-antigravity/node_modules/playwright-core');

async function main() {
  const browser = await chromium.launch({
    executablePath: 'C:/Program Files/Google/Chrome/Application/chrome.exe',
    headless: true,
    args: ['--no-sandbox', '--autoplay-policy=no-user-gesture-required']
  });

  const page = await browser.newPage({ viewport: { width: 1280, height: 800 } });

  await page.goto('http://localhost:8080/templates/mangalammoments/v1/preview?draft=1', {
    waitUntil: 'networkidle',
    timeout: 30000
  });

  await page.waitForTimeout(3000);

  const btn = page.locator('button:has-text("Tap to open the door")').first();
  if (await btn.count() > 0) {
    await btn.click();
    console.log('Clicked door button, waiting 11.5s for door animation to finish...');
  }

  await page.waitForTimeout(11500);

  const wrapClasses = await page.evaluate(() => {
    const wrap = document.querySelector('[class*="_wrap_"]');
    return wrap ? wrap.className : null;
  });
  console.log('Wrap classes after door animation:', wrapClasses);

  const isUnlocked = !wrapClasses.includes('wrapLocked');
  console.log('Is page fully unlocked:', isUnlocked);

  // Scroll down
  await page.evaluate(async () => {
    for (let i = 0; i < 20; i++) {
      window.scrollBy(0, 500);
      await new Promise(r => setTimeout(r, 100));
    }
  });
  await page.waitForTimeout(2000);

  const text = await page.innerText('body');
  console.log('Text checks:');
  console.log('  Has Vinay & Isha:', text.includes('Vinay') && text.includes('Isha'));
  console.log('  Has 16 February 2027:', text.includes('16 February 2027') || text.includes('February 2027'));
  console.log('  Has Sangeet:', text.includes('Sangeet'));
  console.log('  Has Bika Banquet:', text.includes('Bika Banquet'));
  console.log('  Has WedInvite:', /WedInvite/i.test(text));

  await page.screenshot({ path: 'd:/Clone Website/Second/test_screenshot_fully_unlocked.png' });
  console.log('Saved test_screenshot_fully_unlocked.png');

  await browser.close();
}

main().catch(console.error);
