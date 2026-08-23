# Capability Envelope — What Can Only We Do?

**Researched 2026-08-23. Resolves VIABILITY K4.**

The original framing of this test was "wrist-replicable vs wrist-impossible." That was too
narrow — nobody is proposing to build a wrist device, and the wrist market is saturated.
The correct question is: **against every alternative that can produce human movement data,
what capability is structurally ours?**

Alternatives assessed: wrist wearables, phone cameras, stadium camera arrays, fixed testing
equipment (force plates), and instrumented treadmills.

---

## 1. The Envelope

| Capability | Wrist | Phone camera | Stadium camera array | Fixed equipment (VALD) | **Body pods** |
|---|---|---|---|---|---|
| Cadence, GCT, vertical oscillation, stride | ✓ | partial | ✓ | ✗ | ✓ |
| Running power | ✓ (now native) | ✗ | ✗ | ✗ | ✓ |
| Bilateral asymmetry | **✗** | ✓ in frame | ✓ | ✓ in lab | ✓ |
| Joint angles, sagittal | ✗ | ~3–15° | ✓ | ✓ | ~4–6° |
| Joint angles, **transverse (rotation)** | ✗ | **3–57°** | poor | ✓ | ~5–6° |
| **Peak tibial acceleration** | ✗ | ✗ | ✗ | ✗ | **✓ — only** |
| Ground reaction force | ✗ | ✗ | ✗ | ✓ | ✗ (proxy only) |
| **Real-time feedback during the activity** | limited | ✗ | ✗ | ✗ | **✓** |
| Works anywhere, zero install | ✓ | partial | **✗** | ✗ | **✓** |
| Every athlete simultaneously on a large field | ✓ | ✗ | ✓ *in venue only* | ✗ | **✓** |
| Sustained across hours, sessions, months | ✓ | ✗ | ✓ *in venue only* | ✗ | **✓** |
| Cost to deploy at a training ground | — | low | **£125–250k+ per site** | $10k+ | per-athlete |

**Four capabilities are structurally ours.** Not "ours until someone catches up" — ours for
physical reasons that do not change with better software:

1. **Peak tibial acceleration measured at the tibia.** No camera can put an accelerometer on
   a bone. No wrist device can see the shank. This is the single variable the working
   intervention (§3) is built on.
2. **Real-time feedback during the activity.** Cameras observe; they do not intervene. A
   stadium array cannot buzz your leg mid-stride. Every alternative in the table is a
   measurement system; only a body-worn pod closes the loop.
3. **Location independence.** No install, no venue, no calibration volume. Road, trail,
   training ground, high school pitch, warehouse floor.
4. **Per-limb bilateral data outside an instrumented venue.** A wrist device is on one arm
   and is geometrically blind to left/right difference. That blindness is permanent.

---

## 2. The Camera Question — The User's Instinct, Checked

The claim under test: *"camera based is good but a camera can never track movement of each
and every athlete for a sport played on a big field."*

**Mostly correct, but the reason matters and it is not accuracy — it is deployment.**

### Cameras have moved further than expected
Optical skeletal tracking is real and shipping at elite level:
- **Hawk-Eye SkeleTRACK** — dedicated 4K tracking cameras, ball plus **29 points on every
  player, in real time**, marketed explicitly for "performance analysis and injury prevention"
- **FIFA semi-automated offside** runs on this; FIFA and Hawk-Eye have a joint Football
  Technology Centre
- **NFL** adopted Hawk-Eye virtual measurement for first downs from the 2025 season
- **NBA** uses Hawk-Eye tracking; **TRACAB** and **Second Spectrum** compete in football

So "a camera can never track every athlete on a big field" is **false as a technical claim**
at the elite tier. In a fitted stadium, it already does — for every player, in real time,
at 29 body points.

### But the constraint is brutal and it is economic
> *"For 99% of the football world, [these systems] are irrelevant in the most practical
> sense: you cannot buy them for your club. They are league-level infrastructure, installed
> in stadiums, funded centrally."*

Hawk-Eye's goal-line technology alone ran **£125,000–£250,000 per ground**, and SkeleTRACK
adds a dedicated camera array on top. These are permanent installations in venues, procured
centrally by leagues.

**What that leaves uncovered:**
- Every training ground (where, per `regulations.md`, all the actually-permitted usage lives)
- Every high school and college field
- Every road, trail, park and track
- Every warehouse floor (Option B)
- Match day at any club below the top tier

