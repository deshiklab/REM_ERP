# REM ERP Backend (Alternative B — full-stack realization, Phase 0–2)

Flask + SQLite backend mirroring the V10 prototype's data model and business logic.
The prototype (`docs/design-prototype-v10.html`) remains the spec; this is the real API layer it will call after UI rewiring (Phase 3).

## Stack (defaults chosen per plan)
- **Flask 3** (matches the dashboard pattern) · **SQLite** (single-file, upgrade path to PostgreSQL)
- **Session auth** (signed cookie) + **RBAC** via `ROLE_MODULES` (mirrors prototype)
- Passwords hashed with Werkzeug (`generate_password_hash`)

## Run
```bash
cd backend
python3 -m venv venv && venv/bin/pip install -r requirements.txt
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

## API surface (JSON; session cookie auth)
- Auth: `POST /api/login`, `POST /api/logout`, `GET /api/me`
- Dashboard: `GET /api/dashboard` (exec KPIs incl. NBV, dues, cash)
- CRUD: `/api/leads`, `/api/customers`, `/api/projects`, `/api/dues`, `/api/assets`
  - `GET ?status=`, `GET /<id>`, `POST`, `PUT /<id>`, `DELETE /<id>`
- Bookings (BKG-XXX ids): `GET/POST/PUT/DELETE /api/bookings[/<id>]`
- Invoices (NBR ids INV-2026-XXXX, VAT/TDS/AIT net): `GET/POST /api/invoices`, `PUT /api/invoices/<id>`
- Payments (ripple: Cleared → invoice status + dues + cash txn): `POST/PUT /api/payments[/<id>]`
- License: `GET /api/license`, `POST /api/license/status`
- Reports: `GET /api/reports/unpaid-invoices` (outstanding per invoice)

## RBAC example
```bash
curl -c c.txt -H 'Content-Type: application/json' \
  -d '{"email":"finance@rembd.com","password":"demo123"}' http://localhost:5001/api/login
curl -b c.txt http://localhost:5001/api/invoices
curl -b c.txt http://localhost:5001/api/leads          # → 403 for Finance
```

## Roadmap (from `docs/v10-update-plan.md` Alternative B)
- Phase 3 — UI rewiring: prototype `DB.init`/localStorage reads → `fetch()` to these APIs
- Phase 4 — PDF/Excel reports (reportlab/openpyxl), statement exports
- Phase 5 — gunicorn + systemd on AWS Lightsail, Cloudflare tunnel, SQLite dumps → S3
- Phase 6 — PWA manifest + customer portal + payment gateway hooks (bKash/Nagad sandbox)
