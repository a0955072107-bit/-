# Gumroad 上架步驟（照著複製貼上）

> 這份文件每個欄位要填什麼都寫好了，照順序做就能上架。
> 商品說明採用「英文在前、中文在後」的雙語寫法，國際和台灣買家都看得懂。
> 價格、方案都是建議，可以自己調整。
> Gumroad 介面偶爾會改版，欄位名稱以後台實際顯示為準。

---

## 0. 上架前準備（只做一次）

### 0-1. 開啟線上 Demo
1. 把 GitHub 分支 `ccr-df8b4ac9-ey0al4` 合併到 `main`。
2. repo 的 **Settings → Pages → Source** 選 **GitHub Actions**。
3. 幾分鐘後，Demo 網址如下（每個商品都要放）：

| 模板 | 英文 Demo | 中文 Demo（簡體版把 zh-TW 換成 zh-CN） |
|---|---|---|
| 餐廳 | `https://a0955072107-bit.github.io/-/templates/restaurant/en/` | `https://a0955072107-bit.github.io/-/templates/restaurant/zh-TW/` |
| 美容 | `…/templates/beauty/en/` | `…/templates/beauty/zh-TW/` |
| 健身 | `…/templates/fitness/en/` | `…/templates/fitness/zh-TW/` |
| 診所 | `…/templates/clinic/en/` | `…/templates/clinic/zh-TW/` |
| 事務所 | `…/templates/consulting/en/` | `…/templates/consulting/zh-TW/` |
| 工作室 | `…/templates/studio/en/` | `…/templates/studio/zh-TW/` |
| 民宿 | `…/templates/bnb/en/` | `…/templates/bnb/zh-TW/` |
| 房仲 | `…/templates/realestate/en/` | `…/templates/realestate/zh-TW/` |
| 婚禮 | `…/templates/wedding/en/` | `…/templates/wedding/zh-TW/` |
| 攝影師 | `…/templates/photographer/en/` | `…/templates/photographer/zh-TW/` |
| 寵物 | `…/templates/pet/en/` | `…/templates/pet/zh-TW/` |
| 補習班 | `…/templates/education/en/` | `…/templates/education/zh-TW/` |
| 室內設計 | `…/templates/interior/en/` | `…/templates/interior/zh-TW/` |
| 烘焙 | `…/templates/bakery/en/` | `…/templates/bakery/zh-TW/` |
| 手搖飲 | `…/templates/tea/en/` | `…/templates/tea/zh-TW/` |
| 汽車 | `…/templates/auto/en/` | `…/templates/auto/zh-TW/` |
| 清潔 | `…/templates/cleaning/en/` | `…/templates/cleaning/zh-TW/` |
| 花店 | `…/templates/florist/en/` | `…/templates/florist/zh-TW/` |
| 瑜珈 | `…/templates/yoga/en/` | `…/templates/yoga/zh-TW/` |
| 露營 | `…/templates/camping/en/` | `…/templates/camping/zh-TW/` |
| 個人品牌 | `…/templates/freelancer/en/` | `…/templates/freelancer/zh-TW/` |
| App／SaaS | `…/templates/saas/en/` | `…/templates/saas/zh-TW/` |
| 諮商／教練 | `…/templates/coach/en/` | `…/templates/coach/zh-TW/` |
| 水電修繕 | `…/templates/contractor/en/` | `…/templates/contractor/zh-TW/` |
| 非營利 | `…/templates/nonprofit/en/` | `…/templates/nonprofit/zh-TW/` |
| Link-in-bio | `…/templates/linkinbio/en/` | `…/templates/linkinbio/zh-TW/` |
| 理髮廳 | `…/templates/barber/en/` | `…/templates/barber/zh-TW/` |
| 研討會 | `…/templates/conference/en/` | `…/templates/conference/zh-TW/` |
| 刺青 | `…/templates/tattoo/en/` | `…/templates/tattoo/zh-TW/` |
| 共享辦公 | `…/templates/coworking/en/` | `…/templates/coworking/zh-TW/` |
| 牙醫・森林診間（11/27 新增） | `…/templates/dental/en/` | `…/templates/dental/zh-TW/`（日文 `…/templates/dental/ja/`） |
| 中醫／針灸（11/28 新增） | `…/templates/tcm/en/` | `…/templates/tcm/zh-TW/`（日文 `…/templates/tcm/ja/`） |
| 粵菜館（11/28 新增） | `…/templates/canton/en/` | `…/templates/canton/zh-TW/`（日文 `…/templates/canton/ja/`） |
| 髮型沙龍（11/28 新增） | `…/templates/hair/en/` | `…/templates/hair/zh-TW/`（日文 `…/templates/hair/ja/`） |
| 補習班・年級選擇器（11/28 新增） | `…/templates/tutor/en/` | `…/templates/tutor/zh-TW/`（日文 `…/templates/tutor/ja/`） |

上架前每個連結都打開確認一次。

### 0-2. 商店設定（Settings → Profile）
- **Name**：取一個品牌名，例如 `Hearth Templates` 或你自己的工作室名稱。
- **Bio**（直接貼上）：
  ```
  Clean, fast one-page website templates for small businesses. Pure HTML, no monthly fees, English + 繁體 + 简体 included. Need it customised? We can build it for you.
  給小店家的一頁式網站模板，純 HTML、免月費、附中英文版。需要客製？我們幫你做好。
  ```
- **頭像**：用 Canva 做一個簡單的 logo。
- **Payouts**：設定收款方式，台灣通常用 PayPal 或銀行帳戶，依後台可用選項為準。

### 0-3. 打包檔案
```bash
bash scripts/package.sh
```
`dist/` 會產生 35 個標準款單款 zip（原本 30 款＋dental＋11/28 的 tcm、canton、hair、tutor）、5 個 Motion 單款 zip、1 個全套 zip（`all-templates-bundle.zip`，35 款）和 1 個 Motion 全套 zip；每包都附英文、繁體、簡體、日文版。

---

## 封面

- 英文封面和正方形縮圖：`sales/covers/en/`，每款各有 `<slug>-cover.png`（1920×1080）與 `<slug>-thumb.png`（1000×1000）。
- 新增模板後重新產生封面：先在 `scripts/covers/data.json` 加一筆資料，再執行 `node scripts/covers/make.js <slug>`。
- 中文封面（Canva 製作，前 5 款）：`sales/covers/*.png`。

## 1. 上架順序

1. 先上 **網站客製服務**。其他商品的說明會連到它，所以先上才拿得到網址。
2. 再上 30 款單一模板（建議先上最有把握的 6 款，其他陸續上，讓商店持續有新品）。
3. 最後上 **全套組合包**（Bundle）。

---

## 2. 共用文字（每個模板商品都貼在說明最後）

```
──────────
✨ Want it set up for your business?
Don't have time to edit it yourself? We'll customise this template with your text, photos, colours, booking links and domain, ready to launch.
👉 See our Website Customization Service: https://polyglotpages.gumroad.com/l/website-customization

✨ 想要直接幫你改好？
沒時間自己改嗎？我們可以把這個模板改成你店家專屬的網站：換上你的文字、照片、品牌色、預約連結，並設定好網域，直接上線。
👉 網站客製服務：https://polyglotpages.gumroad.com/l/website-customization

Questions or custom work? / 有問題或想客製： polyglotpages.studio@gmail.com
```

> **聯絡方式的原則**：只放品牌 Email，不放個人 LINE 或電話。請另外申請一個品牌專用信箱。
> Etsy 目前不支援台灣賣家收款，所以不上 Etsy，全部集中在 Gumroad。

---

## 3. 網站客製服務（先上這個）

> **11/23 更新：Commission 類型要帳號滿 30 天才能用。** 在那之前改用「訂金＋尾款」兩個 Digital product：
> - 三語店家網站代製（訂金）：URL `trilingual-website-service`，Standard deposit $150／Pro deposit $250（11/27 從 $275 改，合計 $499）
> - 網站客製服務（訂金）：URL `website-customization`，Basic deposit $125／Plus deposit $225
> - 網站尾款（Unlisted 不公開）：URL `final-payment`，Trilingual Standard $149／Pro $249（11/27 從 $274 改）／Customization Basic $124／Plus $224。網站做好、客人確認後才寄這個連結。
> 目前用「訂金＋尾款」兩個 Digital product（見第 3 節開頭）；手上有進行中的案子時不要換成 Commission。
> **Content 頁（買家付款後看到的頁面）不能空白。** 訂金商品貼：
> 「Thank you! Your deposit is confirmed. What happens next: 1. Within 1 business day we'll email you a short form… 2. Your site is ready for review within 7 days… 3. You only pay the remaining 50% after you've approved your finished site.」（中英對照全文見 `sales/交付流程.md` 第六節）
> **尾款商品先不發布**，第一個客人確認網站時才發布並寄連結。



| 欄位 | 填入 |
|---|---|
| 商品類型 | **Commission**（委託）：買家下單時先付 **50% 訂金**，網站做好、買家確認後，Gumroad 再向買家收剩下 50%。後台沒有 Commission 類型時才用一般 Digital product |
| Name | `Website Customization Service — We Build Your Business Site 網站客製服務` |
| URL | `website-customization` |
| Price | `249`（Basic），另外用 **Versions** 加 `Plus $449`（模板代改，和三語代製是不同商品） |
| Cover | 可以先沿用任一張模板封面，之後再用 Canva 另做一張 |
| Summary（You'll get） | `A ready-to-launch website for your business, built from one of our templates.` |

**Versions（方案）**

| 名稱 | 價格 | 說明 |
|---|---|---|
| Basic | $249 | Your text, photos, colours, contact/booking links and form set up; published on a free host. 1 revision round. |
| Plus | $449 | Everything in Basic, plus custom domain setup, one extra page or section, and 2 revision rounds. |

**Description**
```
Love one of our templates but don't have time to set it up? We'll do it for you.

How it works
1. Buy the service and pick any of our templates.
2. We email you a short form: business name, text, photos, colours, links.
3. We build and publish your site, usually within 5 business days after we receive your content.
4. You review it and request changes (1 round on Basic, 2 on Plus).

What's included
- Your content, photos and brand colours
- Phone, WhatsApp/LINE, map and booking buttons connected
- Contact form connected to your email
- Published on a free host (Netlify / GitHub Pages)
- Plus: custom domain connected, one extra section or page

Payment: 50% when you order, 50% after you've seen and approved your site. If we can't deliver, the deposit is refunded in full.

Not included: copywriting from scratch, photography, domain purchase fees.

Questions before buying? Email polyglotpages.studio@gmail.com

──────────
網站客製服務：喜歡我們的模板，但沒時間自己改？交給我們。

流程
1. 購買服務，並選擇任一款模板。
2. 我們會寄一份簡短表單給你，請你填寫店名、文字、照片、品牌色、連結。
3. 收到資料後，通常 5 個工作天內完成並上線。
4. 你確認後可以提出修改（Basic 1 次、Plus 2 次）。

包含：換上你的內容、照片、品牌色；電話、LINE、地圖、預約按鈕串接；表單串接到你的 Email；部署到免費主機。Plus 方案另外包含自訂網域設定，以及多做一個區塊或頁面。
不包含：從零撰寫文案、拍攝照片、網域購買費用。

購買前有問題，歡迎寫信到 polyglotpages.studio@gmail.com
```

**Receipt（購買後訊息）**
```
Thanks! We'll email you within 1 business day with a short form to collect your content.
感謝購買！我們會在 1 個工作天內寄表單給你，用來收集網站內容。
```

> 交件時間和價格請依你實際能接的量調整。初期可以先低價接幾單，累積作品和評價。

---

## 4. 單一模板（35 款：原本 30 款＋4-31～4-35）

每款的共用設定：

| 欄位 | 填入 |
|---|---|
| Price | `39`（上市前 2 週用折扣碼降到 $29） |
| Versions | `Standard license — 1 website`（$39）、`Extended license — up to 10 websites`（$119） |
| Content | 上傳 `dist/` 裡對應的 zip |
| Thumbnail | `sales/covers/en/<slug>-thumb.png`（1000×1000） |
| Additional details | `Format: HTML/CSS/JS` · `Languages: English, 繁體中文, 简体中文 (switchable)` · `Pages: 1 (one-page)` · `Builder needed: None` |
| Receipt | 見下方共用 Receipt |
| Tags | 見各商品 |

