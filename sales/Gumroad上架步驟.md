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

| 模板 | 英文 Demo | 中文 Demo |
|---|---|---|
| 餐廳 | `https://a0955072107-bit.github.io/-/templates/en/restaurant/` | `https://a0955072107-bit.github.io/-/templates/restaurant/` |
| 美容 | `…/templates/en/beauty/` | `…/templates/beauty/` |
| 健身 | `…/templates/en/fitness/` | `…/templates/fitness/` |
| 診所 | `…/templates/en/clinic/` | `…/templates/clinic/` |
| 事務所 | `…/templates/en/consulting/` | `…/templates/consulting/` |
| 工作室 | `…/templates/en/studio/` | `…/templates/studio/` |
| 民宿 | `…/templates/en/bnb/` | `…/templates/bnb/` |
| 房仲 | `…/templates/en/realestate/` | `…/templates/realestate/` |
| 婚禮 | `…/templates/en/wedding/` | `…/templates/wedding/` |
| 攝影師 | `…/templates/en/photographer/` | `…/templates/photographer/` |
| 寵物 | `…/templates/en/pet/` | `…/templates/pet/` |
| 補習班 | `…/templates/en/education/` | `…/templates/education/` |
| 室內設計 | `…/templates/en/interior/` | `…/templates/interior/` |
| 烘焙 | `…/templates/en/bakery/` | `…/templates/bakery/` |
| 手搖飲 | `…/templates/en/tea/` | `…/templates/tea/` |
| 汽車 | `…/templates/en/auto/` | `…/templates/auto/` |
| 清潔 | `…/templates/en/cleaning/` | `…/templates/cleaning/` |
| 花店 | `…/templates/en/florist/` | `…/templates/florist/` |
| 瑜珈 | `…/templates/en/yoga/` | `…/templates/yoga/` |
| 露營 | `…/templates/en/camping/` | `…/templates/camping/` |
| 個人品牌 | `…/templates/en/freelancer/` | `…/templates/freelancer/` |
| App／SaaS | `…/templates/en/saas/` | `…/templates/saas/` |

上架前每個連結都打開確認一次。

### 0-2. 商店設定（Settings → Profile）
- **Name**：取一個品牌名，例如 `Hearth Templates` 或你自己的工作室名稱。
- **Bio**（直接貼上）：
  ```
  Clean, fast one-page website templates for small businesses. Pure HTML, no monthly fees, English + 繁體中文 included. Need it customised? We can build it for you.
  給小店家的一頁式網站模板，純 HTML、免月費、附中英文版。需要客製？我們幫你做好。
  ```
- **頭像**：用 Canva 做一個簡單的 logo。
- **Payouts**：設定收款方式，台灣通常用 PayPal 或銀行帳戶，依後台可用選項為準。

### 0-3. 打包檔案
```bash
bash scripts/package.sh
```
`dist/` 會產生 22 個單款 zip 和 1 個全套 zip，每包都附英文版和繁體中文版。

---

## 1. 上架順序

1. 先上 **網站客製服務**。其他商品的說明會連到它，所以先上才拿得到網址。
2. 再上 22 款單一模板（建議先上最有把握的 6 款，其他陸續上，讓商店持續有新品）。
3. 最後上 **全套組合包**（Bundle）。

---

## 2. 共用文字（每個模板商品都貼在說明最後）

```
──────────
✨ Want it set up for your business?
Don't have time to edit it yourself? We'll customise this template with your text, photos, colours, booking links and domain, ready to launch.
👉 See our Website Customization Service: [貼上客製服務商品網址]

✨ 想要直接幫你改好？
沒時間自己改嗎？我們可以把這個模板改成你店家專屬的網站：換上你的文字、照片、品牌色、預約連結，並設定好網域，直接上線。
👉 網站客製服務：[貼上客製服務商品網址]
```

---

## 3. 網站客製服務（先上這個）

| 欄位 | 填入 |
|---|---|
| 商品類型 | 一般 **Digital product**。若後台有 **Commission**（委託，先收訂金）或 **Call**（預約通話）類型，也可以改用 |
| Name | `Website Customization Service — We Build Your Business Site 網站客製服務` |
| URL | `website-customization` |
| Price | `249`（Basic），另外用 **Versions** 加 `Plus $449` |
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

Not included: copywriting from scratch, photography, domain purchase fees.

Questions before buying? Message us through Gumroad.

──────────
網站客製服務：喜歡我們的模板，但沒時間自己改？交給我們。

