# Who Pays, What We Can Claim, and How the Company Is Structured

**Researched 2026-08-23.** Answers three questions the business model did not address:
who actually holds the budget, what we are legally allowed to say, and whether the founder
constraint is real.

---

## 1. Who Actually Pays — The Budget Numbers

### US high schools: the market cannot afford us
| Metric | Value |
|---|---|
| Annual athletic training supplies budget, typical HS program | **$3,000–$8,000 total** |
| Money available per athlete, range across schools | **$96 – $926** |
| HS athletes with access to an athletic trainer | ~80% |
| HS *schools* that actually employ one | **56%, down 10 points since 2017** |

That $3–8K is the *entire* consumables and equipment-replacement budget for the whole
program. A 25-athlete team at 5 pods each is 125 pods. Even at a fantasy $20/pod that is
$2,500 — a third to most of the annual budget, for one line item, in a market where the
number of schools employing a trainer at all is *falling*.

**Verdict: the US high school team market as a hardware purchase is not viable.** Not at
$35/pod, not at $105/kit. The budget does not exist. Two things could change this:
a subscription small enough to sit inside a season line item (~$500–1,500/team/year), or
booster/parent-funded purchase, which is a consumer sale wearing a team uniform.

### NCAA: budget exists but is not held by anyone who wants our product
| Metric | Value |
|---|---|
| NCAA catastrophic insurance deductible | **$90,000** (school must cover up to this) |
| Estimated cost per D1 athlete for medical coverage + benefits | **$12,250/yr** (→$9,430 if 100k athletes pooled) |
| D1 schools providing *no* health insurance to athletes | **30%** |

The money at NCAA scale is real — $12,250/athlete/year dwarfs any device cost. But it is
insurance and medical spend, controlled by risk management and the athletic department's
finance side, not by the athletic trainer who would use the product.

**To reach that budget you must make a claim you cannot support.** Nobody reallocates
insurance spend to a device that says "your athlete's cadence drifted 4%." They reallocate
it for a demonstrated reduction in claims. That requires the evidence in
`predictive-validity.md` §9 that does not exist yet. **This is a year-3+ market at best.**

### The insurance angle DOES work — just not in sports yet
This is the most useful finding in this file. The exact business model — sensors, real-time
biomechanical feedback, injury-cost reduction, insurer participation — **is already proven
and funded, in workplace safety.**

| Metric | Value | Source |
|---|---|---|
| Average ROI of wearable safety systems | **250%** | StrongArm |
| Work-related injury reduction | up to **52%** | StrongArm |
| Best documented single deployment, year 1 | **64% injury reduction, 58% claims-cost reduction** | Nationwide |
| Claims cost reduction in high strain/sprain environments | up to **50%** | Nationwide |

Kinetic's REFLEX device: sensors detect high-risk postures and give the worker **real-time
feedback whenever a high-risk motion occurs.** That is mechanically the same product as the
ARION intervention that worked — continuous coaching, not prediction. Insurers (Nationwide,
Milliman analyses) actively engage; premium credits exist.

**Why it works there and not in sports:**
1. The payer (employer/insurer) directly eats the injury cost. In sports, the payer is
   diffuse and the injury cost lands on the athlete or a separate insurance pool.
2. The intervention is *posture correction in the moment* — a mechanism with an obvious
   causal path, not a statistical risk forecast.
3. There is a hard dollar denominator: workers' comp claims. Sports has no equivalent
   line item at HS or amateur level.

**Strategic implication: "industrial athlete" is a real adjacent market with a proven payer
and proven ROI, using the same 5–7 pod IMU hardware and the same real-time-coaching
software.** It should be tracked as a genuine pivot option, not a footnote. It is also the
only identified market where injury-cost reduction is a *purchasable* outcome today.

### Where the money actually is for v1
| Buyer | Budget holder | Verdict |
|---|---|---|
| Individual runner | Themselves | **Viable now.** 37–56% annual injury rate; motivated, self-funding, already buys $100–500 of running tech |
| HS team | Athletic director, $3–8K total | Not viable as hardware. Maybe as cheap subscription |
| College team | AD / sports medicine | Viable only with evidence we do not have |
| College risk management | Finance/insurance | Year 3+, needs claims data |
| Pro club | Performance staff | Viable but tiny TAM, long sales cycle, Zone7/Catapult incumbent |
| **Employer / workers' comp insurer** | **Risk & safety budget** | **Proven ROI, active buyers, adjacent pivot** |

**The individual runner is the right v1 buyer** — the one identified in `CLAUDE.md` — and
now for a better reason than founder dogfooding: they are the only sports buyer who holds
their own budget and does not require an injury-prediction claim to justify the purchase.

Base rate supporting this: **recreational runner injury incidence 7.7 per 1000 hours
(95% CI 6.9–8.7), annual incidence 37–56%.** Roughly half of runners get hurt each year.
That is a large, self-aware, self-funding pain population.

---

## 2. What We Are Allowed To Say — Liability and FDA

