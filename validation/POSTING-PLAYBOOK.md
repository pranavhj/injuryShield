# Posting Playbook — Reddit & X

Everything needed to run community validation. Consolidated from
`makingDollarsInIndia/knowledge/playbook-browser-automation.md`,
`makingDollarsInIndia/knowledge/posting-strategy.md`, and its `scripts/`.

**Nothing has been posted yet.** Drafts are in `validation/reddit-twitter-drafts.md`;
machine-readable copies in `scripts/posting/posts/`.

---

## Accounts & Profiles

| Platform | Handle | Playwright profile | Verified present |
|---|---|---|---|
| Reddit | **u/pranavhj1998** | `C:/Users/prana/AppData/Local/Temp/.reddit-profile` | ✅ |
| X | **@pranavhj1998** | `C:/Users/prana/AppData/Local/Temp/.twitter-profile-pw` | ✅ |

⚠️ **`credentials.md` says the X profile is `.twitter-profile`. The working one is
`.twitter-profile-pw`.** The `-pw` suffix means Playwright's own Chromium. Chrome profiles
are NOT compatible with Playwright's bundled Chromium — never mix them.

⚠️ **The X scripts only existed in `C:/Users/prana/AppData/Local/Temp/`.** Temp gets cleaned.
Copies are now preserved at `scripts/posting/_ref_*.py`.

---

## Scripts

```
scripts/posting/
  post_reddit.py            — parameterized Reddit poster, DRY RUN BY DEFAULT
  post_twitter_thread.py    — X thread poster (native thread composer), DRY RUN BY DEFAULT
  posts/*.json              — content, one file per post
  _ref_*.py                 — preserved originals from makingDollarsInIndia + Temp
```

### Usage

```bash
cd scripts/posting

# ALWAYS dry run first. Fills the form, screenshots it, does NOT submit.
python post_reddit.py --file posts/post1-advancedrunning.json

# Only after reviewing the screenshot:
python post_reddit.py --file posts/post1-advancedrunning.json --post

# X thread — validates 280 chars and em dashes before opening a browser
python post_twitter_thread.py --file posts/thread-x.json
python post_twitter_thread.py --file posts/thread-x.json --post
```

Dry run leaves the browser open 90 seconds so you can inspect or submit by hand.
Live mode waits 8 seconds before starting so you can Ctrl+C.
Screenshots go to `C:/Users/prana/AppData/Local/Temp/injuryshield_posting/`.

### Content files ready

| File | Sub | Purpose |
|---|---|---|
| `post1-advancedrunning.json` | r/AdvancedRunning | Did a form change stick? → trigger + retention |
| `post2-running.json` | r/running | What do you blame, what did you change? → attribution |
| `post3-c25k.json` | r/C25K | Do beginners care about form? → **open question O7** |
| `post4-gaitanalysis.json` | r/AdvancedRunning | Worth paying for? → pricing + repeat (**post last**) |
| `thread-x.json` | X | 8-tweet research thread, all ≤280 chars |

---

## 🚨 The Automod Problem — Read Before Posting

Straight from the playbook:

> **"Some subreddits (e.g. r/ExperiencedDevs) auto-remove posts from accounts with no prior
> comment history. Build karma by commenting on 5-10 threads before posting."**

**u/pranavhj1998 has no history in any running subreddit.** All prior strategy targeted
r/embedded and r/ExperiencedDevs, and `engagement/log.md` is empty.

**Do this first, for at least a week:**
1. Comment genuinely on 5–10 threads in each target sub
2. The existing 80/20 rule applies: **4 helpful comments : 1 own post**
3. Only then post, one sub per week

Skipping this is the single most likely way these posts get silently removed.

---

## Timing

From `posting-strategy.md`:
- **Best window: 8–11 PM IST = US morning.** Do not post during Indian business hours.
- **Max 1 original post per platform per day.** These are staggered a week apart anyway.
- **Stagger cross-platform by 2–3 days.** Don't run Reddit and X the same day.
- **Reply to comments within 24 hours.** Threads die fast and unanswered OPs read as drive-by marketing.

---

## Known Technical Gotchas

**Reddit**
- Post button is inside **shadow DOM** (`r-post-form-submit-button`). Standard
  `document.querySelectorAll('button')` will not find it — `post_reddit.py` traverses the
  shadow root, with normal selectors as fallback.
- Flair modal is also shadow DOM: `r-post-flairs-modal` →
  `faceplate-radio-input[name="flairId"]`. Note `flairTemplateId` is the *user* flair, not
  the post flair. **If a sub requires flair, set it by hand during the 30s pause.**
- Body box: `div[role="textbox"][contenteditable="true"]`, needs `force=True` click.

**X**
- **280 chars. Em dash (—) counts as 2 bytes — use `--`.** The script validates this and
  aborts before opening a browser.
- "Unlock more on X" modal appears after early posts — dismissed automatically.
- Thread built via the native add-post button, not reply-chaining.

**General**
- **Never `taskkill //IM chrome.exe`** — kills every Chrome process on the machine.
- Write Python to a file; `python -c` breaks on quoting.
- Screenshots on failure, always.

---

## After Posting

1. Log to **`makingDollarsInIndia/engagement/log.md`** (the existing cross-platform log —
   currently empty). Format is defined at the top of that file.
2. Record findings against the open questions in `DECISIONS.md`:

| Open question | Watching for |
|---|---|
| O2 repeat purchase | Did anyone pay for gait work more than once? |
| O7 novice vs experienced | Do novices care about form at all? |
| O8 honesty as wedge | Does "boring and true" land well or read as weak? |
| O9 pricing | What have people actually paid? Worth it? |
| Trigger | Injury, coach, curiosity, race build — what dominates? |
| Substitutes | Shoes, mileage, strength, physio — what do they do instead? |

3. Update `research/demand-side.md` §5 with what comes back.

---

## If Asked "Why Do You Want To Know?"

> Honestly? I'm an engineer and a runner and I've been researching whether there's a real
> product in running gait feedback. I went in expecting to find that injury prediction works
> and came out fairly convinced it doesn't. So now I'm trying to figure out whether the thing
> that *does* have evidence behind it — short-term gait retraining — is something people
> would actually want, or whether it's a solution looking for a problem. Hence the question.
