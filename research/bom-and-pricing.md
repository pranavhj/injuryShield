# BOM, Volume Pricing, and the Pod Ladder

**Built 2026-08-24.** Supersedes the estimated cost base in `unit-economics.md` §1 with
component-level pricing from actual distributor listings.

Manufacturing assumption: **China sourcing and PCBA, India for assembly/logistics where
useful.** No US production cost assumed.

**All figures are distributor list prices or published factory ranges. Real quotes vary —
Chinese injection-molding quotes for the same part vary by more than 2× between the cheapest
and most expensive quartile. Treat as ±30% until quoted.**

---

## 0. The Reframe That Should Drive This

> *"The main problem we are solving is not the hardware, it's the ease of use."*

This is correct and it is supported by everything in the research so far:

- **ARION RCT:** 47% of dropouts were caused by **app malfunctions**. Top control-group
  dropout reason: *"I don't understand the feedback."* Not sensor accuracy. Software and
  comprehension.
- **NURVV:** died with 16 sensors and good hardware. The post-mortem is about the app
  contradicting itself, incoherent training plans, and coaching that contradicted running
  science.
- **GSSI Tokyo 2020:** a full multi-sensor Olympic deployment produced data on **2 athletes**
  because setup friction beat it.
- **SlimeVR already sells 5–6 body IMU trackers for $219.** If cheap body-worn IMU hardware
  were the product, it would already exist. It does exist. It is not the product.

**Consequence for this document: the pod should be as cheap as is consistent with
trustworthy data, because the pod is not where the value or the difficulty lives.** Do not
over-spend on the IMU chasing specs that do not change the analysis. Spend the saved money
and effort on setup time, auto-detection, and feedback that a runner understands.

---

## 1. Component Selection — Real Prices

### IMU — the one part worth thinking about

| Part | Price (LCSC / community) | Notes |
|---|---|---|
| **LSM6DSV16X** (ST) | **$2.88** | Triple-channel architecture, embedded **Machine Learning Core**, built for wearables. Strong candidate. |
| **ICM-45686** (TDK) | **~$6.70** | SlimeVR community's top pick: *"Best currently available. Reliable, accurate, stays accurate longest."* |
| LSM6DSR (ST) | ~$3.35 | Affordable, shorter drift-free window |
| BMI270 (Bosch) | **$1.79** | Cheapest. SlimeVR rates it a **poor performer** for drift. |
| ICM-42688-P (TDK) | $8.00–13.34 | Lowest noise density (2.8 mdps/√Hz) but expensive and needs a clean 3.3V LDO |

**Important nuance on the SlimeVR rankings.** Their criterion is *orientation drift over
hours*, because VR full-body tracking integrates gyro continuously. **Our use case is
different**: per-stride event detection and peak tibial acceleration are short-window,
mostly accelerometer-driven measurements where slow gyro drift matters far less. A chip
SlimeVR calls "poor" may be entirely adequate for us.

**Recommendation: LSM6DSV16X at $2.88.** It is a genuinely high-quality part built for this
exact application, a third the price of the ICM-45686, and its embedded ML core is a real
asset later. **Buy 10 of each of LSM6DSV16X, ICM-45686 and BMI270 and measure them on the
actual task before committing** — that is a ~$120 experiment that could swing $5/pod at
scale, and it answers the question with our data rather than VR gamers' data.

### MCU — module vs bare chip is the big cost fork

| Option | Price | Certification burden |
|---|---|---|
| **nRF54L15-QFAA-R** bare chip | **$2.55** (LCSC) | Full RF design + FCC/CE: **~$20–30k one-time** |
| **BL54L15** pre-certified module | **$8.11 @ 1k** | Product-level testing only: ~$3–5k |
| nRF52840 bare chip | ~$4–5 | Same as above |
| nRF52840 module (Fanstel BM840) | $4.76 @ 1k | Pre-certified |

