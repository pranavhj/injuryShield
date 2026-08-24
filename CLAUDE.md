# InjuryShield — Real-Time Movement Quality Monitoring for Athletes

> **The name is provisional and must change before launch.** "InjuryShield" asserts a claim
> the evidence does not support, and creates exactly the liability described in
> `research/buyer-and-liability.md` §2. See TRACKER P4.4.6.

## What This Is
A startup building real-time movement-quality monitoring using lightweight wearable sensor
pods. The system measures gait mechanics continuously, detects when an athlete's mechanics
degrade from *their own* baseline, and delivers real-time coaching cues.

**It is not an injury predictor.** That was the original premise; the evidence killed it on
2026-08-23. See `research/predictive-validity.md`. What survived is better-founded and
still valuable.

## The Core Insight (revised 2026-08-23)
- **Injury prediction from biomechanics does not work.** Bahr 2016: no screening test for
  sports injury has ever had adequate test properties. Ruddy 2018: median AUC 0.58,
  between-year 0.52 (coin flip). 23 of 25 meta-analyses on running biomechanics: null.
- **ACWR is not just mathematically flawed — it failed its RCT.** 34 teams, 482 players,
  10 months, ACWR-guided vs normal training: no difference in injury rates. The entire
  load-management category premise fell.
- **IMU loading metrics don't reflect tissue load.** Impact peak r=−0.29, loading rate
  r=−0.20 vs peak tibial load. The sign may be inverted. Named devices make this error.
- **What does work:** (a) real-time gait coaching — ARION RCT, 220 runners, as-treated
  HR 0.53 (ITT null, so: suggestive not proven); (b) universal prevention programs —
  Nordic hamstring ~50%, FIFA 11+ ~39% reduction.
- **The synthesis: what works is the intervention, not the identification.** Nobody has
  ever shown that screening *who* gets the intervention beats giving it to everyone.
- **Fatigue and mechanical degradation ARE reliably IMU-detectable.** GCT↑, stride↓,
  stiffness↓~6%, tibial accel↑. That is a real, defensible measurement product. The
  unproven step is degradation → injury with actionable lead time.
- Multi-point sensors haven't taken off due to setup friction, apparel durability, and data
  overload — not because the tech doesn't work.

## The Product Vision
Sensor pods (~10–15 g each) that snap onto compression apparel or clip to straps. Pods do
high-rate data collection and reliable transport. **The phone does all inference.** The
output is a real-time coaching cue and a within-subject deviation report — never a risk
score, never a safety clearance.

### Key Design Principles
1. **Trustworthy joint data first, then cost.** 5-pod core (lumbar + 2 shanks + 2 ankles),
   scaling to 7 (+2 thighs) for full lower-limb kinematics. 3-pod is the *entry* tier — it
   gives spatiotemporal metrics and asymmetry but **no joint angles**.
2. **Hybrid compute.** Pods collect and stream; the phone infers. No edge ML in v1 —
   nothing in the product needs sub-200 ms on-device inference.
3. **Within-subject always.** Every metric is deviation from that athlete's own baseline.
   Fatigue responses are highly individual; group models underperform individuals. Also,
   IMU knee RMSE ~6° against a 10° threshold means only within-subject change is resolvable.
4. **Claim discipline.** Describe measured mechanics. Never assert risk or safety.
5. **Hybrid form factor.** Snap-on pods for branded apparel OR standalone straps/clips.
6. **Sport-agnostic hardware.** Same pods, sport-specific models.
7. **Subscription, not hardware margin.** BOM is a payback input, not a price ceiling.

### Target Markets (in order)
1. **Individual runners** (v1) — the only sports buyer who holds their own budget and
   needs no injury claim. 37–56% annual injury incidence; 7.7 per 1000 hr.
2. **Industrial athlete / workers' comp** — a genuine pivot option, not a footnote. Same
   hardware, same real-time coaching, a payer who directly eats the injury cost, and proven
   ROI (250% average, 52–64% injury reduction). See `research/buyer-and-liability.md` §1.
3. **High school / college programs** — **budget-constrained to the point of non-viability
   as a hardware sale.** $3–8K total annual athletic training budget; $96–926 per athlete.
   Only works as a cheap subscription.
4. Professional training — small TAM, long sales cycles, entrenched incumbents.
5. In-game use — requires league approval, long-term.

