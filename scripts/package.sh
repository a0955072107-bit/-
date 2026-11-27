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
  "bnb:bnb-guesthouse-template"
  "realestate:real-estate-template"
  "wedding:wedding-event-template"
  "photographer:photographer-portfolio-template"
  "pet:pet-grooming-template"
  "education:tutoring-school-template"
  "interior:interior-design-template"
  "bakery:bakery-dessert-template"
  "tea:bubble-tea-shop-template"
  "auto:auto-care-garage-template"
  "cleaning:home-cleaning-template"
  "florist:florist-template"
  "yoga:yoga-pilates-template"
  "camping:campsite-glamping-template"
  "freelancer:freelancer-portfolio-template"
  "saas:app-saas-landing-template"
  "coach:therapist-coach-template"
  "contractor:contractor-handyman-template"
  "nonprofit:nonprofit-charity-template"
  "linkinbio:link-in-bio-template"
  "barber:barbershop-template"
  "conference:conference-event-template"
  "tattoo:tattoo-studio-template"
  "coworking:coworking-space-template"
  "dental:dental-clinic-forest-template"
  "motion/saas:motion-saas-launch-template"
  "motion/portfolio:motion-creative-portfolio-template"
  "motion/restaurant:motion-fine-dining-template"
  "motion/wedding:motion-wedding-template"
  "motion/realestate:motion-luxury-residences-template"
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
  cn="templates/zh-CN/$slug/index.html"
  if [ -f "$cn" ]; then
    mkdir -p "$dir/zh-CN/images"
    cp "$cn" "$dir/zh-CN/index.html"
    echo "把你的照片放在这个文件夹，使用方法请看「使用說明.md」第 5 节。" > "$dir/zh-CN/images/README.txt"
  fi
  for extra in ja es; do
    xf="templates/$extra/$slug/index.html"
    if [ -f "$xf" ]; then
      mkdir -p "$dir/$extra/images"
      cp "$xf" "$dir/$extra/index.html"
      case $extra in
        ja) echo "写真はこのフォルダに入れてください。GUIDE.md の第 5 章をご覧ください。" > "$dir/$extra/images/README.txt" ;;
        es) echo "Pon tus fotos en esta carpeta. Consulta GUIDE.md, sección 5." > "$dir/$extra/images/README.txt" ;;
      esac
    fi
  done
  python3 scripts/lang-index.py "$dir"
  if [ -f "$en" ]; then
    mkdir -p "$dir/en/images"
    cp "$en" "$dir/en/index.html"
    echo "Put your photos in this folder. See GUIDE.md, section 5." > "$dir/en/images/README.txt"
  fi
  cp templates/_docs/使用說明.md templates/_docs/授權條款.md templates/_docs/隱私權政策範本.md "$dir/"
  cp templates/_docs/en/GUIDE.md templates/_docs/en/LICENSE.md templates/_docs/en/PRIVACY-TEMPLATE.md "$dir/"
  cp templates/_docs/START-HERE.html "$dir/"
  for extra in ja es; do
    [ -d "$dir/$extra" ] && [ -d "templates/_docs/$extra" ] && cp templates/_docs/$extra/*.md "$dir/"
  done
  (cd "$OUT/build" && zip -qr "../$name.zip" "$name")
  echo "✓ $OUT/$name.zip"
done

# 組合包：標準款全套、Motion 全套分開
(cd "$OUT/build" && zip -qr "../all-templates-bundle.zip" . -x 'motion-*')
echo "✓ $OUT/all-templates-bundle.zip"
(cd "$OUT/build" && zip -qr "../motion-bundle.zip" motion-*)
echo "✓ $OUT/motion-bundle.zip"
rm -rf "$OUT/build"