The user's concern ("what if we say a player is safe and they still get injured — that
would kill us") is the correct instinct and it has a clean structural answer.

### FDA general wellness (Jan 2026 guidance, finalized)
FDA **broadened** the low-risk general wellness category to explicitly include
non-invasive, non-implanted wearables using optical sensing and **AI/ML enhancements**.
Products that "promote overall health or healthy activities" are not regulated devices.

**We fall outside general wellness the moment we:**
- claim to diagnose, treat, mitigate, or **prevent disease**
- interpret physiological data **for clinical decision-making**
- reference a specific disease/condition for an individual user

**The bright line for us:** describing observed mechanics = wellness. Telling a coach an
athlete is at risk of a specific injury, or is cleared to play = clinical decision support,
and likely a regulated device.

### The asymmetric liability problem
| We say | Reality | Consequence |
|---|---|---|
| "At risk" | No injury | Annoyance, alert fatigue, churn |
| **"Safe / green"** | **Injury occurs** | **We told them it was fine. This is the company-ending case.** |

The two errors are not symmetric, and the dangerous one is the *reassuring* output. This
means **green must never be an affirmative safety statement.**

### Claim language — use these, never those

| ✅ Say | ❌ Never say |
|---|---|
| "Your ground contact time is 8% above your 30-day baseline" | "You are at risk of injury" |
| "Left/right asymmetry has increased this session" | "Your ACL is at risk" |
| "Mechanics have degraded — typical of fatigue" | "You are safe to continue" |
| "Below your normal range" (yellow) | "Cleared to play" |
| "Significantly outside your normal range" (red) | "No injury risk detected" |
| "Movement quality monitoring" | "Injury prevention system" |
| "Training and performance tool" | "Medical device" / "prevents injury" |

### Green/yellow/red — the user's idea, made defensible
The traffic-light concept survives, with one change: **the scale measures deviation from
the athlete's own baseline, not risk.**

- **Green** — "mechanics consistent with your baseline." *Descriptive. Not a safety claim.*
- **Yellow** — "mechanics drifting from baseline"
- **Red** — "mechanics significantly changed from baseline"

Every state is an observable, verifiable statement about measured movement. None is a
prediction. **If a red athlete keeps going and gets hurt, we were right about what we
measured. If a green athlete gets hurt, we never claimed they were safe** — we said their
mechanics looked normal, which was true.

The user's trust-building model — "people will trust us when someone in red pushes through
and gets injured" — works under this framing, and it works *without* requiring us to be a
predictor. Track it as an outcome we observe and publish, never as a claim we make up front.

**Required product elements:**
- Terms of service disclaiming medical/diagnostic use, prominently, at onboarding
- No "cleared to play" state anywhere in the UI, ever
- Product liability insurance before any team sale
- COPPA compliance before any youth-athlete data is touched
- If we ever want the clinical claim: that is a 510(k)-class project, budget it as such

---

## 3. Hardware-as-Subscription (the WHOOP model)

The user's proposal to make money on subscription rather than hardware is correct, and the
comparable is unambiguous.

### WHOOP proof points (2025)
| Metric | Value |
|---|---|
| ARR | **$1B+** (end of 2025) |
| Members | 2.5M+ |
| Growth | 103% YoY (subscriptions and bookings) |
| Retention | **>80%** in core demographic; 50%+ still daily at 18 months |
| LTV:CAC | **~4.5x** |
| Valuation | $10.1B on $575M raise (~10x ARR) |
| International | 60% of sales outside US |

WHOOP gives away hardware and charges for data. It works, at scale, in exactly our
category of buyer.

### Why this specifically rescues the 5–7 pod decision
A $105 3-pod kit was a constraint imposed by hardware-sale economics. Under subscription,
BOM stops being a retail-price ceiling and becomes a payback-period input. A 5-pod system
at, say, $30 BOM/pod = $150 hardware cost per subscriber. At $15–20/month that pays back in
**8–10 months**, well inside an 18-month-plus retention curve.

**This is why the sensor-count decision should be made on data quality first.** The user's
directive was right and the economics support it.

### The catch — the "fish" problem
HaaS inverts the cash curve. You fund the full COGS of every unit up front and recover it
over months. **The faster you grow, the deeper the hole gets.** This is the standard failure
mode for hardware-subscription startups and it is a financing problem, not a business-model
problem.

- Need to model a **BOM payback period** on fully-loaded COGS (not just BOM — include
  assembly, test, packaging, shipping, support, and returns)
- Requires debt/venture-debt or inventory financing to scale; equity alone is expensive
- Churn before payback is a pure loss of the full hardware cost — early churn is far more
  damaging than in a SaaS business
- Returned pods must be refurbishable. Sealed IP68 pods are good here; skin-contact
  garments (Athos) were not
- **Do not offer month-to-month at launch.** Annual commitment or a hardware deposit until
  the payback math is proven

### Pricing implication
Individual: **$15–25/month, annual commitment**, hardware included. Anchored below WHOOP
($30/mo) because we do a narrower job.

