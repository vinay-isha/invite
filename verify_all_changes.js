const { chromium } = require('D:/Rea-antigravity/node_modules/playwright-core');

async function main() {
  console.log('Starting verification of requested changes...');
  const browser = await chromium.launch({
    executablePath: 'C:/Program Files/Google/Chrome/Application/chrome.exe',
    headless: true,
    args: ['--no-sandbox', '--autoplay-policy=no-user-gesture-required']
  });

  const page = await browser.newPage({ viewport: { width: 1280, height: 950 } });

  await page.goto('http://localhost:8080/', { waitUntil: 'networkidle', timeout: 30000 });
  await page.waitForTimeout(3000);

  // 1. Open doors
  const btn = page.locator('button:has-text("Tap to open the door")').first();
  if (await btn.count() > 0) {
    console.log('   Tapping door to open...');
    await btn.click();
  }
  await page.waitForTimeout(12000);

  // 2. Take screenshot of Page 1 (First page with Ganesha motif at top)
  await page.screenshot({ path: 'd:/Clone Website/Second/verify_p1_ganesha.png' });
  console.log('   Saved verify_p1_ganesha.png');

  // 3. Scroll to Page 3 (Blessings / Invitation)
  await page.evaluate(() => {
    window.scrollTo({ top: 1650, behavior: 'instant' });
  });
  await page.waitForTimeout(1000);
  await page.screenshot({ path: 'd:/Clone Website/Second/verify_p3_blessings.png' });
  console.log('   Saved verify_p3_blessings.png');

  // 4. Scroll to Page 3.5 (Family Lineage - between Page 3 and Page 4)
  await page.evaluate(() => {
    window.scrollTo({ top: 2500, behavior: 'instant' });
  });
  await page.waitForTimeout(1000);
  await page.screenshot({ path: 'd:/Clone Website/Second/verify_p3_5_lineage.png' });
  console.log('   Saved verify_p3_5_lineage.png');

  // 5. Scroll to Page 4 (Gallery / Our Memories)
  await page.evaluate(() => {
    window.scrollTo({ top: 3350, behavior: 'instant' });
  });
  await page.waitForTimeout(1000);
  await page.screenshot({ path: 'd:/Clone Website/Second/verify_p4_gallery.png' });
  console.log('   Saved verify_p4_gallery.png');

  // 6. Scroll to Footer
  await page.evaluate(() => {
    window.scrollTo({ top: document.body.scrollHeight, behavior: 'instant' });
  });
  await page.waitForTimeout(1000);
  await page.screenshot({ path: 'd:/Clone Website/Second/verify_p_footer.png' });
  console.log('   Saved verify_p_footer.png');

  // 7. Verify DOM Order
  const domOrder = await page.evaluate(() => {
    const container = document.querySelector('[class*="unlockedSections"]');
    if (!container) return [];
    return Array.from(container.children).map(c => {
      const text = c.innerText ? c.innerText.replace(/\n/g, ' ').substring(0, 50) : '';
      return { id: c.id, tag: c.tagName, text };
    });
  });

  console.log('7. Unlocked sections DOM order:');
  domOrder.forEach((item, idx) => console.log(`   [${idx}] id="${item.id}" tag=<${item.tag}>: ${item.text}`));

  await browser.close();
  console.log('All verifications finished successfully!');
}

main().catch(err => {
  console.error('Verification failed:', err);
  process.exit(1);
});
