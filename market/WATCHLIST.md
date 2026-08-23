# Market Watch — Standing Discipline

**This never ends.** Market intel decays fast in this category: NURVV went from a $9M
Series A to insolvency in 3.5 years; Garmin deprecated its own accessory category in a
firmware update. A market read that is 12 months old is actively misleading.

**Cadence:** full review quarterly. Trigger-based checks whenever a signal in §3 fires.
**Output:** append to `market/LOG.md`, update `research/market-teardown.md`, revise kill
probabilities in `problems/VIABILITY.md`.

---

## 1. The Watchlist

### Direct — running / gait wearables
| Entity | Why watched | Key question each review |
|---|---|---|
| **ARION / ATO-Gear** | Closest living analogue; source of the only positive RCT | Still alive? Headcount? Pivoted? Any new trial data? |
| **Stryd** | The survival role model | Still one pod? Community/open-data posture intact? New metrics? |
| **NURVV (assets)** | Insolvent 2023 — who bought the IP? | Has anyone relaunched it? Ex-employees findable? |
| **RunScribe** | Named in the GRF-vs-tibial-load critique | Alive? Changed their claims? |
| **Plantiga, Sensoria, Orpyx** | Foot/insole sensing adjacents | Traction? Clinical vs consumer positioning? |

### Team sports / institutional
| Entity | Why watched | Key question |
|---|---|---|
| **Catapult** | Healthy incumbent, active acquirer | What did they buy? Any real-time or biomechanical move? |
| **VALD** | The actual winner (4,000+ orgs, fixed equipment) | Any move into wearables? That would be a major signal |
| **STATSports** | Direct incumbent | Consumer push? Price moves? |
| **Playermaker / PlayerData** | Proof of the per-player parent-funded model | Pricing, channel, retention, funding |
| **Sparta Science** | Competes for the same NCAA budget line | Traction, claims language |
| **KINEXON** | SmartCourt "injury prevention alerts" claim | Have they ever substantiated it? |

### Injury-risk software (no hardware)
| Entity | Why watched | Key question |
|---|---|---|
| **Zone7** (Svexa) | Best commercial prediction claim | Have they *ever* published specificity or flag rate? |
| **Kitman Labs** | Performance intelligence platform | Funding, claims, consolidation |
| **Orreco** | Adjacent analytics | — |

### Industrial / workers' comp — Option B
| Entity | Why watched | Key question |
|---|---|---|
| **StrongArm** ($50M) | Category leader | Growth, churn, insurer partnerships |
| **Kinetic** (REFLEX) | Real-time feedback, same mechanism as ARION | Published outcome data? |
| **Soter Analytics** ($12M) | — | — |
| **Modjoul** ($11.7M, Mar 2025) | Most recent raise | Where is the money going? |

### Platform threats
| Entity | Why watched | Key question |
|---|---|---|
| **Garmin** | Absorbed running power into the wrist | **What did the wrist learn to do this quarter?** |
| **Apple** | Running dynamics native on Ultra | Same |
| **WHOOP** | Owns hardware-subscription; has WHOOP Body multi-position | Any move to multi-point or asymmetry? |
| **Google/Fitbit** | Fitbit Air form factor reference | Sensor additions, price moves |

---

## 2. What To Extract Every Review

For each entity, three columns only — resist writing essays:

1. **Still alive?** Headcount, funding, last product ship, any insolvency signal.
2. **What are they doing right that we should duplicate?**
3. **What are they doing wrong that we should avoid?**

Feed anything new into the Duplicate/Avoid list in `market-teardown.md` §3. That list is
the deliverable; the rest is working notes.

---

## 3. Trigger Signals — Check Immediately, Don't Wait For The Quarter

**Red — may invalidate the thesis:**
- Garmin or Apple ships **bilateral asymmetry or per-limb mechanics** from the wrist or a
  single device → K4 fires hard; our only structurally defensible ground is gone
- Catapult, VALD or WHOOP launches a multi-pod body-worn product → the friction problem is
  either solved by someone with distribution, or about to be publicly proven unsolvable
- A large RCT publishes showing gait retraining does **not** help asymptomatic runners → K3 fires
- A well-funded competitor launches our exact product → check their claim language first;
  they may be about to make the mistake we identified

**Amber — revise plans:**
- Another gait-wearable company folds → run failure archaeology (`VIABILITY.md` §3.2)
- Zone7 or anyone publishes real specificity/flag-rate numbers → update `predictive-validity.md` §6
- FDA revises the general wellness boundary → recheck `buyer-and-liability.md` §2
- Insurers begin underwriting sports injury on wearable data → Option B expands into sports
- NCAA finalises 2026 wearable guidance → regulatory window

**Green — opportunity:**
- A competitor's assets come up for sale (as NURVV's did)
- A platform *deprecates* a running feature — an absorbed feature being abandoned reopens a niche
- New public dataset with longitudinal injury labels → the P0.3 bottleneck loosens

---

## 4. Standing Sources

- **DC Rainmaker** — the gatekeeper in running tech; his reviews function as post-mortems
- **the5krunner** — platform feature absorption tracking
- Catapult ASX filings (CAT) — the only public financials in the space
- Crunchbase / PitchBook / Tracxn — funding and headcount signals
- **PubMed / BJSM / Sports Medicine** alerts on: injury prediction, gait retraining,
  wearable RCTs, ACWR
- Youth Sports Business Report — youth/amateur channel moves
- Risk & Insurance, Milliman — the industrial/insurer side

---

## 5. Review Checklist

Each quarter, in order:

- [ ] Walk the watchlist. Three columns each. Anything dead or newly funded?
- [ ] Platform check: what can the wrist do now that it could not last quarter?
- [ ] Literature check: any new RCT or meta-analysis touching K3 or K1?
- [ ] Update Duplicate/Avoid in `market-teardown.md` §3
- [ ] **Revise kill probabilities in `VIABILITY.md` §1** — with a written reason for each change
- [ ] **Run the pre-mortem** (`VIABILITY.md` §3.1) cold, before re-reading anything
- [ ] Append a dated entry to `market/LOG.md`

---

## Log
See `market/LOG.md`. First full review due **2026-11-23**.
