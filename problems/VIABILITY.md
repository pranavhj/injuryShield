# Viability — Is This Worth Pursuing?

**Created 2026-08-23. This is the decision document. `TRACKER.md` is the work list;
this is what decides whether the work list matters.**

The problem with 80+ tracked problems is that they look equally weighted and invite you to
work on whichever is most tractable. They are not equally weighted. **Roughly five of them
can kill the company; the rest are engineering.** This file separates them, orders the
killers by how cheaply they can be tested, and defines the gates.

---

## 1. Kill Register

Each risk: what it is, honest probability it ends the company *in its current form*, what
would resolve it, and what that test costs.

Probabilities are judgement calls against the evidence, not measurements. They are here to
force ordering, and should be revised at every quarterly review.

### K1 — Injury prediction does not work · **FIRED, MITIGATED**
Status: **confirmed true.** See `predictive-validity.md`. Bahr 2016, Ruddy AUC 0.58,
23/25 null meta-analyses, ACWR RCT null, GRF↛tibial load.

Killed the original product. Did **not** kill the company, because a defensible reframe
exists (real-time coaching + within-subject degradation measurement). Cost of discovery:
one day of research. Cost had we discovered it after building hardware: the company.

**This is the template for everything below. Every remaining killer is worth a day of
research before it is worth a month of building.**

---

### K2 — The multi-pod architecture is the thing that kills companies · **~55%** · CHEAP TO TEST
Every commercial winner in this market uses one sensor or fixed equipment. Every
multi-point body-worn consumer product has died or stalled — Athos, NURVV, formsense,
Lumo, UA HealthBox, Xsens-as-consumer. See `market-teardown.md` §0.

We chose 5–7 pods on 2026-08-23 for good technical reasons (3 pods give no joint angles).
**That decision optimises the axis that does not kill you and worsens the axis that does.**

The trade, stated plainly:
> More pods buy data quality. More pods cost setup friction and retention — the exact
> failure mode of every company that tried it.

**Resolves by:** founder wears the full pod set for 30 consecutive days of real running.
Two measurements, both objective: (a) median don/doff time, (b) **on how many eligible
days did he actually put them on** without being told to. (b) is the real answer. If a
motivated founder who owns the company skips days, no customer will do better.

**Cost:** one prototype set, 30 days, near-zero cash. **Do this first.**

**Open sub-question:** is there a 1–2 pod configuration that captures bilateral asymmetry?
Two ankle pods is the minimum for left/right comparison and is only marginally worse
friction than one. That may be the whole product. Worth explicit analysis before defaulting
to 5.

---

### K3 — The output may not be valuable, even as coaching · **~45%** · CHEAP TO TEST
The reframe rests on the ARION mechanism — real-time cues improve mechanics. But the
sharpest line in the NURVV post-mortem is a value-proposition attack, not a product one:

> *"If running pain-free, you may be best advised not to change your Pronation"*

If an athlete is not hurting, changing their form may harm them. That leaves a narrow
addressable moment: runners who are currently symptomatic, returning from injury, or
deliberately in a form-change block. It may be a much smaller market than "all runners."

**Unresearched and load-bearing:** does gait retraining benefit *asymptomatic* runners?
The ARION RCT enrolled general recreational runners, so it is weak evidence for yes — but
its primary analysis was null. **This needs a dedicated literature search. It is the
highest-value unanswered research question in the project.**

**Also resolves by:** 20 structured interviews with runners. Not "would you buy this" —
that answer is worthless. Ask: *when did you last change something about how you run, what
prompted it, and what would have made you trust the advice?*

**Cost:** two days of literature, two weeks of interviews. **Do this second.**

---

### K4 — Platform absorption · **~40%** · FREE TO TEST
Garmin now computes running power from the wrist on Fenix 7 / Epix Gen 2, deprecating its
own Running Dynamics Pod. Apple Watch Ultra ships running dynamics natively. Cadence, GCT,
vertical oscillation, stride length are all now wrist-derivable.

**Any value we build on a wrist-replicable metric is on a countdown timer.** NURVV died
partly because $299 bought metrics a $200 watch already provided.

Structurally defensible ground: **bilateral asymmetry and per-limb mechanics.** A wrist
device is on one arm and is blind to left/right difference. That is not a temporary
advantage; it is a geometric one.

**Resolves by:** classify every metric in the product as *wrist-replicable* or
*wrist-impossible*. If the value proposition survives deleting every wrist-replicable
metric, K4 is contained. If it does not, the product is a feature waiting to be absorbed.

