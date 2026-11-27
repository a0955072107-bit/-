#!/usr/bin/env bash
# Hallmark 檢查：對所有模板頁面（所有語言、Motion、Luxe）與官網 site/ 跑 sloplint，彙整 FAIL。
# 規格允許忽略：#20（Hallmark 戳記）、#19 的時間或數字範圍。
# 用法：bash scripts/lint-all.sh [hallmark 目錄]
set -uo pipefail
cd "$(dirname "$0")/.."
HM="${1:-${HALLMARK_DIR:-tools/hallmark}}"
[ -d "$HM" ] || HM=/home/user/nutlope/hallmark
LINT="$(cd "$HM" 2>/dev/null && pwd)/skills/hallmark/scripts/sloplint.mjs"
[ -f "$LINT" ] || { echo "找不到 Hallmark（預設 tools/hallmark）；或 git clone --depth 1 https://github.com/Nutlope/hallmark 後用參數指定路徑"; exit 1; }
TMP=$(mktemp -d); trap 'rm -rf "$TMP"' EXIT
total=0; bad=0
while IFS= read -r f; do
  rel=${f#templates/}; d="$TMP/${rel%/index.html}"; mkdir -p "$d"; cp "$f" "$d/index.html"
  raw=$(cd "$TMP" && node "$LINT" "${rel%/index.html}/index.html" 2>&1)
  if ! echo "$raw" | grep -q '^sloplint:'; then echo "✗ $rel：Hallmark 執行失敗"; echo "$raw" | head -3 | sed 's/^/    /'; bad=$((bad+1)); total=$((total+1)); continue; fi
  out=$(echo "$raw" | grep -E '^\s+FAIL' | grep -vE 'FAIL 20 ' | grep -vE 'FAIL 19 .*"–"')
  total=$((total+1))
  if [ -n "$out" ]; then bad=$((bad+1)); echo "✗ $rel"; echo "$out" | sed 's/^/    /'; fi
done < <({ find templates -name index.html -not -path 'templates/_docs/*' -not -path 'templates/index.html' -not -path 'templates/en/index.html'; find site -name index.html; } | sort)
echo "Hallmark：檢查 $total 頁，$bad 頁有需要處理的 FAIL"
