# 行業網站模板集

| 路徑 | 內容 |
|---|---|
| `site/` | Polyglot Pages 官網（GitHub Pages 根目錄）：`index.html` 英文、`zh-TW/`、`zh-CN/`（`python3 scripts/make-home-zh-cn.py` 從繁體產生）、`img/` 範例截圖 |
| `archive/lumen-studio/` | 舊的 Lumen Studio 虛構示範頁（2026-11-08 建立，已不在網站上，只留存） |
| `templates/` | 中文展示頁 + 30 款模板（繁體中文）；`templates/en/` 是英文展示頁與英文版 |
| `templates/_docs/` | 隨商品附上的使用說明、授權條款 |
| `templates/SPEC.md` | 模板製作規格（新增模板時遵循） |
| `scripts/package.sh` | 打包成可販售的 zip → `dist/` |
| `sales/Gumroad上架步驟.md` | Gumroad 每個欄位要填什麼（中英） |
| `sales/行銷計畫.md` | 國外需求、定價、推廣、接案管道 |
| `sales/covers/en/` | 英文封面與正方形縮圖（`node scripts/covers/make.js` 產生） |
| `sales/上架文案.md` | 早期總覽與其他平台建議 |

```bash
bash scripts/package.sh   # 產生 dist/*.zip
```

---

# 官網與部署

GitHub Pages 由 `.github/workflows/pages.yml` 在推送到 `main` 時執行 `bash scripts/build-site.sh`，把 `_site/` 部署到
`https://a0955072107-bit.github.io/-/`。網站根目錄是 Polyglot Pages 官網（`site/`），模板展示在 `/templates/`。

- 改官網：英文改 `site/index.html`，繁體改 `site/zh-TW/index.html`，再跑 `python3 scripts/make-home-zh-cn.py` 產生簡體版。
- 檢查：`bash scripts/lint-all.sh`（包含官網三頁）。
- 原本放在根目錄的 Lumen Studio 示範頁移到 `archive/lumen-studio/index.html`，不會被建置。
