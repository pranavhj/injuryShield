# Community Validation — Post Drafts

**Drafted 2026-08-24. NOTHING HAS BEEN POSTED.** These need your review and a manual rules
check before anything goes out.

Accounts (from `makingDollarsInIndia/credentials.md`): Reddit **u/pranavhj1998**, X
**@pranavhj1998**, both logged in with saved cookies. Posting script exists at
`makingDollarsInIndia/scripts/reddit_post.py` (Playwright).

---

## ⚠️ Read This Before Posting

**1. The account has no history in running subreddits.** All prior strategy in
`presence/reddit-strategy.md` targets r/embedded and r/ExperiencedDevs. The engagement log
is empty. **A first-ever post in r/running that reads as product research will be removed,
and the account can be flagged for that sub permanently.**

**2. I could not verify the current subreddit rules** — Reddit blocks automated fetching and
search did not surface them. **Read the sidebar and rules of each sub manually before
posting.** Known general pattern: 61% of major subreddits either ban self-promotion outright
or restrict it, and **market research / surveys usually require moderator approval by
modmail first.**

**3. Comment before you post.** Spend a week leaving genuine replies in the target subs.
Reddit visibly punishes accounts whose first action in a community is asking for something.

**4. Disclose if asked — and expect to be asked.** These are honest questions from an actual
runner, which you are. But if someone asks why you want to know, say so plainly. A
prepared line is at the bottom. Covert market research is what gets people banned; an
honest "I'm looking into building something here" is usually respected.

**5. Stagger them.** One post per week maximum, different subreddits. Not all at once.

---

## The Design: Two Populations, Same Question

`demand-side.md` §5 flagged the sharpest open question (O7):
**our evidence is in novice runners, but the money and gear appetite are in experienced
runners.** Chan's RCT enrolled novices; experienced runners spend $937–1,132/year.

**So ask the same question in both populations and compare the answers.**

| Sub | Population | Answers |
|---|---|---|
| r/C25K, r/beginnerrunning | Novices — where the evidence is | Do they even think about form? Would they pay? |
| r/AdvancedRunning, r/artc | Experienced — where the money is | Have they tried gait work? Did it stick? |
| r/running | Both, largest reach | General trigger and attribution |

---

## POST 1 — r/AdvancedRunning
**Target open question: what triggers a form change, and does it stick (O2, repeat purchase)**

**Title:** Has anyone here actually changed their running form and had it stick?

**Body:**

> I've been reading the gait retraining literature after my third calf issue in two years and
> I'm stuck between two camps.
>
> One says the stride is self-optimising and messing with it is how you get hurt. The other
> points at studies where cadence and impact retraining cut injury rates substantially.
>
> For those of you who've actually tried to change something — footstrike, cadence, whatever:
>
> 1. What made you decide to do it? Injury, a coach, a gait analysis, or just curiosity?
> 2. How did you know what to change? Video, a physio, a running store, feel?
> 3. Did it stick after you stopped consciously thinking about it?
> 4. Did anything actually improve, or did you just end up with a different set of niggles?
>
> Interested in the ones where it didn't work too — that seems underreported.

*Why this works: genuine question, shows reading, invites negative results (which builds
trust), and answers our trigger + retention questions without mentioning a product.*

---

## POST 2 — r/running
**Target open question: injury attribution (do they blame form?) and what they do about it**

**Title:** When you get injured, what do you actually blame — and what do you change?

**Body:**

> Curious how people here think about cause and effect with running injuries.
>
> When you've picked up something — shin splints, runner's knee, a calf strain — what did you
> conclude caused it? And more importantly, what did you actually *change* afterwards?
>
> I ask because the research I've been reading is surprisingly unconvincing that any single
> thing predicts injury, but everyone I talk to has a confident theory. Mine is usually "I
> ramped up too fast," and then I do it again anyway.
>
> - What did you blame?
> - What did you change — shoes, mileage, strength work, form, nothing?
> - Did the change work, or did you just get injured somewhere else later?

*Why this works: tests whether runners attribute injury to form (the JOSPT study says they
believe biomechanics matters — this checks it in the wild) and reveals the real substitute
set: shoes, mileage, strength work.*

---

## POST 3 — r/C25K or r/beginnerrunning
**Target open question: novice segment — the population Chan's RCT actually studied**

**Title:** Did anyone tell you anything about *how* to run, or just how much?

**Body:**

> Something I noticed getting back into running: every plan I found tells you how far and how
> often, and almost nothing tells you how to actually move.
>
> For people partway through a beginner plan or just finished one:
>
> 1. Has anyone — a video, a running store, a physio, a friend — told you anything about your
>    form?
> 2. Did you want that, or does it feel like something to worry about later?
> 3. If you've picked up any niggles, did form ever come up as a possible reason?
>
> Not trying to say beginners should obsess over form — mostly wondering whether it's a thing
> people want early or something that only becomes interesting once you're hurt.

