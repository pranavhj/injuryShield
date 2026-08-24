# Ecosystem Business Model — InjuryShield

> ## ⚠️ SUPERSEDED ON PRICING AND MODEL — 2026-08-24
> This file argues for hardware-as-subscription at $35/pod. **Both are reversed.**
> Current model is **outright sale at ~$249 for a 2-pod Core kit** — see `DECISIONS.md` D3, D8
> and `research/unit-economics.md`.
>
> Also note: the Section 44ADA point applies to an *individual professional*, not a company.
> See `research/buyer-and-liability.md` §4.


## Core Principle
Sell an ecosystem, not a product. Customers buy whichever parts they need.

## Ecosystem Components

### 1. Hardware: Sensor Pods ($35 each, $105 for 3-pod kit)
- Fitbit Air-sized, screenless, snap-on pebble pods
- 3-axis accelerometer + 3-axis gyroscope (200Hz)
- Edge ML for real-time injury risk inference
- Haptic motor for on-body alert
- BLE 5.x for phone/hub communication
- USB-C or magnetic charging
- IP68 waterproof
- Target weight: <15g per pod

### 2. Hardware: Attachment Options
**Option A — Branded Compression Apparel:**
- Compression shorts (back pod dock)
- Ankle sleeves (ankle pod docks)
- Normal fabric, fully washable — pods snap out before washing
- Magnetic or snap-fit pod docks sewn into garment
- Sizes: XS-XXL
- Price: TBD ($20-40 per garment?)

**Option B — Universal Straps:**
- Adjustable elastic straps with pod dock
- Fits any body size
- Lower cost than apparel
- Price: $5-10 per strap

**Option C — Shoe Clips:**
- Ankle pods clip to shoe laces or heel collar
- Zero-strap option for runners
- Price: $3-5 per clip

### 3. Software: Mobile App (Freemium)
**Free tier:**
- Pod pairing and setup
- Live session view (basic metrics: cadence, ground contact time, stride)
- Session history
- Basic fatigue indicator

**Premium individual ($X/month):**
- Real-time injury risk scoring
- Personalized baselines and trend analysis
- Gait analysis reports
- Training load management
- Export to Strava/TrainingPeaks/Garmin Connect

### 4. Software: Team Dashboard (Subscription)
**Team Basic ($X/month per team):**
- Multi-athlete live view during practice
- Color-coded risk levels per player
- Session summaries
- Roster management

**Team Pro ($X/month per team):**
- Historical injury risk trends per athlete
- Predictive analytics (who's at elevated risk this week)
- Integration with existing platforms (Catapult OpenField, Hudl, etc.)
- Custom alert thresholds per athlete
- Exportable reports for team doctors
- API access for data integration

### 5. Sport-Specific Model Packs
- Running model (v1 — included free with all pods)
- Basketball model (available as add-on or with team subscription)
- Soccer model
- Football model
- Baseball model (may need different pod placement — forearm for pitchers)
- Custom model training service for pro teams

### 6. Services (Future)
- On-site setup and training for athletic departments
- Custom ML model development for specific team needs
- Data analysis consulting
- Integration consulting (connect InjuryShield to existing tech stack)

## Revenue Streams

| Stream | Type | Who Pays |
|---|---|---|
| Pod hardware sales | One-time | Individual athletes, teams, schools |
| Apparel/strap sales | One-time | Same |
| App premium subscription | Monthly/annual | Individual athletes |
| Team dashboard subscription | Monthly/annual | Schools, clubs, pro teams |
| Sport model packs | One-time or included | Teams using non-running sports |
| Consulting/services | Project-based | Pro teams, universities |

## Pricing Strategy

### Phase 1: Individual Athletes (Launch)
- 3-pod kit: $105 ($35/pod)
- App: free tier gets core functionality
- Premium: $5-10/month
- Goal: build community, get feedback, iterate

### Phase 2: School/College Teams
- Team kit (25 athletes × 3 pods = 75 pods): $2,625
- Team dashboard: $50-100/month
- Apparel package: optional add-on
- vs Catapult at $20-40K/year — we're 90% cheaper

### Phase 3: Professional Training
- Premium hardware (higher sampling rate, longer battery)
- Team Pro dashboard: $200-500/month
- Custom model training: $5K-20K project
- Integration consulting: $150-200/hr

## Open-Source Strategy
- **Open-source:** Core firmware, BLE protocol, basic gait analysis algorithms
  - Builds community and trust
  - Free advertising through GitHub stars
  - Attracts contributors who improve the platform
  - Makes us the "Arduino of sports biomechanics"
- **Proprietary:** Injury risk ML models, team dashboard, calibration algorithms
  - This is the moat
  - Trained on real data we collect from users
  - Gets better with more users (network effect on model quality)

## Connection to makingDollarsInIndia
- All revenue in USD (targeting US schools/teams)
- Engineering done from India after move
- Manufacturing: Shenzhen for PCB, India for apparel
- Consulting: remote from India
- Open-source reputation: same playbook as PortPilot strategy
- H-1B phase: build v1 as open-source/personal project, no monetization
- India phase: launch commercially under Indian sole proprietorship
- Section 44ADA applies (digital services to foreign clients)
