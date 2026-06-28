# breakeven.md  

## 1. Variable Cost per Active User (USD / month)

| Cost Component | Assumptions | Unit Cost | Monthly Qty per Active User | **Cost / User** |
|----------------|-------------|-----------|----------------------------|-----------------|
| **Compute (inference)** | 1 M tokens processed / user, GPU‑based inference @ $0.0005 per 1 k tokens (typical on‑demand GPU pricing) | $0.0005 / 1 k tokens | 1 000 k tokens | **$0.50** |
| **Storage** | Shared model + user‑metadata = 20 GB total, amortized across 10 k active users | $0.02 / GB‑mo | 0.002 GB per user | **$0.04** |
| **Bandwidth (egress)** | 10 GB egress per user (API responses) | $0.09 / GB | 10 GB | **$0.90** |
| **Support & Ops overhead (ticket triage, monitoring)** | 5 min support per user @ $30/hr (senior support) | $0.50 / hr | 0.083 hr | **$0.04** |
| **Total Variable Cost** |  |  |  | **$1.48** |

> **Rounded to $1.50** per active user per month for all subsequent calculations.

---

## 2. Pricing Tiers (USD / month)

| Tier | Price | Included Features | Monthly Variable Cost (from above) | **Contribution Margin / User** |
|------|-------|-------------------|-----------------------------------|--------------------------------|
| **Starter** | **$9** | • 100 k tokens<br>• Community forum support<br>• Basic analytics dashboard | $1.50 (pro‑rated to usage) | **$7.50** |
| **Professional** | **$29** | • 1 M tokens<br>• Email + Slack support (24 h SLA)<br>• Advanced analytics & A/B testing<br>• Access to beta models | $1.50 | **$27.50** |
| **Enterprise** | **$99** | • Unlimited tokens<br>• Dedicated account manager<br>• 99.9 % SLA, private VPC deployment<br>• Custom model fine‑tuning<br>• On‑premise licensing option | $1.50 | **$97.50** |

*All tiers share the same underlying infrastructure cost; higher tiers are assumed to stay within the $1.50 variable ceiling because they are priced for volume.*

---

## 3. Customer Acquisition Cost (CAC)

| Source | Typical Spend | CAC Range |
|--------|---------------|-----------|
| Paid developer ads (e.g., StackOverflow, Reddit) | $2 k / 10 k impressions → 0.5 % conversion | **$150 – $250** |
| Content & SEO (blog, webinars) | $1 k / month → 5 % conversion of inbound leads | **$100 – $180** |
| Partnerships / Marketplace listings | $3 k / month → 2 % conversion | **$200 – $300** |

**Adopted CAC for modeling:** **$200** (mid‑point of the realistic range).

---

## 4. Lifetime Value (LTV) Estimate  

Assumptions:  

* Monthly churn = 5 % (average for SaaS developer tools) → average customer lifespan = 1 / 0.05 = **20 months**.  
* Gross margin = (Price – Variable Cost) / Price.  

| Tier | Gross Margin | Avg. Monthly Revenue (ARPU) | LTV = ARPU × Gross Margin × Lifespan |
|------|--------------|----------------------------|--------------------------------------|
| Starter | (9‑1.5)/9 = **83.3 %** | $9 | $9 × 0.833 × 20 = **$150** |
| Professional | (29‑1.5)/29 = **94.8 %** | $29 | $29 × 0.948 × 20 = **$550** |
| Enterprise | (99‑1.5)/99 = **98.5 %** | $99 | $99 × 0.985 × 20 = **$1,950** |

---

## 5. Break‑Even User Count (Monthly Fixed Costs)

**Assumed Fixed Overhead** (salaries, office, legal, marketing, R&D) = **$20,000 / month**.

Break‑even users = Fixed Cost ÷ Contribution Margin per user.

| Tier | Contribution Margin / User | Break‑Even Users |
|------|---------------------------|-----------------|
| Starter | $7.50 | 20,000 ÷ 7.5 ≈ **2,667** users |
| Professional | $27.50 | 20,000 ÷ 27.5 ≈ **727** users |
| Enterprise | $97.50 | 20,000 ÷ 97.5 ≈ **206** users |

*If the mix is mixed, the weighted average can be used; the Professional tier alone gives the lowest absolute headcount.*

---

## 6. Path to $10 K MRR  

| Target MRR | Tier Mix (users) | Monthly Revenue |
|------------|------------------|-----------------|
| **All Starter** | 1,112 users × $9 = **$10,008** | 1,112 |
| **All Professional** | 345 users × $29 = **$10,005** | 345 |
| **All Enterprise** | 101 users × $99 = **$9,999** (≈ $10 K) | 101 |
| **Hybrid (balanced)** | 200 Pro + 150 Starter + 20 Ent | (200×29)+(150×9)+(20×99)= $5,800+$1,350+$1,980 = **$9,130** (still short) → add 10 Pro → **$10,120** |

**Fastest route** (fewest customers) → **Enterprise tier**: acquire ~101 paying enterprises.

**Revenue‑to‑CAC payback** (Professional tier example):  

* CAC $200 ÷ $27.5 margin ≈ 7.3 months* → well within the 20‑month LTV horizon.

---

### Summary of Key Numbers  

| Metric | Value |
|--------|-------|
| Variable cost per active user | **$1.50 / mo** |
| CAC (mid‑point) | **$200** |
| LTV (Professional) | **≈ $550** |
| Break‑even users (Professional) | **≈ 730** |
| Users needed for $10 K MRR (Enterprise) | **≈ 101** |
| Payback period (Professional) | **~7 months** |

These figures provide a concrete financial foundation for launching **lexi‑boost** and guide go‑to‑market prioritization (focus on Enterprise & Professional tiers to hit break‑even quickly).