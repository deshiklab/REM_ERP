# REM ERP — Real Estate Management ERP

A comprehensive Enterprise Resource Planning system for **Mars Constech Limited**, designed to manage the full lifecycle of real estate development — from land acquisition and project planning to sales, finance, procurement, and operations.

> **Based on:** REM_V93 design prototype  
> **Stack:** Python (Django/Flask), PostgreSQL, React/Vue frontend (TBD)

---

## Modules & Features

### 1. Executive Dashboard
- **KPI Cards:** Total projects, active leads, pending approvals, monthly revenue
- **Charts:** Revenue trend (bar/line), expense breakdown (pie/doughnut), lead conversion funnel
- **Quick Actions:** Add lead, create task, view notifications
- **Recent Activity Feed:** Live timeline of system-wide actions (new leads, payments, PO approvals)
- **Task Widget:** Personal to-do list with add/complete functionality

### 2. CRM & Leads
- **Kanban View:** Drag-and-drop pipeline (New Inquiry → Contacted → Site Visit → Negotiation → Booked → Downpayment → Installments)
- **List View:** Sortable/filterable table with status, priority, type (Local/NRB)
- **Lead Details Slide-out Panel:** Profile, communication log, property interest, documents, payment history
- **Add Lead Modal:** Full form with name, contact, property interest, source, priority, assigned agent
- **Filter Slide-out:** Filter by status, priority, type
- **Lead Stages & Auto-advancement**
- **Search & Assign** functionality
- **Dashboard KPIs:** Total leads, conversion rate, hot leads

### 3. Land Acquisition
- **Pipeline Stages (Digital Workflow):**
  1. **Identification & Sourcing** — Track land proposals, location, area, owners, asking price
  2. **Feasibility & Survey** — Soil tests, digital survey, ROI analysis, 4-step progress bar
  3. **Legal & Due Diligence** — Title verification, tax receipts, deed review, valuation reports
  4. **Acquisition & Mutation** — Sale deed, registration, mutation status, payment tracking
  5. **Planning & Approvals** — RAJUK/authority approvals, layout plan, zoning certificates
  6. **Archive** — Completed or rejected proposals
- **Proposal Details Slide-out:** Overview, documents, owners & shares, financials, approvals, timeline
- **Manage Owners Modal:** Add/remove co-owners with shares
- **Feasibility Scorecard:** Automated scoring based on location, price, legal status
- **Legal Vetting Checklist:** Title search, tax payment, deed verification, valuation

### 4. Project Management
- **Project Types:** Land/Plotting, Apartment/Construction
- **Project Dashboard:** Budget vs actual, timeline phases, unit/plot inventory
- **Project Configuration:** Type, location, total area, units/plots, phases, budget
- **Project Lifecycle Stages:** Track each project through a full lifecycle pipeline with status badges and stage-specific actions:
  1. 🔵 **Concept & Feasibility** — Market analysis, site assessment, financial modeling
  2. 🟡 **Pre-Development & Design** — Architectural planning, layout approval, budgeting
  3. 🟣 **Financing** — Loan processing, investor funding, payment structuring
  4. 🟠 **Procurement** — Contractor bidding, material sourcing, supplier agreements
  5. 🔴 **Construction Execution** — Active building, site supervision, quality control
  6. 🟢 **Project Closeout** — Handover, final inspections, documentation
- **Stage Transition Workflow:** Move projects between stages with automatic date logging and audit trail
- **Timeline Phases:** Add milestones with dates, status, progress %
- **Unit/Plot Management:**
  - **Flat units:** Floor-wise grid view with unit details (size, price, status)
  - **Construction Stages:** Per-unit progress tracking (Brickwork → Plastering → Finishing → Completed)
  - **Plots:** Grid layout with color-coded status (Available/Sold/Reserved)
  - **Pricing Modal:** Set base price, final price, discounts
  - **Log Work:** Track man-hours and work logs per unit
