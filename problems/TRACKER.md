# InjuryShield — Master Problem Tracker

Every identified problem, question, and decision point.
Status: [ ] Open | [~] In Progress | [x] Resolved | [?] Needs Research | [!] Blocked | [K] KILLED (evidence says no)

**Last full revision 2026-08-24.** Ordered by what kills the project, not by category.
`VIABILITY.md` decides *whether* to build. This file tracks *what* to build.

**Read before touching P0–P4:** `research/predictive-validity.md`, `problems/VIABILITY.md`.

---

## THE CURRENT ANSWER, IN ONE PARAGRAPH

A **two-pod running gait-retraining programme**. Pods mount to the shoe (zero laundry
exposure). Phone does all inference. Eight sessions over 2–3 weeks with real-time audio
cues on peak tibial acceleration against the runner's own baseline, feedback faded across
the last four sessions. **Sold outright at ~$249**, hardware included, because the customer
graduates. Higher pod tiers (3/5/7) are opt-in for customers who want joint angles. No
injury-prediction claim, ever. Running only — it is the only domain where we have evidence.

---

## P0: EXISTENTIAL

### P0.1: Does the core claim survive evidence? — LARGELY RESOLVED
- [K] **P0.1.1** Baseline/screening biomechanics predict injury? **KILLED.** Bahr 2016: no screening test has ever had adequate test properties. Ruddy 2018: median AUC 0.58, between-year 0.52. 23 of 25 running meta-analyses null.
- [K] **P0.1.2** ACWR/workload management prevents injury? **KILLED.** Cluster RCT, 34 teams, 482 players, 10 months: no difference.
- [K] **P0.1.3** IMU impact/loading metrics reflect tissue load? **KILLED.** Matijevich 2019: impact peak r=−0.29, loading rate r=−0.20 vs peak tibial load; 76 of 80 subject correlations wrong direction.
- [x] **P0.1.4** Real-time gait feedback reduces injury? **YES.** ARION RCT weak (ITT null, as-treated HR 0.53).
- [x] **P0.1.5** **Gait retraining in ASYMPTOMATIC runners? YES — STRONGEST EVIDENCE IN PROJECT.** Chan 2018 AJSM: n=320, 2 weeks retraining, 12-month follow-up, injury **16% vs 38%, HR 0.38 (95% CI 0.25–0.59)**. Answers the NURVV objection directly.
- [x] **P0.1.6** Fatigue IMU-detectable? **YES as measurement.** GCT↑, stride↓, stiffness↓~6%, tibial accel↑.
- [x] **P0.1.7** Fatigue response is **highly individual** → all modeling must be within-subject deviation from own baseline. Also forced by measurement noise (P0.3.5).

### P0.2: The product definition
- [x] **P0.2.1** NOT an injury predictor. Product = **gait retraining programme with real-time feedback**.
- [ ] **P0.2.2** Rewrite public-facing framing to match. `CLAUDE.md` done; nothing public exists yet.
- [ ] **P0.2.3** Green/yellow/red = **deviation from own baseline**, never risk. Green is never a safety statement. Spec exact wording before any UI work.
- [ ] **P0.2.4** Define statistically what "significant deviation" means: baseline length, variance model, multiple-comparison correction across N metrics.
- [x] **P0.2.5** **The programme is finite: 8 sessions over 2–3 weeks, feedback faded across the last four.** Fading is the design, not a limitation — it produces superior retention vs constant feedback.

### P0.3: The data problem
- [ ] **P0.3.1** **No adequate labeled dataset exists publicly.** Median cohort in the ML injury-prediction scoping review: 122 participants; 39% used SMOTE. Data gap, not tech gap.
- [ ] **P0.3.2** Design v1 as the data-collection instrument. Requirements in `predictive-validity.md` §9.
- [ ] **P0.3.3** Injury labels must beat "pain ≥1 for 7 days" self-report. How do we get diagnosed labels from a consumer population?
- [ ] **P0.3.4** Previous injury is the strongest known risk factor and needs zero sensors. Any model must include it and may find it dominates every sensor feature.
- [ ] **P0.3.5** **Measurement noise vs threshold:** IMU knee RMSE ~6° against the literature's 10° asymmetry threshold. Noise is ~60% of signal. Resolve before writing any thresholding logic.
- [ ] **P0.3.6** **Log raw IMU always, never only derived metrics.** Today's running data is tomorrow's training set for a domain not yet chosen.

### P0.4: Kill criteria
- [ ] **P0.4.1** Set falsifiable stopping conditions with dates and a budget cap. See `VIABILITY.md` §4 gates.
- [x] **P0.4.2** **Largest remaining risks: K2 (30%, untested), K6 (97% consumer-hardware base rate, structural), K5 residual = repeat-purchase rate.** CAC is the biggest un-measured number.

