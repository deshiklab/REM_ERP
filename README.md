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

### 14. Contractor & Subcontractor Management
- **Subcontractor Database** — Trades, rates, agreements, insurance, licenses, performance rating
- **Work Orders** — Issue work orders per project/unit with scope, timeline, price, attachments
- **Work Completion Certificates** — Approve completed work stages, release milestone payments
- **Contractor Payment Tracking** — Track advances, milestone payments, retentions, final settlements
- **Agreement Management** — Store signed contracts with expiry alerts, renewal tracking
- **Mobilization Tracking** — Track contractor mobilization status (mobilized, demobilized)
- **Site Attendance** — Daily contractor worker count per project for billing verification

### 15. Bill of Quantities (BOQ) & Cost Control
- **BOQ Builder** — Itemized quantity takeoff per project (excavation, brickwork, plastering, finishing, MEP, etc.)
- **Rate Analysis** — Material + labor + equipment + overhead rates per BOQ item
- **Running Account (R.A.) Bills** — Track partial billing as work progresses, with certified quantities
- **Cost Variance Reports** — Budgeted BOQ vs actual costs in real-time with variance %
- **Work Classification** — Categorize BOQ items by trade (civil, MEP, finishing, external)
- **Unit Rate Database** — Maintain standard rates library for common construction items
- **Budget vs Actual Charts** — Visual comparison across project phases

### 16. Variation Order Management
- **Change Request** — Document scope changes with reason, originator, impact assessment
- **Variation Order Approval** — Multi-level approval workflow (Site Engineer → PM → Director)
- **Cost Impact Analysis** — Auto-calculate revised BOQ totals and budget impact
- **Schedule Impact Analysis** — Track delay impact of each variation
- **VO Log** — Complete audit trail of all changes per project with status tracking
- **Variation Register** — Master register across all projects with financial summary

### 17. Equipment & Machinery Tracking
- **Asset Register** — Excavators, cranes, concrete mixers, dump trucks, vibrators, generators
- **Allocation & Scheduling** — Assign equipment to projects/sites with time-bound schedules
- **Maintenance Schedule** — Preventive maintenance alerts (daily/weekly/monthly), service history log
- **Fuel & Operating Costs** — Track fuel consumption, maintenance costs per project allocation
- **Idle Time Reports** — Utilization analytics, idle time breakdown per equipment
- **Depreciation Tracking** — Calculate and track asset depreciation
- **Operator Assignment** — Link equipment to designated operators

### 18. Labor Management
- **Daily Attendance** — Worker check-in/out per site with biometric/photo support
- **Wage Calculation** — Daily/weekly/monthly wages based on attendance + overtime
- **Labor Categories** — Skilled, semi-skilled, unskilled with configurable rate cards
- **Contractor Labor** — Track labor supplied by contractors vs direct company hire
- **Statutory Compliance** — Provident fund, group insurance, safety gear distribution log
- **Worker Database** — Personal info, skills, certifications, bank accounts, emergency contacts
- **Overtime Management** — Overtime approval, rate calculation (1.5x / 2x)
- **Daily Labor Cost Report** — Per-project labor cost summary

### 19. Quality Control & Inspection
- **Inspection Checklists** — Configurable checklists per trade (concrete, brickwork, finishing, electrical, plumbing, MEP)
- **Snag / Defect List** — Log defects found during inspection with photos, assign for rectification
- **Non-Conformance Report (NCR)** — Formal quality issue tracking with root cause analysis
- **Inspection Schedule** — Planned vs actual inspections per project phase
- **Photo Evidence** — Attach geo-tagged timestamped photos to inspections
- **Hold Points** — Mandatory inspection hold points (e.g., before concrete pour)
- **Testing Register** — Track material tests (cube test, slump test, compaction test) with results
- **Quality Dashboard** — Pass/fail rates, NCR aging, recurring defect patterns

### 20. Sales & Marketing Suite
- **Marketing Campaign Management** — Track campaigns (billboard, social media, newspaper, referral) with budget and ROI
- **Unit Hold / Reservation** — Temporary hold with configurable auto-expiry (7/14/30 days)
- **Follow-up Automation** — Auto-trigger reminders for expiring holds, pending documents
- **Price List Management** — Versioned pricing with effective dates, block discounts, promotional offers
- **Sales Commission Engine** — Tiered commission structure per agent, auto-calculate on booking
- **Refund & Cancellation Processing** — Full workflow with penalty calculation, approval routing, disbursement
- **Source Tracking** — Lead source analysis (walk-in, referral, agent, social media, billboard)
- **Sales Dashboard** — Agent-wise performance, conversion rates, revenue pipeline

### 21. Dues & Recovery Management
- **Automated Dues Tracking** — Overdue installment detection with aging buckets (30/60/90/120+ days)
- **Automated Reminders** — Configurable SMS/Email reminders: X days before due, on due date, overdue alerts
- **Late Fee Calculator** — Configurable penalty %, grace period, waiver approval
- **Collection Follow-up Log** — Track calls, site visits, promises per defaulter with status
- **Legal Notice Workflow** — Generate and track legal notices for chronic defaulters
- **Payment Promise Tracking** — Record and track payment promises, auto-escalate on broken promises
- **Recovery Dashboard** — Aging analysis, collection efficiency, DSO (Days Sales Outstanding)
- **Amortization Schedule Viewer** — Display full payment schedule with paid/due/overdue indicators

