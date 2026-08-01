# REM ERP — V10 Update Plan (next major version)

**Date:** 2026-08 · **Author:** AJ
**Target:** fork `docs/design-prototype-v9.html` → `docs/design-prototype-v10.html` (keep V9 archived), SW v10-v1, per-commit bumps.
**Sources:** `docs/improvement-plan.md` (contracted gaps vs BITSCOL proposals + live MARS ERP), `docs/implementation-plan-ab.md`, `docs/v9-demo-plan.md`, `docs/demo-script.md`, recent V9 commits.

---

## 1. Current state (V9, SW v9-v8, HEAD `7332934`) — what's already done

- **51 modules / 11 groups**, PWA + SW + Cloudflare tunnel; demo-ready (`docs/demo-script.md` 9-step MARS run-through, all PASS).
- **RBAC**: role dashboards (Super Admin / Sales / Engineer / Finance), `ROLE_MODULES` + 9-role permission matrix, gated `switchModule`, `setRole` landing, live perm propagation.
- **Payment core** (recent V9 additions): shared `applyPaymentRipple` — Cleared payments move invoice status + dues ledger + inflow txn + booking schedule; Pending stays inert until approval. Party Ledger module (customers/suppliers/brokers/employees, running-balance ledger, 💳 Collect against unpaid/overdue invoices, partial payments, bulk collect, 📋 Queue for Approval, batch approve/reject, reconciliation). Print fixed (popup-safe `_printDoc`). Invoice/installment logic audit (advance→schedule, payment→installments, Cleared-only status).
- **Already covered from improvement-plan** (V8/V9): currency ৳-only, Under Payment unit status, module toggles (Module Manager), calendar, announcements, fund transfers, journal entries (mock), reconciliation tab, audit statements (SFP/SCI/SCE/SCF), credit notes, purchase invoices, investment & loans, WhatsApp engine (templates/broadcast/log), internal chat, AI copilot, territories/targets/stages, goods receive + stock balance, shifts, contracts/insurance, payment heatmap, financial approvals, ticketing, knowledge base, dual-language, CSV import, backup/restore UI.

## 2. Remaining contracted / roadmap gaps (candidates for V10)

| # | Gap | Source | Notes |
|---|---|---|---|
| G1 | **e-Invoice / VAT compliance engine** — NBR-ready numbering, 5% VAT, TDS 10% contractor, AIT 3% land, VAT challan tracking | proposal §6, improvement #49 | Settings has rates; invoice engine doesn't apply them yet |
| G2 | **Fixed Assets register** | proposal §6 (SFP line) | new module: asset classes, depreciation (straight-line), net book value, disposal |
| G3 | **Functional backup/restore** — real JSON export/import to file, retention policy UI, encryption indicator | proposal §10 | UI exists; wiring is fake |
| G4 | **Data migration tooling** — import master data from live Perfex (erp.appvaley.com) / Excel: customers, plots, units, dues | proposal "import master backup" | we already know the Perfex API/CSRF pattern |
| G5 | **MMC / license enforcement UI** — subscription status, grace period, suspension notice (7-installment SLA) | SLA §4, improvement #53 | closes the business loop for MARS |
| G6 | **Implementation checklist / go-live tracker** in-app (SLA milestones Jul 2026–Jan 2027) | improvement #56 | 7-installment delivery tracker |
| G7 | **Automated dues notifications** — fire WhatsApp/Email templates on due dates from Dues & Recovery | proposal §5, improvement #31 | reminders tab exists; hook template firing |
| G8 | **Bulk PDF / e-Invoice / CSV export utilities** — batch document generation | proposal §8, improvement #14 | per-table CSV exists; batch PDF doesn't |
| G9 | **Audit trail immutability + document versioning** | improvement #51 | activity log exists; make exportable/versioned |
| G10 | **GDPR / data privacy settings** — consent, data export, right-to-erasure | proposal §1, improvement #22 | settings card only |
| G11 | **Unsold Plot / Flat balance ledger** report — open inventory per project/block + availability | proposal §3, improvement #19 | data exists (plots/units) — needs the register view |
| G12 | **Customer segmentation groups** — NRB/Investor/Owner/Prospect targeting | proposal §1, improvement #20 | CUST_GROUPS exists; operationalize in CRM filters + campaigns |

## 3. Recommended direction — **V10: "Compliance & Delivery Readiness"**

Two reasons: (a) the contracted scope's remaining items are mostly finance/compliance + delivery mechanics (G1–G12); (b) MARS presentation is done — the next win is making the **deployment story** real (license, migration, backup, e-invoice) so the client signs off on installments.

