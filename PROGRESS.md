# InjuryShield

## State
Currently: **Premise audit complete — the core claim did not survive.** Injury prediction
is killed by the evidence; the project reframed around real-time movement coaching and
within-subject degradation measurement. Tracker restructured by kill criteria.
Last session: 2026-08-23

## Done
- Market research: competitors, market sizing, gaps identified
- Academic paper review: 9 key papers cataloged
- Regulatory landscape: all major leagues mapped
- Competitor analysis: Catapult, WHOOP, STATSports, formsense, Xsens, Athos (failed)
- **Predictive validity audit** (`research/predictive-validity.md`) — Bahr 2016, Ruddy
  AUC 0.58, 23/25 null meta-analyses, ACWR RCT null, GRF↛tibial load, ARION RCT
- **Sensor architecture research** (`research/sensor-architecture.md`) — placement error
  data, sparse-IMU literature, BLE throughput limits
- **Buyer / liability / structure research** (`research/buyer-and-liability.md`) — HS and
  NCAA budgets, workers' comp ROI, FDA wellness line, WHOOP economics, H-1B 2025 rule
- Tracker restructured: P0 (existential) added and gates everything; 6 decisions reversed

## Next
1. **P0.4.1 — define kill criteria** with dates and a budget cap. Nothing else starts first.
2. **P1.10 / P0.4.1(a) — founder self-experiment.** Can we detect within-subject mechanical
   change above measurement noise in 30 days of the founder's own runs? Fastest real signal.
3. **P0.2.2/P4.4.6 — rename.** "InjuryShield" is the claim we can't make.
4. **P0.2.3/P0.2.4 — spec green/yellow/red** as deviation-from-baseline, with the statistics
   defined (baseline length, variance model, multiple-comparison handling).
5. **P4.1.5 — scope the "industrial athlete" market properly.** Proven payer, proven ROI,
   same hardware. May be the better business.
6. **P1.7 — community validation** of the *honest* framing, not the original pitch.

## Key Decisions
- **Not an injury predictor.** Real-time movement coaching + within-subject degradation.
- **5-pod core / 7-pod full / 3-pod entry.** Trustworthy joint data first, then optimize cost.
- **Hybrid compute:** pods collect and stream at high rate; the phone does all inference.
  No edge ML in v1.
- **Within-subject baselines only** — group models underperform individuals, and IMU noise
  is ~60% of the thresholds the literature uses.
- **Claim discipline is a hard rule.** Describe mechanics; never assert risk or safety.
  A false "safe" is the company-ending error.
- **Subscription (WHOOP model), hardware included.** $35/pod retail target retired.
- Sensors NOT embedded in fabric (removable pod solves wash problem)
- Sport-agnostic hardware, sport-specific models
- Start with individual runners — the only sports buyer holding their own budget
- **H-1B no-monetization assumption dropped** — Jan 2025 DHS rule permits founder
  self-sponsorship at >50% ownership. Attorney needed before acting.
