# 12 月批次：四款新模板設計計畫（2026-11-27 定稿）

> 內部用，打包時不會放進商品。使用者 11/27 指示「繼續做模板、多做一些」，並選擇「直接照設計總監推薦做」。
> 依據：開發名單需求（牙醫 48、中醫 23、美髮 22、補習班 11）。四款都要：繁中、英、簡中、日；附預覽照片；虛構一律標記；高級感（DESIGN.md 2.9）。
> 型錄已有很多綠色系與奶油底，四款刻意分開：丹砂紅、青花藍、黑白＋霧紫、石墨＋鉛筆黃。

共通：
- 英文版以美國華人小店為情境（虛構美國地址、(555) 電話、WhatsApp）；日文版照 SPEC。
- 每個圖片位置用獨立 class，佔位圖要畫出「放什麼照片」的構圖。
- 只有一個記憶點，其餘安靜；全頁只有首屏一次進場動畫。

---

## 1. tcm：中醫／針灸診所（新行業）

- **店家（虛構）**：本草堂中醫診所（台北大同區）／Bencao Acupuncture & Herbs（虛構加州地址）／本草堂鍼灸漢方院。
- **對象與任務**：肩頸痠痛、失眠、調理體質的成人與長輩；主要動作是電話／LINE 預約初診。
- **記憶點**：首屏的「百子櫃」（中藥櫃抽屜牆）。避開太極、龍、書法字、紅金配色這些套路。
- **配色**：灰白紙 `#F2F1ED`（頁面底）／表面 `#FAF9F6`／墨 `#1F1D1B`（文字）／深丹砂 `#7A2E24`（品牌、按鈕；比赤陶深、偏棗紅）／次要文字 `#5C5650`／細線 `#DAD6CE`／艾草灰 `#8A9379`（只用在佔位圖）。
- **字體**：標題 Libre Caslon Text 400（英）＋ Noto Serif TC 500；內文 Public Sans 400/500 ＋ Noto Sans TC；日文 Shippori Mincho 500 ＋ Zen Kaku Gothic New。
- **版面**：
  1. 首屏：左文字（標題、一句說明、預約＋電話），右邊百子櫃大圖出血到右緣（手機圖在下、滿寬）。
  2. 看診流程：問診 → 把脈與望舌 → 說明調理方向 → 治療（真的是順序，可編號）。
  3. 診療項目：針灸、中藥（科學中藥／水煎藥）、傷科推拿、拔罐與艾灸；細線清單，標健保／自費。
  4. 常見求診原因：兩欄文字索引（肩頸腰背痠痛、失眠、過敏與鼻子不適、腸胃不適、經期不適、體質調理…），用「許多人因為這些原因來看診」的中性說法，**不寫療效**。
  5. 醫師：2 位（4:5 直角相框）＋看診時段。
  6. 門診時間表＋今日門診（同 dental 的 JS 做法：時區常數、掛號截止、每分鐘更新）。
  7. 初診須知＋常見問題（健保、針灸會不會痛、服藥方式、孕婦可否看診→請先告知醫師）。
  8. 交通＋地圖。
- **法規**：繁中遵守醫療法（不寫療效、見證、優惠）；英文版避免 cure／treats 等療效字眼，用 "people often visit us for…"，並加註解提醒買家各州規定。
- **照片清單**（預覽用）：
  | class | 比例 | 內容 | 英文提示詞重點 |
  |---|---|---|---|
  | `.img-hero` | 4:5 | 百子櫃抽屜牆，前景一只銅秤與幾味藥材，側光 | traditional Chinese herbal medicine cabinet wall with many small wooden drawers, brass scale and dried herbs in foreground, soft side light, calm, no text, no people |
  | `.img-doc1` | 4:5 | 50 多歲女中醫師，白袍 | East Asian female TCM doctor in her fifties, white coat, warm neutral clinic background, fictional person |
  | `.img-doc2` | 4:5 | 40 歲左右男中醫師 | East Asian male TCM doctor around forty, white coat, same style, fictional person |
  | `.img-herbs` | 3:2 | 俯拍幾碟藥材（枸杞、黃耆、陳皮）在灰白紙上 | overhead dried Chinese herbs in small ceramic dishes on pale paper surface, muted colors |
  | `.img-room` | 3:2 | 安靜的針灸診療室：診療床、白布、小茶几，無人 | calm acupuncture treatment room, treatment bed with white linen, small side table, soft daylight, no people |

## 2. canton：粵菜館（餐廳第二款）

