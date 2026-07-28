# REM ERP — Microservice Architecture

> **Inspired by:** Odoo's modular app architecture  
> **Goal:** Each module runs standalone or as part of a suite. Clients subscribe per-module. Permissions at button/menu/model level.

---

## 🏗 Architecture Overview

```
┌─────────────────────────────────────────────────────────────┐
│                    API Gateway (Kong / Traefik)              │
│  Route: /api/{module}/*  |  Auth  |  Rate Limit  |  Tenant  │
└──────┬──────┬──────┬──────┬──────┬──────┬──────┬──────┬────┘
       │      │      │      │      │      │      │      │
  ┌────┴┐ ┌──┴──┐ ┌─┴───┐ ┌─┴───┐ ┌─┴──┐ ┌─┴──┐ ┌─┴──┐ ┌─┴───┐
  │Auth │ │CRM  │ │Land │ │Proj.│ │Fin. │ │Stock│ │Reports│ ...
  │Svc  │ │Svc  │ │Acq. │ │Mgmt │ │Svc  │ │Svc  │ │Svc   │
  └──┬──┘ └──┬──┘ └──┬──┘ └──┬──┘ └──┬──┘ └──┬──┘ └──┬──┘
     │       │       │       │       │       │       │
     └───────┴───────┴───────┴───────┴───────┴───────┘
                         │
                ┌────────┴────────┐
                │  Message Queue  │  (RabbitMQ / Redis Streams)
                │  Event Bus      │
                └─────────────────┘
```

### Services (Microservices)

| Service | Database | Port | Dependencies | Standalone? |
|---------|----------|------|-------------|-------------|
| **Auth Service** | `auth_db` | 8001 | None | ✅ Yes |
| **CRM & Leads** | `crm_db` | 8002 | Auth, Contacts | ✅ Yes |
| **Land Acquisition** | `land_db` | 8003 | Auth, Contacts | ✅ Yes |
| **Project Management** | `project_db` | 8004 | Auth, Land, Proj. Config | ⚠️ Needs Config |
| **Flat & Plot Booking** | `booking_db` | 8005 | Auth, CRM, Projects | ⚠️ Needs CRM+Proj |
| **Finance & Accounts** | `finance_db` | 8006 | Auth, Booking | ⚠️ Needs Booking |
| **Stock & Procurement** | `stock_db` | 8007 | Auth, Projects | ⚠️ Needs Projects |
| **Contractors** | `contractor_db` | 8008 | Auth, Projects, Finance | ⚠️ Needs Proj+Fin |
| **BOQ & Cost Control** | `boq_db` | 8009 | Auth, Projects | ⚠️ Needs Projects |
| **Equipment Tracking** | `equipment_db` | 8010 | Auth, Projects | ⚠️ Needs Projects |
| **Labor Management** | `labor_db` | 8011 | Auth, Projects | ⚠️ Needs Projects |
| **QC & Inspection** | `qc_db` | 8012 | Auth, Projects, BOQ | ⚠️ Needs Proj+BOQ |
| **Sales & Marketing** | `sales_db` | 8013 | Auth, CRM | ⚠️ Needs CRM |
| **Dues & Recovery** | `dues_db` | 8014 | Auth, Booking, Finance | ⚠️ Needs Book+Fin |
| **Customer Portal** | `portal_db` | 8015 | Auth, Booking, Dues | ⚠️ Needs Book+Dues |
| **Handover & Post-Sales** | `handover_db` | 8016 | Auth, Projects, QC | ⚠️ Needs Proj+QC |
| **Regulatory Compliance** | `compliance_db` | 8017 | Auth, Projects, Land | ⚠️ Needs Proj+Land |
| **BI & Reports** | `bi_db` | 8018 | All (read-only replica) | ❌ Read-only |
| **Notifications** | `notif_db` | 8019 | Auth (pub/sub) | ✅ Yes |
| **Contact Book** | `contact_db` | 8020 | Auth | ✅ Yes |
| **Task Management** | `task_db` | 8021 | Auth | ✅ Yes |
| **Team Workspace (Chat)** | `chat_db` | 8022 | Auth | ✅ Yes |
| **Data Vault** | `vault_db` | 8023 | Auth, Projects (optional) | ✅ Yes |
| **Knowledge Base** | `kb_db` | 8024 | Auth | ✅ Yes |
| **System Settings** | `settings_db` | 8025 | Auth | ✅ Yes |
| **Gateway Config** | `gateway_db` | 8026 | Auth | ✅ Yes |

