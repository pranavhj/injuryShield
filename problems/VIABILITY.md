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

**Open sub-question — ANSWERED 2026-08-23, and it substantially defuses K2.** The
best-evidenced intervention (K3, `predictive-validity.md` §4B) was delivered in the field
with **two IMUs, one on each tibia.** Peak tibial acceleration, per-leg audio cues,
within-subject thresholds. 100% session adherence in the feasibility cohort.

**Two pods is not five, and it is the same wear burden as Playermaker's two cleat sensors —
which sells at $249 into 50+ D1 colleges and 100+ US clubs.** The one-sensor survival
pattern in `market-teardown.md` §0 does not indict a two-pod symmetric configuration
anywhere near as hard as it indicts 5–7.

**Revised probability: ~55% → ~30%**, conditional on **two tibial pods being the default
tier**, not five.

**Resolved further 2026-08-24 by the tier ladder** (`research/bom-and-pricing.md` §3).
The 5–7 pod question stops being an architecture bet and becomes a **customer choice**:
Core (2 pods, the RCT-validated config), Plus (3, + sacrum), Pro (5, + thighs → knee angle),
Full (7, + feet → ankle angle). Same analysis pipeline; the app **states what is missing**
at each tier.

That defuses the market-pattern objection in `market-teardown.md` §0, because the *default*
product is two pods — the low-friction configuration — and higher pod counts are opt-in for
customers who have already decided they want more. Nobody is forced up the ladder.

**The 30-day founder wear test is still the gating experiment**, but its job has changed
twice: it is no longer "will anyone tolerate five pods," it is (a) confirm two pods is a
habit that sticks, and (b) measure actual don/doff seconds at 2, 3, 5 and 7 pods to find
where the friction cliff is. **That is now a ladder-pricing input, not just a kill test.**

---

### K3 — The output may not be valuable, even as coaching · **RESOLVED ~45% → ~15%** · 2026-08-23
**Tested and largely cleared.** See `predictive-validity.md` §4B.

**Chan et al. 2018, AJSM.** n=320 novice runners, RCT, 2 weeks of gait retraining with
real-time feedback, 12-month follow-up. Injury occurrence **16% vs 38%**;
**HR 0.38 (95% CI 0.25–0.59) — 62% risk reduction.** In runners who were *not injured at
baseline*. This directly answers the NURVV objection: retraining pain-free runners reduced
their injuries substantially.

**The field version needs two pods.** A feasibility study (PMC11945614) delivered it outdoors
with IMUs on both tibias, real-time audio cues from a phone when peak tibial acceleration
exceeded **80% of the runner's own baseline**, different tone per leg, faded over the final
four of eight sessions. PTA −29%, loading rate −36%, held at one month, 100% adherence.

**Residual risk (~15%):** Chan studied *novice* runners — highest incidence, most form
headroom. Generalization to trained runners is unproven. It is a single trial, lab-delivered
with visual feedback. The field study is n=7. And the mechanism is not understood — §2 shows
GRF impact metrics do not track tibial bone load, yet impact-reduction feedback reduced
injuries. **We know it works; we do not know why. Do not claim otherwise.**

**Remaining work:** the 20 runner interviews (still worth doing, now about willingness to
pay rather than whether the thing works), and eventually a trained-runner replication.

<details>
<summary>Original K3 framing, retained for the record</summary>

### K3 (original) — The output may not be valuable, even as coaching · ~45%
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
</details>

---

### K4 — Platform absorption · **RESOLVED ~40% → ~15%** · 2026-08-23
**Tested and contained.** See `research/capability-envelope.md`.

The test was: does the value proposition survive deleting every metric an alternative can
produce? **It does.** Four capabilities are structurally ours for physical reasons, not
software reasons:

1. **Peak tibial acceleration measured at the tibia** — no camera or wrist device can obtain it
2. **Real-time feedback during the activity** — every alternative measures; only a body-worn
   pod intervenes
