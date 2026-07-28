# Land Acquisition Flow — End to End

This document maps the complete lifecycle of land, from **raw land identification** through to a **ready plot in the Layout & Planning grid** — covering the acquisition process, the status changes in the plot grid, and the data flow across REM ERP modules.

---

## 1. Overview: The Big Picture

```
  Raw Land                    Land Proposal              Acquired          Master Plan         Ready to Sell
  Identified    ───►  Under Due Diligence   ───►  Owned by Company  ───►  Laid Out & Plotted   ───►  Available in Grid
                       (Not Acquired)                        │                    │
                            │                                 │                    │
                     Grey hatched in                         │              Green in grid
                     master plan only                        │              ("Available")
                     (future vision)                          │
                                                              ▼
                                                    Payment to seller,
                                                    mutation/registration
```

---

## 2. Complete Step-by-Step Flow

### Phase 1: Prospect & Evaluate (Land Acquisition Module)

```
Step 1 ─── Step 2 ─── Step 3 ─── Step 4 ─── Step 5 ─── Step 6
IDENTIFY    SURVEY      LEGAL       ACQUIRE     APPROVE     ARCHIVE
```

#### ① Identification & Sourcing
- Land broker/agent brings a proposal
- User creates a **Land Proposal** in the **Land Acquisition** module
- Fields: Location, mouza, dag/khatian numbers, total area, asking price, owner(s), broker details
- Proposal status: `Sourcing`
- At this stage, the land is **NOT yet added to any project's layout grid**

#### ② Feasibility & Survey
- Site visit conducted: soil test, digital survey, boundary verification
- Documents uploaded: Survey report, soil test report, geo-coordinates
- Feasibility score calculated automatically (location × price × legal status)
- Proposal status: `Survey in Progress` → `Survey Completed`
- Decision gate: **Pass** → move to Legal, **Fail** → Archive

#### ③ Legal & Due Diligence
- Title verification (CS/RS/SA khatian check)
- Tax receipt verification
- Deed review (Saf-Kabala, Baya-deed chain)
- Valuation report from registered valuer
- Checklist items marked complete/incomplete
- Proposal status: `Legal Vetting`
- If title is clear → proceed to Acquisition

#### ④ Acquisition & Mutation
- Sale deed executed and registered
- Mutation application submitted at sub-registry office
- Payment to seller tracked (advance → full payment schedule)
- Mutation status: `Applied` → `Pending` → `Completed`
- **THIS IS THE CRITICAL GATE** — Once mutation is complete, the land becomes **company property**
- Purchase cost recorded in **Accounts & Finance** module

#### ⑤ Planning & Approvals
- RAJUK/City corporation approval application
- Layout plan submission
- Zoning certificate
- Environmental clearance
- Proposal status: `Approvals Pending` → `Approved`

#### ⑥ Archive
- Proposal marked as either `Completed (Acquired)` or `Rejected`
- All documents preserved for audit

---

### Phase 2: Register into Project (Project Management Module)

Once acquisition + approvals are complete:

```
1. Create Project
   ├── Type: Land Plotting or Apartment/Construction
   ├── Link to Land Proposal(s) — one project may consolidate
   │   multiple land parcels
   └── Set total land area, budget, timeline

2. Plot Layout Designer
   ├── Draw the layout grid (rows × cols)
   ├── Define road network (6m, 8m, 10m)
   ├── Mark amenity areas (park, lake, mosque, school)
   └── Assign plot IDs (e.g., M-01 to M-48)

3. Plot Status Assignment
   ├── Plots that are ready to sell → Available (🟢)
   ├── Plots already promised → Reserved (🟡)
   ├── Plots in master plan but NOT yet acquired → Not Acquired (⬜ hatched)
   └── Common areas → Amenity (⚪)
```

---

### Phase 3: Visualise in Layout & Planning

When you open the **Layout & Planning** module:

- **Project tabs** — each layout project shows its total plots
- **Plot grid** — colour-coded cells instantly show the status of every plot
- **Stats bar** — counts for each status (including Not Acquired)
- **Click any plot** — see its full details: ID, type, area, price, road access, customer

---

## 3. How "Not Acquired" Fits In

The diagram below shows what happens when a **Layout Project** includes land that hasn't been fully acquired yet:

