# Lumen Studio — 一頁式網站

極簡、編輯風格的一頁式網站，純 HTML + CSS + 少量 JavaScript，不需要任何建置工具。

## 特色
- 襯線字體排版（Cormorant Garamond + Noto Serif TC）、紙張顆粒質感
- 標題逐行浮現、捲動漸入、數字計數動畫
- 自動深色模式、響應式（手機／桌機）、支援「減少動態效果」設定

## 本機預覽
直接用瀏覽器打開 `index.html` 即可。

## 部署到 GitHub Pages
1. 將此分支合併到 `main`。
2. 到 repo 的 **Settings → Pages → Build and deployment → Source** 選擇 **GitHub Actions**。
3. 推送到 `main` 後，`.github/workflows/pages.yml` 會自動部署，網址為
   `https://<你的帳號>.github.io/<repo 名稱>/`。

## 自訂內容
所有文字都在 `index.html` 中；顏色在檔案開頭 `:root` 的 CSS 變數（`--bg`、`--ink`、`--accent`）。
作品圖目前是 CSS 漸層，可把 `.a1`～`.a4` 換成 `background: url(圖片.jpg) center/cover;`。
