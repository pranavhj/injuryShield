# InjuryShield — Real-Time Sports Injury Prevention System

## What This Is
A startup building a real-time injury risk detection system using lightweight wearable sensor pods. The system detects fatigue, gait degradation, and biomechanical risk during live training/games and alerts coaches BEFORE injuries happen — not after.

## The Core Insight
- Current products (Catapult, STATSports, WHOOP) do post-session workload analysis — they tell you AFTER the session that a player was overloaded
- Academic research has proven real-time injury prediction works (92.3% accuracy, 188ms latency) — but nobody has productized it
- The dominant injury metric (ACWR) is being debunked by researchers as mathematically flawed
- Multi-point body sensors haven't taken off due to setup friction, apparel durability, and data overload — NOT because the tech doesn't work

## The Product Vision
Tiny sensor pods (Fitbit Air-sized, ~10-15g each) that snap onto compression apparel OR clip to straps. Edge ML on the pod computes injury risk in real-time. Alerts via haptic buzz when fatigue/biomechanical patterns degrade.

### Key Design Principles
1. **Hybrid form factor**: Snap-on pods that work with branded compression apparel OR standalone straps/clips
2. **Minimal viable sensors**: 3-pod system (lower back + both ankles) proven optimal by research
3. **Edge-first**: On-device ML inference (<200KB model, <200ms latency), no cloud dependency for alerts
4. **Sport-agnostic hardware**: Same pods, sport-specific ML models
5. **Ecosystem, not product**: Pods + apparel + app + subscription analytics + team dashboard

### Target Markets (in order)
1. Individual runners/athletes (v1 — founder is a runner, self-dogfooding)
2. High school / college athletic programs (price-sensitive, <$35/pod)
3. Professional training (alongside existing Catapult/STATSports setups)
4. In-game use (requires league approval — long-term goal)

## Founder Profile
- Semiconductor software engineer (mid-layer abstraction between customer software and firmware)
- Skills: C++, Python, embedded systems, ROS/Gazebo, Unity/C#, Android
- Currently in Bay Area on H-1B, planning to move to India in ~2 years
- Personal interest: runner, intersection of technology and sports
- **Cannot monetize while on H-1B** — build as open-source/portfolio project during this phase

## Context Management — What to Read and When

### Always read first (after /clear or new session):
1. This file (CLAUDE.md) — project identity and principles
2. `PROGRESS.md` — current state, what's done, what's next
3. `problems/TRACKER.md` — master problem index (scan headers, don't read all 80+ items)

### Read when working on specific areas:

| Working on... | Read this file |
|---|---|
| Hardware decisions (sensors, MCU, battery, form factor) | `research/academic-papers.md` (sensor specs, sampling rates) |
| Competitive positioning, why we're different | `research/competitors.md` |
| Why multi-point sensors haven't taken off | `research/crux-analysis.md` (5 barriers, Athos failure, ACWR debunking) |
| Business model, pricing, revenue | `research/ecosystem-business-model.md` |
| Market size, funding landscape | `research/market-sizing.md` |
| League rules, what's allowed in games | `research/regulations.md` |
| Pod design inspiration | `research/fitbit-air-reference.md` |
| Exploding a specific problem | `problems/TRACKER.md` → find the P-number → create sub-file in `problems/` |

### Do NOT load all research files at once — they total 3000+ lines. Read only what's relevant to the current task.

## Project Structure
```
research/                        # All research findings — read selectively
  academic-papers.md             # 9 key papers with extracted findings
  competitors.md                 # Full competitive landscape + Athos failure
  crux-analysis.md               # WHY multi-point sensors haven't worked (5 barriers)
  ecosystem-business-model.md    # Revenue model, pricing, open-source strategy
  market-sizing.md               # TAM/SAM/SOM, market numbers
  regulations.md                 # League-by-league wearable rules
  fitbit-air-reference.md        # Design reference (user's preferred form factor)
problems/                        # Every identified problem, tracked systematically
  TRACKER.md                     # Master index — 80+ items across 8 categories (P1-P8)
knowledge/                       # Learnings accumulated over time (create as needed)
ideas/                           # Product ideas, feature concepts (create as needed)
validation/                      # User interviews, community feedback (create as needed)
```

## Key Technical Decisions (already made)

| Decision | Rationale | Source |
|---|---|---|
| 3-pod system (back + both ankles) | Research-proven optimal minimum for running gait. Single sensor can't detect asymmetry. | Paper 1 (Frontiers 2026) |
| <200KB ML model on-device | Fits on standard MCU (ESP32, nRF52). <200ms inference. | Paper 1 |
| 200Hz IMU sampling rate | Required for running. 400Hz for cutting sports. Gyroscope > accelerometer. | Multiple papers |
| Auto-calibration (no poses) | Motion-driven alignment. Solves setup friction problem. | Paper 8 (Sensors 2026) |
| Removable pods (NOT embedded in fabric) | Solves wash degradation. Athos failed with embedded approach. | Crux analysis |
| Sport-agnostic hardware | Same pods everywhere. Sport-specific ML models loaded per sport. | Architecture decision |
| Edge-first (not cloud) | <200ms latency needed. Cloud round-trip too slow. Privacy advantage. | Paper 2 (Nature 2026) |

## Connection to makingDollarsInIndia
This project lives separately from `c:\Users\prana\projects\makingDollarsInIndia` but serves the same goal: earning USD from India. The consulting + open-source scanner playbook from PortPilot applies here too. See `research/ecosystem-business-model.md` for the India connection.

## Working Philosophy
- Track EVERY problem explicitly — no assumptions, no hand-waving
- Research before building — validate before committing
- Academic papers are the foundation — copy proven approaches, don't reinvent
- User is the first test subject (runner) — v1 must work for their own runs
- This is a SEPARATE context from makingDollarsInIndia — don't mix projects
