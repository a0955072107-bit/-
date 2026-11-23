# 商品檔改用 Google Drive 連結（給 Claude in Chrome／Cowork 讀）

> 為什麼：擴充功能不能把檔案傳進 Gumroad 的上傳框（系統權限擋下）。所以 zip 放在 Google Drive，Gumroad 的 Content 頁放下載連結；縮圖不放（Gumroad 會用封面）。這樣擴充功能全程不用上傳檔案。

## 使用者只做一次（約 3 分鐘）
1. Chrome 用 **polyglotpages.studio@gmail.com** 登入 https://drive.google.com
2. 新增資料夾：`Polyglot Pages – product files`
3. 把「全部商品zip.zip」**解壓後的 37 個 zip** 整批拖進這個資料夾，等上傳完成。
4. **資料夾本身不要分享**（保持「限制」），只分享個別檔案（下面擴充功能會做）。

## 擴充功能：每個商品做這幾步

### A. 取得下載連結（Google Drive）
1. 在 `Polyglot Pages – product files` 資料夾找到這款的 zip（檔名照 `sales/今天上架總表.md`）。
2. 右鍵 → **共用** → 「一般存取權」改成 **知道連結的任何人**，角色 **檢視者** → 複製連結 → 完成。
3. **不要**分享整個資料夾，**不要**改其他檔案的權限。

### B. 放到 Gumroad 的 Content 頁
1. 打開商品編輯頁 → **Content**，確認是「Use the same content for all versions」。
2. 如果之前有上傳過 zip 檔案，保留不要刪。
3. 在最上面加入下面這段文字，把 `<連結>` 換成剛複製的 Drive 連結；有「按鈕（Button）」功能就把下載那行做成按鈕，沒有就做成文字連結：

```
⬇️ Download your template: <連結>

How to start: unzip the file and open START-HERE.html. Every language version (English, 繁體中文, 简体中文, 日本語) is inside, with a step-by-step guide.

──────────
⬇️ 下載模板：<連結>
解壓縮後先打開 START-HERE.html，裡面有各語言版本和一步一步的說明。
```

4. 儲存。

### C. 縮圖
Thumbnail **不用放**，跳過。

### D. 檢查
- 用無痕視窗打開那個 Drive 連結，確認**不用登入就能下載**。
- 回報：款式、zip 檔名、Drive 連結是否可下載、Content 是否已儲存。**連結不要貼到 GitHub 或任何公開地方。**

## 規則
- 只動這次要處理的商品和檔案。
- 不要刪除任何 Drive 檔案、不要改帳號設定。
- 遇到登入驗證就停下來問使用者。