---

## 🧩 Module Bundles (Client Subscription Tiers)

Modules grouped into standalone saleable bundles:

### Bundle A: Real Estate CRM (Standalone)
*No construction, no land, no finance needed*

| Module | Why |
|--------|-----|
| Auth Service | ✓ |
| CRM & Leads | Core — track inquiries, site visits, bookings |
| Contact Book | Clients, brokers, agents |
| Task Management | Agent task tracking |
| Notifications | Email/SMS alerts |
| System Settings | Company config, users |

### Bundle B: Land & Development (Add-on to A)
| Module | Why |
|--------|-----|
| Land Acquisition | 6-stage pipeline |
| Project Management | Land/flat project tracking |
| Regulatory Compliance | RAJUK, environmental approvals |

### Bundle C: Sales & Customer (Add-on to A+B)
| Module | Why |
|--------|-----|
| Flat & Plot Booking | Full booking lifecycle |
| Sales & Marketing | Campaigns, commissions, price lists |
| Dues & Recovery | Installment tracking, reminders, late fees |
| Customer Portal | Self-service for buyers |

### Bundle D: Construction & Operations (Add-on to B)
| Module | Why |
|--------|-----|
| Contractors | Subcontractor management |
| BOQ & Cost Control | Quantity takeoff, cost variance |
| Variation Orders | Change request workflow |
| Equipment Tracking | Machinery, maintenance |
| Labor Management | Attendance, wages |
| QC & Inspection | Quality control, snag lists |
| Handover & Post-Sales | Handover, warranty |

### Bundle E: Finance & Admin (Add-on to A+B+C)
| Module | Why |
|--------|-----|
| Accounts & Finance | Ledger, payments, expenses |
| Stock & Procurement | Inventory, purchase orders |
| Data Vault | Document management |
| Knowledge Base | Internal wiki |

### Bundle F: BI & Insights (Add-on to any)
| Module | Why |
|--------|-----|
| BI & Reports | Charts, dashboards, exports |
| Team Workspace | Chat, collaboration |

---

## 🔐 Permission System (Button & Menu Level)

### Three-Layer Permission Model

```
Layer 1: Module Access     → Can the user see/use the module?
Layer 2: Menu Access       → Can the user see/click a specific menu item?
Layer 3: Button Access     → Can the user click Create/Edit/Delete/Approve/Export?
```

### Backend Implementation

```python
# Permission table (centralized in Auth Service)
permissions = {
    "user_id": "usr_123",
    "tenant_id": "tenant_456",
    "modules": {
        "crm": {
            "access": True,
            "menus": ["dashboard", "leads", "reports"],
            "buttons": {
                "lead":  ["create", "edit", "delete", "assign", "convert"],
                "pipeline": ["drag", "filter", "export"],
            }
        },
        "finance": {
            "access": False,   # Module not subscribed
            "menus": [],
            "buttons": {}
        }
    }
}
```

### Permission Check Flow

```
User clicks "Delete Lead"
        │
        ▼
Frontend sends: DELETE /api/crm/leads/{id}
        │
        ▼
API Gateway → Auth Service validates:
  1. Does user belong to tenant?
  2. Is "crm" module active for tenant?
  3. Does user's role have "lead.delete" permission?
  4. Is the user the owner / manager of this record?
        │
        ▼
If ALL pass → forward to CRM Service
If ANY fail → 403 Forbidden
```

### Role Templates (Pre-built)

| Role | Modules | Menus | Buttons |
|------|---------|-------|---------|
| **Super Admin** | All | All | All |
| **CEO / MD** | All | All | Read + Approve only |
| **Project Manager** | Projects, Contractors, BOQ, QC, Labor | Project-specific | Create, Edit, Approve |
| **Sales Agent** | CRM, Leads, Bookings | Leads, Pipeline | Create, Edit, Drag, Convert |
| **Accountant** | Finance, Dues | Ledger, Payments | Create (payment), Read |
| **Site Engineer** | Projects, QC, Labor, Equipment | Unit status, QC checklists | Create (QC), Update (status) |
| **Viewer (Client)** | Customer Portal | Dashboard, Bookings, Dues | Read only |

