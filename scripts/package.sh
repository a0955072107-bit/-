#!/usr/bin/env bash
# 把每個模板打包成可上架販售的 zip，輸出到 dist/
#   用法：bash scripts/package.sh
set -euo pipefail
export LC_ALL=C.UTF-8   # 讓 zip 標記 UTF-8 檔名，Windows／Mac 解壓縮中文檔名不會亂碼
cd "$(dirname "$0")/.."

OUT=dist
rm -rf "$OUT" && mkdir -p "$OUT/build"

# slug:商品資料夾名稱
SLUGS=(
  "restaurant:restaurant-template"
  "beauty:beauty-salon-template"
  "fitness:fitness-studio-template"
  "clinic:clinic-template"
  "consulting:consulting-firm-template"
  "studio:design-studio-template"
)

for entry in "${SLUGS[@]}"; do
  slug="${entry%%:*}"; name="${entry#*:}"
  src="templates/$slug/index.html"
  [ "$slug" = studio ] && src="index.html"   # 設計工作室版本就是根目錄的 Lumen Studio
  [ -f "$src" ] || { echo "略過 $slug（找不到 $src）"; continue; }

  dir="$OUT/build/$name"
  mkdir -p "$dir/images"
  cp "$src" "$dir/index.html"
  cp templates/_docs/使用說明.md templates/_docs/授權條款.md "$dir/"
  echo "把你的照片放在這個資料夾，使用方式請看「使用說明.md」第 5 節。" > "$dir/images/README.txt"
  (cd "$OUT/build" && zip -qr "../$name.zip" "$name")
  echo "✓ $OUT/$name.zip"
done

# 全套組合包
(cd "$OUT/build" && zip -qr "../all-templates-bundle.zip" .)
echo "✓ $OUT/all-templates-bundle.zip"
rm -rf "$OUT/build"
