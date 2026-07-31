# REM ERP — Next Big Update Plan

**Current state:** V5 static prototype (`design-prototype-v5.html`, ~1MB, commit `c435b15`) — 29+ modules, RBAC, CRUD, Analytics, Activity Log, Payment Reminders, CSV Import, Floor Plan, Proposals. All data in localStorage (simulated persistence).

---

## Recommended direction: **V6 — Full-Stack Realization**

Turn the validated prototype into a real, deployable ERP. Keep the exact same UI/UX — replace the fake data layer with a real backend.

**Why this first:** the prototype has proven the design; the bottleneck now is that nothing is real (no auth, no persistence, no reports, no deployment). Everything else (portal, mobile, multi-tenancy) depends on having a real backend.

---

## Phase 0 — Foundation (≈1 wk)
- Flask app skeleton with blueprints (`crm`, `properties`, `finance`, `bookings`, `system`)
- SQLite schema mirroring every mock data structure (properties, units, customers, leads, bookings, invoices, payments, proposals, activity_log, users, roles)
- Seed script: parse V5 mock arrays → DB rows (data migration)
- Config/env management, logging

## Phase 1 — Auth & RBAC (≈1-2 wk)
- Login/register, bcrypt password hashing
- Session/JWT auth
- Role-permission matrix mapped from the existing `data-perm` RBAC design
- Server-side permission enforcement (not just UI hiding)
- Real audit log table (UI already exists in V5)

## Phase 2 — Core Module APIs (≈2-4 wk)
- REST endpoints per module: CRUD + search/filter/pagination
  - CRM: customers, leads, contacts, proposals
  - Properties: projects, units, floor plans, bookings
  - Finance: invoices, payments, transactions, dues
  - System: activity log, reminders, settings
- Input validation + error handling
- API docs (OpenAPI/Swagger)

## Phase 3 — UI Rewiring (≈2 wk)
- Replace all `DB.init()` / localStorage reads with `fetch()` calls
- Keep V5 feature set working: Analytics (live data), Payment Reminders (real overdue), CSV Import (writes to DB), Floor Plan, Activity Log (real)
- Loading states, optimistic updates, error toasts
- Cross-module navigation now hits real endpoints

## Phase 4 — Reports & Export (≈1-2 wk)
- PDF invoices/receipts (reportlab or weasyprint)
- Excel/CSV export (openpyxl)
- Report builder: occupancy, sales pipeline, payment collection, revenue vs expense

## Phase 5 — Deployment (≈1 wk)
- Gunicorn + systemd on AWS Lightsail (18.142.98.150)
- Cloudflare tunnel for HTTPS (matches existing setup)
- Backup/restore: scheduled SQLite dumps → S3
- Env secrets management

## Phase 6 — PWA + Customer Portal (≈2 wk, next update)
- PWA manifest + service worker → installable on Android/iOS
- Customer-facing portal: view unit, payment schedule, download invoices
- Payment gateway hooks (bKash/Nagad/SSLCommerz — sandbox first)

---

## Alternative directions (if you prefer)

| Option | Scope | When |
|---|---|---|
| **A. Full-stack (recommended)** | Phases 0-5 above | Now |
| **B. Customer Portal + PWA** | Public portal + payments first, backend later | Needs some backend anyway |
| **C. Microservices/multi-tenant** | Odoo-style per-module subscriptions | After full-stack works |
| **D. Report/BI engine** | Heavy reporting + exports on top of V5 | 1-2 wk quick win |

---

## Deliverables this update
1. Deployable Flask+SQLite app serving the V5 UI
2. Real auth + server-side RBAC
3. All 29 modules working against a real database
4. PDF/Excel export for invoices & reports
5. Live on AWS Lightsail behind HTTPS

## Open decisions needed from you
1. **Direction:** go with A (full-stack) or another option?
2. **Database:** SQLite (easy, single-file) vs PostgreSQL (multi-user, prod-grade)?
3. **Framework:** Flask (matches existing dashboard pattern) vs FastAPI vs Django?
4. **Auth:** simple session login vs JWT with refresh tokens?
5. **Deployment target:** keep AWS Lightsail + Cloudflare tunnel, or dedicated domain?

---
## V8 Reorganization Log (master)
- `87c2dbe` — Sales & CRM / Bookings & Customer split: Dues & Recovery → Bookings & Customer; new **Ticketing & Issue** module (8 seed tickets, full CRUD + detail panel + filters). SW v8-v5.
- **HEAD — Admin & Operations / Legal & Compliance / Accounts & Finance reorg** (SW v8-v6):
  - Renamed group `hr_admin` label → **Admin & Operations** (icon 👥).
  - Renamed group `finance_admin` label → **Accounts & Finance** (icon 💰).
  - New group **Legal & Compliance** (⚖️, 10th sidebar group): **Compliance** moved out of Engineering & Construction; new **Legal Contracts** module (7 seed contracts: land purchase, NDA, construction, utility, sales agreement, vendor framework, JV — full CRUD + detail + activate flow + expiry tracking).
  - New sub-module **Financial Approvals** under Accounts & Finance (8 seed requests: expense/vendor/contractor/refund — Pending/Approved/Rejected workflow, approval levels Manager/Director/Board, pending-value stat, full CRUD + detail panel).
  - Updated everywhere: GROUPS/GROUP_ORDER/GROUPS_LOOKUP, sidebar icons + tooltips, switch cases, search dataset defs + `_sdGroupOrder`, Quick-Add defs + tabs (Accounts & Finance, Legal), PERMISSION_MODULES (33 rows), Bengali dict.
  - Dynamic module counts (dashboard subtitle + search dropdown) — computed from GROUPS (44 modules).
  - Fixed `navigateSearch` to land on the exact module (was: group's first module only).

- **HEAD — Module reshuffle + icon fix** (SW v8-v7):
  - Moved **QC & Inspection** → Legal & Compliance (Compliance, Legal Contracts, QC & Inspection).
  - Moved **Stock & Procurement** → Admin & Operations (HR, Documents Vault, Knowledge Base, Stock & Procurement).
  - Moved **Projects** → Land & Projects (Land Acquisition, Property & Units, Plots & Layout, Projects).
  - Moved **BOQ & Cost Control** → Accounts & Finance (Finance, Payment Heatmap, Financial Approvals, BOQ & Cost Control).
  - **Payment Reminders** is now a **tab of Bookings & Customer › Dues & Recovery** (🔔 Payment Reminders tab; embedded renderer with styled host). `payment_reminders` navigation redirects to Dues › reminders tab. Removed from Accounts & Finance group nav.
  - **Icons changed:** Sales & CRM 👥→🎯 (target), Admin & Operations 👥→💼 (briefcase) — sidebar SVGs + group emoji icons updated.
  - Engineering & Construction now 5 modules (Contractors, Variation Orders, Equipment, Labor Mgmt, Design Mgmt).
  - QA tabs now match actual item groups (Engineering & Construction, Admin & Operations, Docs tabs fixed/added); QA items moved with their modules.
  - GROUPS_LOOKUP + search dataset groups updated for all moved modules. Module count now 43.
