# REM ERP v10 — MARS Client Demo Script (18–25 min)

**Version:** SW v10-vN · **Build:** `docs/design-prototype-v10.html` (PWA)
**Live URL:** https://monkey-window-fort-labor.trycloudflare.com/design-prototype-v10.html
> ⚠️ Tunnel resets on server restart — regenerate with `cloudflared tunnel --url http://localhost:8877` before presenting and swap the URL in.
> **Always hit `↺ Reset Demo Data` (Switch Role panel) before the client arrives** — the demo starts pristine.

**Pitch line:** 52 modules / 11 groups · per-module subscription · offline PWA · NBR-compliant e-invoicing · license & SLA tracker · path to live backend — proposal ৳800,000.

---

## Pre-flight checklist (5 min before)

1. `curl -s https://<tunnel>/design-prototype-v10.html -o /dev/null -w "%{http_code}"` → `200`.
2. Open in Chrome → `↺ Reset Demo Data` → reload lands Super Admin.
3. Verify pristine counts (top-left quick stats): **25 leads · 12 invoices · 12 payments · 17 bookings · 12 projects · 12 employees · 30 txns**.
4. Console clean (F12 → Console → no red).
5. Check offline: DevTools → Network → Offline → reload → app still renders (SW `rem-erp-v10-vN`).

---

## Step 1 — PWA / Offline (2 min)

**What to do**
1. Point out the header **📲** button: "installable on desktop and mobile, works without internet."
2. DevTools → Network → **Offline** → reload → app still renders from the service worker (cache `rem-erp-v10-vN`). Toggle online back.
3. **V10 extra:** System → Backup & Restore → `⬇ Export Backup JSON` — the whole demo database (103 collections) downloads as one file; `📥 Restore from File` brings it back. "Your data is never locked in."

---

## Step 2 — Executive overview (2 min)

1. Dashboard KPIs: **21 plots available · ৳31.6 Cr sales · 17 bookings · 12 projects / ৳626 Cr**.
2. `Ctrl+K` → type **Jolshiri** → click result → jumps into Bookings (global data search).
3. **V10 extra:** Projects tab → bottom card **📒 Unsold Balance Ledger** — per-project plots/units available, sold, open balance. "The land inventory is always visible."

---

## Step 3 — Projects & inventory (2 min)

1. Projects → **Jolshiri Abason** → 65% progress, milestones, plot availability.
2. Stock & Procurement → 18 items (Critical 3 / Warning 2).
3. **V10 extra:** Accounts & Finance → **Fixed Assets** — land/building/vehicles/equipment register with straight-line depreciation schedules and Net Book Value; SFP (Balance Sheet) includes Fixed Assets NBV.

---

## Step 4 — Live sales cycle (3 min)

1. Sales & CRM → **+ New Lead** → "Demo Client" (Jolshiri Abason, Flat, Real Estate Fair, ৳85L) → Contacted → Site Visit → Negotiation.
2. **Convert to Booking** → unit picker is Jolshiri-only (A3), price ৳1.75 Cr, 10% down + 18 monthly → **BKG-119** with 19-installment schedule; the ৳17.5L down shows **Paid** in the schedule (advance-aware).
3. Lead → Booking stage. Unit → Under Payment.

---

## Step 5 — Live finance & e-invoice (3 min)

1. Switch role → **Finance** → ⬇ Receive → ৳5L for Dr. Rubina Ali → INV-002 Overdue → **Partial**, dues 10L→5L, cash flow moves.
2. **V10 extra — e-Invoice:** Invoices → **+ New Invoice** → ৳10,000,000 with **VAT 5%** + challan ref → saves as **INV-2026-0001** (NBR-ready numbering) with Net = ৳10.5M; the **VAT Register** card below the table shows the VAT line; 🖨 Print shows the tax breakdown (Subtotal / VAT / Net Payable / Due).
3. Open INV-002 → **💳 Collect** → pick invoice → partial amounts allowed → Collect Selected or **📋 Queue for Approval**.
4. Party Ledger → **Approvals** tab → ✓ Approve the queued payment → invoice Paid, dues cleared.
5. Open an unpaid invoice → **🧾 Credit Note** → Issue → Apply → the customer's dues reduce + a reversal transaction is logged.

---

## Step 6 — Engineer (1 min)

1. Switch role → **Site Engineer** → P-101 → 65% → 72%; stock alerts.
2. Zero console errors.

---

## Step 7 — Permissions & Party Ledger (2 min)

1. Super Admin → Permissions → 9-role matrix; toggle CRM Create off for Sales Agent → **+ Add Lead disappears**; on → back.
2. **V10 extra — Party Ledger:** 35 parties (Customers/Suppliers/Brokers/Employees) with receivable/payable balances; open a supplier (e.g., Shah Cement) → **Payable Aging** (1-30 / 31-60 / 60+ days); open a customer → ledger + **🛡 Export Data** / **🗑 Erase Data** (GDPR right-to-erasure).

---

## Step 8 — Customer portal (2 min)

1. Customer Portal → **Client Login** → Dr. Rubina Ali → dues ৳5L reflect the Step-5 payment live.
2. **💳 Make Payment** in the portal → shows her unpaid invoices → process a payment as the client.
3. View bookings, payment history, documents.

---

## Step 9 — License, SLA & close (2 min)

1. **V10 — License & SLA** (System group): contract ৳800,000, 7-installment Work Order tracker (2 paid, 5 ahead), implementation checklist with owners (BITSCOL/MARS) — "here is your delivery roadmap with the SLA."
2. Simulate **Grace** → ⚠ banner; **Suspended** → ⛔ read-only notice → **Reactivate**.
3. Close: "Same UI, live backend next — this prototype is the spec. Proposal ৳800,000, 7 installments."

---

## Cheat sheet (numbers to quote)

- 52 modules / 11 groups; 35 parties; 12 projects / ৳626 Cr; 25 leads; 17 bookings / ৳31.6 Cr; 12 invoices; 12 payments / ৳7.12 Cr; 9 dues / ৳5.19 Cr; 8 fixed assets / NBV ৳35.24 Cr.
- INV-002 = ৳2.2 Cr Overdue; Rubina due ৳10L → ৳5L after demo payment.
- Contract ৳800,000 · 7 installments · server ৳12,000/mo · support ৳10,000/mo (SLA).
- New invoice: INV-2026-0001, 10M + 5% VAT → net 10.5M.

## Pitfalls

- **Reset Demo Data before client arrives** (native confirm — accept it).
- Demo conversion must use a unit-bearing project (**Jolshiri**) — Skyline Towers has no seed units.
- Tunnel URL resets on restart — regenerate + swap.
- Portal login is a customer dropdown + email match, not a password.
- V10 `entity_versions` / `license` seeds auto-reset via `DB._seedV` on version bump.
