# Cricket Adjudication Project — Complete Handoff Document

> Created 2026-09-07. This captures ALL research, decisions, and strategy from the
> injuryShield pivot session. The cricket project will live in a SEPARATE repo.
> This file + `cricket-cv-research.md` + `opus.txt` are the seed documents.

---

## 1. What We're Building

**A phone-based cricket match analysis system that automatically captures critical moments
(run-outs, stumpings, wides, no-balls) and presents the key frames for human review.**

It is NOT autonomous adjudication (AI says "out"). It is smart frame capture — the app
finds the 2-3 frames that matter and shows them to the players/umpire. This matches how
professional DRS works: the third umpire looks at frames, the human decides.

**Phase 1 is NOT LBW.** LBW requires 3D trajectory prediction from a single camera — a
fundamentally harder problem that Fulltrack AI already does with 4M users and a 1M delivery
training dataset. We enter through the gap they don't fill.

---

## 2. The Gap — Why This Exists

| Decision type | Pro solution | Amateur solution | Our plan |
|---|---|---|---|
| **LBW** | Hawk-Eye ($250K+, 6-16 cameras) | Fulltrack AI ($10/mo, 1 phone) | Phase 6 (later) |
| **Run-outs** | TV replay + stump cam + LED bails | StumpEye ($499 camera, NO AI) | **Phase 1b** |
| **Stumpings** | TV replay + stump cam + LED bails | Nothing | **Phase 1b** |
| **Wides** | Hawk-Eye (IPL 2025, first ever) | Nothing | **Phase 3** |
| **No-balls (front foot)** | Hawk-Eye auto detection | Nothing | **Phase 3** |
| **Caught behind** | UltraEdge (audio) | Nothing | Later |
| **Ball speed** | Speed gun / Hawk-Eye | Fulltrack AI | **Phase 2** |
| **Pitch maps** | Hawk-Eye | Fulltrack AI | **Phase 2** |
| **Auto-clip deliveries** | Broadcast production | Fulltrack AI | **Phase 1a** |

**Nobody — at any level — does automated run-out or stumping frame capture for amateur
cricket.** This is the confirmed gap.

---

## 3. The Only Real Competitor: Fulltrack AI

### Company
- **Founded:** 2020, Seattle. 9 employees. $420K seed round.
- **Founders:** Vivek Jayaram (UW PhD CV, ex-Second Spectrum NBA/EPL tracking, published
  CVPR/NeurIPS/ICML), Brogan McPartland (Harvard Applied Math/CS), Arjun Verma (Harvard, CEO,
  trained with Andre Russell/Ross Taylor in CPL).
- **Scale:** ~4M users, 157 countries, 500+ pro cricketers, 35+ pro teams.
- **Partnerships:** Cricket South Africa (Official Tracking App), European Cricket Network,
  NT Cricket Darwin DRS trial.

### What they do
- Single phone on tripod, 4m behind non-striker stumps, 1.66m height
- Auto-clips every delivery
- Ball speed (ICC 0.87-0.90 vs radar for pace, 0.72-0.76 for spin)
- Pitch maps (ICC > 0.96 for line/length vs motion capture)
- Swing/spin analytics
- **LBW DRS** (Darwin trial: chest-mounted camera on umpire, 85% agreement with umpire)

### How it works technically
1. Red alignment boxes on screen — line up stumps, press Continue (30 sec setup)
2. 2D ball detection CNN (optimized via Qualcomm AI Hub for on-device NPU inference)
3. Physics-based 3D reconstruction: camera calibration from stump geometry + ballistic
   model + Kalman filter
4. Trained on ~1 million deliveries
5. Post-bounce prediction for LBW (the hard part — spin, seam, pitch surface interaction)
6. US Patent 20230100572 covers 3D trajectory reconstruction method

### What they DON'T do
- Run-outs
- Stumpings
- Wides
- No-balls (front foot)
- Caught behind
- Any multi-camera support

