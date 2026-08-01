# REM ERP v9 — MARS Client Demo Script (15–20 min)

**Version:** SW v9-v5 · **Build:** `docs/design-prototype-v9.html` (PWA)
**Live URL:** https://monkey-window-fort-labor.trycloudflare.com/design-prototype-v9.html
> ⚠️ Tunnel resets on server restart — regenerate with `cloudflared tunnel --url http://localhost:8877` before presenting and swap the URL in.
> **Always hit `↺ Reset Demo Data` (Switch Role panel) before the client arrives** — the demo starts pristine.

**Pitch line:** 50 modules / 11 groups · per-module subscription · offline PWA · path to live Perfex backend (erp.appvaley.com) — proposal ৳800,000.

---

## Pre-flight checklist (5 min before)

1. `curl -s https://<tunnel>/design-prototype-v9.html -o /dev/null -w "%{http_code}"` → `200`.
2. Open in Chrome → `↺ Reset Demo Data` → reload lands Super Admin.
3. Verify pristine counts (top-left quick stats): **25 leads · 12 invoices · 12 payments · 17 bookings · 12 projects · 12 employees · 30 txns**.
4. Console clean (F12 → Console → no red).
5. Check offline: DevTools → Network → Offline → reload → app still renders (SW `rem-erp-v9-v5`).

---

## Step 1 — PWA / Offline (2 min)

**What to do**
1. Point out the header **📲** button: "installable on desktop and mobile, works without internet."
2. Open DevTools (F12) → **Network** tab → toggle **Offline** → press **F5**.
3. App reloads fully from the service worker (`rem-erp-v9-v5`) — dashboard, charts, data all render.

**Talk track**
> "This is a progressive web app — the entire ERP runs in the browser, offline. Your field engineers in Purbachal, sales agents at fairs, and bankers visiting sites get the full system with zero connectivity. When they reconnect, it syncs."

**Exit:** toggle Offline back off → F5.

---

## Step 2 — Super Admin / Executive overview (3 min)

**What to do**
1. Land on **Dashboard** (executive view). Header reads `REM ERP v9 · Role: Super Admin · 50 Modules`.
2. Read the KPI row: **Available Plots 21** (+2 this month), **Sold Plots 8**, **Reserved 7**, **Sales Value ৳31.6 Cr** (৳26.8 Cr YTD), **Active Bookings 10**, **Hot Leads 10** (+3 this week).
3. Scroll the quick-stat tiles: **CRM & Leads 25 · Invoices 12 · Payments 12 · Bookings 17 active · Finance 30 txns · Employees 12 · Projects 12**.
4. Point at the chart row: **Sales vs Expenses · Expense Breakdown · Lead Conversion Trend · Project Progress**.
5. Press **Ctrl+K** (or click "Search anything (Ctrl+K)") → type `BKG-109` → jump straight to the booking. Esc.

**Talk track**
> "One screen, whole company: portfolio value, what's sold, what's reserved, cash coming in, and every department's pulse. Ctrl+K searches across all your data — type a booking number, a client name, or a project and jump straight to the record. Slash (/) opens the module launcher — 50 modules, one keystroke."

**Numbers to quote:** portfolio ৳626 Cr across 12 projects · bookings ৳31.6 Cr · bank balance ৳2.98 Cr · receivables ৳5.19 Cr.

---

## Step 3 — Projects & inventory (2 min)

**What to do**
1. Top-nav tab **Land** (or global-search `Jolshiri`) → **Projects** module.
2. Show the 12-project grid (P-101…P-112, ৳626 Cr) — note **Land/Flat** standardization and the badge split (40 plots / 70 units).
3. Open **P-101** → project detail: **milestones + Progress %** (65%) + plot/unit availability.
4. Tab over to **Inventory / Stock**: low-stock alerts row.

**Talk track**
> "Every project has live milestones and a progress bar the site engineer updates from the field. Land and apartment projects are standardized — plots and units tracked separately, availability updated in real time. Stock alerts show exactly what's running low on site."

---

## Step 4 — Sales cycle live (4 min) ⭐ the money moment