**共用 Receipt**
```
Thanks for your purchase! Unzip the file and double-click START-HERE.html to get started (full guides: GUIDE.md / 使用說明.md).
Want us to set it up for you? See our Website Customization Service.
感謝購買！解壓縮後雙擊 START-HERE.html 就能開始（完整教學：使用說明.md）。需要我們幫你改好嗎？歡迎參考「網站客製服務」。
```

**共用 Summary（You'll get）**
```
A one-page HTML website template in English + 繁體 + 简体, a step-by-step setup guide, and a commercial licence.
```

### 4-1. 餐廳／咖啡廳

- **Name**：`Restaurant & Café Website Template (English + 繁體 + 简体) — One-Page HTML`
- **URL**：`restaurant-website-template`
- **Cover**：`sales/covers/en/restaurant-cover.png`（英文）；台灣平台可用 `sales/covers/restaurant-cover.png`（中文）
- **Tags**：`restaurant website`, `cafe website`, `html template`, `small business`, `website template`
- **Description**：
```
A warm, appetizing one-page website for restaurants, cafés and bistros. Pure HTML, so there's no WordPress, no monthly fees and no coding required.

🔗 Live demo (English): [英文 Demo 網址]
🔗 Live demo (中文): [中文 Demo 網址]

Features
- Tabbed menu with prices and tags (Signature, Vegetarian)
- Live "Open now / Closed" badge based on your opening hours
- Reservation form (works with free Formspree)
- Call, WhatsApp/LINE and Google Maps buttons, plus a sticky mobile "Book a table" button
- Gallery, reviews, hours and location sections
- SEO-ready with schema.org Restaurant data
- Change the whole colour scheme from one place

What you get
- English, Traditional Chinese and Simplified Chinese versions with a built-in language switcher
- Step-by-step guide: edit text, add photos, connect the form, publish for free
- Commercial licence (1 website with Standard)

──────────
餐廳／咖啡廳一頁式網站模板，純 HTML，免 WordPress、免月費，不用會寫程式。

功能：分頁菜單（價格、招牌、素食標籤）、依營業時間自動顯示「營業中／休息中」、線上訂位表單、電話／LINE／地圖按鈕、手機版底部「立即訂位」按鈕、環境照片、顧客好評、營業時間與交通資訊、Google 結構化資料、一處改色全站換色。
內容：英文版與繁體中文版、中文使用教學、商業授權。

[貼上「共用文字」]
```

### 4-2. 美容美髮／美甲

- **Name**：`Hair & Nail Salon Website Template (English + 繁體 + 简体) — One-Page HTML`
- **URL**：`salon-website-template`
- **Cover**：`sales/covers/en/beauty-cover.png`（英文）；台灣平台可用 `sales/covers/beauty-cover.png`（中文）
- **Tags**：`salon website`, `beauty website`, `nail salon`, `html template`, `website template`
- **Description**：
```
A soft, elegant one-page website for hair salons, nail studios and beauty bars. Pure HTML, so there's no WordPress, no monthly fees and no coding required.

🔗 Live demo (English): [英文 Demo 網址]
🔗 Live demo (中文): [中文 Demo 網址]

Features
- Service price list with categories (cut, colour, perm, treatment, nails)
- Stylist profiles with "Book with me" links
- Filterable portfolio gallery
- 4-step booking guide and FAQ accordion
- WhatsApp/LINE booking button, plus a sticky mobile booking bar
- SEO-ready with schema.org BeautySalon data
- Change the whole colour scheme from one place

What you get
- English, Traditional Chinese and Simplified Chinese versions with a built-in language switcher
- Step-by-step guide and commercial licence

──────────
美容美髮／美甲一頁式網站模板。功能：分類價目表、設計師介紹與指定預約、可篩選作品集、預約流程、常見問題、LINE 預約按鈕、手機版底部預約列、Google 結構化資料。附英文、繁體、簡體三種語言（網站內建語言切換）、中文教學、商業授權。

[貼上「共用文字」]
```

### 4-3. 健身房／私人教練

- **Name**：`Gym & Personal Training Website Template (English + 繁體 + 简体) — One-Page HTML`
- **URL**：`gym-website-template`
- **Cover**：`sales/covers/en/fitness-cover.png`（英文）；台灣平台可用 `sales/covers/fitness-cover.png`（中文）
- **Tags**：`gym website`, `fitness website`, `personal trainer`, `html template`, `website template`
- **Description**：
```
A bold, high-energy one-page website for gyms, boxing clubs, yoga and personal training studios. Pure HTML, so there's no WordPress, no monthly fees and no coding required.

🔗 Live demo (English): [英文 Demo 網址]
🔗 Live demo (中文): [中文 Demo 網址]

Features
- Class cards with level and duration
- Colour-coded weekly timetable (scrolls neatly on mobile)
- Coach profiles with certifications
- Pricing plans with a monthly / yearly toggle
- Member results and a free-trial sign-up form
- Sticky mobile "Book a free trial" button
- SEO-ready with schema.org ExerciseGym data

What you get
- English, Traditional Chinese and Simplified Chinese versions with a built-in language switcher
- Step-by-step guide and commercial licence

──────────
健身工作室一頁式網站模板。功能：課程介紹、彩色每週課表、教練團隊、月繳／年繳切換方案價格、學員見證、免費體驗表單、手機版底部預約按鈕、Google 結構化資料。附英文、繁體、簡體三種語言（網站內建語言切換）、中文教學、商業授權。

[貼上「共用文字」]
```

### 4-4. 診所（牙醫，可改其他科別）

- **Name**：`Dental & Medical Clinic Website Template (English + 繁體 + 简体) — One-Page HTML`
- **URL**：`clinic-website-template`
- **Cover**：`sales/covers/en/clinic-cover.png`（英文）；台灣平台可用 `sales/covers/clinic-cover.png`（中文）
- **Tags**：`dental website`, `clinic website`, `medical website`, `html template`, `website template`
- **Description**：
```
A calm, trustworthy one-page website for dental clinics, easily adapted to physiotherapy, dermatology or general practice. Pure HTML, so there's no WordPress, no monthly fees and no coding required.

🔗 Live demo (English): [英文 Demo 網址]
🔗 Live demo (中文): [中文 Demo 網址]

Features
- "Today's hours" card generated from your weekly schedule
- Weekly clinic schedule with today's column highlighted
- Treatment cards with icons, doctor profiles
- First-visit checklist and FAQ accordion
- Call and Book buttons fixed to the bottom on mobile
- Modest, factual sample copy (please follow your local healthcare advertising rules)
- SEO-ready with schema.org Dentist data

What you get
- English, Traditional Chinese and Simplified Chinese versions with a built-in language switcher
- Step-by-step guide and commercial licence

──────────
診所一頁式網站模板（牙醫，可改其他科別）。功能：首屏自動顯示今日門診、門診時間表自動標示今天、診療項目、醫師團隊、就診須知與常見問題、手機版底部「撥打電話／線上預約」。文案遵守醫療廣告法、不誇大。附英文、繁體、簡體三種語言（網站內建語言切換）、中文教學、商業授權。

[貼上「共用文字」]
```

### 4-5. 會計師／律師／顧問事務所

- **Name**：`Law, Accounting & Consulting Firm Website Template (English + 繁體 + 简体)`
- **URL**：`consulting-firm-website-template`
- **Cover**：`sales/covers/en/consulting-cover.png`（英文）；台灣平台可用 `sales/covers/consulting-cover.png`（中文）
- **Tags**：`law firm website`, `accounting website`, `consulting website`, `html template`, `website template`
- **Description**：
```
An authoritative, premium one-page website for accountants, law firms and consultancies. Pure HTML, so there's no WordPress, no monthly fees and no coding required.

🔗 Live demo (English): [英文 Demo 網址]
🔗 Live demo (中文): [中文 Demo 網址]

Features
- Practice areas, "Why us" and a 4-step process timeline
- Partner profiles and client testimonials
- FAQ accordion
- Consultation request form with service selector and privacy consent
- Animated stat counters, sticky mobile "Book a consultation" button
- SEO-ready with schema.org ProfessionalService data

What you get
- English, Traditional Chinese and Simplified Chinese versions with a built-in language switcher
- Step-by-step guide and commercial licence

──────────
會計師／律師／顧問事務所一頁式網站模板。功能：服務領域、選擇我們的理由、服務流程、專業團隊、客戶見證、常見問題、預約諮詢表單、數字動畫、手機版底部預約按鈕、Google 結構化資料。附英文、繁體、簡體三種語言（網站內建語言切換）、中文教學、商業授權。

[貼上「共用文字」]
```

### 4-6. 設計工作室／作品集

- **Name**：`Design Studio & Portfolio Website Template (English + 繁體 + 简体)`
- **URL**：`studio-portfolio-template`
- **Cover**：`sales/covers/en/studio-cover.png`
- **Tags**：`portfolio website`, `design studio`, `agency website`, `html template`, `website template`
- **Description**：
```
A quiet, editorial one-page website for design studios, freelancers and creative agencies. Pure HTML, so there's no WordPress, no monthly fees and no coding required.

🔗 Live demo (English): [英文 Demo 網址]
🔗 Live demo (中文): [中文 Demo 網址]

Features
- Line-by-line hero reveal and smooth scroll animations
- Services, selected work and studio stats
- Project enquiry form with budget selector
- Automatic dark mode, paper-grain texture
- SEO-ready with schema.org data

What you get
- English, Traditional Chinese and Simplified Chinese versions with a built-in language switcher
- Step-by-step guide and commercial licence

──────────
設計工作室／作品集一頁式網站模板。功能：標題逐行浮現、捲動動畫、服務項目、精選作品、專案洽詢表單、自動深色模式。附英文、繁體、簡體三種語言（網站內建語言切換）、中文教學、商業授權。

[貼上「共用文字」]
```

### 4-7. 民宿／B&B

- **Name**：`B&B & Guesthouse Website Template (English + 繁體 + 简体) — One-Page HTML`
- **URL**：`bnb-guesthouse-template`
- **Cover**：`sales/covers/en/<slug>-cover.png`
- **Tags**：`bnb website`, `guesthouse website`, `hotel website`, `html template`, `website template`
- **Description**：
```
A calm, slow-travel one-page website for B&Bs, guesthouses and small inns. Pure HTML, so there's no WordPress, no monthly fees and no coding required.

🔗 Live demo (English): [英文 Demo 網址]
🔗 Live demo (中文): [中文 Demo 網址]

Features
- Room cards with capacity, size, weekday and weekend rates
- Booking form that counts nights from your dates
- Amenities, nearby attractions with travel times
- House rules and cancellation policy accordion
- Sticky mobile "Book your stay" button
- SEO-ready with schema.org LodgingBusiness data

What you get
- English, Traditional Chinese and Simplified Chinese versions with a built-in language switcher
- Step-by-step guide and commercial licence

──────────
民宿／B&B 一頁式網站模板。功能：房型與平假日價格、自動計算住宿晚數的訂房表單、住宿特色、周邊景點、入住須知、住客評價、手機版底部訂房按鈕、Google 結構化資料。附英文、繁體、簡體三種語言（網站內建語言切換）、中文教學、商業授權。

[貼上「共用文字」]
```

### 4-8. 房仲／不動產

- **Name**：`Real Estate Agent Website Template (English + 繁體 + 简体) — One-Page HTML`
- **URL**：`real-estate-website-template`
- **Cover**：`sales/covers/en/<slug>-cover.png`
- **Tags**：`real estate website`, `realtor website`, `property listings`, `html template`, `website template`
- **Description**：
```
A crisp, confident one-page website for independent agents and small agencies. Pure HTML, so there's no WordPress, no monthly fees and no coding required.

🔗 Live demo (English): [英文 Demo 網址]
🔗 Live demo (中文): [中文 Demo 網址]

Features
- Property search bar that filters listings instantly
- Listing cards with price, size, rooms and tags
- Services, track record and agent profile
- 5-step buying process and client reviews
- Viewing / listing request form
- SEO-ready with schema.org RealEstateAgent data

What you get
- English, Traditional Chinese and Simplified Chinese versions with a built-in language switcher
- Step-by-step guide and commercial licence

──────────
房仲／不動產一頁式網站模板。功能：可即時篩選的物件搜尋、物件卡片、服務項目、成交實績、經紀人介紹、買房流程、預約看屋表單、手機版底部預約按鈕、Google 結構化資料。附英文、繁體、簡體三種語言（網站內建語言切換）、中文教學、商業授權。

[貼上「共用文字」]
```

