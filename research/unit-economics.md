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

## Sources
- [Fitbit Air BOM and margin breakdown](https://the5krunner.com/2026/05/15/fitbit-air-cost-breakdown/)
- [Fanstel nRF52840 module pricing](https://www.fanstel.com/bm840) · [ICM-42688-P distributors](https://octopart.com/part/invensense/ICM-42688-P)
- [US gait analysis pricing](https://achillesfootandankle.com/gait-analysis-cost/) · [UK clinic pricing](https://www.thegaitclinic.uk/prices) · [Clinician pricing guidance](https://www.celutionseducation.com/blog/how-much-to-charge-for-a-running-gait-analysis-with-pricing-tool)
- [FDA cuts red tape on CDS software](https://www.arnoldporter.com/en/perspectives/advisories/2026/01/fda-cuts-red-tape-on-clinical-decision-support-software) · [Latham analysis of the 2026 loosening](https://www.lw.com/en/insights/fda-issues-updated-guidance-loosening-regulatory-approach-to-certain-digital-health-tools) · [FDA Law Blog on CDS + wellness updates](https://www.thefdalawblog.com/2026/01/a-busy-day-in-the-cdrh-neighborhood-updates-to-the-cds-and-general-wellness-guidance-documents/)
- [VALD ForceDecks in PT clinics](https://valdhealth.com/products/forcedecks) · [Practitioner review, cash-based practice](https://www.morganmeese.com/post/honest-vald-review-for-cash-based-practices)
- [Playermaker pricing and traction](https://www.forbes.com/sites/robertkidd/2021/01/27/why-playermaker-is-taking-its-soccer-technology-to-amateur-players/)