**What to do**
1. Click the **SA** avatar (top-right) → **Switch Role → Sales Agent** — note the sidebar collapses to Sales's 6 modules (permission scoping live).
2. Open **CRM & Leads** (25 leads) → **+ Add Lead**.
3. Fill the type-driven form: choose **Flat** → watch the form reshape (unit/floor/tower fields appear; Land shows katha/plot). Pick project **Skyline Towers**, name `Demo Client`, phone `01700000000`, source **Real Estate Fair**, budget ৳85L.
4. Save → lead appears at top with status **New** (26 leads).
5. Advance it: ⋯ row menu → **Mark Site Visit** → then **Negotiation**.
6. ⋯ → **Convert to Booking** → unit picker now shows **only Skyline Towers units** (project-filtered) → pick `Apt 12A` → confirm.
7. System creates the customer + **BKG-XXX** booking with payment schedule (down-payment + installments). Show the new booking in **Bookings** (BKG-118).

**Talk track**
> "Watch the whole sales cycle live: a lead walks in at the fair, the agent captures it in 20 seconds — the form changes shape depending on land vs apartment. Site visit, negotiation, and one click converts to a booking with the payment schedule generated automatically. No re-typing, no Excel."

**Exit:** Switch Role → **Super Admin** (or leave for next step via Finance).

---

## Step 5 — Finance live (3 min)

**What to do**
1. **Switch Role → Finance** (7 modules: Finance, Dues, Approvals, Investments…).
2. Open **Invoices** → point at **INV-002 ৳2.2 Cr — Overdue** (Dr. Rubina Ali).
3. Open **Dues** → Rubina's ledger shows **৳10L outstanding** (paid 2.1 Cr of 2.2 Cr), status Overdue.
4. **Payments → + Record Payment** → pick invoice **INV-002**, client Dr. Rubina Ali, amount `৳5,00,000`, mode Bank → Save.
5. Watch the ripple: invoice flips **Overdue → Partial**, dues ledger drops **10L → 5L** (status → Upcoming/On Track), and a **cash inflow** transaction appears — Finance dashboard cash flow moves.
6. Optional second payment `৳5L` → due fully cleared (Paid).

**Talk track**
> "Finance records one payment — and the system does the bookkeeping: the invoice balance updates, the customer's dues ledger drops, and cash position moves on the dashboard. No double entry by hand. Receivables ৳5.19 Cr are reconciled dues, not guesswork."

---

## Step 6 — Site Engineer live (2 min)

**What to do**
1. **Switch Role → Site Engineer** (8 modules: Projects, Construction, QC, BOQ, Stock…).
2. Open **Projects → P-101** → edit **Progress (%)** `65 → 72` → Save — the exec dashboard chart moves.
3. Open **Stock/Inventory** → low-stock alert (e.g., steel/cement below reorder point) → raise a **Purchase Request** (BOQ link).
4. Optionally log a **QC inspection** pass on a unit.

**Talk track**
> "The engineer updates progress from site — one number, and the board and the client portal both reflect it instantly. Stock runs low, the system flags it and the purchase request starts the approval chain. Construction, QC, and BOQ are in one place, not three spreadsheets."

---

## Step 7 — Permissions (2 min)