### Their moat (ranked by defensibility)
1. **Data (strong)** — millions of deliveries with implicit ground truth
2. **Partnerships (medium)** — Cricket SA, ECN, Darwin trial
3. **Patent (medium)** — covers LBW-specific 3D approach. Different from our run-out approach.
4. **Tech (weak)** — approach published in literature and their own patent
5. **Brand (growing)** — 4M users, pro endorsements

### Pricing
- Free: 75 deliveries/month
- Individual: $9.99/month (300 deliveries — "exhausted in less than an hour at nets")
- Club: $99/year
- Coach+: $149/year (unlimited)
- Enterprise/DRS: contact (per-match, min 50 games)

### App reviews: 3.81/5 from 5,600+ ratings
- Love: "best cricket tech I've ever seen", easy setup, auto-clipping
- Hate: 300 delivery limit, speed overestimation, features moved behind paywall,
  single device lock

---

## 4. Other Products in the Space

### StumpEye — $499 wireless stump camera
- Won Sports Startup of the Year 2026. Open for pre-orders.
- Camera integrated into a cricket stump. No AI — human reviews footage.
- Proves demand for crease-level technology.
- Disadvantages: stumps get struck, bails fly, can't see stumps from stumps, moved every
  innings, can't see the crease line from this position.

### Zing Bails — LED stumps/bails
- Light up within 1/1000th second when bails dislodge.
- Pro: $40-50K. Club version: ~$2,450 AUD. Budget bails: ~$39/pair.
- Useful for precise bail-off timing. NOT for crease-line judgment.
- Could complement our system (precise bail-off frame from LED flash detection).

### CricCam — free multi-phone recording app
- Multi-phone recording + manual replay review. No AI.
- Proves the multi-phone architecture is acceptable to users.

### MCC Smart Ball "U1" — $60 ball with chip
- LBW + edge detection via embedded microphone. Announced 2023.
- **No evidence of actual launch.** Likely vaporware.

### iHawk (Hawk-Eye's amateur system)
- Single chest-mounted GoPro, claimed 95-98% accuracy for LBW.
- Trial with county officials only. No public availability. Not a product yet.

### Kookaburra SmartBall (SportCor)
- Nordic nRF52840, BLE 5 Long Range. Ball spin RPM + speed + seam angle.
- Bowling analytics tool, NOT adjudication. Not a competitor.

### PitchVision
- Hardware + software for cricket video analysis and coaching. 35+ countries.
- Coaching tool, not adjudication. Has good camera angle documentation.

### CricHeroes — 30M+ users (India)
- Scoring/stats platform. AI-generated highlights. No DRS.

---

## 5. Camera Placement Strategy

### Why 1 camera isn't enough

Fulltrack's position (behind bowler) cannot see run-outs or stumpings. The crease line
at the striker's end is 22 yards away and completely foreshortened. The non-striker's
crease is 4m away but viewed along the line, not across it — insufficient for close calls.

Run-out/stumping adjudication requires seeing the crease line PERPENDICULAR to the
viewing angle. That's the square leg position.

### Minimum viable: 2 phones

**Camera 1: Behind bowler's arm (Fulltrack position)**
- 4m behind non-striker stumps, 1.66m height, looking down the pitch
- Ball speed, pitch maps, swing/spin, auto-clipping
- Wides (ball passing outside off/leg stump)
- No-balls front foot (crease is 4m away, great angle — paper shows 98% accuracy)
- Foundation for LBW in later phase
- Non-striker end run-outs (marginal for close calls, fine for obvious ones)