**Method (unchanged invariants):** fork V9 → renumber v10 (title/sidebar/subtitle/print footer/SW/manifest) → data-driven module architecture (GROUPS / dispatch / search / Quick-Add / permissions / Bengali) → `DB._seedV` bumps on seed changes → syntax-check extracted JS → browser verify each phase → commit + push per phase → refresh `/tmp/REM-ERP-v10-latest.html`.

---

## Phase A — e-Invoice / VAT compliance engine (≈3–4h)
- A1. Invoice engine applies VAT/TDS/AIT: invoice form gains Tax Basis fields (VAT 5%, TDS %, AIT %) → line-level tax lines, Net = Subtotal ± tax; invoice template + print show tax breakdown. (≈60m)
- A2. NBR-ready numbering: `INV-2026-0001` sequence + VAT challan reference field; VAT register view (tax_entries already exists — link to invoices). (≈45m)
- A3. Purchase invoice linkage: PO → invoice (poRef exists) → supplier payable aging in Party Ledger (already reads Purchase invoices — deepen with tax + due aging buckets). (≈45m)
- A4. Credit note flow: reverse a sales invoice (CN-XXX), reopen customer dues, ripple. (≈45m)
- A5. Fixed Assets module (new, Finance group): asset register, depreciation schedule, NBV report; SFP statement picks up NBV. (≈60m)

## Phase B — Data & compliance mechanics (≈3h)
- B1. Functional backup/restore: export all `rem_*` localStorage keys → downloadable JSON; import restores; retention + encryption indicator UI. (≈45m)
- B2. Audit trail: activity log export (CSV/JSON) + per-entity version history on edit (store snapshots). (≈45m)
- B3. GDPR settings: consent flags per customer, "export my data" (JSON), right-to-erasure (delete customer + linked demo records). (≈30m)
- B4. Unsold plot/flat balance ledger: register per project/block (available/reserved/sold counts + value), availability report. (≈30m)
- B5. Customer segmentation operational: segment filter in CRM + portal, segment-based quick views. (≈30m)

## Phase C — Delivery / SLA readiness (≈2–3h)
- C1. MMC license UI: subscription status card (installed/grace/suspended), 7-installment payment tracker (maps to Work Order), suspension notice + read-only mode. (≈60m)
- C2. Implementation checklist: go-live tracker with SLA milestones (Jul 2026–Jan 2027), per-module sign-off. (≈30m)
- C3. Automated dues notifications: Dues & Recovery fires WhatsApp/email template (from WhatsApp Engine library) for Due Today / Overdue accounts; log to whatsapp_log. (≈45m)
- C4. Bulk PDF/CSV export: batch invoice/receipt PDF pack (reuse `_printDoc` capture → save), CSV export for any table. (≈45m)
- C5. Demo scenario pack v2: extend `demo-script.md` with the new features (e-invoice print, credit note, backup/restore, license tracker) for the closing presentation. (≈30m)

## Phase D — Dry-run & release (≈1h)
- Re-run the full demo script + new scenarios against the live build; zero console errors; offline SW still serves; pristine counts; refresh `/tmp` copy; commit `v10-release` + push.

**Total ≈ 9–11h** of agent work, 7–9 commits.

---

## 4. Alternative directions

| Option | Scope | When |
|---|---|---|
| **A. V10 Compliance & Delivery (recommended)** | Phases A–D above | Now — no user input needed, low risk |
| **B. Backend build (full-stack realization)** | improvement-plan Phases 0–6 (Flask+SQLite→Postgres, real auth/RBAC, REST APIs, UI rewiring, PDF, deploy) | After V10 — **needs the 5 open decisions** |
| **C. Packaging push** | APK wrap, permanent hosting/domain (diziconcard.com), Vercel deploy, .html artifact | 1–2 days, parallel with A |
| **D. MARS data migration pilot** | Pull real master data from erp.appvaley.com (Perfex) into the prototype (plots/units/customers/dues) | 1–2 days — high client impact, needs access confirmation |

---

## 5. Open decisions (need your call before execution)

1. **Scope:** go with **A (V10 Compliance & Delivery)**? Or trim to A+D, or full A–C?
2. **Backend go/no-go** (carried over, now due): direction (full-stack vs keep prototype), DB (SQLite vs Postgres), framework (Flask vs FastAPI vs Django), auth (session vs JWT), deploy target (Lightsail+tunnel vs domain). — *recommendation: prototype-first until MARS signs installment 2; start backend Phase 0–1 right after.*
3. **Migration pilot (D):** OK to log into erp.appvaley.com and pull real master data into the demo? (client data in prototype — confirm with MARS first)
4. **Packaging (C):** include APK + permanent tunnel in this update, or separate?