**Cost:** one day at a desk. **Do this immediately — it is free and it may reshape the
whole spec.**

---

### K5 — Retention · **~50%** · EXPENSIVE TO TEST
Hardware-as-subscription dies without retention, and churn before BOM payback is a total
loss of hardware cost — far worse than SaaS churn.

The comparables are discouraging. WHOOP holds >80% because you *never take it off*. Our
pods must be donned and doffed every session. ARION: only ~60% of completers wanted to keep
using it, and **47% of dropouts were caused by app malfunctions.** ARION itself is 19
employees after 11 years.

**Partially resolves by:** K2's 30-day founder test measures the same behaviour.
**Fully resolves only by:** a beta cohort of 30–50 runners tracked for 90 days. Cost:
30–50 prototype sets. That is the first genuinely expensive experiment, and it should not
be run until K2, K3 and K4 have passed.

---

### K6 — Consumer hardware base rate · **structural** · CANNOT TEST, ONLY MITIGATE
97% of consumer hardware startups fail. 24% raise a second round. ~90% never reach market.
Top causes: no consumer demand, high burn, post-crowdfunding fade, product strategy error.

Not testable. Mitigations, all borrowed from survivors in `market-teardown.md`:
- Pre-sell before committing to inventory (Stryd: 5× goal in 12 days)
- Stay radically narrow at launch (one sport, one job)
- Keep burn near zero during the research phase — which is where we are
- Treat acquisition as a legitimate outcome; Catapult is buying

---

### K7 — Working capital under subscription · **~25%** · CHEAP TO MODEL
The HaaS "fish" problem: full COGS up front, recovered over months, and the faster you grow
the deeper the hole. 5 pods × ~$30 = $150/subscriber before assembly, test, packaging,
shipping, support and returns.

**Resolves by:** a spreadsheet. Model fully-loaded COGS, payback period, and churn
sensitivity. If 20% churn at month 6 makes the model insolvent, that is a design constraint
on pricing and commitment terms, discovered for free.

**Cost:** one day. Do it alongside K4.

---

### K8 — Software reliability · **~20%** · EXECUTION RISK
47% of ARION dropouts were app malfunctions. NURVV's app contradicted its own metrics and
generated incoherent training plans. **In this category, software defects kill more products
than sensor accuracy does.**

Not a research question — a standards question. It argues for the phone-side inference
decision already made (ship fixes in an app update, not an OTA campaign) and for a narrow
feature set that can actually be made correct.

---

### K9 — Distribution and gatekeepers · **~20%**
Running tech has concentrated gatekeepers; a DC Rainmaker review can make or break a
product, and his NURVV review reads as a post-mortem. Integration with TrainingPeaks,
Garmin Connect and Strava is table stakes, not a v2 item.

Mitigation: build in public, community-calibrated, Stryd-style. Earn the review before
asking for it.

---

### K10 — Founder capacity and immigration · **~15%**, reduced
Weaker than believed. The Jan 2025 DHS rule permits founder self-sponsorship at >50%
ownership. Remaining constraints: specialty-occupation framing, independent-oversight
requirement, 18-month initial approvals, lottery risk. Attorney needed before acting.

Real residual risk is **bandwidth**, not legality: a full-time job plus hardware plus ML
plus a distributed cofounder.

---

## 2. What This Ordering Implies

Sorted by information gained per dollar:

| Order | Test | Resolves | Cost | Duration |
|---|---|---|---|---|
| **1** | Classify every metric wrist-replicable vs wrist-impossible | K4 | free | 1 day |
| **2** | Model fully-loaded COGS, payback, churn sensitivity | K7 | free | 1 day |
| **3** | Literature: does gait retraining help *asymptomatic* runners? | K3 | free | 2 days |
| **4** | Founder wears full pod set, 30 days — measure **days actually worn** | K2, part K5 | 1 prototype set | 30 days |
| **5** | 20 structured runner interviews | K3 | free | 2 weeks |
| **6** | Beta cohort, 30–50 runners, 90 days | K5 | 30–50 sets | 4 months |

**Items 1–3 cost nothing but time and could each individually reshape or end the project.
None of them requires a single line of firmware.** They should be done before any hardware
decision is revisited.

**Item 4 is the pivotal one** and it is nearly free. One honest number — how many days out
of 30 did you actually wear five pods — tells you more about this company's future than any
amount of sensor-fusion work.

---

## 3. Finding The Problems We Don't Know About

The user's concern is correct: the dangerous risks are the unlisted ones. K1 was unlisted
for the project's entire life until it was researched. Standing practices to surface more:

