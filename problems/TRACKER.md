# InjuryShield — Master Problem Tracker

Every identified problem, question, and decision point. Each can be exploded into its own deep-dive.
Status: [ ] Open | [~] In Progress | [x] Resolved | [?] Needs Research | [!] Blocked

---

## P1: HARDWARE — Pod Design

### P1.1: Form Factor & Weight
- [ ] **P1.1.1** Target weight per pod? Fitbit Air is ~10g (screenless). Xsens DOT is 11.2g. KINEXON is 15g. Our target: <15g.
- [ ] **P1.1.2** Pod dimensions — coin-sized? Pebble-shaped? Must not restrict joint movement.
- [ ] **P1.1.3** Enclosure material — must be waterproof (IP68 like Xsens DOT), sweat-resistant, skin-safe.
- [ ] **P1.1.4** No sharp edges or hard protrusions (regulatory requirement for competition use).
- [ ] **P1.1.5** Research Fitbit Air teardown — what's inside that makes it so small? Can we match that BOM?

### P1.2: Sensor Selection
- [x] **P1.2.1** What sensors needed? **RESOLVED: 3-axis accelerometer + 3-axis gyroscope (6-DOF IMU) minimum. Magnetometer optional.**
- [x] **P1.2.2** Sampling rate? **RESOLVED: 200Hz for running, 400Hz for cutting sports. Gyroscope rate matters more than accelerometer.**
- [ ] **P1.2.3** Specific IMU chip selection — BMI270? ICM-42688? LSM6DSO? Compare: accuracy, power, size, cost, availability.
- [ ] **P1.2.4** Do we need a barometric pressure sensor? (vertical oscillation accuracy)
- [ ] **P1.2.5** EMG: Paper 2 used sEMG for 92.3% accuracy. IMU-only accuracy? Is the delta worth the complexity of skin-contact electrodes?
- [ ] **P1.2.6** Temperature sensor? (skin temp correlates with fatigue — Fitbit Air has one)

### P1.3: Battery & Power
- [ ] **P1.3.1** Target battery life per charge? Xsens DOT gets 8hr from 70mAh. We need at least 4-6 hours (full practice session).
- [ ] **P1.3.2** Battery chemistry — LiPo? Coin cell? Weight vs capacity tradeoff.
- [ ] **P1.3.3** Charging method — USB-C? Magnetic pogo pins (like Fitbit/WHOOP)? Wireless Qi?
- [ ] **P1.3.4** Charging 3 pods simultaneously — do we need a charging dock? Individual cables = friction.
- [ ] **P1.3.5** Fast charge capability? Fitbit Air: 5 min = 1 day. Can we do similar?
- [ ] **P1.3.6** Power budget calculation: IMU at 200Hz + BLE + ML inference — what does total draw look like?

### P1.4: MCU / Processing
- [x] **P1.4.1** Edge ML requirement confirmed: <200KB model, <200ms inference latency.
- [ ] **P1.4.2** MCU selection — nRF52840? ESP32-S3? STM32WB? Compare: ML capability, BLE, power, cost.
- [ ] **P1.4.3** TinyML framework — TensorFlow Lite Micro? Edge Impulse? CMSIS-NN?
- [ ] **P1.4.4** Does each pod run its own ML model, or do pods stream raw data to a "brain" pod?
- [ ] **P1.4.5** Inter-pod communication — BLE mesh? Proprietary protocol? Latency requirements between pods.
- [ ] **P1.4.6** On-pod storage for session data — flash memory size needed for a 4-hour session at 200Hz?

### P1.5: Communication
- [ ] **P1.5.1** Pod-to-pod: need synchronized timestamps across 3 pods. BLE mesh? ANT+? Proprietary 2.4GHz?
- [ ] **P1.5.2** Pod-to-phone: BLE 5.x for session sync and detailed analytics
- [ ] **P1.5.3** Pod-to-coach-display: real-time alert forwarding. How does coach receive the alert?
- [ ] **P1.5.4** Multi-athlete: if 25 players each have 3 pods = 75 concurrent BLE devices. Can the system handle this?

---

## P2: HARDWARE — Attachment & Form Factor