- **Document Upload** per project
- **Team Management:** Assign project manager, site engineers, sales agents
- **Issue Reporting:** Report and track construction issues per unit

### 5. Flat & Plot Booking
- **Booking List:** Table with customer, project, unit/plot, price, payment schedule
- **Booking Details:** Installment schedule, payment plan, due amounts
- **New Booking Flow:** Select project → select unit → customer info → payment plan → confirmation
- **Payment Schedule Generation:** Auto-generate installment plan
- **Booking Status Tracking:** Downpayment, Installments, Completed, Cancelled

### 6. Accounts & Finance
- **Dashboard:** Gross income, operating expenses, net profit, bank balances
- **All Transactions:** Filterable ledger of all income/expense entries
- **Receive Payment:** Record incoming payments against bookings
- **Record Expense:** Log project/operational expenses with category
- **Bank Accounts:** Multiple account management (BRAC Bank, Dutch Bangla, Cash)
- **Project Budgets:** Budget allocation and tracking per project
- **Tax & Adjustments:** VAT, tax withholding entries
- **Expense Breakdown:** Categorical expense analysis (Materials, Labor, Legal, Admin, Marketing)
- **Charts:** Income vs expense trend, expense breakdown (doughnut)

### 7. Stock & Procurement
- **Inventory Management:**
  - Categorized inventory (Construction Material, Finishes, Plumbing, Electrical, Safety)
  - Stock level with low-stock alerts
  - Quantity tracking with unit of measure
- **Purchase Order (PO) Management:**
  - Create PO with item selection, supplier, delivery date
  - PO approval workflow
  - PO status tracking (Pending, Approved, Delivered, Partially Delivered)
  - PO Details slide-out with line items, costs, delivery status
- **Supplier Management:** Name, contact, address, performance rating
- **Inventory Valuation:** Total inventory value calculation

### 8. Contact Book
- **Contact List:** Searchable table with name, organization, phone, email, type
- **Contact Types:** Buyers, Suppliers, Contractors, Consultants, Brokers, Government
- **Add Contact Modal:** Name, organization, designation, phone, email, address, type, notes
- **View/Edit Contact Details**

### 9. Task Management
- **Personal Tasks:** Add, complete, delete with priority labels
- **Filter:** All, Active, Completed
- **Task count badge**
- **Integration:** Tasks widget on dashboard, tasks panel in workspace

### 10. Team Workspace (Chat)
- **Team Members Sidebar:** List of team members with online status
- **Chat Area:** Group conversation with messages (sender avatar, name, time)
- **Message Input:** Send messages with Enter key
- **Task Integration:** Quick task assignment from chat
- **Sentiment indicators** on messages

### 11. Data Vault (Document Management)
- **Upload Document:** Upload files with project association and category
- **Document List:** Table with filename, project, category, upload date, size
- **Categories:** Legal, Financial, Technical, Marketing, HR, Miscellaneous
- **Download & Preview** capability

### 12. Knowledge Base
- **Article Management:** Add, edit, search knowledge articles
- **Categories:** Land Acquisition, Sales, Legal, Finance, Procurement, HR, IT
- **Rich Content:** Formatted articles with sections, code blocks, key details
- **Search:** Full-text search across articles

### 13. System Settings
- **User Management:** Add/edit users, role assignment, active/inactive status
- **Roles & Permissions Matrix:** Role-based access control (Admin, Finance Manager, Sales Agent, Site Engineer, etc.)
- **Project Configuration:** Company info, logo, contact details, system defaults
- **Activity Log:** Audit trail of user actions with timestamps
- **Security:** Password change, dark mode toggle, fullscreen mode

### Cross-Cutting Features
- **Global Search:** Unified search across properties, leads, documents
- **Notifications System:** Bell icon with badge count, notification dropdown
- **Dark Mode:** Full UI dark mode via CSS filter inversion
- **Zoom Controls:** Zoom in/out/reset for accessibility
- **Responsive Layout:** Mobile sidebar with overlay, adaptive grid
- **Data Export:** Exportable lists and reports
- **Audit Logging:** Track all create/update/delete operations

