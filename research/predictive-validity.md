# Predictive Validity — Does Any of This Actually Predict Injury?

**Status: researched 2026-08-23. This file supersedes optimistic readings of `academic-papers.md`.**

This is the load-bearing question for the whole company. The short answer from the
evidence base: **injury *prediction* does not work and probably will not. Real-time
movement *coaching* has weak but genuine RCT support. Those are different products.**

Read this before making any claim in marketing, to a customer, or to an investor.

---

## 1. The Four Claims — Very Different Evidence

The product concept quietly bundles four claims. They have wildly different support.

| # | Claim | Evidence | Verdict |
|---|---|---|---|
| 1 | Baseline biomechanics identify who will get injured | 23 of 25 meta-analyses null | **FAILS** |
| 2 | Workload ratios (ACWR) guide training to prevent injury | Cluster RCT, 482 players, null | **FAILS** |
| 3 | Real-time gait feedback reduces injury rate | 1 RCT, ITT null / as-treated HR 0.53 | **WEAK POSITIVE** |
| 4 | Prevention programs given to *everyone* reduce injury | Multiple meta-analyses, 39–50% reduction | **STRONG** |

The uncomfortable synthesis: **what works is the intervention, not the identification.**
Screening to decide *who* gets the intervention has never been shown to beat giving the
intervention to everybody. That is Bahr's third step and nobody has cleared it.

---

## 2. Claim 1 — Prediction From Biomechanics: FAILS

### Bahr 2016 — the framework everyone ignores
"Why screening tests to predict injury do not work—and probably never will…: a critical
review." *BJSM* 50(13):776-80. ~489 citations.

Validating a screening test requires three steps:
1. Prospective association between marker and injury risk
2. Adequate test properties (sensitivity/specificity) in a relevant population
3. An RCT showing that intervening on the *screened-positive* group beats intervening on everyone

**"There is currently no example of a screening test for sports injuries with adequate
test properties."** Step 3 has never been passed by anything, for any injury, ever.

Many markers show a statistically significant association with injury. Bahr's point is
that statistical association is nearly worthless for individual prediction because of base
rates — an OR of 2–3 still produces mostly false positives when the event is rare.

### Ruddy et al. 2018 — the cleanest negative result
"Predictive Modeling of Hamstring Strain Injuries in Elite Australian Footballers."
*MSSE*. Used the three best-established HSI risk factors (age, previous HSI, eccentric
hamstring strength) with multiple ML methods.

- 2013 models: median **AUC 0.58** (range 0.26–0.91)
- 2015 models: median **AUC 0.57** (range 0.24–0.92)
- Between-year (i.e. actually predicting the future): median **AUC 0.52** — coin flip

**Conclusion: "risk factor data cannot be used to identify athletes at an increased risk
of hamstring strain injury with any consistency."** The huge AUC range is the tell — some
splits hit 0.91 by luck. Any paper reporting a single high AUC without showing the range
should be assumed to be reporting a lucky split.

### Biomechanics → running injury: 23 of 25 meta-analyses null
"Biomechanical and Musculoskeletal Measurements as Risk Factors for Running-Related Injury
in Non-elite Runners" (*Sports Medicine – Open* 2022) and Vannatta et al. (*Human Movement
Science* 2020).

- **23 of 25 meta-analyses detected no significant difference** between prospectively
  injured and non-injured runners on the biomechanical variable tested
- Where significance was found, effect sizes were "trivial to small"
- Findings "largely dependent on the population and injuries being studied" — i.e. they
  do not transfer between cohorts
- Best surviving signals, and only in *female recreational* runners: increased hip
  adduction, reduced peak rearfoot eversion (moderate evidence)

A 24-week prospective cohort (n=98, 41 injured, 8.1/1000h) tested plantar pressure, hip
strength in 4 planes, knee extensor strength, core stability, ankle DF ROM, hip IR,
limb length, Q-angle, shank-forefoot alignment. **Exactly one variable reached
significance**: hip external rotator strength, OR 0.84 (0.71–0.99), p=0.04. That is a
protective strength factor — not measurable by an IMU at all.

**Implication for us:** the "measure asymmetry → flag injury risk" pathway is the single
most-tested idea in this field and it keeps failing.

### The tissue-load pathway is also broken
Matijevich et al., *PLOS ONE* 2019 — "Ground reaction force metrics are not strongly
correlated with tibial bone load when running across speeds and slopes."

