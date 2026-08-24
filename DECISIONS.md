# Current Decisions — Single Source of Truth

**If any other file contradicts this one, THIS FILE WINS.** Everything else is the
reasoning that produced these; reasoning files are dated and some are superseded.

Last updated: **2026-08-24**

---

## What we are building

**A two-pod running gait-retraining programme.** Pods mount to the shoe. The phone does all
inference. Eight sessions over 2–3 weeks with real-time audio cues on peak tibial
acceleration against the runner's own baseline, feedback faded across the last four
sessions. Sold outright at ~$249. No injury-prediction claim, ever.

---

## Decisions in force

| # | Decision | Status | Why (file) |
|---|---|---|---|
| D1 | **Not an injury predictor.** Product is gait retraining with real-time feedback | Locked | `predictive-validity.md` |
| D2 | **Running only for v1** | Locked | `scope-and-expansion.md` |
| D3 | **Core tier = 2 pods, both tibias.** Ladder: 2 / 3 / 5 / 7 as customer choice | Locked | `bom-and-pricing.md` §3 |
| D4 | **Pods collect and stream; phone infers. No edge ML in v1** | Locked | `archive/sensor-architecture.md` §2 |
| D5 | **Within-subject baselines only.** Never population comparison | Locked | `predictive-validity.md` §7–8 |
| D6 | **Removable pods. Never embedded in fabric** | Locked | `attachment-strategy.md` §1 |
| D7 | **Shoe/lace mount at low end; straps at high end. No apparel line** | Locked | `attachment-strategy.md` §3–4 |
| D8 | **Outright sale, ~$249 Core.** Not subscription | Locked | `unit-economics.md` §2–3 |
| D9 | **No risk or safety claims.** Describe measured mechanics only. Green is never "safe" | Locked | `buyer-and-liability.md` §2 |
| D10 | **Programme is finite — 8 sessions, feedback faded.** Graduation is the success story | Locked | `predictive-validity.md` §4B |
| D11 | **Battery deliberately SHORT (~2–3 sessions)** so charging forces pod removal | Locked | `attachment-strategy.md` §6 |
| D12 | **Pre-certified radio module until ~5,000 pods**, then bare chip | Locked | `bom-and-pricing.md` §1 |
| D13 | **Log raw IMU always**, never only derived metrics | Locked | `scope-and-expansion.md` §6 |
| D14 | **Expansion axis is locomotion**, not "all movement." v2 = return-to-sport/ACL | Locked | `scope-and-expansion.md` §4 |
| D15 | **Build for the platform, do not pitch the platform** | Locked | `scope-and-expansion.md` §6 |
| D16 | **Rename before anything public.** "InjuryShield" is a claim we cannot make | Pending | TRACKER P4.3.6 |

## Reversed decisions — do not resurrect

| Was | Now | Reversed because |
|---|---|---|
| Injury prediction, 92.3% accuracy | Gait retraining | Paper 2 is circular; screening has never worked (Bahr 2016) |
| ACWR as the metric to beat | ACWR is dead, don't position against it | It failed its own RCT (34 teams, null) |
| 3-pod system (lumbar + ankles) | 2-pod Core (both tibias) | 3 gives no joint angles; 2 tibias is what the RCT validated |
| 5-pod core / 7-pod full | Ladder with 2 as default | Multi-pod friction is what kills companies |
| Edge ML, <200 KB, <200 ms | Phone-side inference | No use case needs sub-200 ms; inherited from a paper |
| $35/pod, $105 kit | $249 Core kit | Targeted school budgets that don't exist |
| Hardware-as-subscription (WHOOP) | Outright sale | Needs 9 months average life; intervention takes 3 weeks |
| EMG sensors | IMU only | The 92.3% result justifying EMG is circular |
| Apparel with snap-in pods | Shoe mount / straps | Only carrier washed every session; WHOOP hasn't solved it |
| Gym / resistance form as v2 | Return-to-sport as v2 | A single wrist IMU already does gym at 89–93% |
| "Cannot monetize on H-1B" | Founder self-sponsorship possible | DHS rule effective 17 Jan 2025 |

## Tooling decisions

