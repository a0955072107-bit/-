// 產生英文版 Gumroad 封面（1920×1080）與正方形縮圖（1000×1000）
// 用法：node scripts/covers/make.js [slug ...]   輸出到 sales/covers/en/
const { chromium } = require('playwright');
const fs = require('fs'), path = require('path');
const root = path.resolve(__dirname, '../..');
const data = JSON.parse(fs.readFileSync(path.join(__dirname, 'data.json'), 'utf8'));
const only = process.argv.slice(2);
const out = path.join(root, 'sales/covers/en'); fs.mkdirSync(out, { recursive: true });
const tmp = fs.mkdtempSync(path.join(require('os').tmpdir(), 'covers-'));
(async () => {
  const b = await chromium.launch();
  for (const d of data.filter(x => !only.length || only.includes(x.slug))) {
    const url = 'file://' + path.join(root, 'templates/en', d.slug, 'index.html');
    const dir = path.join(tmp, d.slug); fs.mkdirSync(dir);
    for (const [name, vp, mob] of [['desk.jpg', { width: 1440, height: 900 }, false], ['mob.jpg', { width: 390, height: 844 }, true]]) {
      const c = await b.newContext({ viewport: vp, deviceScaleFactor: 2, isMobile: mob, hasTouch: mob });
      const p = await c.newPage(); await p.goto(url, { waitUntil: 'networkidle' }); await p.waitForTimeout(1800);
      await p.screenshot({ path: path.join(dir, name), type: 'jpeg', quality: 90 }); await c.close();
    }
    fs.copyFileSync(path.join(__dirname, 'cover.html'), path.join(dir, 'cover.html'));
    for (const [sq, w, h, file] of [[0, 1920, 1080, `${d.slug}-cover.png`], [1, 1000, 1000, `${d.slug}-thumb.png`]]) {
      const c = await b.newContext({ viewport: { width: w, height: h }, deviceScaleFactor: 1 });
      const p = await c.newPage();
      await p.goto('file://' + path.join(dir, 'cover.html') + '?sq=' + sq + '&d=' + encodeURIComponent(JSON.stringify(d)), { waitUntil: 'networkidle' });
      await p.waitForSelector('body[data-ready]'); await p.waitForTimeout(200);
      await p.screenshot({ path: path.join(out, file) }); await c.close();
    }
    console.log('✓', d.slug);
  }
  await b.close(); fs.rmSync(tmp, { recursive: true, force: true });
})();
