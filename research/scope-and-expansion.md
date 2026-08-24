# Scope — Stick To Running? And Is The Universal Pod Vision Right?

**Researched 2026-08-24.** Two questions: should v1 stay running-only, and is the long-term
"snap a pod anywhere, app analyses any movement" vision correct?

**Short answers:**
1. **Yes, stay on running** — but for a sharper reason than "focus." The entire evidence
   base is running-specific, and leaving running means leaving the evidence behind.
2. **The universal pod hardware vision is right and also already exists.** Xsens DOT has
   been exactly that for years. It never became a consumer product, and *why* it didn't is
   the most useful thing in this file.
3. **"One app does all types of analysis" is the part I would push back on hardest.** That
   is not one app. It is N products sharing a sensor, and each N needs its own dataset.
4. **The correct expansion axis is locomotion, not "all movement."** Gym form is the worst
   available second market.

---

## 1. The Universal Pod Already Exists — And It Is A Dev Kit

Movella/Xsens DOT is a small snap-anywhere body IMU pod, sold for years, ~$200/sensor.
Their own positioning, verbatim:

> *"A state-of-the-art **development platform** for the measurement and analysis of human
> kinematics."*
> *"An SDK is provided to facilitate the development of mobile applications based on the
> available output data, thereby allowing developers to easily integrate the Xsens DOT into
> a wide range of solutions."*

**They built the hardware you are describing and then sold it to people who would build the
analysis themselves — because the analysis is the product and they do not have it.**

That is the single most instructive fact here. A generic "wear it anywhere, measure any
movement" pod is not a differentiated position; it is an unfinished product. The market has
had one for years and it lives in research labs.

`market-teardown.md` §0 already showed every commercial winner is domain-specific:
Catapult (team sport load), WHOOP (recovery), Stryd (running power), Playermaker (soccer),
VALD (clinical testing). **The generic ones — Xsens DOT, SlimeVR — are tools, not products.**

---

## 2. What Actually Transfers Between Sports

Breaking the product into layers and asking honestly what carries over:

| Layer | Transfers? | Notes |
|---|---|---|
| **Pod hardware** | **~100%** | An IMU is an IMU. Same pod, BLE, dock, battery, enclosure |
| **App shell, pairing, sync, data pipeline** | **~90%** | Real reuse. Not trivial to build, and worth building once properly |
| **Attachment system** | **~30%** | A shoe mount does nothing for a bicep curl. Each domain needs its own mounting |
| **Movement analysis** | **~10%** | Gait analysis ≠ lift form ≠ tennis stroke. Different models, features, events |
| **Labeled dataset** | **0%** | Running data teaches you nothing about a serve |
| **Evidence / claim** | **0%** | Chan's HR 0.38 is a running result. It says nothing about tennis |

**Starting with running builds roughly 40% of the platform** — the hardware and the app
shell. That is real and worth having. But the 60% that decides whether each new domain
works has to be built from scratch, per domain, including a new dataset and new validation.

**The honest framing: this is not one product that grows. It is a hardware platform plus a
sequence of separate analysis products, each with its own multi-year evidence problem.**

That is still a legitimate company — Catapult is exactly that shape. But the plan and the
timeline should reflect it, and the pitch should never be "our app can analyse everything,"
because the first customer who tries the second sport will discover it cannot.

---

## 3. Why The Gym Example Is The Worst Second Market

You raised back and bicep workouts with pods on both arms giving form instruction. The
evidence here is genuinely unfavourable, in a specific way.

**The good news — feedback does work in resistance training.** A systematic review found
feedback enhanced acute kinetic and kinematic output, muscular endurance, motivation and
perceived effort, with chronic improvements in speed, strength, jump performance and
technical competency. Per-rep feedback frequency is best. The mechanism is real.

**The bad news — a wrist device already does it.**

> *"Inertial measurement units appear to be the most accurate technology available and,
> **when worn on the wrist** of the athlete, offer **excellent accuracy, even for lower body
> exercises**."*

Reported performance: exercise classification 89–93%, **rep-counting error under 6%**, and a
**single wrist IMU** supporting real-time rep detection and near-failure states.

So in the gym, our structural advantage from `capability-envelope.md` — that a wrist device
is blind to bilateral asymmetry — **largely evaporates**, because the wrist is holding the
weight. We would be entering Apple Watch, Garmin and WHOOP's home territory with a
higher-friction product that needs strapping to both arms, to do a job a watch already does
at 93%.

**Also note the exit that already happened:** Atlas Wearables — automatic exercise
recognition, rep counting, form evaluation — was **acquired by Peloton in March 2021** as
part of a $78.1M three-company purchase. The gym-form-recognition capability has already
been bought and absorbed into a platform. That space is not empty; it is consolidated.

**Verdict: gym form is the worst available expansion. High friction, no structural
advantage, incumbent platforms, and already consolidated.**

---

## 4. The Right Expansion Axis: Locomotion, Not "All Movement"

The capability that is genuinely ours is not "movement analysis." It is narrower and
stronger:

> **Bilateral asymmetry and per-limb mechanics during locomotion, measured anywhere, with
> the ability to intervene in real time.**

