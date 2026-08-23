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

## Project Structure
```
research/               # All research findings, papers, market data
  academic-papers.md    # Key papers with findings
  competitors.md        # Full competitive landscape
  regulations.md        # League-by-league wearable rules
  market-sizing.md      # TAM/SAM/SOM estimates
  sensor-tech.md        # Sensor specifications, sampling rates, options
problems/               # Every identified problem, tracked systematically
  TRACKER.md            # Master problem tracker (index)
  hardware/             # Pod design, weight, battery, form factor
  software/             # ML models, calibration, data pipeline
  business/             # Pricing, go-to-market, regulatory approval
  user-experience/      # Setup friction, compliance, comfort
knowledge/              # Learnings accumulated over time
ideas/                  # Product ideas, feature concepts, pivot options
validation/             # User interviews, survey data, community feedback
```

## Working Philosophy
- Track EVERY problem explicitly — no assumptions, no hand-waving
- Research before building — validate before committing
- Academic papers are the foundation — copy proven approaches, don't reinvent
- User is the first test subject (runner) — v1 must work for their own runs