流程
1. 購買服務，並選擇任一款模板。
2. 我們會寄一份簡短表單給你，請你填寫店名、文字、照片、品牌色、連結。
3. 收到資料後，通常 5 個工作天內完成並上線。
4. 你確認後可以提出修改（Basic 1 次、Plus 2 次）。

包含：換上你的內容、照片、品牌色；電話、LINE、地圖、預約按鈕串接；表單串接到你的 Email；部署到免費主機。Plus 方案另外包含自訂網域設定，以及多做一個區塊或頁面。
不包含：從零撰寫文案、拍攝照片、網域購買費用。

購買前有問題，歡迎透過 Gumroad 私訊。
```

**Receipt（購買後訊息）**
```
Thanks! We'll email you within 1 business day with a short form to collect your content.
感謝購買！我們會在 1 個工作天內寄表單給你，用來收集網站內容。
```

> 交件時間和價格請依你實際能接的量調整。初期可以先低價接幾單，累積作品和評價。

---

## 4. 單一模板（22 款）

每款的共用設定：

| 欄位 | 填入 |
|---|---|
| Price | `24` |
| Versions | `Standard license — 1 website`（$24）、`Extended license — up to 10 websites`（$79） |
| Content | 上傳 `dist/` 裡對應的 zip |
| Thumbnail | 正方形 600×600 以上，可以在 Canva 用「調整尺寸」從封面另存 |
| Additional details | `Format: HTML/CSS/JS` · `Languages: English, 繁體中文` · `Pages: 1 (one-page)` · `Builder needed: None` |
| Receipt | 見下方共用 Receipt |
| Tags | 見各商品 |

**共用 Receipt**
```
Thanks for your purchase! Unzip the file and open GUIDE.md (English) or 使用說明.md (中文) to get started.
Want us to set it up for you? See our Website Customization Service.
感謝購買！解壓縮後，打開 使用說明.md（中文）或 GUIDE.md（英文）開始使用。需要我們幫你改好嗎？歡迎參考「網站客製服務」。
```

**共用 Summary（You'll get）**
```
A one-page HTML website template in English + 繁體中文, a step-by-step setup guide, and a commercial licence.
```

### 4-1. 餐廳／咖啡廳

- **Name**：`Restaurant & Café Website Template (English + 繁體中文) — One-Page HTML`
- **URL**：`restaurant-website-template`
- **Cover**：`sales/covers/restaurant-cover.png`，另外加上 `sales/screenshots/restaurant-desktop.jpg`、`restaurant-mobile.jpg`
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
- English and Traditional Chinese versions
- Step-by-step guide: edit text, add photos, connect the form, publish for free
- Commercial licence (1 website with Standard)

──────────
餐廳／咖啡廳一頁式網站模板，純 HTML，免 WordPress、免月費，不用會寫程式。

功能：分頁菜單（價格、招牌、素食標籤）、依營業時間自動顯示「營業中／休息中」、線上訂位表單、電話／LINE／地圖按鈕、手機版底部「立即訂位」按鈕、環境照片、顧客好評、營業時間與交通資訊、Google 結構化資料、一處改色全站換色。
內容：英文版與繁體中文版、中文使用教學、商業授權。

[貼上「共用文字」]
```

### 4-2. 美容美髮／美甲

- **Name**：`Hair & Nail Salon Website Template (English + 繁體中文) — One-Page HTML`
- **URL**：`salon-website-template`
- **Cover**：`beauty-cover.png` + `beauty-desktop.jpg` + `beauty-mobile.jpg`
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
- English and Traditional Chinese versions
- Step-by-step guide and commercial licence

──────────
美容美髮／美甲一頁式網站模板。功能：分類價目表、設計師介紹與指定預約、可篩選作品集、預約流程、常見問題、LINE 預約按鈕、手機版底部預約列、Google 結構化資料。附英文版與繁體中文版、中文教學、商業授權。

[貼上「共用文字」]
```

### 4-3. 健身房／私人教練

- **Name**：`Gym & Personal Training Website Template (English + 繁體中文) — One-Page HTML`
- **URL**：`gym-website-template`
- **Cover**：`fitness-cover.png` + `fitness-desktop.jpg` + `fitness-mobile.jpg`
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
- English and Traditional Chinese versions
- Step-by-step guide and commercial licence

──────────
健身工作室一頁式網站模板。功能：課程介紹、彩色每週課表、教練團隊、月繳／年繳切換方案價格、學員見證、免費體驗表單、手機版底部預約按鈕、Google 結構化資料。附英文版與繁體中文版、中文教學、商業授權。

[貼上「共用文字」]
```