### And markerless accuracy degrades exactly where it matters
| Plane | Markerless camera error | Body-worn IMU error |
|---|---|---|
| Sagittal | 3–15° | ~3.9–6.4° |
| **Transverse (rotation)** | **3–57°** | ~5–6° |

Transverse-plane rotation is where ACL mechanism lives. A 57° upper bound is not a
measurement. Documented failure modes compound it: occlusion between players, identity
swaps in crowds, accuracy loss over field distances, and degradation under direct sunlight,
strong shadows and changing light — most pose models were trained indoors.

### The honest conclusion
**Cameras own the instrumented venue on match day. Nothing owns the training ground, the
road, or the amateur field — and cameras structurally cannot, because the cost is per-site
and the athlete has to be inside the volume.**

That is a real, durable gap. But it must be stated correctly. The pitch is **not** "cameras
can't do this." It is: *"cameras do this beautifully in forty stadiums. We do it everywhere
else, and we can also intervene, which no camera can."*

---

## 3. What The Envelope Is Actually For

The capabilities in §1 are only worth having if something valuable sits on top of them. It
does — see `predictive-validity.md` §4B. The published, RCT-supported intervention uses
**exactly** the four structural capabilities and nothing else:

- **Peak tibial acceleration** — capability 1, impossible for every alternative
- **Real-time audible cue when the threshold is exceeded** — capability 2
- **Outdoors, on real runs** — capability 3
- **Per-leg, different tone for each side** — capability 4

That is not a coincidence. **The intervention with the best evidence in this field is the
one that can only be delivered by body-worn sensors.** Cameras cannot deliver it at all —
not for cost reasons, but because they cannot measure the variable and cannot close the loop.

**K4 resolves: the value proposition survives deleting every wrist-replicable and
camera-replicable metric.** What remains — tibial acceleration, bilateral per-limb data,
real-time in-activity intervention, anywhere — is the whole product.

---

## 4. Design Rules That Follow

1. **Never let a wrist-replicable metric be load-bearing.** Cadence, GCT, vertical
   oscillation, stride length and running power are all now native on Garmin and Apple.
   Show them for context; never sell on them. NURVV died charging $299 for them.
2. **Lead with peak tibial acceleration and per-limb asymmetry.** These are the moat.
3. **The product is an intervention, not a measurement system.** Every alternative in §1
   measures. Only we can act inside the activity. That is the category we compete in.
4. **Do not compete with stadium arrays on match day.** Complement them: they cover 90
   minutes in one venue; we cover every training session everywhere.
5. **Expect further wrist absorption.** Assume anything derivable from a single trunk or
   wrist signal ships natively within 24 months. Re-check quarterly per `market/WATCHLIST.md`.

---

## Sources
- [Markerless motion capture review — accuracy and failure modes](https://www.frontiersin.org/journals/sports-and-active-living/articles/10.3389/fspor.2025.1712332/full)
- [Multi-method 3D markerless capture in sport](https://www.tandfonline.com/doi/full/10.1080/02640414.2025.2489868)
- [Motion capture technologies review for multi-sport organisations](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12299843/)
- [Hawk-Eye skeletal tracking / officiating](https://www.hawkeyeinnovations.com/news/4227979/making-sport-fairer-with-accurate-event-detection-the-future-of-officiating-via-skeletal-tracking)
- [Second Spectrum vs TRACAB vs Hawk-Eye comparison](https://gamecode.ai/insights/articles/second-spectrum-vs-tracab-vs-hawk-eye/)
- [Wrexham AFC SkeleTRACK deployment](https://www.sportsvideo.org/2025/09/22/wrexham-afc-select-hawk-eye-to-deliver-skeletal-tracking-and-video-review-system-services-for-home-matches/)
- [NFL Hawk-Eye adoption](https://seekingalpha.com/pr/20053371-sonys-hawk-eye-innovations-selected-by-the-nfl-to-revolutionize-line-to-gain-measurements)
- [Optical tracking economics](https://huddleup.substack.com/p/the-100000-camera-system-thats-quietly)
- [Garmin wrist-based running power](https://www.advnture.com/news/garmin-is-taking-the-fight-to-apple-with-new-running-power-feature-and-its-about-time)