### 4-9. 婚禮／活動

- **Name**：`Wedding Website Template with RSVP & Countdown (English + 繁體 + 简体)`
- **URL**：`wedding-website-template`
- **Cover**：`sales/covers/en/<slug>-cover.png`
- **Tags**：`wedding website`, `rsvp website`, `event website`, `wedding invitation`, `html template`
- **Description**：
```
An elegant, editorial one-page wedding website, also great for parties and events. Pure HTML, so there's no WordPress, no monthly fees and no coding required.

🔗 Live demo (English): [英文 Demo 網址]
🔗 Live demo (中文): [中文 Demo 網址]

Features
- Live countdown to the big day
- Our story timeline, ceremony and reception details with maps
- Day-of schedule, travel and accommodation
- Photo gallery
- RSVP form with meal choice and guest count
- SEO-ready with schema.org Event data

What you get
- English, Traditional Chinese and Simplified Chinese versions with a built-in language switcher
- Step-by-step guide and commercial licence

──────────
婚禮網站模板（也適合活動）。功能：倒數計時、我們的故事、典禮與宴客資訊、當天流程、交通住宿、相簿、RSVP 出席回覆表單、Google 結構化資料。附英文、繁體、簡體三種語言（網站內建語言切換）、中文教學、商業授權。

[貼上「共用文字」]
```

### 4-10. 攝影師

- **Name**：`Photographer Portfolio Website Template (English + 繁體 + 简体) — One-Page HTML`
- **URL**：`photographer-portfolio-template`
- **Cover**：`sales/covers/en/<slug>-cover.png`
- **Tags**：`photography website`, `photographer website`, `portfolio template`, `html template`, `website template`
- **Description**：
```
A dark, gallery-first one-page website for portrait, wedding and commercial photographers. Pure HTML, so there's no WordPress, no monthly fees and no coding required.

🔗 Live demo (English): [英文 Demo 網址]
🔗 Live demo (中文): [中文 Demo 網址]

Features
- Filterable portfolio grid with a keyboard-friendly lightbox
- Session packages with pricing and delivery times
- 4-step booking process and about section
- Client reviews
- Session enquiry form
- Sticky mobile "Book a session" button

What you get
- English, Traditional Chinese and Simplified Chinese versions with a built-in language switcher
- Step-by-step guide and commercial licence

──────────
攝影師作品集網站模板。功能：可篩選的作品集與燈箱看大圖、拍攝方案與價格、拍攝流程、關於我、客戶評價、預約表單、手機版底部預約按鈕。附英文、繁體、簡體三種語言（網站內建語言切換）、中文教學、商業授權。

[貼上「共用文字」]
```

### 4-11. 寵物美容／旅館

- **Name**：`Pet Grooming & Daycare Website Template (English + 繁體 + 简体)`
- **URL**：`pet-grooming-template`
- **Cover**：`sales/covers/en/<slug>-cover.png`
- **Tags**：`pet grooming website`, `dog grooming`, `pet daycare`, `html template`, `website template`
- **Description**：
```
A cheerful, friendly one-page website for pet groomers, daycare and boarding. Pure HTML, so there's no WordPress, no monthly fees and no coding required.

🔗 Live demo (English): [英文 Demo 網址]
🔗 Live demo (中文): [中文 Demo 網址]

Features
- Price list by pet size (small, medium, large, cats) in tabs
- Services, safety measures and groomer profiles
- Before and after gallery
- Booking notes accordion (vaccines, fleas, cancellations)
- Booking form with pet details
- SEO-ready with schema.org LocalBusiness data

What you get
- English, Traditional Chinese and Simplified Chinese versions with a built-in language switcher
- Step-by-step guide and commercial licence

──────────
寵物美容／旅館網站模板。功能：依體型分頁的價目表、服務項目、安心措施、美容師介紹、美容前後對比、預約須知、預約表單、Google 結構化資料。附英文、繁體、簡體三種語言（網站內建語言切換）、中文教學、商業授權。

[貼上「共用文字」]
```

### 4-12. 補習班／才藝教室

- **Name**：`Tutoring Center & Classes Website Template (English + 繁體 + 简体)`
- **URL**：`tutoring-school-template`
- **Cover**：`sales/covers/en/<slug>-cover.png`
- **Tags**：`tutoring website`, `school website`, `education template`, `html template`, `website template`
- **Description**：
```
A bright, trustworthy one-page website for tutoring centres, language schools and kids classes. Pure HTML, so there's no WordPress, no monthly fees and no coding required.

🔗 Live demo (English): [英文 Demo 網址]
🔗 Live demo (中文): [中文 Demo 網址]

Features
- Courses grouped by grade in tabs, with class size and fees
- Teaching approach and teacher profiles
- Weekly timetable (scrolls neatly on mobile)
- Student results and parent reviews
- Free trial class booking form
- SEO-ready with schema.org EducationalOrganization data

What you get
- English, Traditional Chinese and Simplified Chinese versions with a built-in language switcher
- Step-by-step guide and commercial licence

──────────
補習班／才藝教室網站模板。功能：依年級分頁的課程、教學特色、師資介紹、每週課表、學生成果、家長評價、免費試聽預約表單、Google 結構化資料。附英文、繁體、簡體三種語言（網站內建語言切換）、中文教學、商業授權。

[貼上「共用文字」]
```

### 4-13. 室內設計

- **Name**：`Interior Design Studio Website Template (English + 繁體 + 简体)`
- **URL**：`interior-design-template`
- **Cover**：`sales/covers/en/<slug>-cover.png`
- **Tags**：`interior designer`, `renovation website`, `architect portfolio`, `html template`, `website template`
- **Description**：
```
A warm, minimal one-page website for interior designers and renovation firms. Pure HTML, so there's no WordPress, no monthly fees and no coding required.

🔗 Live demo (English): [英文 Demo 網址]
🔗 Live demo (中文): [中文 Demo 網址]

Features
- Filterable project gallery with size, style and budget
- Before and after comparison slider
- 6-step process from consultation to handover
- Fee structure and team profiles
- Consultation booking form
- SEO-ready with schema.org data

What you get
- English, Traditional Chinese and Simplified Chinese versions with a built-in language switcher
- Step-by-step guide and commercial licence

──────────
室內設計網站模板。功能：可篩選的案例、裝修前後對比滑桿、服務流程、收費方式、設計團隊、客戶評價、預約丈量表單、Google 結構化資料。附英文、繁體、簡體三種語言（網站內建語言切換）、中文教學、商業授權。

[貼上「共用文字」]
```

### 4-14. 烘焙／甜點店

- **Name**：`Bakery & Dessert Shop Website Template with Pre-orders (English + 繁體 + 简体)`
- **URL**：`bakery-website-template`
- **Cover**：`sales/covers/en/<slug>-cover.png`
- **Tags**：`bakery website`, `cake shop website`, `pre-order form`, `html template`, `website template`
- **Description**：
```
A fresh, sweet one-page website for bakeries, patisseries and cake shops. Pure HTML, so there's no WordPress, no monthly fees and no coding required.

🔗 Live demo (English): [英文 Demo 網址]
🔗 Live demo (中文): [中文 Demo 網址]

Features
- This week's bake schedule with today highlighted
- Product tabs for bread, cakes and gift boxes
- Pre-order builder that totals your order
- Custom cake options and lead times
- Pickup order form
- SEO-ready with schema.org Bakery data

What you get
- English, Traditional Chinese and Simplified Chinese versions with a built-in language switcher
- Step-by-step guide and commercial licence

──────────
烘焙／甜點店網站模板。功能：本週出爐表、麵包／蛋糕／禮盒分頁、自動計算金額的預訂、客製蛋糕說明、取貨預訂表單、Google 結構化資料。附英文、繁體、簡體三種語言（網站內建語言切換）、中文教學、商業授權。

[貼上「共用文字」]
```

### 4-15. 手搖飲／茶飲店

- **Name**：`Bubble Tea Shop Website Template (English + 繁體 + 简体) — One-Page HTML`
- **URL**：`bubble-tea-shop-template`
- **Cover**：`sales/covers/en/<slug>-cover.png`
- **Tags**：`bubble tea website`, `cafe website`, `drink menu`, `html template`, `website template`
- **Description**：
```
A bold, poppy one-page website for bubble tea shops and tea bars. Pure HTML, so there's no WordPress, no monthly fees and no coding required.

🔗 Live demo (English): [英文 Demo 網址]
🔗 Live demo (中文): [中文 Demo 網址]

Features
- Menu tabs with size prices and tags
- Drink customiser: sweetness, ice and toppings with live price
- Multi-branch locations with hours and maps
- Delivery app buttons and loyalty info
- Franchise enquiry form
- SEO-ready with schema.org data

What you get
- English, Traditional Chinese and Simplified Chinese versions with a built-in language switcher
- Step-by-step guide and commercial licence

──────────
手搖飲／茶飲店網站模板。功能：分頁菜單、甜度冰塊配料客製試算、多門市據點、外送平台按鈕、集點說明、加盟洽詢表單。附英文、繁體、簡體三種語言（網站內建語言切換）、中文教學、商業授權。

[貼上「共用文字」]
```

### 4-16. 汽車美容／保養廠

- **Name**：`Car Detailing & Auto Repair Website Template (English + 繁體 + 简体)`
- **URL**：`auto-care-garage-template`
- **Cover**：`sales/covers/en/<slug>-cover.png`
- **Tags**：`auto repair website`, `car detailing`, `garage website`, `html template`, `website template`
- **Description**：
```
A precise, premium one-page website for car detailing studios and garages. Pure HTML, so there's no WordPress, no monthly fees and no coding required.

🔗 Live demo (English): [英文 Demo 網址]
🔗 Live demo (中文): [中文 Demo 網址]

Features
- Price list by vehicle size in tabs
- Service mileage reminder calculator
- Before and after gallery
- Technician team and FAQ
- Service booking form with plate and model
- SEO-ready with schema.org AutoRepair data

What you get
- English, Traditional Chinese and Simplified Chinese versions with a built-in language switcher
- Step-by-step guide and commercial licence

──────────
汽車美容／保養廠網站模板。功能：依車型分頁的價目表、保養里程提醒、施工前後對比、技師團隊、線上預約表單、Google 結構化資料。附英文、繁體、簡體三種語言（網站內建語言切換）、中文教學、商業授權。

[貼上「共用文字」]
```

### 4-17. 居家清潔

- **Name**：`Home Cleaning Service Website Template with Instant Quote (English + 繁體 + 简体)`
- **URL**：`home-cleaning-template`
- **Cover**：`sales/covers/en/<slug>-cover.png`
- **Tags**：`cleaning website`, `maid service`, `home services`, `html template`, `website template`
- **Description**：
```
A fresh, trustworthy one-page website for home and office cleaning services. Pure HTML, so there's no WordPress, no monthly fees and no coding required.

🔗 Live demo (English): [英文 Demo 網址]
🔗 Live demo (中文): [中文 Demo 網址]

Features
- Instant quote calculator by size, rooms and add-ons
- Room-by-room cleaning checklist
- 4-step process and service areas
- Reviews and FAQ
- Booking form that carries over the quote
- SEO-ready with schema.org data

What you get
- English, Traditional Chinese and Simplified Chinese versions with a built-in language switcher
- Step-by-step guide and commercial licence

──────────
居家清潔網站模板。功能：即時估價計算機、各空間清潔項目、服務流程、服務區域、評價、自動帶入估價的預約表單。附英文、繁體、簡體三種語言（網站內建語言切換）、中文教學、商業授權。

[貼上「共用文字」]
```

### 4-18. 花店

- **Name**：`Florist Website Template (English + 繁體 + 简体) — One-Page HTML`
- **URL**：`florist-template`
- **Cover**：`sales/covers/en/<slug>-cover.png`
- **Tags**：`florist website`, `flower shop`, `flower delivery`, `html template`, `website template`
- **Description**：
```
A lush, botanical one-page website for florists and flower studios. Pure HTML, so there's no WordPress, no monthly fees and no coding required.

🔗 Live demo (English): [英文 Demo 網址]
🔗 Live demo (中文): [中文 Demo 網址]

Features
- Bouquet tabs with size pricing
- Delivery date logic with same-day cut-off
- Monthly flower subscription plans
- Wedding and event florals enquiry
- Gift card message with character counter
- SEO-ready with schema.org Florist data

What you get
- English, Traditional Chinese and Simplified Chinese versions with a built-in language switcher
- Step-by-step guide and commercial licence

──────────
花店網站模板。功能：花束分頁與價格、配送日期判斷（當日截止時間）、每月訂花方案、婚禮活動花藝、花卡字數提示、訂購表單。附英文、繁體、簡體三種語言（網站內建語言切換）、中文教學、商業授權。

[貼上「共用文字」]
```

