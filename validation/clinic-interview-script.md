# Clinic Owner Interview Script — 5 Interviews to Validate RTM as Purchase Driver

> Created 2026-09-01. Target: 5 PT clinic owners or practice managers.
> Goal: Validate P8A.2.4 — does RTM billing actually change purchasing behavior?
> Secondary: understand workflow, EMR, and what dorsaVi-style failures look like from the buyer side.

---

## Finding Interviewees

**Where to find them:**
- LinkedIn: search "physical therapy clinic owner" or "PT practice manager"
- Local PT clinics — call and ask if the owner has 20 minutes for a product research conversation
- APTA (American Physical Therapy Association) local chapters
- r/physicaltherapy on Reddit (for informal conversations)
- PT-specific Facebook groups (private practice PT owners)

**Who to target:**
- Small independent practices (1–5 PTs) — shorter sales cycle, owner makes buying decisions
- Practices that already do some tech (have a modern EMR, do telehealth) — more likely to adopt
- Sports medicine focus preferred but not required

**Compensation:** Offer a $25 Amazon gift card or a free coffee. These are busy people.

---

## Interview Flow (~20 minutes)

### Opening (2 min)
"I'm researching how PT clinics use technology for movement analysis. I'm not selling anything — I'm trying to understand what works and what doesn't before we build anything. Everything you say is confidential and won't be attributed to you by name."

### Section 1: Current Workflow (5 min)

1. **"When a patient comes in with a running-related injury, walk me through how you assess their gait today."**
   - Listen for: visual observation vs video vs any tech
   - Follow-up: "How confident are you in what you see?"

2. **"Do you use any technology for objective movement assessment? Force plates, cameras, sensors, apps?"**
   - If yes: "What do you use? What do you like/hate about it? How much does it cost?"
   - If no: "Have you ever looked into it? What stopped you?"

3. **"What EMR/practice management software do you use?"**
   - Listen for: WebPT, SPRY, Raintree, Jane, Clinicient, or something else
   - Follow-up: "Does any of your tech integrate with it, or is everything separate?"

### Section 2: RTM Awareness and Revenue (5 min)

4. **"Are you currently billing RTM codes — 98977, 98980?"**
   - If yes: "What platform do you use? How many patients are enrolled? What's the revenue impact?"
   - If no: "Are you aware of RTM billing? What's held you back?"
   - Listen for: "don't know how," "too much hassle," "no good device," "not enough patients"

5. **"If a device existed that let you monitor a patient's gait between visits — they wear it during runs, data shows up on your screen — and you could bill RTM for $120–150/month per patient, would that change your interest?"**
   - Listen for: enthusiasm level, skepticism, specific objections
   - Follow-up: "How many of your patients would qualify for that kind of monitoring?"

6. **"What would the device need to do for YOU to actually use it? Not in theory — what would make you reach for it during a session?"**
   - Listen for: simplicity, speed, specific metrics, report format

### Section 3: Purchase Decision (5 min)

7. **"If this device cost $150/month as a subscription — hardware included — and generated $120–150/month in RTM revenue per enrolled patient, how would you evaluate that?"**
   - Listen for: ROI thinking, skepticism about reimbursement, cash flow concerns
   - Follow-up: "How many patients would you need on it to justify the subscription?"

8. **"Who makes the technology purchasing decision at your practice?"**
   - Listen for: owner, office manager, group purchasing, health system IT

9. **"Have you ever tried a movement analysis device and stopped using it? What happened?"**
   - Listen for: dorsaVi-type failures — too complex, took too long, didn't change outcomes, insurance didn't cover it
   - This is GOLD — first-hand buyer regret data

### Section 4: Hardware Friction (3 min)

10. **"If I told you the patient needs to clip a small sensor to each shoe before their run — takes about 10 seconds — and the data syncs to your dashboard automatically, is that acceptable?"**
    - Listen for: "that's fine" vs "patients won't do it" vs "I'd rather have a camera"
    - Follow-up: "What if it's prescribed as part of their treatment plan — like a home exercise programme?"

11. **"Would you prefer an in-clinic camera system that requires no wearable, or a wearable that captures outdoor running data?"**
    - Listen for: which matters more — convenience or data richness

### Closing (1 min)

"This is incredibly helpful. Can I follow up in a few months when we have something to show? And is there anyone else you'd recommend I talk to — another clinic owner, a sports medicine doc, a running coach?"

---

## What to Log After Each Interview

```
Date:
Interviewee role:
Practice size (# PTs):
Location:
EMR used:
Currently billing RTM? Y/N
Currently using any movement tech? What?
Top 3 things they said:
1.
2.
3.
Biggest objection:
Would they use our device? (1-5 scale):
Key quote:
Referred me to:
```

Save to `validation/clinic-interviews/interview-N.md`.

---

## What We're Testing

| Hypothesis | Confirmed if... | Killed if... |
|-----------|----------------|-------------|
| RTM billing drives purchase | 3+ say "the revenue changes the calculus" | 3+ say "RTM is too much hassle regardless" |
| Small clinics decide fast | Average decision timeline <3 months | Most say "I'd need to check with corporate/IT" |
| Outdoor running data has unique value | 3+ say "I can't get that from a camera" | Most say "I'd rather have a camera" |
| Sensor setup is acceptable when prescribed | 3+ say "patients will do it if I tell them to" | Most say "patients won't wear anything" |
| dorsaVi-type failures are known | 1+ has tried and quit a device | — |