### P2.1: Hybrid Approach (Snap-on Pod)
- [ ] **P2.1.1** Snap/magnetic mechanism design — must be secure during sprinting, cutting, jumping. Must not detach on impact.
- [ ] **P2.1.2** Magnetic vs snap-fit vs velcro comparison. Research: US Patent 9,872,525 (snap pod to apparel). WHOOP uses velcro.
- [ ] **P2.1.3** Apparel attachment points — where on compression wear do pods snap? Lower back, both ankles.
- [ ] **P2.1.4** Strap attachment — for users who don't want our apparel. Adjustable elastic strap with pod dock?
- [ ] **P2.1.5** Shoe clip option — for ankle pods, can they clip to shoe laces or heel collar instead of strap?

### P2.2: Apparel Design
- [ ] **P2.2.1** What garments? Compression shorts (back pod)? Ankle sleeves? Shin guards (for soccer)?
- [ ] **P2.2.2** Pod pocket/dock design in fabric — must maintain sensor-to-skin proximity without embedding electronics
- [ ] **P2.2.3** Washability: since electronics are REMOVABLE, apparel is just normal compression fabric. Fully washable. Key advantage over Athos/formsense.
- [ ] **P2.2.4** Sizing: how many sizes? Compression wear must be snug or sensors move. S/M/L/XL minimum.
- [ ] **P2.2.5** Apparel material selection — moisture-wicking, compression, durable. Partnership with existing sportswear manufacturer?
- [ ] **P2.2.6** Cost to manufacture apparel with snap docks vs cost of straps alone.

### P2.3: Comfort & Compliance
- [ ] **P2.3.1** Will athletes actually wear ankle sensors during games? Research: Olympic athletes refused multi-point sensors.
- [ ] **P2.3.2** Strap tightness: too tight = restrictive, too loose = bad data. How to guide users?
- [ ] **P2.3.3** Pod protrusion: does a 11mm thick pod on the ankle cause discomfort against shoes?
- [ ] **P2.3.4** User testing plan: founder runs with 3 prototype pods for 30 days. Log comfort, issues, failures.
- [ ] **P2.3.5** Sock-over-pod approach: ankle pods under socks — does this affect data quality? Movement?

---

## P3: SOFTWARE — ML Models & Algorithms

### P3.1: Injury Risk Models
- [ ] **P3.1.1** What models replicate Paper 1's results (3-sensor, <200KB)? CNN? LSTM? Random Forest?
- [ ] **P3.1.2** Training data: where do we get labeled injury-risk data? Public datasets? Partnerships with universities?
- [ ] **P3.1.3** Sport-agnostic vs sport-specific models — same pod hardware, different firmware/model per sport?
- [ ] **P3.1.4** Fatigue detection model: track declining metrics over session duration. Simpler than acute biomechanical risk.
- [ ] **P3.1.5** What's the false positive rate we can tolerate? Too many alerts = coaches ignore them. Too few = missed injuries.
- [ ] **P3.1.6** Personalization: do models need per-athlete baseline calibration? How long does baseline take?

### P3.2: Calibration & Setup
- [x] **P3.2.1** Auto-calibration is possible (Paper 8 — motion-driven, no poses needed). **Key advantage.**
- [ ] **P3.2.2** Sensor-to-segment alignment: how do we know which way the pod is oriented on the body?
- [ ] **P3.2.3** Left/right ankle identification: must auto-detect which pod is on which ankle.
- [ ] **P3.2.4** Calibration drift during session: does sensor slip on sweaty skin? How to detect and compensate?
- [ ] **P3.2.5** First-use setup flow: pair pods to app, assign positions, collect 30s of walking baseline?

### P3.3: Alert System
- [ ] **P3.3.1** Alert types: haptic buzz on pod? Sound? Push notification to coach's phone/tablet?
- [ ] **P3.3.2** Alert granularity: binary (safe/risk) or graduated (green/yellow/red)?
- [ ] **P3.3.3** Alert latency budget: <200ms total (sensor → inference → alert). Is on-pod haptic the fastest?
- [ ] **P3.3.4** How to communicate WHICH player and WHAT risk to coach during practice with 25 players?
- [ ] **P3.3.5** False alarm handling: snooze? Recalibrate? Manual override?

