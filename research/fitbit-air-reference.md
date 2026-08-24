# Fitbit Air — Design Reference for InjuryShield Pods

The user specifically cited Fitbit Air as the form factor inspiration. This is our design benchmark.

## Fitbit Air Specs (launched May 2026)

| Spec | Value |
|---|---|
| Form factor | Screenless pebble-shaped pod + swappable band |
| Display | NONE — all data in Google Health app |
| Weight | Ultra-light (exact grams TBD — need teardown data) |
| Price | $99.99 (standard), $129.99 (Curry edition) |
| Battery | 7 days. 5-minute fast charge = 1 day of use |
| Sensors | Optical PPG (HR), red+infrared (SpO2, breathing rate), skin temp, 3-axis accelerometer, gyroscope |
| Connectivity | Bluetooth to Android 11+/iOS 16.4+ |
| Water resistance | Likely IP68 (swim-rated, per Fitbit tradition) |

## What Makes It Small
- **No screen** — biggest space/weight savings. All UI on phone app.
- **Pebble pod** — the electronics unit is separate from the band. Pod clips into band.
- **Minimal sensors** — PPG + accel + gyro. No GPS (uses phone GPS).
- **No speaker/microphone** — no NFC payment, no voice assistant.

## What We Can Learn
1. **Screenless = dramatically smaller.** Our pods don't need screens either. All alerts via haptic + app.
2. **Pod + band separation** — the pod is the electronics, the band is just a holder. EXACTLY our approach (pod + apparel/strap).
3. **$99 price point at Google-scale production.** Our landed cost is ~$29/pod at 1,000 units, ~$16 at 10,000 — see `bom-and-pricing.md`. (The old "$35/pod retail" target is retired; we sell a 2-pod Core kit at ~$249.)
4. **Fast charge** — 5 min for a day is aspirational. Magnetic pogo pins likely.
5. **7-day battery** — impressive but they have lower sampling rate (consumer use, not 200Hz sports). We'll get less battery life at higher sampling rates.

## Our Pods vs Fitbit Air

| Feature | Fitbit Air | InjuryShield Pod |
|---|---|---|
| Purpose | 24/7 health tracking | Sports session injury risk |
| Screen | None | None |
| Sensors | PPG, SpO2, temp, accel, gyro | IMU (accel + gyro) at 200Hz |
| ML on device | No (cloud processing) | YES (TinyML, <200KB) |
| Haptic | Likely vibration motor | YES (injury alert buzz) |
| GPS | No (phone GPS) | No (phone GPS or none needed) |
| Battery target | 7 days | 6-8 hours per session |
| Quantity per user | 1 | 3 |
| Price | $99 | <$35 each |
| Attachment | Wrist band | Snap-on to apparel OR strap/clip |
