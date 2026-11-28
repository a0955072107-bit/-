// 模板展示短片（1080×1920、18.5 秒）：標題 → 3 個功能區塊 → 一鍵切換日文 → 片尾
// 用法：bash scripts/build-site.sh && node scripts/videos/render.js <slug> [slug ...]
//   每款的標題、3 個區塊（section id、字幕、往下捲多少）寫在 scripts/videos/data.json
//   輸出 sales/videos/t-<slug>.mp4（需要 ffmpeg；加 --frames-only 只輸出畫格、不轉檔）
//   畫面用 _site/ 的線上預覽頁（含示意照片），所以要先跑 build-site.sh
const { chromium } = require('playwright');
const { spawnSync } = require('child_process');
const fs = require('fs'), os = require('os'), path = require('path');
const D = __dirname, ROOT = path.resolve(D, '../..');
const DATA = JSON.parse(fs.readFileSync(path.join(D, 'data.json'), 'utf8'));
const args = process.argv.slice(2), FRAMES_ONLY = args.includes('--frames-only');
const SLUGS = args.filter(a => !a.startsWith('--'));
if (!SLUGS.length) SLUGS.push('dental');
const FPS = 30, DUR = 18.5, N = Math.round(FPS * DUR);
// 每個區塊的時間點（秒）：字幕出現、捲到區塊、停住、往下捲完、再停住。三個區塊固定用這組（和 t-dental 相同）
const SEG_AT = [2.5, 5.2, 7.9], LANG_AT = 10.6;
const KEY_AT = [[2.9, 4.2, 5.0, 5.1], [6.0, 6.6, 7.5, 7.7], [8.6, 9.2, 9.9, 10.1]];
const ease = x => x < 0 ? 0 : x > 1 ? 1 : (x < .5 ? 4 * x * x * x : 1 - Math.pow(-2 * x + 2, 3) / 2);
const clamp = x => Math.max(0, Math.min(1, x));
function keyed(t, keys) { // keys: [[t0,v0],[t1,v1],...] eased between
  if (t <= keys[0][0]) return keys[0][1];
  for (let i = 1; i < keys.length; i++) if (t <= keys[i][0]) {
    const [a, va] = keys[i - 1], [b, vb] = keys[i];
    return va + (vb - va) * ease((t - a) / (b - a));
  }
  return keys[keys.length - 1][1];
}
function hasFfmpeg() { return spawnSync('ffmpeg', ['-version']).status === 0; }