3. **Location independence** — no venue, no install, no calibrated volume
4. **Per-limb bilateral data outside an instrumented venue** — a wrist is on one arm and is
   permanently blind to asymmetry

Decisive point: the intervention with the best evidence in the field (K3 above) is built on
**exactly these four capabilities and nothing else.** It cannot be delivered by any
alternative — not on cost grounds, but because they cannot measure the variable or close
the loop.

**Camera threat, checked properly.** Optical skeletal tracking is further along than assumed:
Hawk-Eye SkeleTRACK does **29 body points per player in real time**, powering FIFA
semi-automated offside; NFL and NBA use Hawk-Eye. So "cameras can't track everyone on a big
field" is false at elite level. **But it is league-level infrastructure installed in
stadiums and funded centrally** — goal-line tech alone ran £125–250k per ground, and
*"for 99% of the football world… you cannot buy them for your club."* Markerless accuracy is
also 3–15° sagittal and **3–57° transverse** — and transverse rotation is where ACL
mechanism lives.

**Cameras own the instrumented venue on match day. Nothing owns the training ground, the
road, or the amateur field.** The gap is structural because camera cost is per-site and the
athlete must be inside the volume.

**Residual risk (~15%):** further wrist absorption of context metrics (assume anything
derivable from a single trunk/wrist signal ships natively within 24 months), and the
possibility that a platform ships bilateral asymmetry — a red trigger in
`market/WATCHLIST.md`.

**Standing design rule:** never let a wrist-replicable metric be load-bearing. Cadence, GCT,
vertical oscillation, stride and running power are context, never the pitch. NURVV died
charging $299 for exactly those.

---

### K4-old — Platform absorption · original framing, superseded above
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

### K5 — Retention and setup friction · **REFRAMED 2026-08-24** · see `research/friction-and-retention.md`
**An external startup consultant independently identified setup friction and retention as
the two killers. They are right, and the data is worse than stated.**

**Wrist wearables — the lowest-friction category that exists — are abandoned at ~30% within
6 months** (Gartner), 42% by one analysis, and **50% of college students quit within two
weeks** (IEEE). The critical window is the first 2–4 weeks. Most-cited reason: *"most
wearables give you data, but they do not tell you what to do with it."*

That is the floor for a device requiring **zero** additional decisions. Anything with a
separate attachment step starts worse. **Multi-pod makes it strictly worse.**

**But the conclusion "therefore only pro teams, where compliance can be enforced" does not
follow — because our product is not a perpetual wearable.** The RCT-validated intervention
is a **finite 8-session programme over 2–3 weeks**, and the published field study reports
**100% session adherence and 100% completion, with 85% retention at one month.**

**People abandon habits. People complete courses.** The graduation property that broke the
subscription model (K11) is the same property that solves retention here — and since we now
sell outright, graduation costs us nothing.

**The ask must be framed as:** *"Wear these for 8 runs over 3 weeks, then you're done and
you keep the benefit."* Never *"wear these forever."*

**Form factor rule that follows:** attach to something the athlete already puts on. Runners
already put on shoes. Playermaker (cleat-mounted, $249, 50+ D1 colleges) and Stryd (foot
pod, survived a decade) both prove it. **Insole placement has moderate-to-high association
with impact loading and is "easily and consistently fixated"** — heel-mounted specifically
has *poor* association, so placement is not a free choice.

**Residual risk (~30%, down from 50%):** the 100% adherence figure is n=7; field adherence
at scale is unproven; and **one programme per customer is a small business unless there is a
repeat trigger** (new injury, new shoes, new training block). Repeat rate is unmeasured and
determines whether this is a company or a product.

<details>
<summary>Original K5 framing, retained</summary>

### K5 (original) — Retention · ~50% · EXPENSIVE TO TEST
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
</details>

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

### K11 — The science says the customer should graduate · **NEW, ~40%** · 2026-08-23
**Surfaced by the K3 research. This is the new hardest problem.**

