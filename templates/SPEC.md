# 模板製作規格（內部用，打包時不會放進商品）

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
