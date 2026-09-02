# 510(k) Planning — Practical Roadmap

> Created 2026-09-01. Tracks the regulatory path from D18.
> This is NOT the submission — it's the plan to get to submission.

---

## Phase 0: Before Filing (Now → Month 3)

### 0.1 Confirm the predicate — DONE
- [x] **dorsaVi ViMove FDA clearances confirmed:**

| K-Number | Device | Decision Date | Product Codes | Class |
|----------|--------|---------------|---------------|-------|
| **K131094** | ViMove (original) | 2014-07-11 | IKN (Diagnostic Electromyograph), HCC (Biofeedback Device), KQX (Goniometer) | Class II |
| **K142494** | ViMove (expanded) | 2015-05-28 | IKN, HCC, KQX | Class II |
| **K163150** | ViMove2 | 2017 (approx) | IKN, HCC | Class II |

- **Our most relevant predicate:** K163150 (ViMove2) — wireless IMU sensors (accelerometer + gyroscope), Bluetooth, mobile app, measures range of movement. Classified as Electromyograph + Biofeedback device, Class II.
- **Product codes for our device:** HCC (Biofeedback Device) is the strongest fit — our real-time audio cue IS biofeedback. KQX (Goniometer) applies if we claim angle measurement.
- **Key note:** ViMove2 includes EMG; we don't. This is a SIMPLER device than the predicate, which is generally favorable for substantial equivalence arguments.
- [ ] **Search for additional predicates:** BioSensics LEGSys, APDM Opal, VERABAND — for backup

### 0.2 Find a regulatory consultant
Budget: $12,000–20,000 for a focused 510(k) with a good predicate.

**Firms to contact (specializing in wearable/digital health):**
- [Emergo by UL](https://www.emergobyul.com/services/us-fda-510k-consulting-medical-devices-and-ivds) — large, well-known, $$$
- [NAMSA](https://namsa.com/services/consulting/us-fda/fda-510k-consultants/) — full-service, good for first-timers
- [Innolitics](https://fda.innolitics.com/) — SaMD specialists, good 510(k) search tool
- [i3C Global](https://www.i3cglobal.com/fda-510k-fees/) — budget-friendly, $12K–20K range
- [Cruxi](https://cruxi.ai/pages/regulatory/fda-510k-consultant.html) — directory/matching service
- **Ask for:** fixed-price quote for a 510(k) with a known predicate (dorsaVi ViMove), timeline estimate, whether they handle IEC 62304 (software lifecycle), and small business fee eligibility confirmation

### 0.3 Apply for small business status
- [ ] **File FDA small business determination EARLY** — if approved, 510(k) fee drops from $26,067 to $6,517
- [ ] Requires: gross receipts under $100M (we qualify)
- [ ] **WARNING:** if you submit at standard rate then later get small business status, you lose the ~$19,550 difference. Apply before filing.

### 0.4 Start IEC 62304 documentation
- [ ] Software development plan
- [ ] Software requirements specification
- [ ] Software architecture document
- [ ] Risk management file (ISO 14971)
- [ ] This can start NOW with zero hardware — it's documentation of how we build software

---

## Phase 1: Pre-Submission Meeting (Month 3–5)

- [ ] **Request a pre-submission (Pre-Sub) meeting with FDA**
  - Free. Lets you ask FDA exactly what they expect before you file.
  - Submit questions about: predicate choice, testing requirements, clinical data needs
  - Typical turnaround: ~75 days for written feedback, or faster for a meeting
- [ ] **Draft the submission outline** based on Pre-Sub feedback

---

## Phase 2: Testing (Month 4–8, overlaps with Phase 1)

### Required testing:
- [ ] **Biocompatibility (ISO 10993):** skin contact testing — cytotoxicity, sensitization, irritation. ~$5K–15K
- [ ] **EMC/EMI (IEC 60601-1-2):** electromagnetic compatibility. ~$5K–15K
- [ ] **Electrical safety (IEC 60601-1):** battery, charger safety
- [ ] **Software validation (IEC 62304):** verification and validation of the app + firmware
- [ ] **Performance testing:** accuracy against gold standard (Vicon optical motion capture or similar). dorsaVi validated to within 5° — we should match or beat this.

### Probably NOT required:
- Clinical trials — if we have a good predicate and bench testing shows equivalence, clinical data may not be needed. Confirm at Pre-Sub.

---

## Phase 3: Submission (Month 8–10)

- [ ] **Complete 510(k) using eSTAR format** (mandatory since Oct 2023)
- [ ] **Pay the fee** ($6,517 with small business status)
- [ ] **Register the establishment** ($11,423/yr — no discount)
- [ ] Submit and wait for FDA review

---

## Phase 4: Review (Month 10–15)

- Average review: 149 days (recent 2-year average)
- May receive Additional Information (AI) requests — respond promptly
- Target: clearance by month 15 from decision to start

---

## Budget Summary

| Item | Low | High |
|------|-----|------|
| 510(k) user fee (small business) | $6,517 | $6,517 |
| Establishment registration | $11,423 | $11,423 |
| Regulatory consultant | $12,000 | $20,000 |
| Biocompatibility testing | $5,000 | $15,000 |
| EMC/EMI testing | $5,000 | $15,000 |
| Software validation support | $0 (internal) | $10,000 |
| **Total** | **$40,000** | **$78,000** |

---

## Next Actions (This Week)

1. **Search FDA 510(k) database for dorsaVi K-number** — 30 min task
2. **Email 3 regulatory consultants for quotes** — draft email below
3. **Apply for small business determination** — before any filing

### Draft Email to Regulatory Consultants

```
Subject: 510(k) Quote — IMU Wearable for Gait Analysis

Hi,

We're developing a 2-pod IMU wearable system for running gait analysis, targeting the
physiotherapy/sports medicine market. We plan to file a 510(k) using dorsaVi's ViMove
as the predicate device (both are IMU-based motion analysis systems for clinical gait
assessment).

Could you provide:
1. A fixed-price estimate for preparing and filing the 510(k)
2. Whether you handle IEC 62304 software lifecycle documentation
3. Estimated timeline from engagement to submission
4. Whether you can confirm our eligibility for the small business fee ($6,517 vs $26,067)

We're a pre-revenue startup — two founders, one in the US (engineering), one in India.
Hardware is in development; software is in early stages.

Thank you,
[Name]
```
