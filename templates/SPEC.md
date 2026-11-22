# 模板製作規格（內部用，打包時不會放進商品）

> **固定規則：每一個新增或修改的頁面，交付前都要通過 Hallmark 檢查。** 執行 `bash scripts/lint-all.sh`，結果必須是「0 頁有需要處理的 FAIL」（可以忽略的只有 #20 戳記，以及 #19 的時間或數字範圍）。

所有模板都要遵守這份規格，買家才有一致、好改的使用體驗。

## 檔案
- 每個模板只有一個檔案：`templates/<slug>/index.html`，CSS 和 JS 都寫在檔案裡。
- 只能載入 Google Fonts，不能用其他 CDN 或函式庫。原生 JS 控制在約 80 行以內。
- `lang="zh-Hant"`，文案用台灣繁體中文、口吻自然。商家名稱、電話、地址都是虛構的（電話用 `02-1234-5678` 這種格式），不能用真實品牌。

## 主題設定（最重要的賣點）
- `<style>` 一開始先放這段：
  ```
  /* ============================================================
     主題設定：改這裡就能換整站配色與字型
     ============================================================ */
  :root { --brand; --brand-ink（在 brand 色上的文字顏色）; --bg; --surface; --text; --muted; --line; --radius; --font-heading; --font-body; ... }
  ```
  每個變數都要加一行中文註解。
- 這段之外不能寫死任何顏色值，一律用 `var(--x)` 或 `color-mix(in srgb, var(--x) N%, transparent)`。
- 文字對比要達到 WCAG AA。

## 圖片
- 不使用照片，所以沒有圖片授權問題。圖片區塊用
  `<div class="img img-xx" role="img" aria-label="說明"></div>`，
  搭配符合該行業氛圍的 CSS 漸層／幾何圖樣當「藝術佔位圖」，要好看、有設計感，不能只是一塊灰。
- 在圖片相關 CSS 上方加註解，說明怎麼換成真實照片：
  `/* 換成照片：.img-xx { background: url(images/xxx.jpg) center/cover; } */`

## 結構
- 每個區塊前面加 `<!-- ==================== 區塊：名稱 ==================== -->`，讓買家好找、好刪。
- 用語意化標籤（header/nav/main/section/footer），每個 section 都要有 id，給導覽列錨點使用。
- 頁首固定在上方，捲動後出現背景；寬度 760px 以下改成漢堡選單（button 加上 aria-expanded，點連結後選單自動關閉）。
- 捲動漸入動畫：用 IntersectionObserver 加 `.in` class。只在 `<html>` 有 `js` class 時才先隱藏，沒有 JS 的時候內容仍然要看得到。要支援 `prefers-reduced-motion`。
- 要有 `:focus-visible` 樣式。

## 響應式
- 手機優先。360px 寬度不能出現水平捲軸（html/body 都加 `overflow-x: clip`）。表格太寬時，用一個可以水平捲動的外框包住。
- 在 390px 和 1440px 寬度都要好看。

## 聯絡與轉換
- 要有電話 `tel:` 按鈕、LINE 按鈕（`https://line.me/R/ti/p/@yourlineid`）、Google 地圖連結（`https://maps.google.com/?q=地址`）。
- 有表單的話，`action="https://formspree.io/f/your-form-id" method="POST"`，並加註解說明怎麼申請 Formspree（免費）。
- 手機版要在畫面底部放一個固定的主要行動按鈕（例如「立即訂位」「LINE 預約」）。

## SEO
- `<title>`、meta description、Open Graph（og:title、og:description、og:type）、theme-color。
- 依行業放一段 JSON-LD schema.org，例如 Restaurant、BeautySalon、ExerciseGym、Dentist、ProfessionalService/LegalService，內容包含名稱、電話、地址、營業時間。

## 頁尾
- 商家名稱、地址、電話、營業時間、社群連結（`#` 佔位）、`© <span id="y"></span> 商家名稱`（用 JS 填入年份）。

