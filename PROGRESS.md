# InjuryShield

## State
Currently: **Viability assessment, pre-build.** Premise audit killed injury prediction;
reframed around real-time gait retraining. Market teardown done. **Tests 1 and 3 complete
and both favourable** — there is a real RCT-backed intervention (Chan 2018: n=320,
HR 0.38, 62% injury reduction in *uninjured* runners) that needs **two tibial pods**, not
five, and sits in a capability envelope no camera or wrist device can enter.
**The science is stronger than expected; the business model is now the weak point** —
the intervention is a 2–3 week programme with faded feedback, so the customer graduates
(K11), which breaks the WHOOP-style subscription. Clinic/physio channel newly on the table.
Verdict: nothing says stop. Still don't build hardware.
Last session: 2026-08-23

## Done
- Market research: competitors, market sizing, gaps identified
- Academic paper review: 9 key papers cataloged
- Regulatory landscape: all major leagues mapped
- Competitor analysis: Catapult, WHOOP, STATSports, formsense, Xsens, Athos (failed)
- **Predictive validity audit** (`research/predictive-validity.md`) — Bahr 2016, Ruddy
  AUC 0.58, 23/25 null meta-analyses, ACWR RCT null, GRF↛tibial load, ARION RCT
- **Sensor architecture research** (`research/archive/sensor-architecture.md`) — placement error
  data, sparse-IMU literature, BLE throughput limits
- **Buyer / liability / structure research** (`research/buyer-and-liability.md`) — HS and
  NCAA budgets, workers' comp ROI, FDA wellness line, WHOOP economics, H-1B 2025 rule
- Tracker restructured: P0 (existential) added and gates everything; 6 decisions reversed
- **Market teardown** (`research/market-teardown.md`) — full landscape, graveyard analysis
  (NURVV insolvent 2023, Athos, UA HealthBox, Lumo), winners (Catapult $140.7M/94% recurring,
  VALD 4,000+ orgs with *no wearable*, Stryd, Playermaker, WHOOP), platform-absorption threat
- **Kill register** (`problems/VIABILITY.md`) — K1–K10, cheapest-first test order, gates
- **Standing market watch** (`market/WATCHLIST.md` + `LOG.md`) — quarterly, first due 2026-11-23

- **Tests 1 and 3 run** — capability envelope (K4 40%→15%) and gait-retraining literature
  (K3 45%→15%, Chan 2018 RCT HR 0.38). K2 halved to 30%. New K11 at 40%.

## Next
1. **Model the business model against the intervention** (free, ~1 day). Now the top
   priority because of K11: the evidence-based intervention is a 2–3 week programme with
   faded feedback, so model **programme / rental / clinic economics**, not just subscription.
   Resolves K7 and much of K11.
2. **Founder wears two tibial pods for 30 days.** Measure days actually worn; capture first
   within-subject baseline. Resolves K2 remainder and part of K5.
3. **20 runner interviews + 5 physio interviews.** The physios are the buyer in option A′
   and nobody has spoken to one.
4. Scope option A′ (clinic/physio channel) properly — it did not exist before K11.
5. Rename — "InjuryShield" is the claim we can't make (TRACKER P4.4.6).

**Still do not build hardware.** Sensor spec should be revisited only after item 1 —
the field-validated configuration is two tibial pods, not the five in `archive/sensor-architecture.md`.

## Key Decisions
- **Running only for v1 - because it is the only domain where we have a defensible claim.**
  Chan's HR 0.38, peak tibial acceleration, the 8-session protocol and the insole validation
  are all running-specific; step outside and all of them go to zero at once. Expansion axis
  is LOCOMOTION (return-to-sport/ACL asymmetry is the best v2), not "all movement". Gym form
  is the worst option - a wrist IMU already hits 89-93% and Atlas Wearables was absorbed by
  Peloton in 2021.
- **Hardware platform yes, "app analyses everything" no.** Xsens DOT is already the universal
  snap-anywhere pod and sells itself as a "development platform" - because the analysis is the
  product and they do not have it. Analysis transfers ~10% between domains; datasets 0%.
  Build mount-agnostic hardware and a domain-free app shell; do not market a platform.
- **Attachment: removable pods, mounted to what the athlete already puts on.** Shoe/lace
  mount at the low end (zero laundry exposure - Stryd and Playermaker both prove it), straps
  at the high end. NOT apparel: it is the only carrier washed after every session, and WHOOP
  at $1B ARR has not solved it (their answer is "always remove sensors before washing" plus
  a spare pod in the box). No apparel line for now.
- **There is no low-friction way to do 5-7 pods and nobody has one.** Friction tolerance
  scales with the customer, so the attachment system should too.
- **Setup friction is the governing constraint.** Wrist wearables - zero extra decisions -
  are abandoned at ~30% in 6 months; 50% of college students quit in 2 weeks. Every added
  pod is another decision. Fewest pods that works, attached to something already worn (shoe
  or insole). Tier ladder is on hold.
- **The product is a finite 8-session programme, not a perpetual wearable.** Published field
  adherence: 100% completion. People abandon habits; people complete courses. This is what
  makes amateurs reachable rather than pro-teams-only.
- **BOM is not the constraint.** ~$29 landed/pod at 1k units, ~$16 at 10k. Kit COGS
  $76-$256 against $249-$749 retail. ~$150-200 of margin per Core kit is available to spend
  on ease of use, which is where the value and the difficulty actually live.
- **Not an injury predictor.** Real-time movement coaching + within-subject degradation.
- **Core = 2 pods (both tibias) - the RCT-validated config.** Ladder 3/5/7 is an opt-in
  customer choice, not an architecture bet.
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
