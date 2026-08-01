# REM ERP Backend (Alternative B — full-stack realization, Phase 0–4)

Flask + SQLite backend mirroring the V10 prototype's data model and business logic.
The prototype (`docs/design-prototype-v10.html`) remains the spec; this is the real API layer it calls via the **Server Sync** panel (Settings → Server Sync).

## Stack (defaults chosen per plan)
- **Flask 3** (matches the dashboard pattern) · **SQLite** (single-file, upgrade path to PostgreSQL)
- **Token auth** (`Authorization: Bearer <token>`, issued at login) + session cookie fallback + **RBAC** via `ROLE_MODULES` (mirrors prototype)
- Passwords hashed with Werkzeug (`generate_password_hash`)
- **CORS** enabled (prototype served from a different origin via tunnel)

## Run
```bash
cd backend
python3 -m venv venv && venv/bin/pip install -r requirements.txt
venv/bin/pip install reportlab openpyxl   # Phase 4 PDF/Excel
venv/bin/python seed.py          # init schema + demo data
venv/bin/python app.py           # http://0.0.0.0:5001
```

## Login (seeded)
| Email | Password | Role |
|---|---|---|
| admin@rembd.com | admin123 | Super Admin |
| sales@rembd.com | demo123 | Sales Agent |
| finance@rembd.com | demo123 | Finance |
| engineer@rembd.com | demo123 | Site Engineer |

## API surface (JSON; Bearer token or session auth)
- Auth: `POST /api/login` (returns token), `POST /api/logout`, `GET /api/me`
- Dashboard: `GET /api/dashboard` (exec KPIs incl. NBV, dues, cash)
- CRUD: `/api/leads`, `/api/customers`, `/api/projects`, `/api/dues`, `/api/assets`
  - `GET ?status=`, `GET /<id>`, `POST`, `PUT /<id>`, `DELETE /<id>`
- Bookings (BKG-XXX ids): `GET/POST/PUT/DELETE /api/bookings[/<id>]`
- Invoices (NBR ids INV-2026-XXXX, VAT/TDS/AIT net): `GET/POST /api/invoices`, `PUT /api/invoices/<id>`
- Payments (ripple: Cleared → invoice status + dues + cash txn): `POST/PUT /api/payments[/<id>]`
- License: `GET /api/license`, `POST /api/license/status`
- Reports: `GET /api/reports/unpaid-invoices` (outstanding per invoice)

## Phase 3 — Server Sync (doc-store, full prototype shapes)
- `GET /api/bootstrap` — full server snapshot `{collections:{leads:[...], invoices:[...], ...}}`
- `POST /api/sync` — `{collections:{<name>:[rows]}}` bulk upsert into `doc_store` (PK collection+id)
- Prototype side: `Settings → Server Sync` → URL + login → Connect (pushes local seed first), then every `DB.save()` write-through (debounced 800 ms). Push/Pull buttons + status.

## Phase 4 — Server-side reports (reportlab / openpyxl)
- `GET /api/reports/invoice/<INV-ID>.pdf` — tax invoice PDF (VAT/TDS/AIT net table)
- `GET /api/reports/vat-register.pdf` — landscape VAT register with totals
- `GET /api/reports/csv/<collection>.csv` — any synced collection as CSV (BOM)
- `GET /api/reports/xlsx/<collection>.xlsx` — any synced collection as Excel (styled header)
- Wired in the prototype: invoice modal `⬇ PDF`, VAT Register card `⬇ PDF`, Server Sync report cards

## RBAC example
```bash
curl -H 'Content-Type: application/json' \
  -d '{"email":"finance@rembd.com","password":"demo123"}' http://localhost:5001/api/login   # → {"token": "..."}
curl -H 'Authorization: Bearer <token>' http://localhost:5001/api/invoices
curl -H 'Authorization: Bearer <token>' http://localhost:5001/api/leads          # → 403 for Finance
```

## Roadmap (from `docs/v10-update-plan.md` Alternative B)
- Phase 3 — Server Sync: prototype ⇄ Flask doc-store (DONE, see above)
- Phase 4 — PDF/Excel reports (DONE, see above)
- Phase 5 — gunicorn + systemd on AWS Lightsail, Cloudflare tunnel, SQLite dumps → S3
- Phase 6 — PWA manifest + customer portal + payment gateway hooks (bKash/Nagad sandbox)