## Founder Profile
- Semiconductor software engineer (mid-layer abstraction between customer software and firmware)
- Skills: C++, Python, embedded systems, ROS/Gazebo, Unity/C#, Android
- Currently in Bay Area on H-1B; cofounder in India
- Personal interest: runner, intersection of technology and sports
- **The "cannot monetize on H-1B" constraint is out of date.** The DHS rule effective
  17 Jan 2025 eliminated the employer-employee relationship requirement; founders owning
  >50% can self-sponsor. Real remaining constraints: specialty-occupation framing of the
  role, an independent-oversight requirement, 18-month initial approvals, lottery risk.
  **Attorney required before acting** — see TRACKER P4.5.

## Context Management — What to Read and When

### Always read first (after /clear or new session):
1. **`DECISIONS.md` — SINGLE SOURCE OF TRUTH. If any other file contradicts it, DECISIONS.md
   wins.** Lists what is locked, what was reversed, what is still open, and which research
   files are stale. Read this before trusting anything else.
2. This file (CLAUDE.md) — project identity and principles
3. `PROGRESS.md` — current state, what's done, what's next
4. `problems/VIABILITY.md` — kill register and decision gates. Decides *whether* to build.
5. `problems/TRACKER.md` — the work list. Decides *what* to build. Has a research index at
   the bottom.

### Read when working on specific areas:

| Working on... | Read this file |
|---|---|
| **Anything at all — check first** | **`DECISIONS.md` — what is currently true** |
| Deciding whether to build | `problems/VIABILITY.md` — kill register K1–K11, gates |
| Any claim about injury | `research/predictive-validity.md` |
| Running only? Universal pod? Expansion | `research/scope-and-expansion.md` |
| Embedded vs removable vs apparel vs straps | `research/attachment-strategy.md` |
| Setup friction, retention, abandonment | `research/friction-and-retention.md` |
| BOM, volume pricing, certification, test hardware | `research/bom-and-pricing.md` |
| Revenue models, why subscription fails | `research/unit-economics.md` |
| What only we can do vs wrist/camera/force plate | `research/capability-envelope.md` |
| Competitors, who died and why | `research/market-teardown.md` |
| Who pays, claim language, FDA, H-1B | `research/buyer-and-liability.md` |
| Why multi-point sensors haven't taken off | `research/crux-analysis.md` |
| Compute split, BLE budget, flash sizing | `research/sensor-architecture.md` §2 — **§1 pod count is SUPERSEDED** |
| League rules (deferred, year 3) | `research/regulations.md` |
| Pod design reference | `research/fitbit-air-reference.md` |
| Quarterly market review | `market/WATCHLIST.md` → log to `market/LOG.md` |

**Stale files — do not read without their banner:** `competitors.md` (superseded),
`ecosystem-business-model.md` (pricing reversed), `market-sizing.md` (low value),
`academic-papers.md` (two papers misread). Each carries a warning at the top.

### Do NOT load all research files at once — they total 3000+ lines. Read only what's relevant to the current task.

## Project Structure
```
research/                        # All research findings — read selectively
  predictive-validity.md         # * Does any of this predict injury? (answer: no) — READ FIRST
  market-teardown.md             # * Who wins, who died, what to duplicate/avoid
  sensor-architecture.md         # * Pod count, placement, hybrid compute, BLE budget
  buyer-and-liability.md         # * Who pays, claim language, FDA, subscription, H-1B
  academic-papers.md             # 9 key papers — see predictive-validity.md section 7 for corrections
  competitors.md                 # Superseded by market-teardown.md; kept for the Athos detail
  crux-analysis.md               # WHY multi-point sensors haven't worked (5 barriers)
  ecosystem-business-model.md    # Revenue model — pricing superseded
  market-sizing.md               # TAM/SAM/SOM — top-down numbers, low value; see teardown
  regulations.md                 # League-by-league wearable rules
  fitbit-air-reference.md        # Design reference (user's preferred form factor)
market/                          # Standing market-watch discipline — quarterly, never ends
  WATCHLIST.md                   # Who to watch, trigger signals, review checklist
  LOG.md                         # Dated review entries, append-only
problems/
  VIABILITY.md                   # * Kill register K1-K10, test ordering, decision gates
  TRACKER.md                     # Master index — P0 (existential) gates P1-P7
knowledge/                       # Learnings accumulated over time (create as needed)
ideas/                           # Product ideas, feature concepts (create as needed)
validation/                      # User interviews, community feedback (create as needed)
```