| GRF metric vs peak tibial load | r |
|---|---|
| Impact peak | **−0.29 ± 0.37** |
| Loading rate | **−0.20 ± 0.35** |
| Active peak | 0.72 ± 0.42 (inconsistent) |
| GRF impulse vs tibial impulse | −0.11 ± 0.41 |

**76 of 80 subject-specific correlations showed higher GRF metrics did NOT mean higher
tibial force.** Impact peak and loading rate point the *wrong way*.

The authors name names: devices from IMeasureU, RunScribe and others assume lower impact =
lower injury risk, and that assumption is unvalidated. **"The current interpretation of
these values in wearable devices may be leading to the wrong conclusions about the
accumulation of microdamage."**

This kills the intuitive story "accelerometer measures impact → impact damages bone →
alert on high impact." It is not just unproven, the sign may be inverted.

---

## 3. Claim 2 — ACWR / Workload Management: FAILS

The definitive test: a **cluster RCT, 34 elite youth football teams, 482 players aged
13–19, 10 months.** Intervention coaches planned training using ACWR principles; control
coaches trained normally.

**Result: no difference whatsoever in injury rates.**

This is the actual experiment for the entire load-management product category that
Catapult and STATSports sell into. It came back null. Combined with the mathematical
coupling critique already in `crux-analysis.md`, ACWR is done.

Broader: "Direct evidence that wearable-guided interventions reduce injuries remains
scarce… associations between wearable-derived metrics and injuries are inconsistent and do
not support universal risk thresholds."

**Implication:** our positioning that "ACWR is broken, we're the scientific alternative" is
correct about ACWR but must not imply we have cleared a bar nobody has cleared.

---

## 4. Claim 3 — Real-Time Feedback: WEAK POSITIVE (the one green shoot)

**This is the most important paper for us and it is not in `academic-papers.md`.**

"The Effect of Wearable-Based Real-Time Feedback on Running Injuries and Running
Performance: A Randomized Controlled Trial." PMC10905988.

- **220 recreational runners**, randomized, 6–12 months follow-up (median 4.8 months)
- Device: ARION (ATO-Gear) pressure-sensitive insoles, 150 Hz spatiotemporal + IMU
  (30–50 Hz) + GPS
- Both groups saw distance/duration/speed. **Intervention group additionally got
  real-time coaching cues** — cadence, footstrike index, relative speed — with
  individualized target zones ("try to increase your cadence")
- Algorithm inferred *relative* load on foot/ankle/lower-leg vs knee/upper-leg from
  literature correlations, then cued the runner to shift load off the most-stressed segment

**Results:**

| Analysis | All injuries | >7-day injuries |
|---|---|---|
| Intention-to-treat | HR 1.11 (p=.70) — **null** | HR 1.90 (p=.10) — null |
| As-treated | **HR 0.53 (p=.03)** | HR 0.70 (p=.22) |
| Per-protocol | HR 0.67 (p=.30) | HR 1.29 (p=.62) |

Also: first-injury severity −0.43 (p=.042) favouring feedback. No effect on performance
(3.07% PB improvement, p=.26) and none on motivation.

**How to read this honestly.** The pre-registered primary analysis (ITT) was null. The
positive result comes from the as-treated analysis, which was necessitated because 33% of
participants ended up in the wrong group due to app setting confusion. As-treated analysis
breaks randomization and is hypothesis-generating, not confirmatory. This is *suggestive*,
not established.

**But note the mechanism.** The device did not predict who would be injured. It coached
everyone toward better mechanics in real time. That is Claim 4 (universal intervention)
delivered continuously, not Claim 1 (screening).

**Also note the operational lessons, which are brutal and directly about our product:**
- **47% of dropouts were caused by app malfunctions**
- Control-group dropout reason: *"I don't understand the feedback"*
- Intervention-group dropout reasons: feedback not useful (33%), discomfort (13.6%),
  equipment durability (18.2%)
- Only ~60% of completers wanted to keep using it

Software reliability and feedback comprehensibility killed more of this study than the
biomechanics did. That maps exactly onto Barrier 1 and Barrier 4 in `crux-analysis.md`.

---

## 5. Claim 4 — Universal Prevention Programs: STRONG

| Program | Effect | Evidence |
|---|---|---|
| Nordic hamstring exercise | ~**50%** reduction in hamstring injury (8,459 athletes) | Meta-analysis; one reappraisal calls it inconclusive on methods grounds |
| FIFA 11+ | risk ratio 0.612 ≈ **39%** reduction in lower-extremity injury | Meta-analysis |

