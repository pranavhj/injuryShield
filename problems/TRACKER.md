# InjuryShield — Master Problem Tracker

Every identified problem, question, and decision point. Each can be exploded into its own deep-dive.
Status: [ ] Open | [~] In Progress | [x] Resolved | [?] Needs Research | [!] Blocked | [K] KILLED (evidence says no)

**Reordered 2026-08-23 by what kills the project, not by category.** P0 comes first and
gates everything below it. Working on P1 hardware before P0 is answered is wasted effort.

**Required reading before touching P0–P4:** `research/predictive-validity.md`.

---

## P0: EXISTENTIAL — Does The Core Claim Survive Contact With Evidence?

The original tracker had 80+ items and none of them was "is the central premise true?"
It was researched on 2026-08-23. Much of it is not.

### P0.1: Can biomechanical markers predict injury?
- [K] **P0.1.1** Can baseline/screening biomechanics identify who will get injured? **KILLED.** Bahr 2016: no screening test for sports injury has ever had adequate test properties. Ruddy 2018: median AUC 0.58, between-year 0.52 (coin flip). 23 of 25 meta-analyses on running biomechanics found no difference between prospectively injured and uninjured runners. **Do not build a predictor.**
- [K] **P0.1.2** Does ACWR/workload management prevent injury? **KILLED.** Cluster RCT, 34 teams, 482 players, 10 months, ACWR-guided vs normal training: no difference in injury rates. The entire Catapult/STATSports category premise failed its RCT.
- [K] **P0.1.3** Do IMU impact/loading metrics reflect actual tissue load? **KILLED.** Matijevich 2019: impact peak r=−0.29, loading rate r=−0.20 vs peak tibial load. 76 of 80 subject correlations showed higher GRF metrics did NOT mean higher tibial force. The sign may be inverted. Named IMeasureU and RunScribe as making this error.
- [x] **P0.1.4** Does real-time gait feedback reduce injury? **WEAK YES.** ARION RCT, 220 runners: ITT null (HR 1.11), as-treated HR 0.53 (p=.03). Suggestive not confirmatory — but the one green shoot, and the mechanism is *coaching*, not prediction.
- [x] **P0.1.5** What actually prevents injury? **Universal prevention programs.** Nordic hamstring ~50% reduction (8,459 athletes); FIFA 11+ ~39% reduction. Given to everyone, no screening. Only tier with robust evidence.
- [x] **P0.1.6** Is fatigue detectable from IMU? **YES, as measurement.** GCT↑, stride length↓, vertical stiffness↓~6%, tibial accel↑, loading rate↑ all reliably change and are IMU-visible. The unproven step is fatigue → injury with actionable lead time.
- [ ] **P0.1.7** Fatigue response is *highly individual* (some runners ↑vGRF, cadence shows no consistent group-level change; trained runners degrade less). Group-trained models will underperform individuals. **All modeling must be within-subject, deviation-from-own-baseline.** Design consequence, not yet implemented.

### P0.2: The reframe — what do we actually build?
- [x] **P0.2.1** Product is NOT an injury predictor. **Descending order of evidential support:** (1) real-time movement coaching, (2) fatigue/degradation detection reported descriptively, (3) compliance & dosing for interventions that work, (4) performance baselining.
- [ ] **P0.2.2** Rewrite `CLAUDE.md` product vision and the project's own name/framing to match. "InjuryShield" itself implies a claim we cannot support — see P4.4.6.
- [ ] **P0.2.3** Green/yellow/red must measure **deviation from the athlete's own baseline**, never risk. Green = "mechanics consistent with your baseline," never "safe." Spec the exact wording of all three states before any UI work.
- [ ] **P0.2.4** Define statistically what "significant deviation from baseline" means. How many sessions to establish baseline? What variance model? What multiple-comparison correction across N metrics?