### 4-19. 瑜珈／皮拉提斯

- **Name**：`Yoga & Pilates Studio Website Template (English + 繁體 + 简体)`
- **URL**：`yoga-pilates-template`
- **Cover**：`sales/covers/en/<slug>-cover.png`
- **Tags**：`yoga website`, `pilates studio`, `wellness website`, `html template`, `website template`
- **Description**：
```
A serene, sculptural one-page website for yoga and pilates studios. Pure HTML, so there's no WordPress, no monthly fees and no coding required.

🔗 Live demo (English): [英文 Demo 網址]
🔗 Live demo (中文): [中文 Demo 網址]

Features
- Day-by-day class timetable with today selected
- Class types with level and duration
- Intro offers and class packs
- Teacher profiles and studio gallery
- Intro class booking form
- SEO-ready with schema.org data

What you get
- English, Traditional Chinese and Simplified Chinese versions with a built-in language switcher
- Step-by-step guide and commercial licence

──────────
瑜珈／皮拉提斯網站模板。功能：依星期切換的課表（自動選今天）、課程類型、體驗與課程方案、老師介紹、空間介紹、體驗課預約。附英文、繁體、簡體三種語言（網站內建語言切換）、中文教學、商業授權。

[貼上「共用文字」]
```

### 4-20. 露營區／豪華露營

- **Name**：`Campsite & Glamping Website Template (English + 繁體 + 简体)`
- **URL**：`campsite-glamping-template`
- **Cover**：`sales/covers/en/<slug>-cover.png`
- **Tags**：`campground website`, `glamping website`, `outdoor website`, `html template`, `website template`
- **Description**：
```
An adventurous one-page website for campsites and glamping sites. Pure HTML, so there's no WordPress, no monthly fees and no coding required.

🔗 Live demo (English): [英文 Demo 網址]
🔗 Live demo (中文): [中文 Demo 網址]

Features
- Site types with weekday and weekend rates
- Clickable camp map that highlights each site
- Stay estimate from your dates
- Facilities, camp rules and gear tips
- Reservation form
- SEO-ready with schema.org Campground data

What you get
- English, Traditional Chinese and Simplified Chinese versions with a built-in language switcher
- Step-by-step guide and commercial licence

──────────
露營區／豪華露營網站模板。功能：營位類型與平假日價格、可點選的營地地圖、住宿費用試算、營地設施、營地規範、裝備建議、訂位表單。附英文、繁體、簡體三種語言（網站內建語言切換）、中文教學、商業授權。

[貼上「共用文字」]
```

### 4-21. 個人品牌／自由工作者

- **Name**：`Freelancer Portfolio & Résumé Website Template (English + 繁體 + 简体)`
- **URL**：`freelancer-portfolio-template`
- **Cover**：`sales/covers/en/<slug>-cover.png`
- **Tags**：`portfolio website`, `resume website`, `freelancer`, `personal website`, `html template`
- **Description**：
```
A confident, modern one-page website for freelancers, designers and developers. Pure HTML, so there's no WordPress, no monthly fees and no coding required.

🔗 Live demo (English): [英文 Demo 網址]
🔗 Live demo (中文): [中文 Demo 網址]

Features
- Bento-style case study grid
- Services with starting prices
- Skills, experience timeline and résumé download
- Light / dark mode toggle
- Project enquiry form
- SEO-ready with schema.org Person data

What you get
- English, Traditional Chinese and Simplified Chinese versions with a built-in language switcher
- Step-by-step guide and commercial licence

──────────
個人品牌／自由工作者網站模板。功能：作品集、服務與起價、技能與經歷、履歷下載、合作流程、深淺色模式切換、合作洽談表單。附英文、繁體、簡體三種語言（網站內建語言切換）、中文教學、商業授權。

[貼上「共用文字」]
```

### 4-22. App／軟體產品登陸頁

- **Name**：`SaaS & App Landing Page Template (English + 繁體 + 简体) — One-Page HTML`
- **URL**：`app-saas-landing-template`
- **Cover**：`sales/covers/en/<slug>-cover.png`
- **Tags**：`saas landing page`, `app landing page`, `startup website`, `html template`, `landing page`
- **Description**：
```
A crisp product-marketing landing page for apps and SaaS products. Pure HTML, so there's no WordPress, no monthly fees and no coding required.

🔗 Live demo (English): [英文 Demo 網址]
🔗 Live demo (中文): [中文 Demo 網址]

Features
- Product UI mock built in HTML (easy to swap for screenshots)
- Feature sections with mini UI previews
- Pricing tiers with monthly / yearly toggle
- Feature comparison table
- Email sign-up CTA band
- SEO-ready with schema.org SoftwareApplication data

What you get
- English, Traditional Chinese and Simplified Chinese versions with a built-in language switcher
- Step-by-step guide and commercial licence

──────────
App／軟體產品登陸頁模板。功能：產品介面展示、功能介紹、使用流程、月繳／年繳切換的方案價格、功能比較表、Email 訂閱。附英文、繁體、簡體三種語言（網站內建語言切換）、中文教學、商業授權。

[貼上「共用文字」]
```

### 4-23. 心理諮商／教練

- **Name**：`Therapist & Coach Website Template (English + 繁體 + 简体) — One-Page HTML`
- **URL**：`therapist-coach-template`
- **Cover**：`sales/covers/en/coach-cover.png`
- **Tags**：`therapist website`, `counseling website`, `coach website`, `html template`, `website template`
- **Description**：
```
A warm, calm one-page website for therapists, counselors and coaches. Pure HTML, so there's no WordPress, no monthly fees and no coding required.

🔗 Live demo (English): [英文 Demo 網址]
🔗 Live demo (中文): [中文 Demo 網址]

Features
- Services with session length and fees
- Approach, about and credentials sections
- First-session steps and privacy FAQ
- Private booking form
- Crisis-line notice built in
- SEO-ready with schema.org data

What you get
- English, Traditional Chinese and Simplified Chinese versions with a built-in language switcher
- Step-by-step guide and commercial licence

──────────
心理諮商／教練網站模板。功能：服務與費用、諮商取向、關於我、初談流程、保密與取消政策、預約表單、危機專線提醒。附英文、繁體、簡體三種語言（網站內建語言切換）、中文教學、商業授權。

[貼上「共用文字」]
```

### 4-24. 水電修繕／工程行

- **Name**：`Contractor & Handyman Website Template (English + 繁體 + 简体)`
- **URL**：`contractor-handyman-template`
- **Cover**：`sales/covers/en/contractor-cover.png`
- **Tags**：`contractor website`, `plumber website`, `handyman website`, `html template`, `website template`
- **Description**：
```
A rugged, dependable one-page website for plumbers, electricians and handymen. Pure HTML, so there's no WordPress, no monthly fees and no coding required.

🔗 Live demo (English): [英文 Demo 網址]
🔗 Live demo (中文): [中文 Demo 網址]

Features
- Big click-to-call header and sticky call bar
- Emergency / scheduled service toggle
- Price guide table and service area map
- Before and after gallery
- Quote request form
- SEO-ready with schema.org data

What you get
- English, Traditional Chinese and Simplified Chinese versions with a built-in language switcher
- Step-by-step guide and commercial licence

──────────
水電修繕網站模板。功能：大型撥號按鈕、急修／預約切換、參考價目、服務區域、施工前後對比、估價表單。附英文、繁體、簡體三種語言（網站內建語言切換）、中文教學、商業授權。

[貼上「共用文字」]
```

### 4-25. 非營利／教會

- **Name**：`Nonprofit & Church Website Template with Donation Widget (English + 繁體 + 简体)`
- **URL**：`nonprofit-charity-template`
- **Cover**：`sales/covers/en/nonprofit-cover.png`
- **Tags**：`nonprofit website`, `charity website`, `church website`, `donation page`, `html template`
- **Description**：
```
A hopeful, credible one-page website for nonprofits, charities and churches. Pure HTML, so there's no WordPress, no monthly fees and no coding required.

🔗 Live demo (English): [英文 Demo 網址]
🔗 Live demo (中文): [中文 Demo 網址]

Features
- Donation widget with one-time / monthly and impact text
- Programs, stories and volunteer sign-up
- Events calendar
- Transparency section (annual report, registration no.)
- Notes for adapting to a church
- SEO-ready with schema.org NGO data

What you get
- English, Traditional Chinese and Simplified Chinese versions with a built-in language switcher
- Step-by-step guide and commercial licence

──────────
非營利／教會網站模板。功能：捐款小工具（單次／定期、影響力說明）、服務計畫、受助者故事、志工招募、活動行事曆、財務透明。附英文、繁體、簡體三種語言（網站內建語言切換）、中文教學、商業授權。

[貼上「共用文字」]
```

### 4-26. Link-in-bio 個人連結頁

- **Name**：`Link-in-Bio Page Template — Linktree Alternative (English + 繁體 + 简体)`
- **URL**：`link-in-bio-template`
- **Cover**：`sales/covers/en/linkinbio-cover.png`
- **Tags**：`link in bio`, `linktree alternative`, `creator page`, `html template`, `bio link`
- **Description**：
```
A characterful link-in-bio page for creators and small shops. Host it free, no subscription. Pure HTML, so there's no WordPress, no monthly fees and no coding required.

🔗 Live demo (English): [英文 Demo 網址]
🔗 Live demo (中文): [中文 Demo 網址]

Features
- 3 switchable themes (Paper, Midnight, Bold)
- Social icon row and link buttons
- Featured product and latest video cards
- Email sign-up
- Share / copy link button
- SEO-ready with schema.org Person data

What you get
- English, Traditional Chinese and Simplified Chinese versions with a built-in language switcher
- Step-by-step guide and commercial licence

──────────
Link-in-bio 個人連結頁模板（Linktree 替代品）。功能：三種主題切換、社群連結、連結按鈕、精選商品、最新影片、Email 訂閱、分享按鈕。附英文、繁體、簡體三種語言（網站內建語言切換）、中文教學、商業授權。

[貼上「共用文字」]
```

### 4-27. 男士理髮廳

- **Name**：`Barbershop Website Template (English + 繁體 + 简体) — One-Page HTML`
- **URL**：`barbershop-template`
- **Cover**：`sales/covers/en/barber-cover.png`
- **Tags**：`barbershop website`, `barber website`, `mens grooming`, `html template`, `website template`
- **Description**：
```
A classic-meets-modern one-page website for barbershops. Pure HTML, so there's no WordPress, no monthly fees and no coding required.

🔗 Live demo (English): [英文 Demo 網址]
🔗 Live demo (中文): [中文 Demo 網址]

Features
- Price list with durations
- Barber profiles that preselect the booking form
- Open-now badge and typical wait
- Style gallery
- Booking form
- SEO-ready with schema.org data

What you get
- English, Traditional Chinese and Simplified Chinese versions with a built-in language switcher
- Step-by-step guide and commercial licence

──────────
男士理髮廳網站模板。功能：價目表、理髮師介紹（點選自動帶入預約）、營業中與候位提示、作品集、預約表單。附英文、繁體、簡體三種語言（網站內建語言切換）、中文教學、商業授權。

[貼上「共用文字」]
```

### 4-28. 研討會／講座活動

- **Name**：`Conference & Workshop Event Landing Page (English + 繁體 + 简体)`
- **URL**：`conference-event-template`
- **Cover**：`sales/covers/en/conference-cover.png`
- **Tags**：`conference website`, `event landing page`, `workshop page`, `html template`, `event template`
- **Description**：
```
A bold, poster-style landing page for conferences, summits and workshops. Pure HTML, so there's no WordPress, no monthly fees and no coding required.

🔗 Live demo (English): [英文 Demo 網址]
🔗 Live demo (中文): [中文 Demo 網址]

Features
- Live countdown and big-date hero
- Speaker grid with accessible bio modal
- Agenda tabs by track or day
- Add-to-calendar (.ics) download
- Ticket tiers with automatic early-bird cut-off
- SEO-ready with schema.org Event data

What you get
- English, Traditional Chinese and Simplified Chinese versions with a built-in language switcher
- Step-by-step guide and commercial licence

──────────
研討會／講座活動頁模板。功能：倒數計時、講者介紹、分軌議程、加入行事曆、票種與早鳥自動截止、場地交通、贊助方案。附英文、繁體、簡體三種語言（網站內建語言切換）、中文教學、商業授權。

[貼上「共用文字」]
```

