# Market Teardown — Who Wins, Who Dies, and Why

**Researched 2026-08-23. This is a living document — see `market/WATCHLIST.md` for the
review cadence. Stale market intel is worse than none.**

Purpose: catalogue every relevant player, extract what they do right (duplicate it) and
what they did wrong (avoid it). Updated at every quarterly review.

---

## 0. THE PATTERN — Read This First

Sorting every body-worn player in this space by sensor count produces the single strongest
empirical regularity in the market:

| Company | Sensors on body | Status |
|---|---|---|
| WHOOP | **1** | $1B ARR, $10.1B valuation |
| Catapult | **1** (vest unit) | $140.7M revenue, 94% recurring, profitable |
| Stryd | **1** (foot pod) | Survived a decade in a niche where everyone else died |
| Garmin RD Pod | **1** | Alive — but being absorbed into the watch (see §4) |
| Playermaker | **2** (one per cleat) | $249, 50+ D1 colleges, 100+ US clubs |
| PlayerData | **1** | $12M Series A, US Soccer + MLS + FIFA officials |
| VALD | **0** — fixed equipment | **4,000+ elite teams, universities, defence depts** |
| — | — | — |
| ARION / ATO-Gear | 2 insoles + pods | Alive, **19 employees after 11 years** |
| NURVV | 2 insoles, **16 sensors** | **Insolvent, August 2023** (after $9M+ Series A) |
| Athos | Many, embedded in apparel | **Dead** (after $51.2M) |
| formsense | **20+** | Niche clinical, never adopted in team sport |
| Xsens DOT | Multi | Research tool only; never became a consumer product |
| Lumo Run | 1, but form-coaching | **Discontinued** |
| UA HealthBox | 3-device suite | **Killed by Under Armour, 2017** |
| dorsaVi | Multi | A$0.037/share, pivoting to robotics |

**Every commercial winner uses one sensor, or no wearable at all. Every multi-point
body-worn consumer product has died or stalled. The failure rate of that architecture is
effectively 100%.**

This is not proof it cannot work — `crux-analysis.md` argues the five barriers are
addressable, and that argument still stands. But it is a far stronger prior against
multi-pod than this project has been treating it, and it runs directly into the 5–7 pod
decision made on 2026-08-23 in `sensor-architecture.md`.

**The central unresolved trade of this company:**

> More pods buy data quality (joint angles, defensible asymmetry). More pods cost setup
> friction and retention — which is precisely what killed every company that tried it.

That trade must be made **explicitly and with evidence**, not inherited from a paper.
It is logged as K2 in `problems/VIABILITY.md`.

**And note what the biggest winner did:** VALD reaches 4,000+ elite organisations with
**fixed testing equipment and no wearable at all.** Periodic tests in the training room —
ForceDecks, NordBord, ForceFrame — not continuous monitoring in the field. Zero setup
friction per session because the athlete walks to the device rather than wearing it. If
the goal is "trustworthy biomechanical data on athletes," the market's most successful
answer is currently *not a wearable.*

---

## 1. THE GRAVEYARD — What Killed Them

### NURVV — the closest analogue to us, and it died
**16-sensor smart insoles + foot pods, running gait analysis, real-time form coaching.
$9M Series A (Feb 2020, Hiro Capital; some sources report up to $34M total).
Insolvency finalised August 2023.**

