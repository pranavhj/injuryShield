# Clinic Regulatory Landscape: FDA, HIPAA, and Liability

> Research date: 2026-09-01
> Purpose: Map the full regulatory path for bringing an IMU gait analysis device into
> the US physio/clinical channel — what's required, what it costs, and what the fastest
> legal path is.

---

## 1. FDA Device Classification

### Where We Sit Today (Consumer)

Currently: **FDA general wellness** — no regulatory submission required. The device
measures gait mechanics (tibial acceleration, cadence, GCT, asymmetry), provides
real-time audio biofeedback, and shows deviation from the user's own baseline. No
diagnostic claims, no injury prediction, no treatment recommendations.

The **January 6, 2026 FDA General Wellness guidance** (superseding the 2019 version)
confirms: the FDA does not intend to regulate low-risk general wellness products as
medical devices, provided they are intended solely for general wellness use and present
low risk to users.

### What Qualifies as "General Wellness" (2026 Guidance)

Products measuring physiologic parameters can qualify if ALL of these are true:
- Noninvasive
- No safety-risk technology (lasers, radiation, implants)
- **Not intended for diagnosis, cure, mitigation, prevention, or treatment of a disease**
- Not a substitute for an FDA-approved/cleared device
- **No claims or outputs that guide clinical management**
- **No clinical thresholds** or values that mimic clinical diagnostics
- No characterization of outputs as "abnormal" or diagnostic

A product MAY suggest users "consult a health care professional" without losing wellness
status, provided such prompts don't name a specific disease, characterize outputs as
diagnostic, or include clinical thresholds.

