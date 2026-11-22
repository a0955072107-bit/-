# Setup Guide

Thanks for your purchase! This guide gets your site customised and online in about 30 minutes. No coding experience needed.

---

## 1. What's inside

```
index.html           ← language entry: sends visitors to their language
en/index.html        ← English version (the whole site is this one file)
zh-TW/index.html     ← Traditional Chinese version
zh-CN/index.html     ← Simplified Chinese version
*/images/            ← photos, one folder per language
GUIDE.md             ← this guide (使用說明.md is the Chinese guide)
LICENSE.md           ← what you can and can't do
```

Every page has an EN / 繁 / 简 switcher in the header. Want all three languages? Upload the whole folder. Only need one? Upload that language's folder and remove the unused links from the switcher (search for `lang-switch`).

**If you change text in one language, remember to update the others too.**

## 2. Tools you need (all free)

- A text editor: [VS Code](https://code.visualstudio.com/) is recommended. Notepad or TextEdit also work.
- A web browser: Chrome, Edge, Safari or Firefox.

Open `index.html` in your browser to see the site. After editing, save the file and refresh the browser.

## 3. Change the text

Open `index.html` in your editor, press `Ctrl + F` (Mac: `⌘ + F`), search for the text you want to change (business name, phone number…) and type over it.

Every section starts with a marker like this:

```html
<!-- ==================== Section: Menu ==================== -->
```

**Don't need a section?** Delete from its marker down to the next marker, and remove its link from the navigation.

### Things you must change (search for these)

| Search for | Replace with |
|---|---|
| The sample business name | Your business name (use "Replace All") |
| `(555) 012-3456` / `555` numbers | Your phone number |
| `wa.me/15550123456` | Your WhatsApp number (or swap in a LINE / Messenger / Instagram link) |
| The sample address in `maps.google.com/?q=` | Your address |
| `your-form-id` | Your Formspree form ID (see section 6) |
| `<title>` and `description` | Your name and a one-line description (shown in Google results) |
| The `application/ld+json` block | Name, phone, address, opening hours (helps Google Maps and search show your details correctly) |

## 4. Change colours and fonts

Near the top of `index.html` you'll find **THEME SETTINGS**:

```css
:root {
  --brand: #b5532c;   /* main colour: buttons, highlights */
  --bg: #f7f1e8;      /* background */
  --text: #2a211c;    /* text colour */
  ...
}
```

Change these values and the whole site updates. Need a palette? Try [coolors.co](https://coolors.co/).

> Tip: keep enough contrast between text and background. Check it with the [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/).

## 5. Use your own photos

Image areas ship as designed gradient artwork, so there are no stock-photo licences to worry about. To use real photos:

1. Put your photo in the `images/` folder next to your `index.html`, e.g. `images/hero.jpg`.
2. In `index.html`, search for `Replace with a photo`. You'll find comments like:
   ```css
   /* Replace with a photo: .img-hero { background: url(images/hero.jpg) center/cover; } */
   ```
3. Copy that line (without the comment markers) to just before `</style>` and change the file name.

**Photo tips**
- 1600–2000px wide is plenty. Compress with [Squoosh](https://squoosh.app/) for a faster site.
- Only use photos you took yourself or are licensed to use (e.g. free-for-commercial-use images from [Unsplash](https://unsplash.com/) or [Pexels](https://www.pexels.com/)).

## 6. Make the form send you email (Formspree, free)

1. Sign up at [formspree.io](https://formspree.io/) and click **New Form**.
2. Copy the ID at the end of the form URL, e.g. `xyzabcd`.
3. Search `your-form-id` in `index.html` and replace it with your ID.

Submissions now arrive in your inbox. The free plan covers 50 submissions a month. Prefer no form? Delete the form section and keep the phone and chat buttons.

## 7. Put it online (pick one, all free)

### A. Netlify Drop (easiest, ~3 minutes)
1. Go to [app.netlify.com/drop](https://app.netlify.com/drop).
2. Drag the whole folder (all languages go live) or a single language folder onto the page.
3. Done. You get a `xxx.netlify.app` address; create a free account to keep the site and rename it.

### B. GitHub Pages
1. Create a GitHub account and a new repository.
2. Click **Add file → Upload files** and upload `index.html` and the `images/` folder.
3. Go to **Settings → Pages**, choose the `main` branch and click Save.
4. After a minute or two your site is at `https://your-username.github.io/repository-name/`.

### C. Cloudflare Pages
Go to [pages.cloudflare.com](https://pages.cloudflare.com/), choose **Upload assets** and upload the folder.

### Using your own domain (e.g. `www.yourshop.com`)
Buy a domain from a registrar (Cloudflare, Namecheap, Porkbun…), then follow the "Custom domain" steps in Netlify, GitHub or Cloudflare.

## 8. Get found on Google

1. Add and verify your site in [Google Search Console](https://search.google.com/search-console).
2. Create a [Google Business Profile](https://business.google.com/) and add your website. For local businesses this is the single most effective step.

## 9. Privacy and EU visitors (GDPR)

- **Maps**: the templates link to Google Maps instead of embedding it, so nothing loads from Google until a visitor clicks.
- **Fonts**: fonts load from Google Fonts. For strict GDPR compliance (recommended for German businesses), host them yourself:
  1. Go to [gwfh.mranftl.com/fonts](https://gwfh.mranftl.com/fonts) (google-webfonts-helper) and pick the fonts named in the `fonts.googleapis.com` link near the top of `index.html`.
  2. Download the `woff2` files into a `fonts/` folder next to `index.html` and copy the generated CSS into the `<style>` block.
  3. Delete the `<link>` tags that point to `fonts.googleapis.com` and `fonts.gstatic.com`.
- **Privacy policy**: adapt `PRIVACY-TEMPLATE.md`, save it as `privacy.html` and link it in the footer. Businesses in Germany and Austria also need an **Impressum** page (legal business details).
- **Forms**: Formspree stores submissions. Mention it in your privacy policy.

## 10. FAQ

**The fonts look different on my phone.**
The template loads Google Fonts online. On a slow connection the browser shows a system font first; this is normal.

**Can I make it multi-page?**
Yes. Copy `index.html` to e.g. `about.html`, delete the sections you don't need, and point the navigation links to `about.html`.

**I broke something.**
Keep a backup of the original before editing, or re-download your purchase.

---

## Want us to customise it for you?

Don't have time to edit it yourself? We can turn this template into a ready-to-launch site for your business: your text, photos, colours, booking links and domain set up for you. Message us through Gumroad or see our **Website Customization Service** listing.