**nRF54L15 is the right silicon going forward** — Cortex-M33 at 128 MHz (2× the 52840),
1.5 MB memory, sub-1 µA sleep, 22 nm. Community guidance: *"pick the 54L15 for anything
shipping past 2026."* No USB, which we do not need.

**The fork:** at 1,000 units, amortising $25k of certification is **$25/pod** — the module
wins by a mile. At 20,000 pods it is $1.25/pod and the bare chip wins. **Use a
pre-certified module until roughly 5,000 pods, then switch.** Design the PCB so the swap is
a drop-in from day one.

### Everything else

| Part | ~100 units | ~1,000 | ~10,000 |
|---|---|---|---|
| Flash (W25Q128, 16 MB) | $1.20 | $0.90 | $0.70 |
| LiPo cell, ~100 mAh | $2.50 | $1.50 | $1.10 |
| Charge IC (BQ25100 or CN equivalent) | $0.80 | $0.35 | $0.25 |
| LRA haptic + driver | $2.00 | $1.40 | $1.00 |
| PCB, 4-layer, ~20×25 mm | $2.00 | $0.80 | $0.40 |
| Passives, crystal, antenna, pogo pins | $3.00 | $2.00 | $1.40 |

### Enclosure — the sleeper cost

Published China factory data:
- Single-cavity prototype mould: **$1,000–3,000**
- Multi-cavity production tooling: **$5,000–15,000+**
- Piece price at 1k units: **$2.50–6.00** for commodity resin
- **3D print → injection moulding crossover is ~300–500 units** with a $3,000 aluminium mould

IP68 sealing adds cost — ultrasonic welding or overmoulding, plus a gasket. Budget an extra
$0.50–1.00/pod at volume and expect tooling toward the upper end.

---

## 2. Cost Per Pod, Three Volume Tiers

| Line | **100 units** | **1,000 units** | **10,000 units** |
|---|---|---|---|
| MCU | $10.00 (module) | $8.11 (module) | $3.25 (bare + amortised cert) |
| IMU (LSM6DSV16X) | $2.88 | $2.20 | $1.80 |
| Flash | $1.20 | $0.90 | $0.70 |
| Battery | $2.50 | $1.50 | $1.10 |
| Charge IC | $0.80 | $0.35 | $0.25 |
| Haptic + driver | $2.00 | $1.40 | $1.00 |
| PCB | $2.00 | $0.80 | $0.40 |
| Passives, pogo, antenna | $3.00 | $2.00 | $1.40 |
| Enclosure | $8.00 (3D print) | $2.70 (mould amortised) | $1.30 |
| **Components** | **$32.38** | **$19.96** | **$11.20** |
| Assembly, test, yield loss | $8.00 | $3.50 | $2.00 |
| **Factory gate per pod** | **≈ $40** | **≈ $23.50** | **≈ $13.20** |
| Freight, duty, warranty, returns (+22%) | $9 | $5 | $3 |
| **Landed cost per pod** | **≈ $49** | **≈ $29** | **≈ $16** |

**Sanity check:** a published Fitbit Air teardown puts factory gate at $20–22 for a *more*
complex device (PPG, SpO2, skin temp, band) at 8–12 million units/year. Our $13.20 at 10k
for a simpler device is plausible but optimistic — treat $15–17 as the realistic scale
figure.

**Tariff note:** China-made goods sold into the US carry Section 301 tariffs; the +22%
landed uplift assumes this. Selling into India or Europe from China changes that line.

---

## 3. The Pod Ladder — What Each Tier Actually Buys

The tiered idea is good product architecture. Each step must add a **nameable capability**,
and the app must **state what is missing** at each tier rather than silently degrading.