Team: subscription per athlete per season, sized to fit inside a $3–8K HS budget — i.e.
**$500–1,500/team/year all-in**, hardware included. That is the only structure that fits
the numbers in §1.

---

## 4. The Founder / H-1B Constraint — Materially Changed

`CLAUDE.md` states "cannot monetize while on H-1B — build as open-source/portfolio project
during this phase." **This is out of date.**

### DHS rule effective 17 January 2025
- DHS **eliminated the traditional employer-employee relationship requirement** that
  historically blocked founder self-sponsorship
- **Founders owning >50% (up to 100%) of a US company can now petition for their own H-1B**
- Founders with ≤50% and no majority voting rights are not subject to the beneficiary-owner
  provisions merely by holding equity

### Conditions that still apply
1. **Specialty occupation requirement is unchanged.** The role must genuinely require a
   bachelor's-or-higher in a specific specialty. An embedded/ML engineering role at a
   sensor company qualifies cleanly; "CEO" does not.
2. **Independent oversight is required** — a board or governance structure that can hire,
   fire, and supervise the beneficiary. A cofounder in India does not satisfy this alone;
   you need at least one genuinely independent director or an advisory board with real
   authority.
3. **Initial beneficiary-owner approvals are limited to 18 months**, then an 18-month
   extension, before normal validity applies. Plan for two early filings.
4. Cap-subject unless the sponsor qualifies for cap exemption — the lottery still applies
   for a new petition.
5. Current employment must be handled correctly; concurrent H-1B is possible but must be
   structured, not improvised.

### The structure the user described works
US C-corp (Delaware) + cofounder in India + revenue in USD + engineering cost in India is a
completely standard setup. Note the specifics:
- **Transfer pricing:** the India entity must be paid at arm's length (typically
  cost-plus 10–15% for an R&D/services subsidiary). Not optional; it is what makes the
  arrangement defensible to both tax authorities.
- India entity as a **wholly-owned subsidiary** of the US C-corp is cleaner than two
  independent companies with a services agreement, and is what investors expect.
- The Section 44ADA presumptive-taxation route in `ecosystem-business-model.md` applies to
  an *individual professional*, not to a company. If the cofounder is a salaried employee
  of an Indian subsidiary, 44ADA does not apply. If they are an independent contractor
  billing the US entity, it may. **These are different structures — pick one deliberately.**

### What this changes
**The two-year no-monetization assumption should be dropped.** It was the main reason for
deferring the business entirely. The real constraints are now: filing cost and timing,
lottery risk, the independent-oversight requirement, and the specialty-occupation framing
of the founder's own role.

**This is a "consult an immigration attorney before acting" item, not a "read a blog post"
item.** Budget $5–10K for proper counsel before any filing. Nothing in this section is
legal advice.

---

## Sources
- HS athletic training budgets — https://pmc.ncbi.nlm.nih.gov/articles/PMC2808759/
- HS athletic trainer access decline — https://projectplay.org/news/2023/4/3/health-experts-its-time-for-high-schools-to-budget-money-for-athletic-trainers
- NCAA catastrophic injury insurance ($90K deductible) — https://www.ncaa.org/student-athletes/insurance-and-medical-coverage/catastrophic-injury-insurance-program/
- NCAA per-athlete insurance cost / pooling — https://www.cbssports.com/college-football/news/ncaa-ads-consider-pooling-athletes-for-cheaper-better-health-insurance
- Workers' comp wearable ROI — https://strongarmtech.com/blog-posts/the-roi-of-safety-wearables-insurance-loss-control/
- Nationwide on wearables and claims — https://www.nationwide.com/business/risk-management/services-resources/resource-library/articles/wearable-technologies-can-help-reduce-injury-claims-and-costs
- Milliman, workers' comp loss experience — https://www.milliman.com/en/insight/improving-workers-compensation-loss-experience-using-wearable-technology
- FDA 2026 general wellness guidance — https://www.womblebonddickinson.com/us/insights/blogs/fdas-2026-general-wellness-policy-and-what-it-means-manufacturers-wearable-devices
- FDA wellness vs device line — https://www.troutman.com/insights/fdas-2026-guidance-on-general-wellness-devices-policy-for-low-risk-devices/
- WHOOP metrics — https://sacra.com/c/whoop/ and https://savedelete.com/article/whoop-575m-10-billion-valuation-1b-arr/
- HaaS working capital ("fish") problem — https://blog.hardfin.com/why-is-hardware-as-a-service-haas-complicated-for-the-finance-org
- H-1B founder self-sponsorship (Jan 2025 rule) — https://www.startsmartcounsel.com/resource-center/self-sponsorship-under-the-new-h-1b-rules-a-strategic-guide-for-startup-founders
- H-1B entrepreneur analysis — https://blog.cyrusmehta.com/2026/07/h-1b-for-entrepreneurs-can-you-transfer-your-h-1b-to-your-own-startup.html
- Running injury base rates — https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4473093/