Sources:
- [Faegre Drinker — 2026 guidance analysis](https://www.faegredrinker.com/en/insights/publications/2026/1/key-updates-in-fdas-2026-general-wellness-and-clinical-decision-support-software-guidance)
- [Troutman Pepper Locke — 2026 guidance](https://www.troutman.com/insights/fdas-2026-guidance-on-general-wellness-devices-policy-for-low-risk-devices/)
- [ArentFox Schiff — 2026 guidance](https://www.afslaw.com/perspectives/alerts/fda-issues-updated-guidance-low-risk-general-wellness-devices-and-clinical)
- [Womble Bond Dickinson — 2026 guidance](https://www.womblebonddickinson.com/us/insights/blogs/fdas-2026-general-wellness-policy-and-what-it-means-manufacturers-wearable-devices)

### What TRIGGERS Medical Device Classification

Crossing any of these lines makes the product a medical device requiring clearance:

| Claim / Feature | Classification Trigger? | Notes |
|-----------------|------------------------|-------|
| "Measures gait mechanics" | **No** — measurement for wellness | Safe if no diagnostic claim |
| "Shows your running form" | **No** — informational wellness | No disease reference |
| "Detects asymmetry" | **Probably no** — descriptive | Don't add "which may indicate injury risk" |
| "Biofeedback during exercise" | **Depends** — see 97032 | Biofeedback for "wellness" ok; for "treatment" = medical |
| "Used by a clinician to inform treatment" | **YES — likely triggers** | Intended use follows marketing, not user type |
| "Monitors post-ACL rehab progress" | **YES — medical device** | Disease-specific, treatment-related |
| "Return-to-sport clearance" | **YES — medical device** | Safety decision = medical device |
| "Reduces injury risk" | **YES — prevention claim** | Prevention of disease/injury = medical device |

### The Dual-Use Question

**Can a device be "general wellness" for consumers AND "medical device" in clinics?**

The 2026 guidance says: "all labeling, instructions, and promotional materials of the
product must align with the product's wellness-focused intended use." Classification
follows the **marketed intended use**, not who actually uses it.

In practice: if WE market and label it as a wellness device, and a physio happens to use
it clinically, **we are probably still wellness** — as long as we don't market it TO
clinics with clinical claims. But this is a gray area. The moment we have a "clinic"
version with clinical reports, RTM integration, or rehab-specific protocols, the intended
use has shifted.

**The WHOOP warning:** FDA sent WHOOP a warning letter for marketing Blood Pressure
Insights without clearance. The product was framed as consumer wellness, but the specific
claims crossed into medical territory. This shows FDA enforces the line.

### Predicate Devices (Companies That Got 510(k))

| Company | Device | FDA Status | Class | Product Code |
|---------|--------|-----------|-------|-------------|
| **dorsaVi** | ViMove (IMU + EMG) | 510(k) cleared | Class II | Gait analysis system |
| **Hinge Health** | Enso (TENS device) | 510(k) cleared (K233784) | Class II | TENS |
| **Sword Health** | Digital Therapist (IMU sensors + tablet) | FDA-listed | — | Listed, not cleared? |
| **APDM/Clario** | Opal V2C (IMU) | FDA-listed | — | Clinical trial use |
| **BioSensics** | LEGSys (IMU gait/balance) | FDA-listed | — | First FDA-listed wearable for clinical gait |
| **DARI Motion** | Markerless 3D camera | FDA-cleared | — | Motion analysis |

**Key distinction:** "FDA-listed" (establishment registration) ≠ "FDA-cleared" (510(k)
reviewed and found substantially equivalent). Listing is mandatory ($11,423/yr fee);
clearance requires the full 510(k) process.

**dorsaVi's path is our closest precedent:** IMU sensors, clinical gait analysis, Class II,
510(k) cleared. They validated ViMove data against Vicon optical tracking — accuracy
within 5° for lumbopelvic movements, ICC >0.86 inter-tester reliability.

---

## 2. Clinical Decision Support (CDS) Exclusion

The **21st Century Cures Act § 520(o)(1)(E)** excludes certain CDS software from medical
device regulation if ALL FOUR criteria are met:

1. Does **not** process medical images, diagnostic device signals, or complex physiological
   patterns
2. **Displays, analyzes, or distributes** patient medical information and clinical evidence
3. **Supports** HCP recommendations regarding prevention, diagnosis, or treatment
4. Enables clinicians to **"independently review the basis"** for recommendations —
   clinician must be able to reach the same conclusion without relying primarily on software

**Our fit:** Criterion 1 is the risk. IMU data could be interpreted as "physiological
signals," and our algorithms process these signals. If FDA considers our gait analysis
algorithm as "processing physiological signals to derive a conclusion," we fail criterion 1
and CDS exclusion doesn't apply.

**The 2026 CDS guidance update** expanded the exclusion slightly:
- Broader interpretation of acceptable "medical information" sources
- Software identifying eligible patient populations may qualify
- Greater emphasis on clinician's ability to independently evaluate

Source: [Faegre Drinker](https://www.faegredrinker.com/en/insights/publications/2026/1/key-updates-in-fdas-2026-general-wellness-and-clinical-decision-support-software-guidance)

---

## 3. The 510(k) Process — What It Would Actually Take

### Timeline

| Phase | Duration |
|-------|----------|
| Preparation (documentation, testing) | 60–90 days |
| Pre-submission meeting with FDA | ~90 days |
| FDA review (multiple rounds) | 140–180 working days |
| **Total: decision to clearance** | **~9–15 months** |

Average review time has been increasing — last 2-year average of 149 days is 15% above the
all-time median of 129 days. A denied submission (NSE) averages **337 days** before final
decision and requires a new full fee if resubmitted.

### Cost (FY 2026)

| Item | Cost |
|------|------|
| FDA 510(k) user fee (standard) | $26,067 |
| FDA 510(k) user fee (small business <$100M revenue) | $6,517 |
| Establishment registration fee (annual, no discount) | $11,423/yr |
| Regulatory consulting + preparation | $12,000–75,000 |
| Testing (biocompatibility, EMC/EMI, software validation) | Included or additional |
| **Total estimated range** | **$30,000–115,000+** |

The small business discount (up to 75% off the user fee) is available for companies with
gross receipts under $100M — we would qualify.

### Testing Requirements

- **Biocompatibility** (ISO 10993): skin contact testing for wearable sensors
- **EMC/EMI** (IEC 60601-1-2): electromagnetic compatibility
- **Software validation** (IEC 62304): medical device software lifecycle
- **Electrical safety** (IEC 60601-1): if the device has a battery/charger
- **Clinical data:** For a 510(k) with a good predicate (e.g., dorsaVi ViMove), **bench
  testing may suffice** — clinical trials are NOT always required. dorsaVi validated
  against Vicon optical tracking. We could do the same.

### De Novo Pathway

Relevant if no good predicate exists. **Much more expensive:** $100,000–150,000+ and
12–18 months. Requires clinical validation. Probably not necessary for us given dorsaVi
and BioSensics exist as predicates.

Sources:
- [510kfda.com costs](https://510kfda.com/pages/fda-510k-costs)
- [MedDeviceGuide cost breakdown](https://meddeviceguide.com/blog/how-much-does-510k-cost-guide)
- [i3c Global fees](https://www.i3cglobal.com/fda-510k-fees/)
- [Blue Goat Cyber FDA costs](https://bluegoatcyber.com/blog/fda-medical-device-submission-costs-explained-510k-pma-and-more-2025-guide)

---

## 4. Software as Medical Device (SaMD)

### Is the App a Separate Medical Device?

If the hardware is "just" an IMU sensor (dumb data collector) and the **software** does
all the analysis (gait metrics, asymmetry detection, biofeedback logic), the software
itself may be classified as SaMD.

**IEC 62304 compliance** is required for medical device software:
- Software development lifecycle documentation
- Risk management (ISO 14971)
- Software of Unknown Provenance (SOUP) analysis
- Verification and validation

### SaMD Classification

FDA's SaMD framework considers:
- **Significance of information** provided (treat/diagnose vs drive/inform)
- **State of healthcare situation** (critical vs serious vs non-serious)

For our use case (informing exercise modification, non-serious MSK condition), the
classification would likely be **Class I or low Class II** — the lowest SaMD risk category.

### Does the Phone App Need Separate Clearance?

**Possibly.** If the pod is the listed device and the app is its accessory, they can be
covered under one submission. If the app independently provides clinical analysis, it may
need its own clearance. Regulatory counsel needed for this specific question.

---

## 5. HIPAA Requirements

### When HIPAA Applies

If patient gait data flows through our servers (cloud processing, clinician dashboards,
RTM data transmission), we handle Protected Health Information (PHI) and are either a
**Covered Entity** or more likely a **Business Associate** of the clinic.

### Requirements

| Requirement | What It Means |
|-------------|---------------|
| Business Associate Agreement (BAA) | Contract with every clinic + every vendor handling PHI. $500–2,000 per vendor to negotiate. |
| Encryption | Data encrypted at rest and in transit (AES-256, TLS 1.2+) |
| Access controls | Role-based access, audit logging, minimum necessary principle |
| Risk assessment | Annual security risk analysis (required) |
| Breach notification | 60-day notification obligation for breaches affecting 500+ individuals |
| Training | Employee HIPAA training ($50–100/person/year) |
| Policies & procedures | Written privacy and security policies |

### Cost of Minimum Viable HIPAA Compliance (Year 1)

| Item | Estimated Cost |
|------|---------------|
| Compliance platform/automation tool | $3,000–6,000/yr |
| Policies and procedures (template-based) | $2,000–8,000 |
| Risk assessment | $1,000–5,000 (internal) |
| Training | $50–100/person |
| BAAs (legal review) | $500–2,000 per vendor |
| **Year 1 total (lean startup approach)** | **$5,000–20,000** |
| **Ongoing annual** | **$3,000–10,000** |

**Cloud hosting:** AWS, GCP, and Azure all offer HIPAA-eligible services with BAAs.
Using them is standard and acceptable. Data on the patient's phone is generally considered
under the patient's control, not a HIPAA obligation for us.

Sources:
- [Accountable HQ — startup HIPAA costs 2026](https://www.accountablehq.com/post/hipaa-compliance-cost-for-startups-what-to-budget-in-2026)
- [Medcurity — HIPAA costs by size](https://medcurity.com/hipaa-compliance-cost/)
- [LowerPlane — HIPAA for startups 2026](https://lowerplane.com/blog/hipaa-for-startups/)

---

## 6. State-Level Requirements

No US states impose additional medical device requirements **beyond** federal FDA for
devices that are FDA-cleared or exempt. However:

- **Telehealth/remote monitoring** regulations vary by state. Some states require the
  monitoring provider to be licensed in the patient's state.
- **Practice act restrictions:** In most states, providing a "movement analysis report"
  is not restricted to licensed clinicians IF the report is informational and does not
  constitute diagnosis or treatment recommendation. Our "deviation from baseline" framing
  is defensible. However, if our software says "this patient should modify their exercise
  because..." that crosses into clinical recommendation territory.

---

## 7. International Considerations (Brief)

| Market | Pathway | Difficulty vs US |
|--------|---------|-----------------|
| **EU (CE/MDR)** | MDR Class I or IIa; requires a Notified Body audit for Class IIa+ | Harder — MDR is more burdensome than 510(k), longer timelines, and there's a Notified Body bottleneck |
| **UK (UKCA)** | Similar to pre-Brexit CE but with MHRA oversight | Similar to EU |
| **Canada** | Health Canada Class I or II medical device license | Similar to FDA in complexity |
| **Australia** | TGA clearance; dorsaVi already has this, so predicate path exists | Moderate — TGA is well-structured |

**Easiest path:** Stay in the US first. FDA general wellness → 510(k) if needed.
Australia second (TGA, dorsaVi predicate). EU last (MDR is the most burdensome).

Source: [Geyan Technology — medical wearable certification roadmap 2026](https://xdunmedical.com/medical-wearable-certification-roadmap-2026/)

---

## 8. Practical Regulatory Strategy

### The Fastest Legal Path Into Clinics

**Option A: Stay General Wellness (fastest, lowest cost, highest risk of enforcement)**

- Keep current wellness framing and labeling
- Sell pods to consumers; the consumer chooses to share data with their physio
- We provide a "clinician view" that is informational only — no clinical claims
- Clinic uses RTM codes (98977) to bill for monitoring using our device
- **Risk:** If FDA deems our clinic-facing materials as changing the intended use, we're
  in violation. The WHOOP warning letter shows FDA enforces this boundary.
- **Cost:** $0 regulatory, just HIPAA ($5–20K)
- **Timeline:** Immediately

**Option B: 510(k) Clearance (safest, moderate cost)**

- File 510(k) using dorsaVi ViMove as predicate
- Small business fee: ~$6,517 + $12–75K consulting/testing
- **Total cost: $30–90K** (realistic for a startup)
- **Timeline: 9–15 months** from decision to clearance
- Unlocks: explicit clinical marketing, RTM billing confidence, clinic credibility,
  hospital/health system sales (they require FDA clearance)
- **This is what dorsaVi did.** It didn't save them commercially, but it wasn't the
  regulatory step that failed — it was go-to-market execution.

**Option C: Phased Approach (recommended)**

1. **Phase 1 (now):** Launch as general wellness, consumer-facing. Same as current plan.
2. **Phase 2 (months 3–6):** Build the "clinician view" — informational dashboard,
   exportable reports. Keep all language strictly descriptive (measurements only, no
   recommendations). Begin HIPAA compliance.
3. **Phase 3 (months 6–12):** If clinic demand materializes, file 510(k) using dorsaVi
   predicate. Small business fee keeps cost manageable.
4. **Phase 4 (months 12–18):** 510(k) clearance. Switch to explicit clinical marketing.
   RTM billing fully supported. Hospital/health system sales unlocked.

### How Did Others Handle This?

- **dorsaVi:** 510(k) from day one (2015 expanded clearance). Clinical first. Correct
  regulatory path but failed commercially.
- **Sword Health:** FDA-listed (not cleared) for their IMU sensors. Their TENS device
  and some features are 510(k) cleared. Hybrid approach.
- **Hinge Health:** 510(k) cleared the Enso TENS component. The motion sensors/app are
  listed, not necessarily 510(k) cleared separately.
- **WHOOP/Oura:** General wellness framing. Pushed boundaries until FDA sent a warning
  (WHOOP blood pressure). Shows the ceiling of the wellness path.

---

## 9. Liability and Malpractice

### If a Physio Uses Our Device and the Patient Gets Worse

**The "information only — clinician decides" framing provides significant protection:**

- The treating clinician holds the clinical judgment responsibility
- We provide data; the clinician interprets and acts
- Our liability is limited to: data accuracy (did we measure correctly?) and product
  safety (did the device harm the patient physically?)
- We are NOT liable for clinical decisions made by the physio based on our data, provided
  we made no clinical recommendations

### Product Liability Insurance

- Required for any medical device on the US market
- Cost for a startup with low revenue: **$5,000–15,000/yr** for general product liability
- Medical device specific coverage may be higher
- Most clinic contracts will require proof of insurance + indemnification clauses

### Claims/Disclaimers Required

- "This device provides movement measurements for informational purposes only"
- "All clinical decisions must be made by a qualified healthcare professional"
- "This device does not diagnose, treat, or prevent any disease or medical condition"
- "Not a substitute for professional medical advice"

### Indemnification in Clinic Contracts

Standard B2B SaaS practice: mutual indemnification where each party indemnifies the
other against claims arising from their own negligence. The clinic indemnifies us against
clinical malpractice claims; we indemnify them against product defect claims.

---

## 10. Summary: Regulatory Cost and Timeline

### Minimum Viable Path (Option A: Wellness + HIPAA)

| Item | Cost | Timeline |
|------|------|----------|
| HIPAA compliance (year 1) | $5,000–20,000 | 1–3 months |
| Product liability insurance | $5,000–15,000/yr | 1 month |
| Legal review of claims/labeling | $2,000–5,000 | 2 weeks |
| **Total** | **$12,000–40,000** | **1–3 months** |

### Full Clinical Path (Option B: 510(k) + HIPAA)

| Item | Cost | Timeline |
|------|------|----------|
| 510(k) user fee (small business) | $6,517 | — |
| Establishment registration | $11,423/yr | — |
| Regulatory consulting + testing | $12,000–75,000 | — |
| HIPAA compliance | $5,000–20,000 | — |
| Product liability insurance | $5,000–15,000/yr | — |
| Legal review | $2,000–5,000 | — |
| **Total (year 1)** | **$42,000–133,000** | **9–15 months** |
| **Ongoing annual** | **$20,000–50,000** | — |

### The Bottom Line

The regulatory path is **manageable** for a startup. It's not cheap, but it's not
prohibitive either. The phased approach (start wellness → file 510(k) when demand
justifies it) is the standard playbook, used successfully by Sword Health and Hinge Health.

**The real question isn't "can we navigate the regulations?" — it's "does the clinic
market justify the regulatory investment?"** That answer depends on the business model
viability analysis in `clinic-channel-viability.md`.