### P3.4: Data Pipeline & Analytics
- [ ] **P3.4.1** On-pod: real-time inference + alert. Post-session: sync raw data to phone/cloud for deep analysis.
- [ ] **P3.4.2** Session storage: 200Hz * 6-DOF * 3 pods * 4 hours = how much data? Flash sizing.
- [ ] **P3.4.3** Cloud analytics dashboard: team view, individual athlete trends, injury risk history.
- [ ] **P3.4.4** Data export: CSV, API, integration with existing platforms (Catapult, TrainingPeaks, Strava)?
- [ ] **P3.4.5** Available open-source code/libraries for sports biomechanics ML? OpenSim? Biomechanical ToolKit?

---

## P4: BUSINESS — Viability & Go-to-Market

### P4.1: Pricing & Business Model
- [ ] **P4.1.1** Pod cost target: <$35 per pod (user requirement for school market). BOM estimation needed.
- [ ] **P4.1.2** 3-pod kit price: <$105 for hardware. Subscription for analytics?
- [ ] **P4.1.3** Revenue model: hardware sale + freemium app (basic metrics free) + premium subscription (injury risk, team dashboard)?
- [ ] **P4.1.4** Ecosystem pricing: pods + apparel + app + team dashboard. Buy parts or whole.
- [ ] **P4.1.5** Is $35/pod realistic? Xsens DOT is ~$200. Fitbit Air is $100 (but mass production + Google). What's our BOM?
- [ ] **P4.1.6** Subscription tiers: individual free → team basic ($X/month) → team pro ($Y/month)?

### P4.2: Target Market & GTM
- [ ] **P4.2.1** V1 market: individual runners/athletes. Self-dogfood first.
- [ ] **P4.2.2** V2 market: high school/college programs. ~30,000 college sports programs in US. Price-sensitive.
- [ ] **P4.2.3** V3 market: pro training staff. Sell alongside existing Catapult/STATSports.
- [ ] **P4.2.4** V4 market: in-game use (requires league approval). Long-term.
- [ ] **P4.2.5** Geographic: US market first (USD revenue). India as manufacturing/engineering base?
- [ ] **P4.2.6** Channel: direct-to-consumer? Through athletic directors? Team equipment distributors?

### P4.3: Manufacturing
- [ ] **P4.3.1** PCB design and assembly: Shenzhen partners? Local US PCBA for prototypes?
- [ ] **P4.3.2** Enclosure: injection molding for mass production. 3D print for prototypes.
- [ ] **P4.3.3** Apparel manufacturing: partner with existing compression wear brand or manufacture in India?
- [ ] **P4.3.4** MOQ (minimum order quantity): what volume makes $35/pod feasible?
- [ ] **P4.3.5** Supply chain: chip availability for chosen IMU + MCU combination?

### P4.4: IP & Legal
- [ ] **P4.4.1** Freedom to operate: do existing patents block our snap-on pod + edge ML approach?
- [ ] **P4.4.2** Key patents to review: US 9,872,525 (snap pod to apparel), US 12,011,257 (formsense injury biofeedback)
- [ ] **P4.4.3** Patent strategy: file provisional patent for our specific approach?
- [ ] **P4.4.4** Open-source strategy: what to open-source (firmware? ML models?) vs proprietary (algorithms? hardware design?)
- [ ] **P4.4.5** Data privacy compliance: GDPR (Europe), COPPA (US minors in youth sports), state privacy laws

---

## P5: USER EXPERIENCE

### P5.1: Setup & Onboarding
- [ ] **P5.1.1** Unboxing to first session: target <5 minutes total.
- [ ] **P5.1.2** Pod pairing: NFC tap? BLE auto-detect? QR scan?
- [ ] **P5.1.3** Position assignment: how does the app know which pod is back/left-ankle/right-ankle? Auto-detect from movement pattern? Color coding?
- [ ] **P5.1.4** Baseline collection: how many minutes of walking/running needed for personalized baseline?
- [ ] **P5.1.5** Multi-athlete team setup: onboarding 25 players with 3 pods each = 75 devices. Must not take an hour.