---

## 🚀 Tech Stack

### Backend (per service)
```
Language:     Python 3.12+
Framework:    FastAPI (async)
ORM:          SQLAlchemy 2.0 + Alembic
Auth:         JWT (access + refresh) + OAuth2
DB:           PostgreSQL 16 (schema-per-tenant optional)
Cache:        Redis 7
Queue:        RabbitMQ / Redis Streams
```

### Frontend (micro-frontend)
```
Shell:        Next.js 16 (module federation) or Single SPA
UI:           Tailwind v4 + shadcn/ui
State:        Zustand
Auth Flow:    OAuth2 PKCE
Module Load:  Dynamic import per module
```

### Infrastructure
```
Container:    Docker + Docker Compose
Orchestrator: Kubernetes (minikube for dev, EKS/GKE for prod)
Gateway:      Kong / Traefik / Envoy
Monitoring:   Prometheus + Grafana + Loki
Logging:      ELK Stack / SigNoz
CI/CD:        GitHub Actions
```

---

## 📁 Monorepo Structure

```
REM_ERP/
├── gateway/                    # API Gateway (Kong config or custom)
├── shared/                     # Shared libraries
│   ├── python/                 # Python SDK (auth client, models)
│   └── web/                    # Shared UI components, design system
├── services/
│   ├── auth/                   # Auth service (standalone)
│   ├── crm/                    # CRM & Leads
│   ├── land_acquisition/       # Land Acquisition
│   ├── projects/               # Project Management
│   ├── bookings/               # Flat & Plot Booking
│   ├── finance/                # Accounts & Finance
│   ├── stock/                  # Stock & Procurement
│   ├── contractors/            # Contractor Management
│   ├── boq/                    # BOQ & Cost Control
│   ├── equipment/              # Equipment Tracking
│   ├── labor/                  # Labor Management
│   ├── quality/                # QC & Inspection
│   ├── sales/                  # Sales & Marketing
│   ├── dues/                   # Dues & Recovery
│   ├── portal/                 # Customer Portal
│   ├── handover/               # Handover & Post-Sales
│   ├── compliance/             # Regulatory Compliance
│   ├── bi/                     # BI & Reports
│   ├── notifications/          # Notification Service
│   ├── contacts/               # Contact Book
│   ├── tasks/                  # Task Management
│   ├── workspace/              # Team Workspace / Chat
│   ├── vault/                  # Data Vault / Documents
│   ├── knowledge_base/         # Knowledge Base
│   └── settings/               # System Settings
├── frontend/
│   ├── shell/                  # Host app (auth, nav, layout)
│   ├── mfe-crm/                # CRM micro-frontend
│   ├── mfe-finance/            # Finance micro-frontend
│   └── mfe-.../                # Per-module micro-frontends
├── k8s/                        # Kubernetes manifests
├── docs/
│   ├── api/                    # API contracts (OpenAPI 3.0)
│   ├── architecture.md         # This document
│   └── design-prototype.html   # Interactive prototype
└── README.md
```

---

## 🔄 Inter-Service Communication

### Synchronous (REST)
- **API Gateway → Service:** Client requests
- **Service → Service:** Only for read-heavy lookups (e.g., CRM asks Contact Book for contact details)
- Uses internal JWT for service-to-service auth

### Asynchronous (Event Bus)
```
Auth Service publishes:   user.created, user.role_changed
CRM publishes:           lead.converted, booking.created
Finance publishes:       payment.received, invoice.generated
Projects publishes:      project.phase_changed, unit.status_updated

Subscribers:
  Dues Service ← payment.received (update installment status)
  Notifications ← *.created, *.status_changed (send alerts)
  BI Service ← *.* (update analytics)
```

---

## 🧪 Running a Standalone Module

```bash
# Start ONLY the CRM module (with shared services)
docker compose up auth-db redis gateway auth-svc crm-svc

# CRM is fully functional with:
# - Leads (Kanban + List)
# - Contact Book
# - Task Management
# - Notifications
# - Reports
```

---

## Next Steps

1. **Build the scaffolding** — Auth service, API Gateway, shared libraries
2. **Start with Bundle A** — CRM as the first standalone module (proves the architecture)
3. **Add Bundle B** — Land + Projects (proves inter-service communication)
4. **Iterate** — Each new service is a separate Docker container
