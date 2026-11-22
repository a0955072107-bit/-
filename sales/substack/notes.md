# Substack Notes（4 週份，每週一、三、五各 1 則）

## 第 1 週
1. A website builder at $29/month costs a café over $1,000 in three years. Most cafés need one page: hours, menu, map, phone. That fits in a single HTML file and hosts free. Wrote up the whole setup this week.
2. Small detail that matters most on restaurant sites: an "Open now / Closed now" badge that reads your real hours. It's the first thing people look for.
3. Free hosting for a one-page business site: Netlify Drop. Drag the folder onto the page, done, HTTPS included. Your only recurring cost is the domain.

## 第 2 週
1. Walk down Main Street in Flushing and the menus are in English, 繁體 and 简体. The shops speak three languages. Their websites usually speak one.
2. We replaced a row of language links (EN · 繁 · 简 · JA · ES) with one button that opens a list. Five links didn't fit next to the logo on phones. Built with <details>, so it works without JavaScript.
3. Translation vs localisation: the Japanese version of our restaurant template isn't just translated. Prices are in yen with tax included, the contact button is LINE, and hours use 〜.

## 第 3 週
1. We built five animated templates without GSAP or any library. CSS scroll-driven animations + the Web Animations API cover almost everything now.
2. Rule for every animated template: if a visitor turns on "reduce motion", every animation switches off and the content is simply there.
3. `animation-timeline: view()` is the most useful CSS property I've learned this year. Scroll reveals with zero JavaScript.

## 第 4 週
1. New template: a restaurant site that knows when you're open. Live badge, menu tabs, reservation form, five languages.
2. What a local business site needs to answer: Are you open? Where are you? What do you sell? How do I contact you? Everything else is optional.
3. Google Business Profile matters more than the website for most local shops. Fill it in first, then link your site.