Everyone does the program. Nobody is screened. This is the only tier of the pyramid with
robust evidence, and it requires no sensors at all.

**Strategic consequence:** the highest-value thing a sensor can do is not *predict* — it
is to make a proven intervention happen correctly and consistently. Dosing, technique
quality, and adherence to a program that already works.

---

## 6. What About the Commercial Claims? (Zone7)

Zone7 — 50+ pro clubs, $8M Series A, acquired by Svexa Feb 2024. Their public validation
study is the best commercial evidence available, so it is worth dissecting.

**Their claim:** 11 pro football teams, 2019–2021, 423 injuries. Flagged elevated risk
1–7 days before **306 of 423 injuries = 72.4% sensitivity.** Out-of-sample.

**What they do not report:** specificity, false positive rate, precision, or total
athlete-days flagged. They report only this: *"on 80% of all days, no more than three
players were classified as high risk"* (four including medium risk).

**Do the arithmetic.** A pro squad is ~25–30 players. Three high-risk flags per day is
~10–12% of athlete-days. But the success window is **1–7 days**, so a player counts as
"forecast" if any of ~7 daily flags fired. Even at 12%/day with heavy autocorrelation,
a large fraction of the squad gets flagged at some point in any given week — plausibly
30–50%.

**72% sensitivity against a ~30–50% background flag rate is a modest lift, not a
breakthrough.** It is also retrospective and not peer-reviewed.

This is not an accusation of bad faith — it is the standard way sensitivity gets reported
without the denominator. **We must never report sensitivity without the flag rate.** If we
publish, publish precision, specificity, and the fraction of athlete-days flagged.

---

## 7. Why the Papers in `academic-papers.md` Read Better Than They Are

Corrections to earlier readings, so they are not repeated:

**Paper 1 (3-IMU config, R²=0.91).** This is a *measurement fidelity* result — 3 IMUs
reproduce what 17 IMUs measure. It says nothing about injury. Correctly used as a hardware
blueprint. Incorrectly used as evidence for prediction.

**Paper 2 (92.3% accuracy, IMU+sEMG, n=50).** The "injury risk" labels were generated by
thresholding the same signals the model reads (>10° joint asymmetry, >15% muscle force
imbalance). The model is learning the threshold rule, not learning injury. It is
**circular**, and 92.3% accuracy on a self-defined label is not an injury-prediction
result. Also n=50, also EMG-dependent.

**Papers 4, 7, 9.** Measurement/estimation validity, not prospective injury outcomes.

**The fatigue literature.** A 2026 systematic review of 24 studies on fatigue-induced
biomechanical change is explicit: **"did not prospectively track injury incidence…
these variables should be interpreted as biomechanical correlates or theoretical pathways
that may contribute to injury development rather than causal predictors of injury."**

The same review adds a harder problem: **fatigue responses are highly individual.** Some
runners increase peak vGRF and develop a heel-strike transient; cadence and step length
show *no consistent group-level change*. Trained runners maintain mechanics; novices
degrade more. **A group-trained model will therefore underperform on any individual.**

### What fatigue *does* reliably change (all IMU-measurable)
| Variable | Direction | IMU-measurable |
|---|---|---|
| Ground contact time | ↑ consistently | Yes |
| Stride length | ↓ | Yes |
| Vertical stiffness | ↓ ~6% | Yes (derived) |
| Tibial acceleration | ↑ after prolonged fatigue | Yes (direct) |
| Vertical loading rate | ↑ / poorly attenuated | Yes |
| Ankle power | ↓ | No — needs lab |
| Knee/hip moments | ↑ (proximal redistribution) | No — needs lab |

**Fatigue is genuinely detectable from IMUs.** That is real and defensible. The unproven
link is fatigue → injury with actionable lead time and specificity.

---

## 8. Measurement Noise vs Signal Threshold — A Problem We Created

Paper 2's risk rule is ">10° joint angle asymmetry." Published IMU joint-angle accuracy:

| Source | Error |
|---|---|
| Optimized 4-sensor lower-limb set | ankle RMSE 3.90°, knee 6.35°, hip 5.93° |
| Worst placements in same study | knee 9.31°, hip 21.46° |
| 3-DOF knee angle, walking→running | RMSE 1.6°–5.9° |
| Self-placed IMUs, ML method | 0.7° (slow walk) → 3.4° (5 mph run) |
| Markerless video (reference) | 3.0° walk, 4.1° run |

**Knee RMSE of ~6° against a 10° threshold means measurement noise is ~60% of the signal
we intend to threshold on.** Add sensor-to-segment misalignment drift over a session and
the threshold is not reliably resolvable.

