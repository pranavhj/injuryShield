# The Crux Problem: Why Multi-Point Body Sensors Haven't Taken Off

This is the foundational analysis. Every design decision flows from understanding these 5 barriers.

## Barrier 1: Setup Friction (THE #1 KILLER)

Wrist wearables dominate because: put it on once, forget it. No positioning, no pairing, no thinking.

Multi-point sensors require athletes to correctly place 3-5 devices on specific body locations EVERY session, pair them, and charge multiple devices.

**Evidence — Tokyo 2020 Olympics (GSSI Study):**
- Gatorade Sports Science Institute ran a multi-sensor pilot at the Olympics
- Planned broad deployment across athletes
- Result: only **2 athletes** monitored across all events
- A 10,000m Olympic finalist "opted not to wear the chest HR monitor, skin temperature sensor or the foot sensors"
- Athletes were given the option to customize data display — inadvertently reduced standardized collection

**The quote:** "It doesn't matter how accurately a device measures sleep if it's too uncomfortable to wear and sits on an athlete's bedside table instead of their wrist all night."

**Our answer:** Minimal 3-pod system (not 5+). Auto-calibration (no poses). Snap-on in <60 seconds. Apparel option makes it even faster (put on shorts + sleeves, pods already docked).

## Barrier 2: Smart Apparel Durability (Materials Science Dead End)

Companies that embedded sensors IN fabric:

**Athos ($51.2M raised, FAILED):**
- EMG sensors in compression clothing
- Had to wear like wetsuit, no undergarments allowed
- Completely non-breathable
- $600 per set (shirt + shorts + 2 core units)
- Sensors degraded with washing, eventually failed
- Returns = unsaleable (skin-contact garments, can't resell)
- Very niche market (pro athletes only)
- VC invested $50M without proper due diligence on product-market fit

**Smart textile degradation data:**
- 50-70% accuracy loss after 10-15 washes at 40°C
- Complete sensor failure after 20-30 wash cycles
- Consumers expect 50+ wash durability
- No standardized testing methods exist for e-textile washing
- Four stress types during washing: chemical (detergent), thermal, solvent (water), mechanical (friction/twist)
- Silver-plated conductive fibers (used for EMG) "rapidly lose conductivity"

**Companies still trying:**
- Hexoskin: alive but pivoted to space (NASA/Canadian Space Agency). 8.9% of smart clothing market. Not mainstream sports.
- Sensoria: smart socks with textile pressure sensors. Clinical/rehab niche.
- formsense: 20+ sensors in apparel. Clinical focus. Not widely adopted in team sports.

**Our answer:** Don't embed electronics in fabric. Removable snap-on pods. Apparel is just normal compression fabric with snap/magnetic docks. Wash the clothing normally. Charge the pods separately.

## Barrier 3: Weight/Size (LARGELY SOLVED)

Modern sensor pods are already tiny enough:

| Device | Weight | Size |
|---|---|---|
| Xsens DOT | 11.2g | 36×30×11mm |
| KINEXON IMU | 15g | Fits in waistband |
| Garmin Running Pod | <14g | Clips to shoe |
| Zwift Running Pod | ~10g | "Size of a piece of candy" |
| NBA ball sensor | ~1g | "Weight of a raisin" |
| BMI 160 chip | 2.2g | 2.5×3.0×0.83mm |
| Fitbit Air | Ultra-light (TBD) | Pebble-shaped, screenless |

At 11-15g, a pod on the shin or shoe is imperceptible during running. The weight is NOT the barrier anymore — setup friction is.

**Our target:** <15g per pod. Fitbit Air form factor (screenless pebble).

## Barrier 4: Data Overload Without Insight

From GSSI: "Eleven performance variables generated between 1,000 and 5,000 data points per athlete"

Teams collect data but can't interpret it. They "drown in data." The GSSI article explicitly calls for "data science training for future practitioners."

The problem: raw sensor data → ??? → actionable coaching decision. The ??? is unsolved for most teams.

**Current state:** Catapult's OpenField shows 1,800 metrics post-session. A college soccer coach doesn't need 1,800 metrics. They need one signal: "Pull player #7 before they get hurt."

**Our answer:** The product IS the intelligence layer. One clear output: green/yellow/red risk per athlete. Not 1,800 metrics. The detailed data exists for sports scientists who want it, but the default view is simple.

## Barrier 5: Regulatory + Privacy

- NBA: wearables BANNED in live games (training only)
- NHL: wearables banned in games
- World Rugby: chest HR monitors banned in matches
- UCI: physiological sensors banned in cycling competition
- NCAA: new data governance guidelines (2026)
- Athletes raise privacy concerns about coaches seeing menstrual cycle data, sleep data, etc.
- NBA: data "may not be used in contract negotiations" ($250K fine)
- No legal clarity on who OWNS athlete data

**Our answer:** Start with training market (universally allowed). Build for privacy-first design. Athlete controls their own data. Regulatory pathway is a long-term workstream, not a blocker for v1.

## The Core Insight: Convenience-Accuracy Tradeoff

| Approach | Convenience | Accuracy (Biomechanics) | Durability |
|---|---|---|---|
| Wrist wearable | 10/10 | 2/10 (can't measure joints) | 10/10 |
| Smart apparel (20+ sensors) | 6/10 | 9/10 | 3/10 (wash degradation) |
| Multi-pod array (5+ pods) | 3/10 (setup friction) | 9/10 | 8/10 (sealed pods) |
| **Our 3-pod snap-on** | **7/10** | **8/10** | **9/10** |

Nobody has cracked "accurate multi-point biomechanics with near-zero friction." Our bet: 3 pods (not 5+) with snap-on (not strap-and-calibrate) hits the sweet spot.

## Why Existing Companies Don't Solve This

| Company | Why They Don't Build What We're Building |
|---|---|
| Catapult/STATSports | Post-session dashboard SaaS is their revenue model. Real-time on-device alerting would cannibalize dashboard subscriptions. |
| WHOOP | Recovery company (sleep/strain). Not interested in biomechanics. Single-sensor approach is core to their simplicity brand. |
| formsense | Clinical/rehab focus. 20+ sensors is overkill. Apparel durability unsolved. |
| Garmin/Apple/Fitbit | Consumer wrist wearables. Moving to multi-point body sensors would fragment their product lines and confuse consumers. |
| Xsens/IMeasureU | Motion capture research tools. Not consumer products. $200+/sensor, software subscription model targets labs not teams. |
| Academic researchers | Prove concepts but don't build products. Gap between published paper and shipping product is enormous. |

## ACWR (Acute:Chronic Workload Ratio) — The Industry's Broken Metric

The dominant injury prediction metric in pro sports is being DEBUNKED:
- **Mathematical coupling:** acute load is embedded within chronic load, creating spurious correlations
- **No agreed timeframe:** no rationale for specific acute/chronic window lengths
- **Randomized data performs equally well:** some studies show random chronic loads predict as well as ACWR
- **Not biomechanical:** ACWR measures workload volume (distance, sprints), NOT movement quality
- **Retrospective:** calculated post-session, can't prevent anything in real-time

This is a strategic opening. The industry's standard tool is being questioned by its own researchers. A product offering real-time biomechanical risk detection (not retrospective workload ratios) is positioned as the scientifically superior approach.
