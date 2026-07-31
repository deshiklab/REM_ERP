# REM ERP — Implementation Plan: Improvement Set A + B

**Source:** `docs/improvement-plan.md` (gap analysis vs BITSCOL proposals + SLA + live MARS ERP)
**Target file:** `docs/design-prototype-v8.html` (single-file static prototype, localStorage, PWA)
**Method:** data-driven module architecture (GROUPS / GROUP_ORDER / GROUPS_LOOKUP / search dropdown / Quick-Add / PERMISSION_MODULES / Bengali dict / switch-case render map), `DB._seedV` seed versioning, SW cache bump per commit, browser verification after every phase.

---

## Architecture invariants (must follow for every change)

1. **Menu/group changes are data-driven** — coordinate: sidebar HTML, `GROUPS`, `GROUP_ORDER`, `GROUPS_LOOKUP`, search dropdown defs + `_sdGroupOrder`, Quick-Add `_qaDefs`, `PERMISSION_MODULES`, switch-case render map, Bengali dict.
2. **New storage** → `DB.init('key', [...])` + entry in `DB._seedV` (bump on seed-data change → auto-reset stale localStorage).
3. **IDs inline** — `\''+p.id+'\'`; **backticks require `${}`** interpolation.
4. **Validation** — use the `V` toolkit (`V.run` field rules: required/positive/range/phone/email/date) + `_formRules` business rules + `saveDrawer` numeric min/max; red-highlight + toast; block save.
5. **Money** — ৳ only (fix remaining ₹). `fmtNum` for display.
6. **Mobile** — every filterable toolbar control needs an `id`; controls collapse into ⚙ Filters ≤768px; stats hide on scroll.
7. **SW cache** — bump `rem-erp-v8-vNN` on every HTML change; commit + push per phase; refresh `/tmp/REM-ERP-v8-latest.html`.
8. **Icons/emoji** — Python patch safety (emoji chars, never surrogate escapes); build in memory + write once; git restore on corruption.

---

## New group (Phase 5)