### 4-4. 診所（牙醫，可改其他科別）

- **Name**：`Dental & Medical Clinic Website Template (English + 繁體中文) — One-Page HTML`
- **URL**：`clinic-website-template`
- **Cover**：`clinic-cover.png` + `clinic-desktop.jpg` + `clinic-mobile.jpg`
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
- English and Traditional Chinese versions
- Step-by-step guide and commercial licence

──────────
診所一頁式網站模板（牙醫，可改其他科別）。功能：首屏自動顯示今日門診、門診時間表自動標示今天、診療項目、醫師團隊、就診須知與常見問題、手機版底部「撥打電話／線上預約」。文案遵守醫療廣告法、不誇大。附英文版與繁體中文版、中文教學、商業授權。

[貼上「共用文字」]
```

### 4-5. 會計師／律師／顧問事務所

- **Name**：`Law, Accounting & Consulting Firm Website Template (English + 繁體中文)`
- **URL**：`consulting-firm-website-template`
- **Cover**：`consulting-cover.png` + `consulting-desktop.jpg` + `consulting-mobile.jpg`
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
- English and Traditional Chinese versions
- Step-by-step guide and commercial licence

──────────
會計師／律師／顧問事務所一頁式網站模板。功能：服務領域、選擇我們的理由、服務流程、專業團隊、客戶見證、常見問題、預約諮詢表單、數字動畫、手機版底部預約按鈕、Google 結構化資料。附英文版與繁體中文版、中文教學、商業授權。

[貼上「共用文字」]
```

### 4-6. 設計工作室／作品集

- **Name**：`Design Studio & Portfolio Website Template (English + 繁體中文)`
- **URL**：`studio-portfolio-template`
- **Cover**：還沒有封面，需要用 Canva 依同樣版型做一張
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
- English and Traditional Chinese versions
- Step-by-step guide and commercial licence

──────────
設計工作室／作品集一頁式網站模板。功能：標題逐行浮現、捲動動畫、服務項目、精選作品、專案洽詢表單、自動深色模式。附英文版與繁體中文版、中文教學、商業授權。

[貼上「共用文字」]
```

### 4-7. 民宿／B&B

- **Name**：`B&B & Guesthouse Website Template (English + 繁體中文) — One-Page HTML`
- **URL**：`bnb-guesthouse-template`
- **Cover**：還沒做，Canva 依同樣版型做一張
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
- English and Traditional Chinese versions
- Step-by-step guide and commercial licence

──────────
民宿／B&B 一頁式網站模板。功能：房型與平假日價格、自動計算住宿晚數的訂房表單、住宿特色、周邊景點、入住須知、住客評價、手機版底部訂房按鈕、Google 結構化資料。附英文版與繁體中文版、中文教學、商業授權。

[貼上「共用文字」]
```

### 4-8. 房仲／不動產

- **Name**：`Real Estate Agent Website Template (English + 繁體中文) — One-Page HTML`
- **URL**：`real-estate-website-template`
- **Cover**：還沒做，Canva 依同樣版型做一張
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
- English and Traditional Chinese versions
- Step-by-step guide and commercial licence

──────────
房仲／不動產一頁式網站模板。功能：可即時篩選的物件搜尋、物件卡片、服務項目、成交實績、經紀人介紹、買房流程、預約看屋表單、手機版底部預約按鈕、Google 結構化資料。附英文版與繁體中文版、中文教學、商業授權。

[貼上「共用文字」]
```

### 4-9. 婚禮／活動

- **Name**：`Wedding Website Template with RSVP & Countdown (English + 繁體中文)`
- **URL**：`wedding-website-template`
- **Cover**：還沒做，Canva 依同樣版型做一張
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
- English and Traditional Chinese versions
- Step-by-step guide and commercial licence

──────────
婚禮網站模板（也適合活動）。功能：倒數計時、我們的故事、典禮與宴客資訊、當天流程、交通住宿、相簿、RSVP 出席回覆表單、Google 結構化資料。附英文版與繁體中文版、中文教學、商業授權。

[貼上「共用文字」]
```

### 4-10. 攝影師

- **Name**：`Photographer Portfolio Website Template (English + 繁體中文) — One-Page HTML`
- **URL**：`photographer-portfolio-template`
- **Cover**：還沒做，Canva 依同樣版型做一張
- **Tags**：`photography website`, `photographer portfolio`, `portfolio template`, `html template`, `website template`
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
- English and Traditional Chinese versions
- Step-by-step guide and commercial licence