### 22. Customer Portal & Self-Service
- **Booking Dashboard** — View unit/plot details, booking status, payment history
- **Installment Dues** — See upcoming and overdue installments with amounts and dates
- **Online Payment** — Pay installments via integrated gateway (SSLCommerz, bKash, Nagad)
- **Document Access** — Download agreement copy, payment receipts, handover documents
- **Unit Progress** — View construction progress photos and milestone updates
- **Complaint / Query Ticket** — Submit and track complaints or queries
- **Mobile-First Design** — Responsive interface optimized for smartphone access

### 23. Handover & Post-Sales
- **Pre-Handover Inspection (POS)** — Punch list before unit handover, tracked item by item
- **Snag Rectification Tracker** — Assign contractor/team to fix issues with deadline
- **Handover Certificate** — Generate formal handover document with digital signature
- **Warranty Management** — Track warranty period per unit, handle warranty claims
- **Common Area Handover** — Separate checklist for lobby, lift, generator, water pump, security
- **Post-Handover Support** — Track maintenance requests after handover
- **Utility Connection Tracker** — Gas, electricity, water, internet connection status per unit

### 24. Regulatory & Compliance (Bangladesh Focus)
- **RAJUK Approval Tracker** — Application status, fees, inspections, approvals per project
- **REHAB Membership Management** — Renewal dates, project listing updates
- **Bank Lien Tracking** — Track units under bank lien against construction loan
- **Land Mutation Status** — Track mutation application through sub-registry office
- **Tax / VAT Compliance** — TDS on contractor payments, VAT on bookings, AIT on land purchases
- **Fire Department Clearance** — Track NOC application and renewal
- **Environmental Clearance** — Track DoE (Department of Environment) clearance
- **Building Completion Certificate** — Track final certificate application and status
- **Worker Safety Compliance** — Safety equipment log, accident register, compliance reports

### 25. Advanced Reporting & Business Intelligence
- **Interactive Dashboard Builder** — Drag-and-drop charts/KPIs configurable per user role
- **Project Health Scorecard** — RAG status (Red/Amber/Green) across schedule, cost, quality, safety
- **Cash Flow Forecasting** — Projected installments inflow vs contractor/expense outflow
- **Sales Funnel Analytics** — Conversion rates at each pipeline stage with trend analysis
- **Comparative Land Analysis** — Price/sqft, location score, ROI projection across proposals
- **Drill-Down Reports** — From dashboard KPI → list view → detail view in 2 clicks
- **Scheduled Report Emails** — Auto-generate and email reports on configurable schedules
- **Custom Report Builder** — User-defined report dimensions, measures, filters, and export formats (PDF, Excel, CSV)
- **Power BI / Metabase Integration** — Direct database connection for external BI tools

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
│   │   ├── settings/
│   │   ├── contractors/
│   │   ├── boq/
│   │   ├── variations/
│   │   ├── equipment/
│   │   ├── labor/
│   │   ├── quality/
│   │   ├── sales_marketing/
│   │   ├── recovery/
│   │   ├── customer_portal/
│   │   ├── handover/
│   │   ├── compliance/
│   │   └── reports/
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

### 🚀 Release Priority Matrix

| Phase | Focus Area | Key Modules |
|-------|-----------|-------------|
| **Phase 1 — Core Foundation** | MVP | Auth & RBAC, Dashboard, CRM, Land Acquisition, Project Mgmt, Bookings |
| **Phase 2 — Construction Depth** | Operations | Contractor Mgmt, BOQ & Cost Control, Variation Orders, Labor Mgmt, Equipment Tracking |
| **Phase 3 — Finance & Recovery** | Monetization | Dues & Recovery, Sales Commission, Customer Portal, Marketing Suite |
| **Phase 4 — Quality & Handover** | Delivery | QC/Inspection, Snag Lists, Handover Certificates, Warranty Mgmt |
| **Phase 5 — Compliance & BI** | Intelligence | Regulatory Tracker, Tax Compliance, BI Dashboards, Scheduled Reports |

### 🚀 Phase 1 — Core Foundation (MVP)

| Priority | Module | Key Deliverables |
|----------|--------|-----------------|
| P0 | **Auth & RBAC** | JWT auth, role-based access (Super Admin, Admin, Sales, Finance, Site Engineer, Client view) |
| P0 | **Dashboard** | KPI cards, revenue chart, activity feed, task widget |
| P0 | **CRM** | Kanban pipeline, lead CRUD, details slide-out, filters |
| P0 | **Land Acquisition** | 6-stage workflow, proposal CRUD, owner management |
| P0 | **Project Management** | Both land/flat types, unit/plot grid, lifecycle stages |
| P0 | **Bookings** | Booking CRUD, installment schedules, payment tracking |