**Communication & AI** 💬 (`communication`) — new 11th sidebar group:
- `whatsapp` — WhatsApp Engine (templates, template→module mapping, history log, bulk broadcast)
- `chat` — Internal Chat (staff conversations/channels)
- `ai_assistant` — AI Copilot / Chatbot (KB-tied, usage analytics) *[roadmap #3 — prototype simulation]* 

Sidebar: 11 icons still fit (flex-shrink pattern from v8-v12).

---

## Phase 1 — Quick wins (no cross-module risk, 1 commit each)

### 1.1 Currency consistency (BUG) ✅ first
- Replace all `₹` → `৳` (59 occurrences across leads/bookings/transactions/coa/bank_accounts/kb/layouts/master_lists/notifications + `settingsAddAccount` default `'₹0'`).
- Bump `_seedV`: add `leads:1, bookings:1, transactions:1, coa:1, bank_accounts:1, knowledge_base:1, master_lists:1, notifications:1`; `layouts:2→3`.
- SW v8-v13.

### 1.2 Flats & Units — "Under Payment" status
- Add unit status `Under Payment` (booking confirmed, installment in progress) alongside Available/Booked/Reserved/Sold/Registered.
- Status filter chips + stats include Under Payment; pricing matrix unaffected; property form status select gains the option.
- Seed: mark 3–4 units Under Payment; `properties` seedV 2→3.

### 1.3 Unsold plot / flat balance ledger
- Plots & Blocks + Flats & Units: new "Open Inventory" summary — available + reserved units per project/block, total unsold value (available units × rate), availability %.
- Derived from live data (no new store). Projects module card too.

### 1.4 Settings — Module enable/disable + Menu Setup
- Settings gains tabs: **Modules** (toggle per module on/off → hides from nav/search/⌘K; stored in `settings` store, `_seedV settings:1`) and **Menu Setup** (reorder/hide group menus).
- `applyPerms`/render reads module-enabled flags; disabled module shows toast "Module disabled by admin".

### 1.5 Calendar (new module in Collaboration)
- `calendar` module (Collaboration group): month view + event list (site visits, payments due, handovers, milestones), event CRUD, day click → add event.
- Store `calendar_events`, seed 12 events; `_seedV calendar_events:1`; Bengali `ক্যালেন্ডার`.

### 1.6 Announcements (new module in Collaboration)
- `announcements`: publish (title/body/audience/priority/pinned), list, read receipts count, archive.
- Store `announcements`, seed 5; Bengali `ঘোষণা`; permission: publish = Admin/HR, view = all.

### 1.7 Finance — Fund Transfer tab
- New Finance tab `transfers`: transfer between bank accounts (from/to, amount, date, ref), validation amount ≤ source balance, auto journal note.
- Store `transfers`, seed 4; `_seedV transfers:1`.

### 1.8 Finance — Journal Entries tab
- New Finance tab `journals`: manual journal entry (date, ref, line items: account × debit × credit), totals must balance (debit = credit), list + detail + delete.
- Store `journals`, seed 6 balanced entries; `_seedV journals:1`; validation via V + `_formRules`.

### 1.9 HR — Attendance check-in / check-out
- Attendance tab: punch in/out button per employee today, working-hours calc, late flag (>9:30 AM), absent if no punch.
- Store in `hr_attendance` (existing) — extend schema + seedV bump 1→2.

### 1.10 HR — Leave approval workflow
- Leave requests gain status flow: **Pending → Approved/Rejected by Manager** (+ role check), leave balance consumed only on approval, manager summary card.
- Reuse existing leave store; seedV bump.

### 1.11 HR — Timesheets tab
- New HR tab `timesheets`: employee × project × task × hours/day, week view, total hours vs target (160/mo), export CSV.
- Store `hr_timesheets`, seed 10 days × 8 staff; `_seedV hr_timesheets:1`; Bengali `টাইমশিট`.

### 1.12 Notifications — Template management
- Notifications module gains Templates tab: email/SMS/WhatsApp templates (name, channel, subject, body with shortcodes {{customer_name}} {{amount}} {{due_date}}), test-send (toast), edit/delete.
- Store `notif_templates`, seed 6; `_seedV notif_templates:1`.

### 1.13 Bulk PDF / e-Invoice exports
- Reports module: Bulk Export tab — pick module (Invoices/Bookings/Leads/Payments), range, format (PDF/e-Invoice/CSV) → generates combined printable report (open print dialog).
- Client-side only (prototype). Bengali `বাল্ক এক্সপোর্ট`.

---

## Phase 2 — Accounting deep-dive (Finance + new modules)

### 2.1 Finance — Bank Reconciliation
- New Finance tab `reconcile`: bank statement lines (date/ref/amount) vs transactions, match/unmatch, uncleared list, difference summary.
- Store `recon_items` seeded from transactions; validation: match amount equal.
- Bengali `রিকনসিলিয়েশন`.

### 2.2 Finance — Audit Statements (SFP / SCI / SCE / SCF)
- New Finance tab `statements`: live generated SFP (assets=liabilities+equity from CoA), SCI (revenue−expense), SCE, SCF (operating/investing/financing from transactions); export PDF/Excel.
- Computed from `coa` + `transactions` + `journals`; Bengali `অডিট রিপোর্ট`.

### 2.3 Settings — Fiscal Year & Accounting Periods
- Settings tab `fiscal`: define fiscal year (start/end), period open/close lock (prevents posting to closed periods), opening balances per account.
- Store in `settings` (extend) + `opening_balances`; validation: period dates valid, balances ≥ 0.

### 2.4 Finance — Credit Notes / Returns
- New Finance tab `credit_notes`: issue credit note against invoice (invoice ref, reason, amount ≤ invoice paid), list with status (Draft/Issued/Applied).
- Store `credit_notes`, seed 3; validation amount ≤ invoice total; Bengali `ক্রেডিট নোট`.

### 2.5 Finance — Purchase Invoices
- Invoices tab gains type filter (Sales/Purchase); purchase invoice form (supplier, PO ref, items, VAT, TDS) links to Stock PO.
- Store `invoices` extended with `type` + `poRef`; seed 4 purchase invoices.

### 2.6 Finance — CoA → transaction linkage
- Transactions list shows account code from CoA; journal lines pull account names; budgets validate against account groups. No new store — wiring only.

---

## Phase 3 — Sales & Inventory

### 3.1 Stock — Goods Receive / Stock Entry
- Stock module new tab `receive`: receive against PO (PO ref, qty, date, inspection pass/fail) → auto stock balance update; stock entry log.
- Store `stock_receipts`; `_seedV stock_receipts:1`; validation qty > 0, ≤ PO remaining; Bengali `মালামাল রিসিভ`.

### 3.2 CRM — Sales Territories / Targets / Stages config
- CRM & Leads gains Settings sub-tab: territories (add/edit), monthly sales targets per salesperson, stage config; leads carry `territory` + `stage`.
- Store `sales_config`; validation names unique; Bengali `বিক্রয় কনফিগ`.

### 3.3 Customers — Segmentation groups
- Customers module: group field (NRB / Investor / Owner / Prospect / Broker), filter chips, group-wise stats.
- Extend `customers` seed + seedV bump; Bengali `কাস্টমার গ্রুপ`.

### 3.4 Bookings — Payment Terms / Schedule
- Booking detail gains payment schedule (installments: date/amount/status), generated from terms (e.g., 10% down + 18 monthly), validation sum = price; overdue flag.
- Store `booking_schedules`, seed for 5 bookings; Bengali `পেমেন্ট শিডিউল`.

### 3.5 CRM — Lead → Booking conversion
- Convert lead to booking wizard: pick unit (availability check), set advance/terms → creates booking + schedule + marks unit Booked/Under Payment; lead status → Booking.
- Validation reuses unit-availability rule from v8-v11.

---

## Phase 4 — HR deep-dive

### 4.1 HR — Shift management
- New HR tab `shifts`: shift types (General 9–6 / Morning / Evening / Site 7–4), roster assignment per employee/week, overtime flag.
- Store `hr_shifts`, seed 4 types + roster; validation time order (start < end); Bengali `শিফট`.

### 4.2 HR — Contracts & Insurance
- Employees tab: contract record (type, start/end, notice period, salary clause) + insurance (provider, policy no, coverage, expiry).
- Extend `hr_employees` schema + seedV bump; expiry reminder (30-day) on HR dashboard.

---

## Phase 5 — Communication & AI (new group 💬)

### 5.1 WhatsApp Engine
- `whatsapp` module: template library (name/body/shortcodes), template→module/event mapping (booking confirmed, dues reminder, handover), message history log (contact, template, status), bulk broadcast composer (segment by group/status).
- Store `whatsapp_templates`, `whatsapp_log`, `whatsapp_broadcasts`; `_seedV` all :1; Bengali `হোয়াটসঅ্যাপ`.

### 5.2 Internal Chat
- `chat` module: channels (General, Sales, Site, Finance), conversations, message send, unread badge, mentions; persisted per user in `chat_messages`.
- Seed 3 channels + 20 messages; Bengali `চ্যাট`.

### 5.3 AI Copilot
- `ai_assistant` module: floating bubble + panel, intent routing (navigate, create, summarize), KB-article suggestions, usage analytics (queries/day, top intents).
- Simulated responses from KB + data summary; store `ai_usage`; Bengali `এআই সহকারী`.

### 5.4 Dues & Recovery — automated notifications
- Dues module: auto-generated reminders on due date (SMS/Email/WhatsApp templates), escalation ladder (7d → 14d → 30d → legal), send log.
- Reuses `notif_templates` + `whatsapp_templates`; store `reminder_log`; Bengali `ডিউস নোটিফিকেশন`.

---

## Phase 6 — Investment, Loan & Customer Portal

### 6.1 Investment, Loan & Contract Management (new module, Accounts & Finance)
- `investment_loans` module: investors (profile, join date, total invested), investments (amount, rate %, schedule), loans (internal/external, principal, interest, tenure, EMI), automated interest accrual + payable summary, contract links.
- Tabs: Dashboard / Investors / Investments / Loans / Contracts.
- Store `investors`, `investments`, `loans`; `_seedV` all :1; validation: amounts > 0, rate 0–25%, EMI ≤ principal+interest; Bengali `বিনিয়োগ ও ঋণ`.

### 6.2 Customer Portal — client-facing
- `customer_portal` extends to client login simulation (pick customer), own bookings, dues, payment history, unit documents, maintenance request, chat with sales.
- Store `portal_sessions` (mock); validation email match customer; Bengali `কাস্টমার পোর্টাল`.

---

## Verification checklist (per phase)

- [ ] Browser load — 0 new JS errors (5 pre-existing empty exceptions are baseline)
- [ ] New modules render: nav, search, ⌘K, Quick-Add, mobile nav sheet
- [ ] Bengali toggle shows new labels
- [ ] Permissions: role without module access cannot open module
- [ ] Validations: each new rule fires (toast + red highlight + save blocked); valid saves succeed
- [ ] localStorage: seed version resets stale data on reload; CRUD persists
- [ ] Mobile: toolbar controls collapse into ⚙ Filters; sidebar 11 icons fit (320px+)
- [ ] SW cache bumped; `git commit` + push; `/tmp/REM-ERP-v8-latest.html` refreshed

---

## Commit / SW plan

| Phase | SW cache | Deliverable |
|---|---|---|
| 1.1 | v8-v13 | Currency fix + seedV bumps — **✅ DONE `f45121b`** |
| 1.2–1.3 | v8-v14 | Under Payment + unsold balance |
| 1.4 | v8-v15 | Module toggles + menu setup |
| 1.5–1.6 | v8-v16 | Calendar + Announcements |
| 1.7–1.8 | v8-v17 | Fund transfers + Journal entries |
| 1.9–1.11 | v8-v18 | HR: check-in/out, leave approval, timesheets |
| 1.12–1.13 | v8-v19 | Notification templates + bulk exports |
| 2.x | v8-v20..22 | Accounting deep-dive |
| 3.x | v8-v23..25 | Sales & inventory |
| 4.x | v8-v26..27 | HR deep-dive |
| 5.x | v8-v28..31 | Communication & AI group |
| 6.x | v8-v32..33 | Investment/Loan + portal |

## Progress tracker

- [x] **1.1** Currency consistency — 70 ₹→৳, seedV bumps, SW v8-v13 (`f45121b`)
- [x] **1.2+1.3** Under Payment status + Open Inventory ledgers — SW v8-v14 (`3a2ba13`)
- [x] **1.4** Module enable/disable + Menu Setup — SW v8-v15 (`2181345`)
- [x] **1.5+1.6** Calendar + Announcements modules — SW v8-v16 (`28fac14`)
- [x] **1.7+1.8** Fund transfers + Journal entries (balanced dr=cr) — SW v8-v17 (`b37ec61`)
- [ ] 1.9 HR check-in/out · 1.10 Leave approval · 1.11 Timesheets
- [ ] 1.12 Notification templates · 1.13 Bulk exports
- [ ] Phase 2 (accounting) · Phase 3 (sales/inventory) · Phase 4 (HR) · Phase 5 (comm/AI) · Phase 6 (investment/portal)