──────────
攝影師作品集網站模板。功能：可篩選的作品集與燈箱看大圖、拍攝方案與價格、拍攝流程、關於我、客戶評價、預約表單、手機版底部預約按鈕。附英文版與繁體中文版、中文教學、商業授權。

[貼上「共用文字」]
```

### 4-11. 寵物美容／旅館

- **Name**：`Pet Grooming & Daycare Website Template (English + 繁體中文)`
- **URL**：`pet-grooming-template`
- **Cover**：還沒做，Canva 依同樣版型做一張
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
- English and Traditional Chinese versions
- Step-by-step guide and commercial licence

──────────
寵物美容／旅館網站模板。功能：依體型分頁的價目表、服務項目、安心措施、美容師介紹、美容前後對比、預約須知、預約表單、Google 結構化資料。附英文版與繁體中文版、中文教學、商業授權。

[貼上「共用文字」]
```

### 4-12. 補習班／才藝教室

- **Name**：`Tutoring Center & Classes Website Template (English + 繁體中文)`
- **URL**：`tutoring-school-template`
- **Cover**：還沒做，Canva 依同樣版型做一張
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
- English and Traditional Chinese versions
- Step-by-step guide and commercial licence

──────────
補習班／才藝教室網站模板。功能：依年級分頁的課程、教學特色、師資介紹、每週課表、學生成果、家長評價、免費試聽預約表單、Google 結構化資料。附英文版與繁體中文版、中文教學、商業授權。

[貼上「共用文字」]
```

### 4-13. 室內設計

- **Name**：`Interior Design Studio Website Template (English + 繁體中文)`
- **URL**：`interior-design-template`
- **Cover**：還沒做，Canva 依同樣版型做一張
- **Tags**：`interior design website`, `renovation website`, `architect portfolio`, `html template`, `website template`
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
- English and Traditional Chinese versions
- Step-by-step guide and commercial licence

──────────
室內設計網站模板。功能：可篩選的案例、裝修前後對比滑桿、服務流程、收費方式、設計團隊、客戶評價、預約丈量表單、Google 結構化資料。附英文版與繁體中文版、中文教學、商業授權。

[貼上「共用文字」]
```

### 4-14. 烘焙／甜點店

- **Name**：`Bakery & Dessert Shop Website Template with Pre-orders (English + 繁體中文)`
- **URL**：`bakery-website-template`
- **Cover**：還沒做，Canva 依同樣版型做一張
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
- English and Traditional Chinese versions
- Step-by-step guide and commercial licence

──────────
烘焙／甜點店網站模板。功能：本週出爐表、麵包／蛋糕／禮盒分頁、自動計算金額的預訂、客製蛋糕說明、取貨預訂表單、Google 結構化資料。附英文版與繁體中文版、中文教學、商業授權。

[貼上「共用文字」]
```

### 4-15. 手搖飲／茶飲店

- **Name**：`Bubble Tea Shop Website Template (English + 繁體中文) — One-Page HTML`
- **URL**：`bubble-tea-shop-template`
- **Cover**：還沒做，Canva 依同樣版型做一張
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
- English and Traditional Chinese versions
- Step-by-step guide and commercial licence

──────────
手搖飲／茶飲店網站模板。功能：分頁菜單、甜度冰塊配料客製試算、多門市據點、外送平台按鈕、集點說明、加盟洽詢表單。附英文版與繁體中文版、中文教學、商業授權。

[貼上「共用文字」]
```

### 4-16. 汽車美容／保養廠

- **Name**：`Car Detailing & Auto Repair Website Template (English + 繁體中文)`
- **URL**：`auto-care-garage-template`
- **Cover**：還沒做，Canva 依同樣版型做一張
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
- English and Traditional Chinese versions
- Step-by-step guide and commercial licence

──────────
汽車美容／保養廠網站模板。功能：依車型分頁的價目表、保養里程提醒、施工前後對比、技師團隊、線上預約表單、Google 結構化資料。附英文版與繁體中文版、中文教學、商業授權。

[貼上「共用文字」]
```

### 4-17. 居家清潔

- **Name**：`Home Cleaning Service Website Template with Instant Quote (English + 繁體中文)`
- **URL**：`home-cleaning-template`
- **Cover**：還沒做，Canva 依同樣版型做一張
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
- English and Traditional Chinese versions
- Step-by-step guide and commercial licence

──────────
居家清潔網站模板。功能：即時估價計算機、各空間清潔項目、服務流程、服務區域、評價、自動帶入估價的預約表單。附英文版與繁體中文版、中文教學、商業授權。

[貼上「共用文字」]
```