---

## Tech Stack Options

| Layer | Option 1 | Option 2 |
|-------|----------|----------|
| Backend | Django + DRF | FastAPI |
| Frontend | React + Tailwind | Vue 3 + Tailwind |
| Database | PostgreSQL | MySQL |
| Auth | JWT + Role-Based | Django Session Auth |
| Storage | AWS S3 / DigitalOcean Spaces | Local + Backup |
| Deployment | Docker + Nginx | VPS + Supervisor |

---

## Project Structure (Recommended)

```
REM_ERP/
├── backend/
│   ├── apps/
│   │   ├── dashboard/
│   │   ├── crm/
│   │   ├── land_acquisition/
│   │   ├── projects/
│   │   ├── bookings/
│   │   ├── finance/
│   │   ├── procurement/
│   │   ├── contacts/
│   │   ├── tasks/
│   │   ├── workspace/
│   │   ├── vault/
│   │   ├── knowledge_base/
│   │   └── settings/
│   ├── config/
│   ├── middleware/
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── store/
│   │   └── api/
│   └── package.json
└── docs/
```

---

## Future Enhancements & Roadmap

### ✅ Features Present in Design (Not Yet Documented)

These features already exist in the REM_V93 prototype but aren't in the core feature list above — ready to be built:

| Feature | Module | Description |
|---------|--------|-------------|
| **Drag-and-Drop Layout Builder** | Projects | Interactive plot/layout designer with minimap — drag units onto blocks |
| **Journal Vouchers (JVs)** | Finance | Double-entry accounting journal entries with auto-balancing (Debit = Credit) |
| **SMS Gateway Integration** | Settings | Bulk SMS provider config, payment receipt SMS, lead assignment alerts |
| **Email Notification Templates** | Settings | Customizable automated system emails with template editor |
| **Invoice Template Designer** | Finance | Custom invoice layout (logo, fields, styling) with save/load |
| **Kanban Task Board** | Tasks | Internal task kanban with drag-and-drop between To Do → In Progress → Done |
| **Contacts CSV Import** | Contacts | Bulk import contacts from CSV with field mapping |
| **Per-Document Audit Trail** | Vault | Track who viewed/downloaded each document with timestamps |
| **Bulk Actions** | Multiple | Bulk delete/suspend users, bulk delete leads |
| **Feasibility Scorecard** | Land | Auto-score proposals based on location, price, legal status |
| **Custom Checklists** | Land | Configurable checklists for feasibility, legal vetting, acquisition stages |
| **Legal Opinion Log** | Land | Unalterable trail of lawyer remarks and legal opinions |
| **Layout PDF Export** | Projects | Download plot/layout designs as PDF |
| **Activity Logging per Lead** | CRM | Track all communications, calls, meetings per lead |
| **Multi-Project Type Toggle** | Dashboard | Toggle between Land/Flat project views |

### 🚀 Phase 1 — Core Modules (MVP)

| Priority | Module | Key Deliverables |
|----------|--------|-----------------|
| P0 | **Auth & RBAC** | JWT auth, role-based access (Super Admin, Admin, Sales, Finance, Site Engineer, Client view) |
| P0 | **Dashboard** | KPI cards, revenue chart, activity feed, task widget |
| P0 | **CRM** | Kanban pipeline, lead CRUD, details slide-out, filters |
| P0 | **Land Acquisition** | 6-stage workflow, proposal CRUD, owner management |
| P0 | **Project Management** | Both land/flat types, unit/plot grid, lifecycle stages |
| P0 | **Bookings** | Booking CRUD, installment schedules, payment tracking |

### 🚀 Phase 2 — Operations & Finance