**1. Quarterly pre-mortem.** It is 2029 and the company is dead. Write the obituary in
detail — what killed it, in what order, what the warning signs were. Do it cold, before
looking at this file. Anything new goes into the register.

**2. Failure archaeology.** For every dead company in the space, find the *actual*
post-mortem, not the press release. NURVV's real post-mortem was a product review, not a
business article. Still to mine: Lumo Run, Moov, Sensoria, dorsaVi, Athos ex-employees.

**3. Talk to people who already did it.** Ex-employees of NURVV, Athos, Lumo know things
that were never written down. One honest conversation is worth ten market reports.

**4. Adjacent-domain scan.** What killed companies in neighbouring categories — smart
textiles, quantified self, clinical gait labs, consumer medical? Failure modes travel.

**5. Ask "who tried this and why did they stop?" of every design decision.** Applied to
"3 pods," it would have surfaced K2 immediately.

**6. Write the bear case a VC would write** before pitching anyone. If you cannot write a
convincing one, you do not understand the business yet.

**7. Domain red-team.** Each of these sees a failure class the others cannot: a physio, an
athletic trainer, a running coach, a contract manufacturer, an immigration attorney, a
product liability lawyer. One conversation each, early.

**8. Re-audit the premises annually.** K1 sat unexamined under 80 tracked problems. Assume
there is another one.

---

## 4. Decision Gates

**Gate 0 — now → +1 month.** Complete tests 1–3 (all free). Start test 4.
*Continue if:* the value proposition survives deleting every wrist-replicable metric, and
the literature does not say gait retraining harms asymptomatic runners.
*Stop or pivot if:* the product is only wrist-replicable metrics.

**Gate 1 — +2 months.** Founder 30-day wear test complete.
*Continue if:* pods worn on ≥70% of eligible days, median don/doff under 90 seconds.
*Reduce pod count and retest if:* 40–70%.
*Stop the multi-pod thesis if:* below 40%. Fall back to a 1–2 pod asymmetry-only product,
or to the industrial market where wear is mandated rather than chosen.

**Gate 2 — +4 months.** Interviews complete, COGS model built.
*Continue if:* a coherent buyer with a real budget and a repeatable trigger to buy exists.

**Gate 3 — +9 months.** Beta cohort at 90 days.
*Continue if:* ≥60% still active. *Stop or pivot if:* below 40%.

---

## 5. The Three Live Options

**A · Consumer running product.** Honest verdict: **the evidence is against it.** 97%
base rate, every multi-sensor consumer product dead, platform absorption active, value
unproven even as coaching, and the closest honest comparable (ARION) is 19 people after
11 years. Not impossible — Stryd survived — but Stryd did it with one pod, one metric, and
a community that funded it up front.

**B · Industrial athlete / workers' comp.** Materially better on every structural axis:
a payer who directly eats the injury cost, proven ROI (250%, 52–64% injury reduction),
funded comparables (StrongArm $50M, Soter $12M, Modjoul $11.7M), **no consumer retention
problem because the employer mandates wear**, and no platform-absorption risk. Costs: less
personally interesting, and no dogfooding.

**C · Open instrument + dataset.** Cheap, keeps every option open, fits the current phase,
and builds the one asset nobody has — the dataset from `predictive-validity.md` §9. Stryd's
community-calibrated model is the validated playbook. **This is the only option that makes
A and B more likely to work later rather than less.**

**These are not exclusive, and C is the correct next move regardless of whether A or B is
the eventual business.** Option C is also the cheapest way to run tests 1–6.

---

## 6. Honest Overall Read

The project is in better shape than it was a day ago, because the thing that would have
killed it in year three has been found in year zero, for the price of a day's research.
That is the process working.

But the honest position is: **the central architectural decision (multi-pod) points
directly at the market's strongest failure pattern, and the value proposition that survived
the evidence review has not yet been shown to be worth paying for.** Two open killers, both
cheap to test, neither tested.

**The correct posture is not "build it" or "abandon it." It is: spend the next month and
almost no money answering K4, K7, K3 and starting K2.** If those pass, this is worth
serious commitment. If K2 fails at the founder's own wrists — if you will not wear five
pods for thirty days — that is the answer, and it cost one prototype set to learn.

Nothing about the current evidence says stop. Several things say *do not build hardware
yet.*

---

## Changelog
- **2026-08-23** — Created. Kill register K1–K10, cheapest-first test ordering, unknown-unknowns
  practices, decision gates, three live options. Backing research: `market-teardown.md`,
  `predictive-validity.md`, `buyer-and-liability.md`, `sensor-architecture.md`.