---

## 6. Deliverables this update
1. `docs/design-prototype-v10.html` (V9 archived) — SW v10-vN, pushed per phase.
2. e-Invoice/VAT engine + Fixed Assets + credit note flow.
3. Functional backup/restore + audit export + GDPR.
4. MMC license tracker + implementation checklist + automated dues notifications.
5. Extended demo script + dry-run PASS; live tunnel at presentation state.

---

## Status (2026-08) — COMPLETE ✅

- **Phase A** (`d0b42d8`, SW v10-v2): e-Invoice/VAT engine — VAT/TDS/AIT on invoices (Net = Amount + VAT − TDS − AIT, `invNet()` drives outstanding/due everywhere), NBR numbering (`INV-2026-0001` + challan), VAT Register card, supplier Payable Aging in Party Ledger, Credit Notes wired from invoice modal + Applied ripple (dues + reversal txn), new **Fixed Assets** module (8 assets, depreciation, SFP NBV line). Verified: net math, register, CN 10L→8L, aging; 0 JS errors.
- **Phase B** (`1a5598d`, SW v10-v3): functional Backup & Restore (103-collection JSON export/import), Activity Log CSV export + invoice version history (🕓), GDPR Export/Erase in party detail, Unsold Balance Ledger in Projects, segmentation verified. Verified: erase 11→10, ledger rows; 0 errors.
- **Phase C** (`aebfa88`, SW v10-v4): new **License & SLA** module (7-installment Work Order tracker ৳8L, checklist w/ owners, Grace/Suspended simulation + read-only banner), automated dues reminders (WhatsApp templates → whatsapp_log + notifications), bulk invoice print pack + table CSV export, demo-script.md v2. Verified: license sim, reminders 7→15, fns; 0 errors.
- **Phase D**: dry-run PASS — all new modules render, pristine 25/17/12/12/8, zero console errors; release SW v10-v5.
- **Now 53 modules / 11 groups.** `docs/demo-script.md` updated for V10.

---

## Alternative B — Backend build (started 2026-08, auto per user)

**Phases 0–2 delivered** (`backend/`): Flask 3 + SQLite app mirroring the prototype.
- **Phase 0 — Foundation:** app skeleton, SQLite schema (users, leads, customers, projects, bookings, invoices, payments, dues, transactions, activity_log, fixed_assets, license), seed script (4 users / 15 leads / 10 customers / 6 projects / 12 bookings / 8 invoices / 12 payments / 8 dues / 15 txns / 6 assets / license).
- **Phase 1 — Auth & RBAC:** session login (Werkzeug password hashes), `ROLE_MODULES` server-side guards (403 on cross-role access), activity audit log.
- **Phase 2 — Core APIs:** REST CRUD for leads/customers/projects/dues/assets, bookings (BKG-XXX ids), invoices (NBR `INV-2026-XXXX` + VAT/TDS/AIT net computation), payments with the full ripple (Cleared → invoice status + dues ledger + cash-flow txn), license (7-installment tracker), unpaid-invoices report.
- **Verified live:** admin/finance login, bad-password 401, Finance→leads 403 / Finance→invoices 200, VAT invoice INV-2026-0001 net ৳10.5M, payment PAY-013 → INV-002 Overdue→Partial + Rubina dues 10L→8L, license status toggle, report outstanding.
- **Phases 3–4 shipped** (2026-08, `7debe5a` + `4761161`, SW v10-v10): **Server Sync** — prototype Settings → Server Sync panel (Connect/push/pull/disconnect, Bearer token auth, CORS), write-through of every save (debounced), `doc_store` + `GET /api/bootstrap` + `POST /api/sync`; **reports** — server-side PDF (invoice w/ VAT table, VAT register) + CSV/XLSX export of any synced collection. Verified E2E: connect auto-pushed full seed, live write-through, real PDF bytes.
- **Phase 5 deployed** (2026-08, `96683de`, SW v10-v11): gunicorn 3 workers under systemd (`rem-erp-backend`, auto-restart, port 5001), nginx reverse proxy with permanent sslip.io hostnames, **Let's Encrypt HTTPS** (certs to 2026-10-30, auto-renew): `https://rem.18.142.98.150.sslip.io` → backend API, `https://app.18.142.98.150.sslip.io` → PWA. HTTP→HTTPS 301. Prototype default sync URL now points at the permanent backend. **One action left: open TCP 443 in the Lightsail firewall** (port 80 already open) for public HTTPS.
- **Remaining:** Phase 6 portal + bKash/Nagad payment gateway.
- Run: `systemctl start rem-erp-backend` (auto-start on boot). README in `backend/`.