| Tier | Pods | Placement | What it adds | What is still missing |
|---|---|---|---|---|
| **Core** | **2** | Both tibias | **Peak tibial acceleration (bilateral), per-limb ground contact time, impact asymmetry, cadence, stride.** *This is the RCT-validated configuration.* | Joint angles, trunk, hip |
| **Plus** | **3** | + sacrum / L5 | Trunk kinematics, vertical oscillation, pelvic drop proxy, centre-of-mass motion. *Paper 1's config.* | Knee and hip angles |
| **Pro** | **5** | + both thighs | **Knee flexion angle** (thigh–shank pair, best-case bias 0.08°), hip angle estimate | Ankle/foot angle precision |
| **Full** | **7** | + both feet | **Ankle dorsi/plantarflexion, foot strike angle, full lower-limb chain** | Upper body |

**The honest framing for customers, which is also the honest framing internally:** the
2-pod Core tier is not a cut-down version. **It is the configuration the evidence actually
validated.** Tiers 3–7 add measurement richness that is scientifically interesting and
commercially attractive but is *not* what the 62% injury-reduction result was built on.

Selling it that way is both more truthful and better positioning: *"Core does the thing
that's proven. Higher tiers add detail for people who want it."*

---

## 4. Kit Pricing Ladder

At the **1,000-unit tier ($29 landed per pod)**, plus shared items (dock slots ~$5/pod,
straps ~$2/pod, packaging ~$4/kit):

| Tier | Pods | Kit COGS | Retail @ ~3× | Suggested price |
|---|---|---|---|---|
| Core | 2 | $76 | $228 | **$249** |
| Plus | 3 | $110 | $330 | **$349** |
| Pro | 5 | $184 | $552 | **$549** |
| Full | 7 | $256 | $768 | **$749** |

At the **10,000-unit tier ($16/pod)**, COGS falls to $46 / $67 / $111 / $155 — the same
retail prices yield 81–79% gross margin, or prices can drop to $199 / $279 / $429 / $579
while holding ~65–73%.

**Why ~3×:** consumer hardware needs the multiple to absorb CAC ($50–150), support, returns,
channel margin if any, and warranty. At 2× you have no room for CAC. Playermaker sells at
$249 including a year of app access, which anchors the Core tier exactly.

### The competitive reality check
**SlimeVR sells 5–6 body IMU trackers for $219** — roughly $40/tracker retail, against our
$110/pod. They achieve it with cheap IMUs, hobbyist enclosures, community support, and
near-zero margin expectations.

**This means "pods on your body" cannot be the value proposition.** A price of $549 for our
5-pod Pro tier against $219 for SlimeVR's set is only defensible because of the programme,
the validated protocol, the analysis, and the app — never because of the hardware. If a
customer is comparing on hardware alone, we lose that comparison and should not be in it.

---

## 5. What To Buy For Testing — Build Nothing Yet

Three real options, all cheaper than building.

### Recommended: 2 × mbientlab MetaMotionS — **$260**
| Spec | Value |
|---|---|
| Price | **$129.99–136.99** each; bulk discounts available |
| IMU | BMI270 6-axis + BMM150 mag + BMP280 baro + Bosch 9-axis fusion |
| **Logging** | **1–400 Hz to onboard flash** — no BLE bandwidth limit |
| Streaming | 1–100 Hz |
| Storage | **512 MB NAND, ~100M timestamped entries** |
| Battery | 100 mAh LiPo, USB rechargeable |
| Data out | **CSV, or JSON via Python / C++ / Java / JavaScript / Swift SDKs** |

**Why this first:** it replicates the RCT-validated 2-tibia configuration exactly, logs at
400 Hz with timestamps to onboard flash (so no BLE throughput problem at all), and exports
CSV with a mature Python SDK. **You can run the published field protocol next week with
zero firmware written.** It is also research-validated — MetaMotion IMUs have been assessed
for concurrent validity against optical motion capture.

Note it uses the BMI270, the chip SlimeVR rates poorly. For our short-window measurements
that is probably fine — **and finding out whether it is fine is itself a useful result**,
since BMI270 is the $1.79 option.