### 4-29. 刺青工作室

- **Name**：`Tattoo Studio Website Template (English + 繁體 + 简体) — One-Page HTML`
- **URL**：`tattoo-studio-template`
- **Cover**：`sales/covers/en/tattoo-cover.png`
- **Tags**：`tattoo website`, `tattoo studio`, `artist portfolio`, `html template`, `website template`
- **Description**：
```
An edgy, fine-art one-page website for tattoo studios. Pure HTML, so there's no WordPress, no monthly fees and no coding required.

🔗 Live demo (English): [英文 Demo 網址]
🔗 Live demo (中文): [中文 Demo 網址]

Features
- Portfolio filter by artist and style with lightbox
- Flash sheet with fixed prices that preselect the form
- Pricing, process and aftercare
- Age and health notes
- Consultation booking form
- SEO-ready with schema.org data

What you get
- English, Traditional Chinese and Simplified Chinese versions with a built-in language switcher
- Step-by-step guide and commercial licence

──────────
刺青工作室網站模板。功能：依刺青師與風格篩選的作品集、現貨 Flash 圖、價格說明、刺青流程、照護須知、預約表單。附英文、繁體、簡體三種語言（網站內建語言切換）、中文教學、商業授權。

[貼上「共用文字」]
```

### 4-30. 共享辦公室

- **Name**：`Coworking Space Website Template (English + 繁體 + 简体) — One-Page HTML`
- **URL**：`coworking-space-template`
- **Cover**：`sales/covers/en/coworking-cover.png`
- **Tags**：`coworking website`, `office space`, `meeting rooms`, `html template`, `website template`
- **Description**：
```
A lively, design-forward one-page website for coworking spaces. Pure HTML, so there's no WordPress, no monthly fees and no coding required.

🔗 Live demo (English): [英文 Demo 網址]
🔗 Live demo (中文): [中文 Demo 網址]

Features
- Space types from hot desks to private offices
- Day / month pricing toggle
- Meeting room estimator with capacity check
- Amenities, community events and location
- Tour booking form
- SEO-ready with schema.org data

What you get
- English, Traditional Chinese and Simplified Chinese versions with a built-in language switcher
- Step-by-step guide and commercial licence

──────────
共享辦公室網站模板。功能：空間類型、日租／月租切換、會議室即時估價、設施介紹、社群活動、預約參觀。附英文、繁體、簡體三種語言（網站內建語言切換）、中文教學、商業授權。

[貼上「共用文字」]
```

### 4-31. 牙醫第二款「森林診間」（11/27 新增）

> 跟 4-4 的 clinic（安和牙醫，資訊感、無襯線、圓角卡片）是**不同風格的第二款**：滿版診間首屏、襯線標題、清單式、拱形醫師相框。說明裡要寫清楚「second style」，讓買家知道兩款可以比較著選，不要讓兩個商品頁讀起來一樣。
> 名稱直接用 11 節的新格式 `(EN + 中文 + 日本語)`；zip 也含簡體版。

| 欄位 | 填入 |
|---|---|
| Name | `Dental Clinic Website — Forest Edition (EN + 中文 + 日本語)` |
| URL | `dental-clinic-forest-template`（和 clinic 的 `clinic-website-template` 不同） |
| Price | `39` |
| Versions | `Standard license — 1 website`（$39）、`Extended license — up to 10 websites`（$119） |
| Content | `dist/dental-clinic-forest-template.zip` |
| Cover | `sales/covers/en/dental-cover.png` |
| Thumbnail | `sales/covers/en/dental-thumb.png` |
| Summary | `A calm, light-filled one-page website for dental practices in English, 繁體中文, 简体中文 and 日本語, with a step-by-step setup guide and a commercial licence. Buy once, no monthly fees.` |
| Additional details | `Format: HTML/CSS/JS` · `Languages: English, 繁體中文, 简体中文, 日本語 (switchable)` · `Pages: 1 (one-page)` · `Builder needed: None` · `Style: second dental style (see also our Clinic template)` |
| Receipt | 共用 Receipt |
| Tags（10 個，每個 ≤ 20 字元） | `dental website`, `dentist website`, `dental clinic`, `clinic website`, `medical website`, `html template`, `website template`, `one page website`, `ホームページ テンプレート`, `歯科 ホームページ` |

Demo：英文 `https://a0955072107-bit.github.io/-/templates/dental/en/`、繁中 `https://a0955072107-bit.github.io/-/templates/dental/zh-TW/`、簡中 `…/templates/dental/zh-CN/`、日文 `…/templates/dental/ja/`。（線上 Demo 有示意照片；商品 zip 不含照片，用 CSS 畫的構圖佔位圖，買家換成自己的照片。）

**Description**：
```
日本語版つき：テキスト・住所・LINE ボタンまで日本向けに作り直した日本語版が入っています。ガイドとライセンスも日本語で同梱。月額費用なし、買い切りです。

A quiet, light-filled one-page website for dental practices. This is our second dental style: where our Clinic template is crisp and information-first, the Forest Edition leads with a full-width treatment-room image, serif headings and plenty of white space. Pure HTML, so there's no WordPress, no monthly fees and no coding required.

🔗 Live demo (English): https://a0955072107-bit.github.io/-/templates/dental/en/
🔗 Live demo (中文): https://a0955072107-bit.github.io/-/templates/dental/zh-TW/
🔗 Live demo (日本語): https://a0955072107-bit.github.io/-/templates/dental/ja/
(Demo photos are for preview only and are not included. The template ships with drawn placeholders showing what photo goes where.)

Features
- Full-width treatment-room hero with a calm text panel and two buttons
- "Your first visit" in three numbered steps
- Treatments as a clean list with thin rules
- Dentist profiles in arched frames, each with focus areas and hours
- Two wide photo slots for the waiting area and consultation room
- Edit one weekly table and the "Today" board updates itself (open now, later today, check-in closed, closed), using your clinic's time zone
- Directions with transit, parking and step-free access, plus a Google Maps link (no embedded map)
- Call and Book buttons fixed to the bottom on mobile (WhatsApp in English, LINE in Chinese and Japanese, easy to swap)
- SEO-ready with schema.org Dentist data
- Modest, factual sample copy with no reviews, before/after photos or "best/painless" claims. Please follow your local healthcare advertising rules.

What you get
- English, Traditional Chinese, Simplified Chinese and Japanese versions with a built-in language switcher
- Step-by-step guide and commercial licence

Prefer a more information-first layout? See our Clinic template: https://polyglotpages.gumroad.com/l/clinic-website-template

──────────
牙醫診所網站模板・第二款「森林診間」。和我們的「診所模板」不同風格：首屏是滿版診間大圖，襯線標題、大量留白，走安靜、有自然光的精品診所路線。
功能：第一次看診三步驟、診療項目清單、拱形醫師相框（專長與看診時段）、診所環境兩張橫幅照片、只要改一張門診表，「今日門診」看板就自動更新（依診所時區）、交通／停車／無障礙說明與 Google 地圖連結、手機版底部「撥打電話／LINE 預約」。
範例文案遵守醫療廣告規範：不放見證、前後對比、優惠或療效保證。附英文、繁體、簡體、日文四種語言（網站內建語言切換）、中文教學、商業授權。
線上 Demo 的照片僅供示意，商品不含照片。

[貼上「共用文字」]
```

> **建議（待使用者決定）：牙醫 2 款組合包**
> 現在 clinic 和 dental 是同一行業的兩種風格，可以另開一個 Bundle「Dental Website Templates — 2 Styles」$59（單買 $78，省 $19）。
> - 每家多收：原本會買 1 款的牙醫或接案者，估計 1～2 成會升級成 $59（每筆多 $20）；接案者可以給客戶選風格，比較有吸引力。
> - 成本／時間：Gumroad Bundle 選兩個既有商品就好，約 15 分鐘，不用新檔案（封面可用兩張縮圖拼一張）。
> - 風險：兩款單價看起來被打折、單款銷量可能被分走一點；Pinterest／說明裡的連結會多一個要維護。
> - 建議時機：dental 上架後 2～4 週，看兩款各自有沒有被點擊再決定。**現在先不要上架。**

### 4-32. 中醫／針灸診所「本草堂」（11/28 新增）

> 新行業（中醫、針灸、漢方）。和 4-4 clinic、4-31 dental 同屬診所類，但內容是針灸、中藥、推拿，另有「常見求診原因」索引。**商品頁和宣傳文字都不寫療效**：不寫 treat／cure／heal／relief／effective，也不列病名當賣點；只描述網站有哪些區塊。範例店名「Bencao Acupuncture & Herbs／本草堂」是虛構的示範內容。
> 名稱用 11 節的格式 `(EN + 中文 + 日本語)`；zip 也含簡體版。

| 欄位 | 填入 |
|---|---|
| Name | `Acupuncture & TCM Clinic Website Template (EN + 中文 + 日本語)` |
| URL | `tcm-acupuncture-clinic-template`（和 clinic 的 `clinic-website-template`、dental 的 `dental-clinic-forest-template` 不同） |
| Price | `39` |
| Versions | `Standard license — 1 website`（$39）、`Extended license — up to 10 websites`（$119） |
| Content | `dist/tcm-acupuncture-clinic-template.zip` |
| Cover | `sales/covers/en/tcm-cover.png` |
| Thumbnail | `sales/covers/en/tcm-thumb.png` |
| Summary | `A calm one-page website for acupuncture and Chinese medicine clinics in English, 繁體中文, 简体中文 and 日本語, with a step-by-step setup guide and a commercial licence. Buy once, no monthly fees.` |
| Additional details | `Format: HTML/CSS/JS` · `Languages: English, 繁體中文, 简体中文, 日本語 (switchable)` · `Pages: 1 (one-page)` · `Builder needed: None` · `Style: herb-cabinet hero, serif headings (see also our Clinic template)` |
| Receipt | 共用 Receipt |
| Tags（10 個，每個 ≤ 20 字元） | `acupuncture website`, `tcm website`, `acupuncturist`, `clinic website`, `wellness website`, `html template`, `website template`, `one page website`, `ホームページ テンプレート`, `鍼灸院 ホームページ` |

Demo：英文 `https://a0955072107-bit.github.io/-/templates/tcm/en/`、繁中 `https://a0955072107-bit.github.io/-/templates/tcm/zh-TW/`、簡中 `…/templates/tcm/zh-CN/`、日文 `…/templates/tcm/ja/`。（線上 Demo 有示意照片；商品 zip 不含照片，用 CSS 畫的構圖佔位圖，買家換成自己的照片。）

