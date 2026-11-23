# Substack Notes（4 週份，每天 1 則）

> 用擴充功能存草稿時說「發第 X 週第 Y 天的 Note」。第 1 週第 1 天＝ 11/24（二），之後每天 1 則。

## 第 1 週（11/24～11/30）
1. A website builder at $29/month costs a café over $1,000 in three years. Most cafés need one page: hours, menu, map, phone. That fits in a single HTML file and hosts free. Wrote up the whole setup this week.
2. The four questions every local business site has to answer: Are you open? Where are you? What do you sell? How do I contact you? Everything else is optional.
3. Small detail that matters most on restaurant sites: an "Open now / Closed now" badge that reads your real hours. It's the first thing people look for.
4. Free hosting for a one-page business site: Netlify Drop. Drag the folder onto the page, done, HTTPS included. Your only recurring cost is the domain.
5. Google Business Profile matters more than the website for most local shops. Fill it in first, then link your site from it.
6. A sticky "Call" and "Book" bar at the bottom of the phone screen does more for a small business site than any hero animation.
7. Things a one-page site doesn't need: a blog nobody updates, a slider, a newsletter popup on first visit. Things it does: hours, a map link, a phone number you can tap.

## 第 2 週（12/1～12/7）
1. Walk down Main Street in Flushing and the menus are in English, 繁體 and 简体. The shops speak three languages. Their websites usually speak one.
2. We replaced a row of language links (EN · 繁 · 简 · JA · ES) with one button that opens a list. Five links didn't fit next to the logo on phones. Built with <details>, so it works without JavaScript.
3. Translation vs localisation: the Japanese version of our restaurant template isn't just translated. Prices are in yen with tax included, the contact button is LINE, and hours use 〜.
4. Each language is its own page, not a translation layer in JavaScript. Google indexes each one, and the owner can edit the Chinese menu without touching the English one.
5. OpenCC converts Traditional to Simplified Chinese with regional vocabulary (影片 → 视频, 軟體 → 软件). We still fix a few things by hand: the link to the Traditional page keeps saying 繁體中文.
6. Japanese headings need different line-break rules, or a single character ends up alone on the last line. `word-break: auto-phrase` fixes most of it.
7. The root index.html of each template checks the browser language and sends visitors to the right folder. Taiwan → 繁體, Singapore → 简体, everyone else → English.

## 第 3 週（12/8～12/14）
1. We built five animated templates without GSAP or any library. CSS scroll-driven animations + the Web Animations API cover almost everything now.
2. Rule for every animated template: if a visitor turns on "reduce motion", every animation switches off and the content is simply there.
3. `animation-timeline: view()` is the most useful CSS property I've learned this year. Scroll reveals with zero JavaScript.
4. Nothing should be hidden behind an animation. With JavaScript off, every section of our templates is still visible and every button works.
5. A shader background can be a few dozen lines of plain WebGL. No library, nothing to update, nothing to license.
6. Animate transform and opacity only. Anything else causes layout shift, and on a cheap phone you can feel it.
7. If a browser doesn't support scroll-driven animations, elements just appear without the effect. For a business website that's the right way to fail.

## 第 4 週（12/15～12/21）
1. New template: a restaurant site that knows when you're open. Live badge, menu tabs, reservation form, five languages.
2. Why one HTML file? You can open it, edit it in any text editor, and move it to any host. No account to lose, no platform to shut down.
3. Change your brand colour in one place at the top of the file and the whole site follows. That's what CSS custom properties are for.
4. Before buying a website builder subscription, ask: will I update this site more than once a month? If not, you're paying for an editor you won't use.
5. A contact form doesn't need a backend. Formspree's free plan sends submissions straight to your inbox.
6. Your domain is the one thing to keep in your own name. Hosts can change; the domain is how customers find you.
7. Small shops don't need more features. They need the four basics done well, on a phone, in the languages their customers read.