This is the most instructive failure in the file because it is nearly our product. The
[DC Rainmaker in-depth review](https://www.dcrainmaker.com/2021/02/nurvv-depth-review.html)
is effectively the post-mortem. His verdict: *"they've framed up one heck of a
house… far from finished."*

| What went wrong | Why it matters to us |
|---|---|
| **Coaching contradicted running science** — the app "continuously demanded lower cadence," the opposite of the evidence | Our coaching cues must be defensible or we lose credibility instantly |
| **App contradicted its own metrics** — post-run summaries disagreed with displayed numbers | Trust is destroyed once. Consistency is a correctness requirement, not polish |
| **Training plans were internally incoherent** — suggested an 8.13-mile run after telling the user not to exceed 6.3 that week | Any coaching layer needs the same rigour as the sensing layer |
| **$299 for metrics a $200+ watch already gives** | Our value must be what the watch *cannot* do — and must stay that way (§4) |
| **5-hour battery** | We are contemplating continuous high-rate streaming from 5–7 pods |
| **No TrainingPeaks, incomplete Garmin, no raw export** | Integration is table stakes in running, not a v2 feature |
| **Standalone GPS placed runners "50m or more, into the trees, water, or buildings"** | Do not ship a subsystem worse than the phone already in the runner's pocket |

And the deepest criticism, which strikes at the value proposition itself:

> *"If running pain-free, you may be best advised not to change your Pronation"*

**If a runner is not hurting, telling them to change their form may harm them.** That
narrows the addressable moment dramatically — and it applies to our real-time coaching
product too, which is currently our best-supported claim. Logged as K3.

### Athos — $51.2M, embedded EMG apparel
Already covered in `crux-analysis.md`. Wetsuit-like, non-breathable, $600/set, sensors
degraded with washing, returns unsaleable, pro-athletes-only market. **Lesson already
absorbed: removable pods, never embedded electronics.**

### Under Armour HealthBox — the strategic retreat
Three connected devices (tracker, HR strap, scale), launched Jan 2016, killed Nov 2017.
Died partly as collateral damage from a company-wide sales slump. **Under Armour's own
conclusion is the lesson: they exited hardware and put their software on other people's
hardware** (Samsung, Apple), aiming for "a very clean and simple experience."

An apparel giant with distribution, brand, and capital concluded that multi-device fitness
hardware was not worth owning. That is a strong signal about the category, not just about
UA.

### Lumo Run, Moov, dorsaVi
Lumo Run — running form coaching from a single waist pod — discontinued. dorsaVi, a listed
clinical-motion company, trades at A$0.037 and is pivoting to robotics. **Form-coaching as
a standalone product has a poor track record even at one sensor.**

### The base rate
[CB Insights](https://www.cbinsights.com/research/report/hardware-startups-failure-success/):
**97% of consumer hardware startups fail. Only 24% raise a second round.** Top four causes:
lack of consumer demand, high burn, loss of interest after crowdfunding, product strategy
mistakes. Separately, ~90% never reach market at all — *"the gap between a working
prototype and a manufacturable, certifiable, sellable product is far wider than anyone
expects."*

---

## 2. THE WINNERS — What To Duplicate

### Catapult — the incumbent is healthy, and that changes our positioning
FY26 (year ended 31 Mar 2026):

| Metric | Value |
|---|---|
| Revenue | **US$140.7M**, +19% cc |
| Core ACV | US$133.8M, **+28% YoY** (+18% organic) |
| Recurring revenue | $110M — **94% of total** |
| Management EBITDA | $24.7M, **+67%**; margin 13% → 18% |
| Free cash flow | $8.6M, nearly doubled; net cash >$7M |
| Acquisitions | Perch (gym monitoring), IMPECT (match data) |

**Correction to `competitors.md`.** It frames Catapult as vulnerable — post-session only,
ACWR-dependent, ripe for disruption. The financials say otherwise: profitable, accelerating,
94% recurring, and **actively consolidating the space through M&A.** They are a buyer, not
a sitting duck.

That has two implications. First, "Catapult won't build this because it cannibalises their
dashboard" is weaker than ever — they are buying adjacent capability aggressively and could
buy or build ours. Second, **acquisition is a realistic exit path** and should be modelled
as such rather than treated as failure.

**Duplicate:** 94% recurring revenue. Institutional buyers with real budget lines. Land-and-
expand cross-selling.

### WHOOP — hardware-as-subscription, one sensor, never removed
$1B+ ARR, 2.5M members, 103% growth, >80% retention, LTV:CAC ~4.5x, 60% international.
Already analysed in `buyer-and-liability.md` §3.

**Duplicate:** the subscription structure. **Note the thing we cannot duplicate:** WHOOP's
retention comes from a device you *never take off*. Our 5–7 pods must be donned before every
session and doffed after. That is a categorically worse retention posture, and it is the
mechanism behind K4.

### Stryd — how to survive a decade in a running-hardware niche
Most running power meter companies "never made it to market or failed within their first
year." Stryd is still here. Why:

- **Kickstarter pre-sold ~1,600 units in 12 days, 5× the goal.** Pre-sales funded working
  capital *before* committing to inventory — a direct answer to the HaaS "fish" problem in
  `buyer-and-liability.md` §3.
- **Community-calibrated.** They said openly: *"We can't do that ourselves. We need the
  running community to help us"* — using community data both to calibrate the model and to
  determine whether the metric was even valuable.
- **Committed to publishing anonymised data openly** to invite refinement.
- **Radical narrowness.** One pod, one metric, one sport.
- Garmin publicly had no plans to enter — a window they exploited (which is now closing, §4).

**Duplicate all of this.** Community-calibrated development plus open data is *exactly* the
open-source instrument strategy, and it is the only validated playbook in the file for
solving the "no dataset exists" problem from `predictive-validity.md` §9. Stryd is the
closest thing to a role model this project has.

### VALD — the biggest winner is not a wearable
4,000+ elite teams, universities and defence departments. Premier League, NBA, NFL, NCAA,
MLB, MLS, AFL. Product line is **fixed testing equipment**: ForceDecks (dual force plates),
NordBord (hamstring), ForceFrame (strength), HumanTrak, SmartSpeed.

They deliver exactly what our customers claim to want — asymmetry, fatigue status,
return-to-play, force generation — via **periodic tests with zero per-session setup burden.**

**The lesson is uncomfortable and important: the market's most successful answer to
"trustworthy biomechanical data" is not continuous wearable monitoring.** Any pitch we make
must explain why continuous field data beats a weekly ForceDecks test — and "we measure
during the actual activity" is a real answer, but it has to be argued, not assumed.

### Playermaker — proof the youth/amateur team market *is* reachable
$249 including a one-year app subscription, cleat-mounted, 50+ D1 colleges, 100+ US clubs.

**This partially corrects `buyer-and-liability.md` §1.** The claim there — that US school
budgets ($3–8K/yr total) cannot fund this — remains true for *institutional* purchase. But
Playermaker demonstrates a working alternative: **per-player, parent-funded purchase, sold
through the club rather than to the club.** The club is the distribution channel; the parent
is the payer.

That is a real GTM path we had written off. It is a consumer sale wearing a team uniform,
and it works.

### PlayerData — $12M Series A, integrated stack
US Soccer, several MLS clubs, officials at every FIFA men's World Cup match. Building a
combined stack: wearable + connected ball + AI video. **Direction of travel: sensors alone
are becoming a commodity; the integrated data picture is the product.**

### The industrial safety cluster — the funded, insurer-aligned adjacency
| Company | Founded | Funding |
|---|---|---|
| StrongArm Technologies | 2011 | **$50M** (largest ever in the category, Dec 2022) |
| Soter Analytics | 2015 | $12M (Apr 2022) |
| Modjoul | 2016 | $11.7M (Mar 2025) |

Kinetic's REFLEX gives real-time feedback the moment a high-risk motion occurs —
mechanically the same intervention as the ARION RCT. ROI evidence in
`buyer-and-liability.md` §1: 250% average, 52–64% injury reduction.

Sober note: these are $12–50M raises, not $500M ones. It is a real category with real
payers, not a rocket. But it has **a payer who eats the injury cost, no consumer retention
problem** (the employer mandates wear), and **no platform-absorption risk** — Apple is not
building for warehouse workers.

---

## 3. Duplicate / Avoid — The Working List

### Duplicate
1. **Subscription with high recurring share** — Catapult 94%, WHOOP. Non-negotiable.
2. **Community-calibrated development with open data** — Stryd. Also solves our dataset problem.
3. **Pre-sales before inventory commitment** — Stryd's Kickstarter funded working capital.
4. **Radical narrowness at launch** — one sport, one job, one metric that matters.
5. **Sell through clubs to parents** — Playermaker's $249 per-player model reaches the youth
   market that institutional budgets cannot.
6. **Insurer-aligned ROI framing** — StrongArm. The only place injury cost is a purchasable outcome.
7. **Integration from day one** — TrainingPeaks, Garmin Connect, Strava, raw export.
8. **Periodic-test simplicity where possible** — VALD. Ask what we genuinely need continuously.
9. **Model acquisition as a real exit** — Catapult is buying.

### Avoid
1. **Electronics embedded in fabric** — Athos.
2. **Coaching advice that contradicts sports science** — NURVV told runners to lower cadence.
3. **An app that contradicts its own metrics** — NURVV. Trust dies once.
4. **Metrics a $200 watch already provides** — NURVV at $299.
5. **Advising form changes to pain-free athletes** — may cause harm; narrows the market.
6. **Shipping a subsystem worse than the phone** — NURVV's GPS.
7. **Building on a feature the platform will absorb** — see §4.
8. **Skimping on integrations and raw export** — running users demand them.
9. **Multi-device consumer suites** — UA HealthBox; even a giant retreated.
10. **Assuming the incumbent is asleep** — Catapult is profitable and acquiring.

---

## 4. THE STRUCTURAL RISK: Platform Absorption

Garmin has rolled out **wrist-based running power** to Fenix 7 / Quatix 7 / Epix Gen 2.
Previously this required an accessory — the HRM-Pro strap or the Running Dynamics Pod.
Apple Watch Ultra ships running power and running dynamics natively.

**Garmin just deprecated its own accessory category.** That is the exact fate that awaits
any product whose value is a metric a watch can eventually estimate from the wrist.

The read-across is direct: cadence, ground contact time, vertical oscillation, stride length
and running power are all now wrist-derivable. Our defensible ground is only what a wrist
**cannot** see — **bilateral asymmetry and per-limb mechanics.** A wrist sensor is on one
arm; it is structurally blind to left/right limb differences.

**Strategic consequence:** every metric in the product should be classified as
*wrist-replicable* or *wrist-impossible*. Anything wrist-replicable is a feature on a
countdown timer and must not be load-bearing for the value proposition. This is a permanent
watch item, not a one-time analysis.

---

## 5. Corrections To Earlier Research

| File | Claim | Correction |
|---|---|---|
| `competitors.md` | Catapult vulnerable, real-time would cannibalise their dashboard | **Wrong.** $140.7M revenue, 18% EBITDA margin, 28% ACV growth, acquiring aggressively. Healthy consolidator. |
| `competitors.md` | Missing most of the field | Absent: NURVV, ARION/ATO-Gear, Stryd, VALD, Playermaker, Zone7, Kitman, Sparta, StrongArm, Kinetic, Soter, Modjoul, Lumo, UA HealthBox |
| `buyer-and-liability.md` §1 | HS/youth team market not viable | **Half-wrong.** Not viable as *institutional* purchase. Playermaker proves per-player parent-funded sales through clubs works at $249. |
| `market-sizing.md` | TAM/SAM/SOM from market reports | Top-down report numbers are near-useless here. The real constraint is the 97% hardware failure rate and the one-sensor pattern in §0. |
| `sensor-architecture.md` | 5–7 pods for trustworthy joint data | Still technically correct — but §0 shows it fights the strongest survival pattern in the market. Trade must be made explicitly. See VIABILITY K2. |

---

## Sources
- [DC Rainmaker — NURVV in-depth review](https://www.dcrainmaker.com/2021/02/nurvv-depth-review.html) · [NURVV Series A](https://tech.eu/2020/02/07/nurvv-series-a/) · [NURVV company profile](https://www.cbinsights.com/company/nurvv)
- [Under Armour on walking away from HealthBox](https://www.wareable.com/fitness-trackers/under-armour-interview-healthbox-wearables-4593) · [UA exits trackers](https://www.wareable.com/fitness-trackers/under-armout-out-fitness-trackers-1948)
- [CB Insights — hardware startup failure](https://www.cbinsights.com/research/report/hardware-startups-failure-success/) · [Why hardware startups fail](https://www.macrofab.com/blog/why-hardware-startups-fail)
- [Catapult FY26 results](https://ministryofsport.com/catapult-sports-ltd-record-usd141m-revenue-as-operating-profit-surges-67-per-cent/) · [Catapult H1](https://www.capitalbrief.com/briefing/catapult-first-half-revenue-lifts-17-to-104m-15649b4d-2792-4a1f-995c-0d48bf13f58d/)
- [Stryd origins and community approach](https://www.outsideonline.com/outdoor-gear/tools/science-behind-stryd-worlds-first-running-power-meter/) · [Running power rethink](https://www.outsideonline.com/health/training-performance/running-power-stryd-research-2020/)
- [VALD Performance](https://www.linkedin.com/company/vald-performance) · [ForceDecks](https://www.scienceforsport.com/forcedecks-dual-force-plate-system-by-vald/)
- [Playermaker amateur strategy](https://www.forbes.com/sites/robertkidd/2021/01/27/why-playermaker-is-taking-its-soccer-technology-to-amateur-players/) · [PlayerData $12M Series A](https://youthsportsbusinessreport.com/playerdata-closes-12m-series-a-as-connected-ball-and-camera-round-out-performance-stack/)
- [StrongArm $50M](https://www.iotworldtoday.com/health-care/strongarm-raises-50m-for-industrial-safety-wearables) · [Soter](https://pitchbook.com/profiles/company/169180-48) · [Modjoul](https://www.cbinsights.com/compare/modjoul-vs-strong-arm-technologies)
- [ATO-Gear / ARION profile](https://tracxn.com/d/companies/arion/__dwgbnT_nOZqnhXLiK7uNj3F_8VQzc5WanfYnMXqku5w)
- [Garmin wrist-based running power](https://www.advnture.com/news/garmin-is-taking-the-fight-to-apple-with-new-running-power-feature-and-its-about-time) · [Apple Watch running dynamics](https://the5krunner.com/2022/06/06/apple-watch-triathlon-running-power-running-dynamics-yes-really/)
