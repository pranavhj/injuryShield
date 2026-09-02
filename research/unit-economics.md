# Unit Economics — Four Revenue Models Against The Actual Intervention

**Built 2026-08-23. Resolves VIABILITY K7, and most of K11.**

The question: given that the evidence-based intervention is a **2–3 week programme with
feedback deliberately faded** (K11), which revenue model survives?

**Headline answer: perpetual subscription is the worst fit and loses money on every
customer unless they stay 9+ months. Selling the product outright is not a retreat — it is
the model that fits both the science and the one proven comparable in this segment.**

All figures are estimates with stated assumptions. Where a conclusion depends on an
assumption, the sensitivity is shown. **CAC is the single largest unknown throughout.**

---

## 1. Cost Base — Two-Pod System

Benchmark: a published Fitbit Air teardown estimate puts factory-gate cost at **$20–22 per
unit** for a device with PPG, SpO2, skin temp, accelerometer, gyro, battery, enclosure,
band, assembly, packaging and a charging puck — at 8–12 million units/year.

Our pod is simpler (no PPG, no SpO2, no display, no band) but adds large flash and a haptic
motor, and — critically — we are at **~1,000 units, not 10 million.** Low volume is the
dominant cost driver.

### Per pod, ~1,000 unit volume

| Line | Est. |
|---|---|
| MCU module (nRF52840 class; Fanstel BM840 ≈ $4.76 @ 1k) | $5.00 |
| 6-axis IMU (ICM-42688-P class — volume price, not the $34 single-unit list) | $6.00 |
| QSPI flash 128 MB | $2.00 |
| LiPo cell (~100 mAh) | $1.50 |
| PMIC / charge management | $1.00 |
| LRA haptic + driver | $1.50 |
| PCB (4-layer, small) | $1.50 |
| Passives, magnetic pogo connector, misc | $2.00 |
| Enclosure (injection moulded, tooling amortised over 5k) | $3.00 |
| **Components subtotal** | **$23.50** |
| Assembly, test, ~20% yield loss | $4.50 |
| **Factory gate, per pod** | **≈ $28** |

### Per two-pod system

| Line | Est. |
|---|---|
| 2 × pod | $56 |
| Charging dock | $6 |
| Straps / clips | $4 |
| Packaging | $4 |
| **System factory gate** | **$70** |
| Freight, tariffs, warranty reserve, returns (+25%) | $18 |
| **Landed COGS** | **≈ $88** |

**Working figure: $90 landed at 1,000 units. Roughly $55–65 at 10,000 units.**

Fitbit's own fully-loaded figure ($37–43 including amortised R&D and go-to-market against a
$99 retail) is a useful sanity check on how thin consumer hardware margins get even at
enormous scale.

### CAC assumption
Consumer wearable CAC typically runs $50–150. **Base case $80.** Every model below is shown
against CAC sensitivity because this number moves conclusions more than BOM does.

---

## 2. Model A — Perpetual Subscription (WHOOP style)

Hardware free, $19/month.

| Line | Value |
|---|---|
| Upfront COGS | $90 |
| CAC | $80 |
| **Total upfront per subscriber** | **$170** |
| Monthly revenue | $19 |
| **Months to break even** | **9.0** |

### The problem, stated precisely

**Every customer must stay 9 months just to return the cash spent acquiring them.** The
intervention is designed to be complete in 2–3 weeks, with feedback faded on purpose.

| Average customer life | Revenue | Contribution |
|---|---|---|
| 1 month | $19 | **−$151** |
| 3 months (the programme) | $57 | **−$113** |
| 6 months | $114 | **−$56** |
| 9 months | $171 | $1 — breakeven |
| 12 months | $228 | +$58 |
| 18 months (WHOOP-like) | $342 | +$172 |

### Sensitivity — the conclusion is robust
| COGS | CAC | Break-even months |
|---|---|---|
| $90 | $80 | 9.0 |
| $60 (at 10k units) | $80 | 7.4 |
| $60 | $50 | 5.8 |
| $40 (optimistic) | $50 | 4.7 |

Even under aggressive assumptions you need ~5 months. The intervention takes three weeks.

### Does perpetual subscription work *at all*?
**Only if the reason to keep paying is something other than retraining.** There are real
candidates:
- **Repeat injury.** Recreational runner incidence is 37–56% per year. People come back.
- **Seasonal re-check** around a marathon build or a training block change.
- **Ongoing monitoring** — the fatigue/degradation detection use case. You graduate from
  retraining; you do not graduate from "tell me when my mechanics are drifting."
- The cadence review notes *"long-term adherence remains a challenge"* without continued
  feedback — an argument that some ongoing contact is genuinely useful.