**Description**：
```
日本語版つき：テキスト・住所・LINE ボタンまで日本向けに作り直した日本語版（鍼灸・漢方相談の院向け）が入っています。ガイドとライセンスも日本語で同梱。月額費用なし、買い切りです。

A calm one-page website for acupuncture and Traditional Chinese Medicine clinics. It opens with a herb-cabinet image and a plain promise to explain the plan and the cost first, then walks a new patient through the first visit. Pure HTML, so there's no WordPress, no monthly fees and no coding required.

🔗 Live demo (English): https://a0955072107-bit.github.io/-/templates/tcm/en/
🔗 Live demo (中文): https://a0955072107-bit.github.io/-/templates/tcm/zh-TW/
🔗 Live demo (日本語): https://a0955072107-bit.github.io/-/templates/tcm/ja/
(Demo photos are for preview only and are not included. The template ships with drawn placeholders showing what photo goes where. "Bencao Acupuncture & Herbs" and the practitioners are fictional examples.)

Features
- Hero with a herb-cabinet image, a short statement and two buttons
- "Your first visit" in four numbered steps
- Services list (acupuncture, herbs, tui na, cupping and moxibustion) with insurance or self-pay labels
- "People often visit us for…" index, worded as common reasons for visiting, with a note that these are not claims about results
- Two practitioner profiles with focus, training and schedule
- Edit one weekly table and the "Today" board updates itself, using your clinic's time zone
- "Before you come" notes and a four-question FAQ
- Location with parking, transit and step-free access, plus a Google Maps link (no embedded map)
- Call and Book buttons fixed to the bottom on mobile (WhatsApp in English, LINE in Chinese and Japanese, easy to swap)
- SEO-ready with schema.org MedicalBusiness data
- Sample copy is modest and factual, with no testimonials, before/after photos or outcome promises. Please follow your local healthcare advertising rules.

What you get
- English, Traditional Chinese, Simplified Chinese and Japanese versions with a built-in language switcher
- Step-by-step guide and commercial licence

Looking for a general or dental clinic layout? See our Clinic template, another style in the same field: https://polyglotpages.gumroad.com/l/clinic-website-template

──────────
中醫／針灸診所網站模板。首屏是藥櫃圖與一句「先聽、再說明計畫與費用」，接著帶新病人看完第一次看診的流程。
功能：初診四步驟、診療項目（針灸、中藥、推拿、拔罐艾灸，標示健保或自費）、「常見求診原因」索引（附註不代表療效）、兩位醫師簡介與看診時段、只要改一張門診表，「今日門診」看板就自動更新（依診所時區）、看診前須知與常見問題、交通／停車／無障礙說明與 Google 地圖連結、手機版底部「撥打電話／LINE 預約」。
範例文案遵守醫療廣告規範：不放見證、前後對比、優惠或療效保證。附英文、繁體、簡體、日文四種語言（網站內建語言切換）、中文教學、商業授權。
線上 Demo 的照片僅供示意，商品不含照片；「本草堂」與醫師皆為虛構範例。
想要一般診所或牙醫的版型，可以看另一款風格的「診所模板」。

[貼上「共用文字」]
```

### 4-33. 粵菜館「瑞記」（11/28 新增，餐廳第二款）

> 跟 4-1 的 restaurant（咖啡廳／小餐館，暖色、照片為主）是**不同風格的第二款**：以菜單為主角，首屏就是「今日招牌」板，青花瓷藍配色，菜名中英對照，外帶表單優先。說明裡寫清楚「another style」。範例店名「Sui Kee Cantonese Kitchen／瑞記粵菜」是虛構的示範內容。

| 欄位 | 填入 |
|---|---|
| Name | `Cantonese & Chinese Restaurant Website Template (EN + 中文 + 日本語)` |
| URL | `cantonese-restaurant-template`（和 restaurant 的 `restaurant-website-template` 不同） |
| Price | `39` |
| Versions | `Standard license — 1 website`（$39）、`Extended license — up to 10 websites`（$119） |
| Content | `dist/cantonese-restaurant-template.zip` |
| Cover | `sales/covers/en/canton-cover.png` |
| Thumbnail | `sales/covers/en/canton-thumb.png` |
| Summary | `A menu-first one-page website for Cantonese and Chinese restaurants in English, 繁體中文, 简体中文 and 日本語, with a step-by-step setup guide and a commercial licence. Buy once, no monthly fees.` |
| Additional details | `Format: HTML/CSS/JS` · `Languages: English, 繁體中文, 简体中文, 日本語 (switchable)` · `Pages: 1 (one-page)` · `Builder needed: None` · `Style: menu-first, porcelain blue (see also our Restaurant & Café template)` |
| Receipt | 共用 Receipt |
| Tags（10 個，每個 ≤ 20 字元） | `restaurant website`, `chinese restaurant`, `cantonese restaurant`, `menu website`, `takeout website`, `html template`, `website template`, `one page website`, `ホームページ テンプレート`, `飲食店 ホームページ` |

Demo：英文 `https://a0955072107-bit.github.io/-/templates/canton/en/`、繁中 `https://a0955072107-bit.github.io/-/templates/canton/zh-TW/`、簡中 `…/templates/canton/zh-CN/`、日文 `…/templates/canton/ja/`。（線上 Demo 有示意照片；商品 zip 不含照片，用 CSS 畫的構圖佔位圖，買家換成自己的照片。）

**Description**：
```
日本語版つき：テキスト・住所・価格（税込表示）・LINE ボタンまで日本向けに作り直した日本語版が入っています。ガイドとライセンスも日本語で同梱。月額費用なし、買い切りです。

A menu-first one-page website for Cantonese and Chinese restaurants. This is our second restaurant style: where our Restaurant & Café template is warm and photo-led, this one puts the menu up front with a signatures board, Chinese and English dish names side by side and a porcelain-blue palette. Pure HTML, so there's no WordPress, no monthly fees and no coding required.

🔗 Live demo (English): https://a0955072107-bit.github.io/-/templates/canton/en/
🔗 Live demo (中文): https://a0955072107-bit.github.io/-/templates/canton/zh-TW/
🔗 Live demo (日本語): https://a0955072107-bit.github.io/-/templates/canton/ja/
(Demo photos are for preview only and are not included. The template ships with drawn placeholders showing what photo goes where. "Sui Kee Cantonese Kitchen" and its menu are fictional examples.)

Features
- Hero with an "On today's board" panel for three signature dishes
- Open or closed status worked out from your hours and time zone
- Full menu in five tabs (roast meats, wok dishes, rice and noodles, clay pots, dim sum), each dish with its Chinese name, a one-line note and Signature, Spicy or Vegetarian labels
- Weekday lunch special band with its own prices
- Banquets and catering: private rooms, set dinners and tray sizes
- Hours, "How pickup works" in three steps, directions and a Google Maps link (no embedded map)
- Order form for pickup, a table or a banquet enquiry (works with Formspree, no backend needed)
- Order and Call buttons fixed to the bottom on mobile
- SEO-ready with schema.org Restaurant data

What you get
- English, Traditional Chinese, Simplified Chinese and Japanese versions with a built-in language switcher
- Step-by-step guide and commercial licence

Running a café or bistro? See our Restaurant & Café template, another style for the same trade: https://polyglotpages.gumroad.com/l/restaurant-website-template

──────────
粵菜館／中餐廳網站模板・餐廳第二款。和我們的「餐廳／咖啡廳模板」不同風格：菜單當主角，首屏就是「今日招牌」板，菜名中英對照，青花瓷藍配色。
功能：依營業時間與時區顯示營業中或休息、五個分頁的完整菜單（燒臘、小炒、粉麵飯、煲仔、點心，可標招牌／辣／素）、平日商業午餐、包廂／合菜／外燴、營業時間與外帶三步驟、交通說明與 Google 地圖連結、外帶／訂位／宴席表單（接 Formspree，不用後端）、手機版底部「線上點外帶／來電」。
附英文、繁體、簡體、日文四種語言（網站內建語言切換）、中文教學、商業授權。
線上 Demo 的照片僅供示意，商品不含照片；「瑞記粵菜」與菜單皆為虛構範例。
開咖啡廳或小餐館，可以看另一款風格的「餐廳／咖啡廳模板」。

[貼上「共用文字」]
```

### 4-34. 髮型沙龍「SOU 髮藝」（11/28 新增，美髮第二款）

> 跟 4-2 的 beauty（美髮美甲，粉色系、作品集篩選）是**不同風格的第二款**：黑白雜誌感、大字價目表、每位設計師有自己的預約按鈕、橫向滑動 Lookbook。說明裡寫清楚「another style」。範例店名「SOU Hair Studio／SOU 髮藝」與設計師是虛構的示範內容。

| 欄位 | 填入 |
|---|---|
| Name | `Hair Studio Website Template — Editorial Edition (EN + 中文 + 日本語)` |
| URL | `hair-studio-template`（和 beauty 的 `salon-website-template` 不同） |
| Price | `39` |
| Versions | `Standard license — 1 website`（$39）、`Extended license — up to 10 websites`（$119） |
| Content | `dist/hair-studio-template.zip` |
| Cover | `sales/covers/en/hair-cover.png` |
| Thumbnail | `sales/covers/en/hair-thumb.png` |
| Summary | `A black-and-white editorial one-page website for hair salons in English, 繁體中文, 简体中文 and 日本語, with a step-by-step setup guide and a commercial licence. Buy once, no monthly fees.` |
| Additional details | `Format: HTML/CSS/JS` · `Languages: English, 繁體中文, 简体中文, 日本語 (switchable)` · `Pages: 1 (one-page)` · `Builder needed: None` · `Style: black-and-white editorial (see also our Hair & Nail Salon template)` |
| Receipt | 共用 Receipt |
| Tags（10 個，每個 ≤ 20 字元） | `hair salon website`, `salon website`, `hairstylist website`, `hairdresser website`, `beauty website`, `html template`, `website template`, `one page website`, `ホームページ テンプレート`, `美容室 ホームページ` |

Demo：英文 `https://a0955072107-bit.github.io/-/templates/hair/en/`、繁中 `https://a0955072107-bit.github.io/-/templates/hair/zh-TW/`、簡中 `…/templates/hair/zh-CN/`、日文 `…/templates/hair/ja/`。（線上 Demo 有示意照片；商品 zip 不含照片，用 CSS 畫的構圖佔位圖，買家換成自己的照片。）

**Description**：
```
日本語版つき：テキスト・住所・価格（税込表示）・LINE ボタンまで日本向けに作り直した日本語版が入っています。ガイドとライセンスも日本語で同梱。月額費用なし、買い切りです。

A black-and-white, editorial one-page website for hair salons and independent stylists. This is our second salon style: where our Hair & Nail Salon template is soft and portfolio-led, the Editorial Edition is built around a large-type price list and stylists you can book directly. Pure HTML, so there's no WordPress, no monthly fees and no coding required.

🔗 Live demo (English): https://a0955072107-bit.github.io/-/templates/hair/en/
🔗 Live demo (中文): https://a0955072107-bit.github.io/-/templates/hair/zh-TW/
🔗 Live demo (日本語): https://a0955072107-bit.github.io/-/templates/hair/ja/
(Demo photos are for preview only and are not included. The template ships with drawn placeholders showing what photo goes where. "SOU Hair Studio" and its stylists are fictional examples.)

Features
- Hero with a big two-line headline, one portrait image and two buttons
- Price list in large type, grouped by cut, colour, perm and care, with time needed and add-ons for longer hair
- Three stylist profiles, each with what they are known for, working days and their own booking button
- Lookbook that scrolls sideways (CSS scroll-snap, no script), six looks with captions
- "Your first visit" in three steps and a four-question FAQ
- Hours with last-appointment times, address, parking note and a Google Maps link (no embedded map)
- Call and Book buttons fixed to the bottom on mobile (WhatsApp in English, LINE in Chinese and Japanese, easy to swap)
- SEO-ready with schema.org HairSalon data

What you get
- English, Traditional Chinese, Simplified Chinese and Japanese versions with a built-in language switcher
- Step-by-step guide and commercial licence

Also offer nails or want a softer look? See our Hair & Nail Salon template, another style for the same trade: https://polyglotpages.gumroad.com/l/salon-website-template

──────────
髮型沙龍網站模板・美髮第二款「雜誌感」。和我們的「美髮美甲模板」不同風格：黑白配色、大字價目表，每位設計師都有自己的預約按鈕。
功能：大字價目表（剪、染、燙、護，標示所需時間與長髮加價）、三位設計師簡介（擅長風格、上班日、各自的預約按鈕）、橫向滑動的 Lookbook（六款髮型）、第一次來店三步驟與常見問題、營業時間與最後預約時間、地址／停車與 Google 地圖連結、手機版底部「撥打電話／選設計師預約」。
附英文、繁體、簡體、日文四種語言（網站內建語言切換）、中文教學、商業授權。
線上 Demo 的照片僅供示意，商品不含照片；「SOU 髮藝」與設計師皆為虛構範例。
有做美甲或想要柔和一點的版型，可以看另一款風格的「美髮美甲模板」。

[貼上「共用文字」]
```

### 4-35. 補習班／課後輔導「學行教室」（11/28 新增，補習班第二款）

> 跟 4-12 的 education（補習班／才藝教室，藍色、課表為主）是**不同風格的第二款**：石墨色配紙白、首屏就是「孩子幾年級」選擇器，點了只顯示適合的班別；班別、人數、學費放在同一張清單。說明裡寫清楚「another style」。兩款的 URL 很像（`tutoring-school-template` 是舊款、`tutoring-center-template` 是這款），填的時候看清楚。範例店名「Stride Learning Center／學行教室」與老師是虛構的示範內容。
> 範例文案不放榜單、不保證分數；商品頁也不要寫「提分」「保證進步」。