### For exploring the 3/5/7 ladder: SlimeVR V1.2 — **from $219**
Open source (MIT / Apache 2.0), a full set of trackers, straps and charging already solved,
10–15 hour battery, and firmware you are legally and practically free to modify. **Far
cheaper per node than $130 research sensors** — 7 MetaMotionS would be ~$900.

Use it to answer the ladder questions: does adding a sacrum pod change the analysis
usefully? Do thigh pods survive soft-tissue artifact while running? What does 7-pod don/doff
actually cost in seconds? Data quality is lower, but these are *architecture* questions, not
precision questions.

### Do not buy: Movella / Xsens
**$8,500 hardware plus $13,500/year software** for a full system. Individually the DOT is
~$200+/sensor with a software subscription. Research-grade and excellent, but it buys
nothing at this stage that MetaMotionS does not.

### Suggested spend
| Item | Cost |
|---|---|
| 2 × MetaMotionS (the validated protocol) | $260 |
| 1 × SlimeVR set (ladder exploration) | $219 |
| IMU sample pack — 10 each of LSM6DSV16X, ICM-45686, BMI270 | ~$120 |
| **Total** | **≈ $600** |

**Under $600 answers the sensor-selection question, the pod-ladder question, and the K2
wear-test question — with no PCB, no firmware, and no tooling.**

---

## 6. What This Tells Us About The Business

1. **Pod cost is not the constraint.** At $29 landed (1k) and $16 (10k), a 7-pod kit lands
   at $256 COGS against $749 retail. The hardware economics work across the whole ladder.
2. **The old $35/pod retail target was impossible; $110/pod retail is comfortable.** The
   original constraint was self-imposed by targeting school budgets that
   `buyer-and-liability.md` §1 shows do not exist anyway.
3. **Certification, not components, is the volume cliff.** $25k of FCC/CE is $25/pod at
   1,000 units and $1.25 at 20,000. Use a pre-certified module until ~5,000 pods.
4. **Tooling is the other cliff.** Stay on 3D-printed enclosures below ~300–500 units.
5. **The differentiation budget is large.** Roughly $150–200 of gross margin per Core kit is
   available to spend on the thing that actually matters — setup time, auto-detection of pod
   position, and feedback a runner understands. **That is where the money should go**, and
   it is the one place SlimeVR, NURVV and Athos all failed.

---

## Sources
- [LSM6DSV16X on LCSC](https://www.lcsc.com/product-detail/C5267406.html) · [ST product page](https://www.st.com/en/mems-and-sensors/lsm6dsv16x.html)
- [BMI270 on LCSC](https://www.lcsc.com/product-detail/C2836813.html) · [ICM-42688-P on LCSC](https://www.lcsc.com/product-detail/C1850418.html)
- [SlimeVR IMU comparison — community field data](https://docs.slimevr.dev/diy/imu-comparison.html)
- [nRF54L15 on LCSC](https://www.lcsc.com/product-detail/C42458750.html) · [nRF54L15 vs nRF52840](https://hubble.com/community/comparisons/nrf54l15-vs-nrf52840-what-changes-in-power-and-architecture-and-tooling/)
- [Fanstel nRF52840 modules](https://www.fanstel.com/bm840)
- [China injection molding tooling cost data](https://www.haizol.com/blog/injection-molding-tooling-cost-china) · [Low-volume molding crossover](https://www.haizol.com/blog/low-volume-injection-molding)
- [JLCPCB PCBA cost breakdown](https://jlcpcb.com/blog/pcba-cost-breakdown)
- [mbientlab MetaMotionS](https://mbientlab.com/store/metamotions/)
- [SlimeVR](https://slimevr.dev/) · [SlimeVR on Crowd Supply](https://www.crowdsupply.com/slimevr/slimevr-full-body-tracker)
- [Fitbit Air BOM benchmark](https://the5krunner.com/2026/05/15/fitbit-air-cost-breakdown/)