- **店家（虛構）**：瑞記粵菜（台北中山區）／Sui Kee Cantonese Kitchen（虛構紐約法拉盛地址）／瑞記広東料理。
- **對象與任務**：家庭聚餐、外帶的客人；主要動作是「線上點外帶」與訂位。跟日和食堂（照片首屏、訂位為主）不同：這款是**菜單即首屏、外帶為主**。
- **記憶點**：首屏的「今日招牌」菜牌（三道招牌菜＋價格，像餐館牆上的菜牌），旁邊一張燒臘照片。
- **配色（青花瓷）**：白瓷 `#F7F8FA`（頁面底）／表面 `#FFFFFF` 近似但帶藍調 `#FCFDFE`／墨藍黑 `#16203A`（文字）／青花藍 `#1F3F8F`（品牌、按鈕）／次要文字 `#4B5670`／細線 `#D9DEE8`／印章朱紅 `#C0321F`（只用在「招牌」印章標記與營業中，≤5%，旁邊一定有文字）。避開黑底燙金與大紅配金。
- **字體**：標題 DM Serif Display 400（英）＋ Noto Serif TC 500；內文 DM Sans 400/500 ＋ Noto Sans TC；日文 Shippori Mincho ＋ Zen Kaku Gothic New。
- **版面**：
  1. 首屏：左邊標題＋一句說明＋「線上點外帶」（主要）與「訂位」；右邊「今日招牌」菜牌（3 道，中英對照菜名＋價格）＋燒臘照片；營業狀態（JS，同日和食堂做法）。
  2. 菜單：分頁（燒臘、小炒、飯麵、湯與煲、點心甜品），每道菜「中文菜名＋英文菜名＋一句說明＋價格」，辣／素標記用文字；無 JS 時全部展開並有小標。
  3. 午間特餐：時段與價格的一條橫幅（細線表格）。
  4. 宴席與外燴：包廂人數、合菜套餐（2 種）、外燴托盤；一張大圖。
  5. 營業時間與位置（今天標示）＋外帶取餐說明。
  6. 訂位／外帶表單（Formspree；外帶可填取餐時間）。
- **照片清單**：
  | class | 比例 | 內容 | 英文提示詞重點 |
  |---|---|---|---|
  | `.img-hero` | 4:5 | 俯拍燒臘拼盤（叉燒、燒鴨、油雞）在白瓷盤，青花小碟醬料，白色桌面 | overhead Cantonese roast meat platter (char siu, roast duck, soy chicken) on white porcelain, blue-and-white sauce dish, white table, soft daylight |
  | `.img-banquet` | 16:9 | 圓桌合菜：轉盤上幾道菜，無人 | round banquet table with lazy susan and several Cantonese dishes, bright restaurant, no people |
  | `.img-d1` | 1:1 | 一籠蝦餃 | bamboo steamer with har gow shrimp dumplings, overhead |
  | `.img-d2` | 1:1 | 乾炒牛河 | plate of beef chow fun, overhead |
  | `.img-d3` | 1:1 | 雲吞麵 | bowl of wonton noodle soup, overhead |
  | `.img-room` | 3:2 | 明亮的餐館內景：白瓷磚牆、木桌、青花瓷擺飾，無人 | bright Cantonese restaurant interior, white tile wall, wooden tables, blue-and-white porcelain details, no people |

## 3. hair：髮型沙龍（美髮第二款）

- **店家（虛構）**：SOU 髮藝（台北信義區）／SOU Hair Studio（虛構洛杉磯地址）／SOU ヘアスタジオ。
- **對象與任務**：20～40 歲、不分性別、想找設計師的客人；主要動作是「選設計師預約」。跟 beauty（玫瑰色、Cormorant、柔美）不同：這款是**黑白編輯風、價目表當主角**。
- **記憶點**：大字價目表（「剪髮 800 起」這種大數字是這一行真正的資訊，不是裝飾數據）。
- **配色**：淺水泥灰 `#ECEAE6`（頁面底）／表面 `#F6F5F2`／近黑 `#191817`（文字與主要按鈕）／次要文字 `#57534E`／細線 `#D3D0CA`／霧紫灰 `#6F5F7A`（唯一點綴：目前語言、選中的分頁底線，≤5%）。
- **字體**：標題 Archivo 500（英，數字 tabular）＋ Noto Sans TC 500；內文 Archivo 400 ＋ Noto Sans TC 400；日文 Zen Kaku Gothic New 500／400。全站單一字族，靠字級與留白做層級。
- **版面**：
  1. 首屏：左邊超大標題（兩行）＋一句說明＋「選設計師預約」；右邊直幅照片（髮型背影，不露臉），出血到右緣。
  2. 價目表：剪／染／燙／護，四組大字清單（項目＋「起」價＋所需時間），註明長度加價。
  3. 設計師：3 位（職級、擅長、每週班表一行、各自的預約按鈕 → LINE／WhatsApp）；照片 4:5。
  4. Lookbook：橫向捲動相簿（CSS scroll-snap，有鍵盤可捲、無 JS 可用），6 張髮型照。
  5. 第一次來＋常見問題（染燙時間、改期與取消、兒童剪髮）。
  6. 營業時間與位置＋底部預約 CTA。