That is wrist-impossible (one arm, no per-limb view), camera-impossible outside an
instrumented venue, and force-plate-impossible outside a lab. Check where it applies:

| Domain | Uses per-limb locomotion asymmetry? | Evidence base | Verdict |
|---|---|---|---|
| **Running** | Yes — the core case | **Chan 2018 RCT, HR 0.38** | **v1** |
| **Return-to-sport / ACL rehab** | **Yes — asymmetry *is* the clinical metric** | Real clinical literature; wearables validated for joint kinematics in high-speed tasks | **Best v2** |
| Team sport locomotion (soccer, basketball) | Yes — cutting, landing, deceleration | Partial (ACL cutting algorithms) | v3 |
| Tennis footwork | Partly — movement yes, stroke no | None found | Later |
| Tennis stroke mechanics | No | None | Different product |
| **Gym / resistance form** | **No** | Feedback works, but a wrist does it | **Avoid** |

**Return-to-sport is the strongest second market** and it is worth naming explicitly:
inter-limb asymmetry after ACL reconstruction is *literally the measurement clinicians
already use* to decide whether an athlete can return. There is existing clinical literature,
an existing payer, an existing workflow, and an existing decision that our data feeds. It
also reuses the running gait analysis almost entirely.

On tennis specifically — a 7-pod full-body capture of a match is a legitimate *research*
product, and the hardware supports it. But the analysis and the evidence would both start
from zero, and the market is small. Treat it as something the platform *can* do for a
customer who asks and pays, not something we productise.

---

## 5. So: Stick To Running — And The Reason Matters

The usual reason given for focus is "startups should do one thing." That is true but weak.
The specific reason here is stronger:

**Everything we have that is defensible is running-specific.**

- Chan et al. HR 0.38 (0.25–0.59), n=320 — running
- Peak tibial acceleration as the feedback variable — running
- The 8-session protocol with faded feedback, 100% adherence — running
- Insole/shoe mounting validated for impact loading — running
- The claim language that keeps us inside FDA general wellness — built on running measurements

**Step outside running and every one of those goes to zero simultaneously.** We would be
back at K1 — "we think this helps" — which is exactly the position the evidence audit killed
on day one.

Running is not a starting point chosen for simplicity. It is **the only domain where we can
currently make a defensible claim at all.**

---

## 6. What To Build Now So The Platform Stays Possible

The vision is not wrong as a destination. It is wrong as a *positioning today*. Concretely,
build for the platform without pitching the platform:

**Do now:**
- **Pod hardware that is genuinely mount-agnostic.** Same pod, interchangeable mounts. Costs
  nothing extra and preserves every future option.
- **Separate the analysis layer from the app shell** — pairing, sync, storage, session model
  and dock logic should have no running-specific logic in them. This is the 90% that reuses.
- **Log raw IMU always, never only derived metrics.** Today's raw running data is tomorrow's
  training set for a domain we have not chosen yet. Storage is cheap; unrecorded data is
  gone forever.
- **Design the tier ladder (more pods → more analysis) as a capability contract**, so adding
  a domain means adding a model, not re-architecting.

**Do not do now:**
- Do not market a multi-sport platform. Xsens DOT shows where that positioning lands.
- Do not build a second sport before running is validated in the field.
- Do not build gym/resistance analysis at all on current evidence.
- Do not claim the app "can analyse any movement." It cannot, and the first customer who
  tries will find out.

---

## 7. My Honest View, Stated Plainly

**The hardware vision is right.** A small snap-anywhere pod, sold in increasing counts for
increasing analysis depth, is a coherent product architecture and the BOM in
`bom-and-pricing.md` supports it.

**The app vision is where I would push back.** "The app can and should do all this" treats
the analysis as a software feature. It is not — it is the entire moat, it is domain-specific,
and each domain needs its own labeled dataset, which `predictive-validity.md` §9 identified
as the hardest unsolved problem in this whole space. One app that analyses running well is a
multi-year effort. One app that analyses running, tennis and lifting well is three companies.

**And the risk of holding the platform vision too close right now is concrete:** it pulls you
toward building a *generic* pod, which is a development kit, which is what Xsens DOT is, which
is why it sits in labs instead of on runners.

**Win running first. Not because focus is a virtue, but because running is the only place we
currently have a weapon.**

---

## Sources
- [Movella/Xsens DOT white paper — "development platform" positioning](https://www.movella.com/hubfs/Downloads/Whitepapers/Xsens%20DOT%20WhitePaper.pdf) · [Xsens DOT datasheet](https://www.xsens.com/hubfs/Xsens%20DOT%20data%20sheet.pdf)
- [Feedback in resistance training — systematic review and meta-analysis](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10432365/)
- [Exercise classification in resistance training — technological approaches review](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12513948/) · [Commercial resistance-training device validity](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7900050/)
- [Atlas Wearables acquired by Peloton](https://www.crunchbase.com/acquisition/peloton-interactive-acquires-atlas--41015b91) · [Peloton three-company acquisition](https://www.wareable.com/wearable-tech/peloton-acquires-atlas-wearables-8366)
- [Wearables for ACL return-to-sport joint kinematics](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8037754/)
- [Xsens IMU lower-extremity joint angles, in-field running](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10856827/)
