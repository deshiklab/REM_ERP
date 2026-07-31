# REM ERP — Improvement & Upgradation Plan (vs BITSCOL Proposals + Live MARS ERP)

**Date:** 2026-06 · **Author:** AI-assisted analysis (AJ)
**Sources studied:**
1. `ERP_Software_Proposal_For_MARS_CONSTECH_LIMITED_By_BITSCOL_Revised.pdf` — Real-Estate (Land) ERP scope, 10 module families, BDT 800,000
2. `CRM Software Proposal For MARS CONSTECH LIMITED By BITSCOL.docx` — Real-Estate CRM scope (Stock, Products, CRM, Sales, Accounts, Notifications, Reports, Settings, Backup, Users), ERPNext/Frappe stack
3. `Work Order & SLA - MARS CONSTECH LIMITED V3.docx` — 7-installment BDT 800,000 delivery + MMC/SLA terms (server 12,000/mo, support 10,000/mo)
4. `design-prototype-v8.html` — REM ERP V8 prototype (10 groups / 44 modules, static, localStorage)
5. Live MARS ERP (erp.appvaley.com — Perfex-based, logged in as rofiq@gmail.com) — 27 top-level modules incl. submenus

---

## 1. What the BITSCOL proposal promises (the contracted scope)

| # | Module family | Key features promised |
|---|---|---|
| 1 | Setup & Security | user/role mgmt, **customer segmentation into groups**, **GDPR privacy**, **menu customization**, **module enable/disable switches**, theme styling |
| 2 | HR, Timesheets & Leave | HR dashboard, **check-in/check-out**, leave requests + **approval workflows**, leave balance, **payroll** |
| 3 | CRM & Sales | customer DB, follow-ups, sales pipeline, leads w/ filters, proposals, cost estimates, invoicing, payment tracking, **balance of unsold plots** |
| 4 | Properties (Land) | land records (qty, **dag, khatian, seller details**), purchase values, land sales records, plot records, **real-time land balance** |
| 5 | Credit Recovery | client balances, recovery monitoring, **automated dues notifications**, collection reports |
| 6 | Accounting & Finance | CoA, **bank reconciliations**, budget monitoring, **SFP/SCI/SCE/SCF audit reports** (PDF & Excel), manual + auto **journal entries**, fund transfers |
| 7 | Investment, Loan & Contract | **investor profiles, internal/external investments & loans, automated interest calc**, centralized contracts |
| 8 | Project Mgmt & Utilities | project dashboard, tasks, site progress, utilities vault (**media storage, DB backups, calendar events, announcements, bulk PDF/e-Invoice exports**) |
| 9 | WhatsApp, Messaging & AI Chatbot | **internal staff chat**, **WhatsApp template mapping + history + bulk broadcast**, **AI chatbot + KB + analytics** |
| 10 | Data & Backup | automated daily/weekly backups, off-site storage, **encryption**, data retention policies |

## 2. What the prototype already covers (V8: 10 groups / 44 modules)

- **Executive:** Dashboard, Analytics, Reports, BI Reports
- **Sales & CRM:** Customers, CRM & Leads, Proposals, Contact Book, Sales & Marketing
- **Projects:** Project Acquisition, Flats & Units, Plots & Blocks, Layout & Unit Builder, Projects
- **Bookings & Customer:** Bookings, Customer Portal, Handover & Post-Sales, Dues & Recovery (+ Payment Reminders tab), Ticketing & Issue
- **Engineering & Construction:** Contractors, Variation Orders, Equipment, Labor Mgmt, Design Mgmt
- **Accounts & Finance:** Finance (Dashboard/Transactions/Receive/Expense/Invoices/Payments/Banks/Budgets/Tax), Payment Heatmap, Financial Approvals, BOQ & Cost Control
- **Admin & Operations:** HR (Dashboard/Employees/Attendance/Leave/Payroll/Recruitment), Documents Vault, Knowledge Base, Stock & Procurement (Inventory/PO/Suppliers)
- **Legal & Compliance:** Compliance, Legal Contracts, QC & Inspection
- **Collaboration:** Tasks, Team Workspace, Notifications, Activity Log
- **System:** Permissions, Settings (Chart of Accounts, Banks, Tax/VAT, Invoice Template, Integrations), System Manual, Backup & Restore, CSV Import

**Already strong:** module coverage breadth, RBAC UI, CSV import, backup/restore UI, layout builder, pricing matrices, payment heatmap, financial approvals, leave balance rules, ticketing, knowledge base, dual-language, PWA.