### P5.2: During Session
- [ ] **P5.2.1** Coach's view: tablet/phone dashboard showing all players, color-coded risk levels?
- [ ] **P5.2.2** Alert delivery: does coach get a ping per player, or aggregate "2 players in yellow zone"?
- [ ] **P5.2.3** What does the athlete feel? Subtle vibration? Distinct buzz pattern for "take a break"?
- [ ] **P5.2.4** Can athlete dismiss/snooze alerts? Or coach-only control?
- [ ] **P5.2.5** Battery status during session: how does coach know if any pod is dying mid-practice?

### P5.3: Post-Session
- [ ] **P5.3.1** Auto-sync when pods return to charging dock?
- [ ] **P5.3.2** Session summary: what happened, which athletes flagged, trends over time
- [ ] **P5.3.3** Shareable reports for parents (youth sports) or team doctors?
- [ ] **P5.3.4** Integration with existing workflows: Catapult users want InjuryShield data IN their OpenField dashboard

---

## P6: SPORT-SPECIFIC CONSIDERATIONS

### P6.1: Hardware Consistency
- [x] **P6.1.1** Decision: Keep hardware sport-agnostic. Same 3 pods for all sports. **Sport-specific ML models, not hardware.**
- [ ] **P6.1.2** Ankle pod placement: same for running vs soccer vs basketball? Or different optimal positions?
- [ ] **P6.1.3** Contact sports (football, rugby): pods must survive collisions. Durability testing needed.
- [ ] **P6.1.4** Swimming/water sports: IP68 rating sufficient? Completely different biomechanics model needed.

### P6.2: Sport-Specific Models
- [ ] **P6.2.1** Running: gait asymmetry, ground contact time, stride changes, cadence drift, vertical oscillation
- [ ] **P6.2.2** Basketball: landing mechanics, knee valgus on deceleration, cumulative jump load
- [ ] **P6.2.3** Soccer/Football: cutting deceleration, hamstring load, groin strain indicators
- [ ] **P6.2.4** Baseball: arm slot tracking (forearm pod instead of ankle?), pitch count fatigue
- [ ] **P6.2.5** American Football: deceleration forces, non-contact ACL risk, cumulative impact load
- [ ] **P6.2.6** Do we need DIFFERENT pod placements per sport? (e.g., forearm for pitchers instead of back?)

---

## P7: REGULATORY PATHWAY

- [ ] **P7.1** Phase 1: Training market — no approval needed. Start here.
- [ ] **P7.2** FIFA EPTS certification process: what are the requirements? Timeline? Cost?
- [ ] **P7.3** NBA approved wearables list: application process? Technical requirements?
- [ ] **P7.4** MLB device approval: 6-8 month process. What do they evaluate?
- [ ] **P7.5** NCAA compliance: new 2026 guidelines. Be early-compliant.
- [ ] **P7.6** IEEE P3716 standard: get involved in the standards process for credibility.
- [ ] **P7.7** Data privacy policy template: GDPR, COPPA, state laws. Must handle before youth market.
- [ ] **P7.8** Medical device classification: does injury "prediction" make this a medical device? FDA implications?

---

## P8: VALIDATION & RESEARCH GAPS

- [ ] **P8.1** Paper 1 (3-sensor optimal) was running-only. Validate for other sports.
- [ ] **P8.2** Paper 2 (92.3% accuracy) used EMG. What's IMU-only accuracy? Literature search needed.
- [ ] **P8.3** False positive rate in real-world conditions (not lab). No paper addresses this well.
- [ ] **P8.4** Long-term prediction accuracy: does the model stay accurate over weeks/months of use?
- [ ] **P8.5** Cross-athlete generalization: does a model trained on 50 athletes work for athlete 51?
- [ ] **P8.6** Community validation: post in r/running, r/sportsanalytics about the concept. Gauge interest.
- [ ] **P8.7** Talk to college athletic directors about willingness to pay and pain points.
- [ ] **P8.8** Talk to sports medicine doctors about what metrics they actually want.
