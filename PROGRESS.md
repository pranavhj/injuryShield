# InjuryShield

## State
Currently: **Viability assessment, pre-build.** Premise audit killed injury prediction;
project reframed around real-time coaching + within-subject degradation. Market teardown
complete. Kill register open with two untested killers (K2 multi-pod architecture,
K3 value of the output). **Verdict: nothing says stop; several things say don't build
hardware yet.** Next month is free desk tests + a 30-day founder wear test.
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
- **Market teardown** (`research/market-teardown.md`) — full landscape, graveyard analysis
  (NURVV insolvent 2023, Athos, UA HealthBox, Lumo), winners (Catapult $140.7M/94% recurring,
  VALD 4,000+ orgs with *no wearable*, Stryd, Playermaker, WHOOP), platform-absorption threat
- **Kill register** (`problems/VIABILITY.md`) — K1–K10, cheapest-first test order, gates
- **Standing market watch** (`market/WATCHLIST.md` + `LOG.md`) — quarterly, first due 2026-11-23

## Next — in this order, first three cost nothing
1. **Classify every metric wrist-replicable vs wrist-impossible** (1 day, free). Resolves K4.
   If the value prop dies without wrist-replicable metrics, the product is a feature waiting
   to be absorbed.
2. **Model fully-loaded COGS, payback period, churn sensitivity** (1 day, free). Resolves K7.
3. **Literature search: does gait retraining help *asymptomatic* runners?** (2 days, free).
   Highest-value unanswered research question in the project. Resolves much of K3.
4. **Founder wears the full pod set for 30 days.** Measure **days actually worn out of 30**,
   not comfort. Resolves K2 and part of K5. One prototype set. *The pivotal test.*
5. 20 structured runner interviews — "when did you last change how you run, and why?"
6. Rename — "InjuryShield" is the claim we can't make (TRACKER P4.4.6).

**Do not revisit hardware decisions until 1–4 are done.**

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