| Priority | Module | Key Deliverables |
|----------|--------|-----------------|
| P1 | **Accounts & Finance** | Ledger, payments, expenses, bank accounts, JVs, budgets |
| P1 | **Stock & Procurement** | Inventory, POs, suppliers, approval workflow, stock alerts |
| P1 | **Contacts** | Contact CRUD, CSV import, types, search |
| P1 | **Data Vault** | Document upload, categories, per-project vault, audit trail |
| P1 | **Invoice Templates** | Customizable invoice design, auto-generation from bookings |

### 🚀 Phase 3 — Collaboration & Intelligence

| Priority | Module | Key Deliverables |
|----------|--------|-----------------|
| P2 | **Team Workspace** | Chat, member status, task assignment |
| P2 | **Task Management** | Personal tasks, kanban board, dashboard widget |
| P2 | **Knowledge Base** | Articles, categories, search, rich content |
| P2 | **Notifications** | Real-time notifications, bell icon, dropdown, auto-email |
| P2 | **Activity Log** | System-wide audit trail, per-document tracking |

### 🚀 Phase 4 — Advanced Features & Integrations

| Priority | Feature | Description |
|----------|---------|-------------|
| P3 | **Contract Management** | Sales agreements, supplier contracts, contractor agreements, auto-renewal alerts |
| P3 | **HR & Payroll** | Employee records, attendance, leave management, salary processing, tax calculation |
| P3 | **Payment Gateway Integration** | SSLCommerz, bKash, Nagad for online payments and auto-reconciliation |
| P3 | **WhatsApp Business API** | Automated lead follow-ups, booking confirmations, payment reminders |
| P3 | **Client Portal** | Self-service: view booking status, payment history, download documents |
| P3 | **Vendor Portal** | Vendor login to view POs, submit invoices, track payments |
| P3 | **Webhook System** | Trigger external actions (Slack, Zapier) on system events |

### 🚀 Phase 5 — Analytics & Automation

| Priority | Feature | Description |
|----------|---------|-------------|
| P4 | **Automated Workflows** | Rule-based triggers: auto-assign leads, send reminders, escalate approvals |
| P4 | **Bank Reconciliation** | Upload bank statements, auto-match transactions, flag discrepancies |
| P4 | **Profitability Reports** | Per-project P&L, margin analysis, budget vs actual variance |
| P4 | **Calendar View** | Gantt timeline for projects, milestone calendar, meeting scheduler |
| P4 | **Asset Management** | Track company vehicles, equipment, office assets with depreciation |
| P4 | **Meeting Management** | Schedule meetings, agenda, minutes, action item tracking |
| P4 | **Legal Case Tracker** | Track active litigation, case status, court dates, legal expenses |
| P4 | **Custom Fields** | User-definable fields per module for flexible data capture |
| P4 | **Language Localization** | Bangla/English toggle, currency formatting, date localization |

### 🛠️ Technical Enhancements

| Area | Enhancement |
|------|-------------|
| **Performance** | Caching (Redis), pagination, lazy loading, DB indexing |
| **Security** | 2FA, IP whitelisting, session management, data encryption at rest |
| **Mobile** | Progressive Web App (PWA) or React Native companion app |
| **Data** | Automated daily backups, point-in-time recovery, data retention policies |
| **API** | RESTful public API for third-party integrations, rate limiting |
| **Infrastructure** | Docker containerization, CI/CD pipelines, staging/production environments |
| **Monitoring** | Error tracking (Sentry), performance monitoring, uptime alerts |

---

## Next Steps

1. **Choose stack** — Recommending Django + DRF (backend) + React + Tailwind (frontend)
2. **Design database schema** — ERD for all 13+ modules
3. **Set up project structure** — Multi-app Django project
4. **Implement Phase 0** — Auth, base templates, RBAC
5. **Iterate** — Build modules per priority

The REM_V93 design prototype provides a complete interactive blueprint — each screen, modal, slide-out panel, and workflow is already mapped out in the HTML.