**What to do**
1. **Switch Role → Super Admin** → top-nav **Admin & Operations** → **Permissions** module.
2. Show the **9-role matrix** (Admin, Manager, Sales Rep, Accounts, Viewer + Super Admin / Sales Agent / Site Engineer / Finance) — Sales Agent shows **65/280** granted.
3. Toggle off **CRM → Create** for Sales Agent → Save → switch to **Sales Agent** → the **+ Add Lead** button is gone.
4. Toggle back on → button returns. (Optional: revoke a module's View → nav entry disappears.)

**Talk track**
> "Nine roles, one permission matrix. You decide who sees what — revoke Create and the button disappears for that role immediately. This is the same engine that scopes each dashboard we just walked through."

---

## Step 8 — Customer portal (2 min)

**What to do**
1. **Switch Role → Super Admin** → top-nav **Customer** tab → **Customer Portal**.
2. Click **👤 Client Login** tab → pick **Dr. Rubina Ali — Jolshiri Abason - Apt 4B** from the Customer dropdown → **🔐 Sign in to Portal**.
3. Show the client's world: **My Bookings, Dues Outstanding ৳5L, Total Paid ৳2.15 Cr, 📁 Documents, 📄 Installment Schedule, 🔧 Maintenance Request** (the ৳5L reflects the payment just recorded in Step 5 — cross-module live).
4. Optional: open **Maintenance Request** tab → submit a request → it appears in Admin & Operations → Ticketing.

**Talk track**
> "Your buyers get a self-service portal: their installments, their documents, their unit's construction progress. Fewer phone calls to your sales office, and every interaction is logged."

---

## Step 9 — Close (1 min)

**What to do**
1. Head back to **Dashboard** (Super Admin). Press **🖨 Print Report** → show the clean printable executive report.
2. Recap slide-less: **50 modules / 11 groups**, per-module subscription, offline PWA, one-click demo reset, live data path to the Perfex backend at erp.appvaley.com.

**Talk track**
> "Fifty modules, eleven groups — CRM, land, finance, construction, HR, customer. You subscribe per module, so MARS pays for what it uses and grows module by module. Today was a prototype running entirely in the browser; the production path is the same screens wired to a real database — the backend we already run at erp.appvaley.com. Proposal ৳800,000, work order in seven installments."

**Then:** stop. Ask for questions.

---

# Demo Cheat Sheet

## Keyboard / UI shortcuts
| Key | Action |
|---|---|
| **Ctrl+K / ⌘K** | Global search — leads, projects, contacts, bookings (all 50 modules) |
| **/** | Command palette (module launcher) |
| **🕘** (header) | Recent-items tray (persisted) |
| **⌨** (header) | Shortcuts reference |
| **📲** (header) | Install PWA (offline) |
| **🌙 / 🎨** | Dark mode / theme switcher |
| **EN** | Language switcher (i18n) |
| **SA** avatar | Switch Role (Super Admin / Sales Agent / Site Engineer / Finance) + **↺ Reset Demo Data** |
| **🖨 Print Report** | Per-role report pack (executive / sales / finance / engineer) |

## Exact records to create (in order)
1. **Lead:** name `Demo Client`, type **Flat**, project **Skyline Towers**, source **Real Estate Fair**, budget ৳85L → status New → Site Visit → Negotiation.
2. **Conversion:** ⋯ → **Convert to Booking** → unit **Apt 12A** (Skyline-only picker) → creates customer + **BKG-118**.
3. **Payment:** INV-002 (Dr. Rubina Ali, Overdue ৳10L) → **৳500,000** → invoice Partial, dues 5L. (Repeat ৳5L → Paid/cleared.)

## Numbers to quote
- Portfolio: **৳626 Cr** · 12 projects (P-101…P-112) · P-101 progress **65%** (demo → 72%)
- Bookings: **17 / ৳31.6 Cr** · Payments: **12 / ৳7.12 Cr** · Dues: **9 accounts / ৳5.19 Cr**
- Bank balance **৳2.98 Cr** · Receivables **৳5.19 Cr** (reconciled) · Sales pipeline **৳56.7 Cr**
- Sales YTD 2026: **৳17.1 Cr** (exec card shows ৳26.8 Cr incl. reserved)
- Inventory: **40 plots / 70 units** · Available plots **21** · Sold **8** · Reserved **7**
- People: **12 employees** · HR leaves: Annual 14 / Sick 10 / Casual 7 / Festival 7
- Investments: **6 investors / ৳14.5 Cr** · Loans: **5 / ৳12 Cr**
- Proposal: **৳800,000** · Work order **7 installments** · Modules **50 / 11 groups**

## Key invoices
- **INV-001** ৳46L (Kamrul) · **INV-002** ৳10L **Overdue** (Rubina — the demo payment) · **INV-004** ৳1.2 Cr (Jahanara) · **INV-006** ৳3 Cr · **INV-008** ৳4.66L

## Portal login
- **Dr. Rubina Ali** — `rubina.ali@yahoo.com` (demo password; any value accepted in prototype).

## Pitfalls to avoid
1. **Tunnel URL changed?** Regenerate: `cloudflared tunnel --url http://localhost:8877` — update URL before presenting.
2. **Data looks dirty from rehearsal?** Switch Role → **↺ Reset Demo Data** → reload → pristine (25/17/12/12).
3. **Offline toggle left on** after Step 1 → browser won't load new tunnel pages. Turn Offline off.
4. **Don't quote stale money numbers** — read the live KPI cards; seed values above are the baseline.
5. **Charts animate** — let them settle before clicking, avoids a "broken chart" impression.
6. **Console open during demo?** Keep it closed for clients; it's for rehearsals only.

## Rehearsal checklist (Phase D output)
- [ ] Every step above executed against live build — pass/fail logged
- [ ] Zero JS console errors across full walkthrough
- [ ] Offline reload served by SW `rem-erp-v9-v5`
- [ ] Pristine counts before presenting (25 leads / 17 bookings / 12 payments / 12 projects / 20 entities)
- [ ] `/tmp/REM-ERP-v9-latest.html` refreshed after push
