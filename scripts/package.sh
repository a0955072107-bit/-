#!/usr/bin/env bash
# 把每個模板打包成可上架販售的雙語 zip（英文 + 繁體中文），輸出到 dist/
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
  zh="templates/$slug/index.html"
  en="templates/en/$slug/index.html"
  [ -f "$zh" ] || { echo "略過 $slug（找不到 $zh）"; continue; }
  [ -f "$en" ] || echo "注意：$slug 沒有英文版（找不到 $en），只打包中文版"

  dir="$OUT/build/$name"
  mkdir -p "$dir/zh-TW/images"
  cp "$zh" "$dir/zh-TW/index.html"
  echo "把你的照片放在這個資料夾，使用方式請看「使用說明.md」第 5 節。" > "$dir/zh-TW/images/README.txt"
  if [ -f "$en" ]; then
    mkdir -p "$dir/en/images"
    cp "$en" "$dir/en/index.html"
    echo "Put your photos in this folder. See GUIDE.md, section 5." > "$dir/en/images/README.txt"
  fi
  cp templates/_docs/使用說明.md templates/_docs/授權條款.md "$dir/"
  cp templates/_docs/en/GUIDE.md templates/_docs/en/LICENSE.md "$dir/"
  (cd "$OUT/build" && zip -qr "../$name.zip" "$name")
  echo "✓ $OUT/$name.zip"
done

# 全套組合包
(cd "$OUT/build" && zip -qr "../all-templates-bundle.zip" .)
echo "✓ $OUT/all-templates-bundle.zip"
rm -rf "$OUT/build"
