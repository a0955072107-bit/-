const { chromium } = require('playwright');
const fs = require('fs');
const D = __dirname, SITE = 'file:///home/user/-/.claude/worktrees/agent-a39045d27d15c2910/_site/templates/dental';
const FPS = 30, DUR = 18.5, N = Math.round(FPS * DUR);
const OUT = D + '/frames';
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
const SEG = [
  [0, 'Dental Clinic website<br>template, Forest Edition', 'No monthly fees · you own it'],
  [2.5, 'Your first visit, step by step', 'Feature 1 of 3'],
  [5.2, 'Dentist profiles', 'Feature 2 of 3'],
  [7.9, 'Today’s hours update itself', 'Feature 3 of 3'],
  [10.6, 'Switch languages in one tap', 'English'],
];
(async () => {
  fs.rmSync(OUT, { recursive: true, force: true }); fs.mkdirSync(OUT);
  const html = fs.readFileSync(D + '/stage.html', 'utf8').replaceAll('SITE', SITE);
  fs.writeFileSync(D + '/stage.built.html', html);
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1080, height: 1920 } });
  await p.goto('file://' + D + '/stage.built.html', { waitUntil: 'load' });
  await p.waitForTimeout(2500);
  const en = p.frame({ url: /\/en\// }), ja = p.frame({ url: /\/ja\// });
  for (const f of [en, ja]) await f.addStyleTag({ content: '*,*::before,*::after{transition:none!important;animation:none!important}.reveal{opacity:1!important;transform:none!important}' });
  const top = await en.evaluate(() => { const o = {}; document.querySelectorAll('section[id]').forEach(s => o[s.id] = Math.round(s.getBoundingClientRect().top + scrollY)); return o; });
  const S = { first: top.first - 60, doctors: top.doctors - 60, hours: top.hours - 60 };
  const enKeys = [[1.6, 0], [2.9, S.first], [4.2, S.first], [5.0, S.first + 300], [5.1, S.first + 300], [6.0, S.doctors], [6.6, S.doctors], [7.5, S.doctors + 330], [7.7, S.doctors + 330], [8.6, S.hours], [9.2, S.hours], [9.9, S.hours + 200], [10.1, S.hours + 200], [10.7, S.hours]];
  const jaKeys = [[13.6, 0], [15.0, 330]];
  const sumRect = await en.evaluate(() => { const r = document.querySelector('.lang-menu summary').getBoundingClientRect(); return [r.x + r.width / 2, r.y + r.height / 2]; });
  await en.evaluate(() => document.querySelector('.lang-menu').setAttribute('open', ''));
  const jaRect = await en.evaluate(() => { const r = document.querySelector('.lang-list a[hreflang="ja"]').getBoundingClientRect(); return [r.x + r.width * 0.45, r.y + r.height / 2]; });
  await en.evaluate(() => document.querySelector('.lang-menu').removeAttribute('open'));
  const toStage = ([x, y]) => [10 + 2.6 * x, 10 + 2.6 * y]; // inside .phone (border 10)
  const A = toStage(sumRect), B = toStage(jaRect);
  console.log({ top, A, B });
  let lastSeg = -1, menuOpen = false, lang = 'en', pillText = null;
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
  await b.close();
})();