### 4-18. 花店

- **Name**：`Florist Website Template (English + 繁體中文) — One-Page HTML`
- **URL**：`florist-template`
- **Cover**：還沒做，Canva 依同樣版型做一張
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
- English and Traditional Chinese versions
- Step-by-step guide and commercial licence

──────────
花店網站模板。功能：花束分頁與價格、配送日期判斷（當日截止時間）、每月訂花方案、婚禮活動花藝、花卡字數提示、訂購表單。附英文版與繁體中文版、中文教學、商業授權。

[貼上「共用文字」]
```

### 4-19. 瑜珈／皮拉提斯

- **Name**：`Yoga & Pilates Studio Website Template (English + 繁體中文)`
- **URL**：`yoga-pilates-template`
- **Cover**：還沒做，Canva 依同樣版型做一張
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
- English and Traditional Chinese versions
- Step-by-step guide and commercial licence

──────────
瑜珈／皮拉提斯網站模板。功能：依星期切換的課表（自動選今天）、課程類型、體驗與課程方案、老師介紹、空間介紹、體驗課預約。附英文版與繁體中文版、中文教學、商業授權。

[貼上「共用文字」]
```

### 4-20. 露營區／豪華露營

- **Name**：`Campsite & Glamping Website Template (English + 繁體中文)`
- **URL**：`campsite-glamping-template`
- **Cover**：還沒做，Canva 依同樣版型做一張
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
- English and Traditional Chinese versions
- Step-by-step guide and commercial licence

──────────
露營區／豪華露營網站模板。功能：營位類型與平假日價格、可點選的營地地圖、住宿費用試算、營地設施、營地規範、裝備建議、訂位表單。附英文版與繁體中文版、中文教學、商業授權。

[貼上「共用文字」]
```

### 4-21. 個人品牌／自由工作者

- **Name**：`Freelancer Portfolio & Résumé Website Template (English + 繁體中文)`
- **URL**：`freelancer-portfolio-template`
- **Cover**：還沒做，Canva 依同樣版型做一張
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
- English and Traditional Chinese versions
- Step-by-step guide and commercial licence

──────────
個人品牌／自由工作者網站模板。功能：作品集、服務與起價、技能與經歷、履歷下載、合作流程、深淺色模式切換、合作洽談表單。附英文版與繁體中文版、中文教學、商業授權。

[貼上「共用文字」]
```

### 4-22. App／軟體產品登陸頁

- **Name**：`SaaS & App Landing Page Template (English + 繁體中文) — One-Page HTML`
- **URL**：`app-saas-landing-template`
- **Cover**：還沒做，Canva 依同樣版型做一張
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
- English and Traditional Chinese versions
- Step-by-step guide and commercial licence

──────────
App／軟體產品登陸頁模板。功能：產品介面展示、功能介紹、使用流程、月繳／年繳切換的方案價格、功能比較表、Email 訂閱。附英文版與繁體中文版、中文教學、商業授權。

[貼上「共用文字」]
```

---

## 5. 全套組合包（最後上）

Gumroad 可以建立 **Bundle**，把已上架的商品組合起來賣。如果後台沒有 Bundle，就另外上一個商品，上傳 `all-templates-bundle.zip`。

- **Name**：`All 22 Business Website Templates Bundle (English + 繁體中文)`
- **URL**：`website-templates-bundle`
- **Price**：`129`（單買合計 $528，約打 2.5 折）
- **Cover**：用 Canva 把多張封面拼成一張
- **Description**：
```
All 22 templates in one bundle, from restaurants, salons and clinics to campsites, florists and SaaS products. Save over 75% versus buying separately.

Perfect for freelancers who build sites for local businesses: one licence per template per website (see LICENSE.md).

──────────
二十二款模板一次帶走，從餐廳、美業、診所到露營、花店、軟體產品都有，比單買省超過七成五。適合幫在地店家接案的人。

[貼上「共用文字」]
```

---

## 6. 上架後

- [ ] 每個商品頁都打開，確認 Demo 連結、封面、價格正確
- [ ] 自己用最低價測試購買一次（可以先設 100% 折扣碼），確認收得到 zip
- [ ] 把商店網址放到 IG、Threads、FB 接案社團、Dcard
- [ ] 第一個月可以用折扣碼（例如 `LAUNCH30`，打 7 折）衝第一批評價
