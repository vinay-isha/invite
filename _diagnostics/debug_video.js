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

  // Check button prompt
  const btn = page.locator('button:has-text("Tap to open the door")').first();
  console.log('Button found:', await btn.count());
  if (await btn.count() > 0) {
    await btn.click();
    console.log('Clicked button!');
  }

  // Poll video status every second for 8 seconds
  for (let s = 1; s <= 8; s++) {
    await page.waitForTimeout(1000);
    const videoStats = await page.evaluate(() => {
      const v = document.querySelector('video');
      if (!v) return { exists: false };
      return {
        exists: true,
        paused: v.paused,
        currentTime: v.currentTime,
        duration: v.duration,
        readyState: v.readyState,
        ended: v.ended,
        src: v.currentSrc
      };
    });
    console.log(`Second ${s} video stats:`, videoStats);
    const wrapLocked = await page.evaluate(() => {
      const wrap = document.querySelector('[class*="_wrap_"]');
      return wrap ? wrap.className : null;
    });
    console.log(`Second ${s} wrap classes:`, wrapLocked);
  }

  await browser.close();
}

main().catch(console.error);
