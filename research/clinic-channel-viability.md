# Clinic Channel Viability: Business Model for Physio/Sports Medicine

> Research date: 2026-09-01
> Purpose: Evaluate whether selling IMU sensor pods through the physio/clinic channel
> is financially viable — insurance, reimbursement, barriers, pricing, and market size.

---

## 1. Insurance and Reimbursement

### Motion Analysis CPT Codes (96000–96004)

These are the codes that cover instrumented gait/movement analysis:

| Code | Description | Notes |
|------|-------------|-------|
| 96000 | Comprehensive computer-based motion analysis (3D kinematics, video) | Technical component |
| 96001 | Motion analysis with dynamic plantar pressure measurements | Technical + plantar |
| 96002 | Dynamic surface EMG during gait/functional movement | Add-on for EMG |
| 96003 | Fine wire EMG — each muscle | Rarely used outside research |
| 96004 | Physician review and interpretation of gait analysis data | Professional component only |

**Reimbursement:** These codes may be **contractor-priced** under Medicare — no single
national rate. Each Medicare Administrative Contractor (MAC) sets its own amount. The 2026
Medicare conversion factor is **$33.40/RVU** (non-APM) or **$33.57/RVU** (APM).

**Coverage is narrow.** Cigna, for example, considers 96000 medically necessary **only**
for cerebral palsy or myelomeningocele in children/adolescents. Gait analysis for any other
indication is "not covered or reimbursable." This is a critical constraint — many insurers
treat instrumented gait analysis as investigational for adult musculoskeletal conditions.
([Cigna coverage policy](https://static.cigna.com/assets/chcp/pdf/coveragePolicies/medical/mm_0315_coveragepositioncriteria_gait_analysis.pdf))

### Therapeutic Procedure Codes (More Widely Covered)

| Code | Description | Typical Use |
|------|-------------|-------------|
| 97116 | Gait training (per 15-min unit) | Walking on surfaces, obstacles, assistive devices |
| 97110 | Therapeutic exercise (per 15-min unit) | Strength, endurance, flexibility exercises |
| 97530 | Therapeutic activities (per 15-min unit) | Functional activities for physical deficits |
| 97032 | Biofeedback (per 15-min unit) | EMG or other biofeedback during therapy |
| 97750 | Physical performance test/measurement | Objective functional testing |

These are **widely reimbursed** — they're standard PT billing codes. The biofeedback code
(97032) is particularly relevant: our real-time audio cue during running IS biofeedback.
A clinic could bill 97032 for a session where a patient wears our pods and receives
real-time tibial acceleration feedback.

### Remote Therapeutic Monitoring (RTM) — The Revenue Multiplier

RTM is the **most relevant reimbursement pathway** for our device. PTs can bill for
monitoring patients between visits using connected devices. Key codes:

| Code | Description | 2026 Rate (approx) |
|------|-------------|---------------------|
| 98975 | RTM setup and patient education | Billed once per episode |
| 98977 | MSK device supply, 16+ days/month | ~$52/month |
| 98985 | MSK device supply, 2–15 days/month (**NEW 2026**) | Newly introduced |
| 98980 | Treatment management, first 20 min/month | ~$51/month |
| 98981 | Treatment management, each add'l 20 min | ~$39/month |

**Monthly revenue per enrolled patient: ~$120–150** (98977 + 98980 under Medicare).

**Who can bill:** Physical therapists billing under their own NPI for MSK RTM (98977).
PTAs and OTAs can contribute monitoring time under general supervision. This is a
significant expansion vs RPM (which is largely physician-only).

**The 2026 CMS update is a tailwind.** New codes (98985 for 2–15 days, 98979 for 10–19
min) lower the old thresholds, making it viable for patients who use devices less
frequently. This maps directly to our 8-session programme — patients might only use pods
8 days in a month, which now qualifies under 98985.

**The economic case:** If a clinic enrolls 20 patients in RTM using our pods at $130/month
reimbursement, that's **$2,600/month or $31,200/year in new revenue** — from one code set,
with minimal incremental clinician time. This far exceeds the cost of purchasing our
hardware.

Sources:
- [Tenovi RPM codes 2026](https://www.tenovi.com/rpm-cpt-codes-2026/)
- [Tenovi RTM codes 2026](https://www.tenovi.com/rtm-cpt-codes-2026/)
- [Medbridge RTM guide](https://www.medbridge.com/blog/what-is-remote-therapeutic-monitoring-billing-codes-and-best-practices-for-success)
- [Limber Health 2026 CMS Final Rule RTM](https://www.limberhealth.com/blog/2026-cms-final-rule-rtm-codes)
- [Sprypt CPT codes guide](https://www.sprypt.com/blog/physical-therapy-cpt-codes-reference-sheet)
- [Sprypt 96000-96001 guide](https://www.sprypt.com/cpt-codes/96000-96001)
- [clinIQ RTM billing guide](https://www.cliniqhealthcare.com/blog/rtm-revenue-guide)

### How Much of Clinic Revenue Comes From Insurance?

The vast majority. Physical therapy is **insurance-dependent**: Medicare, Medicaid, and
private insurers cover most visits. Out-of-pocket / cash-pay PT is a growing niche but
still <10% of the market. Insurance denial rates are ~12.9% and climbing.

---

## 2. Barriers to Clinic Adoption

### Why Clinics Don't Adopt New Technology

1. **Budget constraints.** Small independent PT practices have tight margins. Technology
   budgets are minimal — $3–8K/year for all new equipment in many cases. 59% of employers
   are making cost-cutting changes to health plans in 2026.
   ([Sprypt](https://www.sprypt.com/blog/physical-therapy-digital-innovation-guide))

2. **Workflow disruption.** Over 90% of PTs rely on subjective assessment despite evidence
   that objective tools improve outcomes 30–40%. Technology adoption has been "low and slow."
   Clinicians don't change workflow easily — even when the evidence is strong.
   ([Benchmark PS](https://www.benchmarkps.org/blog/posts/state-of-physiotherapy-technology/))

3. **Training time.** Most clinicians will tolerate 1–2 hours of training for a new device.
   Anything requiring multi-day training or certification is a non-starter for busy practices.

4. **EMR/EHR integration.** Clinics want data to flow into their existing systems. Standalone
   apps that don't integrate create double-documentation burden. HIPAA compliance adds
   complexity.

   **Top PT EMR systems (2026):** WebPT ($99/mo/user, most widely used for PT-specific),
   SPRY (AI-powered, 4.7/5 rated), Raintree (enterprise/multi-location), Jane, Clinicient.
   Cloud-based systems now 62.4% of market (up from 41% in 2019). Most do NOT have open
   APIs for third-party device data import — integration may require FHIR/HL7 standards or
   manual PDF report upload as a starting point. **MVP integration: generate a PDF or CSV
   report the clinician can attach to the patient record.** Full API integration is a
   later-stage investment ($15K–40K per EMR platform).
   ([SPRY buyers guide](https://www.sprypt.com/blog/best-emr-physical-therapy-2025-buyers-guide))

5. **Reimbursement uncertainty.** If a clinic can't bill for the service, the technology is
   a cost center. The good news: RTM codes now make our device billable.

6. **Insurance denials.** 12.9% denial rate; frequent no-shows 15–31%; therapist burnout
   16% annual turnover. Clinics are survival-focused, not innovation-focused.

### Sales Cycle

- **Small independent clinics:** 1–3 months. Owner-clinician decides.
- **Hospital/health system clinics:** 6–18 months. Procurement, IT security, credentialing,
  pilot period required.
- **Employer/payer channel (Hinge/Sword model):** 3–12 months, but larger contract values.

### Buying Preferences

Clinics generally prefer **subscription** over large upfront purchases — it maps to their
cash flow (monthly insurance reimbursements). VALD's success at $3,600–5,100/yr
subscription validates this. Our current $249 outright sale model would need to shift to
a monthly subscription (e.g., $99–199/month for hardware + software + cloud) or a
per-assessment fee.

---

## 3. The Compliance/Adherence Advantage

### Home Exercise Program (HEP) Baseline Adherence

- Adherence to prescribed HEPs is typically **50–70%** across studies
- Self-reported adherence is often poor and unreliable (diaries have 60–75% completion)
- Non-adherence is "overwhelmingly high" — commonly >65%
- Adherence to duration per session (70.9%) is more probable than frequency (60.7%)

Sources: [PMC systematic review](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5856927/),
[Tandfonline](https://www.tandfonline.com/doi/full/10.2147/PPA.S346680)

### Does Professional Oversight Improve Adherence?

**Yes — significantly.** Key findings:

- Connected health interventions with intermittent therapist supervision equal or exceed
  face-to-face therapy outcomes
- Frequency adherence is more probable when patients receive clarification of doubts
- Duration adherence is more probable when patients are supervised during exercise learning
- Wearable-monitored adherence reached **80.1%** in one clinical trial (vs 50–70% baseline)
- Sword Health reports **81% programme completion** with their sensor + PT model
- Social support and self-efficacy are the strongest predictors of adherence

**The key insight:** Our device in a clinic context solves two problems simultaneously:
(1) the clinician provides accountability and motivation the consumer channel lacks, and
(2) RTM billing means the clinic gets paid for the monitoring, creating an economic
incentive to keep the patient engaged.

### Does RPM/RTM Improve Adherence?

Emerging evidence says yes. Remote monitoring creates a "someone is watching" effect.
The 2026 RTM expansion (lower day thresholds, 10-min management increments) makes this
economically viable even for patients using devices sporadically.

---

## 4. Market Size and Clinical Use Cases

### US Physical Therapy Market

- **$50–56 billion** in 2024–2025; projected **$70B by 2030** (6.4% CAGR)
- **39,000–151,000+ PT-related businesses** (depending on category definition)
- **~602,000 practicing physical therapists** in 2024; 14% employment growth projected 2023–2033
- **1 in 4 US adults** has a musculoskeletal condition requiring medical attention
- Average **8 visits per episode** of MSK care

Sources: [Grand View Research](https://www.grandviewresearch.com/industry-analysis/us-physical-therapy-services-market-report),
[IBISWorld](https://www.ibisworld.com/united-states/industry/physical-therapists/1562/),
[Marketdata](https://blog.marketresearch.com/strong-demand-for-53-billion-u.s.-physical-therapy-clinics-industry)

### Common Movement Assessments Physios Perform

- Functional Movement Screen (FMS) — 7 movement patterns
- Y-Balance Test — dynamic balance
- Single-leg squat assessment — knee valgus, control
- Gait analysis — cadence, stride, asymmetry, limp
- Range of motion (goniometry) — joint-by-joint
- Manual muscle testing — strength grading
- Return-to-sport testing — hop tests, agility

**Current standard: visual observation.** Inter-rater reliability is poor (kappa
0.04–0.59). Clinicians detected only 22% of deviations predicted by biomechanical
analysis. This is a real clinical gap — but willingness to pay for the solution is unclear.

### Expansion Beyond Running

**In-clinic exercise form monitoring** for rehab (squats, lunges, step-ups) is almost
entirely visual observation today. Technology adoption is minimal. Kinvent's K-Move and
Sword Health's sensors are the closest, but Sword is home-use and Kinvent is still small.

**Workers' comp / occupational health** is a genuine opportunity:
- Employer directly pays (not insurance complexity)
- Workers' comp injury costs motivate ROI-driven purchases
- Employer-mandated wear solves retention problem entirely
- Already identified in CLAUDE.md as target market #3

---

## 5. Pricing Models That Work

### What Clinics Pay Today

| Company | Model | Price Range |
|---------|-------|-------------|
| VALD | Annual subscription | $3,600–5,100/yr |
| dorsaVi | Monthly SaaS | $59–550/month |
| Kinvent | Hardware + app subscription | ~$3,000+ hardware |
| DARI Motion | Enterprise SaaS + per-scan | Undisclosed (quote-based) |
| Noraxon | Hardware + license | $10,000–25,000+ |

### The Sweet Spot

**$3,000–6,000/yr subscription** appears to be the ceiling for routine clinic use
(VALD's price point, where they've achieved the most traction at 5,000+ orgs).

### ROI Calculation for a Clinic Owner

The RTM codes change the math entirely:

| Item | Amount |
|------|--------|
| Monthly RTM revenue per patient (98977 + 98980) | ~$130 |
| Patients enrolled in RTM per month | 10–20 |
| Monthly new revenue | $1,300–2,600 |
| Annual new revenue | $15,600–31,200 |
| Cost of our device (subscription model) | $3,000–6,000/yr |
| **Net ROI** | **~$10,000–25,000/yr** |

**This is a strong pitch:** "Our device pays for itself in the first 2–3 months through
RTM billing you're not currently capturing." This is how VALD sells — not on clinical
outcomes (though those matter) but on revenue generation.

### Can Clinics Charge Extra?

Yes — "technology-assisted assessment" can be billed as a separate service (97750
physical performance test, or 96000 motion analysis where covered). Some clinics charge
patients a cash-pay technology assessment fee ($75–200) on top of insurance-covered PT.

---

## 6. Synthesis: Is the Clinic Channel Viable?

### Arguments FOR

1. **RTM reimbursement is real and growing.** The 2026 CMS expansion specifically helps
   our use case (MSK, lower day thresholds, PT can bill directly). Monthly $120–150/patient.
2. **The ROI pitch works.** Device pays for itself through new billing codes. This is VALD's
   playbook and it's working at 5,000+ organizations.
3. **Professional oversight solves the retention problem.** 81% completion (Sword) vs
   50–70% self-directed. The physio IS the forcing function the consumer channel lacks.
4. **Market is large.** $50B+ US PT market, 39,000+ clinics, 602,000+ PTs. Even 1%
   penetration = 390+ clinics.
5. **Insurance makes price invisible.** Patient doesn't pay $249 out of pocket; it's
   absorbed into covered PT sessions and RTM billing.
6. **Expansion beyond running is natural.** Clinic sees all MSK conditions — knee rehab,
   hip replacement, low back pain, shoulder. Same hardware, different protocols.

### Arguments AGAINST

1. **dorsaVi is the precedent and it's at AU$1.13M/yr after 19 years.** This is the
   single biggest warning. They do exactly this — IMU sensors to clinics — and have not
   found scale.
2. **Clinic sales are slow and expensive.** 1–18 month cycles. A 2-person startup cannot
   afford enterprise sales.
3. **Technology adoption in PT is stubbornly low.** >90% rely on subjective assessment
   despite 30–40% better outcomes with objective tools.
4. **Camera-based alternatives are gaining.** DARI Motion, Kinetisense, and phone-based CV
   eliminate sensor setup entirely. A clinic might prefer a camera that requires zero
   per-patient hardware.
5. **HIPAA and potentially 510(k) add cost.** Even minimum viable HIPAA is $5–20K year one.
   510(k) is $30–115K+ and 6–12 months if required.
6. **Per-clinic revenue is small.** Even at $5K/yr subscription, you need thousands of
   clinics for a meaningful business. This is a grind, not a rocket ship.

### The dorsaVi Question

**Is dorsaVi's failure a market problem or an execution problem?** This is the critical
question. If the market is structurally small for "wearable IMU + clinics," no amount of
execution fixes it. But dorsaVi also had: declining product investment, ASX listing
overhead, no RTM billing (didn't exist until 2022), and arguably poor timing. The RTM
codes may have changed the economic equation since dorsaVi's peak.

### Net Assessment

**Conditionally viable — but only if:**
1. We lead with the RTM revenue pitch (not clinical outcomes)
2. We price as subscription ($99–199/month), not outright sale
3. We stay within general wellness / biofeedback framing initially (avoid 510(k))
4. We target small independent practices first (shorter sales cycle)
5. We plan for 1–3 month sales cycles and build accordingly

The clinic channel won't produce Hinge Health scale ($588M) because that requires the
employer channel. But it could produce a sustainable, profitable business at $1–10M ARR
if execution is strong — which is a better outcome than dorsaVi achieved because they
didn't have RTM billing as a revenue driver.

---

## RTM Billing Reality Check — Researched 2026-09-01

### Adoption Rate: How Many PT Clinics Actually Bill RTM?

**Short answer: very few.** No comprehensive industry-wide survey exists, but the strongest
data point comes from APTA PPS 2025: **only 1.6% of Medicare patients are receiving RTM.**
This was presented by Dr. Andrew Gorecki (Superior Physical Therapy) and framed as evidence
that "most clinics are failing to implement it correctly."
([Movement Rx / APTA PPS 2025](https://mymovementrx.com/rtm-outcomes-profitability-apta-2025/))

Additional context:
- RTM codes were introduced by CMS in **January 2022** — they are only ~4 years old
- The US RTM market was valued at ~$387M in 2024 with 17.2% CAGR projected through 2030
  ([Actuvi](https://www.actuvi.com/blog/the-surge-in-remote-therapeutic-monitoring-a-market-on-the-rise))
- Multiple RTM platform vendors describe awareness among outpatient PT clinic owners as
  "surprisingly low" ([PhyxUp](https://blog.phyxuphealth.com/remote-therapeutic-monitoring-rtm-in-physical-therapy-a-complete-guide/))
- VMG Health (PT M&A advisory) identifies RTM as a growth opportunity for PT operators but
  does not cite an adoption percentage ([VMG Health](https://vmghealth.com/insights/blog/remote-therapeutic-monitoring-implications-for-physical-therapy-operators/))

**Implication for us:** The 1.6% number is both a warning and an opportunity. Warning:
clinics aren't adopting this even when the codes exist. Opportunity: clinics that DO adopt
see large revenue gains (see below), and "we help you bill RTM" is a genuine value prop.
But it means our sales motion includes *teaching clinics how to bill RTM*, not just selling
hardware — which adds cost and complexity to the sales cycle.

### Common RTM Claim Denial Reasons

The five most common denial triggers for RTM claims
([PhyxUp](https://blog.phyxuphealth.com/rtm-claim-denials-2026/)):

| # | Denial Reason | Details |
|---|---|---|
| 1 | **Data transmission days mismatch** | Billing 98977 (16+ days) when actual monitored days are fewer. Must use 98985 (2–15 days) instead. Most frequent denial trigger. |
| 2 | **Missing or backdated patient consent** | Consent must be documented (verbal or written) and dated at enrollment, not at billing time. |
| 3 | **Incomplete time logs** | Treatment management codes (98979/98980/98981) require timestamped start/end, specific activity performed, and who performed it. Self-attestation is not accepted. |
| 4 | **Mutually exclusive code billing** | Billing both 98977 AND 98985 in the same 30-day period, or both 98979 AND 98980. Only one from each pair per period. |
| 5 | **Outdated 2025 code logic** | CMS introduced new codes and thresholds effective Jan 1, 2026 (98985 for 2–15 days, 98979 for 10–19 min). Clinics still using pre-2026 billing logic trigger denials. |

PhyxUp claims their billing engine targets a denial rate of **<4%**, implying the industry
average is materially higher. No published industry-wide RTM denial rate was found.

**Implication for us:** If we bundle our hardware with an RTM billing workflow, we need to
either (a) partner with an RTM platform that handles claim logic, or (b) build our own
compliance layer — which is costly. The documentation burden (consent, time logs, day
counts) is non-trivial and falls on the clinic staff, not on us.

### Does CPT 98977 Require an FDA-Cleared Device?

**This is the critical question, and the answer is nuanced.**

Per CMS rules, the device used for RTM must be a **"medical device" as defined by the FDA
FD&C Act** — but this does **NOT** mean it must go through the FDA "clearance" (510(k)) or
"approval" (PMA) process.
([HealthSnap](https://healthsnap.io/resources/rtm-billing-overview/))

Specifically, the device must fall into one of these categories:
1. Subject to current FDA **"enforcement discretion"** (many wellness/fitness devices)
2. **Registered** with the FDA
3. **Cleared** via 510(k) submission
4. **Approved** via PMA application

The FDA definition of "medical device" also **includes Software as a Medical Device (SaMD)**.
This means a software-only app on the patient's phone could theoretically qualify, provided
it meets the FDA's definition of a medical device (intended for diagnosis, cure, mitigation,
treatment, or prevention of disease).

**What this means for us:** We do NOT necessarily need full 510(k) clearance to bill 98977.
If our device + app is positioned as a "general wellness" product under FDA enforcement
discretion (which our current "biofeedback for gait retraining" framing supports), it may
qualify. However, this is a grey area:

- "Enforcement discretion" means the FDA *could* regulate it but currently *chooses not to*.
  This is not the same as a formal exemption.
- Some payers may independently require FDA clearance even if CMS does not.
- The risk is that a payer audits a claim and decides our device doesn't meet their internal
  definition of a qualifying medical device.

**Bottom line:** The 510(k) is not legally required for RTM billing, but it provides
defensibility. A registered device under enforcement discretion is the minimum viable path.
**Legal review required before committing to this strategy.**

### RTM Billing Platforms for PT Clinics

A competitive market of RTM software platforms has emerged. Key players (2026):

| Platform | Key Differentiator | Notes |
|---|---|---|
| **MedBridge** | Bundles clinician education + HEP + RTM; largest brand in PT education | Broad feature set but RTM is add-on to education platform |
| **Limber Health** (acquired by Net Health) | RTM-first; MIPS/QCDR reporting; value-based care workflows | Enterprise-oriented, service-managed model |
| **Physitrack** | Global scale; Epic integration; ISO compliance | Best for large health systems; less suited for small clinics |
| **Wibbi** | Integrates with 75+ EMRs; updated for 2026 codes | Strong integration story |
| **Orva** | All 6 RTM codes in one workflow; built for ortho/rehab | Streamlined billing logic |
| **PhyxUp Health** | Claims automation; targets <4% denial rate | Small-clinic focused; billing engine emphasis |
| **Movement Rx** | Transparent pricing; licensed virtual monitoring team | Outsources monitoring staff to the clinic |
| **AC Health** | RTM cheat sheets and workflow guides | Education-forward approach |

([Physitrack](https://www.physitrack.com/insights/best-rtm-software-physical-therapy);
[Movement Rx](https://mymovementrx.com/best-rtm-software-for-physical-therapy-clinics-2026-buyers-guide/);
[Hemscap](https://hemscap.com/blogs/81/top-5-rtm-platforms-for-physical-therapy-in-2026))

**Implication for us:** We would NOT build an RTM billing platform — we'd integrate with
one. The question is whether our device data can feed into these platforms' workflows. Most
accept data via API or manual entry. A clean integration with MedBridge or Limber Health
would be the highest-leverage partnership.

### Average RTM Patients Per Clinic (Among Those That Bill RTM)

Hard numbers are scarce, but converging signals:

- Clinics typically **launch with 10–20 patients** in the first month
  ([Wibbi](https://wibbi.com/resource/how-to-implement-rtm-in-a-physical-therapy-practice/))
- At 40 patients, spreadsheet-based workflows still work; at 100–200, they break and
  require dedicated software
  ([Physitrack](https://www.physitrack.com/insights/best-rtm-software-physical-therapy))
- A 30–40% enrollment rate (of eligible patients) is referenced as a reasonable target
  ([Movement Rx](https://mymovementrx.com/rtm-outcomes-profitability-apta-2025/))
- Average Medicare reimbursement is ~$119/patient/month across RTM codes at that
  enrollment rate
- Superior Physical Therapy's case study: profit per case increased **277%** (from ~$91–104
  to $362–393) after implementing RTM across 2,223 tracked patients
  ([Movement Rx / APTA PPS 2025](https://mymovementrx.com/rtm-outcomes-profitability-apta-2025/))

**Implication for us:** A realistic target is 10–30 RTM patients per clinic using our pods.
At ~$120/patient/month RTM reimbursement, that's $1,200–3,600/month in new clinic revenue.
The 277% profit-per-case increase is a compelling sales stat — but it comes from one case
study at one clinic chain, not an industry-wide average. Use with attribution, not as a
universal claim.

### RTM Reality Check: Net Assessment

| Factor | Finding | Impact on Us |
|---|---|---|
| Adoption rate | ~1.6% of Medicare patients in RTM | Market is early; education cost is high |
| FDA device requirement | FD&C Act definition, NOT 510(k) clearance | We may qualify under enforcement discretion; legal review needed |
| Top denial reasons | Day-count mismatches, missing consent, incomplete logs | Compliance burden falls on clinic; we need platform integration |
| Billing platforms | 8+ competing platforms; no dominant winner | Partner, don't build; integrate with MedBridge or Limber |
| Patients per clinic | 10–30 typical; 40+ needs software | Revenue per clinic is real but modest |
| Profit impact | 277% increase in one case study | Compelling sales pitch if validated by more data |

**The RTM revenue model is real but early-stage.** The codes exist, the reimbursement is
real, and clinics that adopt see meaningful revenue. But adoption is extremely low (1.6% of
Medicare patients), the compliance burden is non-trivial, and we'd be selling into a market
that mostly doesn't know RTM exists yet. This means our sales pitch has to include "here's
what RTM is and how to bill it" before we can get to "here's our device." That's a longer,
more expensive sales cycle than "plug in our device and start billing."
