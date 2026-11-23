# Pinterest 一次排好 167 張（批次上傳 CSV）

不用每天發、不用拖 167 張圖：上傳一個 CSV，Pinterest 會依網址自己抓圖，照排好的時間每天發 15 張（11/26～12/7，台灣時間 09:00～23:00）。

## 開始前（只做一次）
1. **確認 Gumroad 模板商品都已發布**：圖片的連結會連到各模板的商品頁。還沒上架完的話，跟 Claude 說新的開始日期，重新產生 CSV：`python3 scripts/pins/bulk-csv.py 2026-11-28`
2. **先建好 5 個看板**（名稱要一字不差，設為公開）。可以叫擴充功能建：
   - Small Business Website Templates
   - Multilingual Website Templates
   - Animated Website Templates
   - Small Business Website Ideas
   - ホームページ テンプレート

## 上傳（你做，約 3 分鐘）
1. 電腦打開 Pinterest，右上角 **建立（Create）** → **建立 Pin** → 找 **批次建立 Pin（Bulk create Pins）**。
   （有些帳號在 **Pinterest 商業中心 → 建立 → 批次建立 Pin**。）
2. **上傳 .csv 檔** → 選 `pinterest-bulk.csv`。
3. Pinterest 會檢查每一列。有錯誤的列會標出來，截圖給 Claude。
4. 確認後送出。之後每天會自動發 15 張，在「已排程的 Pin」裡看得到。

## 注意
- 一個 CSV 最多 200 張，這份有 167 張。
- Pinterest 最多只能排到 30 天後。
- 圖片網址是 `https://a0955072107-bit.github.io/-/pins/…`，要等 GitHub 合併、部署完成後才抓得到圖。
- 之後每週日的新圖，Claude 會另外產生一份小 CSV。
