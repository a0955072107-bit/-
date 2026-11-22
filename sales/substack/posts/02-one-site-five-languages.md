# One website, five languages: how we built a language switcher for small shops

*Subtitle: A dumpling house in Queens has customers who read English, Traditional Chinese and Simplified Chinese. Its website should too.*

Walk down Main Street in Flushing, or through the San Gabriel Valley, and look at the menus in the windows. English, Traditional Chinese, Simplified Chinese, often Korean or Spanish too. The shops already speak several languages. Their websites, when they have one, usually speak one.

When we started building templates, we decided every template would ship in several languages from day one: English, Traditional Chinese, Simplified Chinese and Japanese, with Spanish on some. Here's how it works and what we learned.

## The structure: one folder per language

Each template is a folder like this:

```
index.html      ← sends visitors to their language
en/index.html
zh-TW/index.html
zh-CN/index.html
ja/index.html
```

Each language is a complete page, not a translation layer bolted on with JavaScript. That matters for three reasons:

- **Google indexes each language separately.** Someone searching in Chinese can find the Chinese page.
- **It works without JavaScript.** Nothing to load, nothing to break.
- **The owner can edit it.** Changing the Chinese menu means opening the Chinese file. No translation keys, no plugin.

The root `index.html` checks the browser's language and sends the visitor to the right folder. A Taiwanese visitor lands on Traditional Chinese, someone in Singapore on Simplified, everyone else on English.

## The switcher: one button, not five

Our first version had a row of links in the header: EN · 繁 · 简. When we added Japanese and Spanish, the row no longer fit next to the logo and menu button on phones. On some layouts it pushed the menu button off the screen.

So the header now shows only the current language, "EN ▾", and tapping it opens the full list. It's built with the HTML `<details>` element, so it works with JavaScript turned off, is keyboard accessible, and takes less room than the original three links did. The footer still lists every language as plain links.

## Translation is not the same as localisation

The surprising part wasn't the code. It was the content. A literal translation reads like a translation. So each language version is localised:

- **Prices and currency** match the market: dollars in the US, yen with tax included in Japan.
- **Contact buttons** match what people use: WhatsApp in many places, LINE in Taiwan and Japan, WeChat for many Chinese-speaking customers.
- **Addresses, phone formats and opening hours** follow local conventions.
- **Typography changes.** Japanese headings need different line-breaking rules, or a single character ends up alone on the last line.

## Simplified from Traditional, carefully

We write Traditional Chinese first and convert to Simplified with OpenCC, which handles regional vocabulary, not just characters (影片 becomes 视频, 軟體 becomes 软件). Then a few things are fixed by hand. Language names, for example, stay in their own script: the link to the Traditional version still says 繁體中文 even on the Simplified page.

## Try it

Open any demo and tap the language button in the top corner:
[Restaurant template demo](https://a0955072107-bit.github.io/-/templates/restaurant/en/)

All 35 templates work this way: [polyglotpages.gumroad.com](https://polyglotpages.gumroad.com)

If you run a shop that serves customers in English and Chinese, we also build these for you: [trilingual website service](https://polyglotpages.gumroad.com/l/trilingual-website-service).
