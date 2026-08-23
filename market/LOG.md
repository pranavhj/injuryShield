# Market Watch — Log

Append-only. One dated entry per review. Newest at top.
Process and checklist: `WATCHLIST.md`.

---

## 2026-08-23b — Camera / optical tracking threat assessment

Triggered by the question: can camera systems track every athlete on a large field?

**Answer: yes, at elite level — but only inside instrumented venues.**
- Hawk-Eye **SkeleTRACK**: dedicated 4K arrays, ball + **29 points per player, in real time**,
  marketed for performance analysis and injury prevention
- Powers FIFA semi-automated offside; FIFA/Hawk-Eye joint Football Technology Centre
- NFL adopted Hawk-Eye virtual measurement from the 2025 season; NBA uses Hawk-Eye
- Competitors: TRACAB (EA), Second Spectrum
- **Wrexham AFC took SkeleTRACK for home matches, Sept 2025** — moving below the top tier

**The constraint is economic, not technical.** Goal-line technology alone ran
**£125,000–250,000 per ground**; SkeleTRACK adds a dedicated array on top. Quoted:
*"for 99% of the football world… you cannot buy them for your club. They are league-level
infrastructure, installed in stadiums, funded centrally."*

**Accuracy caveat:** markerless error is 3–15° sagittal but **3–57° transverse**.
Transverse rotation is where ACL mechanism lives. Plus occlusion, identity swaps in crowds,
and degradation under sunlight and shadow (pose models are mostly trained indoors).

**Conclusion:** cameras own the instrumented venue on match day. Nothing owns the training
ground, the road, or the amateur field — and cameras structurally cannot, since cost is
per-site and the athlete must be inside the capture volume. Full analysis in
`research/capability-envelope.md`.

**New watch item (amber trigger):** SkeleTRACK moving further down-market (Wrexham is the
signal), or any portable/temporary camera rig that removes the per-venue install cost.

---

## 2026-08-23 — Baseline (first full teardown)

**Scope:** full landscape sweep, graveyard analysis, platform threat assessment.
Full write-up in `research/market-teardown.md`.

**Headline finding.** Every commercial winner in body-worn sports sensing uses **one
sensor or no wearable at all**. Every multi-point body-worn consumer product has died or
stalled. The largest winner (VALD, 4,000+ elite organisations) sells **fixed testing
equipment, not wearables.**

**Alive and healthy**
- Catapult — US$140.7M revenue, +19% cc; ACV $133.8M +28%; EBITDA $24.7M +67%; margin
  13%→18%; **94% recurring**; acquiring (Perch, IMPECT). *Correction: `competitors.md`
  framed them as vulnerable. They are a profitable consolidator.*
- WHOOP — $1B+ ARR, 2.5M members, >80% retention, LTV:CAC 4.5x
- VALD — 4,000+ elite teams/universities/defence, fixed equipment
- Stryd — survived a decade; Kickstarter 5× goal in 12 days; community-calibrated; open data
- Playermaker — $249 incl. 1yr app, 50+ D1 colleges, 100+ US clubs, **parent-funded via clubs**
- PlayerData — $12M Series A; US Soccer, MLS, FIFA officials
- Industrial: StrongArm $50M · Soter $12M · Modjoul $11.7M (Mar 2025)

**Alive but stalled**
- ARION / ATO-Gear — **19 employees, founded 2015, Series A 2023.** Our closest honest
  comparable and the source of the only positive RCT. Eleven years to 19 people.

**Dead**
- NURVV — 16-sensor running gait insoles. **Insolvency finalised August 2023** after a $9M
  Series A. Nearly our product. Post-mortem is DC Rainmaker's review: coaching contradicted
  running science, app contradicted its own metrics, incoherent training plans, $299 for
  metrics a $200 watch gives, 5hr battery, no integrations, GPS worse than a phone.
- Athos — $51.2M, embedded EMG apparel
- UA HealthBox — killed 2017; Under Armour exited hardware and put software on other
  people's devices
- Lumo Run — discontinued; dorsaVi — A$0.037, pivoting to robotics

**Platform threat — active**
Garmin shipped **wrist-based running power** to Fenix 7 / Quatix 7 / Epix Gen 2,
deprecating its own Running Dynamics Pod. Apple Watch Ultra has running dynamics natively.
Cadence, GCT, vertical oscillation, stride length are all wrist-derivable now.
**Remaining defensible ground: bilateral asymmetry / per-limb mechanics** — geometrically
invisible to a single wrist device.

**Base rate.** CB Insights: 97% of consumer hardware startups fail; 24% raise a second
round; ~90% never reach market.

**Actions taken**
- Created `problems/VIABILITY.md` — kill register K1–K10, cheapest-first test ordering,
  decision gates, unknown-unknowns practices
- K2 (multi-pod architecture) opened at ~55% — directly tensions the 5–7 pod decision made
  earlier the same day in `sensor-architecture.md`
- K3 (value unproven even as coaching) opened at ~45%; K4 (platform absorption) ~40%
- Corrections logged against `competitors.md`, `buyer-and-liability.md` §1, `market-sizing.md`

**Next review due: 2026-11-23.**
