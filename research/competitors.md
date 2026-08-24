# Competitive Landscape — InjuryShield

> ## ⚠️ SUPERSEDED — 2026-08-24
> Replaced by `research/market-teardown.md`, which covers ~20 more companies and the
> graveyard analysis. **This file also contains one wrong conclusion:** it frames Catapult as
> vulnerable. Catapult posted US$140.7M revenue, 94% recurring, EBITDA +67%, and is acquiring.
>
> Kept only for the Athos failure detail, which is still accurate.


## Direct Competitors (injury prevention focus)

### Catapult Sports (Australia) — Market Leader
- **What:** GPS + IMU wearable (back-of-vest), OpenField analytics platform
- **Injury prevention:** ACWR (acute:chronic workload ratio) — POST-SESSION only
- **Real-time:** Tracks 200 parameters live (speed, HR, distance, load thresholds). NO biomechanical injury alerting.
- **Post-session:** 1,800 parameters analyzed after training
- **Price:** $20,000-$40,000/year per team
- **Weight:** ~50g sensor in vest pouch
- **Target:** Professional teams (3,500+ teams globally)
- **Gap:** No real-time injury prediction. ACWR is retrospective and mathematically questioned.

### STATSports (Ireland)
- **What:** Apex GPS tracker, vest-mounted
- **Injury prevention:** Workload monitoring, post-session dashboards
- **Real-time:** Basic live metrics (speed, HR zones, distance)
- **Price:** Consumer version ~$80-100; pro version $15,000-25,000/team
- **Target:** Pro + semi-pro teams; also consumer (Apex Athlete Series)
- **Gap:** Same as Catapult — post-session workload, no biomechanical risk alerting

### WHOOP (USA)
- **What:** Wrist/body-worn PPG + accelerometer. Recovery/strain focus
- **Injury prevention:** Recovery score, strain, HRV — all calculated OVERNIGHT
- **Real-time:** None for injury. Real-time HR display only
- **Price:** $30/month subscription (device "free" with membership)
- **Weight:** ~27g (WHOOP 4.0)
- **Any-Wear:** WHOOP Body — snap-on pod moves to torso/calf via compression apparel ($55-110/garment)
- **Target:** Individuals + pro athletes
- **Gap:** Single sensor, no biomechanics, no multi-point, no in-session alerting

### KINEXON (Germany) — NBA Official Tracking
- **What:** Ultra-wideband (UWB) + IMU sensors for indoor tracking
- **SmartCourt (July 2025):** "Real-time tracking, AI performance analysis, injury prevention alerts" — details sparse
- **Weight:** 15g per sensor
- **Price:** Enterprise only (league-level contracts)
- **Target:** NBA, Bundesliga, top-tier only
- **Gap:** Primarily position tracking, not biomechanical. SmartCourt injury claims unverified.

### formsense (San Diego, USA)
- **What:** Smart apparel with 20+ embedded sensors, biomechanics
- **Injury prevention:** Real-time form detection, biomechanical insights
- **Form factor:** Compression clothing with embedded sensors
- **Target:** Clinical rehab + sports medicine (not team sports)
- **Status:** Active but niche. Not widely adopted in sports teams
- **Gap:** Clinical focus. Apparel durability issues. Not sold to teams.

### PlayerData (UK)
- **What:** GPS tracker for amateur/youth sports
- **Price:** <$5,000 for 20-25 units
- **Target:** Youth and amateur teams priced out of Catapult
- **Gap:** Basic GPS only — no injury prediction, no biomechanics

---

## Adjacent Competitors (not injury-focused but overlap)

### Xsens/Movella DOT (Netherlands)
- **What:** IMU sensor pods for motion capture
- **Weight:** 11.2g, 36x30x11mm (IP68 waterproof)
- **Battery:** 8 hours continuous, 70mAh
- **Sampling:** 120Hz accelerometer/gyroscope
- **Price:** ~$200+ per sensor, software subscription required
- **Target:** Biomechanics research, motion capture, animation
- **Gap:** Research tool, not consumer/team product. No injury alerting. No edge ML.

### IMeasureU (NZ → acquired by Vicon/Oxford Metrics)
- **What:** Multi-limb IMU platform
- **Price:** $5,500/year subscription
- **Target:** Sports science research, elite teams
- **Gap:** Research-grade, expensive, no real-time alerting

### DorsaVi (Australia, ASX:DVL)
- **What:** Wearable sensors for clinical motion analysis (ViPerform for sports)
- **Status:** Publicly listed, stock at A$0.037 (tiny market cap). Pivoting toward robotics.
- **Target:** Clinical rehab primarily
- **Gap:** Not productized for team sports. Company struggling financially.

### Garmin Running Dynamics Pod
- **What:** Single foot/waist pod, <14g
- **Metrics:** Cadence, ground contact time, stride length, vertical oscillation
- **Price:** ~$70
- **Gap:** Post-run analysis only. No injury prediction. No multi-point.

### Fitbit Air (Google, 2026)
- **What:** Screenless pebble-shaped tracker, PPG + accelerometer + gyroscope
- **Weight:** Ultra-light (exact specs TBD)
- **Price:** $99.99 ($129.99 Curry edition)
- **Battery:** 7 days
- **Gap:** Wrist-only. No biomechanics. No multi-point. No injury prediction.

---

## Failed Competitors (LESSONS)

### Athos (USA) — DEAD
- **Raised:** $51.2M (Social Capital, DCM Ventures)
- **What:** EMG sensors in compression clothing
- **Why it failed:**
  1. Had to wear like a wetsuit — no undergarments
  2. Completely non-breathable
  3. $600 per set (shirt + shorts + 2 cores)
  4. Sensors degraded with washing
  5. Returns = unsaleable (skin contact garment)
  6. Very niche market (pro athletes only)
  7. VC raised $50M without proper market validation
- **Lesson:** Don't embed sensors in fabric. Don't target only pro athletes. Don't price at $600.

---

## Our Positioning vs. Competitors

| Feature | Catapult | WHOOP | formsense | Xsens DOT | **InjuryShield** |
|---|---|---|---|---|---|
| Real-time injury alert | No | No | Partial (clinical) | No | **YES** |
| Multi-point biomechanics | No (single vest) | No (single sensor) | Yes (20+ sensors) | Yes (research) | **Yes (3 pods)** |
| Edge ML on device | No | No | Unknown | No | **YES** |
| Setup time | 2 min (vest) | 0 (always on) | 5+ min (apparel) | 10+ min (calibrate) | **<1 min (snap-on)** |
| Wash durability | N/A (separate pod) | N/A (band) | Degrades | N/A (pod) | **N/A (removable pod)** |
| Price per athlete | $500-1000/yr | $360/yr | Unknown (clinical) | $1000+/yr | **<$105 (3 pods)** |
| Target market | Pro teams | Individuals | Clinical | Research | **Everyone** |
