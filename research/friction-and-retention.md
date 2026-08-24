# Setup Friction and Retention — The Actual Central Problem

**Researched 2026-08-24.** Prompted by a startup consultant's assessment that setup friction
and retention are the two things that kill products like this. **They are right, the data is
worse than they said, and it reshapes the product.**

---

## 1. The Abandonment Numbers

These are for **wrist wearables** — the lowest-friction category that exists.

| Finding | Source |
|---|---|
| ~**30%** of wearable owners abandon within 6 months | Gartner, consistent across surveys |
| **29%** of smartwatches, **30%** of fitness trackers abandoned | Gartner |
| **42%** lose interest after the first six months | Big Think analysis |
| **50% of college students stopped within TWO WEEKS** | IEEE study |
| Critical window: **first 2–4 weeks** | Multiple |

**Top stated reason for abandonment:**
> *"Most wearables give you data, but they do not tell you what to do with it."*

Read that carefully. A third of people abandon a device that requires **zero additional
decisions** — you put on a watch you were going to wear anyway. That is the floor for our
category, not the ceiling. Anything requiring a separate attachment step starts worse.

**The consultant's argument is therefore correct on the facts.** The counter-argument that
follows is not a rebuttal of it.

---

## 2. Why "Only Pro Teams" Does Not Follow

The argument runs: friction kills adoption → amateurs lack motivation → only environments
where compliance can be enforced (pro teams) work → tiny market.

**Every step is sound except the one that assumes our product is a perpetual wearable.
It is not.**

`predictive-validity.md` §4B established that the RCT-validated intervention is a **finite
programme**:

| Study | Structure | Adherence |
|---|---|---|
| Chan et al. 2018 (n=320, AJSM) | **2 weeks** of retraining → 12-month injury benefit | — |
| Field study (PMC11945614) | **8 sessions over 2–3 weeks**, outdoors, feedback faded | **100% session adherence, 100% completion, 85% retention at 1 month** |

**100% session adherence.** Not 70%, not 30%. In a field study, outdoors, with IMUs strapped
to both tibias and an app giving audio cues.

That is not a contradiction of the abandonment data — it is a different psychological
category. **People abandon habits. People complete courses.** Nobody says "I gave up on my
physiotherapy programme after two weeks" the way they say "I stopped wearing my Fitbit."
A finite thing with an endpoint and an outcome recruits completion motivation, not habit
motivation.

**This is the same property that broke the subscription model (K11), now paying us back.**
The customer graduating in three weeks was a business-model problem. It is a
retention *solution*. We resolved the business model by selling outright — which means
graduation costs us nothing and completion is the only behaviour we need.

**Restating the ask honestly:**
- ❌ *"Wear these pods on every run, forever."* — this loses to the 30% abandonment data
- ✅ *"Wear these for 8 runs over 3 weeks. Then you're done, and you keep the benefit."*

The second is a real product with published 100% completion. The first is the thing that
killed Athos, NURVV, Lumo and UA HealthBox.

---

## 3. The Form Factor Rule That Follows

The consultant's principle — watches and rings work because people already wear watches and
rings — generalises correctly, but not to "wrist only." The real rule is:

> **Attach to something the athlete already puts on. Minimise the number of separate
> attachment decisions, ideally to zero.**

Runners already put on **shoes**. That is an untapped zero-decision attachment point, and
the market proves it:

| Product | Attachment | Outcome |
|---|---|---|
| **Playermaker** | Cleat-mounted, 2 sensors | $249, **50+ D1 colleges, 100+ US clubs** |
| **Stryd** | Foot pod, clips to shoe | **Survived a decade** where every rival died |
| **Garmin RD Pod** | Clips to waistband/shoe | Long-lived (now absorbed into the watch) |

### But placement affects the measurement — and this matters

| Placement | Peak acceleration validity | Friction |
|---|---|---|
| **Distal tibia** | The reference standard. Vertical peak positive acceleration measured here is what's **associated with tibial stress fracture and vertical GRF loading rate** | Strap required — a separate decision |
| **Shoe heel-mounted** | **Poor** association with impact loading (AVLR) | Zero decisions |
| **Insole-embedded** | **Moderate-to-high** association with impact loading; *"easily and consistently fixated"* | Zero decisions |

Shoe-mounted IMUs read **higher** peak accelerations than the tibia because the ankle joint
attenuates impact before it reaches the shank — so the numbers are not interchangeable, and
heel mounting specifically fails to track loading.