### 🚀 Phase 2 — Construction & Operations

| Priority | Module | Key Deliverables |
|----------|--------|-----------------|
| P1 | **Accounts & Finance** | Ledger, payments, expenses, bank accounts, JVs, budgets |
| P1 | **Stock & Procurement** | Inventory, POs, suppliers, approval workflow, stock alerts |
| P1 | **Contractor Management** | Subcontractors, work orders, completion certificates, payment tracking |
| P1 | **BOQ & Cost Control** | BOQ builder, rate analysis, R.A. bills, cost variance reports |
| P1 | **Equipment Tracking** | Asset register, allocation, maintenance, fuel tracking, idle reports |
| P1 | **Labor Management** | Attendance, wage calculation, contractor labor tracker, compliance |
| P1 | **Contacts** | Contact CRUD, CSV import, types, search |

### 🚀 Phase 3 — Sales, Recovery & Collaboration

| Priority | Module | Key Deliverables |
|----------|--------|-----------------|
| P2 | **Variation Orders** | Change requests, multi-level approval, cost/schedule impact, VO log |
| P2 | **Sales & Marketing** | Campaign tracking, unit holds, price lists, commission engine |
| P2 | **Dues & Recovery** | Aging buckets, auto-reminders, late fees, legal notice workflow |
| P2 | **Customer Portal** | Self-service booking dashboard, online payment, document access |
| P2 | **Team Workspace** | Chat, member status, task assignment |
| P2 | **Task Management** | Personal tasks, kanban board, dashboard widget |
| P2 | **Knowledge Base** | Articles, categories, search, rich content |
| P2 | **Notifications** | Real-time notifications, bell icon, dropdown, auto-email |
| P2 | **Data Vault** | Document upload, categories, per-project vault, audit trail |

### 🚀 Phase 4 — Quality, Handover & Compliance

| Priority | Module | Key Deliverables |
|----------|--------|-----------------|
| P3 | **QC & Inspection** | Checklists, snag lists, NCRs, testing register, quality dashboard |
| P3 | **Handover & Post-Sales** | Pre-handover inspection, handover cert, warranty management |
| P3 | **Regulatory Compliance** | RAJUK tracker, bank lien, mutation, tax/VAT, fire/DOE clearance |
| P3 | **Activity Log** | System-wide audit trail, per-document tracking |
| P3 | **Invoice Templates** | Customizable invoice design, auto-generation from bookings |

### 🚀 Phase 5 — Analytics, Automation & Integrations

| Priority | Feature | Description |
|----------|---------|-------------|
| P4 | **BI & Reporting** | Dashboard builder, project health scorecard, cash flow forecasting, custom reports |
| P4 | **Automated Workflows** | Rule-based triggers: auto-assign leads, send reminders, escalate approvals |
| P4 | **Bank Reconciliation** | Upload bank statements, auto-match transactions, flag discrepancies |
| P4 | **Payment Gateway** | SSLCommerz, bKash, Nagad for online payments and auto-reconciliation |
| P4 | **Client & Vendor Portal** | Self-service for clients and vendors |
| P4 | **Calendar View** | Gantt timeline for projects, milestone calendar, meeting scheduler |
| P4 | **HR & Payroll** | Employee records, attendance, leave, salary processing, tax |
| P4 | **Contract Management** | Sales agreements, supplier contracts, auto-renewal alerts |
| P4 | **Legal Case Tracker** | Track active litigation, case status, court dates, legal expenses |
| P4 | **Asset Management** | Track company assets with depreciation |
| P4 | **Custom Fields** | User-definable fields per module for flexible data capture |
| P4 | **Language Localization** | Bangla/English toggle, currency formatting, date localization |

### 🛠️ Technical Enhancements

| Area | Enhancement |
|------|-------------|
| **Performance** | Caching (Redis), pagination, lazy loading, DB indexing, CDN for documents |
| **Security** | 2FA, IP whitelisting, session management, data encryption at rest, audit trails |
| **Mobile** | Progressive Web App (PWA) or React Native companion app |
| **Messaging** | WhatsApp Business API, SMS gateway, email automation |
| **Data** | Automated daily backups, point-in-time recovery, data retention policies |
| **API** | RESTful public API for third-party integrations, rate limiting, webhooks |
| **Infrastructure** | Docker containerization, CI/CD pipelines, staging/production environments |
| **Monitoring** | Error tracking (Sentry), performance monitoring, uptime alerts, logging (ELK) |
| **Search** | Full-text Elasticsearch across all modules |

---

## Next Steps

1. **Choose stack** — Recommending Django + DRF (backend) + React + Tailwind (frontend)
2. **Design database schema** — ER diagram covering all modules
3. **Set up project structure** — Monorepo with backend/ and frontend/
4. **Start Phase 1** — Auth & RBAC → Dashboard → CRM → Land Acquisition → Projects → Bookings
5. **Ship MVP** — Iterate based on real user feedback

The REM_V93 design prototype provides a complete interactive blueprint — each screen, modal, slide-out panel, and workflow is already mapped out in the HTML.
