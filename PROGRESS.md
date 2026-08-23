# InjuryShield

## State
Currently: Initial research and ideation phase complete. Problem tracker created.
Last session: 2026-08-23

## Done
- Market research: competitors, market sizing, gaps identified
- Academic paper review: 9 key papers cataloged with findings
- Regulatory landscape: all major leagues mapped
- Problem tracker: 80+ problems/questions across 8 categories
- Competitor analysis: Catapult, WHOOP, STATSports, formsense, Xsens, Athos (failed), etc.
- Key technical decisions: 3-pod system, <200KB ML model, auto-calibration, snap-on hybrid design

## Next
- Deep-dive each problem category (start with P1: Hardware)
- BOM estimation for $35/pod target
- MCU and IMU chip comparison
- Literature search: IMU-only accuracy (without EMG)
- Community validation plan

## Key Decisions
- 3-sensor minimum (lower back + both ankles) — backed by 2026 paper
- Sport-agnostic hardware, sport-specific ML models
- Hybrid form factor: snap-on pods for both apparel and straps
- Sensors NOT embedded in fabric (removable pod solves wash problem)
- Edge ML on pod (not cloud) for real-time alerting
- Start with running (founder is a runner), expand to team sports
- Target <$35/pod for school market accessibility
