# V9 Next Phase — MARS Client Demo Run-Through (Demo-Ready Polish)

**Status:** Phase A ✅ DONE (SW v9-v5) · Phase B ✅ DONE (SW v9-v5) · Phase C ✅ DONE (SW v9-v5) · Phase D ✅ DONE (SW v9-v5)
**Base:** af2ad06 (SW v9-v4, RBAC complete) · **Target:** SW v9-v5
**Why this phase:** "Client demo polish — run through the flow as if presenting to MARS" was
user-selected earlier but never delivered. Role dashboards (v9-v2) + role-based access (v9-v4)
are done, so the demo story is now whole. Goal: a 15–20 min walkthrough that sells the
৳800,000 MARS proposal — 50 modules / 11 groups, per-module subscription model, offline PWA.

---

## Phase A — Demo-critical fixes (must-fix before presenting)

### A1. Consistent record IDs (High)
Form-created bookings/projects get **numeric** IDs (`118`) while seeds use `BKG-101…117` /
`P-101…112`; the lead→booking conversion already emits `BKG-XXX`. Mixed formats look broken in a demo.
- Make `nextId(arr, prefix)` prefix-aware: scan numeric suffixes, return `prefix + (max+1)`.
- `crudBooking` → `nextId(mockBookings,'BKG-')`; `crudProject` → `nextId(mockProjects,'P-')`.
- Verify: new booking shows `BKG-118`, new project `P-113`; existing numeric records (if any in localStorage) still render.

### A2. Payment auto-adjusts invoice + dues (High)
Recording a payment doesn't reduce the linked invoice balance or the customer's dues account
(known F7 finding). In the demo "record payment → dues drop" is a natural expectation.
- On `crudPayment` save with `invoiceId`: compute paid-so-far; if `>= invoice.amount` → `status='Paid'`, else keep (optionally set status='Partial' display).
- Also decrement the matching `mockDues` record (by customer) by the amount; floor at 0; flip status to `Upcoming/Paid` when cleared.
- Push an inflow transaction into `mockTransactions` so the Finance dashboard cash flow moves.
- Verify: PAY on Rubina INV-002 → invoice due text drops, dues account decreases, bank/cash stat updates.

### A3. Conversion unit picker project-filtered (Medium)
`convertLeadToBooking`'s unit dropdown lists units from **all** projects. Filter to the lead's project only.
- Verify: converting a Jolshiri lead shows only Jolshiri units.

### A4. "Reset Demo Data" button (Medium, high demo value)
Presenters need a one-click restore to pristine seed state.
- Add button in Settings → System (or header menu): confirm → `localStorage.clear()` → reload.
- Verify: reload lands on Super Admin with 25 leads / 17 bookings / 12 payments / 12 projects / 20 entities.

### A5. Stale-date sweep (Low)
Check "Today/Tomorrow/Overdue" follow-up strings and 2026 dates still render sensibly; no frozen "X days ago" that looks wrong at presentation time.

---

## Phase B — Demo polish & per-role report packs (the sell)

### B1. Per-role report packs (one-click print/export)
Folds in the previously-suggested "reporting deep-dive". Each role dashboard gets a "Print Report" button:
- **Sales Agent** → Pipeline Report (pipeline by stage, hot leads, conversion trend, recent bookings).
- **Finance** → Cash Position Report (bank balances, monthly cash flow, overdue invoices, top dues).
- **Site Engineer** → Construction Progress Report (project progress, unit availability, inventory alerts).
- Reuse existing print template infra (`_INV_TPL_*` style) → `window.print()` with a print-only report section, or a clean printable overlay.
- Super Admin keeps executive dashboard print.

### B2. Print CSS for role dashboards
Ensure the printed report pages are clean (no sidebar/toolbar bleed) — add `@media print` rules scoping print output to the report card.

### B3. (Optional, only if time) Demo-mode banner
Subtle "DEMO" chip in header so the presenter can show they're in a sandbox; skip if A4 covers reset expectations.

---

## Phase C — Demo script (`docs/demo-script.md`)

Write a 15–20 min presentation script with exact clicks/navigation/values:

1. **PWA/offline (2 min)** — install prompt, airplane-mode reload still renders (SW).
2. **Super Admin (3 min)** — executive dashboard: ৳626 Cr portfolio, ৳31.6 Cr bookings, cash position; Ctrl+K search; 50 modules / 11 groups.
3. **Projects & inventory (2 min)** — 12 projects, Land/Flat standardization, plot/unit availability, project detail (milestones + progress).
4. **Sales cycle live (4 min)** — switch to Sales Agent → New Lead (type-driven) → advance → convert → BKG-XXX booking + schedule.
5. **Finance live (3 min)** — switch to Finance → receivables ৳5.19 Cr, overdue invoices → record payment → dues drop (A2) → cash flow moves.
6. **Site Engineer live (2 min)** — switch → progress update (A-progress field) → inventory alerts.
7. **Permissions (2 min)** — 9-role matrix, toggle a permission, see it bite live.
8. **Customer portal (2 min)** — client login → own dues/payments/docs/maintenance.
9. **Close (1 min)** — 50 modules, per-module subscription, offline PWA, path to live Perfex backend (erp.appvaley.com).

Include a **demo cheat sheet**: keyboard shortcuts, exact records to create, numbers to quote.

---

## Phase D — Dry-run & verification

- Rehearse every script step against the live build; log pass/fail; fix any break.
- Zero JS errors across the entire walkthrough (console watch).
- Offline (SW `rem-erp-v9-v8`) still serves after changes.
- Pristine counts verified before presenting.
- Refresh `/tmp/REM-ERP-v9-latest.html`; commit + push `master`.

**Results (2026-08-01):** All 9 script steps PASS against live build — Step 1 SW/offline (cache holds current HTML incl. fixes), Step 2 exec + Ctrl+K global search (fixed double-handler conflict → data search only, palette on `/`), Step 3 projects/inventory (12/৳626 Cr, P-101 65%, stock Critical 3/Warning 2), Step 4 full sales cycle (lead → Contacted/Site Visit/Negotiation → convert → BKG-118, Jolshiri-only picker, 19-installment schedule), Step 5 Finance receive (INV-002 → Partial, dues 10L→5L Upcoming, PAY + inflow — `crudReceivePayment` now mirrors A2; button only existed in CRM before), Step 6 Engineer (P-101 65→72%, stock alerts), Step 7 Permissions (9-role matrix, CRM Create off → + Add Lead gone; on → back), Step 8 Portal (Rubina login → dues ৳5L reflects Step 5 payment live), Step 9 Print Report (clean exec report). Console: 0 app JS errors (2 empty exceptions were test-stub artifacts, not reproducible with error hooks). Pristine restored 25/17/12/12/20. Committed + pushed.

---

## Deliverables
- Commit `A1–A5 + B1–B2` (SW v9-v5), pushed to origin/master.
- `docs/demo-script.md` (script + cheat sheet).
- Live tunnel verified at presentation state.

## Effort estimate
A1 ~30m · A2 ~45m · A3 ~20m · A4 ~15m · A5 ~10m · B1/B2 ~60m · C ~45m · D ~30m — **≈ 4–5h total**

## Parked (not in this phase)
- Backend build (V7 5-question go/no-go still open).
- `.html` packaging / APK / Vercel / permanent tunnel; AFM Medimart items.
- Low findings: payment terms fixed 5-option list (partially covered by A2), legacy free-text select preservation (already handled), form-created lead numeric IDs (seed norm — acceptable).