But that is a **bet against the mechanism that makes the product work**, and it must clear
9 months of average life before it earns a cent. **Not the launch model.** Possibly a
secondary tier later, priced far lower.

---

## 3. Model B — Outright Sale

Sell the 2-pod kit with a structured programme and 12 months of app access. This is exactly
**Playermaker's proven structure**: $249 including a one-year subscription, into 50+ D1
colleges and 100+ US clubs.

**Caveat added 2026-08-24:** Playermaker has raised $45M+ in VC funding — proven at *their*
resource level, not a bootstrapped precedent. And more broadly: no company found in a
dedicated precedent search (`research/programme-model-precedents-bigco.md`,
`-smallco.md`) has proven "outright sale + genuinely finite programme + zero ongoing
revenue" direct-to-consumer, at any scale. Every large player survives on a subscription
layered over hardware; every small/bootstrapped running-hardware peer either never bundled a
finite programme (Stryd, ARION) or had to abandon the consumer channel entirely to survive
(RunScribe, Sensoria). The finite-programme *mechanism* has real support (Noom RCT,
Reflexion Health VERA's 75-80% vs 15-40% adherence) — but only in programmes sold to a payer
with a bounded budget (hospital, employer), never direct-to-consumer. This does not
invalidate Model B's math below, but it should be read as an unproven combination, not a
proven one.

| Line | $249 | $299 | $349 |
|---|---|---|---|
| Revenue | $249 | $299 | $349 |
| COGS | −$90 | −$90 | −$90 |
| CAC | −$80 | −$80 | −$80 |
| **Contribution, immediate** | **$79** | **$129** | **$179** |
| Gross margin | 64% | 70% | 74% |

**Cash positive from unit one. No payback period. No working-capital hole.**

Add optional renewal after year one at $60/year (85% margin ≈ $51). At 25% renewal that is
~$13 per customer per subsequent year — modest, but free.

### What this fixes
- **K7 (working capital) disappears entirely.** The HaaS "fish" problem was the reason
  subscription looked risky; outright sale has no fish.
- **K11 stops mattering.** A customer who graduates in three weeks has already paid in full.
  Graduation becomes a *feature* — "this worked, you're done" — instead of churn.
- **K5 (retention) is de-fanged.** Retention was existential under subscription. Under
  outright sale it only affects word-of-mouth and renewals.

### What it costs
- No recurring revenue, so growth requires constant new customer acquisition
- The 97% consumer-hardware failure base rate lands most directly on this model
- **Do not price at $299 without a differentiated claim.** NURVV died at exactly $299
  selling metrics a $200 watch already gave. Our $299 has to buy the RCT-backed programme
  and per-limb tibial data — things a watch cannot do (`capability-envelope.md`).

---

## 4. Model C — Programme / Rental

A 6-week structured retraining programme. Pods ship out, customer returns them. Price $199.
Reference point: a single clinic gait analysis costs **$75–150 (2D) or $350–450+ (3D)** in
the US, £72–98 in the UK — for one session. We deliver eight sessions in the real world.

Assume each pod pair completes **8 cycles over ~2 years**.

| Line | Per customer |
|---|---|
| Revenue | $199 |
| Hardware, amortised ($90 ÷ 8) | −$11 |
| Round-trip shipping | −$20 |
| Refurb, cleaning, battery check | −$10 |
| Loss/damage reserve (5% of $90) | −$5 |
| Support | −$10 |
| **Variable cost** | **−$56** |
| CAC | −$80 |
| **Contribution** | **$63** |

**Hardware turn: one $90 pod pair generates $1,592 of revenue across 8 cycles — a 17×
return on hardware capital.**

### Honest downsides
- **Reverse logistics is operationally hard**, and it is a fixed overhead a solo founder
  must run every week. Expect 10–20% of returns to be late, damaged or absent.
- CAC at $80 against $199 revenue is heavy — 40% of the price.
- Seasonal: demand clusters in spring and pre-marathon.
- Sensitivity: at 4 cycles per pair instead of 8, hardware cost doubles to $22 — contribution
  falls only to $52. **The model is resilient to cycle count**, which is its strength.

---

## 5. Model D — Clinic / Physio Channel

Clinic buys hardware, pays for software, cycles patients through the programme.

| Line | Value |
|---|---|
| Hardware: 2 pod pairs + dock | $899 |
| Our COGS (2 pairs) | −$180 |
| **Hardware contribution** | **$719** |
| Software subscription | $99/month |
| Software gross margin ~85% | $84/month |
| CAC (demo, sales cycle, onboarding) | −$900 |
| **Payback on CAC** | hardware margin covers 80%; rest in ~2.2 months |
| **LTV at 36-month clinic life** | $719 + (36 × $84) = **$3,743** |
| **LTV − CAC** | **$2,843 per clinic** |

The clinic charges patients $150–250 for the programme, comfortably inside the existing
$75–500 gait-analysis price band, and runs 20–50 patients a year through one pod pair.

### The regulatory question — checked, and the assumption is inverted

**Your instinct was that selling to clinicians adds regulation and cost. The evidence says
the opposite: the clinic channel is regulatorily *easier* than direct-to-consumer.**

- FDA's **January 2026 CDS guidance loosened** the rules. Commissioner Makary framed it as
  the FDA choosing to *"get out of the way as a regulator."* Coverage headline: *"FDA Cuts
  Red Tape on Clinical Decision Support Software."*
- CDS is **not** regulated as a device when it *supports* rather than *drives* a clinician's
  decision, uses validated data, and lets the clinician independently review the basis.
- The 2026 update went further: **a single recommendation now qualifies** for the non-device
  exemption (2022 required presenting a list of options).
- **Crucially, the exemption is specifically for software intended for health care
  professionals.** FDA expressly notes existing device policies "continue to apply to
  software functions… intended for use by patients or caregivers." **Patient-facing software
  gets *less* latitude than clinician-facing software.**
- Real-world confirmation: **VALD sells ForceDecks widely into US physical therapy clinics**,
  including cash-based practices, marketed for assessing "strength, movement, asymmetry and
  balance" and "monitoring rehabilitation progress and injury risk." Practitioner reviews
  discuss cost and ROI at length and **mention no regulatory or billing obstacles at all.**

**So the regulatory burden you were worried about is not where you thought it was.** The
burden attaches to *claims*, not to *customers*. Selling a measurement-and-coaching tool to
a physio who exercises their own judgement is a well-trodden, low-friction path — arguably
safer than telling a consumer directly what their body is doing.

### The real objection to clinics is commercial, not regulatory
This part of your instinct is right:
- **Long sales cycles.** Weeks to months per clinic, with demos.
- **CAC is ~10× consumer** and requires a person who can sell, not just build.
- **Support burden** is higher — clinics expect responsiveness.
- **You need clinical credibility** before the first sale: published evidence, references,
  ideally a name clinic using it.
- It is a **different company** — B2B sales motion, not a product-led consumer motion.

**Verdict: keep it, but as a later channel, not the launch. Your ranking is right; your
reason is wrong.** Deprioritise clinics because the sales motion is expensive and slow for a
solo founder, not because of regulation.

---

## 6. Side by Side

| | A · Subscription | B · Outright sale | C · Programme/rental | D · Clinic |
|---|---|---|---|---|
| Price | $19/mo | $299 | $199 | $899 + $99/mo |
| COGS per customer | $90 | $90 | $56 (amortised) | $180 |
| CAC | $80 | $80 | $80 | $900 |
| **Contribution** | **$1 at 9 mo** | **$129 immediate** | **$63 immediate** | **$2,843 over 36 mo** |
| Cash cycle | **−$170 then wait 9 mo** | **positive day one** | positive day one | positive month 3 |
| Fit with a 3-week intervention | **terrible** | **excellent** | **excellent** | excellent |
| Working capital risk (K7) | **high** | low (inventory only) | **lowest — 17× turn** | low |
| Retention risk (K5) | **existential** | cosmetic | cosmetic | moderate |
| Operational burden | low | low | **high (reverse logistics)** | **high (B2B sales)** |
| Regulatory exposure | consumer claims | consumer claims | consumer claims | **lowest** |
| Founder-feasible solo | yes | **yes** | partly | no |

---

## 7. Recommendation

**Launch with Model B — outright sale at $299 for a two-pod kit including a structured
6-week programme and 12 months of app access.**

Rationale:
1. **It fits the science.** The intervention finishes; so does the transaction. Graduation
   becomes the success story rather than a churn event.
2. **It is the proven structure in this exact segment.** Playermaker: $249, hardware plus
   one year of app, into 50+ D1 colleges and 100+ clubs.
3. **It kills two open risks outright.** K7 (working capital) and most of K11. K5 drops from
   existential to cosmetic.
4. **It is the only model a solo founder can run** without either reverse logistics
   operations or a B2B sales function.
5. **$129 contribution per unit from unit one** means the business funds itself rather than
   requiring debt to cover COGS.

**So yes — returning to selling the product is the right call, and it is not a retreat.**
The earlier move to subscription was made to escape the $35/pod trap, and it was correct
*given the assumption of perpetual use*. That assumption is now known to be false. At
$299 with a real programme attached, hardware sale is simply the better model.

**Keep as live options, in order:**
- **C (programme/rental)** if returns logistics prove manageable — best capital efficiency
  by a wide margin (17× hardware turn), and it may suit an India-based operation better
- **A as a cheap secondary tier only** — $8–10/month post-programme monitoring for the
  subset who want ongoing tracking. Never the primary model.
- **D (clinic)** as a later channel once evidence and references exist. Lowest regulatory
  exposure of all four; highest sales cost.

---

## 8. What Would Change This

- **CAC above ~$150** — Model B contribution falls to $59 and outright sale gets thin.
  *CAC is the number to measure first, and it is measurable cheaply with a landing page and
  a small ad spend before anything is built.*
- **COGS above ~$130** at 1k units — revisit the two-pod spec or raise price to $349
- **Return rate above 20%** in Model C — reverse logistics stops working
- **Evidence that gait changes decay in 3–6 months** — that would *rescue* subscription by
  creating a genuine re-training cycle. Watch for retention studies (`market/WATCHLIST.md`)

---

## 9. Clinic Channel Unit Economics (Model D — Deep Dive)

**Added 2026-09-01. Resolves O11 partially. Complements the sketch in §5 above.**

Decision D17 made the clinic/physio channel the primary go-to-market. This section models the
economics in detail: what a clinic earns, what we earn, and how the numbers move under
stress.

### 9.1 Pod Utilisation and Per-Patient Hardware Cost

**Assumptions:**
- Programme: 8 sessions over 2–3 weeks per patient
- Turnaround between patients: 2–3 days (charging, cleaning, scheduling)
- Each patient cycle = ~3 weeks active + ~0.5 weeks downtime = **~3.5 weeks per patient**
- Clinic may not run pods at 100% utilisation (vacations, no-shows, seasonal demand)
- **Effective utilisation: 70%** (conservative — accounts for scheduling gaps)

| Line | Value |
|---|---|
| Weeks per year | 52 |
| Weeks per patient cycle | 3.5 |
| Max patients per pod set per year (100% util.) | 14.9 |
| **Patients per pod set per year (70% util.)** | **~10** |
| At 85% utilisation (mature clinic) | ~13 |

**Pod lifespan estimate:**

LiPo batteries rated at 300–500 cycles to 80% capacity. At ~100 mAh our pod charges roughly
every 2–3 sessions. Over an 8-session programme, each pod charges ~3–4 times. At 10 patients
per year, that is 30–40 charge cycles per year. The battery is therefore NOT the limiting
factor — at 500 cycles, the battery lasts **12–17 years** of clinic use.

The actual limiting factors are:
- **Connector wear** (magnetic pogo — rated ~5,000–10,000 cycles; ~15+ years at clinic use)
- **Enclosure / strap degradation** (clinic cleaning chemicals, physical handling)
- **Obsolescence** (firmware, BLE standard, app compatibility)

**Working estimate: 3-year pod lifespan in clinic use** — conservative, driven by
obsolescence and wear rather than component failure. This gives ~30 patients per pod set
over its life.

| Line | Value |
|---|---|
| Pod set COGS (landed, 1k units) | $90 |
| Patients over 3-year lifespan | ~30 |
| **Effective per-patient hardware cost** | **$3.00** |
| If lifespan is only 2 years (~20 patients) | $4.50 |
| If lifespan is 4 years (~40 patients) | $2.25 |

**Hardware cost per patient is negligible.** The value is entirely in software, cloud,
and the RTM billing infrastructure.

---

### 9.2 Clinic Subscription Pricing Model

**What the clinic earns (RTM reimbursement per enrolled patient):**

2026 Medicare Part B national rates (Physitrack / Tenovi):

| Code | Description | Rate |
|---|---|---|
| 98975 | RTM setup + patient education (billed once) | $21.71 |
| 98977 | MSK device supply, 16+ days/month | $39.75 |
| 98985 | MSK device supply, 2–15 days/month (NEW 2026) | $39.75 |
| 98980 | Treatment management, first 20 min/month | $53.77 |
| 98981 | Each additional 20-min block | $41.08 |
| 98979 | Treatment management, 10–19 min (NEW 2026) | $26.05 |

**Per-patient monthly revenue to the clinic:**

| Scenario | Monthly RTM Revenue |
|---|---|
| Base: 98977 + 98980 (16+ days, 20 min review) | **$93.52** |
| First month (add 98975 setup) | $115.23 |
| Light-touch: 98985 + 98979 (2–15 days, 10–19 min) | $65.80 |
| High-touch: 98977 + 98980 + 98981 (40+ min) | $134.60 |

**Our 8-session programme maps to ~1 month of RTM billing.** A patient using pods 8 days
in a month qualifies for 98985 (2–15 days) at minimum. If the clinic stages sessions
across 16+ days, they qualify for the higher 98977 rate.

**What we charge the clinic:**

Three subscription tiers, benchmarked against VALD ($3,600–5,100/yr) and dorsaVi ($59–550/mo):

| Tier | Monthly | Annual | Includes |
|---|---|---|---|
| **Starter** | $99/mo | $1,188/yr | 1 pod set, software, cloud, basic support |
| **Growth** | $149/mo | $1,788/yr | 2 pod sets, RTM documentation templates, priority support |
| **Pro** | $199/mo | $2,388/yr | 3 pod sets, white-label reports, dedicated onboarding, EMR export (PDF/CSV) |

**Why this is below VALD ($3,600–5,100/yr):** We are unproven, have no clinical validation
studies, and no brand recognition. Entering below the established price ceiling is
necessary. We can raise prices as clinical evidence and references accumulate.

**Clinic margin per patient (base case: Growth tier, 10 patients/year):**

| Line | Per patient/month | Notes |
|---|---|---|
| RTM revenue (98977 + 98980) | +$93.52 | Medicare base; private payers often higher |
| Clinician time cost (~25 min @ $45/hr) | −$18.75 | Review data, document, call patient |
| Our subscription (amortised: $149 ÷ ~3 concurrent patients) | −$49.67 | See note below |
| **Clinic net margin per patient/month** | **+$25.10** | Before overhead |

**Note on amortisation:** Our 8-session programme runs ~3 weeks. At 70% utilisation, a
clinic runs ~3 patients concurrently with 2 pod sets (staggered starts). The subscription
cost is shared across these concurrent patients.

**At higher utilisation (10 patients/year, each for 1 month of RTM billing):**

| Line | Annual |
|---|---|
| RTM revenue: 10 patients x $93.52 x 1 month each | $935 |
| First-month setup bonus: 10 x $21.71 | $217 |
| Our subscription cost | −$1,788 |
| Clinician time: 10 x $18.75 | −$188 |
| **Clinic annual net from RTM** | **−$824** |

**The problem:** At only 10 patients per year, each generating just 1 month of RTM billing,
the clinic loses money. The RTM revenue does not cover the subscription.

**The fix — extend RTM beyond the 8-session programme:**

The programme is 8 sessions over 2–3 weeks, but RTM billing does not require the patient
to be in the programme. Post-programme check-ins (patient runs with pods once per week,
clinic reviews data monthly) can sustain RTM billing for 2–3 additional months. This is
clinically defensible — monitoring whether gait changes persist.

**Revised model: 3 months of RTM per patient (1 month active + 2 months monitoring):**

| Line | Annual |
|---|---|
| RTM revenue: 10 patients x $93.52 x 3 months | $2,806 |
| Setup: 10 x $21.71 | $217 |
| Our subscription | −$1,788 |
| Clinician time: 10 patients x 3 months x $18.75 | −$563 |
| **Clinic annual net** | **+$672** |

**At 15 patients/year (85% pod utilisation):**

| Line | Annual |
|---|---|
| RTM revenue: 15 x $93.52 x 3 | $4,208 |
| Setup: 15 x $21.71 | $326 |
| Our subscription | −$1,788 |
| Clinician time: 15 x 3 x $18.75 | −$844 |
| **Clinic annual net** | **+$1,902** |

**At 20 patients/year (Pro tier, 3 pod sets):**

| Line | Annual |
|---|---|
| RTM revenue: 20 x $93.52 x 3 | $5,611 |
| Setup: 20 x $21.71 | $434 |
| Our subscription (Pro) | −$2,388 |
| Clinician time: 20 x 3 x $18.75 | −$1,125 |
| **Clinic annual net** | **+$2,532** |

**Break-even for the clinic:**
- Growth tier ($149/mo): **~8 patients/year at 3 months RTM each**
- Pro tier ($199/mo): **~10 patients/year at 3 months RTM each**
- If only 1 month RTM per patient: **~20 patients/year** — requires near-100% utilisation

**Conclusion: the RTM pitch only works if we help clinics bill 2–3 months per patient,
not just the 1-month programme.** This is the most important operational design decision
for the clinic channel.

---

### 9.3 Our Economics (What We Capture Per Clinic)

**Revenue per clinic per year:**

| Tier | Monthly | Annual Revenue |
|---|---|---|
| Starter | $99 | $1,188 |
| Growth | $149 | $1,788 |
| Pro | $199 | $2,388 |

**COGS per clinic per year:**

| Line | Starter | Growth | Pro |
|---|---|---|---|
| Hardware (amortised over 3 years) | $30 | $60 | $90 |
| Replacement reserve (10%/yr of hardware) | $9 | $18 | $27 |
| Cloud / HIPAA infra (per clinic share) | $25 | $25 | $25 |
| Support (email + onboarding, amortised) | $100 | $100 | $150 |
| **Total COGS per clinic/year** | **$164** | **$203** | **$292** |

**HIPAA infrastructure cost assumption:** At minimum viable HIPAA ($5,000–10,000/yr for a
startup), spread across 50+ clinics = $100–200 per clinic. At 200 clinics = $25–50. Using
$25/clinic assumes 200+ clinics — at fewer clinics this cost is higher.

**Contribution margin per clinic per year:**

| Tier | Revenue | COGS | Contribution | Margin % |
|---|---|---|---|---|
| Starter | $1,188 | $164 | **$1,024** | 86% |
| Growth | $1,788 | $203 | **$1,585** | 89% |
| Pro | $2,388 | $292 | **$2,096** | 88% |

**CAC per clinic:**

B2B SaaS CAC for healthcare ranges widely. For small independent clinics (our initial
target), we estimate:

| Channel | Est. CAC | Notes |
|---|---|---|
| Referral / word-of-mouth | $200–400 | Cheapest, but slow to start |
| Content marketing + inbound | $500–800 | Blog, webinars, conference presence |
| Inside sales (outbound) | $800–1,500 | Founder-led; 1–3 month cycle |
| Field sales + demo | $1,500–2,500 | Higher touch; needed for larger practices |
| **Blended base case** | **$900** | Matches §5 estimate |

Benchmark: median B2B SaaS CAC is $702 self-serve, $11,400 sales-led. At $900 blended
we are assuming founder-led sales to independent clinics — no sales team.

**Payback period:**

| Tier | CAC | Monthly contribution | Payback |
|---|---|---|---|
| Starter | $900 | $85 | **10.6 months** |
| Growth | $900 | $132 | **6.8 months** |
| Pro | $900 | $175 | **5.1 months** |

**LTV at 36-month average clinic life:**

| Tier | 36-mo contribution | LTV:CAC |
|---|---|---|
| Starter | $3,072 | 3.4:1 |
| Growth | $4,755 | **5.3:1** |
| Pro | $6,288 | **7.0:1** |

All tiers exceed the 3:1 LTV:CAC threshold for B2B SaaS profitability. Growth tier is the
sweet spot — high enough margin, low enough price to reduce sales friction.

**Clinics needed for revenue milestones (Growth tier):**

| Target ARR | Clinics needed | Notes |
|---|---|---|
| $100K | 56 | Founder-feasible with 12–18 months sales effort |
| $500K | 280 | Requires 1–2 dedicated salespeople |
| $1M | 559 | ~1.4% of US independent PT clinics (~39,000) |
| $3M | 1,677 | ~4.3% penetration — ambitious but within reach |
| $10M | 5,593 | ~14% penetration — requires enterprise deals or multi-location chains |

**At Pro tier the numbers improve:**

| Target ARR | Clinics (Pro) |
|---|---|
| $1M | 419 |
| $3M | 1,257 |
| $10M | 4,189 |

---

### 9.4 CAC Comparison: Clinic vs Consumer

| Metric | Consumer (D2C) | Clinic (B2B) |
|---|---|---|
| **CAC** | $80–150 | $800–1,500 |
| **Revenue per sale** | $249 (one-time) | $1,788/yr (recurring) |
| **LTV (3 yr)** | $249 + ~$13/yr renewal = ~$275 | $5,364 |
| **LTV:CAC** | 1.8–3.4:1 | 3.6–6.7:1 |
| **Payback** | Immediate (day one) | 6–11 months |
| **Revenue type** | One-time (with tiny renewal tail) | Recurring |
| **Sales motion** | Performance marketing, SEO, content | Founder-led outbound, demos, referrals |
| **Scalability** | Self-serve (if CAC holds) | Sales-constrained |
| **Churn impact** | None (already paid) | Direct revenue loss |

**Key insight: clinic CAC is 10x higher but LTV is 20x higher.** The unit economics
are structurally better, but the sales motion is slower and harder for a solo founder.

**Consumer CAC is the more dangerous unknown.** Consumer wearable CAC of $80 is an
assumption — actual could be $150+ (which kills Model B). Clinic CAC is more predictable
because the sales process is direct and measurable from the first demo.

---

### 9.5 Sensitivity Analysis

#### What if RTM reimbursement rates drop 20%?

RTM rates are set by CMS annually. A 20% cut would reduce 98977+98980 from $93.52 to
$74.82/month.

| Scenario | Clinic annual net (Growth, 10 patients, 3 mo RTM) |
|---|---|
| Current rates ($93.52/mo) | +$672 |
| **−20% rates ($74.82/mo)** | **−$889** |
| To break even at −20%: need | **15 patients/year** |

**Impact: a 20% rate cut makes the pitch unviable at 10 patients/year.** The clinic needs
15+ patients. This is achievable at 85% utilisation with 2 pod sets, but it removes the
margin of safety. Our response: emphasise non-RTM revenue streams (cash-pay assessments,
97032 biofeedback billing, patient retention value).

**On our side:** our subscription revenue is unaffected. The risk is indirect — clinics
that can't make RTM work will churn.

#### What if only 5 patients per clinic enrol?

| Line | 5 patients, 3 mo RTM | 5 patients, 1 mo RTM |
|---|---|---|
| RTM revenue | $1,403 | $468 |
| Setup fees | $109 | $109 |
| Our subscription (Growth) | −$1,788 | −$1,788 |
| Clinician time | −$281 | −$94 |
| **Clinic net** | **−$557** | **−$1,305** |

**At 5 patients the clinic loses money on every scenario.** This is the minimum viable
patient load problem — if a clinic cannot fill the pods, the subscription is a cost centre.

**Implication for us:** clinic churn will be high among low-volume practices. Target clinics
with existing running/sports patient flow. Pre-qualify: "How many running-related patients
do you see per month?" If the answer is <2, do not sell.

**On our side at 5 patients/clinic (assuming they still pay for 12 months before churning):**

| Line | Value |
|---|---|
| Revenue (12 months x $149) | $1,788 |
| COGS | −$203 |
| CAC | −$900 |
| **Contribution** | **+$685** |

We are still contribution-positive even if the clinic churns at 12 months. But chronic
churn at 12 months means we are in a CAC treadmill — constantly replacing clinics. The
business works only if average clinic life is 24+ months.

#### What if pod replacement is needed every 6 months?

This would mean 2 replacements per year per pod set instead of once every 3 years.

| Line | 3-year lifespan (base) | 6-month lifespan |
|---|---|---|
| Hardware cost per year (Growth, 2 sets) | $60 | $360 |
| Replacement reserve | $18 | $0 (already replacing) |
| Total COGS per clinic/year | $203 | $485 |
| Contribution margin | $1,585 (89%) | $1,303 (73%) |

**Even at 6-month replacement, contribution margin stays above 70%.** This is because
the hardware is cheap relative to the subscription revenue. Pod durability matters for
customer experience and brand perception, but it does not break the economics.

#### Combined worst case: −20% RTM + 5 patients + 6-month pods

| Line | Value |
|---|---|
| Clinic cannot justify subscription | Churn at 6–12 months |
| Our revenue (6 months x $149) | $894 |
| COGS (6 months, including pod replacement) | −$243 |
| CAC | −$900 |
| **Our contribution** | **−$249** |

**The combined worst case is a $249 loss per clinic — manageable individually but fatal
at scale.** This scenario requires all three things to go wrong simultaneously. If any
one of them is at base case, we remain contribution-positive.

#### What if private payers reimburse higher than Medicare?

Medicare rates are typically the floor. Private payer RTM rates are often 10–30% higher.

| Payer | Est. 98977+98980/mo | Clinic net (Growth, 10 pts, 3 mo) |
|---|---|---|
| Medicare (base) | $93.52 | +$672 |
| Private (+20%) | $112.22 | +$2,233 |
| Private (+30%) | $121.58 | +$3,014 |

**Private payer mix dramatically improves clinic economics.** Clinics with 50%+ private
payers will see meaningfully better margins — and be stickier customers.

---

### 9.6 Clinic Channel — Summary Table

| Metric | Base Case | Optimistic | Pessimistic |
|---|---|---|---|
| Patients per pod set/year | 10 | 13 | 5 |
| RTM months per patient | 3 | 3 | 1 |
| RTM rate (98977+98980) | $93.52/mo | $112/mo (+20% private) | $74.82/mo (−20%) |
| **Clinic annual net** | **+$672** | **+$3,014** | **−$1,305** |
| Our subscription (Growth) | $1,788/yr | $2,388/yr (Pro) | $1,188/yr (Starter) |
| Our COGS per clinic | $203 | $292 | $164 |
| **Our contribution per clinic** | **$1,585** | **$2,096** | **$1,024** |
| CAC | $900 | $400 (referral) | $1,500 (field sales) |
| **LTV:CAC (36 mo)** | **5.3:1** | **15.7:1** | **2.0:1** |
| Clinics for $1M ARR | 559 | 419 | 842 |
| Clinics for $3M ARR | 1,677 | 1,257 | 2,525 |

---

### 9.7 Critical Dependencies and Open Questions

1. **RTM billing duration per patient is the single biggest lever.** 1 month vs 3 months
   per patient is the difference between the clinic losing money and making money. We must
   design the post-programme monitoring protocol to sustain 2–3 months of RTM billing. This
   is clinically defensible (monitoring persistence of gait changes) but must be explicit
   in our product design and clinic training.

2. **Minimum viable patient load is ~8/year (Growth tier, 3 months RTM).** Below this,
   the clinic loses money and will churn. Pre-qualification of clinics by running/sports
   patient volume is essential.

3. **510(k) may be required for RTM billing.** Decision D18 addresses this — phased
   approach, wellness first, file when demand proves out. But some payers may require
   FDA clearance before covering RTM with our device. This is an open risk.

4. **HIPAA infrastructure is a fixed cost that hurts at low clinic counts.** At 10 clinics,
   HIPAA costs $500–1,000 per clinic per year. At 200 clinics, $25–50. The early clinics
   subsidise the infrastructure build-out.

5. **Churn rate is unknown.** The model assumes 36-month average clinic life. If average
   life is 18 months, LTV:CAC drops to 2.6:1 (Growth) — still viable but tight. If 12
   months, LTV:CAC is 1.8:1 — below the 3:1 threshold.

---

## Sources
- [Fitbit Air BOM and margin breakdown](https://the5krunner.com/2026/05/15/fitbit-air-cost-breakdown/)
- [Fanstel nRF52840 module pricing](https://www.fanstel.com/bm840) · [ICM-42688-P distributors](https://octopart.com/part/invensense/ICM-42688-P)
- [US gait analysis pricing](https://achillesfootandankle.com/gait-analysis-cost/) · [UK clinic pricing](https://www.thegaitclinic.uk/prices) · [Clinician pricing guidance](https://www.celutionseducation.com/blog/how-much-to-charge-for-a-running-gait-analysis-with-pricing-tool)
- [FDA cuts red tape on CDS software](https://www.arnoldporter.com/en/perspectives/advisories/2026/01/fda-cuts-red-tape-on-clinical-decision-support-software) · [Latham analysis of the 2026 loosening](https://www.lw.com/en/insights/fda-issues-updated-guidance-loosening-regulatory-approach-to-certain-digital-health-tools) · [FDA Law Blog on CDS + wellness updates](https://www.thefdalawblog.com/2026/01/a-busy-day-in-the-cdrh-neighborhood-updates-to-the-cds-and-general-wellness-guidance-documents/)
- [VALD ForceDecks in PT clinics](https://valdhealth.com/products/forcedecks) · [Practitioner review, cash-based practice](https://www.morganmeese.com/post/honest-vald-review-for-cash-based-practices)
- [Playermaker pricing and traction](https://www.forbes.com/sites/robertkidd/2021/01/27/why-playermaker-is-taking-its-soccer-technology-to-amateur-players/)
- [Physitrack RTM revenue ROI for PT practices](https://www.physitrack.com/insights/rtm-revenue-roi-pt-practice) — 2026 Medicare Part B RTM rates, per-patient revenue, case study
- [Tenovi RTM CPT codes 2026](https://www.tenovi.com/rtm-cpt-codes-2026/) — code descriptions, billing rules
- [247 Medical Billing RTM codes 2026](https://www.247medicalbillingservices.com/blog/new-rtm-codes-for-physical-therapy-2026-cpt-98985-98979-reimbursement-rates-247-mbs) — new 98985/98979 codes
- [MovementRx RTM CPT codes](https://mymovementrx.com/rtm-cpt-codes/) — rates and billing guide
- [B2B SaaS CAC benchmarks 2026](https://www.data-mania.com/blog/cac-benchmarks-for-b2b-tech-startups-2025/) · [SaaS CAC by segment](https://unbuiltlab.com/learn/benchmarks/saas-cac-benchmarks)
- [LTV:CAC ratio benchmarks](https://www.saashero.net/strategy/b2b-saas-ltv-cac-benchmarks/) — 3:1 minimum, median 3.2:1
- [Healthcare SaaS CAC trends](https://firstpagesage.com/reports/average-cac-for-startups-benchmarks/)
- [LiPo battery cycle life](https://www.grepow.com/blog/charging-cycles-of-lithium-ion-polymer-batteries.html) · [LiPo 500 cycle expectancy](https://www.lipobattery.us/lipo-batterys-life-expectancy-after-500-cycles/) — 300–500 cycles, 80% capacity at 500
- [HIPAA compliance cost for startups 2026](https://www.accountablehq.com/post/hipaa-compliance-cost-for-startups-what-to-budget-in-2026) — $5K–25K year one, $2K–10K ongoing
- [PT clinic software pricing 2026](https://www.sprypt.com/blog/multi-location-pt-clinic-software-pricing) — $200–500/mo solo, $1K–5K/mo multi-provider
- [RTM adoption: 81% of clinicians use remote monitoring (2023)](https://www.sprypt.com/blog/how-remote-monitoring-is-transforming-physical-therapy) — 305% increase since 2021