---

## 3. Gap analysis → improvement list

### A. MISSING MODULES (add to prototype)

1. **Investment, Loan & Contract Management** *(promised §7)* — investor profiles, internal/external investment & loan registers, balances, automated interest/payable calc. Today "investor" exists only as a contact-book role. **HIGH priority — explicitly contracted.**
2. **General Ledger / Journal Entries** *(promised §6; live ERP has Journal Entry)* — manual + auto double-entry journals. Prototype has 0 journal support.
3. **Bank Reconciliation** *(promised §6; live ERP has Reconcile)* — statement upload, matching, uncleared items.
4. **Audit Statement Reports — SFP / SCI / SCE / SCF** *(promised §6)* — live generated statements with PDF & Excel export (BI Reports is only a report catalog today).
5. **Fiscal Year / Accounting Period / Opening Balance / Company Setup** *(CRM proposal Accounts)* — accounting calendar, period locking, opening balances.
6. **Fund Transfers** *(promised §6; live ERP has Transfer)* — between bank accounts / cash.
7. **Credit Notes / Returns & Credit** *(CRM proposal)* — reverse sales invoices.
8. **Purchase Invoices** — prototype invoices are sales-only; expenses are one-off.
9. **WhatsApp Engine** *(promised §9)* — template library, template→module/event mapping, message history log, bulk broadcast. Prototype has only a Settings integration card + activity-type labels.
10. **Internal Chat / Messaging** *(promised §9; live ERP has Messaging)* — staff conversations, channels.
11. **AI Chatbot / Copilot** *(promised §9; roadmap #3)* — live AI support tied to Knowledge Base + usage analytics.
12. **Calendar** *(promised §8)* — events, reminders, meeting scheduling. Zero calendar in prototype.
13. **Announcements** *(promised §8; live ERP has Announcements)* — internal broadcast board.
14. **Bulk PDF / e-Invoice / CSV Export utilities** *(promised §8)* — batch document generation (prototype has per-table CSV + print only).
15. **Timesheets** *(promised §2)* — staff time entry per project/task, billable hours.
16. **Attendance check-in/check-out (punch) tracking** *(promised §2)* — live ERP Attendance.
17. **Shift Management** *(live ERP: Work Shift Table, Shift, Shift type)* — rostering.
18. **Staff Contracts & Insurance** *(live ERP HR: Contract, Insurance, Salary)*.
19. **Unsold Plot / Flat Balance ledger** *(promised §3)* — open inventory per project/block, availability report.
20. **Customer Segmentation Groups** *(promised §1)* — segment customers (NRB, investor, owner, prospect) for targeting.
21. **Module enable/disable switches + Menu Setup UI** *(promised §1; live ERP Menu Setup)*.
22. **GDPR / Data Privacy settings** *(promised §1)* — consent, data export, right-to-erasure.
23. **Sales Territories, Targets, Stages config** *(CRM proposal Sales Management)*.
24. **Goods Receive / Stock Entry for materials** *(CRM proposal Stock)* — receive against PO, stock entry, stock balance per item, valuation.

### B. IMPROVE EXISTING MODULES

25. **Currency consistency — BUG:** 59 `₹` remain in mock data (bookings BKG-105+ etc.) vs 232 `৳`. Replace all with `৳`. *(verifiable in dashboard Recent Bookings)*
26. **HR:** leave approval workflow (manager approve/reject, escalation); check-in/out tab; timesheets; shifts; contract/insurance records; payroll → payslip e-delivery.
27. **Finance:** link Chart of Accounts to transactions; journal entry tab; reconciliation; fund transfer; purchase invoices; credit notes; fiscal year & period lock; opening balances; audit statements (SFP/SCI/SCE/SCF); VAT challan tracking.
28. **Flats & Units:** add **"Under Payment"** status (installment in progress) — today only Available/Booked/Reserved/Sold/Registered; per-unit payment schedule; per-unit legal document store (mutation, agreement, handover docs).
29. **Plots & Blocks:** unsold balance per block; land sales register; generate plots from Layout Builder; plot rate history.
30. **CRM & Leads:** lead source config; sales territories/targets; cost-estimate fields on proposals; automated follow-up reminders (SMS/Email/WhatsApp triggers); lead→booking conversion flow.
31. **Dues & Recovery:** **automated dues notifications** (WhatsApp/SMS/Email templates fired on due dates) *(promised §5)*; collection call log; ageing report export.
32. **Bookings:** payment schedule/terms per booking (CRM proposal Payment Terms); partial-payment tracking; deposit receipt printing; cancellation/refund flow.
33. **Stock & Procurement:** goods receive against PO; stock entry; stock balance per item; low-stock alert rules; valuation summary; PO → invoice link.
34. **Customer Portal:** make it a real client-facing portal (roadmap #6) — client login, own bookings/dues/payment history, unit documents, maintenance requests, chat.
35. **Notifications:** template management (Email & Message Templates); history log; send custom SMS/email; per-user preferences.
36. **Reports / BI:** live statement generation (SFP/SCI/SCE/SCF), PDF/Excel export, scheduled email reports, drill-down.
37. **Settings:** module enable/disable; menu setup; GDPR; business settings (company profile, fiscal year); integration config functional states.
38. **Backup & Restore:** functional upload/restore (real JSON export/import to file), encryption indicator, off-site storage, retention policy config UI.
39. **Permissions:** field-level permissions; approval-workflow config (who approves what); module-scoped roles.
40. **Projects:** site progress photo upload; milestone approvals; Gantt export; contractor payment linkage.
41. **Layout & Unit Builder:** save/share layouts; auto cost estimate (plots × block rate); export layout PDF.
42. **System Manual:** regenerate to cover all new modules; add Bengali version.

### C. TECHNICAL / ARCHITECTURE UPGRADES (roadmap)

43. **Real backend (roadmap #7)** — Flask/FastAPI + PostgreSQL; server-side auth & RBAC; real persistence; server-side audit log.
44. **Payment Gateway simulation (roadmap #2)** — bKash / Nagad / SSLCommerz flows for advance & installments.
45. **AI Copilot bubble (roadmap #3)** — in-app assistant across modules.
46. **Customer Portal (roadmap #6)** — public-facing portal.
47. **Mobile app** — promised in ERP proposal (integration + auth for staff & clients); prototype already PWA — build APK.
48. **Data migration tooling** — import existing Perfex/Excel master data (promised "import master backup").
49. **e-Invoice / VAT compliance** — NBR-ready invoice numbering, 5% VAT, TDS on contractor (10%), AIT on land (3%) — prototype Settings has rates; apply in invoice engine.
50. **Multi-tenant SaaS + per-module subscription** (V8 core goal, Odoo-like) — tenant isolation, license enforcement, MMC suspension logic.
51. **Server-side immutability for audit trail**; document versioning.
52. **Real integrations** — WhatsApp Business API, Twilio SMS, SendGrid SMTP, bKash/Nagad, Zoho Books sync (settings card already lists them).

### D. BUSINESS / SLA-ALIGNED

53. **MMC/license enforcement UI** — subscription status, grace period, suspension notice (aligns with SLA §4).
54. **In-app onboarding & Train-the-Trainer materials** (SLA training commitment).
55. **Self-serve custom report builder** (proposal promises 4–7 day custom reports → reduce turnaround).
56. **Implementation checklist / go-live tracker** in-app (SLA milestones Jul 2026 – Jan 2027).

---

## 4. Recommended priority order

**Phase 1 — Quick wins (prototype-level, 1–2 days each):**
25 (currency fix) · 28 (Under Payment status) · 19 (unsold balance) · 21 (module toggles + menu setup) · 12 (calendar) · 13 (announcements) · 6 (fund transfer) · 2 (journal entries mock) · 16 (check-in/out) · 26 (leave approval) · 35 (notification templates) · 15 (timesheets) · 14 (bulk exports)

**Phase 2 — Contracted gaps (prototype-level, 2–4 days each):**
1 (investment/loan) · 4 (audit statements) · 3 (reconciliation) · 9 (WhatsApp engine) · 10 (internal chat) · 11 (AI chatbot) · 5 (fiscal year/periods) · 7 (credit notes) · 8 (purchase invoices) · 22 (GDPR) · 20 (segmentation) · 23 (territories/targets) · 24/33 (goods receive & stock balance) · 17/18 (shifts, contracts/insurance)

**Phase 3 — Architecture (roadmap):**
43 backend · 44 payment gateway · 45 AI copilot · 46 customer portal · 47 mobile app · 50 multi-tenant SaaS · 52 real integrations · 53 license/MMC enforcement

---
*Full analysis sources: /tmp/mars_docs/{erp_proposal,work_order_sla,crm_proposal}.txt (extracted) + live ERP menu dump.*