### P0.3: The data problem — the actual moat and actual bottleneck
- [ ] **P0.3.1** **No adequate labeled dataset exists publicly.** Median cohort in the ML injury-prediction scoping review: 122 participants. 39% used SMOTE to fake class balance. This is why nobody has solved it — not a tech gap, a data gap.
- [ ] **P0.3.2** Design the data collection instrument as the *primary* v1 deliverable. Requirements in `predictive-validity.md` §9: within-subject longitudinal, thousands of athlete-seasons, time-stamped diagnosed injuries, context features (previous injury, sleep, surface, footwear age, training history).
- [ ] **P0.3.3** Injury labels must be better than "pain ≥1 for 7 days" self-report (the ARION RCT's weakest point). How do we get diagnosed, tissue-level labels from a consumer population? Partnership with physio clinics?
- [ ] **P0.3.4** Previous injury is by far the strongest known risk factor and needs zero sensors. Any model must include it — and we must be honest that it may dominate every sensor-derived feature.
- [ ] **P0.3.5** Measurement noise vs signal: IMU knee angle RMSE ~6°, against Paper 2's ">10° asymmetry" threshold. Noise is ~60% of the threshold. Either widen thresholds or work purely in within-subject change. **Resolve before any thresholding logic is written.**

### P0.4: Kill criteria — when do we stop?
- [ ] **P0.4.1** Define falsifiable stopping conditions. Candidates: (a) cannot detect within-subject mechanical change above measurement noise in the founder's own 30-day run data; (b) <20% of beta users still wearing pods at 60 days; (c) cannot recruit 50 runners willing to log injuries for 6 months.
- [ ] **P0.4.2** Set a date and a budget cap for the v1 data-collection instrument before starting.

---

## P1: EVIDENCE & VALIDATION (was P8 — promoted)

- [x] **P1.1** Paper 1 (3-sensor optimal) is a *measurement fidelity* result, not an injury result. Valid as hardware blueprint only.
- [x] **P1.2** Paper 2 (92.3% accuracy) is **circular** — labels were generated by thresholding the same signals the model reads. Not an injury-prediction result. Also n=50, also EMG-dependent. **Stop citing it as validation.**
- [x] **P1.3** Real-world false-positive rate: no paper addresses it. Commercial claims dodge it — Zone7 reports 72.4% sensitivity but no specificity, precision, or flag rate. With ~3 of ~25 players flagged daily over a 1–7 day window, background flag rate is plausibly 30–50%, making the lift modest.
- [ ] **P1.4** **Rule for us: never report sensitivity without the flag rate.** Publish precision, specificity, and % of athlete-days flagged. Make this a stated principle.
- [ ] **P1.5** Long-term accuracy: does a within-subject baseline model stay valid over weeks/months as fitness changes? Baseline drift vs degradation signal is a real confound — getting fitter and getting tired both change mechanics.
- [ ] **P1.6** Cross-athlete generalization: given P0.1.7 (individual fatigue responses), does a model trained on 50 athletes work for athlete 51? Probably not — design for per-athlete adaptation from day 1.
- [ ] **P1.7** Community validation: post the *honest* framing (movement quality monitoring, not injury prediction) in r/running, r/AdvancedRunning, r/sportsanalytics. Gauge interest in what we can actually deliver.
- [ ] **P1.8** Talk to sports medicine doctors and physios about what metrics they actually want — and what claims would make them refuse to touch the product.
- [ ] **P1.9** Talk to college athletic directors about budget reality (see P4.1.1 — the numbers suggest they cannot buy).
- [ ] **P1.10** Founder self-experiment: 30 days of running with prototype pods. Primary question is not comfort — it is *can we detect a real within-subject mechanical change above noise*. This is the fastest path to P0.4.1(a).

---

## P2: HARDWARE — Pod Design

### P2.1: Sensor Count & Placement (REVISED — see `research/sensor-architecture.md`)
- [x] **P2.1.1** ~~3-pod system~~ **REVISED: optimize for trustworthy joint data, then cost.** 3 pods (lumbar + ankles) gives spatiotemporal + asymmetry but **no joint angles** — no thigh or shank sensor.
- [x] **P2.1.2** **Design target: 5 pods (lumbar + 2 shanks + 2 feet/ankles). Architecture scales to 7 (+2 thighs) for full lower-limb kinematics. 3-pod becomes the entry tier.**
- [x] **P2.1.3** Optimized 4-sensor unilateral set (sacrum + lower anterior thigh + lower lateral shank + heel) achieves ankle 3.90°, knee 6.35°, hip 5.93° RMSE. Bilateral doubles limb sensors → 7.
- [x] **P2.1.4** **Placement matters more than count.** Best knee pairing: mid-lateral-shank + lower-anterior-thigh (bias 0.08°). Worst in same study: 9.31° knee, 21.46° hip.
- [ ] **P2.1.5** Soft tissue artifact on thigh and shank pods during running — worse than sacrum. Measure before committing to 7 pods.
- [ ] **P2.1.6** Sparse-IMU deep learning (DIP/FDIP, 6 sensors, full-body SMPL pose) — evaluate as the joint-angle estimator rather than hand-rolled biomechanics.

### P2.2: Sensor Selection
- [x] **P2.2.1** 6-DOF IMU (3-axis accel + 3-axis gyro) minimum. Magnetometer optional.
- [x] **P2.2.2** 200 Hz for running/event detection. **Revised: proximal pods (thigh/lumbar) can run 100–150 Hz** — joint angle needs less bandwidth than foot-strike event detection, and this buys BLE headroom.
- [ ] **P2.2.3** IMU chip selection — BMI270? ICM-42688? LSM6DSO? Compare accuracy, power, size, cost, availability. **Do after P0, not before.**
- [ ] **P2.2.4** Barometric pressure sensor for vertical oscillation accuracy?
- [K] **P2.2.5** ~~EMG for 92.3% accuracy~~ **The 92.3% figure is circular (P1.2). EMG is not justified by it.** Skin-contact electrodes reintroduce every Athos failure mode. Drop unless a real prospective result justifies it.
- [ ] **P2.2.6** Temperature sensor? (skin temp correlates with fatigue)
- [ ] **P2.2.7** Tibial acceleration is the one loading variable measured *directly* rather than derived from a discredited GRF proxy (P0.1.3). Shank pod placement should be optimized for it specifically.

### P2.3: Battery & Power
- [ ] **P2.3.1** Target 4–6 hours (full session). Xsens DOT: 8 hr from 70 mAh at 120 Hz. **Power budget is easier now — no on-pod ML (P2.4.1).**
- [ ] **P2.3.2** Battery chemistry — LiPo vs coin cell. Weight vs capacity.
- [ ] **P2.3.3** Charging — magnetic pogo pins likely. USB-C per pod is friction at 5–7 pods.
- [ ] **P2.3.4** **Charging dock is now mandatory, not optional.** 5–7 pods × individual cables is a non-starter. Dock doubles as the auto-sync trigger.
- [ ] **P2.3.5** Fast charge? Fitbit Air: 5 min = 1 day.
- [ ] **P2.3.6** Power budget: IMU at 200 Hz + continuous BLE streaming (higher duty cycle than burst-sync) + flash writes. Streaming costs more radio power than the old edge-inference design — recompute.

### P2.4: MCU / Processing (REVISED — hybrid architecture)
- [K] **P2.4.1** ~~Edge ML required, <200 KB model, <200 ms inference~~ **REMOVED FROM V1.** No use case needs sub-200 ms on-device: ACL rupture takes ~50 ms (cannot be pre-empted), gait cues need seconds, fatigue needs minutes. The 188 ms figure was inherited from Paper 2, not derived from a user need.
- [x] **P2.4.2** **Pod = high-rate collection + reliable transport. Phone = all inference.** Rationale beyond compute: every algorithm on the pod needs an OTA campaign to fix; every algorithm on the phone ships in an app update. Iteration speed > architectural elegance pre-PMF.
- [ ] **P2.4.3** MCU selection — nRF52840 class. Now over-spec'd for the reduced role, but BLE 2M PHY + DLE maturity and cheap headroom justify it. Compare nRF5340.
- [K] **P2.4.4** ~~TinyML framework selection~~ Not needed for v1.
- [x] **P2.4.5** ~~Does each pod run its own model, or stream to a brain pod?~~ **All pods stream to the phone.**
- [ ] **P2.4.6** Inter-pod time sync — synchronized timestamps across 5–7 pods is now *the* critical firmware problem, since all fusion happens downstream. Sub-millisecond alignment needed for asymmetry work.
- [x] **P2.4.7** On-pod flash: 5 pods × 6 ch × 2 B × 200 Hz = 12 kB/s/pod → ~173 MB per 4-hr session raw, ~35–60 MB compressed. **Spec 64–128 MB QSPI per pod. Log raw always — the data is the asset.**
- [ ] **P2.4.8** Ring buffer + flash spill for BLE dropouts. Non-negotiable — dropouts will happen and the ARION RCT shows software failure is what actually kills adoption.

### P2.5: Communication
- [x] **P2.5.1** BLE capacity measured: 1–2 sensors @ 400 Hz, **3–6 @ 200 Hz**, 7–12 @ 100 Hz. **5 pods @ 200 Hz fits. 7 pods needs mixed rates or two links.**
- [ ] **P2.5.2** Tune PHY mode (2M), Data Length Extension, ATT MTU (247), connection interval. Validate real throughput early with a bench rig.
- [ ] **P2.5.3** Pod-to-coach display: how does a coach receive anything during practice? Deferred — individual v1 does not need it.
- [x] **P2.5.4** Team scale: 25 athletes × 5 pods = **125 concurrent BLE devices. No phone handles this.** Options: per-athlete phone (zero new hardware), dedicated multi-radio hub, or store-and-forward at the dock. **Decide when a team customer exists. Do not build the hub speculatively.**

### P2.6: Form Factor & Weight
- [ ] **P2.6.1** Target <15 g/pod. Fitbit Air ~10 g, Xsens DOT 11.2 g, KINEXON 15 g.
- [ ] **P2.6.2** Pod dimensions — must not restrict joint movement. Shank/thigh pods are new placements with new constraints.
- [ ] **P2.6.3** Enclosure — IP68, sweat-resistant, skin-safe. **Sealed pods are also what makes subscription refurbishment viable (P5.1.6).**
- [ ] **P2.6.4** No sharp edges or hard protrusions (competition requirement).
- [ ] **P2.6.5** Fitbit Air teardown — what makes it that small, can we match the BOM?

---

## P3: ATTACHMENT & COMFORT

### P3.1: Snap-on Pod
- [ ] **P3.1.1** Snap/magnetic mechanism — secure during sprinting, cutting, jumping; must not detach on impact.
- [ ] **P3.1.2** Magnetic vs snap-fit vs velcro. Research US Patent 9,872,525. WHOOP uses velcro.
- [ ] **P3.1.3** Attachment points now 5–7: lumbar, both shanks, both ankles/feet, optionally both thighs.
- [ ] **P3.1.4** Strap attachment for users who don't want branded apparel.
- [ ] **P3.1.5** Shoe clip option for foot pods.

### P3.2: Apparel
- [x] **P3.2.1** Electronics NOT embedded in fabric — removable pods. Apparel is normal washable compression fabric. Key advantage over Athos/formsense.
- [ ] **P3.2.2** Garment set: compression shorts (lumbar + thigh docks), calf sleeves (shank docks), ankle sleeves. **More pods = more garments = more friction. This directly fights Barrier 1.**
- [ ] **P3.2.3** Pod dock design in fabric — sensor-to-skin proximity without embedding electronics.
- [ ] **P3.2.4** Sizing S–XXL minimum; compression must be snug or sensors move.
- [ ] **P3.2.5** Partner with an existing sportswear manufacturer vs manufacture ourselves.
- [ ] **P3.2.6** Cost: apparel with docks vs straps alone.

### P3.3: Comfort & Compliance — THE #1 ADOPTION RISK
- [ ] **P3.3.1** **Setup friction gets worse with 5–7 pods.** Barrier 1 in `crux-analysis.md` was the #1 killer at 3 pods. Quantify: measure actual don/doff time with 5 pods. If >90 s, reconsider the count.
- [ ] **P3.3.2** ARION RCT dropout data is the best available evidence on why people quit: **47% of dropouts from app malfunctions**, 33% "feedback not useful," 18.2% equipment durability, 13.6% discomfort. Only ~60% of completers wanted to continue. **Software reliability outranks biomechanics as an adoption risk.**
- [ ] **P3.3.3** "I don't understand the feedback" was the top control-group dropout reason. Feedback comprehensibility is a first-class design problem (Barrier 4).
- [ ] **P3.3.4** Will athletes wear shank + thigh pods? Olympic athletes refused multi-point sensors (GSSI, Tokyo 2020: 2 athletes total).
- [ ] **P3.3.5** Founder 30-day wear test — comfort, failures, and the P1.10 signal-detection question together.
- [ ] **P3.3.6** Pod protrusion at ankle against shoe collar; shank pod under sock.

---

## P4: BUSINESS — Who Pays (REVISED — see `research/buyer-and-liability.md`)

### P4.1: Budget reality
- [x] **P4.1.1** **US high school teams cannot afford this as hardware.** Typical HS athletic training supplies budget: **$3,000–8,000 total per year**; per-athlete range **$96–926**. Only 56% of HS employ a trainer at all, down 10 points since 2017. 125 pods for a 25-athlete team does not fit any version of that budget.
- [x] **P4.1.2** **NCAA money exists but is not held by our user.** $12,250/athlete/yr medical coverage; $90K catastrophic deductible; 30% of D1 schools provide no athlete health insurance. Reaching that budget requires a claims-reduction claim we cannot make (P0.1). **Year 3+ at best.**
- [x] **P4.1.3** **Individual runner is the correct v1 buyer** — the only sports buyer who holds their own budget and needs no injury-prediction claim. Base rate: **7.7 injuries/1000 hr (CI 6.9–8.7), 37–56% annual incidence.** Half of runners get hurt each year.
- [x] **P4.1.4** **The insurance-funded model is proven — in workplace safety, not sports.** Wearable safety systems: **250% average ROI, up to 52% injury reduction**; best documented deployment **64% injury reduction / 58% claims-cost reduction in year 1**. Kinetic REFLEX does real-time posture feedback — mechanically the same product as the ARION intervention that worked. Insurers actively participate.
- [ ] **P4.1.5** **Track "industrial athlete" as a genuine pivot option, not a footnote.** Same 5–7 pod hardware, same real-time coaching software, a payer who directly eats the injury cost, and a hard dollar denominator (workers' comp claims) that sports lacks. Scope this properly.
- [ ] **P4.1.6** Who signs at a HS: athletic director, not coach, not trainer. Booster/parent-funded purchase is a consumer sale in team clothing — model it that way.

### P4.2: Pricing & Model (REVISED — subscription, not hardware sale)
- [x] **P4.2.1** **Hardware-as-subscription confirmed as the model.** WHOOP: $1B+ ARR, 2.5M members, 103% YoY growth, **>80% retention** in core demographic, **LTV:CAC ~4.5x**, $10.1B valuation. Gives hardware away, charges for data.
- [x] **P4.2.2** **This is what rescues the 5–7 pod decision.** Under subscription, BOM is a payback-period input, not a retail-price ceiling. 5 pods @ ~$30 BOM = $150/subscriber, paying back in 8–10 months at $15–20/mo — inside an 18-month retention curve.
- [x] **P4.2.3** ~~$35/pod, $105 3-pod kit~~ **Retired.** It was a constraint imposed by hardware-sale economics that no longer apply.
- [ ] **P4.2.4** Individual pricing: **$15–25/month, annual commitment.** Anchored below WHOOP ($30/mo) — narrower job.
- [ ] **P4.2.5** Team pricing must fit inside a $3–8K budget: **$500–1,500/team/year all-in, hardware included.** Nothing else fits P4.1.1.
- [ ] **P4.2.6** **The "fish" problem:** HaaS inverts the cash curve — full COGS up front, recovered over months, and the faster you grow the deeper the hole. Model BOM payback on *fully-loaded* COGS (assembly, test, packaging, shipping, support, returns), not BOM alone.
- [ ] **P4.2.7** Churn before payback is a total loss of hardware cost — far more damaging than SaaS churn. **No month-to-month at launch.** Annual commitment or hardware deposit until payback math is proven.
- [ ] **P4.2.8** Returned pods must be refurbishable. Sealed IP68 pods are good here; skin-contact garments (Athos) were not.
- [ ] **P4.2.9** Inventory/venture debt financing needed to scale. Equity-only funding of COGS is expensive.

### P4.3: Manufacturing
- [ ] **P4.3.1** PCB design and assembly — Shenzhen for production, local PCBA for prototypes.
- [ ] **P4.3.2** Enclosure: injection molding at volume, 3D print for prototypes.
- [ ] **P4.3.3** Apparel: partner with existing compression brand or manufacture in India.
- [ ] **P4.3.4** MOQ vs unit cost curve — now a payback-period question, not a retail-price question.
- [ ] **P4.3.5** Supply chain: IMU + MCU availability.

### P4.4: IP, Legal & Claims (ELEVATED — this is now a strategic fork)
- [x] **P4.4.1** **FDA line (Jan 2026 finalized guidance):** wellness category was *broadened* to include non-invasive wearables with AI/ML. We exit wellness the moment we claim to prevent disease, interpret data for clinical decision-making, or reference a condition for an individual user.
- [x] **P4.4.2** **The liability asymmetry:** "at risk" + no injury = churn. **"Safe/green" + injury = company-ending.** The dangerous output is the *reassuring* one. Green must never be an affirmative safety statement.
- [ ] **P4.4.3** **Adopt the claim-language table in `buyer-and-liability.md` §2 as a binding style guide.** Say: "GCT is 8% above your 30-day baseline." Never say: "at risk of injury," "safe to continue," "cleared to play."
- [ ] **P4.4.4** No "cleared to play" state anywhere in the UI, ever. Enforce in design review.
- [ ] **P4.4.5** Terms of service disclaiming medical/diagnostic use, shown at onboarding. Product liability insurance before any team sale. COPPA before any youth data.
- [ ] **P4.4.6** **The name "InjuryShield" itself makes a claim we cannot support** and is exactly the framing that creates P4.4.2 liability. Rename before any public launch. Candidates should describe measurement, not protection.
- [ ] **P4.4.7** Freedom to operate: do existing patents block snap-on pod + phone-side inference? Review US 9,872,525 and US 12,011,257.
- [ ] **P4.4.8** Open-source strategy: firmware and BLE protocol open (builds trust, attracts contributors); the within-subject baseline models and the dataset are the moat.
- [ ] **P4.4.9** Data privacy: GDPR, COPPA, state laws. Athlete owns their data — say so from day 1.

### P4.5: Founder Structure (REVISED — constraint is weaker than assumed)
- [x] **P4.5.1** **The "cannot monetize on H-1B" assumption is out of date.** DHS rule effective **17 Jan 2025** eliminated the employer-employee relationship requirement. **Founders owning >50% (up to 100%) can self-sponsor H-1B.**
- [ ] **P4.5.2** Conditions that still bind: specialty-occupation requirement (an embedded/ML engineering role qualifies; "CEO" does not); **independent oversight required** — a board or advisory structure with real hire/fire authority, which a cofounder in India does not satisfy alone; **initial approval limited to 18 months** then an 18-month extension; cap-subject unless exempt.
- [ ] **P4.5.3** Structure: Delaware C-corp + wholly-owned India subsidiary is cleaner than two independent companies with a services agreement, and is what investors expect.
- [ ] **P4.5.4** **Transfer pricing is not optional** — the India entity must be paid at arm's length (typically cost-plus 10–15% for R&D/services).
- [ ] **P4.5.5** **Section 44ADA in `ecosystem-business-model.md` applies to an individual professional, not a company.** If the cofounder is a salaried employee of an Indian subsidiary it does not apply; if an independent contractor billing the US entity, it may. Different structures — pick deliberately.
- [ ] **P4.5.6** **Immigration attorney before any filing.** Budget $5–10K. Nothing researched here is legal advice.

---

## P5: USER EXPERIENCE

### P5.1: Setup & Onboarding
- [ ] **P5.1.1** Unboxing to first session <5 min — harder with 5–7 pods.
- [ ] **P5.1.2** Pod pairing: NFC tap? BLE auto-detect? QR?
- [x] **P5.1.3** Auto-calibration is possible (Paper 8, motion-driven SO(3) alignment, no poses). Still our key friction advantage.
- [ ] **P5.1.4** Position auto-detection: which pod is lumbar vs left shank vs right ankle? Must be automatic at 5–7 pods — manual assignment is a friction disaster.
- [ ] **P5.1.5** Baseline collection: how many sessions to establish a personal baseline? Ties to P0.2.4.
- [ ] **P5.1.6** Calibration drift on sweaty skin mid-session — detect and compensate.
- [ ] **P5.1.7** Multi-athlete team onboarding: 125 devices. Deferred with the hub decision.

### P5.2: During Session
- [ ] **P5.2.1** What does the athlete actually feel/hear? Haptic pattern vocabulary.
- [ ] **P5.2.2** **Feedback must be a coaching cue, not a warning.** The ARION mechanism that worked was "try to increase your cadence" — actionable, specific, immediate. Not "you are at risk."
- [ ] **P5.2.3** Alert fatigue: too many cues = ignored. What is the minimum useful cue rate?
- [ ] **P5.2.4** Coach view for teams — deferred.
- [ ] **P5.2.5** Battery/connection status surfaced before it matters.

### P5.3: Post-Session
- [ ] **P5.3.1** Auto-sync when pods hit the dock.
- [ ] **P5.3.2** Session summary: what changed vs *your* baseline. Not 1,800 metrics (Barrier 4).
- [ ] **P5.3.3** Shareable report for a physio or coach.
- [ ] **P5.3.4** Export: CSV, API, Strava/TrainingPeaks/Garmin Connect.

---

## P6: SPORT-SPECIFIC

- [x] **P6.1** Hardware stays sport-agnostic. Sport-specific models, not sport-specific pods.
- [ ] **P6.2** Running is v1 and the only sport with adequate literature. **Everything below is speculative until P0 is answered for running.**
- [ ] **P6.3** Basketball: landing mechanics, cumulative jump load.
- [ ] **P6.4** Soccer/football: cutting deceleration, hamstring load.
- [ ] **P6.5** Baseball: forearm pod instead of lower-limb set — different hardware config after all.
- [ ] **P6.6** Contact sports: pod durability under collision.
- [ ] **P6.7** Do optimal placements differ per sport?

---

## P7: REGULATORY PATHWAY

- [x] **P7.1** Phase 1 training/practice market — no approval needed anywhere. Start here.
- [x] **P7.2** FDA: stay inside general wellness by claim discipline (P4.4.1–P4.4.3). A clinical claim is a 510(k)-class project — budget it as such if ever pursued.
- [ ] **P7.3** FIFA EPTS certification — requirements, timeline, cost.
- [ ] **P7.4** NBA approved wearables list — application process.
- [ ] **P7.5** MLB device approval — 6–8 month process.
- [ ] **P7.6** NCAA 2026 guidelines — be early-compliant.
- [ ] **P7.7** IEEE P3716 — get involved for credibility.
- [ ] **P7.8** Data privacy policy template: GDPR, COPPA, state laws.

---

## Changelog
- **2026-08-23** — Restructured by kill criteria. Added P0 (existential). Killed P0.1.1–P0.1.3 (prediction, ACWR, GRF-tissue-load), P2.2.5 (EMG), P2.4.1/P2.4.4 (edge ML). Revised sensor count 3 → 5 core / 7 full / 3 entry. Revised compute to hybrid (pod collects, phone infers). Retired $35/pod hardware pricing for subscription. Added P4.1.4–P4.1.5 (industrial athlete / insurance market). Added P4.5 (founder structure — H-1B constraint materially weaker than assumed). Elevated claims/liability to strategic fork. Backing research: `predictive-validity.md`, `sensor-architecture.md`, `buyer-and-liability.md`.
