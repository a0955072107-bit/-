// 產生 Pinterest 直式圖（1000×1500）：每款 3 張
//   a = 英文功能圖、b = 多語言切換圖、c = 日文圖
// 用法：node scripts/pins/make.js [slug ...]   輸出到 sales/pins/，並寫出 sales/pins/pins.csv
const { chromium } = require('playwright');
const fs = require('fs'), path = require('path');
const root = path.resolve(__dirname, '../..');
const data = JSON.parse(fs.readFileSync(path.join(__dirname, 'data.json'), 'utf8'));
const only = process.argv.slice(2);
const VARS = (process.env.VARIANTS || 'a,b,c').split(',');
const out = path.join(root, 'sales/pins'); fs.mkdirSync(out, { recursive: true });
const tmp = fs.mkdtempSync(path.join(require('os').tmpdir(), 'pins-'));

const shots = [
  ['en-desk.jpg', 'templates/en', { width: 1440, height: 900 }, false],
  ['en-mob.jpg', 'templates/en', { width: 390, height: 844 }, true],
  ['zh-mob.jpg', 'templates', { width: 390, height: 844 }, true],
  ['zh-desk.jpg', 'templates', { width: 1440, height: 900 }, false],
  ['ja-desk.jpg', 'templates/ja', { width: 1440, height: 900 }, false],
  ['ja-mob.jpg', 'templates/ja', { width: 390, height: 844 }, true],
];

(async () => {
  const b = await chromium.launch();
  for (const d of data.filter(x => !only.length || only.includes(x.slug))) {
    const name = d.slug.replace(/\//g, '-');
    const dir = path.join(tmp, name); fs.mkdirSync(dir);
    for (const [file, base, vp, mob] of shots) {
      const c = await b.newContext({ viewport: vp, deviceScaleFactor: 2, isMobile: mob, hasTouch: mob });
      const p = await c.newPage();
      await p.goto('file://' + path.join(root, base, d.slug, 'index.html'), { waitUntil: 'networkidle' });
      await p.waitForTimeout(d.wait || 1800);
      await p.screenshot({ path: path.join(dir, file), type: 'jpeg', quality: 88 });
      if (file === 'en-mob.jpg' && VARS.includes('d')) {
        // 整頁截圖：用「減少動態效果」讓捲動淡入的內容直接顯示
        const c2 = await b.newContext({ viewport: vp, deviceScaleFactor: 2, isMobile: true, hasTouch: true, reducedMotion: 'reduce' });
        const p2 = await c2.newPage(); await p2.goto('file://' + path.join(root, base, d.slug, 'index.html'), { waitUntil: 'networkidle' });
        for (let y = 0; y < 20000; y += 600) { await p2.evaluate(y => window.scrollTo(0, y), y); await p2.waitForTimeout(60); }
        await p2.evaluate(() => window.scrollTo(0, 0)); await p2.waitForTimeout(600);
        await p2.screenshot({ path: path.join(dir, 'en-full.jpg'), type: 'jpeg', quality: 85, fullPage: true }); await c2.close();
      }
      await c.close();
    }
    fs.copyFileSync(path.join(__dirname, 'pin.html'), path.join(dir, 'pin.html'));
    for (const v of VARS) {
      const c = await b.newContext({ viewport: { width: 1000, height: 1500 } });
      const p = await c.newPage();
      await p.goto('file://' + path.join(dir, 'pin.html') + '?v=' + v + '&d=' + encodeURIComponent(JSON.stringify(d)), { waitUntil: 'networkidle' });
      await p.waitForSelector('body[data-ready]'); await p.waitForTimeout(200);
      await p.screenshot({ path: path.join(out, `${name}-${v}.jpg`), type: 'jpeg', quality: 88 }); await c.close();
    }
    console.log('✓', d.slug);
  }
  await b.close(); fs.rmSync(tmp, { recursive: true, force: true });

  // 文字資料：標題、說明、連結、看板、關鍵字
  const q = s => '"' + String(s).replace(/"/g, '""') + '"';
  const rows = [['file', 'board', 'title', 'description', 'link', 'keywords']];
  for (const d of data) {
    const name = d.slug.replace(/\//g, '-'), cat = d.cat, langs = d.es ? 'English, Chinese, Japanese and Spanish' : 'English, Chinese and Japanese';
    const motion = d.slug.startsWith('motion/');
    const kw = `${cat.toLowerCase()} website template, html website template, small business website, one page website, ${motion ? 'animated website template' : 'landing page template'}`;
    rows.push([`${name}-a.jpg`, motion ? 'Animated Website Templates' : 'Small Business Website Templates',
      `${cat} Website Template — HTML, No Monthly Fees`,
      `A ready-to-launch ${cat.toLowerCase()} website you own forever. Mobile-friendly, edit in any text editor, upload free to Netlify or GitHub Pages. Includes ${langs} versions and a step-by-step guide. ${d.pills.join(' · ')}.`,
      d.url, kw]);
    rows.push([`${name}-b.jpg`, 'Multilingual Website Templates',
      `${cat} Website in ${d.es ? 'Five' : 'Four'} Languages — One-Tap Language Switcher`,
      `Serve every customer in their own language: English, Traditional and Simplified Chinese, Japanese${d.es ? ' and Spanish' : ''}. One HTML template, a language switcher built in, no website builder subscription.`,
      d.url, `multilingual website template, bilingual website, ${kw}`]);
    rows.push([`${name}-c.jpg`, 'ホームページ テンプレート',
      `${d.ja}向けホームページテンプレート｜月額0円・買い切り`,
      `${d.ja}のホームページがすぐ作れる HTML テンプレート。スマホ対応、LINE ボタン付き、日本語ガイド同梱。月額料金なしで、Netlify などに無料で公開できます。`,
      d.url, `ホームページ テンプレート, ${d.ja} ホームページ, HTML テンプレート, 個人店 ホームページ, LP テンプレート`]);
  }
  const csvName = process.env.CSV || 'pins.csv';
  if (process.env.CSV2) {
    const r2 = [['file', 'board', 'title', 'description', 'link', 'keywords']];
    for (const d of data) {
      const name = d.slug.replace(/\//g, '-'), cat = d.cat, langs = d.es ? 'English, Chinese, Japanese and Spanish' : 'English, Chinese and Japanese';
      const kw = `${cat.toLowerCase()} website template, html website template, small business website, one page website, mobile website template`;
      r2.push([`${name}-d.jpg`, 'Small Business Website Templates', `${cat} Website Template — See the Whole Page`, `Every section of a ready-to-launch ${cat.toLowerCase()} website, shown on a phone. ${d.pills.join(' · ')}. Includes ${langs} versions. Buy once, no monthly fees.`, d.url, kw]);
      r2.push([`${name}-e.jpg`, 'Small Business Website Ideas', `${cat}: From a Map Listing to a Real Website`, `Customers want more than hours and a phone number. Give your ${cat.toLowerCase()} business a real website with ${d.pills.slice(0,2).join(' and ').toLowerCase()}, in ${langs}. One-time price, you own it.`, d.url, `small business website ideas, website for local business, ${kw}`]);
    }
    fs.writeFileSync(path.join(out, process.env.CSV2), '\ufeff' + r2.map(r => r.map(q).join(',')).join('\n') + '\n');
    console.log('✓', process.env.CSV2, r2.length - 1, 'pins'); return;
  }
  fs.writeFileSync(path.join(out, csvName), '﻿' + rows.map(r => r.map(q).join(',')).join('\n') + '\n');
  console.log('✓ pins.csv', rows.length - 1, 'pins');
})();
