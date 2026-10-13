# n8n B2B Lead Enrichment & AI Triage Engine (Python + FastAPI)

Stop paying 300+ USD/month for Clearbit or Clay just to qualify inbound form submissions. This lightweight self-hosted pipeline filters free email providers, live-scrapes corporate domains, and scores ICP fit (0-100) via GPT-4o-mini in under 3 seconds.

## Download the Complete Production System
Get the full plug-and-play package (**`enrichment_service.py` FastAPI async scraper + GPT-4o-mini scoring service + ready-to-import `n8n_workflow.json` + 5-min setup guide**):

**[Download the B2B Lead Triage and AI Enrichment Engine on Gumroad (18 EUR OFF Auto-Applied)](https://kritikos12.gumroad.com/l/qjimps/LAUNCH29)**
*(Code **LAUNCH29** is automatically applied via the link above for the first 5 downloads)*

---

## Architecture
1. **Webhook Trigger (n8n):** Captures inbound leads from Typeform, Tally, Webflow, or custom HTML forms.
2. **Corporate Domain Filter (Python):** Automatically separates corporate domains from 100+ free/disposable email providers.
3. **Zero-API Live Domain Scraper (`httpx` + `BeautifulSoup4`):** Extracts company title, meta description, and homepage copy in real time with zero third-party API fees.
4. **AI ICP Qualification (`gpt-4o-mini`):** Outputs strict JSON (`icp_score`, `priority`, `recommended_action`, and a personalized `draft_reply`).
5. **Instant Slack Routing:** High-priority leads (score >= 70) trigger an instant alert in `#sales-alerts`.