## 驗收
- 用 Playwright（`require('playwright')`，chromium.launch() 不需要參數）分別截 1440×900 和 390×844 的整頁截圖（fullPage、deviceScaleFactor 1），存到
  `/tmp/claude-0/-home-user--/205e49d8-9465-5a2b-bca8-edeae4bfe130/scratchpad/shots/<slug>-desktop.png`、`<slug>-mobile.png`。
  實際打開圖片檢查，修好版面問題後再截一次。Google Fonts 在沙箱裡不一定載得到；系統的中文備用字型是 WenQuanYi Zen Hei，這是正常的。
- 用 JS 檢查 390px 寬度時 `document.documentElement.scrollWidth <= 390`，而且 console 不能有錯誤。

## 設計規則（Hallmark 防 AI 感，必須遵守）
1. 標題上方不要放小標籤（eyebrow，例如 h2 上面的「OUR SERVICES」）。
2. 不要用「大寫字母＋加寬字距」的小字標籤。導覽列、標籤、說明文字、表頭都用內文字型，字級小一階，正常大小寫，字距正常。
3. 不要用「A · B · C」這種用中間點串起來的資訊字串，不要在連結文字後面黏箭頭（「了解更多 →」），不要用裝飾性的狀態圓點，不要用 emoji 當圖示，不要在標題裡把單一個字改成斜體或另一個顏色。
4. 不要用紫色到藍色、紫色到粉色的漸層。
5. 不要寫 `transition: all`，也不要對 width、height、top、left 做動畫。
6. 所有顏色（包含陰影的 rgba）都要用 :root 裡的變數。白色也要略帶主色調，不要用純 #fff。
7. 放圖片的 grid 欄位用 `minmax(0,1fr)`。大標題加上 `overflow-wrap: break-word; min-width: 0; text-wrap: balance`。
8. 按鈕和連結要有 :hover、:active、:focus-visible 三種狀態。標題層級一次只能降一級（不要從 h1 直接跳到 h3）。
9. 1280×800 的畫面不捲動，就要看得到首屏的大標題、一句說明和主要按鈕。首屏文字要簡短。
10. 內文的句子裡不要用破折號（—、–）。時間範圍可以用，例如 10:00–18:00。
11. 虛構的評價和數據旁邊，都要加上 `<!-- 範例內容：上線前請換成真實資料 -->`。
12. 手機選單要有不用 JS 也能運作的備案：隱藏選單的樣式只在 `html.js` 底下生效。沒有 JS 時，選單換行顯示在 logo 下方，header 改成 position: sticky。

## 英文版
- 同一個模板要另外做一份英文版，放在 `templates/en/<slug>/index.html`。設計、CSS、JS 都要和中文版一樣，只改語言和跟語言有關的內容。
- 英文版用自然、道地的行銷英文，不要直譯。店名改成英文的虛構名稱，地址用虛構的美國地址（例如 `128 Maple Street, Portland, OR 97205`），電話用 `(555) 012-3456`，價格用美元。
- LINE 按鈕改成 WhatsApp（`https://wa.me/15550123456`），並加註解說明買家可以換回 LINE、Messenger 或 Instagram。
- 所有程式碼註解都翻成英文：例如 `Section: 名稱`、`THEME SETTINGS`、`Replace with a photo: …`、`Sample content — replace before going live`。
- 中文字型換成風格相近的拉丁字型，並移除用不到的字型載入。
- 檢查英文版裡沒有殘留任何中文字。

## 驗收補充
- lint：把檔案複製到 scratchpad，執行 `node /home/user/nutlope/hallmark/skills/hallmark/scripts/sloplint.mjs <副本>`。第 20 條（戳記）可以忽略，第 19 條如果是時間範圍也可以忽略，其他 FAIL 都要修掉。
- 截圖和所有暫存檔都只能放在 scratchpad 裡，不要寫進 repo。