**The insole is the only placement that is simultaneously low-friction and validated for
the variable our intervention actually uses.**

### The uncomfortable part
**ARION and NURVV both used insoles. NURVV went insolvent; ARION is 19 people after 11
years.** So the insole form factor is *necessary but nowhere near sufficient*.

Critically, NURVV did not die of friction — DC Rainmaker's post-mortem is about the app
contradicting its own metrics, incoherent training plans, and coaching that contradicted
running science. **They solved friction and still died, on execution.**

That is the honest read of this space: **form factor gets you the right to compete; the
analysis and coaching decide whether you win.**

---

## 4. The Second Point The Consultant Made — And It Is The Opening

> *"People like wearing Fitbits because they get an analysis of what they did in a very good
> structured way."*

The single most-cited reason for wearable abandonment is:
> *"Most wearables give you data, but they do not tell you what to do with it."*

**Our product is literally the answer to that complaint.** It does not report a number. It
issues an instruction — *"increase your cadence," "soften your landing," left leg, right
now — and then it stops when you no longer need it.*

That is the opposite of the failure mode. It also matches the ARION dropout data from the
other direction: the top control-group reason for quitting was *"I don't understand the
feedback."* Comprehensible, actionable output is not polish. **It is the product.**

---

## 5. What This Changes

| Decision | Before | After |
|---|---|---|
| Framing | A wearable you use ongoing | **A finite 8-session programme with an endpoint** |
| Retention target | Months of continued wear | **Completion of 8 sessions** (published precedent: 100%) |
| Attachment | Straps on tibias | **Insole or shoe-integrated** — zero additional decisions |
| Pod count | Ladder to 7 | **Fewest that works.** Every added pod is another decision, and decisions are the thing that kills us |
| Where the money goes | Sensor quality | **Setup time, auto-detection, and comprehensible coaching** |
| Market | Pro teams only (if perpetual wear) | **Amateurs are reachable** — for three weeks, which is all we need |

**The consultant's diagnosis is right and should be treated as the governing constraint. The
conclusion that it shrinks us to pro teams only holds if we insist on building a perpetual
wearable — which the evidence says we should not build anyway.**

---

## 6. Honest Risks That Remain

1. **We are converging on what ARION and NURVV built.** Insole/shoe-mounted running gait
   feedback. One is dead, one is small after eleven years. Any plan must state explicitly
   what we do differently, and "better app" is a weak answer until it is specific.
2. **The 100% adherence figure is n=7.** A feasibility study. Chan's n=320 is the strong
   evidence, but that was lab-delivered. **Field adherence at scale is unproven.**
3. **One programme per customer is a small business** unless there is a repeat trigger —
   new injury, new shoes, a new training block, a new season. Repeat rate is unmeasured and
   directly determines whether this is a company or a product.
4. **Insole means shoe compatibility, sizing, and wear-out** — a whole class of problems
   strap-mounted pods do not have. NURVV had documented fit complaints with certain shoes.

---

## Sources
- [Gartner abandonment data](https://www.bitdefender.com/en-us/blog/hotforsecurity/a-third-of-wearable-device-owners-quit-using-them-gartner-says) · [42% after six months](https://bigthink.com/technology-innovation/users-lose-interest-in-fitness-trackers-after-6-months/) · [Abandonment reasons study](https://www.sciencedirect.com/science/article/abs/pii/S0747563219303127) · [Adoption/abandonment stages](https://arxiv.org/pdf/1904.13226)
- [Sensor placement and distal tibial accelerations](https://journals.humankinetics.com/view/journals/jab/39/3/article-p199.xml) · [Footwear, speed and location validity](https://pmc.ncbi.nlm.nih.gov/articles/PMC8107270/) · [Peak impact accelerations by foot strike](https://pmc.ncbi.nlm.nih.gov/articles/PMC8931222/)
- [Field-based tibial accelerometer retraining, 100% adherence](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11945614/) · [Chan et al. 2018 RCT](https://journals.sagepub.com/doi/abs/10.1177/0363546517736277)
- [Playermaker amateur strategy](https://www.forbes.com/sites/robertkidd/2021/01/27/why-playermaker-is-taking-its-soccer-technology-to-amateur-players/) · [DC Rainmaker NURVV post-mortem](https://www.dcrainmaker.com/2021/02/nurvv-depth-review.html)
