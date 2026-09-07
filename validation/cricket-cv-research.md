# Cricket Computer Vision -- GitHub Repos & Footage Sources

Research date: 2026-09-06

---

## Part 1: GitHub Repositories

### Tier 1 -- Most Relevant to Run-Out / Stumping / Wide Adjudication

| Repo | Stars | Last Push | Language | What It Does | Relevance |
|------|-------|-----------|----------|-------------|-----------|
| [nikhil-dev/hawkeye](https://github.com/nikhil-dev/hawkeye) | 54 | 2018-01 | Python | Perception system for ball tracking in cricket and tennis using smartphone camera. Generates 3D trajectory from single camera. | **HIGH** -- 3D ball trajectory from a single camera is exactly what we need for wide-ball adjudication. Stale but has the core concept. |
| [uditarora/cricket-umpire-assistance](https://github.com/uditarora/cricket-umpire-assistance) | 35 | 2019-02 | Python | Cricket umpire assistance + ball tracking from a single smartphone camera. Generates 3D ball coords, visualizes trajectory, outputs umpiring decisions. | **HIGH** -- directly targets umpire decisions from smartphone video. Closest existing project to our goal. |
| [kushagra3204/Cricket-Ball-Trajectory-Prediction](https://github.com/kushagra3204/Cricket-Ball-Trajectory-Prediction) | 17 | 2025-03 | Python | YOLOv8-based ball detection + trajectory prediction. Custom dataset of 1778 annotated images from YouTube. | **HIGH** -- recent, actively maintained, YOLOv8 ball detection with real dataset. Trajectory prediction directly useful. |
| [sanjusabu/Cricket-Ball-and-Stumps-Detection](https://github.com/sanjusabu/Cricket-Ball-and-Stumps-Detection) | 1 | 2023-07 | Jupyter | Roboflow + YOLOv8 for detecting cricket ball AND stumps. | **HIGH** -- stump detection is critical for run-out and stumping adjudication. |
| [kabrakeshav/DRS-System-Run-Out----Cricket](https://github.com/kabrakeshav/DRS-System-Run-Out----Cricket) | 0 | 2019-12 | Python | DRS system specifically for run-out decisions. | **DIRECT** -- targets run-out, but very old and zero stars. Likely a student project. Worth reading for approach. |
| [docsallover/lbw-detection-in-cricket](https://github.com/docsallover/lbw-detection-in-cricket) | 5 | 2025-02 | Python | LBW detection using OpenCV + NumPy. Identifies ball, batsman, pitch. | **MEDIUM** -- LBW is adjacent. The pitch/ball/batsman detection pipeline is reusable. |

### Tier 2 -- Useful Components (Ball Tracking, Object Detection)

| Repo | Stars | Last Push | Language | What It Does | Relevance |
|------|-------|-----------|----------|-------------|-----------|
| [akraimit/CTRXNet](https://github.com/akraimit/CTRXNet) | 4 | 2020-04 | Python | High-speed ball tracking during cricket match using CNN + heat map (TrackNet-style). | **MEDIUM** -- heat-map ball tracking approach is proven for small fast objects. |
| [fardinkhanz/Detection-and-Tracking-of-Cricket-Ball](https://github.com/fardinkhanz/Detection-and-Tracking-of-Cricket-Ball) | 1 | 2023-07 | Jupyter | YOLOv7 + BoT-SORT ball detection and tracking. 56.8% AP at 30 FPS. | **MEDIUM** -- multi-object tracking pipeline useful for tracking ball + players. |
| [siddharthksah/cricket_computer_vision_sports](https://github.com/siddharthksah/cricket_computer_vision_sports) | 2 | 2023-03 | Jupyter | YOLOv5/v8 + DeepSORT. Detects ball, bat, stumps, batsmen. | **MEDIUM** -- multi-class detection (stumps + ball + batsman) is exactly our detection stack. |
| [kushaldev75/Bat-Ball-Tracking-System](https://github.com/kushaldev75/Bat-Ball-Tracking-System) | 2 | 2021-09 | Jupyter | YOLOv5 real-time object detection on international cricket dataset. | **LOW** -- generic YOLO ball tracking. |
| [ashish-AIML/Cricket_Analytics_Computer_Vision](https://github.com/ashish-AIML/Cricket_Analytics_Computer_Vision) | 3 | 2020-09 | Python | YOLOv3 to detect ball, bat, pitch, batsman. Outputs ball speed, impact point, swing speed. | **MEDIUM** -- ball speed and impact point extraction could be useful for ball tracking at crease. |
| [rb1193/cricket-ball-tracking](https://github.com/rb1193/cricket-ball-tracking) | 1 | 2024-03 | Python | Simple ball tracker using color/shape detection. | **LOW** -- basic approach, but clean code for prototyping. |
| [MotiBaadror/cricket-video-analysis](https://github.com/MotiBaadror/cricket-video-analysis) | 7 | 2021-05 | Jupyter | Ball-bat impact point detection. Shows the frame where bat hits ball. | **LOW** -- impact detection concept could be adapted for ball-stump contact. |

### Tier 3 -- Adjacent / Action Recognition / Umpire Gestures

| Repo | Stars | Last Push | Language | What It Does | Relevance |
|------|-------|-----------|----------|-------------|-----------|
| [aaravindravi/...Umpire-Pose-Detection](https://github.com/aaravindravi/A-Dataset-and-Preliminary-Results-for-Umpire-Pose-Detection-Using-SVM-Classification-of-Deep-Feature) | 2 | 2020-02 | Python | SNOW dataset -- classifies umpire gestures (Six, No Ball, Out, Wide, No Action). SVM on deep features. | **MEDIUM** -- the "Wide" and "Out" gesture classes have a labeled dataset. Could be used to validate our output against umpire calls. |
| [zubaer93/Real-time-Human-Static-Dynamic-Gesture-Recognition](https://github.com/zubaer93/Real-time-Human-Static-Dynamic-Gesture-Recognition) | 5 | 2017-10 | Python | Cricket umpire gesture detection using Haar cascade + logistic regression. | **LOW** -- very old, but concept of detecting umpire signals is interesting for ground-truth labeling. |
| [Tasin5541/Detection-of-Cricketing-Activities-using-Deep-Learning](https://github.com/Tasin5541/Detection-of-Cricketing-Activities-using-Deep-Learning) | 4 | 2020-11 | Jupyter | Neural network to classify player/umpire actions in images. | **LOW** -- action classification, not adjudication. |
| [dvanderhaar/uj-aqa-cricketvision](https://github.com/dvanderhaar/uj-aqa-cricketvision) | 4 | 2026-07 | Jupyter | CricketVision: 8,540 video clips for Action Quality Assessment of cricket strokes. I3D-AE-LSTM architecture. | **LOW** -- batting quality, not umpiring. But the dataset and architecture are recent and well-structured. |
| [gouthamvgk/deep_cricket](https://github.com/gouthamvgk/deep_cricket) | 6 | 2018-12 | Python | Sequence model for cricket shot classification. | **LOW** -- shot classification, not relevant to adjudication. |
| [rsnk96/Cricket-Activity-Recognition](https://github.com/rsnk96/Cricket-Activity-Recognition) | 1 | 2019-01 | Python | 2D-to-3D pose estimation for cricket activity recognition. | **LOW** -- pose estimation pipeline could help detect batsman's foot position for run-out. |

### TrackNet (Not Cricket-Specific, But Key Architecture)

| Repo | Stars | Last Push | Language | What It Does | Relevance |
|------|-------|-----------|----------|-------------|-----------|
| [yastrebksv/TrackNet](https://github.com/yastrebksv/TrackNet) | -- | -- | Python | Unofficial PyTorch implementation of TrackNet -- deep learning for tracking high-speed tiny objects in sports (originally tennis). | **HIGH** -- TrackNet is the gold-standard architecture for small fast ball tracking. Paper: [arxiv.org/abs/1907.03698](https://arxiv.org/abs/1907.03698). Directly applicable to cricket ball tracking. |

### Roboflow Datasets (Pre-Annotated, Ready for Training)

| Dataset | Source | Classes | Size | Relevance |
|---------|--------|---------|------|-----------|
| [Stumps v10 -- Cardiff University](https://universe.roboflow.com/cardiff-university-moxse/stumps/dataset/10) | Roboflow | stump, batsman, ball | 844 images | **HIGH** -- annotated stumps + ball + batsman. Ready for YOLOv8/v11. |
| [Stumps Detection -- FAST NUCES](https://universe.roboflow.com/fast-nuces-9dpr4/stumps-detection) | Roboflow | stumps, wickets, ball, batsman | 826 images + pretrained model | **HIGH** -- includes pretrained model. |
| [Cricket DRS System](https://universe.roboflow.com/cricket-ball-detection-ryu9b/cricket-drs-system) | Roboflow | ball, stumps, pitch, bat | 170 images + pretrained model | **MEDIUM** -- small but directly DRS-focused. |
| [Cricket Dataset](https://universe.roboflow.com/cricket-ball-tracking-dataset/cricket-dataset-z2wkt) | Roboflow | cricket ball, stump | -- | **MEDIUM** -- ball + stump detection. |
| [Crease datasets](https://universe.roboflow.com/search?q=class:crease) | Roboflow | crease (various) | varies | **HIGH** -- crease line detection is critical for run-out. Check these for annotation quality. |

### Academic Papers (No GitHub, But Relevant)

| Paper | Year | What It Does | Relevance |
|-------|------|-------------|-----------|
| [Deep Transfer Learning-Based Foot No-Ball Detection](https://pmc.ncbi.nlm.nih.gov/articles/PMC10299879/) | 2023 | VGG16 achieves 0.98 accuracy detecting foot no-balls. Uses bowling crease + foot position. | **HIGH** -- crease line detection + foot position is the same problem as run-out (foot behind crease). |
| [Crick-net: Waist High No Balls](https://arxiv.org/pdf/1805.05974) | 2018 | CNN for detecting waist-high no-balls. | **MEDIUM** -- different detection target but same single-camera approach. |
| [Automated Third Umpire Decision Making](https://www.semanticscholar.org/paper/Automated-Third-Umpire-Decision-Making-in-Cricket-Iyer-BalaVignesh/9ce6935e0a02450205dd10fe0fe33be9769bbc41) | -- | ML-based automated third umpire for run-out and no-ball. | **HIGH** -- directly our problem. Read this paper. |
| [Medium Scale Benchmark for Cricket Excited Actions (CVPR 2024 Workshop)](https://openaccess.thecvf.com/content/CVPR2024W/CVsports/papers/Hussain_Medium_Scale_Benchmark_for_Cricket_Excited_Actions_Understanding_CVPRW_2024_paper.pdf) | 2024 | Benchmark dataset for cricket action understanding. CVPR workshop paper. | **MEDIUM** -- recent, CVPR-quality benchmark. Check if includes dismissal actions. |

### Key Observations -- GitHub Landscape

1. **No production-quality run-out or stumping detection system exists on GitHub.** Everything is student projects or proof-of-concepts. This is a gap.
2. **Ball tracking is the most developed area** -- multiple approaches (YOLO, TrackNet, color/contour) with real datasets.
3. **Stump detection exists but is basic** -- Roboflow datasets have annotated stumps, but nobody has combined stump detection + crease detection + ball tracking + timing into an adjudication system.
4. **Crease line detection is almost completely absent.** The foot no-ball paper is the closest thing. This is a key technical challenge.
5. **The umpire-assistance repo (35 stars) is the closest to our goal** -- single smartphone, umpiring decisions. But it is 7 years old and focused on ball trajectory/LBW, not run-out.
6. **TrackNet architecture is the state of the art** for small fast ball tracking. It was designed for tennis but directly applies.
7. **Roboflow has usable annotated datasets** for stumps, ball, and batsman. The crease datasets need quality verification.

---

## Part 2: Cricket Footage Sources

### YouTube -- Side-On / Crease-Level Footage

| Source | URL | Camera Angle | Quality | Crease Visible | Licensing | Notes |
|--------|-----|-------------|---------|----------------|-----------|-------|
| **Go Cricket Pro** (GoPro Village Cricket POV) | [youtube.com/@GoCricketPro](https://www.youtube.com/c/GoCricketPro) | Keeper POV, stump-level | 4K GoPro Hero 10 | Yes -- stump-cam shows crease clearly | YouTube Standard (fair use for research) | Best source for stump-level crease footage. Multiple full innings. Ball hits stumps visible. |
| **MySide of Cricket** | [youtube.com/@mysidecricket](https://www.youtube.com/@mysidecricket) | Keeper + umpire camera, close-up | HD | Yes -- close action at stumps | YouTube Standard | Village cricket in Dorset/London. ~60 games/season. Entertaining but good close-up crease footage. |
| **"Ball HITS STUMPS! IN or OUT?"** | [youtube.com/watch?v=0AGCxxiUEaU](https://www.youtube.com/watch?v=0AGCxxiUEaU) | GoPro stump-level | HD/4K | Yes | YouTube Standard | Literally a run-out decision from stump-cam perspective. Perfect test clip. |
| Run-out compilations | Search: "cricket run out compilation" | Broadcast (behind bowler + side-on replays) | HD | Yes (in replay angles) | YouTube Standard | Broadcast replays often show side-on crease views for run-out decisions. Good for training data extraction. |
| Stumping compilations | e.g. [Top 7 Fastest Stumpings](https://www.youtube.com/watch?v=Wj61ficxSzs) | Broadcast multi-angle | HD | Yes (replay angles) | YouTube Standard | Broadcast stumpings always include side-on replay. Multiple angles available. |
| **Cricket Classics** | [youtube.com/c/cricketclassics](https://www.youtube.com/c/cricketclassics) | Broadcast | HD | Varies | YouTube Standard | Full classic matches. Broadcast quality but not always crease-level. |
| Live cricket playlists | [youtube.com/playlist?list=PLPdQWkjOHWIPu0ja5Ot4IfTlx3eOAf7Zi](https://www.youtube.com/playlist?list=PLPdQWkjOHWIPu0ja5Ot4IfTlx3eOAf7Zi) | Various broadcast | Varies | Sometimes | YouTube Standard | Full match streams. Quality and angles vary. |

### Video Datasets (Academic / Open Source)

| Dataset | Source | Size | Content | Relevance |
|---------|--------|------|---------|-----------|
| **CricketVision** | [github.com/dvanderhaar/uj-aqa-cricketvision](https://github.com/dvanderhaar/uj-aqa-cricketvision) | 8,540 clips | Cricket stroke video clips with phase annotations | LOW for adjudication -- batting quality, not dismissals. But structured video dataset. |
| **Cricket Shots IPL 2023** | Kaggle (Apache 2.0) | 150+ videos per shot type | Short clips of IPL batting shots | LOW -- shot classification, not crease/run-out. But licensed properly. |
| **Front Pitch View dataset** (IEEE DataPort) | [ieee-dataport.org](https://ieee-dataport.org/documents/front-pitch-view-shot-extraction-and-ball-tracking-cricket-using-deep-learning) | 10K frames (FPV), 5K frames (PUD), 3K frames (ball tracking) | Annotated frames: pitch, umpire, ball positions | **HIGH** -- annotated ball position frames from cricket broadcasts. Directly useful. |
| **CricShot10** | Academic | 10 shot types | Video action recognition dataset from YouTube | LOW -- shot classification. |
| **Large-scale cricket actions** | Academic (arxiv 1901.03107) | 273 GB, 73M+ frames | Test/ODI/T20 untrimmed videos | **MEDIUM** -- massive but untrimmed, needs extraction. |

### CricSheet

[cricsheet.org](https://cricsheet.org/) provides ball-by-ball data in JSON/YAML/CSV for all formats (Test, ODI, T20I, IPL, BBL, etc.). **No video -- data only.** Useful for:
- Ground truth labels (was the delivery a wide? was there a run-out?)
- Matching ball-by-ball events to video timestamps if we have broadcast footage
- Building training labels by cross-referencing with video

### Amateur Cricket Streaming Platforms

| Platform | URL | Video Archive? | Camera Setup | Notes |
|----------|-----|---------------|--------------|-------|
| **CricHeroes** | [cricheroes.com](https://cricheroes.com/live-stream-page) | Yes -- AI-generated highlights after every match | Single phone camera | India's largest amateur cricket app. Live stream from mobile. AI highlights include dismissals. Massive volume of amateur footage. |
| **CricClubs** | [cricclubs.com](https://cricclubs.com/liveStream.do) | Yes -- live and on-demand | Phone or broadcasting software | US-focused cricket league platform. Streams to Facebook/YouTube. Video archives accessible. |
| **PitchVision** | [pitchvision.com](https://www.pitchvision.com/video-angles) | Yes | Multi-camera (3-4 HD feeds), side-on angle explicitly documented | Professional-grade amateur recording. Recommends "open side" camera at stump level. Best camera angle guidance for our setup. |
| **Pixellot CricketTV** | [pixellot.tv/sports/cricket](https://www.pixellot.tv/sports/cricket/) | Yes -- OTT platform | AI-automated multi-angle (bowler + batsman perspective) | Partnership with Lions Cricket Union (South Africa). Automated camera switching. Lower-league and grassroots. Expensive hardware. |
| **LastManStands** | lastmanstands.com | Unknown | Unknown | Social cricket league. No streaming info found. |

### Stock Footage

| Source | URL | Content | License | Price |
|--------|-----|---------|---------|-------|
| **Pexels** | [pexels.com/search/videos/cricket](https://www.pexels.com/search/videos/cricket/) | 5,774+ cricket videos | Free (Pexels license, no attribution required) | Free |
| **Pixabay** | [pixabay.com/videos/search/cricket%20sports](https://pixabay.com/videos/search/cricket%20sports/) | Cricket sports videos | Free (Pixabay license, no attribution) | Free |
| **iStock** | [istockphoto.com/videos/cricket-stumps](https://www.istockphoto.com/videos/cricket-stumps) | 1,100+ cricket stumps videos | Royalty-free | Paid ($15-50/clip) |
| **Adobe Stock** | [stock.adobe.com/search?k=cricket+stumps](https://stock.adobe.com/search?k=cricket+stumps) | 654K+ cricket stumps images/videos | Royalty-free | Paid |
| **Storyblocks** | [storyblocks.com/video/search/cricket](https://www.storyblocks.com/video/search/cricket) | Cricket stock footage | Royalty-free (subscription) | Subscription |

### Key Observations -- Footage

1. **The Go Cricket Pro channel is the single best source** for stump-level crease footage. GoPro mounted at stump height gives exactly the side-on crease view needed for run-out detection. 4K quality.
2. **Broadcast run-out/stumping compilations on YouTube** are the easiest way to get high-quality side-on replay footage showing crease decisions. These replays are specifically designed to show whether the batsman was in or out.
3. **CricHeroes and CricClubs have massive archives** of amateur matches recorded from single phone cameras. The volume is enormous but camera angles are uncontrolled.
4. **PitchVision has the best camera angle documentation** -- their guide specifically recommends stump-level side-on positioning. Their hardware is purpose-built for this.
5. **CricSheet has no video but is the best source for ground-truth labels** -- ball-by-ball data with wide/no-ball/run-out/stumping flags.
6. **Pexels and Pixabay are free** but unlikely to have match-action crease footage. Mostly atmosphere/stock shots.
7. **No open-source annotated dataset specifically for run-out or stumping decisions exists.** This is a dataset we would need to create.
8. **The IEEE DataPort front-pitch-view dataset** (10K annotated frames) is the most research-ready existing resource for ball tracking in cricket broadcasts.

---

## Recommended Next Steps

1. **Watch and download** the Go Cricket Pro stump-cam videos for initial prototyping
2. **Read the "Automated Third Umpire Decision Making" paper** for the closest existing approach
3. **Read the foot no-ball paper** -- crease + foot detection is the same core problem as run-out
4. **Pull the Roboflow stumps datasets** (Cardiff University + FAST NUCES) for pretrained stump detection
5. **Check the Roboflow crease datasets** for annotation quality
6. **Try TrackNet architecture** for ball tracking -- proven for small fast objects
7. **Use CricSheet data** to build ground-truth labels for training
8. **Extract run-out replay clips from YouTube compilations** as annotated training data