Either the threshold must be much larger, or we must work in **within-subject change from
that athlete's own baseline** (where systematic placement error partially cancels) rather
than absolute joint angles. The within-subject framing is also what the fatigue
literature's individuality finding demands.

---

## 9. So What Data Would Actually Be Needed?

Synthesized from the scoping review recommendations and the failure modes above.

**Why current datasets fail:** median cohort in the ML injury-prediction scoping review was
**122 participants**. AUC range across 27 studies 0.57–0.95; only 3 studies (11%) >0.90.
39% used SMOTE to fake balance, which manufactures synthetic injuries and invites
overfitting. GPS external load appeared in only 7 of 38 studies (avg AUC 0.75).

**What a credible dataset needs:**

1. **Within-subject longitudinal design.** Each athlete is their own control. Deviation
   from personal baseline, not population comparison. This is the only framing consistent
   with the individuality finding.
2. **Thousands of athlete-seasons.** Injuries are rare; you need the events, not the
   subjects. 122 people is not a dataset, it is a pilot.
3. **Time-stamped injury surveillance with tissue-level diagnosis** — not "pain ≥1 for
   7 days" self-report. The ARION RCT's biggest weakness was self-reported injury.
4. **Context features that are known to matter more than biomechanics:**
   - previous injury (by far the strongest established risk factor)
   - training history and rate of load change
   - sleep, illness, menstrual cycle phase
   - surface, footwear age, terrain
   - psychological state
5. **Continuous exposure data, not session summaries** — the whole point of the pod.
6. **Prospective, out-of-sample, externally validated** on athletes and teams never seen
   in training. Cross-year, not cross-fold.

**Nobody has this.** It does not exist publicly. It is the actual moat and the actual
bottleneck. It is also why Zone7 (50+ clubs, real pro data, $8M funded) still cannot
publish a peer-reviewed specificity number.

---

## 10. Honest Verdict

**Do not build an injury predictor. It is not a technology gap; it is an evidence gap that
30 years of sports science has failed to close.**

What is defensible to build today, in descending order of evidential support:

1. **Real-time movement coaching** — the ARION mechanism. Cue better mechanics
   continuously. Weak RCT support, plausible mechanism, no prediction claim required.
2. **Fatigue and mechanical-degradation detection** — well-supported as *measurement*.
   GCT ↑, stride ↓, stiffness ↓, tibial accel ↑ are real and IMU-visible. Report them as
   what they are: "your mechanics have degraded X% from your baseline," not "you are at
   risk of injury."
3. **Compliance and dosing for interventions that actually work** — Nordic hamstring
   execution quality, FIFA 11+ adherence. This is the only tier with 39–50% effect sizes.
4. **Performance and readiness baselining** — no injury claim at all, and the market
   already pays for it.

The green/yellow/red idea survives **only if red means "your mechanics have changed
significantly from your own baseline"** — an observable, verifiable statement — and never
"you are likely to be injured," which we cannot support and which creates the liability
described in `positioning-and-liability.md`.

---

## Sources
- Bahr R. *BJSM* 2016;50(13):776-80 — screening does not work
- Ruddy et al. *MSSE* 2018 — hamstring prediction, median AUC 0.58 — https://pubmed.ncbi.nlm.nih.gov/29266094/
- Sports Medicine – Open 2022 — https://sportsmedicine-open.springeropen.com/articles/10.1186/s40798-022-00416-z
- Vannatta et al. *Human Movement Science* 2020 — https://www.sciencedirect.com/science/article/abs/pii/S0268003320300930
- Prospective cohort n=98 — https://pmc.ncbi.nlm.nih.gov/articles/PMC11532757/
- Matijevich et al. *PLOS ONE* 2019 — https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0210000
- ML scoping review — https://pmc.ncbi.nlm.nih.gov/articles/PMC12013557/
- ARION RCT — https://pmc.ncbi.nlm.nih.gov/articles/PMC10905988/
- Fatigue biomechanics systematic review — https://pmc.ncbi.nlm.nih.gov/articles/PMC12942261/
- IMU placement optimization — https://pmc.ncbi.nlm.nih.gov/articles/PMC7660215/
- Zone7 validation — https://zone7.ai/case-studies/validation-study/validation-study-injury-risk-forecasting-with-zone7-ai/
- Nordic/FIFA11+ meta-analyses — https://www.physio-pedia.com/Nordic_Hamstring_Training