*Why this works: directly tests O7. If novices don't care about form, our best evidence
sits in a segment that will not buy, and that is a significant finding.*

---

## POST 4 — r/AdvancedRunning or r/RunningShoeGeeks (LATER, only after 1–3 land)
**Target open questions: pricing (O9) and honest-vs-bold claims (O8)**

**Do not post this until at least two of the above have gone well.** This one is close
enough to product research that disclosure should be in the post itself.

**Title:** Gait analysis — worth paying for? What did you actually get?

**Body:**

> Being upfront: I'm an engineer and a runner, and I've been looking into whether there's
> anything worth building in running gait feedback. Before I waste a year on it I'd rather
> hear from people who've paid for the existing options.
>
> If you've done any of these — a running store treadmill analysis, a physio gait assessment,
> a 3D lab session, one of the phone-camera apps, or a wearable like Stryd or an insole
> system:
>
> 1. What did you pay and what did you actually get?
> 2. Did you change anything as a result, and did it last?
> 3. Would you do it again, or was it a one-time curiosity?
> 4. What would have made it genuinely worth it?
>
> Especially interested in the last one. My honest read of the research is that most of these
> products claim more than the evidence supports, and I'd rather build something boring and
> true than something impressive and wrong.

*Why this works: discloses openly, asks about willingness to pay and repeat purchase (the
two biggest unknowns), and the last line directly tests O8 — whether honesty reads as
trustworthy or as weak.*

---

## Twitter / X — @pranavhj1998

Lower stakes, different norms, disclosure is normal. Post as a thread.

**Tweet 1**
> Spent the last week reading every study I could find on whether running wearables can
> predict injury.
>
> Short answer: they can't, and the evidence against it is much stronger than the industry
> lets on.
>
> Thread on what I found 🧵

**Tweet 2**
> The definitive paper is Bahr 2016 in BJSM. To validate an injury screening test you need
> three things. Nobody has ever cleared the third.
>
> His conclusion: "there is currently no example of a screening test for sports injuries with
> adequate test properties."

**Tweet 3**
> Ruddy 2018 tested the three best-known hamstring injury risk factors with ML on elite AFL
> players.
>
> Median AUC 0.58. Between-year prediction: 0.52.
>
> That's a coin flip.

**Tweet 4**
> ACWR — the workload metric the entire industry runs on — got a proper RCT.
>
> 34 teams. 482 players. 10 months.
>
> No difference in injury rates.

**Tweet 5**
> Here's the one that surprised me most. GRF impact metrics — what your wearable calls
> "impact load" — don't track actual tibial bone load.
>
> Impact peak: r = −0.29. Loading rate: r = −0.20.
>
> Negative. 76 of 80 subject correlations pointed the wrong way.

**Tweet 6**
> But there IS something that works, and it isn't prediction.
>
> Chan et al. 2018, AJSM. 320 novice runners. Two weeks of gait retraining with real-time
> feedback. 12-month follow-up.
>
> Injury rate: 16% vs 38%. HR 0.38.

**Tweet 7**
> The pattern across everything I read:
>
> What works is the intervention, not the identification.
>
> Nobody has ever shown that screening *who* gets the intervention beats just giving it to
> everyone.

**Tweet 8**
> If you're a runner who has tried changing your form — deliberately, with any kind of
> feedback — I'd genuinely like to hear whether it stuck.
>
> Building something in this space, and the honest version of it looks very different from
> what's on the market.

*Why this works: gives real value before asking for anything, establishes credibility with
specific citations, and the ask at the end is soft. Also seeds the honest-claims positioning
publicly, which is a hedge against the Aletheia comparison.*

---

## If Asked "Why Do You Want To Know?"

> Honestly? I'm an engineer and a runner and I've been researching whether there's a real
> product in running gait feedback. I went in expecting to find that injury prediction works
> and came out fairly convinced it doesn't. So now I'm trying to figure out whether the thing
> that *does* have evidence behind it — short-term gait retraining — is something people
> would actually want, or whether it's a solution looking for a problem. Hence the question.

---

## What To Record

Log every response against the open questions in `DECISIONS.md`. Append findings to
`validation/` and update `demand-side.md` §5.

| Open question | Watching for |
|---|---|
| O2 repeat purchase | Did anyone do gait work more than once? |
| O7 novice vs experienced | Do novices care about form at all? |
| O8 honesty as wedge | Does the "boring and true" line get positive or dismissive replies? |
| O9 pricing | What have people actually paid, and did they think it was worth it? |
| Trigger | Injury, coach, curiosity, race build — what dominates? |
| Substitutes | Shoes, mileage, strength, physio — what do they do instead? |

**Also log outcomes to `makingDollarsInIndia/engagement/log.md`** — that is the existing
cross-platform engagement log and it is currently empty.
