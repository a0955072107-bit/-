# 外部 skill 來源（使用者 2026-11-25 同意放入）

| 資料夾 | 來源 | 版本 | 授權 |
|---|---|---|---|
| `frontend-design/` | https://github.com/anthropics/skills/tree/main/skills/frontend-design | commit e4bb5d9（2026-11-16） | Apache-2.0（見資料夾內 LICENSE.txt） |
| `web-design-guidelines/` | https://github.com/vercel-labs/agent-skills/tree/main/skills/web-design-guidelines | commit 5a37a63（2026-11-20） | MIT（vercel-labs/agent-skills README） |

兩者都只有 Markdown 說明文件，沒有可執行程式。內容原樣複製、未修改。
本專案的設計標準以 `templates/DESIGN.md` 為準；這兩個 skill 是參考依據。
web-design-guidelines 有些規則是針對 React／Next.js（hydration、useState 等），純 HTML 模板可略過。