The evidence-based intervention is **a 2–3 week retraining block with feedback deliberately
faded out.** Fading is not a limitation — it is the design. Faded feedback produces
*superior* retention and transfer versus constant feedback, because constant feedback
creates dependence. Chan's trial: two weeks of retraining, benefits measured at **twelve
months**. The field study: eight sessions, faded across the last four, gains held at one
month with no device.

**That is in direct conflict with hardware-as-subscription.** WHOOP retains >80% because you
never take it off. A gait retrainer works *because you eventually don't need it*. A product
that succeeds makes itself unnecessary in three weeks.

If we ignore this and design for perpetual wear, we are (a) contradicting the mechanism that
makes the intervention work, and (b) building the dependence the motor-learning literature
says to avoid.

**RESOLVED 2026-08-23 — see `research/unit-economics.md`. K11 40% → ~10%.**

The economics were modelled across all four options. **Perpetual subscription requires
every customer to stay 9 months just to return the cash spent acquiring them** ($90 COGS +
$80 CAC ÷ $19/mo). The intervention takes three weeks. Even at optimistic COGS/CAC the
break-even is ~5 months. Subscription is the *worst* fit for this intervention.

**Outright sale at $299 (2-pod kit + 6-week programme + 12 months app) contributes $129 per
unit from unit one**, matching Playermaker's proven $249 structure in this exact segment.
**Graduation stops being churn and becomes the success story.**

This resolves K11 *and* K7 (the working-capital "fish" problem disappears with no
subscription to fund), and downgrades K5 from existential to cosmetic.

**Options as modelled:**
1. **Program / rental model.** Pay for a retraining block; return the pods. Matches the
   science exactly. Kills recurring revenue per customer but **fixes the HaaS working-capital
   problem outright** — one pod set serves many customers in sequence.
2. **Clinic / physio channel.** The clinic buys one or a few sets and cycles patients
   through a structured programme. Payer exists (patient or insurance), device is reused,
   the professional supplies the coaching judgement we cannot. Strong fit with the
   claim-language constraints in `buyer-and-liability.md` §2.
3. **Periodic re-check subscription.** Quarterly form audit rather than continuous wear.
   Lower value, lower price, but genuinely recurring and honest.
4. **Broaden the job.** Give a reason to keep wearing — training load, performance, other
   sports, return-to-play tracking. Risks becoming the undifferentiated thing Garmin absorbs.

**Decision: launch with outright sale (option 5, added after modelling).** Keep rental as
the best capital-efficiency alternative (17× hardware turn), subscription only as a cheap
$8–10/mo post-programme monitoring tier, and clinic as a later channel.

**On clinics — the regulatory assumption was inverted.** FDA's Jan 2026 CDS guidance
*loosened* the rules ("FDA cuts red tape"; single-recommendation CDS now qualifies for the
non-device exemption), and **the exemption is specifically for software intended for health
care professionals** — patient-facing software gets *less* latitude. VALD sells ForceDecks
into US PT clinics with no regulatory friction reported by practitioners. **Clinics are the
lowest-regulatory-exposure option of the four.** The real objection to them is commercial —
~10× CAC, long sales cycles, a B2B motion a solo founder cannot run. Right conclusion,
wrong reason.

`buyer-and-liability.md` §3 is now partly superseded — it argued for subscription on the
assumption of perpetual use.

**Residual K11 (~10%):** if gait changes decay in 3–6 months, a genuine re-training cycle
exists and subscription becomes viable after all. That would be good news. Watch for
retention studies.

---

### K10 — Founder capacity and immigration · **~15%**, reduced
Weaker than believed. The Jan 2025 DHS rule permits founder self-sponsorship at >50%
ownership. Remaining constraints: specialty-occupation framing, independent-oversight
requirement, 18-month initial approvals, lottery risk. Attorney needed before acting.

Real residual risk is **bandwidth**, not legality: a full-time job plus hardware plus ML
plus a distributed cofounder.

---

## 2. Test Ordering and Status

Sorted by information gained per dollar. **Updated 2026-08-23 after tests 1 and 3.**

