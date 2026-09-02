# Test Hardware Shopping List — Updated 2026-09-01

> From TRACKER P9.1 (was P8.1). Purpose: buy the minimum hardware to
> (a) replicate the Chan 2018 2-tibia protocol, (b) demo to clinic owners,
> (c) run the founder 30-day wear test.

---

## Priority 1: Research-Grade IMU Sensors (~$200–260)

**mbientlab MetaMotionS+ (MMS+)** — 2 units
- 9-axis IMU (3-axis accel + 3-axis gyro + 3-axis magnetometer) + barometer
- 512 MB onboard NAND flash — can log raw data without a phone connection
- Up to 800 Hz sampling over BLE
- Very small form factor, wearable-ready
- Python/C++/JS SDKs — can prototype the analysis pipeline immediately
- Price: ~$87–107 each → **~$175–215 for 2 units**
- [mbientlab.com/shop](https://mbientlab.com/shop/)

**Why this over alternatives:**
- SlimeVR ($219 for a set) is cheaper per sensor but optimized for VR/full-body tracking, not clinical logging. 6-axis only (no magnetometer), no onboard flash.
- Movella/Xsens DOT ($200/sensor) is overpriced for what we need at this stage.
- mbientlab is specifically designed for clinical/research gait analysis — it's what many published gait studies use.

## Priority 2: IMU Chip Samples (~$50–80)

For evaluating which chip goes in our custom pod (TRACKER P2.2.3):

| Chip | Price/unit | Key spec | Buy from |
|------|-----------|----------|----------|
| LSM6DSV16X (ST) | ~$2.88 | Wearable-optimized, embedded ML core, low power | DigiKey/Mouser |
| ICM-45686 (TDK) | ~$6.70 | SlimeVR's top pick for drift, 6-axis | DigiKey/Mouser |
| BMI270 (Bosch) | ~$1.79 | Cheapest, SlimeVR rates "poor" for drift | DigiKey/Mouser |

Buy 3–5 of each on eval boards. ~$50–80 total.

**Note:** SlimeVR's ranking is for VR (orientation drift over hours). Our task is different
(short-window gait dynamics, <1 hour sessions). Their ranking may not apply — we must test
on OUR task.

## Priority 3: Mounting/Attachment Prototyping (~$30–50)

- Elastic shoe-clip prototypes (3D-printable or off-the-shelf sport clips)
- Double-sided adhesive pads for direct shin mounting (test P3.2.1 — tibia vs shoe)
- Velcro straps in various widths
- A digital scale (0.1g resolution) for weighing prototypes

## Optional: SlimeVR Set (~$219)

Only if we want to prototype the 3/5/7 ladder. **Not needed for the clinic demo** which
only requires the 2-pod Core. Defer unless the founder specifically wants to explore
multi-pod during the wear test.

---

## Total Budget

| Item | Cost |
|------|------|
| 2× mbientlab MMS+ | $175–215 |
| IMU chip samples | $50–80 |
| Mounting supplies | $30–50 |
| **Total (minimum)** | **$255–345** |
| + SlimeVR (optional) | +$219 |

This is cheaper than the original P8.1 estimate ($600) because we're focusing on the
2-pod Core demo for clinics rather than the full ladder exploration.

---

## What This Hardware Enables

1. **Founder 30-day wear test** (P9.2) — wear during runs, log raw data, measure comfort
2. **Clinic demo** — show a physio real gait data from a real run on a real dashboard
3. **P3.2.1 resolution** — test tibia vs shoe placement for peak tibial acceleration
4. **Analysis pipeline development** — build the phone app algorithms using real sensor data
5. **510(k) performance testing** — compare our readings against a reference system

---

## Where to Buy

- [mbientlab store](https://mbientlab.com/shop/) — direct, ships from US
- [DigiKey](https://www.digikey.com/) — IMU chip samples, eval boards
- [Mouser](https://www.mouser.com/) — alternative for chip samples
- Amazon — mounting supplies, scale
