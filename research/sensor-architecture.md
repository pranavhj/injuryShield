# Sensor Architecture — How Many Pods, Where, and Who Computes

> ## ⚠️ PARTLY SUPERSEDED — 2026-08-24
> **The pod-count recommendation in this file is WRONG.** It says "Design target: 5 pods."
> The current decision is **Core = 2 pods (both tibias)**, with 3/5/7 as an opt-in customer
> ladder. See `DECISIONS.md` D3 and `research/bom-and-pricing.md` §3.
>
> **Still valid and useful here:** the hybrid compute split (pods collect, phone infers),
> the BLE throughput data, flash sizing, and the IMU placement-error tables.


**Researched 2026-08-23.** Supersedes the "3 pods, edge-first" decisions in `CLAUDE.md`.

Two decisions changed based on evidence:
1. **Sensor count: optimize for trustworthy joint data, then cost — not for the minimum.**
2. **Compute: hybrid. Pods collect and stream. The phone infers.**

---

## 1. Sensor Count — Reframed

The old framing was "what is the fewest sensors that works?" (Paper 1's 3-IMU config).
The better framing: **what is the fewest sensors that produces joint data we can defend?**

Paper 1's 3-sensor config achieves R²=0.91 for *spatiotemporal gait parameters* — cadence,
GCT, vertical oscillation, stride, asymmetry. It does **not** give joint angles. Lumbar +
two ankles has no sensor on the thigh or shank, so knee and hip angles are unobserved and
can only be inferred through a model.

### What each tier actually buys you

| Pods | Placement | What you get | What you cannot get |
|---|---|---|---|
| 1 | Lumbar (L5/S1) | Cadence R²=0.99, VO R²=0.96, GCT R²=0.95 | Any asymmetry. Blind. |
| 3 | Lumbar + both ankles | + asymmetry, foot-ground events, per-limb GCT | Knee/hip joint angles |
| **5** | **+ both shanks (mid-lateral)** | **+ knee flexion, tibial acceleration directly** | Hip rotation, trunk lean detail |
| **7** | **+ both thighs (lower anterior)** | **Full lower-limb joint kinematics** | Upper body |

### The measured accuracy of an optimized set
From the IMU placement optimization study (11 placements, 7 participants, all combinations
tested against motion capture):

**Recommended 4-sensor lower-limb configuration: sacrum + lower anterior thigh + lower
lateral shank + heel.** Errors across all movements:

| Joint | RMSE |
|---|---|
| Ankle | 3.90° |
| Knee | 6.35° |
| Hip | 5.93° |

Best individual pairings: knee via mid-lateral-shank + lower-anterior-thigh (bias 0.08°
during turning); ankle via mid-lateral-shank + dorsal-foot (RMSE 2.33°).

Worst placements in the same study: knee 9.31° (shin + lower lateral thigh), hip 21.46°
(L4-L5 + lower posterior thigh). **Placement choice matters more than sensor count** —
a badly placed 7-pod system is worse than a well-placed 5-pod system.

Note that config is *unilateral*. Bilateral (which we need for asymmetry) doubles the limb
sensors: sacrum + 2 thighs + 2 shanks + 2 feet/ankles = **7 pods**.

### Sparse-IMU deep learning: 6 sensors, full body
Deep Inertial Poser (DIP) and successors reconstruct full-body SMPL pose in real time from
**6 IMUs** (lower arms, lower legs, back, head). FDIP reports 250% faster inference and 16%
lower angular error than prior SOTA. For our purposes the lower-body subset matters, but it
confirms 5–7 well-placed sensors is the regime where full kinematics becomes tractable.

### Reference errors for context
| Method | Running joint-angle error |
|---|---|
| Self-placed IMU + ML | 3.4° at 5 mph |
| 3-DOF knee, IMU | 1.6°–5.9° RMSE |
| Markerless video | 4.1° |
| Optimized IMU set | 3.9°–6.4° |

**Everything sits in the 3–6.5° band.** That is the physical floor for body-worn sensing,
and it drives the threshold problem in §8 of `predictive-validity.md`.

### Recommendation

**Design target: 5 pods. Architecture that scales to 7.**

- **5-pod core (lumbar + 2 shanks + 2 feet/ankles):** gets asymmetry, per-limb GCT, direct
  tibial acceleration (the one loading variable that is directly measured rather than
  inferred), and knee flexion via shank-thigh substitute modeling. Tibial accel matters —
  it is measured at the tibia, not derived from a GRF proxy that `predictive-validity.md`
  §2 shows is uncorrelated with actual bone load.
- **7-pod full (+2 thighs):** full lower-limb joint kinematics at published accuracy.
  Sell as a pro/clinical tier or a research SKU.
- **3-pod is now the *entry* tier**, not the product. It gives spatiotemporal metrics and
  asymmetry only — a legitimate running product, but not "trustworthy joint data."

Cost optimization happens *after* fixing the count, per the user's directive. See
`buyer-and-liability.md` for why subscription pricing makes a 5–7 pod BOM survivable in a
way that $35 hardware sales never could.

**Open question (P1.2.7):** thigh and shank pods sit on large soft-tissue masses. Soft
tissue artifact during running is a known error source and is worse there than at the
sacrum or the shank's medial border. Needs measurement before committing to 7.

---

## 2. Compute Architecture — Hybrid Confirmed

The user's instinct is correct and the bandwidth numbers support it.

### BLE capacity (measured, from commercial IMU systems)
| Sensors on one link | Max sustained rate |
|---|---|
| 1–2 | 400 Hz |
| **3–6** | **200 Hz** |
| 7–12 | 100 Hz |

**A 5-pod system streaming raw 6-DOF at 200 Hz to a phone is inside the envelope.** A
7-pod system at 200 Hz is at or slightly past it — either drop to 100–150 Hz for the thigh
pods (joint angle does not need 200 Hz; foot-strike event detection does), or accept
7 pods at 100 Hz, or split across two links.

Throughput depends on PHY mode, Data Length Extension, ATT MTU, and connection interval —
all tunable on nRF52/nRF53. Assume 2M PHY + DLE + MTU 247 and the numbers above hold.

### Division of labour

**On the pod (minimal):**
- IMU sampling at fixed rate with hardware timestamping
- Sensor fusion to orientation *only if* it reduces bytes on the wire (quaternion is 4
  floats vs 6 for raw accel+gyro — but raw is more useful for us; prefer raw)
- Ring buffer + flash spill for BLE dropouts (non-negotiable — dropouts will happen)
- Time sync across pods
- Haptic driver
- **No ML inference**

**On the phone (everything else):**
- Multi-pod time alignment
- Sensor-to-segment calibration
- Gait event detection, joint angle estimation
- Baseline modeling, degradation detection
- Feedback generation and cue timing

**Rationale beyond raw compute:** the ARION RCT killed 47% of its dropouts through app
malfunctions. Every algorithm on the pod is one you cannot fix without an OTA firmware
campaign across N pods. Every algorithm on the phone ships in an app update. **For a
pre-product-market-fit system, iteration speed on the model is worth more than
architectural elegance.** Move logic to the pod later, once the model stops changing.

### Latency budget — recheck what actually needs speed
The old <200 ms edge requirement came from Paper 2, not from a user need.

| Event | Timescale | Needs edge? |
|---|---|---|
| ACL rupture | ~50 ms | **Cannot be alerted before it happens. Irrelevant.** |
| Gait cue ("increase cadence") | seconds — must land within a few strides | No. BLE round trip ~20–100 ms. Fine. |
| Fatigue degradation | minutes | No. |
| Session summary | post-hoc | No. |

**Nothing in the actual product needs sub-200 ms on-device inference.** The requirement was
inherited from a paper. Dropping it removes the MCU-class, power, battery, and BOM pressure
that was driving the hardest hardware constraints.

### Team scale — a hub is required, confirm later
25 athletes × 5 pods = **125 concurrent BLE devices.** No phone handles that. Options:

1. **Per-athlete phone → cloud/coach tablet.** Zero new hardware. Requires every athlete to
   carry a phone in practice. Fine for HS/college, awkward in-game.
2. **Dedicated hub** (multi-radio, e.g. several nRF52840 or an nRF5340 + companion radios,
   or 2.4 GHz proprietary instead of BLE). Handles the many-to-one problem properly.
3. **Store-and-forward.** Pods log to flash, sync at the charging dock. Kills real-time
   coaching but is trivially reliable — and note that for the *team* market, post-session
   may be sufficient given the real-time claim is the weakest one anyway.

**Decide when we have a team customer.** Do not build the hub speculatively. The individual
runner product (v1) needs only path 1.

### Flash sizing for store-and-forward
5 pods × 6 channels × 2 bytes × 200 Hz = 12 kB/s per pod. A 4-hour session = ~173 MB per
pod raw. With simple delta+LZ compression (typically 3–5× on IMU streams) → ~35–60 MB.
**A 128 MB QSPI flash per pod covers a session uncompressed-ish; 64 MB covers it
compressed.** Cheap either way. Log everything — this data is the moat.

---

## 3. Revised Hardware Decisions

| Decision | Old | New | Why |
|---|---|---|---|
| Pod count | 3 (fixed) | 5 core / 7 full / 3 entry | 3 gives no joint angles |
| Edge ML | Required, <200 KB, <200 ms | **Removed from v1** | No use case needs it; costs BOM and iteration speed |
| Pod role | Inference node | **High-rate collection + reliable transport** | Matches user's directive |
| Sampling | 200 Hz all pods | 200 Hz distal, 100–150 Hz proximal | BLE budget; joint angle needs less than event detection |
| Flash | Unsized | 64–128 MB per pod | Log raw always — data is the asset |
| MCU | nRF52840 / ESP32-S3 for ML | nRF52840 class is now over-spec'd but keep it | BLE 2M PHY + DLE maturity; headroom is cheap |
| Hub | Assumed needed | Deferred until a team customer exists | Individual v1 does not need it |

---

## Sources
- IMU placement optimization (11 sites, all combinations) — https://pmc.ncbi.nlm.nih.gov/articles/PMC7660215/
- Deep Inertial Poser (6 sparse IMUs) — https://arxiv.org/html/1810.04703
- Faster Deep Inertial Pose (FDIP) — https://pmc.ncbi.nlm.nih.gov/articles/PMC9573697/
- BLE multi-sensor IMU throughput — https://qsense-motion.com/support/frequently-asked-questions/
- BLE throughput optimization (PHY/DLE/MTU/interval) — https://punchthrough.com/ble-throughput-optimization-faq/
- BLE for motion capture feasibility — https://www.sciencedirect.com/science/article/pii/S1084804522002077
- Knee angle misalignment error — https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9697725/
- Self-placed IMU real-time joint angles — https://www.sciencedirect.com/science/article/pii/S0966636225000281