- **照片清單**：
  | class | 比例 | 內容 | 英文提示詞重點 |
  |---|---|---|---|
  | `.img-hero` | 4:5 | 短髮鮑伯頭的背影與側後方，灰色背景，不露臉 | back view of a person with a sleek short bob haircut, neutral grey studio background, editorial, face not visible |
  | `.img-s1`～`.img-s3` | 4:5 | 三位設計師半身照（虛構）：女 30 多歲、男 30 歲左右、女 20 多歲，黑色上衣 | East Asian hairstylist portrait, black top, grey studio background, fictional person |
  | `.img-l1`～`.img-l6` | 3:4 | 六種髮型（長捲、短髮、男士漸層、挑染、直髮、編髮），背影或側後方，不露臉 | back or side-back view of hairstyle, grey studio background, face not visible |
  | `.img-shop` | 3:2 | 店內：水泥牆、鏡台、黑色座椅，無人 | minimalist hair salon interior, concrete wall, mirrors, black chairs, no people |

## 4. tutor：補習班／課後輔導（補習班第二款）

- **店家（虛構）**：學行教室（新北板橋區）／Stride Learning Center（虛構加州爾灣地址）／学行教室。
- **對象與任務**：國小到高中學生的家長；主要動作是「預約免費程度評估」。跟 education（亮藍、Lexend、活潑）不同：這款是**沉穩、像一本好筆記**，並以「依年級找課」為入口。
- **記憶點**：首屏的年級選擇器（國小／國中／高中／升學考試），點了就篩選下方課程清單（原生 JS；無 JS 時顯示全部）。
- **配色**：紙白 `#F6F6F3`（頁面底）／表面 `#FCFCFA`／石墨 `#22262B`（文字）／墨藍 `#253046`（品牌、按鈕）／次要文字 `#555B66`／細線 `#D8D9D4`／鉛筆黃 `#E3B23C`（唯一點綴：選中的年級、重點底線，≤5%，上面只放石墨色字）。
- **字體**：標題 Zilla Slab 500（英）＋ Noto Sans TC 500；內文 Source Sans 3 400/600 ＋ Noto Sans TC；日文 Zen Kaku Gothic New。
- **版面**：
  1. 首屏：標題＋一句說明＋年級選擇器（4 顆）＋「預約免費評估」；右邊一張教室照片（3:2）。
  2. 課程：清單（科目、適合年級、上課時段、每班人數、費用「起」），依年級篩選。
  3. 上課方式：程度評估 → 學習計畫 → 每週回報（真的是順序）。
  4. 老師：3 位（學歷、教學年資、科目）；4:5。
  5. 學期行事曆：開課日、段考衝刺、寒暑假班（細線表格）。
  6. 常見問題（試聽、請假補課、退費）＋「學習成果」只放可查證的中性描述；虛構數據一律加範例註解。
  7. 評估預約表單（Formspree：家長姓名、電話、孩子年級、想加強的科目）＋位置。
- **照片清單**：
  | class | 比例 | 內容 | 英文提示詞重點 |
  |---|---|---|---|
  | `.img-hero` | 3:2 | 明亮的小班教室：幾張課桌、白板、窗光，無人 | bright small classroom with a few desks, whiteboard, window light, calm and tidy, no people |
  | `.img-t1`～`.img-t3` | 4:5 | 三位老師半身照（虛構）：女 30 多歲、男 40 歲左右、女 20 多歲，素色襯衫 | East Asian teacher portrait, plain shirt, bright classroom background softly blurred, fictional person |
  | `.img-desk` | 3:2 | 俯拍書桌：筆記本、黃色鉛筆、計算紙 | overhead study desk with notebook, yellow pencils and worksheet, soft light |

---

## 預設值自我檢查
- 中醫最容易掉進「紅金＋書法＋太極」→ 用百子櫃與安靜的灰白紙＋深丹砂，丹砂只當品牌色、不配金。
- 粵菜館最容易掉進「黑底燙金」或「大紅燈籠」→ 用青花瓷的白與藍，朱紅只當印章。
- 沙龍最容易掉進「近黑＋單一亮色」或玫瑰金 → 淺水泥灰底、黑字、霧紫只當細節。
- 補習班最容易掉進「亮藍漸層＋卡通插圖＋誇大升學數據」→ 石墨與紙白、鉛筆黃只當標記，不放誇大數據。