```
┌──────────────────────────────────────────────────────┐
│                 MASTER PLAN VIEW                      │
│                                                        │
│   ┌────┬────┬────┬────┐  ┌────┬────┬────┬────┐        │
│   │🟢  │🟢  │🟢  │⬜  │  │🟢  │🔴  │🟢  │🟢  │        │
│   │M-01│M-02│M-03│M-04│  │M-05│M-06│M-07│M-08│        │
│   └────┴────┴────┴────┘  └────┴────┴────┴────┘        │
│   ┌────┬────┬────┬────┐  ┌────┬────┬────┬────┐        │
│   │⬜  │🟡  │🟢  │🔴  │  │🟢  │🟢  │⬜  │🟢  │        │
│   │M-09│M-10│M-11│M-12│  │M-13│M-14│M-15│M-16│        │
│   └────┴────┴────┴────┘  └────┴────┴────┴────┘        │
│                                                        │
│   ═══ 8m Road ════          ═══ 6m Road ════         │
│                                                        │
│   Legend: 🟢 Available  🔴 Sold  🟡 Reserved          │
│           ⬜ Not Acquired  ⚪ Amenity (park)           │
└──────────────────────────────────────────────────────┘

Status transitions for each plot:

    ⬜ Not Acquired    ───►    🟢 Available    ───►    🔴 Sold
     (in master plan,        (company owns,         (transferred to
      not yet purchased)      ready to sell)          customer)
                                                        │
                                                   🟡 Reserved
                                                 (under booking /
                                                  earnest money)
```

**Not Acquired → Available transition:**
1. Land acquisition team continues negotiation on the grey hatched parcel
2. Once the purchase deed is registered:
   - **Land Proposal** moves to stage ④ (Acquisition Complete)
   - **Finance** records the purchase payment
   - **User manually updates** the plot status in Layout & Planning from `not_acquired` → `available`
   - The plot turns green, receives a price, and becomes available for sale

---

## 4. Data Flow Across Modules

```
┌──────────────┐    ┌──────────────┐    ┌──────────────┐
│  LAND        │    │  PROJECT     │    │  LAYOUT &    │
│  ACQUISITION │───►│  MANAGEMENT  │───►│  PLANNING    │
│              │    │              │    │              │
│ Proposal     │    │ Create       │    │ Draw grid    │
│ Survey       │    │ Link parcel  │    │ Assign       │
│ Legal check  │    │ Set budget   │    │  statuses    │
│ Deed/reg     │    │ Timeline     │    │ Visualise    │
│ Mutation     │    │              │    │              │
└──────┬───────┘    └──────────────┘    └──────┬───────┘
       │                                       │
       ▼                                       ▼
┌──────────────┐                    ┌──────────────┐
│  ACCOUNTS &  │                    │  CRM &       │
│  FINANCE     │                    │  BOOKING     │
│              │                    │              │
│ Payment to   │                    │ Customer     │
│  seller      │                    │  buys plot   │
│ Land cost    │                    │ Booking →    │
│  amortised   │                    │  Sold        │
└──────────────┘                    └──────────────┘
```

---

## 5. Real-World Scenario: Muktodhara Green Park

| Stage | Detail |
|---|---|
| **Land identified** | 12 Katha in Purbachal, asking ৳40 Cr, 3 owners |
| **Survey done** | Soil OK, boundary verified, coordinates: 23.8544, 90.4512 |
| **Legal cleared** | CS Khatiyan verified, no dispute |
| **Only 8 of 12 Katha acquired so far** | 2 owners sold (8 Katha) — payment: ৳28 Cr |
| **Plot grid created** | 48 plots in master plan, **but only 8 Katha = 34 plots owned** |
| **14 plots are Not Acquired ⬜** | Grey hatched — the remaining 4 Katha belong to the 3rd owner who hasn't sold yet |
| **Land team working on it** | Negotiation ongoing for the remaining 4 Katha |
| **When acquired** | The 14 grey plots turn 🟢 green, priced, and go on sale |

---

## 6. Summary: The 3 Critical Gates

```
Gate 1: ┌─ Due Diligence Pass ─┐
         │   Legal title OK     │  → Proceed to Acquisition
         │   Survey passed      │
         └──────────────────────┘

Gate 2: ┌─ Acquisition Complete ─┐
         │   Deed registered     │  → Land is company property
         │   Mutation done       │  → Now can be plotted
         └──────────────────────┘

Gate 3: ┌─ Master Plan Approved ┐
         │   RAJUK approval      │  → Grid goes live
         │   Layout drawn        │  → Plots get prices
         └──────────────────────┘     → Ready to sell (Available)
```