## Motion 動態系列（高價款）額外規格
- 檔案放在：中文 `templates/motion/<slug>/index.html`，英文 `templates/en/motion/<slug>/index.html`。
- **不使用任何第三方動畫函式庫**（包含 GSAP、Lottie、Three.js），以避免授權風險。只用瀏覽器內建的技術：CSS 動畫、CSS 捲動驅動動畫（`animation-timeline: view()／scroll()`，並用 `@supports` 提供備案）、Web Animations API、IntersectionObserver、requestAnimationFrame、Canvas 2D 或手寫 WebGL。
- 動畫要「精緻、有記憶點」，至少包含 4 種：捲動視差、跟著捲動播放的進度動畫、文字逐字或逐行浮現、圖片或區塊遮罩展開、磁吸按鈕或游標互動、首屏 Canvas 或 WebGL 背景、數字或圖表動畫、水平捲動區塊。
- 效能：只對 transform 和 opacity 做動畫；不在 scroll 事件裡改版面；Canvas 或 WebGL 在畫面外時要暫停，裝置像素比上限設為 2，手機上要降低粒子數；WebGL 不可用時退回 CSS 漸層。
- 無障礙：`prefers-reduced-motion: reduce` 時關掉所有動畫，內容直接呈現；關掉 JS 時內容也要完整可見。
- 主題設定區要多一組「動畫設定」變數：`--motion-speed`、`--motion-ease`、`--motion-distance`，並加中文或英文註解。
- 其餘規格（主題設定、區塊註解、SEO、表單、手機版、Hallmark 規則、英文版規則、驗收）照舊。

## 語言切換（每款的每個語言版本都要有）
上線時的資料夾結構是 `en/`、`zh-TW/`、`zh-CN/` 三個並排的資料夾，所以連結一律用 `../<語言>/`。

1. `<head>` 裡加入下面這段（含註解，買家上線後要換成完整網址）：
```html
<!-- 多語版本（SEO）：上線後把 href 換成完整網址，例如 https://www.你的店.com/en/ -->
<link rel="alternate" hreflang="en" href="../en/">
<link rel="alternate" hreflang="zh-Hant" href="../zh-TW/">
<link rel="alternate" hreflang="zh-Hans" href="../zh-CN/">
<link rel="alternate" hreflang="x-default" href="../en/">
```
2. 頁首放語言切換，標記固定如下（目前所在的語言加上 `aria-current="page"`）：
```html
<!-- lang-switch：語言切換。要新增語言時，在這裡加一個連結，並新增對應的資料夾 -->
<nav class="lang-switch" aria-label="Language 語言">
  <a href="../en/" hreflang="en" lang="en">EN</a>
  <a href="../zh-TW/" hreflang="zh-Hant" lang="zh-Hant">繁</a>
  <a href="../zh-CN/" hreflang="zh-Hans" lang="zh-Hans">简</a>
</nav>
```
3. 位置：桌機放在頁首主要按鈕旁邊；手機放在漢堡按鈕旁邊，保持可見，或放在展開選單的最上方。沒有 JS 時也要看得到、點得到。
4. 樣式：用該模板自己的主題變數，小巧低調。目前語言要用字重或底線標示，不能只靠顏色。點擊範圍至少 32×32px，要有 :hover、:active、:focus-visible。不要讓頁首換行或擠壓到 logo；360px 寬度也不能出現水平捲軸。
5. 頁尾也放同一組連結（可以更簡單，例如文字連結）。

## 日本語版（templates/ja/<款式>/index.html）

- 從英文版複製後翻譯成自然的日文（です・ます調），不要逐字直譯。`<html lang="ja">`。
- 字型：內文 `Noto Sans JP` 或 `Zen Kaku Gothic New`，標題可用 `Noto Serif JP`／`Shippori Mincho`，透過 Google Fonts 載入，並保留系統字型備援（`"Hiragino Sans", "Yu Gothic", sans-serif`）。
- 日文排版：`line-break: strict;`，標題不要加字距（letter-spacing 保持 0 或 normal），長標題用 `<wbr>` 或 `text-wrap: balance` 避免單字斷行。
- 在地化範例資料：店名、東京或大阪的地址、`03-1234-5678` 格式電話、`¥` 價格（含稅表示「税込」）、營業時間「11:00〜21:00」、聯絡方式以 LINE、電話、Instagram 為主。
- JSON-LD 的地址、電話、`priceCurrency: "JPY"` 都要改。
- 語言切換：不要自己加 JA 連結，也不要保留 EN 連結上的 `aria-current`；全部日文頁做完後，統一執行一次 `python3 scripts/add-lang.py ja JA 日本語`，它會在所有語言版本加上 JA 連結，並在日文頁標記目前語言。
- 驗收和其他語言相同，並且必須通過 Hallmark（`bash scripts/lint-all.sh` 為 0 頁 FAIL）。
