# Precedent Check — Does "Outright Sale + Finite Program" Work At Scale?

**Researched 2026-08-24. Answers a direct question raised against D8 (outright sale, ~$249)
and D10 (finite 8-session programme, feedback faded): has any large, well-funded company
actually run "buy the hardware once, get a genuinely time-bounded programme, no perpetual
subscription" — and if so, how did it go?**

**Headline answer: no. Among every large, well-capitalised player checked — fitness
hardware, wearables, and connected-equipment — the model that survives and scales is
hardware (sold outright or "free") *plus a perpetual subscription*. Every company that
tried hardware-plus-finite-program-only either never scaled past $30–60M raised, or (in
Peloton's own case) built literal finite/locked training programmes and then loosened the
finite structure because it fought their subscription retention economics.** The closest
things to a working "outright + finite, no subscription" pattern live outside consumer
fitness entirely — in clinical/DTx rehab sold B2B2C to a payer with a bounded per-patient
budget, which is a different buyer structure than a direct-to-consumer sale. This does not
kill D8/D10 — the unit-economics math in `unit-economics.md` still holds on its own terms —
but it means **D8 is not "the proven model," it is "the model nobody big has tested in our
exact configuration," and the gap should be closed with real CAC/repeat-purchase data (O2,
O3), not by pointing at a comparable that doesn't quite exist.**

---

## 1. THE PATTERN — Read This First

| Company | Hardware model | Programme structure | Subscription required for full value? | Scale |
|---|---|---|---|---|
| Peloton | Sold outright, price *cut* in 2025 | Structured plans exist, but the 2025 "Programs 3.0" update **removed the lock-step finite structure** | **Yes** — All-Access $49.99/mo as of Oct 2025 | $418.5M subscription rev/yr, 2.78–2.88M subscribers |
| Mirror (lululemon) | Sold outright, $1,495 | Class content, no defined end | **Yes, mandatory** — $39/mo | **Dead.** $500M acquisition, $442.7M writedown |
| Tonal | Sold outright, $4,295+ | AI coaching program, ongoing | **Yes, mandatory** — $59.95/mo | Alive, ~$204M revenue (2026), valuation fell 64% then recovered to $1.6B |
| Tempo | Sold outright, ~$2,000+ | AI form-coaching, ongoing | Yes — subscription-gated | Alive but stalled — no new funding round since 2021, 10% layoff Mar 2024 |
| Hydrow | Sold outright, $1,545–2,295 | "Journeys"/live classes, ongoing | **Yes, functionally mandatory** — without it you're limited to "Just Row" | Alive, multiple layoff rounds amid cooling demand |
| NordicTrack / iFit | Sold outright | 12-week style transformation programmes | **Yes** for interactive/coached content — "manual mode" works without it but is a stripped-down fallback, not the sold experience | Alive; iFit hit with class actions over forced software updates |
| WHOOP | **Never sold** — hardware bundled into subscription, explicitly by design | Ongoing coaching, no defined end | **Yes, by definition — subscription IS the product** | $1.1B ARR (2025), $10.1B valuation, 2.5M+ members, record-low churn |
| Oura | Sold outright, $299–399 | No structured "programme" — passive continuous scores | **No** for the three core daily scores (Sleep/Activity/Readiness); **yes** for deeper insights, trends, stress tools | $500M rev (2024) → ~$1B (2025E), $11B valuation (Oct 2025) |
| Theragun / Therabody | Sold outright, no bundled paid tier | "Coach" recovery plans exist | **No** — Coach is a free app feature, not a paywalled programme | Private, large (no clean scale figure found) |
| Reflexion Health (VERA) | Hardware (Kinect-based) sold/leased to health systems, program genuinely finite (post-op knee/hip rehab course) | **Yes — genuinely finite**, clinician-prescribed course | No consumer subscription — reimbursed/institutional | **Defunct.** $29.8M raised total, no longer active |
| Moving Analytics (Movn) | Care kit (BP cuff, activity tracker) sent to patient, sold to payer/health system | **Yes — genuinely finite**, 12-week intensive cardiac rehab phase | No consumer subscription — paid by health plan/hospital per enrolled patient | Alive, ~$30M raised, "#1 virtual cardiac rehab program in the US" (self-reported) |
| Sword Health / Kaia Health | Sensor kit + tablet (Sword) or phone-only (Kaia), sold to employer/payer | Structured MSK programme, typically weeks, but **relationship often continues** (member stays enrolled, not a hard graduation point) | No consumer subscription — paid by employer/payer per member | Alive and consolidating — Sword raised $468M, acquired Kaia for $285M (Jan 2026) |