async function render(b, slug) {
  const cfg = DATA[slug];
  if (!cfg) throw new Error(`scripts/videos/data.json 沒有「${slug}」的設定`);
  if (cfg.sections.length !== 3) throw new Error(`${slug}：sections 要剛好 3 個`);
  const site = path.join(ROOT, '_site/templates', slug);
  for (const l of ['en', 'ja']) if (!fs.existsSync(path.join(site, l, 'index.html'))) throw new Error(`找不到 ${site}/${l}/index.html，請先跑 bash scripts/build-site.sh`);
  const tmp = fs.mkdtempSync(path.join(os.tmpdir(), `video-${slug}-`));
  const OUT = FRAMES_ONLY ? path.join(D, 'frames', slug) : path.join(tmp, 'frames');
  fs.rmSync(OUT, { recursive: true, force: true }); fs.mkdirSync(OUT, { recursive: true });
  const SEG = [[0, cfg.title, 'No monthly fees · you own it'],
    ...cfg.sections.map((s, i) => [SEG_AT[i], s.caption, `Feature ${i + 1} of 3`]),
    [LANG_AT, 'Switch languages in one tap', 'English']];
  const stage = path.join(tmp, 'stage.html');
  fs.writeFileSync(stage, fs.readFileSync(path.join(D, 'stage.html'), 'utf8').replaceAll('SITE', 'file://' + site));
  const p = await b.newPage({ viewport: { width: 1080, height: 1920 } });
  await p.goto('file://' + stage, { waitUntil: 'load' });
  await p.waitForTimeout(2500);
  const en = p.frame({ url: /\/en\// }), ja = p.frame({ url: /\/ja\// });
  for (const f of [en, ja]) await f.addStyleTag({ content: '*,*::before,*::after{transition:none!important;animation:none!important;scroll-behavior:auto!important}.reveal{opacity:1!important;transform:none!important}' });
  const top = await en.evaluate(() => { const o = {}; document.querySelectorAll('section[id]').forEach(s => o[s.id] = Math.round(s.getBoundingClientRect().top + scrollY)); return o; });
  const off = cfg.offset == null ? 60 : cfg.offset;
  const enKeys = [[1.6, 0]];
  cfg.sections.forEach((s, i) => {
    if (top[s.id] == null) throw new Error(`${slug}：英文版找不到 <section id="${s.id}">（有：${Object.keys(top).join(', ')}）`);
    const y = top[s.id] - off, [a, h1, d, h2] = KEY_AT[i];
    enKeys.push([a, y], [h1, y], [d, y + s.drift], [h2, y + s.drift]);
  });
  enKeys.push([LANG_AT + .1, top[cfg.sections[2].id] - off]);
  const jaKeys = [[13.6, 0], [15.0, cfg.jaDrift == null ? 330 : cfg.jaDrift]];
  const sumRect = await en.evaluate(() => { const r = document.querySelector('.lang-menu summary').getBoundingClientRect(); return [r.x + r.width / 2, r.y + r.height / 2]; });
  await en.evaluate(() => document.querySelector('.lang-menu').setAttribute('open', ''));
  const jaRect = await en.evaluate(() => { const r = document.querySelector('.lang-list a[hreflang="ja"]').getBoundingClientRect(); return [r.x + r.width * 0.45, r.y + r.height / 2]; });
  await en.evaluate(() => document.querySelector('.lang-menu').removeAttribute('open'));
  const toStage = ([x, y]) => [10 + 2.6 * x, 10 + 2.6 * y]; // inside .phone (border 10)
  const A = toStage(sumRect), B = toStage(jaRect);
  console.log(slug, { top, A, B });
  let menuOpen = false;
  for (let i = 0; i < N; i++) {
    const t = i / FPS;
    // caption
    let si = 0; for (let k = 0; k < SEG.length; k++) if (t >= SEG[k][0]) si = k;
    const next = SEG[si + 1] ? SEG[si + 1][0] : 99;
    let capOp = 1;
    if (si > 0 && t < SEG[si][0] + .25) capOp = clamp((t - SEG[si][0]) / .25);
    if (t > next - .25) capOp = clamp((next - t) / .25);
    let pill = SEG[si][2], pillScale = 1;
    if (si === 4 && t >= 12.5) { pill = '日本語'; pillScale = 1 + 0.12 * Math.max(0, 1 - (t - 12.5) / .25) * Math.sin(Math.min(1, (t - 12.5) / .25) * Math.PI); }
    // phone / end
    const endOp = clamp((t - 15.4) / .5);
    // tap indicator
    let tap = { op: 0, x: A[0], y: A[1], s: 1 };
    if (t >= 10.9 && t < 12.75) {
      tap.op = clamp((t - 10.9) / .2) * (t > 12.55 ? clamp((12.75 - t) / .2) : 1);
      const m = keyed(t, [[11.65, 0], [12.15, 1]]);
      tap.x = A[0] + (B[0] - A[0]) * m; tap.y = A[1] + (B[1] - A[1]) * m;
      const press = (c) => (t > c - .1 && t < c + .15) ? 0.82 : 1;
      tap.s = Math.min(press(11.3), press(12.35)) * (t < 11.1 ? 0.6 + 0.4 * clamp((t - 10.9) / .2) : 1);
    }
    const wantOpen = t >= 11.35 && t < 12.5;
    if (wantOpen !== menuOpen) { await en.evaluate(o => { const d = document.querySelector('.lang-menu'); o ? d.setAttribute('open', '') : d.removeAttribute('open'); }, wantOpen); menuOpen = wantOpen; }
    const wantLang = t >= 12.5 ? 'ja' : 'en';
    if (wantLang === 'en') await en.evaluate(y => scrollTo(0, y), Math.round(keyed(t, enKeys)));
    else await ja.evaluate(y => scrollTo(0, y), Math.round(keyed(t, jaKeys)));
    await p.evaluate(st => {
      const L = document.getElementById('L');
      if (L.dataset.si != st.si) { document.getElementById('T').innerHTML = st.title; L.dataset.si = st.si; }
      const P = document.getElementById('P'); if (P.textContent !== st.pill) P.textContent = st.pill;
      P.style.transform = `scale(${st.pillScale})`; P.style.transformOrigin = 'left center';
      L.style.opacity = st.capOp; L.style.transform = `translateY(${(1 - st.capOp) * 14}px)`;
      document.getElementById('cap').style.opacity = 1 - st.endOp;
      document.getElementById('phone').style.opacity = 1 - st.endOp;
      document.getElementById('end').style.opacity = st.endOp;
      document.getElementById('en').style.visibility = st.lang === 'en' ? 'visible' : 'hidden';
      const tp = document.getElementById('tap'); tp.style.opacity = st.tap.op; tp.style.left = st.tap.x + 'px'; tp.style.top = st.tap.y + 'px'; tp.style.transform = `scale(${st.tap.s})`;
    }, { si, title: SEG[si][1], pill, pillScale, capOp, endOp, lang: wantLang, tap });
    await p.screenshot({ path: `${OUT}/f${String(i).padStart(4, '0')}.png` });
  }
  await p.close();
  if (FRAMES_ONLY) { console.log('✓ 畫格', OUT); fs.rmSync(tmp, { recursive: true, force: true }); return; }
  const mp4 = path.join(ROOT, 'sales/videos', `t-${slug}.mp4`);
  const r = spawnSync('ffmpeg', ['-y', '-loglevel', 'error', '-framerate', String(FPS), '-i', path.join(OUT, 'f%04d.png'),
    '-c:v', 'libx264', '-profile:v', 'high', '-pix_fmt', 'yuv420p', '-crf', '20', '-preset', 'slow', '-movflags', '+faststart', mp4], { stdio: 'inherit' });
  fs.rmSync(tmp, { recursive: true, force: true });
  if (r.status !== 0) throw new Error(`${slug}：ffmpeg 轉檔失敗`);
  console.log('✓', path.relative(ROOT, mp4));
}

(async () => {
  if (!FRAMES_ONLY && !hasFfmpeg()) { console.error('找不到 ffmpeg：先安裝（apt-get install -y ffmpeg），或加 --frames-only 只輸出畫格'); process.exit(1); }
  const b = await chromium.launch();
  try { for (const s of SLUGS) await render(b, s); }
  finally { await b.close(); }
})().catch(e => { console.error(e.message); process.exit(1); });
