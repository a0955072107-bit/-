# Regional Market Entry for HTML One-Page Templates and Website Services: Germany/France, SEA (TH/VN/ID), Singapore/Malaysia Chinese Businesses (Taiwan-based solo seller)

Research date: 2026-11-22. Method: 15 web searches/fetches. Limits: gumroad.com could not be fetched from this session (the network blocked the host), so the Gumroad VAT claims below come from search snippets of Gumroad's own help pages plus third-party summaries. Many price figures come from agency or vendor marketing blogs and are marked as such.

## 1. Germany and France: legal requirements, demand, prices, VAT, platforms

### Takeaway
Germany and France will pay high prices for websites; a basic freelance site plausibly costs EUR 1,000+ (inferred from day rates). The catch is compliance: a template sold there must ship "compliance-ready". That means a place for the Impressum and privacy policy, self-hosted fonts with no Google Fonts CDN call, no third-party embeds or trackers without consent, and a contact form with a privacy notice. Gumroad says it acts as merchant of record for EU/UK digital sales, which removes the VAT burden for template sales. Services such as customization are a separate VAT question.

### Cited Findings
**Impressum (Germany, § 5 DDG)**
- Since 14 May 2024 the Digitale-Dienste-Gesetz (DDG) replaces the TMG. The old §§ 5–6 TMG duties carry over almost unchanged into §§ 5–6 DDG, so references to "§ 5 TMG" are outdated. — [IHK Dresden](https://www.ihk.de/dresden/hauptnavigation/recht-steuern/merkblaetter-von-a-bis-z/impressum--6697212); [IHK München](https://www.ihk-muenchen.de/ratgeber/recht/internetrecht/impressum/)
- The duty is triggered by a digital service offered "geschäftsmäßig, in der Regel gegen Entgelt", which covers essentially every small-business website. — [IHK Köln](https://www.ihk.de/koeln/hauptnavigation/recht-steuern/impressum-pflichtangaben-auf-websites-5271690)
- Required items:
  - company name, legal form and address
  - fast electronic contact plus direct communication, in practice email and phone
  - competent supervisory authority (§ 5 Abs. 1 Nr. 3)
  - register entries
  - USt-IdNr or Wirtschafts-ID (Nr. 6)
  - for regulated professions such as clinics and doctors: the Berufskammer and the professional title
  - the information must be "leicht erkennbar, unmittelbar erreichbar und ständig verfügbar"

  Sources: [IHK Köln](https://www.ihk.de/koeln/hauptnavigation/recht-steuern/impressum-pflichtangaben-auf-websites-5271690); [IHK Hanau](https://www.ihk.de/hanau/recht/rechtsgebiete/internetrecht/pflichtangaben-im-internet-impressum-6981984); [datenschutz-generator.de](https://datenschutz-generator.de/ratgeber-impressum/)
- Fines of up to EUR 50,000 apply for a missing or incorrect Impressum. Editorial content also triggers § 18 Abs. 2 MStV. — [IHK Köln](https://www.ihk.de/koeln/hauptnavigation/recht-steuern/impressum-pflichtangaben-auf-websites-5271690); [WBS Legal](https://www.wbs.legal/medienrecht/webseiten/impressum)

**Cookie consent: TTDSG renamed TDDDG**
- A genuine consent requirement for cookies and tracking has applied since December 2021. It was first codified in the TTDSG and carried into the TDDDG; the rename changed nothing in substance. — [e-recht24](https://www.e-recht24.de/datenschutz/12834-tdddg.html); [CMS](https://cms.law/de/deu/legal-updates/das-ende-der-cookie-banner-dienste-zur-einwilligungsverwaltung)
- § 25 Abs. 2 TDDDG exempts strictly necessary storage. Examples: a cookie that stores the language setting, and cookies for security or fraud prevention. The seller's language switcher, if it uses localStorage or a cookie only for the language preference, likely falls under this exemption. — [DFN Recht (2026)](https://recht.dfn.de/wp-content/uploads/2026/08/Website-Cookies-DSGVO.pdf)
- Pre-ticked tracking or third-party cookies in a banner do not create valid consent. — [IHK Köln](https://www.ihk.de/koeln/hauptnavigation/recht-steuern/regeln-fuer-cookies-ttdsg-5259484)
- A banner offering only "Akzeptieren & Schließen" plus an "X" was found problematic in a consumer-protection case in NRW. — [Verbraucherzentrale NRW](https://verbraucherzentrale.nrw/node/85693)

**Cookie consent: France (CNIL)**
- CNIL rule: refusing must be as easy as accepting, and the banner must be clear and not misleading. A consolidated recommendation was published in January 2026 after a deliberation of 18 Dec 2025 on multi-device consent. — [CNIL consolidated recommendation PDF](https://cnil.fr/sites/default/files/2026-01/recommandation_cookies_consolidee.pdf); [CNIL bilan 2025](https://cnil.fr/fr/bilan-sanctions-2025)
- 2025 enforcement:
  - SHEIN, EUR 150M (1 Sep 2025): the banner gave no information on advertising purposes
  - Google, sanctioned the same day
  - Condé Nast/vanityfair.fr, EUR 750k (20 Nov 2025): cookies were set before any interaction, and "Tout refuser" was ineffective
  - American Express, EUR 1.5M (27 Nov 2025)
  - In total, 83 sanctions in 2025 worth EUR 486.8M, with cookies a main theme

  Sources: [CNIL SHEIN](https://www.cnil.fr/fr/cookies-deposes-sans-consentement-la-cnil-sanctionne-shein-dune-amende-de-150-millions-deuros); [CNIL Vanity Fair](https://cnil.fr/fr/cookies-deposes-sans-consentement-la-cnil-sanctionne-la-societe-editrice-du-site-vanityfairfr); [CNIL AmEx](https://www.cnil.fr/fr/cookies-la-cnil-sanctionne-american-express-dune-amende-de-15-million-deuros); [CNIL 2025 actions (EN)](https://www.cnil.fr/en/sanctions-and-corrective-measures-cnils-actions-2025)
- CNIL has also issued formal notices (mises en demeure) to website publishers over misleading cookie banners. — [CNIL](https://cnil.fr/fr/bannieres-cookies-trompeuses-la-cnil-met-en-demeure-des-editeurs-de-sites-web)

**Google Fonts (German rulings)**
- LG München I, 20.01.2022, Az. 3 O 17493/20: dynamically loading Google Fonts transmits the visitor's IP address to Google without consent and violates the GDPR. The court ordered the site to stop and awarded EUR 100 in damages under Art. 82 GDPR. — [IHK Bergisch](https://www.ihk.de/bergische/recht-und-steuern/wettbewerbsrecht/google-fonts-5646176); [dr-datenschutz](https://www.dr-datenschutz.de/schadensersatz-urteil-google-fonts-und-die-dsgvo/)
- A mass warning-letter (Abmahnung) wave followed in 2022.
  - LG München I, 30.03.2023 (4 O 13063/22): no claim exists where the claimant crawled sites automatically to provoke violations; such letters are an abuse of rights.
  - Court commentary also found the use of a lawyer meant to intimidate recipients.

  Sources: [Der Betrieb](https://der-betrieb.de/meldungen/google-fonts-abmahnwelle-war-rechtsmissbraeuchlich); [Händlerbund](https://ohn.haendlerbund.de/recht/urteile-entscheidungen/138187-urteil-zu-google-fonts-abmahnungen-ohrfeige-fuer-massenabmahner); [WKO](https://www.wko.at/datenschutz/abmahnungen-google-fonts)
- Rulings date from 2022–2023; I found no 2025–2026 development. Self-hosting fonts remains the standard mitigation, and Google Fonts are still a known red flag for German buyers.

**Contact forms and the privacy policy**
- A contact form processes personal data, so the GDPR requires information under Art. 13 in the privacy policy (Datenschutzerklärung). German practice guides (GDD Praxishilfe) cover this for online presences. — [GDD Praxishilfe (2024)](https://gdd.de/wp-content/uploads/2024/05/GDD-Praxishilfe-DS-GVO-ePrivacy-und-Datenschutz-beim-Onlineauftritt.pdf)
- This was not verified line by line in this session. Specific form requirements (a linked privacy notice, a minimal set of required fields, no pre-ticked newsletter box) are standard guidance but not individually sourced here.

**EU VAT and Gumroad**
- Gumroad's help center says it handles VAT for creators on all digital product sales in the EU and UK. For those sales Gumroad is the "merchant of record" and is responsible for collecting and remitting VAT. — [Gumroad Help: Dealing with VAT](https://gumroad.com/help/article/10-dealing-with-vat) (snippet only; the page could not be fetched)
- From 1 Jan 2025 Gumroad says it handles all creators' tax obligations as merchant of record where it has obligations. — [Gumroad taxes](https://gumroad.com/taxes)
- Third-party sources describe Gumroad as merchant of record with a fee of roughly 10% + $0.50 per transaction. These are competitor or commercial sources and should be verified. — [Fungies](https://fungies.io/gumroad-vs-paddle/); [DEV Community 2026](https://dev.to/devtoolpicks/how-to-handle-eu-vat-as-a-solo-saas-founder-in-2026-jpd)
- Non-EU sellers owe EU VAT from the first euro of B2C sales when selling directly, without a merchant of record; the EUR 10k threshold applies only to EU-established sellers. — [Fungies EU VAT 2026](https://fungies.io/eu-vat-digital-services-merchant-of-record-2026)

**Prices: France freelance**
- On Malt, developer day rates (TJM) shown run about EUR 450–600. Beginner profiles show EUR 150–250/day. — [Malt tech](https://www.malt.fr/a/freelance/tech); [Blog du Modérateur 2025](https://www.blogdumoderateur.com/freelances-taux-journaliers-moyens-it-france-2025/)
- 2026 average freelance developer TJM is about EUR 520; junior EUR 320, confirmed EUR 575, senior EUR 670. Paris is 5–10% above the national average. — [La Fabrique du Net 2026](https://www.lafabriquedunet.fr/tarifs-des-developpeurs-freelances-dans-les-grandes-villes-de-france/)

### Inferences
- A one-page site takes about 2–4 freelance days, so local French or German freelancers likely charge roughly EUR 800–2,500. On that basis the seller's $249–449 customization is very cheap, but it will be compared against Wix, Jimdo and IONOS builders, not against local freelancers.
- To be sellable in Germany and France, a template needs:
  - a footer link to "Impressum" / "Mentions légales" and to "Datenschutzerklärung" / "Politique de confidentialité", with placeholder pages
  - fonts bundled locally (woff2), with no fonts.googleapis.com call
  - no Google Maps or YouTube embeds without click-to-load consent placeholders
  - a contact form with a privacy notice line
  - no analytics, or analytics behind an opt-in banner
  - German and French language versions (currently missing)

  "DSGVO-konform" and "ohne Google Fonts" are selling points to put in the listing title.
- France also requires "mentions légales" under LCEN. This is the seller's general knowledge and was not verified in this session.
- Gumroad as merchant of record makes the $39/$199 sales VAT-free work for the seller.
- Customization services sold B2B to German or French businesses: an EU business customer would normally self-account for VAT under reverse charge. Inferred; not verified for Taiwan-origin services.
- Liability risk: the template is used by the buyer, so the buyer is the controller and responsible for compliance. Add a disclaimer that the template is not legal advice.

### Gaps
- No direct data on demand or sales volume for HTML templates in Germany or France on Etsy DE/FR, Creative Market or ThemeForest. Local template marketplaces were not researched.
- No German price data for small-business sites (search returned only legal pages).
- Whether Malt accepts freelancers based outside Europe (Taiwan), and Malt's fees: not found.
- Gumroad page not fetched directly. Payout options to Taiwan and the exact current fee should be verified on gumroad.com.
- Etsy seller eligibility for Taiwan and its handling of digital-product VAT: not researched in this session.

## 2. Southeast Asia: Thailand, Vietnam, Indonesia

### Takeaway
SMBs in TH, VN and ID mostly operate through LINE OA (TH), Zalo OA (VN), WhatsApp/Instagram (ID) and marketplaces such as Shopee, not standalone websites. Local website prices are low: about VND 3–10M (roughly USD 115–380) for a standard Vietnamese site, and an advertised THB 9,900 promo. Every local market needs its own language, and local freelance platforms favour local sellers. For an English/Chinese template seller, this region looks low-margin and high-effort.

### Cited Findings
**Platforms SMBs use**
- Thailand: LINE Thailand cites 56 million users and 12 billion Official Account conversations in its 2026 business pitch (secondary article, not opened). — [Relevant Audience](https://www.relevantaudience.com/digital-marketing-en/line-thailand-business-solutions-2026/); [LY Corp 2026](https://www.lycorp.co.jp/en/story/20260106/lineth_forbusiness.html)
- Thailand: LINE OA subscribers grew 25% to 5 million in one year, an older Bangkok Post article (date not shown; likely around 2022). — [Bangkok Post](https://www.bangkokpost.com/business/2272307/line-oa-signups-surge-as-smes-go-digital)
- A Thai marketing outlet argues an official website may not be essential when sales happen on LINE or Facebook. — [Marketing Oops](https://www.marketingoops.com/news/biz-news/line-official-account-sme/)
- Indonesia: WhatsApp reaches about 90.9% of internet users and Instagram about 85.3% (population-wide, not SMB). — [Meltwater](https://www.meltwater.com/en/blog/social-media-statistics-indonesia)
- Indonesia: many micro-entrepreneurs sell mainly via WhatsApp and Instagram rather than formal marketplaces. — [MicroSave 2025 Social Commerce report](https://www.microsave.net/wp-content/uploads/2025/09/Social-Commerce-Initiatives_Report_English.pdf)
- Indonesia: an INDEF study is reported as finding that 50% of UMKM (Indonesian micro, small and medium businesses) use Shopee as their main online sales platform (headline only). — [IDN Times](https://www.idntimes.com/business/economy/shopee-pilihan-umkm-csc-02-4hwqt-9ydr27)
- Indonesia: BPS counts website, marketplace, social media and instant messaging together as e-commerce, so the share of UMKM with their own website is not separated out. — [UNSIAP/BPS 2026](https://www.unsiap.or.jp/sites/default/files/doc/2026-04/08_Measuring%20E-Commerce%20in%20Indonesia_Webinar%20on%20Digitalization_update1.pdf)
- Indonesia: about 55% of online MSMEs use WhatsApp to communicate with customers (older, undated DAI brief). — [DAI](https://www.dai.com/uploads/final-msme-reports/indonesia-country-brief.pdf)
- Vietnam: local vendors bundle Zalo OA messaging and landing pages built for Facebook, Zalo and TikTok ads. — [Sapo](https://www.sapo.vn/website-mobile.html)
- Regional macro: the e-Conomy SEA 2025 report puts the SEA digital economy above USD 300B GMV, growing 15% year on year. 3 in 5 people shop online and over 60% of payments are digital. — [Google blog](https://blog.google/company-news/inside-google/around-the-globe/google-asia/sea-economy-2025/); [Temasek release](https://www.temasek.com.sg/en/news-and-resources/news-room/news/2025/e-conomy-sea-2025-report-aseans-digital-economy-poised-to-surpass-300-billion)

**Local prices**
- Vietnam:
  - standard website: VND 3–10M, packages about VND 6–20M
  - themes at design firms: VND 3–5M
  - SaaS builders: Sapo from VND 499k/month, Haravan from VND 400k/month

  Vendor source, updated for 2026. — [Sapo blog](https://www.sapo.vn/blog/huong-toi-kinh-doanh-truc-tuyen-nho-thiet-ke-web-do-the-thao)
- Thailand (Bangkok agency figures): landing page of 1–3 pages THB 15,000–40,000; business site of 5–10 pages THB 40,000–100,000. Another agency advertises THB 9,900 per site as a promotion. Vendor source. — [Digital Agency Bangkok](https://digitalagencybangkok.com/web-design-packages-in-thailand/); [Clearpath](https://clearpath-site.pages.dev/blog/website-cost-bangkok)
- Thai designers on Dribbble list prices "from $70/project". — [Dribbble](https://dribbble.com/freelance-mobile-designers-for-hire-nong-ki-th)
- Fastwork holds client funds in escrow and releases them after the employer approves the work. — [Fastwork listing](https://fastwork.co/user/markwst/web-development-78729584)

### Inferences
- Approximate USD conversions: VND 3–10M is about USD 115–380; THB 15–40k is about USD 450–1,200; THB 9,900 is about USD 300. These use approximate 2026 exchange rates and are not sourced.
- A $39 template competes with Sapo or Haravan subscriptions and free Facebook/LINE pages. A $249–449 service sits in the middle of the local range but requires the Thai, Vietnamese or Indonesian language, plus LINE OA, Zalo or WhatsApp click-to-chat integration.
- Product adaptation if entering: add a "Chat on LINE / Zalo / WhatsApp" button, a Shopee or Tokopedia store link block, mobile-first design, and local languages.
- Expected revenue for a non-native solo seller is low. A better angle may be selling to Western expats and tourism businesses in Thailand (B&Bs, gyms, restaurants in Phuket and Chiang Mai) in English, which is speculative.
- Local platforms (Fastwork, Sribulancer/Projects.co.id, vLance) typically need local language, local payout or ID, and local reviews. Not verified.

### Gaps
- No country-specific SMB website-ownership statistic for TH, VN or ID was found. The e-Conomy SEA SMB breakdown was not extracted from the PDF.
- Fastwork, Sribulancer, Projects.co.id and vLance: fees and whether a Taiwan individual can register or receive payouts were not found. Search returned nothing on their foreign-seller rules.
- No Indonesian website price data (IDR) was found.
- Willingness to pay for templates specifically (as opposed to done-for-you sites) was not found.

## 3. Singapore and Malaysia Chinese-speaking businesses

### Takeaway
Singapore has the highest price levels in Asia for small-business sites: SGD 1,000–5,000 basic, freelancers SGD 1,200–3,000. Bilingual English plus Simplified Chinese is a recognized need, though no premium is quantified. The seller's existing EN/ZH templates with a language switcher fit almost directly. Malaysia is cheaper (around RM 500–3,000 basic). PDPA compliance for contact forms is light: a purpose notice, consent, withdrawal, and DPO contact. This looks like the best fit and lowest effort of the three regions.

### Cited Findings
**Prices**
- Singapore: basic small-business site about SGD 1,000–5,000, and SGD 1,500–4,000 for a 4–6 page informational site. — [GoDaddy SG](https://godaddy.com/resources/asia/skills/how-much-does-a-website-cost-in-singapore); [Creativeans 2025](https://www.creativeans.com/resources/web-design-singapore-real-costs-pricing-guide-for-2025)
- Singapore agencies charge SGD 2,500–8,000, or SGD 3,000–6,000 for a small-business site. — [OOm](https://www.oom.com.sg/website-design-cost-singapore/); [NUS blog 2025](https://blog.nus.edu.sg/webdesignsingapore/how-much-does-web-design-cost-in-singapore-in-2025)
- Singapore freelancers: SGD 1,200–3,000 per site, or SGD 30–100 per hour. Hosting runs SGD 120–500 per year. — [marketingagency.sg](https://marketingagency.sg/website-cost-singapore); [Kaopiz](https://kaopiz.com/en/articles/website-design-cost-in-singapore/)
- Singapore: an instant web design subscription from Exabytes is listed at SGD 279/month. — [whtop](https://www.whtop.com/plans/exabytes.sg/70262)
- Malaysia: basic small-business site RM 500–3,000 per year; semi-professional RM 1,000–15,000. Vendor source. — [GoDaddy MY](https://godaddy.com/resources/asia/skills/how-much-does-a-website-cost-in-malaysia)
- Bilingual: guides note that Chinese adds work on fonts, line breaking, search and forms. A common approach is one site with an English/Chinese toggle, which matches the seller's design. — [bilingual SG guide](https://growuildrevamp.pages.dev/blog/bilingual-website-design-singapore-english-chinese/); [Kolonell 2026](https://kolonell.com/en/blog/multilingual-b2b-website-cost-singapore-2026)
- Singapore funds up to 50% of eligible projects through EDG support (an agency claim; EDG is aimed at Singapore-registered firms and is not a factor for a foreign freelancer). — [Creativeans](https://www.creativeans.com/resources/web-design-singapore-real-costs-pricing-guide-for-2025)

**PDPA (Singapore) and contact forms**
- Organisations may collect, use or disclose personal data only with knowledge and consent, subject to exceptions. Notification must say why data is collected. No specific form of notice is prescribed, and a website notice is acceptable. — [PDPC Guide to Notification](https://www.pdpc.gov.sg/-/media/Files/PDPC/PDF-Files/Other-Guides/Guide-to-Notification-260919.pdf)
- Consent should be clear, and individuals must be able to withdraw it. — [PDPC DP Starter Kit](https://www.pdpc.gov.sg/-/media/files/pdpc/pdf-files/dp-starter-kit---171017.pdf)
- The business contact of at least one DPO must be publicly available, via ACRA or a readily accessible part of the website. Organisations must also make information about their data-protection policies available. — [PDPC obligations](https://www.pdpc.gov.sg/-/media/files/pdpc/pdf-files/resource-for-organisation/obligations_edm_01.pdf)
- If a form collects Singapore phone numbers for marketing, the Do Not Call Registry rules apply unless clear consent was obtained. — [PDPC Advisory Guidelines on Key Concepts](https://www.pdpc.gov.sg/-/media/files/pdpc/pdf-files/advisory-guidelines/ag-on-key-concepts/%20advisory-guidelines-on-key-concepts-in-the-pdpa-17-may-2022.pdf)

### Inferences
- The seller's $249–449 customization (about SGD 330–600) sits at roughly 20–50% of local freelancer prices. Positioning: "bilingual EN/中文 site in 7 days, from SGD 399".
- Template additions for SG/MY:
  - a PDPA notice line under the contact form ("By submitting, you consent to [Business] collecting your data to respond to your enquiry...")
  - a privacy policy page with a DPO contact
  - WhatsApp click-to-chat, which is ubiquitous in SG/MY
  - Malay or Simplified Chinese variants
- Malaysia has its own PDPA 2010, amended in 2024. It was not researched here, so the details need checking.
- Channels (unverified in this session): Carousell SG/MY service listings, Facebook groups for SG/MY Chinese business owners, Xiaohongshu (used by Chinese-speaking Singaporeans and Malaysians), and Fiverr. The seller's Traditional/Simplified Chinese content marketing could double as Xiaohongshu posts.

### Gaps
- Carousell rules for non-resident sellers and payments (Carousell mostly relies on meet-ups or local payments): not researched.
- Statistics on Xiaohongshu usage by SG/MY business owners: not found.
- A bilingual price premium was not quantified.
- Malaysia PDPA contact-form requirements and Malaysia Chinese-business price levels were not found.

## 4. Cross-region: competition, payments for a Taiwan individual, revenue potential vs effort

### Takeaway
Payments are solvable everywhere through Gumroad (merchant of record), Fiverr/Upwork (Payoneer), and direct invoicing via PayPal or Wise. Country-local freelance platforms (Fastwork, Sribulancer, vLance, Malt) are the uncertain part for a Taiwan individual. Ranking by revenue potential versus effort, inferred from the evidence above:
1. SG/MY Chinese businesses: high price, existing language assets, light compliance.
2. Germany/France: high price, but needs translation plus a compliance redesign and must compete with builders.
3. TH/VN/ID: low price, needs localization, and SMBs favour social and messaging channels over websites.

### Cited Findings
- Payoneer connects to Upwork and Fiverr for payouts. Fiverr payout options depend on location (PayPal, Payoneer, Revenue Card), and each Fiverr-to-Payoneer withdrawal costs USD 1. — [Payoneer](https://www.payoneer.com/ko/get-paid-by-fiverr/); [Wise](https://wise.com/us/blog/how-to-get-paid-on-fiverr)
- Gumroad is merchant of record for EU/UK digital sales, so EU VAT is not the seller's job for template sales. — [Gumroad Help](https://gumroad.com/help/article/10-dealing-with-vat)
- Competition signal: Thai designers on Dribbble start from USD 70 per project; Vietnamese SaaS builders cost around USD 16–20 per month. — [Dribbble](https://dribbble.com/freelance-mobile-designers-for-hire-nong-ki-th); [Sapo](https://www.sapo.vn/blog/huong-toi-kinh-doanh-truc-tuyen-nho-thiet-ke-web-do-the-thao)

### Inferences
- Effort estimates, all inferred:
  - DE/FR: translate 35 templates, add legal page stubs and self-hosted fonts. Roughly 2–4 weeks one-off, plus an ongoing need to stay current on law.
  - SG/MY: about 1 week of PDPA and WhatsApp tweaks plus channel marketing.
  - SEA: 3 extra languages plus channel integrations, for low prices.
- Revenue: no sourced sales-volume data exists for any region, so any revenue projection would be speculative.

### Gaps
- Fastwork, Sribulancer, Projects.co.id, vLance and Malt eligibility for a Taiwan individual was not confirmed.
- Etsy and Creative Market seller eligibility for Taiwan, and their fees, were not researched.
- No template sales-volume data was found for any region.