## Key Technical Decisions

Revised 2026-08-23. Struck-through rows were reversed by evidence — see TRACKER changelog.

| Decision | Rationale | Source |
|---|---|---|
| **5-pod core / 7-pod full / 3-pod entry** | 3 pods give no joint angles (no thigh/shank sensor). Optimized set: ankle 3.90°, knee 6.35°, hip 5.93° RMSE. Placement matters more than count. | `sensor-architecture.md` |
| **Pods collect, phone infers** | No use case needs sub-200 ms on-device inference. ACL rupture ~50 ms (can't pre-empt); gait cues need seconds; fatigue needs minutes. Phone logic ships in an app update; pod logic needs an OTA campaign. | `sensor-architecture.md` |
| **Within-subject baselines only** | Fatigue responses are highly individual; cadence shows no consistent group-level change. IMU knee RMSE ~6° vs a 10° threshold = noise is 60% of signal. | `predictive-validity.md` §7–8 |
| **No injury-risk claims; deviation-from-baseline only** | Liability is asymmetric — a false "safe" is company-ending. Also keeps us inside FDA general wellness. | `buyer-and-liability.md` §2 |
| **Subscription, hardware included** | WHOOP: $1B ARR, >80% retention, LTV:CAC 4.5x. Makes a 5–7 pod BOM a payback input rather than a price ceiling. | `buyer-and-liability.md` §3 |
| 200 Hz distal / 100–150 Hz proximal | BLE fits 3–6 sensors @ 200 Hz. Joint angle needs less bandwidth than foot-strike detection. | `sensor-architecture.md` |
| 64–128 MB flash per pod, log raw always | The dataset is the moat and the bottleneck. ~35–60 MB compressed per 4 hr session. | `sensor-architecture.md` |
| Auto-calibration (no poses) | Motion-driven SO(3) alignment. Solves setup friction. | Paper 8 (Sensors 2026) |
| Removable pods (NOT embedded in fabric) | Solves wash degradation. Athos failed with embedded. Also makes subscription refurbishment viable. | `crux-analysis.md` |
| Sport-agnostic hardware | Same pods everywhere, sport-specific models. | Architecture decision |
| ~~3-pod system~~ | Reversed — a measurement-fidelity result misread as a product spec. | — |
| ~~<200 KB edge ML model, <200 ms~~ | Reversed — inherited from a paper, not derived from a user need. | — |
| ~~$35/pod hardware sale, $105 kit~~ | Retired — replaced by subscription. | — |
| ~~EMG for 92.3% accuracy~~ | Reversed — that result is circular (labels thresholded from the same signals). | — |

## Connection to makingDollarsInIndia
This project lives separately from `c:\Users\prana\projects\makingDollarsInIndia` but serves
the same goal: earning USD from India. See `research/ecosystem-business-model.md` for the
India connection, and `research/buyer-and-liability.md` §4 for the corrected entity
structure — note that Section 44ADA applies to an *individual professional*, not to a
company, so the structure choice matters.

## Working Philosophy
- Track EVERY problem explicitly — no assumptions, no hand-waving
- **Interrogate the premise before optimizing the implementation.** The project ran 80+
  tracked problems for a while without asking whether the central claim was true. It wasn't.
- Research before building — validate before committing
- **Academic papers are evidence, not authority.** Check what a result actually measured.
  Two of the nine founding papers were being read for more than they showed.
- **Never report sensitivity without the flag rate.** Applies to us and to everyone else.
- **Not every problem is equal.** ~5 of the 80+ tracked items can kill the company; the rest
  are engineering. Work the killers first, cheapest test first. See `problems/VIABILITY.md`.
- **A day of research beats a month of building.** K1 (injury prediction doesn't work) would
  have killed this in year three. It cost one day to find in year zero.
- **The market is watched forever, not once.** NURVV went Series A → insolvent in 3.5 years;
  Garmin deprecated its own accessory category in a firmware update. Quarterly review,
  `market/WATCHLIST.md`. Intel older than 12 months is actively misleading.
- User is the first test subject (runner) — v1 must work for their own runs
- This is a SEPARATE context from makingDollarsInIndia — don't mix projects
