const { chromium } = require('D:/Rea-antigravity/node_modules/playwright-core');
const fs = require('fs');

async function main() {
  console.log('Launching browser to verify clone...');
  const browser = await chromium.launch({
    executablePath: 'C:/Program Files/Google/Chrome/Application/chrome.exe',
    headless: true,
    args: ['--no-sandbox']
  });

  const page = await browser.newPage({
    viewport: { width: 1280, height: 800 }
  });

  const errors = [];
  page.on('console', msg => {
    if (msg.type() === 'error') {
      errors.push(msg.text());
      console.log('Browser console error:', msg.text());
    }
  });

  page.on('pageerror', err => {
    errors.push(err.message);
    console.log('Page error:', err.message);
  });

  console.log('Navigating to http://localhost:8080/templates/mangalammoments/v1/preview?draft=1 ...');
  await page.goto('http://localhost:8080/templates/mangalammoments/v1/preview?draft=1', {
    waitUntil: 'networkidle',
    timeout: 30000
  });

  // Wait 4 seconds for react to mount and render
  await page.waitForTimeout(4000);

  // Take screenshot 1: Before door open
  await page.screenshot({ path: 'd:/Clone Website/Second/test_screenshot_1_gate.png' });
  console.log('Saved screenshot 1: gate/door');

  // Check if door/gate is present and click it
  const doorLocator = page.locator('text=Tap to open the door').first();
  if (await doorLocator.count() > 0) {
    console.log('Door trigger element found by text, clicking to open door...');
    await doorLocator.click();
    await page.waitForTimeout(3000);
  } else {
    const classLocator = page.locator('[class*="_gateTap"]').first();
    if (await classLocator.count() > 0) {
      console.log('Door trigger element found by class, clicking...');
      await classLocator.click();
      await page.waitForTimeout(3000);
    } else {
      console.log('Clicking center of screen...');
      await page.mouse.click(640, 400);
      await page.waitForTimeout(3000);
    }
  }

  // Take screenshot 2: After door open
  await page.screenshot({ path: 'd:/Clone Website/Second/test_screenshot_2_opened.png' });
  console.log('Saved screenshot 2: opened invitation');

  // Scroll down smoothly to trigger scroll animations
  await page.evaluate(async () => {
    window.scrollBy({ top: 800, behavior: 'smooth' });
  });
  await page.waitForTimeout(2000);
  await page.screenshot({ path: 'd:/Clone Website/Second/test_screenshot_3_scrolled.png' });
  console.log('Saved screenshot 3: scrolled');

  // Check Watermark presence
  const wmHost = await page.$('[data-wm-host]');
  const wmMeshes = await page.$$('.wm-10kkvf, [class*="_mark_1rkxo"], [class*="_mesh_1rkxo"]');
  const wmPills = await page.$$('[class*="_pill_1rkxo"]');
  console.log('Watermark check:');
  console.log('  [data-wm-host] count:', wmHost ? 1 : 0);
  console.log('  .wm-10kkvf meshes count:', wmMeshes.length);
  console.log('  Pill count:', wmPills.length);

  // Check BrandCard presence
  const brandCard = await page.$('[class*="_brandCard"]');
  const brandLogo = await page.$('[class*="_brandLogo"]');
  const ctaDock = await page.$('[class*="_ctaDock"]');
  console.log('Brand card check:');
  console.log('  BrandCard count:', brandCard ? 1 : 0);
  console.log('  BrandLogo count:', brandLogo ? 1 : 0);
  console.log('  CTADock count:', ctaDock ? 1 : 0);

  // Check Couple Name & Date text
  const bodyText = await page.innerText('body');
  const hasVinay = bodyText.includes('Vinay');
  const hasIsha = bodyText.includes('Isha');
  const hasDate = bodyText.includes('16 February 2027') || bodyText.includes('February 2027');
  const hasVenue = bodyText.includes('Bika Banquet');
  const hasWedInviteText = /WedInvite/i.test(bodyText);

  console.log('Content check:');
  console.log('  Has Vinay:', hasVinay);
  console.log('  Has Isha:', hasIsha);
  console.log('  Has 16 February 2027:', hasDate);
  console.log('  Has Bika Banquet:', hasVenue);
  console.log('  Has "WedInvite" visible in text:', hasWedInviteText);

  await browser.close();
  console.log('Verification completed successfully!');
}

main().catch(err => {
  console.error('Verification failed:', err);
  process.exit(1);
});