**The dividing line is not "outright sale vs subscription." It is who pays and whether that
payer has a naturally bounded budget.** Every consumer-direct company that endures charges
an ongoing fee *regardless of whether hardware is sold, leased, or free*, because a consumer
subscriber can churn at will and the company needs recurring revenue to survive that. Every
genuinely finite-program company found here sells into a payer (hospital, health plan,
employer) whose payment is *already* structured as one bounded amount per enrolled patient —
the "graduation" concept is native to how insurance and employer benefits pay for care, not
something the vendor invented against the grain of the buyer relationship.

**We are not selling into that kind of payer. We are selling direct to a consumer runner.**
That is the gap between this project's D8/D10 model and every precedent that has "finite" in
its actual structure.

---

## 2. The Consumer Fitness Giants — Hardware Sale Is a Loss-Leader For a Subscription

### Peloton — the most direct evidence, and it cuts against a pure finite-program model
Peloton sells the Bike/Tread outright and layers a mandatory-for-full-value subscription on
top. Two facts matter most for this question:

1. **Peloton raised subscription price while cutting hardware price** — the opposite
   direction you'd expect if hardware margin were the objective. All-Access Membership rose
   from $44 to $49.99/month effective October 2025, timed with cheaper hardware. [Retail
   Dive](https://www.retaildive.com/news/peloton-raises-membership-pricing-holidays/761567/)
   confirms the hardware-price-cut/subscription-price-hike pairing; [TechRadar's
   coverage](https://www.techradar.com/news/peloton-subscription-prices-go-up-for-the-first-time-but-the-hardware-is-cheaper)
   frames it as the same trade explicitly. **The subscription, not the hardware sale, is the
   business.**
2. **Peloton built literal finite, locked-schedule training programmes — then loosened
   them.** "Programs 3.0," rolled out in 2025, changed the model so **members are no longer
   locked into a strict weekly schedule** and **can view all classes without officially
   joining** — i.e., Peloton walked back the "start, follow a fixed sequence, finish"
   structure their own programmes used to have. [Peloton
   Buddy](https://www.pelobuddy.com/programs-2025-relaunch/) documents this change directly.
   Separately, [Peloton's own retention data](https://www.trypropel.ai/resources/blogs/peloton-retention-strategy-teardown)
   shows churn runs **60% lower** for subscribers who engage with 2+ disciplines per month —
   i.e., breadth and ongoing engagement, not completing a single finite course, is what
   Peloton's own numbers say drives retention.
3. **Hardware ownership itself is the retention lever, not the programme.** Connected
   Fitness (hardware-owning) subscribers churn at roughly **1.6%/month**, versus **5.2%/month**
   for digital-only (app, no hardware) subscribers — a >3x gap — per aggregated reporting via
   [Peloton retention teardown](https://www.trypropel.ai/resources/blogs/peloton-retention-strategy-teardown).
   Separately, Peloton's own FY25 shareholder letters report churn near **1.2%/month** for
   the hardware-owning base. ([Q2 2025 shareholder letter](https://investor.onepeloton.com/static-files/9404c038-4c2e-4652-8069-c6b5cd393b46);
   [PYMNTS coverage](https://www.pymnts.com/earnings/2025/peloton-continues-comeback-with-strong-subscription-metrics/))

**Read for us:** Peloton is the single largest live experiment in "does a finite structure
help or hurt a fitness company," and their own 2025 product decision was to make programmes
*less* finite, not more. This is genuine counter-evidence to assume-nothing risk on D10 — it
does not invalidate our finite-programme bet (our mechanism is different: a graduating
retraining intervention, not an engagement-maximizing content library), but it means we
should not cite Peloton as support for "finite programmes work commercially" — their own
data points the other way for *their* business model.

### Mirror — the closest same-category cash comp, and it died
- **Pricing:** $1,495 hardware (or $32/mo × 48-month financing) **plus a mandatory $39/month**
  subscription for all class content — no offline/standalone mode of real value.
  ([mysubscriptionaddiction.com](https://www.mysubscriptionaddiction.com/b/mirror))
- **Scale/funding:** Acquired by lululemon for **$500M in 2020**.
- **Outcome:** Shut down 2023. lululemon took a **$442.7M post-tax impairment charge**,
  replaced Mirror's subscription with "lululemon Studio," then in 2023 struck a 5-year deal
  making **Peloton its exclusive digital content provider** and discontinued the Mirror
  hardware line entirely. ([SportsPro](https://www.sportspro.com/news/lululemon-peloton-mirror-connected-fitness/);
  [Yahoo Finance](https://finance.yahoo.com/news/lululemons-ill-timed-mirror-acquisition-is-now-almost-worthless-124822875.html))
- **Stated reason:** lululemon CFO Meghan Frank said the **at-home fitness category itself
  remained challenged** and **Mirror hardware sales came in below expectations** — a
  category-collapse and hardware-sell-through failure, not evidence against finite programmes
  specifically (Mirror never ran a finite-programme model — it was perpetual class content,
  same as Peloton).

**Read for us:** Mirror is proof that a large, well-capitalised company can burn $500M+ in
this exact adjacent category and still fail — but it failed at the *hardware-plus-mandatory-
perpetual-subscription* model, the opposite of what we're testing. It is evidence about
category risk (post-pandemic home-fitness demand collapse) more than about programme
structure.

### Tonal, Tempo, Hydrow, NordicTrack/iFit — same shape, none finite
All four sell hardware outright at high price points ($1,500–$4,295+) and gate the coaching/
programming layer behind mandatory monthly fees ($39–$60/mo). None of them run a
"complete-the-programme-and-you're-done" structure — content is continuous and open-ended by
design, because continuous engagement is what the subscription revenue needs.

- **Tonal**: $4,295 base + $59.95/mo mandatory membership for AI-adjusted resistance and
  coaching. Valuation fell from $1.6B to as low as $600M in 2023 (some reporting suggested
  risk of a 90% fall) before a $130M raise and partial recovery; 2026 revenue ~$204M.
  ([Forbes](https://www.forbes.com/sites/korihale/2023/03/01/athlete-investors-cant-save-tonals-falling-500-million-valuation/);
  [Athletech News](https://athletechnews.com/tonal-valuation-could-fall-90-percent/);
  [Front Office Sports](https://frontofficesports.com/tonal-raises-130m-after-big-value-drop/))
- **Tempo**: raised **$398M total** (including a $220M Series C), but hasn't closed a new
  round since 2021 and cut 10% of staff in March 2024 — still operating, not thriving.
  ([Crunchbase News](https://news.crunchbase.com/health-wellness-biotech/home-fitness-studio-tempo-gets-stronger-with-220m-series-c/))
- **Hydrow**: $1,545–$2,295 hardware, $50/mo (or $600/yr) All-Access; without it you're
  restricted to a bare "Just Row" mode. Multiple rounds of layoffs amid cooling post-pandemic
  demand. ([Crunchbase News on sector-wide cooling](https://news.crunchbase.com/health-wellness-biotech/fitness-startup-funding-falls/))
- **NordicTrack/iFit**: equipment works in unassisted "manual mode" without a subscription,
  but the sold experience — interactive trainer-led routes, transformation-style programmes —
  is subscription-gated. iFit was also hit with a **$3M class-action settlement** over
  mandatory software updates that bricked the touchscreens customers had paid for, and a
  separate horsepower-misrepresentation settlement — a caution about durability/trust risk
  when hardware value depends on a vendor-controlled software layer.
  ([Top Class Actions](https://topclassactions.com/lawsuit-settlements/closed-settlements/nordictrack-proform-ifit-class-action-settlement/))

---

## 3. The Wearable Contrast Cases — WHOOP vs Oura

### WHOOP — deliberately subscription-only, and explains why
Founder Will Ahmed has said publicly that he modeled WHOOP's business on **Fitbit's and
Peloton's public-market performance**, specifically because investors valued their
subscription revenue more highly than one-time hardware sales — and made hardware bundled
into the subscription (effectively "free," never sold outright) *by design*, starting in
2018. Ahmed: **"WHOOP membership is unique in that we believe hardware should be included
with the subscription."** ([Contrary Research](https://research.contrary.com/company/whoop);
[Medium/Ben Foster interview](https://robbiebax.medium.com/subscriptions-that-combine-hardware-and-software-with-ben-foster-chief-product-officer-of-whoop-e0972049175))

This paid off: **$1.1B ARR in 2025 (+103% YoY), $10.1B valuation (March 2026 Series G,
$575M raised), 2.5M+ members, 83% daily engagement, 50%+ of members still active daily 18
months in, and record-low churn.**
([TechCrunch](https://techcrunch.com/2026/03/31/whoop-valuation-10b-series-g-fundraise/);
[getlatka](https://getlatka.com/companies/whoop.com))

**Critical structural difference from us, already flagged in `market-teardown.md`:** WHOOP's
retention comes from a device **never taken off** — the opposite retention posture from a
gait-retraining pod donned and doffed every session for a programme designed to *end*. WHOOP
is strong evidence that subscription-only works when the hardware is worn continuously and
the value proposition is open-ended monitoring — neither of which describes our product.

### Oura — the closest big winner to a "core function works without subscription" model
- **Pricing:** ring $299–399 sold outright; optional membership **$6/month or $69/year**.
- **What works without the subscription:** the three core daily scores — **Sleep, Activity,
  Readiness** — plus battery status and basic profile. What's paywalled: deeper sleep/heart
  data screens, trend history, reports, stress tools.
  ([thewearify.com](https://thewearify.com/can-i-use-oura-ring-without-subscription/);
  [Notebookcheck on Oura defending the paywall](https://www.notebookcheck.net/Oura-defends-subscription-paywall-of-the-Oura-Ring-4.1218222.0.html))
- **Outcome:** thriving — **$500M revenue (2024) → forecast >$1B (2025) → >$1.5B (2026
  forecast)**, 5.5M rings sold, **$11B valuation** on a $900M Series E closed October 2025.
  ([CNBC](https://www.cnbc.com/2025/10/14/oura-ringmaker-valuation-fundraise.html);
  [Forerunner Ventures](https://www.forerunnerventures.com/perspectives/from-ring-to-revolution-oura-becomes-an-11-billion-company))

**Read for us:** Oura is real evidence that a large, well-funded hardware company can sell
outright and let *core* value work without a subscription while still building a large
business — but the subscription still exists and Oura has explicitly refused to drop it. And
critically, **Oura's core, non-paywalled function is passive, perpetual monitoring — not a
finite programme.** It's the closest thing to "hardware pays for itself, subscription is
pure upsell" among the winners, but it does not test the "genuinely finite, zero ongoing
revenue" question either.

### Theragun/Therabody — the pure-hardware control case
Therabody sells the Theragun outright with **no bundled paid programme at all**. Its "Coach"
structured recovery plans are a **free app feature**, not a paywalled tier.
([Therabody](https://www.therabody.com/pages/coach)) This is useful as a control: a large,
well-known recovery-hardware company chose *not* to monetize a structured-programme layer at
all, rather than either subscription-gating it (WHOOP/Tonal/Hydrow pattern) or selling it as
a bounded paid course (our D10 bet). No public revenue/scale breakdown was found specific to
Coach's commercial impact, so this is a data point about *positioning choice*, not proof of
outcome either way.

---

## 4. The Actual Closest Analogue — Clinical/DTx Rehab, Not Consumer Fitness

This is the one part of the brief worth stressing: **when a genuinely finite, "graduate and
you're done" programme bundled with hardware does exist, it lives in digital-therapeutics/
clinical rehab, sold to a payer, not to the consumer directly.**

### Reflexion Health / VERA — the failure case, and the closest true match to our product shape
- **Product:** Kinect-based motion-sensing system prescribing and tracking a **finite,
  clinician-set post-op rehab course** — primarily hip/knee replacement recovery.
- **Adherence result (the actual win):** patients using VERA completed **75–80%** of
  prescribed exercises vs a self-reported **15–40%** for traditional home PT — a huge,
  real, sourced adherence effect from real-time feedback against a structured programme.
  ([MedCityNews](https://medcitynews.com/2016/09/avatar-microsoft-kinect-may-smoothe-bundled-care/))
- **Funding:** **$29.8M total** across multiple rounds (including an $18M raise reported by
  [pharmaphorum](https://pharmaphorum.com/news/reflexion-health-secures-18bn-financing-develop-virtual-rehab)
  and a $7.5M seed from the West Health Fund).
- **Outcome:** **Defunct** — no longer an active company. Specific cause of shutdown was not
  found in public reporting (no post-mortem article located); circumstantial evidence points
  to reimbursement/institutional-sales-cycle difficulty, a pattern common to hardware sold
  into hospital systems rather than consumers, but this could not be confirmed with a direct
  source and should be treated as unverified.
- **Scale ceiling:** even with a real, measurable adherence win, Reflexion never grew past a
  $29.8M raise before going dark — an order of magnitude below every consumer-fitness
  comparable in this file. **This is the closest product-shape match to InjuryShield (device
  + real-time feedback + finite structured course, no consumer subscription) and it is also
  the smallest, most fragile company in this entire survey.**

### Moving Analytics / Movn — the working case, still small, still B2B2C
- **Product:** ships a care kit (BP cuff, activity tracker) to enrolled patients; runs a
  genuinely finite **12-week intensive cardiac rehab phase** with weekly clinician contact,
  then patients graduate.
- **Buyer:** health plans, hospitals, cardiology practices — **not the patient.** The payer
  funds a bounded per-patient engagement because that maps directly onto how cardiac rehab is
  already reimbursed.
- **Funding:** **~$30M total** raised (most recently a $20M Series A).
  ([TechCrunch](https://techcrunch.com/2022/07/08/this-cardiac-care-startup-just-landed-20m-for-virtual-rehab-services/))
- **Outcome:** alive, self-described as the **#1 virtual cardiac rehab program in the US**
  (company/press claim, not independently verified), with reported outcomes like **doubling**
  a health system's cardiac rehab participation rate.
  ([USC Viterbi coverage](https://viterbischool.usc.edu/news/2022/05/another-10-million-years-of-living-usc-viterbi-start-up-is-the-no-1-virtual-cardiac-rehab-program-in-the-u-s/))

### Sword Health / Kaia Health — MSK, structured but not strictly "finite"
Sword ships a sensor kit + tablet; Kaia is phone-camera-only. Both are sold to
**employers/payers**, and while programmes are structured around weekly progress, members
commonly **stay enrolled** rather than hitting a hard graduation/exit point the way Movn's
cardiac rehab or VERA's post-op course do — this is closer to an open-ended benefit than a
finite course. Scale is large for this category: Sword has raised **$468.1M** and just
acquired Kaia for **$285M** (Jan 2026), a real signal this category consolidates and has
real payer money behind it — but it further confirms the pattern: **even the well-funded MSK
players tend toward continued enrollment, not a hard finite structure, once real B2B revenue
is on the table.**
([Fierce Healthcare](https://www.fiercehealthcare.com/tech/sword-health-draws-up-85m-to-build-out-value-based-virtual-msk-care);
[Galen Growth](https://www.galengrowth.com/in-the-battle-for-digital-health-supremacy-sword-healths-european-roots-fuel-a-global-power-play/))

---

## 5. What This Means For InjuryShield

1. **D8 (outright sale) is not contradicted by any of this** — it remains the right model
   for the reasons already in `unit-economics.md` (cash-positive day one, no working-capital
   hole, matches a finite intervention). But it should no longer be described as "the model
   Playermaker/others have proven" without a caveat: **even Playermaker's $249 bundles a full
   year of app access**, not a hard-stop few-week programme with zero further monetization.
   No large player checked here sells hardware once with a truly finite programme and *no*
   subsequent revenue relationship of any kind.

2. **D10 (finite 8-session programme) has its best real-world support outside fitness
   entirely** — Reflexion Health's 75–80% vs 15–40% adherence result is a genuinely strong,
   sourced data point *for* the mechanism (structured, feedback-driven, time-bounded
   programme beats unsupervised home exercise on adherence). But the company that produced
   that number went dark on $29.8M, and the two DTx companies that are alive and growing
   (Movn, Sword/Kaia) both sell to a payer with a bounded budget, not to the consumer.

3. **The open question this surfaces, worth adding to `problems/TRACKER.md` / `DECISIONS.md`
   O2 (repeat-purchase rate):** if no consumer-direct company has proven "outright sale +
   truly finite programme + zero ongoing revenue" works at scale, our runway to prove it
   ourselves is thinner than the market-teardown comparables suggested. The two paths that
   *do* have working precedent are (a) bundle a year of access like Playermaker (already the
   $249+ model in `unit-economics.md` §3's renewal tier), or (b) look harder at a B2B2C
   channel — a physio/clinic or an employer — where a bounded budget per patient is the norm,
   which is exactly what `unit-economics.md` Model D (clinic channel) already proposes as a
   later channel. **This research raises Model D's priority slightly: it is the only channel
   in this entire survey where "sell once, finite programme, no consumer subscription" is an
   actually-proven structure (Movn), not just a hoped-for one.**

4. **No large player anywhere in this survey monetizes a genuinely finite consumer programme
   with zero further revenue relationship.** If InjuryShield's $249 Core with 12 months of
   app access converts to renewals at the ~25% rate assumed in `unit-economics.md`, that is
   already closer to the proven pattern (Playermaker-style year-one bundle, WHOOP/Peloton-
   style low-friction renewal upsell) than to a hard, one-time, no-further-contact sale — and
   that's a feature, not a compromise; it should be stated as the model, not softened.

---

## 6. Sources
- [Retail Dive — Peloton raises membership pricing, cuts hardware](https://www.retaildive.com/news/peloton-raises-membership-pricing-holidays/761567/) · [TechRadar — same trade](https://www.techradar.com/news/peloton-subscription-prices-go-up-for-the-first-time-but-the-hardware-is-cheaper)
- [Peloton Buddy — Programs 3.0, removal of locked schedule](https://www.pelobuddy.com/programs-2025-relaunch/) · [Peloton Buddy — Road to 10K program](https://www.pelobuddy.com/road-10k-program/)
- [Propel — Peloton retention teardown (multi-discipline churn, hardware vs digital churn)](https://www.trypropel.ai/resources/blogs/peloton-retention-strategy-teardown)
- [Peloton Q2 2025 shareholder letter](https://investor.onepeloton.com/static-files/9404c038-4c2e-4652-8069-c6b5cd393b46) · [PYMNTS — Peloton subscription metrics](https://www.pymnts.com/earnings/2025/peloton-continues-comeback-with-strong-subscription-metrics/)
- [SportsPro — lululemon shuts down Mirror](https://www.sportspro.com/news/lululemon-peloton-mirror-connected-fitness/) · [Yahoo Finance — Mirror acquisition "almost worthless"](https://finance.yahoo.com/news/lululemons-ill-timed-mirror-acquisition-is-now-almost-worthless-124822875.html) · [Mirror pricing detail](https://www.mysubscriptionaddiction.com/b/mirror)
- [Forbes — Tonal valuation fall](https://www.forbes.com/sites/korihale/2023/03/01/athlete-investors-cant-save-tonals-falling-500-million-valuation/) · [Athletech News — Tonal 90% fall risk](https://athletechnews.com/tonal-valuation-could-fall-90-percent/) · [Front Office Sports — Tonal $130M raise](https://frontofficesports.com/tonal-raises-130m-after-big-value-drop/)
- [Crunchbase News — Tempo $220M Series C / funding history](https://news.crunchbase.com/health-wellness-biotech/home-fitness-studio-tempo-gets-stronger-with-220m-series-c/) · [Crunchbase News — sector-wide fitness funding cooling, Hydrow layoffs](https://news.crunchbase.com/health-wellness-biotech/fitness-startup-funding-falls/)
- [Top Class Actions — iFit/NordicTrack settlement](https://topclassactions.com/lawsuit-settlements/closed-settlements/nordictrack-proform-ifit-class-action-settlement/)
- [Contrary Research — WHOOP business breakdown](https://research.contrary.com/company/whoop) · [Medium — Ben Foster (WHOOP CPO) on hardware-in-subscription](https://robbiebax.medium.com/subscriptions-that-combine-hardware-and-software-with-ben-foster-chief-product-officer-of-whoop-e0972049175) · [TechCrunch — WHOOP $10.1B Series G](https://techcrunch.com/2026/03/31/whoop-valuation-10b-series-g-fundraise/) · [getlatka — WHOOP revenue](https://getlatka.com/companies/whoop.com)
- [thewearify.com — Oura without subscription, what still works](https://thewearify.com/can-i-use-oura-ring-without-subscription/) · [Notebookcheck — Oura defends paywall](https://www.notebookcheck.net/Oura-defends-subscription-paywall-of-the-Oura-Ring-4.1218222.0.html) · [CNBC — Oura $11B valuation](https://www.cnbc.com/2025/10/14/oura-ringmaker-valuation-fundraise.html) · [Forerunner Ventures — Oura revenue trajectory](https://www.forerunnerventures.com/perspectives/from-ring-to-revolution-oura-becomes-an-11-billion-company)
- [Therabody — Coach (free structured recovery plans)](https://www.therabody.com/pages/coach)
- [MedCityNews — Reflexion Health VERA adherence data (75-80% vs 15-40%)](https://medcitynews.com/2016/09/avatar-microsoft-kinect-may-smoothe-bundled-care/) · [pharmaphorum — Reflexion Health $18M raise](https://pharmaphorum.com/news/reflexion-health-secures-18bn-financing-develop-virtual-rehab)
- [TechCrunch — Moving Analytics/Movn $20M Series A](https://techcrunch.com/2022/07/08/this-cardiac-care-startup-just-landed-20m-for-virtual-rehab-services/) · [USC Viterbi — Movn "#1 virtual cardiac rehab," outcomes](https://viterbischool.usc.edu/news/2022/05/another-10-million-years-of-living-usc-viterbi-start-up-is-the-no-1-virtual-cardiac-rehab-program-in-the-u-s/)
- [Fierce Healthcare — Sword Health raise/model](https://www.fiercehealthcare.com/tech/sword-health-draws-up-85m-to-build-out-value-based-virtual-msk-care) · [Galen Growth — Sword acquires Kaia, $285M](https://www.galengrowth.com/in-the-battle-for-digital-health-supremacy-sword-healths-european-roots-fuel-a-global-power-play/)