| 欄位 | 填入 |
|---|---|
| Name | `Tutoring & Learning Center Website — Grade Picker Edition (EN + 中文 + 日本語)` |
| URL | `tutoring-center-template`（和 education 的 `tutoring-school-template` 不同） |
| Price | `39` |
| Versions | `Standard license — 1 website`（$39）、`Extended license — up to 10 websites`（$119） |
| Content | `dist/tutoring-center-template.zip` |
| Cover | `sales/covers/en/tutor-cover.png` |
| Thumbnail | `sales/covers/en/tutor-thumb.png` |
| Summary | `A clear one-page website for tutoring and learning centers in English, 繁體中文, 简体中文 and 日本語, with a grade picker, a step-by-step setup guide and a commercial licence. Buy once, no monthly fees.` |
| Additional details | `Format: HTML/CSS/JS` · `Languages: English, 繁體中文, 简体中文, 日本語 (switchable)` · `Pages: 1 (one-page)` · `Builder needed: None` · `Style: grade picker, graphite and paper white (see also our Tutoring School template)` |
| Receipt | 共用 Receipt |
| Tags（10 個，每個 ≤ 20 字元） | `tutoring website`, `learning center`, `tutor website`, `after school`, `education website`, `html template`, `website template`, `one page website`, `ホームページ テンプレート`, `学習塾 ホームページ` |

Demo：英文 `https://a0955072107-bit.github.io/-/templates/tutor/en/`、繁中 `https://a0955072107-bit.github.io/-/templates/tutor/zh-TW/`、簡中 `…/templates/tutor/zh-CN/`、日文 `…/templates/tutor/ja/`。（線上 Demo 有示意照片；商品 zip 不含照片，用 CSS 畫的構圖佔位圖，買家換成自己的照片。）

**Description**：
```
日本語版つき：テキスト・住所・料金（税込表示）・LINE ボタンまで日本向けに作り直した日本語版（学習塾向け）が入っています。ガイドとライセンスも日本語で同梱。月額費用なし、買い切りです。

A clear one-page website for tutoring and learning centers. This is our second education style: where our Tutoring School template leads with courses and a timetable, the Grade Picker Edition asks "What grade is your child in?" first and shows only the classes that fit. Pure HTML, so there's no WordPress, no monthly fees and no coding required.

🔗 Live demo (English): https://a0955072107-bit.github.io/-/templates/tutor/en/
🔗 Live demo (中文): https://a0955072107-bit.github.io/-/templates/tutor/zh-TW/
🔗 Live demo (日本語): https://a0955072107-bit.github.io/-/templates/tutor/ja/
(Demo photos are for preview only and are not included. The template ships with drawn placeholders showing what photo goes where. "Stride Learning Center" and its teachers are fictional examples.)

Features
- Hero with a grade picker (elementary, middle school, high school, test prep) that filters the class list
- Classes and tuition in one list: grades, schedule, class size and price for each class. Add or remove a class without touching any script
- "How it works" in three steps: assessment, learning plan, weekly update
- Three teacher profiles with degree, years teaching and subjects
- This year's calendar: start dates, review weeks and the summer session
- A sample weekly update card and an FAQ (trial class, make-ups, refunds)
- Free assessment booking form (works with Formspree, no backend needed), plus hours, address and a Google Maps link
- Call and Book buttons fixed to the bottom on mobile
- SEO-ready with schema.org EducationalOrganization data
- Sample copy publishes no rankings and promises no scores

What you get
- English, Traditional Chinese, Simplified Chinese and Japanese versions with a built-in language switcher
- Step-by-step guide and commercial licence

Prefer a timetable-led layout for a cram school or enrichment classes? See our Tutoring School template, another style for the same trade: https://polyglotpages.gumroad.com/l/tutoring-school-template

──────────
補習班／課後輔導網站模板・補習班第二款「年級選擇器」。和我們的「補習班／才藝教室模板」不同風格：首屏先問「孩子現在幾年級」，點了只顯示適合的班別。
功能：年級選擇器（國小、國中、高中、升學考試）篩選班別、班別與學費清單（年級、上課時間、人數、費用，增減班別不用改程式）、「評估、學習計畫、每週回報」三步驟、三位老師簡介、年度行事曆、每週回報範例與常見問題（試聽、補課、退費）、免費評估預約表單（接 Formspree，不用後端）、營業時間／地址與 Google 地圖連結、手機版底部「撥打電話／預約免費評估」。
範例文案不放榜單、不保證分數。附英文、繁體、簡體、日文四種語言（網站內建語言切換）、中文教學、商業授權。
線上 Demo 的照片僅供示意，商品不含照片；「學行教室」與老師皆為虛構範例。
想要以課表為主的版型，可以看另一款風格的「補習班／才藝教室模板」。

[貼上「共用文字」]
```

---

## 5. 全套組合包（最後上）

> **11/28 更新（取代 11/27「維持 All 30」的註記）**：組合包現在是 **35 款**（原本 30 款＋dental＋tcm、canton、hair、tutor）。`bash scripts/package.sh` 產生的 `dist/all-templates-bundle.zip` 已經是 35 款。**價格不變**（$249）。要做兩件事：
> 1. 把新的 `all-templates-bundle.zip` **重新上傳到 Google Drive**（取代舊的 30 款檔；如果 Drive 連結會變，Gumroad 商品 Content 裡的連結也要換）。
> 2. 到 Gumroad 組合包商品頁，照下面「要改的 4 個地方」改文字。URL、價格、封面、標籤都不用動。
> 建議順序：先上架 dental 和這 4 款單品 → 換 Drive 的 zip → 最後改組合包文字，避免頁面寫 35 款、買家卻下載到 30 款。

Gumroad 可以建立 **Bundle**，把已上架的商品組合起來賣。如果後台沒有 Bundle，就另外上一個商品，上傳 `all-templates-bundle.zip`。

**要改的 4 個地方（30 → 35）**

| 欄位 | 現在（30 款） | 改成（35 款） |
|---|---|---|
| Name | `All 30 Business Website Templates Bundle (…)` | `All 35 Business Website Templates Bundle (…)`：只把 `30` 改成 `35`，括號裡的語言標示照線上現有的不動 |
| Summary | `All 30 one-page HTML website templates …` | `All 35 one-page HTML website templates for small businesses, each in English, 繁體中文, 简体中文 and 日本語 (6 also in Español). Buy once, no monthly fees.` |
| Description | 第 1 段 `All 30 templates … Save over 75% …`、中文段 `三十款…省超過七成五` | 整段換成下面的新 Description（`All 35`、`Save over 80%`、`三十五款…省超過八成`，並補上新行業） |
| Additional details | `Templates: 30 (one-page each)` | `Templates: 35 (one-page each)`（其他 4 行不變） |

折扣怎麼算：35 × $39 = **$1,365**，組合包 $249，省 $1,116，約 **81.8%**（約 1.8 折）。原本 30 款是 $1,170、省 78.7%，所以寫「over 75%」。現在寫「over 80%」成立；想保守一點，沿用「over 75%」也仍然正確。

- **Name**：`All 35 Business Website Templates Bundle (English + 繁體 + 简体)`（線上如果已照 11 節改成 `(EN + 中文 + 日本語)`，就維持那個括號，只改數字）
- **URL**：`website-templates-bundle`（不變）
- **Price**：`249`（不變；單買合計 $1,365，約 1.8 折；上市優惠 $199）
- **Cover**：用 Canva 把多張封面拼成一張（不用換）
- **Description**：
```
All 35 templates in one bundle, from restaurants, salons and clinics to acupuncture clinics, tutoring centers, campsites, florists and SaaS products. Save over 80% versus buying separately.

Perfect for freelancers who build sites for local businesses: one licence per template per website (see LICENSE.md).

──────────
三十五款模板一次帶走，從餐廳、美業、診所到中醫診所、補習班、露營、花店、軟體產品都有，比單買省超過八成。適合幫在地店家接案的人。

[貼上「共用文字」]
```
- **Summary**：`All 35 one-page HTML website templates for small businesses, each in English, 繁體中文, 简体中文 and 日本語 (6 also in Español). Buy once, no monthly fees.`
- **Additional details**（5 行）：`Templates: 35 (one-page each)`、`Format: HTML / CSS / JS`、`Languages: English, Traditional Chinese, Simplified Chinese, Japanese (6 with Spanish), switchable`、`Builder needed: None`、`Includes: step-by-step setup guide in each template`

> **11/28 已完成**：組合包已改成 35 款並確認下載的是新 zip；商店共 44 款。商店 Bio、Pinterest 看板說明裡的「30」由擴充功能另外改。

---

## 6. 上架後

- [ ] 每個商品頁都打開，確認 Demo 連結、封面、價格正確
- [ ] 自己用最低價測試購買一次（可以先設 100% 折扣碼），確認收得到 zip
- [ ] 把商店網址放到 IG、Threads、FB 接案社團、Dcard
- [ ] 第一個月可以用折扣碼（例如 `LAUNCH30`，打 7 折）衝第一批評價
- [ ] **Settings → Payments** 打開 **Purchasing power parity（購買力平價）**：拉美、東南亞、印度的買家會自動看到較低價格，歐美維持原價
- [ ] **Settings → Payments** 確認收款方式（PayPal 或銀行帳戶）已設定並驗證，第一筆款項才撥得下來

---

## 7. Motion 動態系列（第 2 週上架）

共用設定：Price `69`；Versions：`Standard license — 1 website`（$69）、`Extended license — up to 10 websites`（$189）；Cover／Thumbnail 用 `sales/covers/en/motion-<款式>-cover.png`／`-thumb.png`；Content 上傳 `dist/motion-*.zip`。

**共用說明開頭**（貼在每款說明最前面）：
```
Motion Edition: a premium, animated version built with native browser animation only. No GSAP, no Three.js, no libraries to license or update. Smooth on phones, and every animation switches off automatically for visitors who prefer reduced motion.
Motion 動態版：只用瀏覽器內建技術做的高級動畫網站，不依賴任何第三方函式庫，手機上也流暢；訪客開啟「減少動態效果」時會自動關閉動畫。
```

| 款式 | Name | URL | 主打動畫 |
|---|---|---|---|
| SaaS | `SaaS Launch Page — Motion Edition (English + 繁體 + 简体)` | `motion-saas-launch-template` | 手寫 WebGL 背景、固定產品畫面的捲動故事、橫向用例帶、價格切換動畫 |
| 作品集 | `Creative Portfolio — Motion Edition (English + 繁體 + 简体)` | `motion-creative-portfolio-template` | 名字逐字組合、跟隨游標的作品預覽、流線背景、橫向畫廊 |
| 餐廳 | `Fine Dining Restaurant — Motion Edition (English + 繁體 + 简体)` | `motion-fine-dining-template` | 炭火火星粒子、六道菜捲動故事、圓形展開、訂位微互動 |
| 婚禮 | `Wedding Website — Motion Edition with RSVP (English + 繁體 + 简体)` | `motion-wedding-template` | 信封開場、花瓣光點、自動描繪的故事路徑、翻牌倒數 |
| 豪宅 | `Luxury Residences — Motion Edition (English + 繁體 + 简体)` | `motion-luxury-residences-template` | 建築線稿自動描繪、固定平面圖導覽、房型切換、地圖標記落下 |

每款說明：共用開頭 → Demo 網址（`…/templates/motion/<款式>/en/`、`…/templates/motion/<款式>/zh-TW/`）→ 上表的動畫清單（用條列）→ What you get → 共用文字。

**Motion 全套組合包**：Name `All 5 Motion Edition Templates Bundle`，URL `motion-bundle`，Price `199`，Content 上傳 `dist/motion-bundle.zip`。

