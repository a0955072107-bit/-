# Hallmark（部分收錄，內部工具）

來源：https://github.com/Nutlope/hallmark ，commit 04977e1（2026-11-11），MIT 授權（見 LICENSE）。
使用者 2026-11-25 同意以「lint＋參考文件」方式收錄。內容原樣複製、未修改。

## 收錄了什麼
- `skills/hallmark/scripts/sloplint.mjs`：防 AI 感 lint。只讀檔、不連網；執行時會在當前資料夾寫 `.hallmark/before.json` 快取（已加入 .gitignore）。
  `bash scripts/lint-all.sh` 預設就用這一支。
- `skills/hallmark/SKILL.md`、`references/**/*.md`、`references/themes/index.json`：設計參考文件（規則、版面、主題說明）。

## 刻意沒收錄
- `imagegen.mjs`（呼叫 Together AI 付費 API）、`theme.mjs`（從 Wikimedia 下載照片）、`install*.mjs`（改 Claude 設定）、`capture.mjs`／`picture.mjs`／`sloplint-render.mjs`（開瀏覽器、執行外部指令）、`photos.json`（照片清單）、50 張主題範例圖。
- 因此不支援 `--render` 參數；截圖檢查改用 `templates/DESIGN.md` 第 4 節的 Playwright 流程。

## 為什麼不放進 .claude/skills/
Hallmark 的完整流程（發主題、放圖庫照片、先問四個問題）和本專案的 `templates/SPEC.md`（不用照片、固定主題變數區）衝突。放在這裡只當工具與參考，不會自動載入；SPEC 與 DESIGN.md 優先。