| Decision | Status | Reasoning |
|---|---|---|
| **Retrieval is split by content type, not unified** | Decided 2026-08-24 | See below |

**Decisions / research / tracker → grep + `DECISIONS.md`.** These need *completeness* and
*authority*. Vector top-k retrieval hides contradictions (it returns the best-matching chunk
and may never surface the one that disagrees — the exact 5-pod/2-pod failure we fixed), and
chunking strips supersession banners so a stale chunk arrives looking authoritative.
Embeddings have no concept of recency; a stale and a current chunk on the same topic are
semantically near-identical by design.

**Transcripts / interview notes / user feedback → semantic search.** Unstructured, vocabulary
unpredictable, completeness does not matter. Grep is genuinely bad at this. Use the existing
**Notebook API on port 18790** (workspace `CLAUDE.md`) — store sources, query in natural
language. No MCP server needed; it already exists.

**Revisit a dedicated MCP when:** there is real sensor data (session logs, IMU time series,
per-athlete baselines) that Claude cannot grep, or the corpus passes ~50k lines. Not before —
at 12 files and ~5k lines a server is overhead without a capability gain.

## Open — genuinely undecided

| # | Question | Blocks | Where |
|---|---|---|---|
| O1 | **Distal tibia vs shoe vs insole** for peak tibial acceleration | The Core tier | TRACKER P3.2.1 |
| O2 | **Repeat-purchase rate** — company or product? | The whole business model | TRACKER P4.2.6 |
| O3 | **CAC** — above ~$150 the Core tier stops working | Pricing | TRACKER P4.2.5 |
| O4 | **Will two pods actually get worn?** (K2, 30%) | Everything | TRACKER P8.2 |
| O5 | IMU chip choice — measure on our task, not VR benchmarks | BOM | TRACKER P2.2.3 |
| O6 | Does Chan's result generalise beyond **novice** runners? | Target market | TRACKER P1.7 |
| O7 | **Novice vs experienced: evidence is in novices, money is in experienced** | Target market | `demand-side.md` §5 |
| O8 | **Is honest claim discipline a wedge or a handicap** vs Aletheia's bolder claims? | Positioning | `demand-side.md` §4 |
| O9 | **$249 upfront vs Aletheia's $239/yr at $0 upfront** — which converts? | Pricing | `demand-side.md` §4 |

---

## File status — read this before trusting a file

| File | Status |
|---|---|
| `problems/VIABILITY.md` | **Current** — go/no-go, kill register |
| `problems/TRACKER.md` | **Current** — full work list |
| `research/predictive-validity.md` | **Current** — the evidence base |
| `research/scope-and-expansion.md` | **Current** |
| `research/attachment-strategy.md` | **Current** |
| `research/friction-and-retention.md` | **Current** |
| `research/bom-and-pricing.md` | **Current** — costs, tiers, test hardware |
| `research/unit-economics.md` | **Current** — revenue models |
| `research/capability-envelope.md` | **Current** |
| `research/market-teardown.md` | **Current** — the competitive picture |
| `research/buyer-and-liability.md` | **Current** except §3 (subscription — superseded by D8) |
| `research/crux-analysis.md` | **Current** — still the best strategic analysis in the repo |
| `research/archive/sensor-architecture.md` | ⚠️ **PARTLY SUPERSEDED** — pod count wrong (says 5, now 2). Compute split and BLE data still valid |
| `research/archive/academic-papers.md` | ⚠️ **READ WITH CORRECTIONS** — Papers 1 and 2 misread; see `predictive-validity.md` §7 |
| `research/archive/competitors.md` | ⚠️ **SUPERSEDED** by `market-teardown.md`. Kept for the Athos detail |
| `research/archive/ecosystem-business-model.md` | ⚠️ **SUPERSEDED** on pricing and model by `unit-economics.md` |
| `research/archive/market-sizing.md` | ⚠️ **LOW VALUE** — top-down report numbers; the real constraints are elsewhere |
| `research/regulations.md` | Current but deferred — league rules are a year-3 concern |
| `research/fitbit-air-reference.md` | Current — design reference only |
| `market/WATCHLIST.md`, `market/LOG.md` | **Current** — quarterly discipline |