| # | Test | Resolves | Cost | Status |
|---|---|---|---|---|
| 1 | Capability envelope vs wrist / camera / fixed equipment | K4 | free | ✅ **DONE — K4 40%→15%** |
| 3 | Literature: does gait retraining help *asymptomatic* runners? | K3 | free | ✅ **DONE — K3 45%→15%** |
| 2 | Model COGS + all four revenue models | K7, **K11** | free | ✅ **DONE — K11 40%→10%, K7 25%→10%** |
| 4 | **Wear test on bought hardware** — 30 days; days actually worn + don/doff seconds at 2/3/5/7 pods | K2, part K5 | **~$600, no build** | ⬜ **next** |
| 5 | 20 runner interviews | K3 residual | free | ⬜ |
| 6 | Beta cohort, 30–50 runners, 90 days | K5 | 30–50 kits | ⬜ gated |

**Test 4 requires no manufacturing.** `research/bom-and-pricing.md` §5: 2 × mbientlab
MetaMotionS ($260, 400 Hz logging to onboard flash, CSV + Python SDK) replicates the
RCT-validated two-tibia protocol with zero firmware written; 1 × SlimeVR set ($219,
open-source, MIT/Apache) explores the 3/5/7 ladder cheaply; ~$120 of IMU samples answers
chip selection on our own task. **≈$600 total.**

**Two of the three free tests are done and both came back favourable.** The remaining free
test (COGS/business-model modelling) is now more important than it was, because K11 changed
what has to be modelled.

**Item 4's job has changed.** It is no longer "will anyone tolerate five pods" — the
evidence points at two. It is now: confirm two tibial pods is a habit that sticks, and
capture the first within-subject baseline data.

### Kill register at a glance, after 2026-08-23

| Risk | Was | Now | Note |
|---|---|---|---|
| K1 prediction doesn't work | fired | mitigated | reframe holds |
| K2 multi-pod architecture | 55% | **30%** | conditional on shipping **two** pods |
| K3 output not valuable | 45% | **15%** | Chan RCT, HR 0.38 |
| K4 platform absorption | 40% | **15%** | four structural capabilities survive |
| K5 retention / friction | 50% | **30%** | reframed 2026-08-24: finite programme, not perpetual wear. Published 100% session adherence. Residual = repeat-purchase rate |
| K7 working capital | 25% | **10%** | no subscription to fund; inventory only |
| K11 customer graduates | 40% | **10%** | resolved by outright sale — graduation is the success story |

**After 2026-08-23, the largest remaining risks are K2 (30%, untested — the 30-day wear
test) and K6 (the 97% consumer-hardware base rate, structural). CAC is the biggest
un-measured number in the business and is cheap to measure.**

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

## 5. The Live Options

**A · Consumer running product — upgraded, but now shaped differently.** The evidence
review that cleared K3 and K4 makes this materially more attractive than it was this
morning: there is a real RCT-backed intervention (HR 0.38), it needs only two pods, and it
sits inside a capability envelope no camera or wrist device can enter. What remains against
it is the 97% hardware base rate, K5 retention (untested), and **K11 — the customer
graduates in three weeks.** A perpetual-subscription consumer product is now the *worst*
fit for the evidence; a programme is the best fit.

**A′ · Clinic / physio channel — newly the strongest sports option.** Falls directly out of
K11. A clinic buys one or two pod pairs and cycles patients through a structured 2–3 week
retraining programme. It matches the intervention's actual shape, has an existing payer,
reuses hardware across many customers (which dissolves K7 working capital), and puts a
qualified professional between us and the claim-language risk in `buyer-and-liability.md`
§2. **This did not exist as an option until K11 surfaced. It deserves proper scoping.**

**B · Industrial athlete / workers' comp.** Still strong on structure: a payer who eats the
injury cost, proven ROI (250%, 52–64% injury reduction), funded comparables (StrongArm
$50M, Soter $12M, Modjoul $11.7M), employer-mandated wear so no retention problem, no
platform-absorption risk. Kinetic's REFLEX is mechanically the same intervention. Costs:
less personally interesting, no dogfooding.

