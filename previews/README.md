# 線上預覽用照片（內部用，不放進商品）

使用者 2026-11-25 決定：**線上預覽頁用真實感照片，買家下載的模板維持 CSS 佔位圖＋換照片說明。**

- `previews/<款式>/photos/*.webp`：示意照片；`photos.css`：把佔位圖換成照片的覆蓋樣式。
- `previews/preview-note.css`：頁尾「示意照片」說明的樣式。
- `scripts/build-site.sh` 建置時把 `previews/<款式>/` 複製到 `_site/templates/<款式>/_preview/`，並在各語言頁加入樣式與說明文字。
- `scripts/package.sh` 只打包 `templates/`，**不會**包含這裡的任何檔案。

## 來源與授權
- 全部照片由使用者的 Canva 帳號以 AI 生成（2026-11-25），再匯出原尺寸、縮圖轉 WebP。
- Canva 官方說明：AI 生成圖片可在設計中商用（例如商品網站的預覽頁），但不可單獨販售或做成素材轉賣，也不能主張著作權。因此這些照片**只能用在預覽頁，不可放進販售的模板檔案**。
- clinic 的醫師照片是 AI 生成的**虛構人物**，不是真人。

| 檔案 | 內容 |
|---|---|
| restaurant/hero | 俯拍燉牛肉蓋飯、半熟蛋、藍染筷架、醃蘿蔔 |
| restaurant/about | 手沖咖啡與莓果塔 |
| restaurant/gallery-1～5 | 窗邊座位、藍染暖簾前的拿鐵、莓果塔、夜晚吧台、三碟小菜 |
| clinic/hero | 深藍綠診療椅、大窗的診間 |
| clinic/doctor-1～3 | 虛構醫師半身照（院長、主治醫師兩位） |
