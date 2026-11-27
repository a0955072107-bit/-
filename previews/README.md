# 線上預覽用照片（內部用，不放進商品）

使用者 2026-11-25 決定：**線上預覽頁用真實感照片，買家下載的模板維持 CSS 佔位圖＋換照片說明。**

- `previews/<款式>/photos/*.webp`：示意照片；`photos.css`：把佔位圖換成照片的覆蓋樣式。
- `previews/preview-note.css`：頁尾「示意照片」說明的樣式。
- `scripts/build-site.sh` 建置時把 `previews/<款式>/` 複製到 `_site/templates/<款式>/_preview/`，並在各語言頁加入樣式與說明文字。
- `scripts/package.sh` 只打包 `templates/`，**不會**包含這裡的任何檔案。

## 新款的製作流程（2026-11-25 起每款必做）
1. 設計總監在設計計畫裡寫「照片清單」：class、比例、內容、英文提示詞。
2. 主工作階段用 Canva：`generate-image`（指定比例）→ `create-design`（只放這張照片、滿版）→ `export-design`（jpg；方形圖指定 width／height 1600，避免只匯出 529px）。
3. 用 Pillow 縮到長邊 1000～1600px、轉 WebP（quality 78），放進 `previews/<slug>/photos/`。
4. 寫 `previews/<slug>/photos.css`：每個 class 設 `background: url(photos/xxx.webp) center / cover`，並關掉佔位圖的 ::before／::after。
5. `bash scripts/build-site.sh` 後截圖檢查，在下方表格補上這款的照片清單。

## 來源與授權
- 全部照片由使用者的 Canva 帳號以 AI 生成（2026-11-25），再匯出原尺寸、縮圖轉 WebP。
- Canva 官方說明：AI 生成圖片可在設計中商用（例如商品網站的預覽頁），但不可單獨販售或做成素材轉賣，也不能主張著作權。因此這些照片**只能用在預覽頁，不可放進販售的模板檔案**。
- clinic 的醫師照片是 AI 生成的**虛構人物**，不是真人。
- 預覽頁頁尾會自動加上可見說明：店名、人物、評價、數據與照片皆為虛構（`scripts/build-site.sh` 的 NOTE）。

| 檔案 | 內容 |
|---|---|
| restaurant/hero | 俯拍燉牛肉蓋飯、半熟蛋、藍染筷架、醃蘿蔔 |
| restaurant/about | 手沖咖啡與莓果塔 |
| restaurant/gallery-1～5 | 窗邊座位、藍染暖簾前的拿鐵、莓果塔、夜晚吧台、三碟小菜 |
| clinic/hero | 深藍綠診療椅、大窗的診間 |
| clinic/doctor-1～3 | 虛構醫師半身照（院長、主治醫師兩位） |
| dental/hero | 霧鼠尾草牆、大窗、松綠色診療椅與觀葉植物，左側留白給文字面板（16:9） |
| dental/doctor-1～3 | 虛構醫師半身照：院長（50 多歲男性）、主治醫師（30 多歲女性、40 多歲男性）（4:5） |
| dental/space-1、space-2 | 候診區（橡木長椅、植物）、諮詢室（平板顯示牙齒 X 光）（3:2） |