- **說明**（11/26 上架時的組法）：日文段落 → Motion 共用開頭 → 下面這段 → 第 9 節 Studio 段落 → 第 2 節共用文字。
```
Includes all 5 Motion Edition templates: SaaS Launch Page, Creative Portfolio, Fine Dining Restaurant, Wedding Website with RSVP, Luxury Residences.
包含全部 5 款 Motion 動態版模板：SaaS 發表頁、創意作品集、高級餐廳、婚禮網站（含 RSVP）、豪宅建案。
```
- **Summary**：`All 5 animated one-page HTML templates (Motion Edition), each in English, 繁體中文, 简体中文 and 日本語. Scroll animations without any library. Buy once, no monthly fees.`
- **Additional details**（5 行）：`Templates: 5 animated one-page templates`、`Format: HTML / CSS / JS (no libraries)`、`Languages: English, Traditional Chinese, Simplified Chinese, Japanese, switchable`、`Builder needed: None`、`Includes: step-by-step setup guide in each template`
- 價格目前用原價（Standard $199／Studio $349），沒用上市優惠價。

---

## 8. 三語店家網站代製（海外華人、新馬；訂金商品已上架）

研究結果：海外華人店家（美加澳的餐廳、診所、補習班，以及新加坡、馬來西亞的小店）天生需要「繁體＋簡體＋英文」網站，而市面上很少有人專做這件事。我們的模板本來就是三語，所以成本最低、最有優勢。

| 欄位 | 填入 |
|---|---|
| 商品類型 | 目前用「訂金＋尾款」兩個 Digital product（見第 3 節開頭）；手上有進行中的案子時不要換成 Commission |
| Name | `Trilingual Business Website (English + 繁體 + 简体) — Done For You 三語店家網站代製` |
| URL | `trilingual-website-service` |
| Price | 訂金商品：Standard deposit `150`／Pro deposit `250`；尾款商品：Standard `149`／Pro `249`（合計 $299／$499，跟第 3 節開頭一致；11/28 更正，原本誤寫成全額 299／499） |
| Cover | 用 `sales/covers/en/restaurant-cover.png`，之後再做專屬封面 |
| Summary | `A ready-to-launch website in English, Traditional and Simplified Chinese, with a language switcher. Ready for your review within 7 days after we receive your content.` |

**Versions（方案）**

| 名稱 | 價格 | 說明 |
|---|---|---|
| Standard | $299 | One-page site in 3 languages with switcher, your content and photos, call/map/booking/WhatsApp/WeChat buttons, contact form, connected to your own domain (bought in your name). 1 revision round. |
| Pro | $499 | Everything in Standard, plus a design tailored to your brand, trilingual text written for you, your photos edited for the web, your Google Business Profile tidied up, search basics set up, and 2 revision rounds. |

**Description**
```
Serve every customer in their own language. We build your business a website in English, Traditional Chinese and Simplified Chinese, with a one-tap language switcher. No monthly fees, no website builder subscription.

Made for restaurants, clinics, tutoring centres, salons, travel agencies and shops serving Chinese-speaking and English-speaking customers in the US, Canada, Australia, the UK, Singapore and Malaysia.

How it works
1. Buy the service and pick any of our templates.
2. We email you a short form. Send us your text in any one language.
3. We translate and adapt it into all three languages, build the site and send it for your review within 7 days after we receive your content.
4. You review it and request changes (1 round on Standard, 2 on Pro).

What's included
- English, 繁體中文 and 简体中文 versions with a language switcher
- Your text, photos, brand colours and opening hours
- Call, WhatsApp, WeChat, LINE, map and booking buttons
- Contact form sent to your email
- Connected to your own domain (bought in your name); free hosting, you own all the files
- Pro: design tailored to your brand, text written for you, photo editing, Google Business Profile, search basics

Payment: 50% to start, 50% after you approve the finished site. If we can't deliver, the deposit is refunded in full.

Not included: domain purchase fees, photography, legal review of medical or financial claims.

──────────
三語店家網站代製：一次做好英文、繁體、簡體三種語言，訪客點一下就能切換。沒有月費，檔案全部歸你。

適合：美國、加拿大、澳洲、英國、新加坡、馬來西亞的華人餐廳、診所、補習班、美容院、旅行社、商店。

流程：購買後選一款模板 → 填寫表單，只要給我們一種語言的文字 → 我們翻成三語，收到資料後 7 天內給你預覽 → 你確認並提出修改。

包含：三語版本與切換按鈕；你的文字、照片、品牌色、營業時間；電話、WhatsApp、微信、LINE、地圖、預約按鈕；表單寄到你的 Email；接上你自己的網域（用你的名字購買），主機免費，檔案全部歸你。Pro 方案另含：依品牌調整設計、代寫三語文字、照片修圖、整理 Google 商家檔案、搜尋基本設定。
不包含：網域費用、拍攝照片、醫療或金融宣傳用語的法律審查。

[貼上「共用文字」]
```

**Receipt**
```
Thanks! Within 1 business day we'll email you a short form. Your site is ready for your review within 7 days after we receive your content.
感謝購買！我們會在 1 個工作天內寄表單給你，收到資料後 7 天內給你預覽。
```

> **翻譯品質**：簡體版用 OpenCC 轉換後，要人工檢查用詞（例如「影片→视频」「網路→网络」「軟體→软件」）。新馬客人常用簡體，美加澳的老一輩客人常用繁體，所以兩種都要給。

### 在哪裡曝光
| 管道 | 怎麼做 |
|---|---|
| 小紅書 | 帳號簡介寫「幫海外華人店家做繁簡英三語網站」，每週 2～3 篇：前後對比、省月費計算、各行業範例。先經營 3 個月自然內容。 |
| Facebook 社團 | 多倫多、溫哥華、西雅圖、灣區、雪梨、墨爾本的華人商家社團，用「分享案例」的方式發文，不要直接貼廣告。 |
| 華人分類廣告 | 51.ca、溫哥華港灣、華人生活網、Carousell（新馬）。 |
| Google 地圖主動開發 | 搜尋「Chinese restaurant Toronto」等，找有評價、沒網站的店，私訊附上用他們店名做好的三語 Demo。 |

---

## 9. 工作室無限授權（Studio License）

給接案者和小型設計公司：同一款模板可以做**不限數量**的客戶網站。研究顯示這類買家願意付較高價格，而且會重複購買。

- 在**全套組合包**加一個 Version：`Studio license — unlimited client websites`，價格 `$399`（上市優惠 $299）。
- 單款模板不用加 Studio 版，維持 Standard $39／Extended $119。
- Motion 全套組合包也加一個 Version：`Studio license — unlimited client websites`，價格 `$349`。
- 條款寫在 `LICENSE.md`／`授權條款.md` 的「工作室授權」段落，已更新。

說明裡加一段：
```
Studio license: build unlimited client websites with every template in the bundle. Ideal for freelancers and small agencies. You still may not resell the template files themselves.
工作室授權：組合包裡的每一款，都可以用在不限數量的客戶網站。適合接案者和小型設計公司。仍然不可轉售模板檔案本身。
```

---

## 10. 稅務與法規提醒

- **Gumroad 是代收代付的賣方（merchant of record）**：歐盟增值稅、英國 VAT、美國各州銷售稅、澳洲 GST 都由 Gumroad 代收代繳，你不用另外申報這些國家的稅。
- **台灣的所得稅**：Gumroad 撥給你的錢是你的收入。金額變大後，請詢問會計師要用個人執行業務所得申報，或是辦理商業登記。
- **買家網站的法規**：模板已經做到下列幾點，說明文件也有教買家怎麼處理：
  - 地圖用「開啟 Google 地圖」連結，不內嵌 iframe，所以不會在訪客同意前載入 Google 的追蹤。
  - 想完全符合 GDPR 的歐洲買家，可以把 Google Fonts 改成自架字型（GUIDE.md 第 10 節有步驟）。
  - 附上一份隱私權政策範本（`PRIVACY-TEMPLATE.md`／`隱私權政策範本.md`）。德國買家需要另外加上 Impressum（業者資訊頁）。

---

## 11. 日文版與西班牙文版（已放進同一個 zip，不用另外上架）

每款的 zip 已經包含 `ja/`（全部 35 款）和 `es/`（6 款：餐廳、美業、健身、房仲、清潔、水電）。不用新增商品，只要**修改既有商品**：

### 名稱
- 35 款全部：把名稱結尾的 `(English + 繁體 + 简体)` 改成 `(EN + 中文 + 日本語)`。
- 有西文的 6 款：改成 `(EN + 中文 + 日本語 + Español)`。

### 說明最前面加一段日文
```
日本語版つき：テキスト・住所・価格（税込表示）・LINE ボタンまで日本向けに作り直した日本語版が入っています。ガイドとライセンスも日本語で同梱。月額費用なし、買い切りです。
```

### 6 款加一段西文
```
Incluye versión en español: textos, precios, WhatsApp y datos de ejemplo adaptados para negocios en Latinoamérica y EE. UU. Guía y licencia en español. Pago único, sin mensualidades.
```

### 標籤（Tags）
- 日文：`ホームページ テンプレート`、`LP テンプレート`、`HTML テンプレート`、`店舗 ホームページ`
- 西文：`plantilla web`、`plantilla html`、`página web negocio`、`landing page español`

### 日本市場在哪裡曝光
| 管道 | 怎麼做 |
|---|---|
| ココナラ（coconala） | 開「ホームページ制作（テンプレート使用・日本語対応）」服務，¥30,000〜，連到 Gumroad 作品。這是日本小店家找人做網站最常用的平台。 |
| note | 每月寫 1〜2 篇「個人店のホームページを月額0円で作る方法」，文末放 Gumroad 連結。 |
| X（Twitter）／Instagram | 發 Demo 截圖與 15 秒滑動影片，hashtag `#ホームページ制作` `#個人店`。 |
| Pinterest | 每款加 1 張日文直式圖。 |

### 西語市場（測試 60 天）
- 每週發 2 張西文 Pinterest 圖、1 支短影片（YouTube Shorts／Instagram Reels，西文字幕）。
- Workana 開一個「Diseño de página web para negocios」服務，$199 起。
- 60 天後看數據：6 款有西文的模板銷量如果比其他款高 30% 以上，再把其餘 29 款也做西文版。

---

## 12. 網站維護月費「Website Care」（11/24 改成 11/30 上架、12/1 開始賣）

給已經做好網站的客人（客製案、三語代製），也賣給自己架好模板、但不想自己改的買家。這是**每月固定收入**的來源。

| 欄位 | 填入 |
|---|---|
| 商品類型 | **Membership**（每月自動扣款，可隨時取消） |
| Name | `Website Care — Monthly Updates & Hosting Help 網站維護月費` |
| URL | `website-care` |
| Price | `49`／月（11/26 決定：單一方案 $49，取代原本 $19／$29 兩個 tier） |

**包含（$49/月）**
- 每月最多 3 次小修改（營業時間、菜單、價格、文字、換照片），其中 1 次可以是季節性更新（節日營業時間、新菜單）
- Google 商家檔案代管：營業時間、照片、公告跟網站同步
- 每月檢查網站上線、表單、電話和地圖連結
- 網域續約提醒

**Description**
```
Your website and Google profile, kept up to date, without you touching any code.

Send us an email when something changes: new hours, a new dish, a price update, a holiday closure. We update your website and your Google Business Profile, usually within 2 business days.

Website Care, $49/month
- Up to 3 small updates a month (text, hours, menu, prices, photos), including seasonal updates
- Your Google Business Profile kept in sync with your site (hours, photos, posts)
- Monthly check that your site, forms, phone and map links work
- Domain renewal reminders

Cancel any time. Your site, domain and files always stay yours.

──────────
網站維護月費 $49：有任何變動寄信給我們（營業時間、新菜色、價格、公休），通常 2 個工作天內更新網站和 Google 商家檔案。隨時可以取消，網站、網域和檔案永遠是你的。
```

**規則**
- 網域和主機都用**客人自己的帳號**，我們只當協作者。客人取消維護，網站照常運作。
- 「小修改」＝ 15 分鐘內能完成的修改。超過的另外報價。
- 當月沒用完的次數不累積。

**怎麼賣**
- 客製案、三語代製交件時，**第 1 個月免費**，之後客人自己決定要不要續。
- 交件信裡附上維護月費連結（`sales/交付流程.md` 的交接範本已加上）。
- 目標：每 3 個客製客人有 1 個續訂。

---

## 13. 介紹獎勵（口碑轉介紹）

客人介紹別的店家來成交，**介紹人得到 $50**，或維護月費免費 3 個月（二選一）。
- 交件信和維護月費的每月更新信裡都提一次。
- 用 Gumroad **Affiliates** 功能：給介紹人一個專屬連結，成交後自動分潤。不想用連結的客人，就請新客人下單時寫上介紹人的店名，你手動發獎勵。
