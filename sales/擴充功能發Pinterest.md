# 用 Chrome 擴充功能發 Pinterest（給 Claude in Chrome／Cowork 讀）

> **使用者怎麼用**：
> 1. 在電腦把 `sales/pins/` 這個資料夾準備好（星期一會和上架包一起傳給你），裡面有 105 張圖和 `pins.csv`。
> 2. Chrome 登入 Pinterest **商業帳號**（Business account，免費；個人帳號可在設定裡免費轉換）。
> 3. 打開 Claude 擴充功能，新對話貼上：
>
> 「照 https://github.com/a0955072107-bit/-/blob/main/sales/擴充功能發Pinterest.md 發 Pinterest，今天做第 1 天。」

---

## 給擴充功能的規則

1. **每天最多 15 張**。新帳號一次發太多容易被 Pinterest 判定成垃圾帳號。照下面「每天的份量」做，做完就停。
2. 圖片上傳要使用者做：每一張開始前，告訴使用者「請把 `檔名` 拖進上傳框」，等使用者說好了再填文字。
3. 文字一律照 `pins.csv` 對應那一列，一字不改：
   `https://github.com/a0955072107-bit/-/blob/main/sales/pins/pins.csv`
   - **標題**＝`title`、**說明**＝`description`、**連結**＝`link`、**看板**＝`board`
   - `keywords` 欄：在說明最後空一行，用 `#` 加上前 3 個關鍵字（去掉空格），例如 `#restaurantwebsitetemplate`
4. 看板不存在就建立（名稱照 `board` 欄），設為公開。
5. 用 **排程發布（Schedule）**：同一天的圖平均分散在台灣時間 09:00～23:00，不要同時發。
6. 不要按讚、留言、追蹤別人，不要改帳號設定。遇到驗證或付款畫面就停下來問。
7. 每做完一張回報一行：檔名、看板、排程時間。

---

## 先建好的看板（第 1 天開始前）

| 看板 | 放哪些圖 |
|---|---|
| Small Business Website Templates | 每款的 `-a.jpg`（英文功能圖） |
| Multilingual Website Templates | 每款的 `-b.jpg`（多語言圖） |
| Animated Website Templates | Motion 系列的 `-a.jpg` |
| ホームページ テンプレート | 每款的 `-c.jpg`（日文圖） |

## 每天的份量（7 天發完 105 張）

`pins.csv` 從上往下，每天做 15 列：

| 天 | csv 列 |
|---|---|
| 第 1 天 | 第 1～15 列 |
| 第 2 天 | 第 16～30 列 |
| 第 3 天 | 第 31～45 列 |
| 第 4 天 | 第 46～60 列 |
| 第 5 天 | 第 61～75 列 |
| 第 6 天 | 第 76～90 列 |
| 第 7 天 | 第 91～105 列 |

（列數不含標題列。）

**注意**：連結要等 Gumroad 商品**發布後**才打得開。第 1 天開始前，先確認 `pins.csv` 裡的商品都已發布；還沒發布的那幾列先跳過，最後再補。

---

## 第 2 批（第 8～12 天，每天 14 張）

使用者說「發第 2 批第 N 天」時，改用 `pins-2.csv`：
`https://github.com/a0955072107-bit/-/blob/main/sales/pins/pins-2.csv`

| 天 | pins-2.csv 列 |
|---|---|
| 第 8 天 | 第 1～14 列 |
| 第 9 天 | 第 15～28 列 |
| 第 10 天 | 第 29～42 列 |
| 第 11 天 | 第 43～56 列 |
| 第 12 天 | 第 57～70 列 |

新看板（不存在就建立，公開）：**Small Business Website Ideas**（`-e.jpg` 用）。
每週日新模板的 3 張圖，下週一跟當天的份量一起發（當天最多 20 張）。