**C · Open instrument + dataset.** Cheap, keeps everything open, fits the current phase,
builds the asset nobody has. Stryd's community-calibrated playbook. **Still the correct
next move regardless of which of A / A′ / B becomes the business**, and still the cheapest
way to run the remaining tests.

---

## 6. Honest Overall Read

**Updated 2026-08-23, after tests 1 and 3.**

Two free desk tests moved three risks and surfaced a fourth. Net position is meaningfully
better than this morning:

- **K3 was the big one and it cleared.** Chan et al. — n=320, RCT, 12-month follow-up,
  **HR 0.38 (0.25–0.59)** — is the strongest evidence in the entire project, in either
  direction, and it is *for* us. Gait retraining reduces injuries in runners who are not
  hurting. That was the open question the whole reframe rested on.
- **K4 cleared.** Four capabilities are structurally ours. Decisively, the RCT-backed
  intervention is built on exactly those four and nothing else.
- **K2 halved.** The field-validated configuration is **two tibial pods**, not five. The
  one-sensor survival pattern does not indict two symmetric pods the way it indicts 5–7.
- **K11 appeared, then resolved the same day.** The intervention is a 2–3 week programme
  with feedback deliberately faded, so the customer graduates. Modelling all four revenue
  options showed **perpetual subscription needs 9 months of average customer life just to
  break even** — the worst possible fit. **Outright sale at $299 contributes $129 from unit
  one**, and turns graduation from a churn event into the success story. K11 40%→10%,
  and it took K7 down with it (no subscription to fund ⇒ no working-capital hole).
- **K5 downgraded 50%→20%** as a consequence. Retention was existential under subscription;
  under outright sale it only affects word-of-mouth and renewals.

**The honest position now: the science is more supportive than expected, and the business
model is settled and simpler than assumed.** Selling the product outright is not a retreat
to the old plan — the old plan was $35/pod hardware with no programme attached. This is a
$299 kit wrapped around an RCT-backed intervention, which is a different product.

**Largest remaining risks: K2 (30%, untested) and K6 (97% consumer-hardware base rate,
structural).** And **CAC is the biggest un-measured number in the business** — every model
is more sensitive to it than to BOM, and it can be measured with a landing page and a small
ad spend before anything is built.

**Posture: still do not build hardware.** Run test 4 (two pods, 30 days) and add a CAC probe
ahead of it, since it is cheaper and faster. Physio interviews stay on the list but drop in
priority — clinics are a later channel, not the launch.

Nothing says stop. Considerably more than yesterday says this could work.

---

## Changelog
- **2026-08-23 (latest)** — Ran test 2 (`research/unit-economics.md`). **K11 40%→10%,
  K7 25%→10%, K5 50%→20%.** Decision: **launch with outright sale, $299 for a two-pod kit +
  6-week programme + 12 months app.** Perpetual subscription needs 9 months average customer
  life to break even against a 3-week intervention. Clinic channel's regulatory burden was
  found to be *inverted* — FDA's Jan 2026 CDS guidance loosened rules and the exemption is
  specifically for clinician-facing software, so clinics are the lowest-regulatory-exposure
  option; the real objection is commercial (10× CAC, B2B motion). Kept as a later channel.
- **2026-08-23 (later)** — Ran tests 1 and 3. K3 45%→15% (Chan 2018 RCT, HR 0.38, n=320,
  asymptomatic runners). K4 40%→15% (`capability-envelope.md`; four structural capabilities;
  camera threat is real but stadium-bound). K2 55%→30% (field-validated config is **two**
  tibial pods). **New K11 at 40%** — faded feedback means the customer graduates, which
  conflicts with hardware-as-subscription and opens the clinic/rental option A′.
- **2026-08-23** — Created. Kill register K1–K10, cheapest-first test ordering, unknown-unknowns
  practices, decision gates, three live options. Backing research: `market-teardown.md`,
  `predictive-validity.md`, `buyer-and-liability.md`, `sensor-architecture.md`.