---

## P1: EVIDENCE & VALIDATION

- [x] **P1.1** Paper 1 (3-sensor) is a measurement-fidelity result, not an injury result.
- [x] **P1.2** Paper 2 (92.3%) is **circular** — labels thresholded from the same signals. Stop citing it.
- [x] **P1.3** Commercial claims dodge false-positive rate. Zone7: 72.4% sensitivity, no specificity or flag rate published.
- [ ] **P1.4** **Standing rule: never report sensitivity without the flag rate.** Publish precision, specificity, % of athlete-days flagged.
- [ ] **P1.5** Baseline drift vs degradation signal — getting fitter and getting tired both change mechanics. Real confound.
- [ ] **P1.6** Cross-athlete generalization: design for per-athlete adaptation from day one.
- [ ] **P1.7** **Chan's cohort was NOVICE runners** — highest incidence, most form headroom. Generalization to trained runners is unproven. Needs replication or careful targeting.
- [ ] **P1.8** **Mechanism is unknown.** GRF impact metrics don't track tibial bone load (P0.1.3), yet impact-reduction feedback reduced injuries. Do not claim we know why it works.
- [ ] **P1.9** Field adherence at scale unproven — the 100% figure is n=7.
- [ ] **P1.10** 20 runner interviews + willingness-to-pay across the tier ladder.
- [ ] **P1.11** Talk to sports medicine doctors/physios: what claims would make them refuse to touch it.
- [ ] **P1.12** Community validation of the *honest* framing in r/running, r/AdvancedRunning.
- [ ] **P1.13** Founder 30-day wear test — see P8.

---

## P2: HARDWARE — Pod Design

### P2.1: Pod count — now a customer choice, not an architecture bet
- [x] **P2.1.1** **Ladder: Core 2 (both tibias — the RCT-validated config) / Plus 3 (+sacrum) / Pro 5 (+thighs → knee angle) / Full 7 (+feet → ankle angle).** App states what is missing at each tier.
- [x] **P2.1.2** Core is not a cut-down version — **it is the configuration the evidence validated.** Frame it that way.
- [x] **P2.1.3** Optimized placement data: ankle 3.90°, knee 6.35°, hip 5.93° RMSE. **Placement matters more than count** — worst placements hit 21.46° at the hip.
- [ ] **P2.1.4** Soft-tissue artifact on thigh/shank pods during running — measure before committing to Pro/Full tiers.
- [ ] **P2.1.5** Evaluate sparse-IMU deep learning (DIP/FDIP, 6 sensors, full-body pose) as the joint-angle estimator vs hand-rolled biomechanics.