**Camera 2: Square leg at striker's end**
- Side-on to the popping crease, stump height or slightly elevated
- Run-outs at striker's end (~60% of all run-outs)
- Stumpings (always at striker's end)
- Crease line visible as clear horizontal line
- Bat/foot position directly observable relative to crease

### Ideal: 3 phones

Add **Camera 3: Square leg at non-striker's end** for:
- Run-outs at non-striker's end (~40% of all run-outs)
- Better no-ball angle (see foot from the side)

### Design for 3, ship with 2

Teams have 11+ players with phones. "Put your phone on a tripod at square leg" is
reasonable. CricCam already proved multi-phone recording is acceptable.

Phones don't need millisecond-level sync — each camera's footage is analyzed independently.
Cross-camera matching (e.g., "which frame on Camera 2 corresponds to the stumps being hit
on Camera 1") can be done post-hoc via audio matching (sound of ball hitting stumps).

---

## 6. Technical Architecture — What the App Does

### The MVP insight: "show me the frames, don't make the call"

Professional third umpire system works the SAME way — human watches frames, human decides.
The technology captures and presents. We do the same.

### Event detection triggers (how we find the critical moments)

| Event | Trigger | Camera | Difficulty |
|---|---|---|---|
| Delivery bowled | Ball detected leaving bowler's hand | Cam 1 | Medium |
| Ball bounces | Ball trajectory changes direction | Cam 1 | Medium |
| Ball passes bat | Ball enters bat region | Cam 1 | Medium |
| **Bail movement** | Sudden pixel change in stump-top region | Cam 2 | **Easy** (motion detection) |
| **Ball near stumps** | Ball tracking + proximity to stump position | Cam 2 | Medium |
| **Ball passes wide line** | Ball position vs stump position at crease | Cam 1 | Medium |
| **Foot on crease** | Motion in crease region during delivery stride | Cam 1 | Medium |

### What the user sees

**For a run-out review:**
1. Bail movement detected on Camera 2
2. App presents 5-frame sequence centered on the bail-off moment
3. User scrubs through frame-by-frame
4. App overlays the crease line for visual reference (Phase 4)
5. User taps "Out" or "Not Out" → result logged in match scorecard

**For auto-clip:**
1. Ball detection triggers start/end of each delivery
2. Each delivery auto-saved as a clip
3. Clips tagged with metadata (speed, bounce point, outcome)
4. Searchable/filterable after the match

---

## 7. Phased Delivery Plan

| Phase | What ships | Cameras needed | Tech difficulty | Dependencies |
|---|---|---|---|---|
| **1a** | Auto-clip deliveries + manual replay review | 1 (behind bowler) | Low-Medium | Ball detection model |
| **1b** | Auto-find run-out/stumping moments → show critical frames | 2 (add square leg) | Low-Medium | Bail/stump motion detection |
| **2** | Ball speed + pitch map from Camera 1 | 1 | Medium-Hard | 3D trajectory reconstruction |
| **3** | Wide + no-ball frame capture | 1 | Medium | Ball position at stump line, foot detection |
| **4** | Semi-automated: overlay crease line on frame, user judges | 2 | Medium | Crease line detection + perspective transform |
| **5** | Swing/spin analytics | 1 | Hard | Lateral deviation measurement, RPM estimation |
| **6** | LBW prediction | 1 | Very Hard | 3D physics model, post-bounce prediction, massive data |

**Phase 1a + 1b is the MVP.** "Record your match, the app finds every close call and
shows you the frames." That alone is worth $99/year to a club with no review capability.

---

## 8. Technical Feasibility — Ball Speed & Analytics from Phone Cameras

### Ball speed (Camera 1, behind bowler)
- Ball moves along optical axis (away from camera). Can't measure from lateral pixel movement.
- Fulltrack's approach: known geometry (22 yards, stump heights) → camera calibration →
  ball detection in multiple frames → physics model → 3D trajectory fit → speed from trajectory.
- At 30fps: ~15 frames of ball in flight for 140 km/h delivery. Enough data points.
- Ball is tiny at distance (few pixels at 22m) but Fulltrack proves detection works.
- Peer-reviewed: ICC 0.87-0.90 for pace bowling speed. Overestimates speed.
- **Hard but proven possible.** Phase 2, not Phase 1.

### Pitch map (where ball bounces)
- Bounce point is visible from behind bowler as a clear trajectory change.
- 2D position on pitch is detectable with camera calibration.
- Fulltrack validated: ICC > 0.96 for line/length.
- **Medium difficulty.** Phase 2.

### Swing (lateral air movement)
- Left-right ball deviation visible from behind bowler.
- Requires accurate ball detection + calibrated camera.
- **Medium difficulty.** Phase 5.

### Spin (RPM)
- Cannot directly see ball rotation from a single camera at 22m distance.
- Estimated from trajectory deviation + bounce behavior. Inherently approximate.
- Fulltrack's spin speed ICC: 0.72-0.76 (significantly worse than pace).
- **Very hard. Phase 5.**
- Note: CricketAnalyzer already measures spin directly with colored stickers + PnP — but
  that's for nets/training, not matches.

### Crease line detection
- Thick white line on green grass. HSV threshold + Hough line transform.
- **Trivially solvable.** Not the hard part.

### Stump/bail detection
- Roboflow datasets exist: 844 images (Cardiff University) + 826 images (FAST NUCES)
  with annotated stumps.
- YOLOv8 pipeline exists: `sanjusabu/Cricket-Ball-and-Stumps-Detection`
- **Low-Medium difficulty with existing datasets.**

### Bail-off detection
- From Camera 2 (square leg): sudden motion in the stump-top region.
- Simple motion detection / frame differencing in the stump ROI.
- LED Zing bails ($39/pair) would make this trivial (bright flash = bail off).
- **Easy without Zing bails. Trivial with them.**

---

## 9. Community Sentiment & Market

### Umpire shortage (the demand driver)
- **UK:** 56% of umpires experienced verbal abuse. 20% quit citing abuse. Many leagues
  only provide 1 standing umpire per week.
- **Australia:** Sunraysia — 13 umpires for 21 senior games (need 42). Three umpires
  over 70. Tasmania "at breaking point."
- **India:** 2,000+ domestic matches/season. Gully cricket has no neutral umpire.
  LBW rarely called because no one trusts informal umpires.

### Demand signals
- **Organic grassroots demand: WEAK.** No Reddit/Twitter threads asking for amateur DRS.
- **Institutional demand: MODERATE.** Cricket Australia interested in Fulltrack.
  Darwin trial happened. CPL 2026 announced AI umpires.
- **"Spirit of the game" is NOT a barrier.** Cost and setup friction are the real objections.
  One club (Nightcliff CC) declined Fulltrack trial due to cost, not philosophy.
- **The buyer is leagues/associations, not individual clubs.** Top-down adoption.

### Market size
- ~125,000 cricket clubs worldwide, ~30,000 in India alone
- Cricket tech has <$20M total early-stage VC for 2.5B fans — "starved of capital"
- Indian sports economy $2.13B, cricket = 89%
- At 1% club adoption × $100/year = $125K ARR
- At 50 league deals × $5K/year = $250K ARR
- This is a sustainable side project, not a unicorn — which matches the founder's intent
  ("I don't care if I don't make money, if I can build something that helps people")

### Key market dynamics
- **IPL media rights:** $6.2B (2023-2028). Cricket is exploding commercially.
- **ICC expanding:** T20 World Cup → 20 teams. USA Major League Cricket launched.
- **Leagues WANT technology.** Darwin trial, CPL AI umpires, IPL Hawk-Eye for wides.
- **Amateur level has almost nothing.** Fulltrack is the only real product.

---

## 10. Existing Resources — GitHub Repos, Datasets, Footage

### Full details in `cricket-cv-research.md`. Highlights:

#### Most useful GitHub repos
| Repo | What | Stars | Relevance |
|---|---|---|---|
| `sanjusabu/Cricket-Ball-and-Stumps-Detection` | YOLOv8 ball + stumps detection | 1 | **HIGH** — stump detection with Roboflow data |
| `kushagra3204/Cricket-Ball-Trajectory-Prediction` | YOLOv8 ball detection, 1778 images | 17 | **HIGH** — recent, maintained |
| `uditarora/cricket-umpire-assistance` | Umpire assistance, smartphone camera | 35 | **HIGH** — closest to our goal, but stale (2019) |
| `kabrakeshav/DRS-System-Run-Out----Cricket` | Run-out DRS system | 0 | **DIRECT** — only run-out specific repo |
| `nikhil-dev/hawkeye` | 3D trajectory from single camera | 54 | **HIGH** — 3D reconstruction approach |
| TrackNet (yastrebksv) | Small fast object tracking | — | **HIGH** — gold standard for ball tracking |

#### Annotated datasets
- Roboflow: 7,452 images (ball + stump classes, YOLO/COCO export)
- Roboflow: Cardiff University stumps dataset (844 images)
- Roboflow: FAST NUCES stumps dataset (826 images + pretrained model)
- Roboflow: crease datasets (quality needs verification)
- IEEE DataPort: 10K+ annotated cricket frames (ball tracking)
- Kaggle: sample cricket video clips

#### Academic papers (directly relevant)
- "AI Third Umpire Run-out Decision Making Using Image Processing" (2021)
- "Computing Run-out Decisions Using Object Detection and SVM" (2022) — **87% accuracy**
- "Deep Transfer Learning-Based Foot No-Ball Detection" (2023) — **98% accuracy**
- "Cricket Activity Detection Using CV" — wide + no-ball detection
- "Automated Third Umpire Decision Making in Cricket Using ML" (IEEE 2020)
- TechRxiv 2026: Kalman filter 3D ball trajectory from single camera

#### Test footage (YouTube, free)
- **Cricket Australia run-outs:** youtube.com/watch?v=23ZQ3IAMvnY (Best of 2024-25)
- **Cricket Australia direct hits:** youtube.com/watch?v=zmiVWO7ab88
- **ECB run-outs:** youtube.com/watch?v=9GY8ZRrQk-E (May 2026)
- **Bairstow stumping (multi-angle):** youtube.com/watch?v=EulOKkMHkJ4
- **Third umpire room:** youtube.com/watch?v=ETOjuWXdVus
- **Go Cricket Pro (4K GoPro keeper cam):** youtube.com/c/GoCricketPro
- **"Ball HITS STUMPS! IN or OUT?":** youtube.com/watch?v=0AGCxxiUEaU
- **Last Man Stands (amateur T20):** youtube.com/@lastmanstandst20cricket
- **IPL stump cam:** youtube.com/watch?v=Yir18o7a2gI

---

## 11. Existing Codebase — What the Founder Already Has

### CricketAnalyzer (C:\Users\prana\AndroidStudioProjects\CricketAnalyzer)
**Ball spin/speed measurement app. Production-ready, validated.**

- **Tech:** Android, Java + Kotlin, Jetpack Compose, OpenCV 4.9.0, Room DB
- **What it does:** 10 colored stickers on ball → HSV blob detection → PnP pose estimation →
  frame-to-frame rotation → RPM/velocity. Real-time on-device processing.
- **Validated:** Phone pipeline matches PC reference. RPM 3.2% error, speed 0.3% error.
- **Tests:** 352 JVM + 42 instrumented tests green.
- **Key reusable components:**
  - OpenCV integration + frame extraction from video (VideoFrameExtractor.kt)
  - Frame-by-frame analysis pipeline (FrameProcessor.kt)
  - PnP pose estimation (PnPSolver.java) — reusable for camera calibration
  - RANSAC assignment (AssignmentSolver.java)
  - Video export with HUD overlay (VideoExporter.kt)
  - Room database for session/frame results
  - 5-screen Compose UI (Home, Video, Analysis, Calibration, Results)
  - CSV export, video annotation, color profile presets
- **Architecture:** MVVM, coroutines, IO/Default dispatchers
- **Deployment:** GitHub Actions CI, adb deploy script, Tailscale device

### CricketApp2 (C:\Users\prana\AndroidStudioProjects\CricketApp2)
**Cricket scoring app. Ball-by-ball entry, ICC rules.**

- Scoring, dismissal types (run-out, stumped, caught, bowled, etc.), extras
- Full ICC rules (wides, no-balls, 8 dismissal types)
- MVVM + Room DB
- **Eventually:** "disputed decision" button → opens adjudication → result flows to scorecard

### Architecture decision
- **CricketAnalyzer = CV engine.** Run-out detection, ball tracking, frame analysis live here.
  Already has OpenCV, video processing, frame extraction.
- **CricketApp2 = match management platform.** Scoring, match flow, decisions.
- **New module/feature in CricketAnalyzer** for adjudication, not a new app.
- Eventually: CricketApp2 calls CricketAnalyzer for reviews.

---

## 12. Why Run-Out Detection is Technically Easier than LBW

| Dimension | LBW (Fulltrack's problem) | Run-out (our problem) |
|---|---|---|
| Core question | Where WOULD the ball have gone? (prediction) | Where IS the bat/foot? (observation) |
| Dimensionality | 3D trajectory from 2D (ill-posed) | 2D spatial analysis (side-on camera) |
| Physics model needed | Yes — gravity, bounce, spin, seam, pitch | No — pure geometry |
| Depth estimation | Critical and hard | Not needed |
| Training data needed | Millions of deliveries | Hundreds of labeled frames |
| Camera position | Behind bowler (depth matters) | Square leg (depth irrelevant) |
| Decision type | Probabilistic | Binary / deterministic |
| Patent risk | Fulltrack patent covers this | Different problem, different approach |
| Accuracy bar | Must predict trajectory to within stump width | Must identify bat position ± few cm |

---

## 13. Strategy — How We Enter the Market

### Strategy 3: Start with the gap, expand to compete

1. Ship run-out/stumping/wide frame capture (the unfilled gap)
2. This gets users, footage data, league relationships
3. Add ball analytics (speed, pitch maps) to match Fulltrack's core
4. Add LBW when we have data and distribution
5. **This is what Fulltrack did in reverse** — they started with analytics, added DRS later

### Why not replicate Fulltrack first?
- Their moat is data (1M deliveries). We'd start with zero.
- Their founding team has deep CV credentials (UW PhD, Second Spectrum). Hard to out-tech.
- Their patent covers the 3D trajectory approach.
- LBW is the hardest problem. Run-outs are easier and unfilled.

### Positioning options
- **Complement Fulltrack** — "the other half of amateur DRS" (leagues buy both)
- **Full competitor** — do everything they do + what they don't (long term)
- **Get acquired** — build the run-out capability, Fulltrack or a cricket board acquires it

---

## 14. The Origin — How We Got Here

### The Opus conversation (validation/opus.txt)
Founder had Opus (without project context) evaluate the injuryShield running gait wearable.
Opus gave a devastating critique: "bottom decile of ideas by expected value." ~dozen funded
teams tried and died. Value failure, not GTM failure. Then Opus identified cricket
adjudication as structurally better: real dispute, no incumbent owns the tractable calls,
setup complexity is the moat, founder has surplus passion for cricket.

### The pivot
Founder agreed: "my gut tells me to abandon the wearable project and work on cricket."
injuryShield was formally closed (DECISIONS.md updated, repo stays public as reference).
Research methodology (kill-register, cheapest-test-first) transfers to the new project.

### What transfers from injuryShield
- Research discipline: cheapest test first, never report sensitivity without flag rate
- Kill-register methodology (VIABILITY.md)
- "A day of research beats a month of building"
- File hygiene: DECISIONS.md as single source of truth, supersession banners, corpus cap
- Hardware economics knowledge (BOM, certification)
- Market research rigor (competitive teardowns, failure archaeology)

---

## 15. Immediate Next Steps for Next Session

### Weekend test (zero cost, proves/kills the concept)
1. Download 10-15 run-out clips from YouTube (Cricket Australia, ECB compilations)
2. Extract frames from side-on replays
3. In CricketAnalyzer's OpenCV pipeline:
   - Crease line detection (HSV white threshold + Hough transform)
   - Stump detection (use Roboflow dataset or color/shape detection)
   - Bail movement detection (frame differencing in stump-top ROI)
4. Can you reliably identify the crease line and the frame where bails come off?
5. If yes → the concept works. If no → understand why and whether it's solvable.

### Project setup
- Create new repo (e.g., `cricket-umpire` or `cricket-review`)
- Copy relevant research files from injuryShield/validation/
- Set up CLAUDE.md, DECISIONS.md, VIABILITY.md, TRACKER.md
- Port the kill-register methodology

### Read these papers first
1. "AI Third Umpire Run-out Decision Making" — closest to our problem
2. "Deep Transfer Learning-Based Foot No-Ball Detection" — crease + foot detection (98%)
3. "Computing Run-out Decisions Using Object Detection and SVM" — 87% accuracy
4. TechRxiv 2026 Kalman filter paper — 3D ball trajectory from single camera (for Phase 2)

### Download these datasets
1. Roboflow Cardiff stumps dataset (844 images)
2. Roboflow FAST NUCES stumps dataset (826 images + pretrained model)
3. Roboflow crease datasets (verify quality)
4. `sanjusabu/Cricket-Ball-and-Stumps-Detection` repo

---

## 16. Key Open Questions (for the new project's kill register)

| # | Question | Risk level | How to test |
|---|---|---|---|
| K1 | Can a phone camera at square leg reliably detect bail-off and show the right frames? | **Medium** | Weekend test with YouTube clips |
| K2 | Will clubs/leagues actually pay for this, or is demand purely institutional? | **High** | 5 club/league interviews |
| K3 | Can ball speed be measured accurately enough from a phone behind the bowler? | **Medium** | Fulltrack proves yes; we need to replicate |
| K4 | Is Fulltrack going to add run-out support and close the gap? | **Medium** | Monitor their releases |
| K5 | Can multi-phone setup be made frictionless enough for amateur matches? | **Medium** | Usability testing |
| K6 | Will cricket boards mandate technology at lower levels? (adoption driver) | **Medium** | Watch Darwin trial results, ECB/CA announcements |
| K7 | Is the patent (US 20230100572) broad enough to block our LBW approach? | **Low** | Legal review when we get to Phase 6 |
| K8 | Can we build a training dataset cheaply from YouTube clips? | **Low** | Weekend test |

---

## 17. Reference Links

### Fulltrack AI
- Website: fulltrack.ai
- Pricing: fulltrack.ai/pricing
- Technology: fulltrack.ai/technology
- Darwin DRS trial: abc.net.au/news/2026-04-27/nt-ai-decision-review-system-technology-darwin-cricket/106604718
- NT Cricket announcement: ntcricket.com.au/news/4465425/australian-first-for-premier-cricket-with-ddcc-to-introduce-drs
- Patent: patents.justia.com/patent/20230100572
- Academic validation (line/length): tandfonline.com/doi/full/10.1080/14763141.2024.2381108
- Academic validation (speed): journals.sagepub.com/doi/full/10.1177/17479541241284714

### Other products
- StumpEye: stumpeye.com
- Zing Bails (club): clubs.zings.biz/club
- CricCam: criccam.com
- CricHeroes: cricheroes.com
- PitchVision: pitchvision.com

### Datasets
- Roboflow cricket: universe.roboflow.com (search "stumps", "cricket", "crease")
- IEEE DataPort: ieee-dataport.org (front pitch view dataset)
- Kaggle: kaggle.com (sample cricket video clips)
- CricSheet (ball-by-ball data, no video): cricsheet.org

### Academic papers
- Run-out SVM: researchgate.net/publication/365680809
- AI Third Umpire: researchgate.net/publication/349435248
- Foot no-ball: pmc.ncbi.nlm.nih.gov/articles/PMC10299879
- 3D ball trajectory: techrxiv.org/doi/full/10.36227/techrxiv.176761698.86519755/v1
- TrackNet: arxiv.org/abs/1907.03698
