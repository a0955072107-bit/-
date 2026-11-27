// Polyglot Pages｜後台
// 排程：schedule.json（scripts/admin/build-schedule.py 產生，公開）
// 使用者資料（打勾、每週數字、收入、開發數量、校正值）：只存在這台裝置的 localStorage，可匯出／匯入備份
'use strict';

const KEY = 'pp-admin.v1';
const CATS = ['上架', 'Pinterest', '影片', 'Substack', '開發', '檢查'];
const TYPES = { '模板': 'var(--k-shelf)', '客製服務': 'var(--k-video)', 'Website Care': 'var(--k-lead)', '其他': 'var(--k-check)' };
const STAGES = [
  ['sent', '寄出', '開發信或私訊寄出'],
  ['replied', '回覆', '有任何回覆'],
  ['demo', '看過示範', '確定點開過示範站'],
  ['won', '成交', '收到訂金'],
  ['lost', '不需要', '說不需要或要求別再聯絡'],
];
const WD = ['日', '一', '二', '三', '四', '五', '六'];
const $ = (s) => document.querySelector(s);
const esc = (s) => String(s ?? '').replace(/[&<>"']/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
const fmt = (n) => Math.round(n).toLocaleString('zh-Hant-TW');
const usd = (n) => 'US$ ' + (Math.round(n * 100) / 100).toLocaleString('en-US', { maximumFractionDigits: 2 });

// ---- 台北時間 ----
function tpeNow() { return new Date(Date.now() + 8 * 3600e3); }           // 用 UTC 欄位表示台北時間
function tpeToday() { return tpeNow().toISOString().slice(0, 10); }
function tpeHM() { return tpeNow().toISOString().slice(11, 16); }
function ymd(d) { return d.toISOString().slice(0, 10); }
function addDays(s, n) { const d = new Date(s + 'T00:00:00Z'); d.setUTCDate(d.getUTCDate() + n); return ymd(d); }
function daysBetween(a, b) { return Math.round((new Date(b + 'T00:00:00Z') - new Date(a + 'T00:00:00Z')) / 864e5); }
function mmdd(s) { return Number(s.slice(5, 7)) + '/' + Number(s.slice(8, 10)); }
function wd(s) { return WD[new Date(s + 'T00:00:00Z').getUTCDay()]; }
function mondayOf(s) { const d = new Date(s + 'T00:00:00Z'); const k = (d.getUTCDay() + 6) % 7; return addDays(s, -k); }

// ---- 本機資料 ----
function blank() { return { v: 1, done: {}, weekly: [], income: [], leads: null, leadLog: [], over: {}, lastExport: null }; }
function load() {
  try { const o = JSON.parse(localStorage.getItem(KEY) || 'null'); if (o && typeof o === 'object') return Object.assign(blank(), o); } catch {}
  return blank();
}
let S = load();
function save() { try { localStorage.setItem(KEY, JSON.stringify(S)); } catch {} renderMeta(); }
const uid = () => Date.now().toString(36) + Math.random().toString(36).slice(2, 6);

const state = { page: 'overview', sched: null, cal: null, sel: null, recFilter: 'weekly' };
const tip = $('#tip');
function showTip(e, html) { tip.innerHTML = html; tip.style.opacity = 1; const x = Math.min(e.clientX + 12, innerWidth - tip.offsetWidth - 8); tip.style.left = Math.max(8, x) + 'px'; tip.style.top = (e.clientY - 10 - tip.offsetHeight) + 'px'; }
function hideTip() { tip.style.opacity = 0; }

// ---- 分頁＋滑動藥丸（同清醒行動派後台）----
const tabs = $('#tabs'), pill = tabs.querySelector('.pill'), topLayer = pill.querySelector('.layer.top'), baseLayer = tabs.querySelector('.layer.base');
const PAGES = ['overview', 'calendar', 'stats', 'income', 'leads', 'record'];
function movePill(animate = true) {
  const btn = tabs.querySelector(`button[data-page="${state.page}"]`); if (!btn) return;
  const x = btn.offsetLeft - baseLayer.offsetLeft, w = btn.offsetWidth;
  topLayer.style.width = baseLayer.offsetWidth + 'px';
  const btns = baseLayer.children, copies = topLayer.children;
  for (let i = 0; i < btns.length && i < copies.length; i++) { copies[i].style.width = btns[i].offsetWidth + 'px'; copies[i].style.justifyContent = 'center'; }
  if (!animate) { pill.style.transition = 'none'; topLayer.style.transition = 'none'; }
  pill.style.transform = `translateX(${x}px)`; pill.style.width = w + 'px';
  topLayer.style.transform = `translateX(${-x}px)`;
  if (!animate) requestAnimationFrame(() => { pill.style.transition = ''; topLayer.style.transition = ''; });
}
function go(page, push = true) {
  if (!PAGES.includes(page)) page = 'overview';
  state.page = page;
  document.querySelectorAll('.page').forEach((p) => p.classList.toggle('on', p.id === 'page-' + page));
  movePill();
  if (push && location.hash !== '#' + page) history.replaceState(null, '', '#' + page);
  try { localStorage.setItem('pp-admin.page', page); } catch {}
  renderPage();
  window.scrollTo({ top: 0 });
}
tabs.querySelectorAll('button').forEach((b) => (b.onclick = () => go(b.dataset.page)));
document.addEventListener('click', (e) => { const a = e.target.closest('[data-go]'); if (a) { e.preventDefault(); go(a.dataset.go); } });
addEventListener('hashchange', () => go(location.hash.slice(1), false));
let rz; addEventListener('resize', () => { movePill(false); clearTimeout(rz); rz = setTimeout(renderPage, 150); });

// ---- 排程 ----
const items = () => state.sched?.items || [];
const byDate = (d) => items().filter((x) => x.date === d);
const isDone = (id) => !!S.done[id];
const DAILY = /-(daily|note|video|outreach|linkedin)$/;

function summaryText() {
  const t = tpeToday(), k = kpiValues();
  const lines = [`（後台數字，${t}）`, `Gumroad 已上架 ${k.gum}/${k.gumTotal}；Pinterest 已發 ${k.pins}；影片已發 ${k.vids}/${k.vidTotal}`];
  const L = leadCounts();
  lines.push(`開發：寄出 ${L.sent}、回覆 ${L.replied}、看過示範 ${L.demo}、成交 ${L.won}、不需要 ${L.lost}`);
  const weeks = [...S.weekly].sort((a, b) => (a.week < b.week ? 1 : -1)).slice(0, 6);
  if (weeks.length) {
    lines.push('每週數字（週一｜Pinterest 曝光／外連點擊｜TikTok 平均觀看｜YouTube 觀看／訂閱｜Substack 訂閱｜Gumroad 瀏覽／銷售）：');
    for (const w of weeks) lines.push(`${w.week}｜${v(w.pinImpr)}／${v(w.pinClicks)}｜${v(w.ttAvg)}｜${v(w.ytViews)}／${v(w.ytSubs)}｜${v(w.ssSubs)}｜${v(w.gumViews)}／${v(w.gumSales)}`);
  } else lines.push('每週數字：還沒記錄');
  const m = monthly();
  if (m.length) lines.push('每月收入：' + m.map((x) => `${x.month} ${usd(x.total)}（${Object.entries(x.by).map(([k2, v2]) => `${k2} ${usd(v2)}`).join('、')}）`).join('；'));
  else lines.push('收入：還沒記錄');
  return lines.join('\n');
  function v(x) { return x == null || x === '' ? '—' : x; }
}
const promptOf = (it) => (it.prompt || '').replace('{{summary}}', () => summaryText());

function taskHTML(it, opt = {}) {
  const done = isDone(it.id);
  const files = it.files?.length ? `<div class="files">${it.files.map((f) => `<code>${esc(f)}</code>`).join('')}</div>` : '';
  const late = opt.late ? `<span class="late">${mmdd(it.date)}（${wd(it.date)}）的</span>` : '';
  const acts = it.prompt ? `<div class="acts"><button class="btn sm" type="button" data-copy="${esc(it.id)}">複製提示</button></div>
    <details><summary>看提示內容</summary><pre>${esc(it.prompt.replace('{{summary}}', '（複製時會自動帶入你在後台記的數字）'))}</pre></details>` : '';
  return `<li class="task k-${esc(it.cat)}${done ? ' done' : ''}" data-id="${esc(it.id)}">
    <label class="ck" title="完成打勾"><input type="checkbox" data-done="${esc(it.id)}" ${done ? 'checked' : ''} aria-label="${esc(it.title)} 完成"><span></span></label>
    <div class="body"><div class="tt"><span class="tm">${esc(it.time)}</span>${esc(it.title)}</div>
      <div class="mt">${late}<span class="who w-${esc(it.who)}">${esc(it.who)}</span><span class="cat">${esc(it.cat)}</span>${it.sub ? `<span class="cat" style="--k:transparent">${esc(it.sub)}</span>` : ''}</div>
      ${it.note ? `<div class="note">${esc(it.note)}</div>` : ''}${files}${acts}</div></li>`;
}

document.addEventListener('change', (e) => {
  const c = e.target.closest('input[data-done]'); if (!c) return;
  const id = c.dataset.done;
  if (c.checked) S.done[id] = Date.now(); else delete S.done[id];
  save();
  document.querySelectorAll(`li.task[data-id="${CSS.escape(id)}"]`).forEach((li) => { li.classList.toggle('done', c.checked); const x = li.querySelector('input[data-done]'); if (x) x.checked = c.checked; });
  renderOverviewCounts(); renderKpis();
  if (state.page === 'calendar') renderCalendar();
});

async function copyText(t) {
  try { await navigator.clipboard.writeText(t); return true; } catch {}
  try {
    const ta = document.createElement('textarea'); ta.value = t; ta.setAttribute('readonly', ''); ta.style.position = 'fixed'; ta.style.opacity = '0';
    document.body.appendChild(ta); ta.select(); const ok = document.execCommand('copy'); ta.remove(); return ok;
  } catch { return false; }
}
document.addEventListener('click', async (e) => {
  const b = e.target.closest('button[data-copy]'); if (!b) return;
  const it = items().find((x) => x.id === b.dataset.copy); if (!it) return;
  const ok = await copyText(promptOf(it));
  b.textContent = ok ? '已複製 ✓' : '複製失敗，請打開「看提示內容」手動複製';
  if (ok) b.classList.add('copied');
  setTimeout(() => { b.textContent = '複製提示'; b.classList.remove('copied'); }, 1800);
});

// ---- KPI ----
function leadCounts() {
  if (S.leads) return S.leads;
  const seed = state.sched?.outreachSeed || {};
  return { sent: seed.sent || 0, replied: seed.replied || 0, demo: seed.demo || 0, won: seed.won || 0, lost: seed.lost || 0 };
}
function kpiValues() {
  const t = tpeToday(), hm = tpeHM(), sc = state.sched || {};
  const g = sc.gumroad || { before: 0, total: 39 };
  let gum = g.before;
  for (const it of items()) if (it.listing && (it.date < t || (it.date === t && isDone(it.id)))) gum += it.listing;
  let pins = 0;
  const nowAt = t + 'T' + hm;
  for (const p of sc.pinsPlan || []) {
    if (p.at) { if (p.at <= nowAt) pins += p.n; }
    else if (p.date < t || (p.date === t && (!p.id || isDone(p.id)))) pins += p.n;
  }
  const vids = (sc.videos || []).filter((v) => v.date < t || (v.date === t && v.time <= hm)).length;
  const o = S.over || {}, num = (x) => (x === '' || x == null ? null : Number(x));
  return {
    gum: num(o.gumroad) ?? gum, gumAuto: num(o.gumroad) == null, gumTotal: g.total,
    pins: num(o.pins) ?? pins, pinsAuto: num(o.pins) == null,
    vids: num(o.videos) ?? vids, vidsAuto: num(o.videos) == null, vidTotal: (sc.videos || []).length,
  };
}
function kpi(l, v, d, extra = '', cls = '') { return `<div class="kpi"><div class="l">${l}</div><div class="v">${v}</div>${extra}<div class="d ${cls}">${d}</div></div>`; }
function renderKpis() {
  if (!state.sched) return;
  const k = kpiValues(), L = leadCounts(), t = tpeToday();
  const nextList = items().find((x) => x.listing && x.date >= t && !isDone(x.id));
  const pct = Math.min(100, Math.round(k.gum / k.gumTotal * 100));
  const m = monthly().find((x) => x.month === t.slice(0, 7));
  $('#kpisOverview').innerHTML =
    kpi('Gumroad 已上架', `${k.gum}<small>/${k.gumTotal}</small>`, k.gumAuto ? (nextList ? `下一批 ${mmdd(nextList.date)} ${nextList.listing} 款` : '全部上架完成') : '手動填的數字', `<div class="bar"><i style="width:${pct}%"></i></div>`) +
    kpi('Pinterest 已發', fmt(k.pins), k.pinsAuto ? '依上傳計畫估算（含預排）' : '手動填的數字') +
    kpi('影片已發', `${k.vids}<small>/${k.vidTotal}</small>`, k.vidsAuto ? 'TikTok＋YouTube 每天 1 支' : '手動填的數字') +
    `<div class="kpi"><div class="l">開發信</div><div class="v trio"><span>${fmt(L.sent)}<em>已寄</em></span><span>${fmt(L.replied)}<em>回覆</em></span><span>${fmt(L.won)}<em>成交</em></span></div><div class="d">${L.sent ? `回覆率 ${Math.round(L.replied / L.sent * 100)}%` : '到「開發」更新'}</div></div>` +
    kpi(`本月收入（${Number(t.slice(5, 7))} 月）`, usd(m?.total || 0), `${m?.n || 0} 筆`);
}

// ---- 總覽 ----
function renderOverviewCounts() {
  const t = tpeToday(), list = byDate(t), done = list.filter((x) => isDone(x.id)).length, left = list.length - done;
  $('#nToday').textContent = $('#nToday2').textContent = left || '';
  $('#todayTag').textContent = list.length ? (left ? `還有 ${left} 件` : '全部完成') : '';
  $('#todayProg').innerHTML = list.length ? `<span>${done}/${list.length}</span><span class="bar"><i style="width:${list.length ? done / list.length * 100 : 0}%"></i></span>` : '';
  movePill(false);
}
function renderOverview() {
  if (!state.sched) return;
  const now = tpeNow(), t = tpeToday(), h = now.getUTCHours();
  $('#greet').firstChild.textContent = h < 5 ? '晚安' : h < 11 ? '早安' : h < 18 ? '午安' : '晚安';
  $('#todayLine').textContent = `${now.getUTCMonth() + 1} 月 ${now.getUTCDate()} 日（${WD[now.getUTCDay()]}）`;
  renderKpis();
  const list = byDate(t);
  $('#todayList').innerHTML = list.length ? list.map((x) => taskHTML(x)).join('') : `<li class="empty">今天沒有排定的事</li>`;
  // 前 7 天沒打勾的（每天固定的不算）
  const late = items().filter((x) => x.date < t && x.date >= addDays(t, -7) && !isDone(x.id) && !DAILY.test(x.id));
  $('#lateWrap').hidden = !late.length;
  $('#lateList').innerHTML = late.map((x) => taskHTML(x, { late: true })).join('');
  renderOverviewCounts();
  // 接下來 7 天
  const up = items().filter((x) => x.date > t && x.date <= addDays(t, 7) && !DAILY.test(x.id));
  let html = '', last = '';
  for (const x of up) {
    if (x.date !== last) { const diff = daysBetween(t, x.date); html += `<li class="dayhead">${mmdd(x.date)}（${wd(x.date)}）· ${diff === 1 ? '明天' : diff + ' 天後'}</li>`; last = x.date; }
    html += `<li class="k-${esc(x.cat)}${isDone(x.id) ? ' done' : ''}"><span class="dot"></span><span class="d">${esc(x.time)}</span><span class="t" title="${esc(x.title)}">${esc(x.title)}</span><span class="who w-${esc(x.who)}">${esc(x.who)}</span></li>`;
  }
  $('#upcoming').innerHTML = html || `<li class="empty">接下來 7 天沒有特別的事</li>`;
  // 重要日期
  const ms = (state.sched.milestones || []).filter(([d]) => d >= t).slice(0, 8);
  $('#dates').innerHTML = ms.length ? ms.map(([d, txt]) => { const diff = daysBetween(t, d); return `<li><span class="d">${mmdd(d)}（${wd(d)}）</span><span class="t" title="${esc(txt)}" style="white-space:normal">${esc(txt)}</span><span class="in ${diff === 0 ? 'today' : diff <= 3 ? 'soon' : ''}">${diff === 0 ? '今天' : diff + ' 天'}</span></li>`; }).join('') : `<li class="empty">沒有接下來的重要日期</li>`;
}

// ---- 日曆 ----
$('#calPrev').onclick = () => { state.cal.setUTCMonth(state.cal.getUTCMonth() - 1); renderCalendar(); };
$('#calNext').onclick = () => { state.cal.setUTCMonth(state.cal.getUTCMonth() + 1); renderCalendar(); };
$('#calToday').onclick = () => { state.cal = null; state.sel = tpeToday(); renderCalendar(); };
$('#cal').onclick = (e) => { const c = e.target.closest('.cell'); if (!c) return; state.sel = c.dataset.d; renderCalendar(); if (innerWidth <= 860) $('#dayCard').scrollIntoView({ behavior: 'smooth', block: 'start' }); };
function renderCalendar() {
  if (!state.sched) return;
  const t = tpeToday();
  if (!state.sel) state.sel = t;
  if (!state.cal) { const n = new Date(state.sel + 'T00:00:00Z'); state.cal = new Date(Date.UTC(n.getUTCFullYear(), n.getUTCMonth(), 1)); }
  const y = state.cal.getUTCFullYear(), m = state.cal.getUTCMonth(), ym = `${y}-${String(m + 1).padStart(2, '0')}`;
  $('#calTitle').textContent = `${y} 年 ${m + 1} 月`;
  $('#calLegend').innerHTML = CATS.map((c) => `<span class="k-${c}"><i style="background:var(--k)"></i>${c}</span>`).join('');
  const first = new Date(Date.UTC(y, m, 1)), start = addDays(ymd(first), -first.getUTCDay());
  const msBy = {}; for (const [d, txt] of state.sched.milestones || []) (msBy[d] ||= []).push(txt);
  const cells = [];
  for (let i = 0; i < 42; i++) {
    const d = addDays(start, i), inMonth = d.slice(0, 7) === ym;
    if (i === 35 && !inMonth) break;
    const list = byDate(d), cats = CATS.filter((c) => list.some((x) => x.cat === c));
    const special = list.filter((x) => !DAILY.test(x.id));
    const evs = special.slice(0, 3).map((x) => `<span class="ev k-${esc(x.cat)}${isDone(x.id) ? ' done' : ''}"><i></i><span>${esc(x.title)}</span></span>`).join('');
    const more = list.length > special.slice(0, 3).length ? `<span class="more">共 ${list.length} 件</span>` : '';
    const ms = (msBy[d] || []).slice(0, 1).map((txt) => `<span class="ms" title="${esc(txt)}">${esc(txt)}</span>`).join('');
    cells.push(`<button type="button" class="cell ${inMonth ? '' : 'out'} ${d === t ? 'today' : ''} ${d === state.sel ? 'sel' : ''}" data-d="${d}" aria-label="${mmdd(d)} ${list.length} 件事">
      <span class="dn"><b>${Number(d.slice(8))}</b><span>${d === t ? '今天' : ''}</span></span>${ms}${evs}${more}
      <span class="dots">${cats.map((c) => `<i class="k-${c}"></i>`).join('')}</span></button>`);
  }
  $('#cal').innerHTML = WD.map((w) => `<div class="wd">${w}</div>`).join('') + cells.join('');
  const sel = state.sel, list = byDate(sel), diff = daysBetween(t, sel);
  $('#dayTitle').textContent = `${mmdd(sel)}（${wd(sel)}）${diff === 0 ? '今天' : diff === 1 ? '明天' : ''}`;
  $('#daySub').textContent = (msBy[sel] || []).join('；') || (list.length ? `${list.length} 件事，打勾會同步到總覽` : '');
  $('#dayList').innerHTML = list.length ? list.map((x) => taskHTML(x)).join('') : `<li class="empty">這天沒有排定的事</li>`;
}

// ---- 圖表（同清醒行動派後台的 SVG 畫法）----
let W = 600; const H = 200, PL = 44, PR = 12, PT = 14, PB = 28;
function setW(el) { W = Math.max(280, Math.round(el.clientWidth || 600)); }
function niceMax(v) { if (v <= 0) return 1; const p = Math.pow(10, Math.floor(Math.log10(v))); const n = v / p; const m = n <= 1 ? 1 : n <= 2 ? 2 : n <= 5 ? 5 : 10; return m * p; }
function short(v) { return v >= 10000 ? (v / 1000).toFixed(0) + 'k' : v >= 1000 ? +(v / 1000).toFixed(2) + 'k' : String(Math.round(v * 10) / 10); }
function frame(max) { const out = []; for (let i = 0; i <= 4; i++) { const y = PT + (H - PT - PB) * (1 - i / 4); out.push(`<line class="gridline" x1="${PL}" x2="${W - PR}" y1="${y}" y2="${y}"/><text class="tick" x="${PL - 6}" y="${y + 4}" text-anchor="end">${short(max * i / 4)}</text>`); } return out.join(''); }
function xPos(i, n) { return PL + (W - PL - PR) * (i + 0.5) / n; }
function xLabels(keys) { const n = keys.length; if (!n) return ''; const every = Math.ceil(n / 6); return keys.map((k, i) => ((i % every === 0 && n - 1 - i >= every / 2) || i === n - 1) ? `<text class="tick" x="${xPos(i, n)}" y="${H - 8}" text-anchor="middle">${esc(k)}</text>` : '').join(''); }
function hits(n) { return Array.from({ length: n }, (_, i) => `<rect x="${xPos(i, n) - (W - PL - PR) / n / 2}" y="${PT}" width="${(W - PL - PR) / n}" height="${H - PT - PB}" fill="transparent" data-i="${i}"/>`).join(''); }
function hover(el, html) {
  el.querySelectorAll('rect[data-i]').forEach((r) => {
    r.addEventListener('mousemove', (e) => showTip(e, html(Number(r.dataset.i))));
    r.addEventListener('mouseleave', hideTip);
    r.addEventListener('touchstart', (e) => showTip(e.touches[0], html(Number(r.dataset.i))), { passive: true });
  });
}
function lineChart(el, keys, vals, color, unit) {
  setW(el);
  const pts = vals.map((v, i) => v == null ? null : [xPos(i, keys.length), v]);
  if (!pts.some(Boolean)) return (el.innerHTML = `<div class="empty">還沒有資料</div>`);
  const max = niceMax(Math.max(...vals.filter((v) => v != null)));
  const y = (v) => PT + (H - PT - PB) * (1 - v / max);
  let d = ''; for (const p of pts) if (p) d += (d ? 'L' : 'M') + p[0].toFixed(1) + ' ' + y(p[1]).toFixed(1) + ' ';
  el.innerHTML = `<svg viewBox="0 0 ${W} ${H}" role="img">${frame(max)}<path d="${d}" fill="none" stroke="${color}" stroke-width="2" stroke-linejoin="round"/>
    ${pts.filter(Boolean).map((p) => `<circle cx="${p[0]}" cy="${y(p[1])}" r="4" fill="${color}" stroke="var(--card)" stroke-width="2"/>`).join('')}${hits(keys.length)}
    <line class="axis" x1="${PL}" x2="${W - PR}" y1="${H - PB}" y2="${H - PB}"/>${xLabels(keys)}</svg>`;
  hover(el, (i) => `${esc(keys[i])} 那週<br><b>${vals[i] == null ? '—' : fmt(vals[i])}</b> ${unit}`);
}
function barChart(el, keys, vals, color, unit, money = false) {
  setW(el);
  if (!vals.some((v) => v)) return (el.innerHTML = `<div class="empty">還沒有資料</div>`);
  const max = niceMax(Math.max(...vals.map((v) => v || 0)));
  const n = keys.length, bw = Math.max(3, Math.min(36, (W - PL - PR) / n * 0.6));
  const y = (v) => PT + (H - PT - PB) * (1 - v / max);
  el.innerHTML = `<svg viewBox="0 0 ${W} ${H}" role="img">${frame(max)}
    ${vals.map((v, i) => v ? `<rect x="${xPos(i, n) - bw / 2}" y="${y(v)}" width="${bw}" height="${Math.max(0, H - PB - y(v))}" rx="${Math.min(4, bw / 2)}" fill="${color}"/>` : '').join('')}${hits(n)}
    <line class="axis" x1="${PL}" x2="${W - PR}" y1="${H - PB}" y2="${H - PB}"/>${xLabels(keys)}</svg>`;
  hover(el, (i) => `${esc(keys[i])}<br><b>${vals[i] == null ? '—' : money ? usd(vals[i]) : fmt(vals[i]) + ' ' + unit}</b>`);
}

// ---- 數據 ----
const METRICS = [
  ['pinImpr', 'Pinterest 曝光', '次', 'bar', 'var(--k-pin)'],
  ['pinClicks', 'Pinterest 外連點擊', '次', 'bar', 'var(--k-pin)'],
  ['ttAvg', 'TikTok 每支平均觀看', '次', 'line', 'var(--k-video)'],
  ['ytViews', 'YouTube 觀看', '次', 'bar', 'var(--k-video)'],
  ['ytSubs', 'YouTube 訂閱', '人', 'line', 'var(--k-video)'],
  ['ssSubs', 'Substack 訂閱', '人', 'line', 'var(--k-sub)'],
  ['gumViews', 'Gumroad 瀏覽', '次', 'bar', 'var(--k-shelf)'],
  ['gumSales', 'Gumroad 銷售', '筆', 'bar', 'var(--k-shelf)'],
];
const num = (x) => (x === '' || x == null ? null : Number(x));
function renderStats() {
  const weeks = [...S.weekly].sort((a, b) => (a.week < b.week ? -1 : 1));
  const last = weeks.at(-1), prev = weeks.at(-2);
  const pick = ['pinImpr', 'pinClicks', 'ttAvg', 'ytSubs', 'ssSubs', 'gumSales'];
  $('#kpisStats').innerHTML = pick.map((k) => {
    const m = METRICS.find((x) => x[0] === k), a = num(last?.[k]), b = num(prev?.[k]);
    const dd = a != null && b != null ? a - b : null;
    return kpi(m[1], a == null ? '—' : fmt(a), last ? (dd == null ? `${mmdd(last.week)} 那週` : `${dd >= 0 ? '+' : ''}${fmt(dd)} 比前一週`) : '還沒有資料', '', dd > 0 ? 'up' : dd < 0 ? 'down' : '');
  }).join('');
  const keys = weeks.map((w) => mmdd(w.week));
  const box = $('#statCharts');
  if (!box.children.length) box.innerHTML = METRICS.map(([k, l, u]) => `<div class="card"><h2>${l}</h2><div class="sub">每週，單位：${u}</div><div id="ch-${k}"></div></div>`).join('');
  for (const [k, , u, kind, color] of METRICS) {
    const el = $('#ch-' + k), vals = weeks.map((w) => num(w[k]));
    if (!weeks.length) { el.innerHTML = `<div class="empty">還沒有資料，到「紀錄」填第一週</div>`; continue; }
    (kind === 'line' ? lineChart : barChart)(el, keys, vals, color, u);
  }
  const rows = [...weeks].reverse(), v = (x) => (x == null || x === '' ? '—' : fmt(x));
  $('#tblWeeks').innerHTML = rows.length ? `<table><thead><tr><th>週一</th>${METRICS.map((m) => `<th class="num">${m[1]}</th>`).join('')}</tr></thead><tbody>${rows.map((w) => `<tr><td>${esc(w.week)}</td>${METRICS.map((m) => `<td class="num">${v(w[m[0]])}</td>`).join('')}</tr>`).join('')}</tbody></table>` : `<div class="empty">還沒有資料</div>`;
}

// ---- 收入 ----
function monthly() {
  const by = {};
  for (const r of S.income) { const m = r.date.slice(0, 7); const o = (by[m] ||= { month: m, total: 0, n: 0, by: {} }); o.total += Number(r.amount) || 0; o.n++; o.by[r.type] = (o.by[r.type] || 0) + (Number(r.amount) || 0); }
  return Object.values(by).sort((a, b) => (a.month < b.month ? -1 : 1));
}
function goalLine(total) {
  const p = state.sched?.plan; if (!p?.grossUsd) return '';
  return `目標 ${p.goalDate.replaceAll('-', '/')} 前淨收 NT$${fmt(p.goalTwd)}（約要賣 ${usd(p.grossUsd[0])}，已 ${Math.min(100, Math.round(total / p.grossUsd[0] * 100))}%）`;
}
function renderIncome() {
  const t = tpeToday(), ym = t.slice(0, 7), months = monthly();
  const prevYm = (() => { const d = new Date(ym + '-01T00:00:00Z'); d.setUTCMonth(d.getUTCMonth() - 1); return d.toISOString().slice(0, 7); })();
  const cur = months.find((m) => m.month === ym) || { total: 0, n: 0 }, prv = months.find((m) => m.month === prevYm) || { total: 0, n: 0 };
  const total = S.income.reduce((s, r) => s + (Number(r.amount) || 0), 0);
  const care = S.income.filter((r) => r.type === 'Website Care' && r.date.slice(0, 7) === ym).reduce((s, r) => s + (Number(r.amount) || 0), 0);
  $('#kpisIncome').innerHTML = kpi(`本月（${Number(ym.slice(5))} 月）`, usd(cur.total), `${cur.n} 筆`) + kpi(`上月（${Number(prevYm.slice(5))} 月）`, usd(prv.total), `${prv.n} 筆`) +
    kpi('累計', usd(total), goalLine(total) || `${S.income.length} 筆`) + kpi('本月 Website Care', usd(care), '固定月費收入');
  // 每月堆疊
  const el = $('#chMonthly'); setW(el);
  const used = Object.keys(TYPES).filter((k) => months.some((m) => m.by[k]));
  $('#legType').innerHTML = used.map((k) => `<span><i style="background:${TYPES[k]}"></i>${k}</span>`).join('');
  if (!months.length) el.innerHTML = `<div class="empty">還沒有收入，到「紀錄」記第一筆</div>`;
  else {
    const max = niceMax(Math.max(...months.map((m) => m.total))), n = months.length, bw = Math.min(56, (W - PL - PR) / n * 0.6);
    const y = (v) => PT + (H - PT - PB) * (1 - v / max);
    el.innerHTML = `<svg viewBox="0 0 ${W} ${H}" role="img" aria-label="每月收入">${frame(max)}
      ${months.map((m, i) => { let acc = 0; const cx = xPos(i, n); return used.map((k) => { const v = m.by[k] || 0; if (!v) return ''; const y1 = y(acc + v), h = y(acc) - y1; acc += v; return `<rect x="${cx - bw / 2}" y="${y1}" width="${bw}" height="${Math.max(0, h - 2)}" rx="3" fill="${TYPES[k]}"/>`; }).join('') + `<text class="lbl" x="${cx}" y="${y(m.total) - 6}" text-anchor="middle">${short(m.total)}</text>`; }).join('')}${hits(n)}
      <line class="axis" x1="${PL}" x2="${W - PR}" y1="${H - PB}" y2="${H - PB}"/>${months.map((m, i) => `<text class="tick" x="${xPos(i, n)}" y="${H - 8}" text-anchor="middle">${Number(m.month.slice(5))} 月</text>`).join('')}</svg>`;
    hover(el, (i) => { const m = months[i]; return `${m.month} · <b>${usd(m.total)}</b> · ${m.n} 筆<br>` + used.filter((k) => m.by[k]).map((k) => `${k} ${usd(m.by[k])}`).join('<br>'); });
  }
  const tk = Object.keys(TYPES), tv = tk.map((k) => S.income.filter((r) => r.type === k).reduce((s, r) => s + (Number(r.amount) || 0), 0));
  barChart($('#chType'), tk, tv, 'var(--accent)', '', true);
  const recent = [...S.income].sort((a, b) => (a.date < b.date ? 1 : -1)).slice(0, 20);
  $('#tblIncome').innerHTML = recent.length ? `<table><thead><tr><th>日期</th><th>類型</th><th>品項</th><th class="num">金額</th><th>管道</th><th>備註</th></tr></thead><tbody>${recent.map((r) => `<tr><td>${esc(r.date)}</td><td><i style="display:inline-block;width:9px;height:9px;border-radius:3px;background:${TYPES[r.type] || 'var(--k-check)'};margin-right:6px;vertical-align:-1px"></i>${esc(r.type)}</td><td>${esc(r.item)}</td><td class="num"><b>${usd(Number(r.amount) || 0)}</b></td><td>${esc(r.channel)}</td><td style="white-space:normal">${esc(r.note)}</td></tr>`).join('')}</tbody></table>` : `<div class="empty">還沒有收入</div>`;
}

// ---- 開發 ----
function setLead(key, val, how) {
  const cur = { ...leadCounts() }, before = cur[key];
  val = Math.max(0, Math.round(Number(val) || 0));
  if (val === before) return;
  cur[key] = val; S.leads = cur;
  S.leadLog.push({ at: Date.now(), date: tpeToday(), key, from: before, to: val, how });
  S.leadLog = S.leadLog.slice(-200);
  save(); renderLeads(); renderKpis();
}
function renderLeads() {
  const L = leadCounts(), seed = state.sched?.outreachSeed;
  $('#seedNote').hidden = !!S.leads;
  $('#seedNote').innerHTML = `起始數字來自 repo 的 leads.csv（只算數量）。寄出、回覆時按 ＋，之後就以這台裝置記的為準。`;
  const caps = state.sched?.plan?.emailCap || [], cap = caps.filter(([d]) => d <= tpeToday()).pop()?.[1];
  const sentWeek = S.leadLog.filter((x) => x.key === 'sent' && x.date >= mondayOf(tpeToday())).reduce((s, x) => s + (x.to - x.from), 0);
  $('#stages').innerHTML = STAGES.map(([k, l, d]) => `<div class="stage"><div class="l">${l}</div>
    <div class="ctl"><button type="button" data-lead="${k}" data-step="-1" aria-label="${l} 減 1">−</button><input type="number" min="0" inputmode="numeric" value="${L[k]}" data-leadin="${k}" aria-label="${l}"><button type="button" data-lead="${k}" data-step="1" aria-label="${l} 加 1">＋</button></div>
    <div class="d">${k === 'sent' ? `本週 +${sentWeek}${cap ? `；Email 上限每天 ${cap} 封（含追問）` : ''}` : d}</div></div>`).join('');
  const base = L.sent || 0;
  $('#funnel').innerHTML = STAGES.map(([k, l]) => { const v = L[k] || 0, p = base ? v / base * 100 : 0; return `<div class="fr"><span>${l}</span><span class="fb"><i style="width:${Math.min(100, p)}%;${k === 'lost' ? 'background:var(--k-check)' : k === 'won' ? 'background:var(--good)' : ''}"></i></span><span class="fv">${fmt(v)}${k === 'sent' ? '' : `（${base ? p.toFixed(p < 10 && p > 0 ? 1 : 0) : 0}%）`}</span></div>`; }).join('');
  // 名單現況：repo 的 leads.csv／linkedin.csv 在產生排程時的數量（只有數量）
  const snap = state.sched?.leads;
  $('#snapCard').hidden = !snap;
  if (snap) {
    const row = (l, v, tot, color = '') => `<div class="fr"><span>${l}</span><span class="fb"><i style="width:${tot ? Math.min(100, v / tot * 100) : 0}%;${color}"></i></span><span class="fv">${fmt(v)}</span></div>`;
    const c = snap.channel || {}, chTot = Math.max(1, c.email || 0, c.form || 0, c.instagram || 0, c.linkedin || 0);
    $('#snapSub').textContent = `共 ${fmt(snap.total)} 家，美國日期 ${mmdd(snap.asOf)} 的狀態；每次部署會重新算`;
    $('#snapStatus').innerHTML = row('已聯絡', snap.sent, snap.total) + row('已排程', snap.scheduled, snap.total, 'background:var(--accent3)') + row('有回覆', snap.replied, snap.total) +
      row('成交', snap.won, snap.total, 'background:var(--good)') + row('不需要', snap.lost, snap.total, 'background:var(--k-check)') +
      row('擱置', snap.hold, snap.total, 'background:var(--k-check)') + row('未聯絡', snap.todo, snap.total, 'background:var(--k-check)');
    $('#snapChannel').innerHTML = row('Email', c.email || 0, chTot) + row('表單', c.form || 0, chTot) + row('Instagram', c.instagram || 0, chTot) + row('LinkedIn', c.linkedin || 0, chTot);
  }
  const names = Object.fromEntries(STAGES.map(([k, l]) => [k, l]));
  const log = [...S.leadLog].reverse().slice(0, 12);
  $('#leadLog').innerHTML = log.length ? log.map((x) => { const d = x.to - x.from; return `<li><span class="d">${mmdd(x.date)}</span><span class="t">${names[x.key]} ${d > 0 ? '+' : ''}${d}（${x.from} → ${x.to}）</span></li>`; }).join('') : `<li class="empty">還沒有變動</li>`;
}
document.addEventListener('click', (e) => { const b = e.target.closest('button[data-lead]'); if (!b) return; const k = b.dataset.lead; setLead(k, leadCounts()[k] + Number(b.dataset.step), '按鈕'); });
document.addEventListener('change', (e) => { const i = e.target.closest('input[data-leadin]'); if (i) setLead(i.dataset.leadin, i.value, '手動'); });

// ---- 紀錄 ----
const fWeek = $('#fWeek'), fIncome = $('#fIncome'), fOver = $('#fOver');
const formData = (f) => Object.fromEntries([...new FormData(f)].map(([k, v]) => [k, String(v).trim()]));
function hint(el, text, ok = true) { el.className = 'hint ' + (ok ? 'ok' : 'bad'); el.textContent = text; if (ok) setTimeout(() => { if (el.textContent === text) el.textContent = ''; }, 3000); }
function resetWeekForm() { fWeek.reset(); fWeek.id.value = ''; fWeek.week.value = addDays(mondayOf(tpeToday()), -7); $('#wEdit').hidden = true; fWeek.querySelector('[type=submit]').textContent = '儲存'; }
function resetIncomeForm() { fIncome.reset(); fIncome.id.value = ''; fIncome.date.value = tpeToday(); fIncome.channel.value = 'Gumroad'; $('#iEdit').hidden = true; fIncome.querySelector('[type=submit]').textContent = '儲存'; }
fWeek.onsubmit = (e) => {
  e.preventDefault();
  const v = formData(fWeek), h = $('#wHint');
  const keys = METRICS.map((m) => m[0]);
  if (!keys.some((k) => v[k] !== '')) return hint(h, '至少要填一個數字', false);
  v.week = mondayOf(v.week);
  const row = { id: v.id || uid(), week: v.week }; for (const k of keys) row[k] = v[k] === '' ? null : Number(v[k]);
  const same = S.weekly.findIndex((w) => w.week === row.week || w.id === row.id);
  if (same >= 0) { row.id = S.weekly[same].id; S.weekly[same] = row; } else S.weekly.push(row);
  S.weekly = S.weekly.filter((w, i, a) => a.findIndex((x) => x.week === w.week) === i);
  save(); resetWeekForm(); hint(h, same >= 0 ? `已更新 ${mmdd(row.week)} 那週` : `已儲存 ${mmdd(row.week)} 那週`); renderRecords();
};
fIncome.onsubmit = (e) => {
  e.preventDefault();
  const v = formData(fIncome), h = $('#iHint');
  if (!(Number(v.amount) > 0)) return hint(h, '金額要大於 0', false);
  if (/@|\+?\d[\d\s-]{8,}/.test(v.note + v.item)) return hint(h, '備註和品項不要放 Email 或電話', false);
  const row = { id: v.id || uid(), date: v.date, type: v.type, item: v.item, amount: Number(v.amount), channel: v.channel, note: v.note };
  const i = S.income.findIndex((r) => r.id === row.id);
  if (i >= 0) S.income[i] = row; else S.income.push(row);
  save(); resetIncomeForm(); hint(h, i >= 0 ? '已更新' : `已記一筆 ${usd(row.amount)}`); renderRecords(); renderKpis();
};
$('#wCancel').onclick = resetWeekForm; $('#iCancel').onclick = resetIncomeForm;
function fillOver() { for (const k of ['gumroad', 'pins', 'videos']) fOver[k].value = S.over?.[k] ?? ''; }
fOver.onsubmit = (e) => { e.preventDefault(); const v = formData(fOver); S.over = {}; for (const k of ['gumroad', 'pins', 'videos']) if (v[k] !== '') S.over[k] = Number(v[k]); save(); renderKpis(); hint($('#oHint'), '已儲存'); };
$('#overClear').onclick = () => { S.over = {}; save(); fillOver(); renderKpis(); hint($('#oHint'), '已改回自動'); };

$('#recFilter').onclick = (e) => { const b = e.target.closest('button'); if (!b) return; state.recFilter = b.dataset.v; $('#recFilter').querySelectorAll('button').forEach((x) => x.setAttribute('aria-pressed', String(x === b))); renderRecords(); };
function renderRecords() {
  const el = $('#tblRecords'), v = (x) => (x == null || x === '' ? '—' : fmt(x));
  if (state.recFilter === 'income') {
    const rows = [...S.income].sort((a, b) => (a.date < b.date ? 1 : -1));
    el.innerHTML = rows.length ? `<table><thead><tr><th>日期</th><th>類型</th><th>品項</th><th class="num">金額</th><th>管道</th><th></th></tr></thead><tbody>${rows.map((r) => `<tr><td>${esc(r.date)}</td><td>${esc(r.type)}</td><td>${esc(r.item)}</td><td class="num">${usd(Number(r.amount) || 0)}</td><td>${esc(r.channel)}</td><td class="num"><button class="btn ghost sm" type="button" data-edit="income" data-id="${esc(r.id)}">修改</button> <button class="btn ghost sm danger" type="button" data-del="income" data-id="${esc(r.id)}">刪除</button></td></tr>`).join('')}</tbody></table>` : `<div class="empty">還沒有收入</div>`;
  } else {
    const rows = [...S.weekly].sort((a, b) => (a.week < b.week ? 1 : -1));
    el.innerHTML = rows.length ? `<table><thead><tr><th>週一</th>${METRICS.map((m) => `<th class="num">${m[1]}</th>`).join('')}<th></th></tr></thead><tbody>${rows.map((w) => `<tr><td>${esc(w.week)}</td>${METRICS.map((m) => `<td class="num">${v(w[m[0]])}</td>`).join('')}<td class="num"><button class="btn ghost sm" type="button" data-edit="weekly" data-id="${esc(w.id)}">修改</button> <button class="btn ghost sm danger" type="button" data-del="weekly" data-id="${esc(w.id)}">刪除</button></td></tr>`).join('')}</tbody></table>` : `<div class="empty">還沒有每週數字</div>`;
  }
}
$('#tblRecords').onclick = (e) => {
  const ed = e.target.closest('[data-edit]'), dl = e.target.closest('[data-del]');
  if (ed) {
    if (ed.dataset.edit === 'weekly') {
      const w = S.weekly.find((x) => x.id === ed.dataset.id); if (!w) return;
      fWeek.id.value = w.id; fWeek.week.value = w.week; for (const [k] of METRICS) fWeek[k].value = w[k] ?? '';
      $('#wEditTxt').textContent = `正在修改 ${mmdd(w.week)} 那週`; $('#wEdit').hidden = false; fWeek.querySelector('[type=submit]').textContent = '儲存修改';
      fWeek.scrollIntoView({ behavior: 'smooth', block: 'start' });
    } else {
      const r = S.income.find((x) => x.id === ed.dataset.id); if (!r) return;
      for (const k of ['id', 'date', 'type', 'item', 'amount', 'channel', 'note']) fIncome[k].value = r[k] ?? '';
      $('#iEditTxt').textContent = `正在修改 ${mmdd(r.date)} ${r.type} 這一筆`; $('#iEdit').hidden = false; fIncome.querySelector('[type=submit]').textContent = '儲存修改';
      fIncome.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
  }
  if (dl) {
    if (!confirm('確定要刪除這一筆嗎？')) return;
    if (dl.dataset.del === 'weekly') S.weekly = S.weekly.filter((x) => x.id !== dl.dataset.id); else S.income = S.income.filter((x) => x.id !== dl.dataset.id);
    save(); renderRecords(); renderKpis();
  }
};

// ---- 備份 ----
$('#exportBtn').onclick = () => {
  S.lastExport = tpeToday(); save();
  const blob = new Blob([JSON.stringify(S, null, 2)], { type: 'application/json' });
  const a = document.createElement('a'); a.href = URL.createObjectURL(blob); a.download = `polyglot-後台備份-${tpeToday()}.json`;
  document.body.appendChild(a); a.click(); a.remove(); setTimeout(() => URL.revokeObjectURL(a.href), 1000);
  $('#bHint').textContent = '已匯出，檔案在下載資料夾';
};
$('#importBtn').onclick = () => $('#importFile').click();
$('#importFile').onchange = (e) => {
  const f = e.target.files[0]; if (!f) return;
  const r = new FileReader();
  r.onload = () => {
    try {
      const o = JSON.parse(r.result);
      if (!o || typeof o !== 'object' || !('done' in o || 'weekly' in o || 'income' in o)) throw 0;
      if (!confirm('匯入會蓋掉這台裝置目前的資料，確定嗎？')) return;
      S = Object.assign(blank(), o); save(); renderAll(); $('#bHint').textContent = '匯入完成';
    } catch { $('#bHint').textContent = '這不是後台的備份檔'; }
    e.target.value = '';
  };
  r.readAsText(f);
};
$('#resetBtn').onclick = () => {
  if (!confirm('會清除所有打勾、數字和收入，確定嗎？建議先匯出備份。')) return;
  S = blank(); save(); renderAll(); $('#bHint').textContent = '已清除';
};
function renderMeta() {
  const n = Object.keys(S.done).length + S.weekly.length + S.income.length;
  const gen = state.sched?.generated ? `排程 ${state.sched.generated.slice(5, 10).replace('-', '/')}` : '';
  const b = S.lastExport ? `<span class="badge">備份 ${mmdd(S.lastExport)}</span>` : n ? `<a href="#record" data-go="record" class="badge warn" style="text-decoration:none">還沒備份</a>` : '';
  $('#meta').innerHTML = gen + b;
}

// ---- 繪製 ----
function renderPage() {
  if (!state.sched) return;
  ({ overview: renderOverview, calendar: renderCalendar, stats: renderStats, income: renderIncome, leads: renderLeads, record: renderRecords })[state.page]?.();
}
function renderAll() { renderMeta(); fillOver(); renderOverviewCounts(); renderKpis(); renderPage(); }

// ---- 啟動 ----
resetWeekForm(); resetIncomeForm();
document.fonts?.ready.then(() => movePill(false));
(() => { let p = location.hash.slice(1); if (!PAGES.includes(p)) { try { p = localStorage.getItem('pp-admin.page') || 'overview'; } catch { p = 'overview'; } } go(p); })();
fetch('schedule.json?v=' + Date.now()).then((r) => { if (!r.ok) throw new Error(r.status); return r.json(); }).then((j) => {
  state.sched = j; renderAll();
  // 過了午夜自動換到新的一天
  let day = tpeToday();
  setInterval(() => { if (tpeToday() !== day) { day = tpeToday(); state.sel = null; state.cal = null; renderAll(); } else renderKpis(); }, 60000);
}).catch(() => { $('#meta').textContent = '讀不到排程'; $('#todayList').innerHTML = `<li class="empty">讀不到 schedule.json，連上網路後重新整理</li>`; });

// ---- 安裝成 App ----
if ('serviceWorker' in navigator) navigator.serviceWorker.register('sw.js').catch(() => {});
let installEvt = null;
addEventListener('beforeinstallprompt', (e) => { e.preventDefault(); installEvt = e; $('#installBtn').hidden = false; });
$('#installBtn').onclick = async () => { if (!installEvt) return; installEvt.prompt(); await installEvt.userChoice; installEvt = null; $('#installBtn').hidden = true; };