### P2.2: Sensors
- [x] **P2.2.1** 6-DOF IMU (accel + gyro) minimum. Magnetometer optional.
- [x] **P2.2.2** 200 Hz distal / 100–150 Hz proximal. Joint angle needs less bandwidth than foot-strike detection.
- [ ] **P2.2.3** **Chip selection — buy samples and measure on OUR task.** LSM6DSV16X $2.88 (recommended: wearable-optimised, embedded ML core) vs ICM-45686 $6.70 (SlimeVR's top pick) vs BMI270 $1.79 (SlimeVR rates poor). **Their criterion is orientation drift over hours; ours is short-window dynamics — their ranking may not apply.**
- [x] **P2.2.4** **Peak tibial acceleration is the feedback variable** — measured directly at the tibia, not derived from the discredited GRF proxy.
- [K] **P2.2.5** EMG — dropped. The 92.3% result justifying it is circular, and electrodes reintroduce every Athos failure mode.
- [ ] **P2.2.6** Barometer for vertical oscillation? Temperature for fatigue? Probably not worth the BOM.

### P2.3: Battery & Power
- [x] **P2.3.1** **Counterintuitive spec: battery should be SHORT enough (~2–3 sessions) that charging forces pod removal.** Long battery life makes the laundry problem worse. Charging is the forcing function.
- [ ] **P2.3.2** Power budget: IMU at 200 Hz + continuous BLE streaming (higher duty cycle than burst sync) + flash writes.
- [ ] **P2.3.3** Battery chemistry, charging method (magnetic pogo likely).
- [x] **P2.3.4** **Charging dock is mandatory** — and doubles as a physical checklist (see P3.3.2).

### P2.4: Compute — hybrid, settled
- [K] **P2.4.1** Edge ML **removed from v1.** No use case needs sub-200 ms on-device: ACL rupture ~50 ms (can't pre-empt), gait cues need seconds, fatigue needs minutes. The 188 ms figure was inherited from a paper.
- [x] **P2.4.2** **Pod collects and streams; phone infers.** Phone logic ships in an app update; pod logic needs an OTA campaign. Iteration speed > elegance pre-PMF.
- [ ] **P2.4.3** MCU: nRF54L15 class (Cortex-M33 @128 MHz, 1.5 MB, sub-1 µA sleep, 22 nm). Bare chip $2.55 vs pre-certified module $8.11 — see P2.6.1.
- [ ] **P2.4.4** **Inter-pod time sync is now THE critical firmware problem** since all fusion happens downstream. Sub-ms alignment needed for asymmetry.
- [x] **P2.4.5** Flash 64–128 MB per pod. ~12 kB/s/pod at 200 Hz → ~173 MB per 4 hr raw, ~35–60 MB compressed.
- [ ] **P2.4.6** Ring buffer + flash spill for BLE dropouts. Non-negotiable — software failure is what actually kills adoption.

### P2.5: Communication
- [x] **P2.5.1** BLE capacity measured: 1–2 sensors @400 Hz, **3–6 @200 Hz**, 7–12 @100 Hz. Core/Plus fit comfortably; Full needs mixed rates or two links.
- [ ] **P2.5.2** Tune PHY (2M), DLE, ATT MTU (247), connection interval. Validate on a bench rig early.
- [ ] **P2.5.3** Team scale (125 devices) needs a hub — **deferred until a team customer exists. Do not build speculatively.**

### P2.6: Manufacturing cost — NEW, researched 2026-08-24
- [x] **P2.6.1** **Certification is the volume cliff, not components.** Pre-certified module route $3,000–10,000 all-in; bare chip / custom RF $15,000–50,000+. First-pass failure adds $5,000–30,000 and 4–12 weeks. **Use a module until ~5,000 pods; design the PCB for a drop-in swap.**
- [x] **P2.6.2** **Tooling is the second cliff.** 3D print below ~300–500 units; single-cavity mould $1,000–3,000; multi-cavity $5,000–15,000. Chinese quotes vary >2× — get several.
- [x] **P2.6.3** **Landed cost per pod: ~$49 @100, ~$29 @1,000, ~$16 @10,000.** Component-only: $32.38 / $19.96 / $11.20.
- [x] **P2.6.4** **Capital: 1,000 pods ≈ $55–80k total and is bootstrappable. 10,000 pods ≈ $170–200k.** Do not plan for 10k. Stryd pre-sold ~1,600 units at 5× goal before committing inventory.
- [ ] **P2.6.5** UN38.3 battery testing ($2,000–20,000) — scope once the cell is chosen.
- [ ] **P2.6.6** Enclosure must survive a 40°C wash cycle. **Do not fight the tumble dryer** — not winnable at our price.

---

## P3: ATTACHMENT — Rewritten 2026-08-24

### P3.1: Carrier decision — settled
- [x] **P3.1.1** **Removable pods. Never embedded.** Smart textile: 50–70% accuracy loss after 10–15 washes, total failure at 20–30, against a 50+ expectation. Athos died on this. Returns unsaleable.
- [x] **P3.1.2** **Low end (Core/Plus): shoe or lace mount.** Zero new garment, zero laundry exposure. Stryd (decade) and Playermaker ($249, 50+ D1 colleges) both prove it.
- [x] **P3.1.3** **High end (Pro/Full): straps.** Playermaker uses THREE straps per foot and sells fine. Complaints are about slippage on flat indoor shoes, not setup burden.
- [x] **P3.1.4** **No apparel line.** It is the only carrier washed after every session. WHOOP at $1B ARR has not solved it — their guidance is "always remove sensors before washing" and they ship a spare pod. WHOOP Body is a niche accessory, not a primary experience.
- [x] **P3.1.5** **There is no low-friction way to do 5–7 pods. Nobody has one.** Friction tolerance scales with the customer; so should the attachment system. Do not burn months looking for the design that makes 7 pods frictionless.

### P3.2: Open attachment problems
- [ ] **P3.2.1** **CRITICAL TENSION:** peak tibial acceleration wants the **distal tibia**; **shoe-heel mounting has POOR association with loading rate**; **insole-embedded has moderate-to-high association** and is "easily and consistently fixated." **The low-friction mount and the validated measurement site may not be the same place.** Resolve before committing the Core tier.
- [ ] **P3.2.2** Mount mechanism: magnetic vs snap-fit vs strap. Must not detach during sprinting/cutting. Review US Patent 9,872,525.
- [ ] **P3.2.3** Shoe compatibility, sizing and wear-out if insole route is chosen — NURVV had documented fit complaints with certain shoes.
- [ ] **P3.2.4** Pod protrusion at ankle against shoe collar.
- [ ] **P3.2.5** Mount-agnostic pod design — same pod, interchangeable mounts. Costs nothing, preserves every future option.

### P3.3: Friction mitigations to build regardless
- [ ] **P3.3.1** **Measure actual don/doff seconds at 2/3/5/7 pods.** This prices the ladder and finds the friction cliff.
- [ ] **P3.3.2** **Dock with a visible slot per pod** — empty slots are a physical checklist. AirPods pattern. Nearly free.
- [ ] **P3.3.3** **"Pods still in your shorts" alert** — pod motionless for hours and not on dock → notify. Software-only, cheap, **and nobody in this space appears to do it.**
- [ ] **P3.3.4** Ship a spare pod; price replacements low. WHOOP already concluded this.
- [x] **P3.3.5** **Attachment is a necessary condition, NOT the differentiator.** NURVV had attachment solved (insoles) and died on app and coaching quality. Get it good enough, then move on.

---

## P4: BUSINESS

### P4.1: Who pays — settled
- [x] **P4.1.1** **US high school teams cannot afford this as hardware.** $3,000–8,000 total annual athletic training budget; $96–926 per athlete; only 56% of HS employ a trainer at all, down 10 points since 2017.
- [x] **P4.1.2** NCAA money exists ($12,250/athlete/yr medical) but is held by risk management and requires a claims-reduction claim we cannot make. **Year 3+.**
- [x] **P4.1.3** **Individual runner is the v1 buyer** — only sports buyer who holds their own budget and needs no injury claim. 7.7 injuries/1000 hr; 37–56% annual incidence.
- [x] **P4.1.4** **Youth/club market IS reachable per-player, parent-funded, sold through the club** — Playermaker $249, 50+ D1 colleges, 100+ US clubs. Corrects the earlier write-off.
- [ ] **P4.1.5** **Industrial athlete / workers' comp remains a live pivot.** 250% avg ROI, 52–64% injury reduction, funded comparables (StrongArm $50M, Soter $12M, Modjoul $11.7M), employer-mandated wear (no retention problem), no platform-absorption risk. Scope properly.

### P4.2: Pricing & model — settled
- [x] **P4.2.1** **Outright sale.** $249 Core / $349 Plus / $549 Pro / $749 Full, hardware + programme + 12 months app.
- [x] **P4.2.2** **Perpetual subscription FAILS.** $90 COGS + $80 CAC ÷ $19/mo = **9 months to break even** against a 3-week intervention. Robust: even $40 COGS + $50 CAC needs 4.7 months.
- [x] **P4.2.3** **Graduation is the success story, not churn.** Selling outright means K11 costs nothing and kills K7 (working capital) entirely.
- [x] **P4.2.4** **The 3× multiple is not margin.** At $249 with $76 COGS, real contribution is $0–70 after CAC ($50–150), support, and amortised app/tooling/cert. **CAC is the whole game.**
- [ ] **P4.2.5** **Measure CAC.** Every model is more sensitive to it than to BOM. Above ~$150 the Core tier stops working.
- [ ] **P4.2.6** **Repeat-purchase rate is unmeasured and decides whether this is a company or a product.** One programme per customer is a small business unless there is a repeat trigger — new injury, new shoes, new training block, new season. **Top interview question.**
- [ ] **P4.2.7** Programme/rental kept as the best capital-efficiency alternative (17× hardware turn) if reverse logistics proves manageable.
- [ ] **P4.2.8** Cheap $8–10/mo post-programme monitoring tier as a secondary, never primary.

### P4.3: Claims & liability — elevated
- [x] **P4.3.1** **FDA general wellness (Jan 2026, broadened to include AI/ML wearables).** We exit it the moment we claim to prevent disease, interpret data for clinical decisions, or reference a condition for an individual.
- [x] **P4.3.2** **Liability is asymmetric:** "at risk" + no injury = churn. **"Safe/green" + injury = company-ending.** Green must never be an affirmative safety statement.
- [ ] **P4.3.3** Adopt the claim-language table in `buyer-and-liability.md` §2 as a binding style guide.
- [ ] **P4.3.4** No "cleared to play" state anywhere in the UI, ever. Enforce in design review.
- [ ] **P4.3.5** ToS disclaiming medical/diagnostic use at onboarding. Product liability insurance before any team sale. COPPA before any youth data.
- [ ] **P4.3.6** **Rename. "InjuryShield" is itself the claim we cannot make.** Before anything public.
- [x] **P4.3.7** **Clinic channel has the LOWEST regulatory exposure of all options** — Jan 2026 CDS guidance loosened rules and the exemption is specifically for clinician-facing software; patient-facing gets less latitude. VALD sells into US PT clinics with no reported friction. **The objection to clinics is commercial (10× CAC, B2B motion), not regulatory.**
- [ ] **P4.3.8** Freedom to operate: US 9,872,525, US 12,011,257.
- [ ] **P4.3.9** Open-source firmware and BLE protocol; keep baseline models and dataset proprietary.

### P4.4: Founder structure
- [x] **P4.4.1** **"Cannot monetize on H-1B" is out of date.** DHS rule effective 17 Jan 2025 — founders owning >50% can self-sponsor.
- [ ] **P4.4.2** Binding conditions: specialty-occupation framing (engineering role qualifies, "CEO" does not); **independent oversight required** — a cofounder in India does not satisfy it; 18-month initial approvals; lottery risk.
- [ ] **P4.4.3** Delaware C-corp + wholly-owned India subsidiary; transfer pricing at arm's length (cost-plus 10–15%).
- [ ] **P4.4.4** **Section 44ADA applies to an individual professional, not a company.** Different structures — pick deliberately.
- [ ] **P4.4.5** Immigration attorney before any filing. Budget $5–10k.

---

## P5: USER EXPERIENCE — where the product is actually won

- [x] **P5.0** **Top industry-wide abandonment reason: "most wearables give you data but do not tell you what to do with it."** Our product issues an instruction, not a number. That is the differentiation.
- [ ] **P5.1** Unboxing to first session <5 min.
- [ ] **P5.2** **Pod position auto-detection** — which pod is left vs right tibia. Must be automatic; manual assignment is a friction disaster.
- [x] **P5.3** Auto-calibration is possible (Paper 8, motion-driven SO(3), no poses). Key friction advantage and what makes straps tolerable.
- [ ] **P5.4** Calibration drift on sweaty skin mid-session — detect and compensate.
- [ ] **P5.5** Baseline collection: how many sessions? Ties to P0.2.4.
- [ ] **P5.6** **Feedback must be a coaching cue, not a warning.** "Try to increase your cadence" — actionable, specific, immediate. Different tone per leg.
- [ ] **P5.7** **Feedback comprehensibility is a correctness requirement.** ARION's top control-group dropout reason was "I don't understand the feedback"; NURVV's app contradicted its own metrics.
- [ ] **P5.8** Alert fatigue: minimum useful cue rate.
- [ ] **P5.9** Session summary shows change vs *your* baseline. Not 1,800 metrics.
- [ ] **P5.10** **Integrations are table stakes, not v2:** TrainingPeaks, Garmin Connect, Strava, raw CSV export. NURVV was criticised for lacking exactly these.
- [ ] **P5.11** Programme progress UI — 8 sessions, faded feedback, a visible endpoint and a completion moment.

---

## P6: SCOPE & EXPANSION — Rewritten 2026-08-24

- [x] **P6.1** **Running only for v1** — not for focus, but because **every defensible asset we have is running-specific.** Chan's HR 0.38, peak tibial acceleration, the 8-session protocol, the placement validation, and the wellness-safe claim language all go to zero simultaneously outside running.
- [x] **P6.2** **The universal snap-anywhere pod already exists.** Xsens DOT, ~$200/sensor, positioned verbatim as "a state-of-the-art **development platform**." Generic body pods are tools, not products — same as SlimeVR at $219.
- [x] **P6.3** **Layer transfer between domains:** hardware ~100%, app shell ~90%, attachment ~30%, **analysis ~10%, dataset 0%, evidence 0%.** Running builds ~40% of the platform.
- [x] **P6.4** **Expansion axis is LOCOMOTION, not "all movement."** The capability is *bilateral asymmetry and per-limb mechanics during locomotion, anywhere, with real-time intervention.*
- [ ] **P6.5** **Best v2: return-to-sport / ACL rehab.** Inter-limb asymmetry *is* the clinical metric; existing literature, payer, workflow and decision; reuses the gait analysis almost entirely.
- [ ] **P6.6** v3: team-sport locomotion (cutting, landing, deceleration).
- [K] **P6.7** **Gym / resistance form — AVOID.** Feedback works, but a **single wrist IMU** achieves 89–93% classification and <6% rep error "even for lower body exercises," so our asymmetry advantage evaporates. Also consolidated: Atlas Wearables acquired by Peloton, March 2021.
- [ ] **P6.8** Tennis: footwork partially applicable; stroke mechanics is a different product with zero evidence base. A 7-pod match capture is a research service, not a product.
- [ ] **P6.9** **Build for the platform, do not pitch the platform.** Mount-agnostic pod, analysis layer separated from app shell, raw logging always. Never claim the app analyses any movement.

---

## P7: REGULATORY — Rewritten 2026-09-01

### P7.0: Strategy shift — 510(k) is the plan
- [x] **P7.0.1** **"Stay wellness" is not viable for the clinic channel.** RTM billing (98977) requires FDA-cleared devices. Clinics won't bill with uncleared devices due to audit risk.
- [~] **P7.0.2** **File 510(k) using dorsaVi ViMove as predicate.**
  - **Consultant outreach status (2026-09-01):** Gmail drafts created for 5 firms: Emergo by UL, NAMSA, i3C Global (enquiry@i3cglobal.com), Medical Device Academy (lindsey@medicaldeviceacademy.com), SafeLink Consulting (info@safelinkconsulting.com). Key question: 510(k) vs exempt under 21 CFR 882.5050 HCC. Same device class (IMU gait analysis, Class II). Small business fee: $6,517. Total cost: $30–90K. Timeline: 9–15 months.
- [ ] **P7.0.3** **Phased approach:** launch consumer wellness (current plan) → build clinician data view → file 510(k) when clinic demand materializes → clearance unlocks RTM billing and hospital/health system sales.
- [ ] **P7.0.4** **IEC 62304 software lifecycle compliance.** Required for 510(k). Must be in place before submission.
- [ ] **P7.0.5** **Biocompatibility testing (ISO 10993)** — skin contact testing for wearable pods.
- [ ] **P7.0.6** **EMC/EMI testing (IEC 60601-1-2)** — electromagnetic compatibility.

### P7.1: HIPAA
- [ ] **P7.1.1** **HIPAA compliance required if patient data flows through our servers.** Minimum viable year-1 cost: $5–20K.
- [ ] **P7.1.2** BAAs with every cloud vendor (AWS/GCP) and every clinic customer.
- [ ] **P7.1.3** Encryption at rest and in transit, role-based access, audit logging.

### P7.2: Liability
- [ ] **P7.2.1** Product liability insurance before any clinical sale. $5–15K/yr.
- [ ] **P7.2.2** "Information only — clinician makes all decisions" framing in all materials.
- [ ] **P7.2.3** Indemnification clauses in clinic contracts — mutual indemnification standard.

### P7.3: League/sport-specific (deferred)
- [x] **P7.3.1** Phase 1 training/practice market — no approval needed anywhere.
- [ ] **P7.3.2** FIFA EPTS certification — deferred to year 3.
- [ ] **P7.3.3** NBA, NCAA — deferred.
- [ ] **P7.3.4** IEEE P3716 — deferred.
- [ ] **P7.3.5** Privacy: GDPR, COPPA, state laws. Athlete owns their data.

---

## P8A: CLINIC CHANNEL (MODEL D) — NEW 2026-09-01

### P8A.0: Why clinic channel
- [x] **P8A.0.1** **Direct-to-consumer value prop is weak.** Self-guided biofeedback for $249 — founder wouldn't buy it. Prevention is invisible. "You didn't get injured" has zero emotional payoff.
- [x] **P8A.0.2** **Professional oversight solves retention.** Prescribed device use: 80%+ adherence vs 50–70% self-directed. Physio IS the forcing function the consumer channel lacks.
- [x] **P8A.0.3** **Insurance makes price invisible.** Patient doesn't pay $249 — absorbed into PT visits + RTM billing.
- [x] **P8A.0.4** **Expansion beyond running is natural in clinic.** Physio sees all MSK conditions — knee rehab, hip replacement, low back pain, ACL. Same hardware, different protocols.

### P8A.1: RTM billing — the revenue engine
- [x] **P8A.1.1** **RTM code 98977 (MSK device supply): ~$52/month per patient.** + 98980 (treatment management, 20 min): ~$51/month. Monthly total: ~$120–150/patient.
- [x] **P8A.1.2** **2026 CMS expansion helps us:** new code 98985 for 2–15 days/month (our 8-session programme fits), new code 98979 for 10–19 min management increments.
- [ ] **P8A.1.3** **RTM requires FDA-cleared device.** Clinics won't bill with uncleared devices → 510(k) is the gateway.
- [ ] **P8A.1.4** **Calculate clinic ROI pitch:** device subscription cost vs RTM revenue per enrolled patient. Target: device pays for itself in 2–3 months.
- [ ] **P8A.1.5** **PTs can bill RTM under their own NPI for MSK (98977).** PTAs/OTAs contribute monitoring time under general supervision. Verify state-by-state scope.

### P8A.2: dorsaVi lessons — problems we MUST solve differently
Sourced from `research/clinic-channel-landscape.md`. dorsaVi does exactly what we'd do (IMU → clinics, 510(k) cleared) and is at AU$1.13M/yr after 19 years.

- [ ] **P8A.2.1** **Sales cycle is brutal (1–18 months).** dorsaVi couldn't scale selling one clinic at a time. **Our mitigation:** RTM revenue pitch ("this device generates $31K/yr in new billing") is a stronger hook than dorsaVi had. Target small independent practices (1–3 month cycle), not hospital systems (6–18 months).
- [ ] **P8A.2.2** **Clinicians don't change workflow.** >90% of PTs rely on visual observation despite 30–40% better outcomes with tech. **Our mitigation:** fit INTO existing workflow. Don't replace the assessment — add data to it. Must integrate with common EMR/EHR systems.
- [ ] **P8A.2.3** **Camera alternatives eliminate sensor setup.** DARI Motion, Kinetisense = zero per-patient hardware. **Our mitigation:** cameras can't follow athletes outdoors. Our advantage is CONTINUOUS, OUTDOOR, REAL-WORLD data across thousands of strides — not a 10-step clinic walkthrough. Must articulate this clearly.
- [ ] **P8A.2.4** **dorsaVi had no RTM billing.** RTM codes didn't exist until 2022, expanded 2026. This is our single biggest structural advantage vs dorsaVi's era. **Validate that RTM billing actually drives purchase decisions with 5 clinic owner interviews.**
- [ ] **P8A.2.5** **Revenue per clinic is small.** Even at $5K/yr subscription, need thousands of clinics. **Our mitigation:** RTM billing means revenue scales with PATIENTS, not just clinic count. 1 clinic with 20 RTM patients = $31K/yr revenue for the clinic, of which we capture $3–6K. Still need volume.
- [ ] **P8A.2.6** **Product must be dead simple.** dorsaVi's declining product investment hurt them. Our sensor must be invisible to the runner (<10g, shoe-mounted, unnoticeable during sprinting). Training time for clinician: max 1–2 hours. App must just work.

### P8A.3: Sensor invisibility requirement
- [ ] **P8A.3.1** **Pod must be unnoticeable during running, sprinting, cutting.** Target: <10g, no protrusion past shoe collar, no movement restriction, no change to natural gait.
- [ ] **P8A.3.2** **Waterproof/sweatproof.** IP67 minimum.
- [ ] **P8A.3.3** **Test with real runners:** can they tell the pod is there after 1 mile? After 5 miles? During sprints? Subjective comfort survey + biomechanical comparison (gait with vs without pod).

### P8A.4: Partnership/acquisition scenarios
- [ ] **P8A.4.1** **Hinge Health / Sword Health as potential partners or acquirers.** Their sensors are indoor-only (knee straps for squats/stretches). Running gait is a gap. But: they may build it themselves, they're moving toward camera-based tracking, and Hinge is in IPO process.
- [ ] **P8A.4.2** **Don't build to be acquired.** Build the best running gait product → become a natural target. 510(k) clearance + proprietary dataset + proven clinical outcomes = acquisition value.
- [ ] **P8A.4.3** **Hinge's user feedback on their sensors:** mixed. Accuracy complaints, app usability issues, sensor placement friction. Instructional videos removed in 2026. They're not great at hardware UX — possible opening.

---

## P9: NEXT EXPERIMENTS — Was P8, renumbered 2026-09-01

Ordered by information gained per dollar. **Nothing here requires building hardware.**

- [~] **P8.1** **Buy test hardware, ~$255–345.**
  - ~~mbientlab MetaMotionS~~ — **OUT OF STOCK.**
  - **Xsens DOT** — $132/unit, 10g, IP68, 120 Hz, 9-axis. Quote requested from Movella 2026-09-01. Cannot buy directly online. Alternatives: Unbound XR, or buy the 5-sensor set from buy.xsens.com.
  - ~$50–80 of IMU chip samples (LSM6DSV16X / ICM-45686 / BMI270) — settles P2.2.3 on our own task.
  - ~$30–50 mounting supplies (clips, adhesive pads, velcro, digital scale).
- [ ] **P8.2** **30-day founder wear test.** Primary metric: **days actually worn out of 30**, unprompted. Secondary: don/doff seconds at 2/3/5/7 pods (P3.3.1). Also captures first within-subject baseline data.
- [ ] **P8.3** **Resolve P3.2.1** — tibia vs shoe vs insole placement for peak tibial acceleration. This decides whether the low-friction Core tier can deliver the validated measurement.
- [~] **P8.4** **Clinic owner interviews (5 minimum) + runner interviews (20).** Clinic interviews: LinkedIn requests sent (exhausted free tier), Gmail drafts ready for Golden Hills PT + 6 more clinics, phone numbers collected. Runner interviews: not started.
  - **Clinic outreach status:** LinkedIn connection requests sent. Email drafts ready. Phone: Golden Hills (408) 274-0888, Silver Creek (408) 325-6251. Script: `validation/clinic-interview-script.md`.

### P8.4a: Community validation — staged sequence
Full operational guide: `validation/POSTING-PLAYBOOK.md`. Content ready in
`scripts/posting/posts/`. **Nothing posted yet.**

- [ ] **P8.4a.1** **Build standing in the target subs FIRST — ~1 week, before any post.**
      Several subs auto-remove posts from accounts with no prior comment history, and
      u/pranavhj1998 has none in any running sub. Target 5–10 genuine comments per sub.
      **These must be posted by the founder, not automated** — see `validation/comment-drafts.md`
      for research-grounded starting points that require no fabricated personal experience.
- [ ] **P8.4a.2** Post 1 → r/AdvancedRunning: "Has anyone actually changed their form and had it stick?" (trigger + retention)
- [ ] **P8.4a.3** Post 2 → r/running: "What do you blame, and what do you change?" (attribution + substitutes). **+1 week after post 1.**
- [ ] **P8.4a.4** Post 3 → r/C25K: "Did anyone tell you *how* to run?" (**settles O7 — novice vs experienced**). **+1 week.**
- [ ] **P8.4a.5** Post 4 → r/AdvancedRunning: "Gait analysis — worth paying for?" (pricing + repeat purchase). **Post LAST, with disclosure in the post.** Only after 2 of the above land well.
- [ ] **P8.4a.6** X thread (8 tweets, research findings). **Stagger 2–3 days from any Reddit post.**
- [ ] **P8.4a.7** Verify r/C25K is the right novice sub — rules and activity unchecked. Alternatives: r/beginnerrunning, r/running's daily thread.
- [ ] **P8.4a.8** Reply to every comment within 24 hours. Unanswered OPs read as drive-by marketing.
- [ ] **P8.4a.9** Log outcomes to `makingDollarsInIndia/engagement/log.md` and update `research/demand-side.md` §5 + the O2/O7/O8/O9 rows in `DECISIONS.md`.
- [ ] **P8.4a.10** Timing: **8–11 PM IST** (US morning). Never during Indian business hours. Max 1 post/platform/day.
- [ ] **P8.5** Measure CAC once there is something concrete to show (P4.2.5).
- [ ] **P8.6** Quarterly market review — `market/WATCHLIST.md`. **First due 2026-11-23.**

---

## Research Index

| Question | File |
|---|---|
| Does any of this predict injury? | `research/predictive-validity.md` |
| Should we build at all? Kill register, gates | `problems/VIABILITY.md` |
| Who wins, who died, what to copy/avoid | `research/market-teardown.md` |
| What can only we do (vs wrist/camera/force plate) | `research/capability-envelope.md` |
| Setup friction and retention | `research/friction-and-retention.md` |
| Embedded vs removable vs apparel vs straps | `research/attachment-strategy.md` |
| Running only? Universal pod vision? | `research/scope-and-expansion.md` |
| BOM, volume tiers, certification, test hardware | `research/bom-and-pricing.md` |
| Revenue models, why subscription fails | `research/unit-economics.md` |
| Who pays, claim language, FDA, H-1B | `research/buyer-and-liability.md` |
| Pod count, placement, compute split, BLE | `research/archive/sensor-architecture.md` |
| Why multi-point sensors haven't taken off | `research/crux-analysis.md` |
| Clinic channel competitive landscape | `research/clinic-channel-landscape.md` |
| Clinic channel business model viability | `research/clinic-channel-viability.md` |
| Clinic regulatory: FDA, HIPAA, 510(k), liability | `research/clinic-regulatory-landscape.md` |
| "Outright sale + finite programme" precedents | `research/programme-model-precedents.md` |
| Standing market watch | `market/WATCHLIST.md` → `market/LOG.md` |

---

## Changelog
- **2026-09-01 (session 2)** — Outreach phase: LinkedIn requests sent (exhausted free tier), 5 regulatory consultant Gmail drafts created, clinic outreach drafts created (Golden Hills + 6 more), Xsens DOT quote requested (can't buy directly), hardware buy list updated. P7.0.2 and P8.1 marked in-progress. P8.4 updated for clinic interviews.
- **2026-09-01** — Major strategic shift: clinic channel (Model D) elevated to primary go-to-market. Added P8A (clinic channel problems, dorsaVi lessons, RTM billing, sensor invisibility, partnership scenarios). Rewrote P7 (regulatory) — 510(k) is now the plan, not a fallback; added HIPAA and liability subsections. Archived regulations.md and fitbit-air-reference.md; merged programme-model-precedents. Added 4 new research files to index. P8 renumbered to P9.
- **2026-08-24** — Full revision after five research rounds. P3 (attachment) and P6 (scope) rewritten. Added P2.6 (manufacturing cost) and P8 (next experiments). Pod count became a customer-facing ladder. Pricing settled on outright sale. Running-only scope with locomotion as the expansion axis; gym form killed. Attachment settled: removable, shoe-mounted low end, no apparel line. Added P3.2.1 as the critical open tension (validated measurement site vs low-friction mount) and P4.2.6 (repeat-purchase rate) as the open commercial unknown.
- **2026-08-23** — Restructured by kill criteria. Added P0. Killed prediction, ACWR, GRF-tissue-load, EMG, edge ML. Revised sensor count and compute architecture. Retired $35/pod pricing.
