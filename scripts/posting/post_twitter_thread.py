"""Post a THREAD to X/Twitter via Playwright.

The reference script (Temp/twitter_post.py) posts a single tweet only. This adds native
thread composition using X's "add another post" button, which is more reliable than
reply-chaining after the fact.

SAFETY: dry-run is the DEFAULT. Pass --post to actually submit.

Usage:
    python post_twitter_thread.py --file posts/thread.json           # dry run
    python post_twitter_thread.py --file posts/thread.json --post    # live

JSON format:
    {"tweets": ["first tweet", "second tweet", ...]}

Playbook constraints (makingDollarsInIndia/knowledge/playbook-browser-automation.md):
  - 280 char limit; em dash counts as 2 bytes -- use "--" instead
  - "Unlock more on X" modal appears after first posts; dismiss with "Got it"
"""

import argparse
import json
import sys
import time
from pathlib import Path

from playwright.sync_api import sync_playwright

PROFILE = "C:/Users/prana/AppData/Local/Temp/.twitter-profile-pw"
SHOT_DIR = Path("C:/Users/prana/AppData/Local/Temp/injuryshield_posting")
SHOT_DIR.mkdir(parents=True, exist_ok=True)


def shot(page, name):
    p = SHOT_DIR / f"x_{name}.png"
    try:
        page.screenshot(path=str(p))
        print(f"[shot] {p}")
    except Exception as e:
        print(f"[shot] failed: {e}")


def dismiss_modals(page):
    for sel in ['button:has-text("Got it")', 'button:has-text("Not now")',
                'button:has-text("Maybe later")', '[data-testid="app-bar-close"]']:
        try:
            b = page.locator(sel).first
            if b.is_visible(timeout=1200):
                b.click()
                print(f"[info] dismissed modal via {sel}")
                time.sleep(0.8)
        except Exception:
            continue


def validate(tweets):
    ok = True
    for i, t in enumerate(tweets, 1):
        n = len(t)
        if n > 280:
            print(f"[FAIL] tweet {i}: {n} chars -- OVER LIMIT")
            ok = False
        elif "\u2014" in t:
            print(f"[FAIL] tweet {i}: contains an em dash (counts double). Use '--'")
            ok = False
        else:
            print(f"[ok]   tweet {i}: {n} chars")
    return ok


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--file", required=True)
    ap.add_argument("--post", action="store_true", help="ACTUALLY SUBMIT (default is dry run)")
    args = ap.parse_args()

    tweets = json.loads(Path(args.file).read_text(encoding="utf-8"))["tweets"]

    print(f"\n{'='*60}\n  X THREAD -- {len(tweets)} tweets")
    print(f"  MODE: {'LIVE POST' if args.post else 'DRY RUN (will not submit)'}\n{'='*60}\n")

    if not validate(tweets):
        print("\n[ABORT] fix the tweets above first.")
        sys.exit(1)

    if args.post:
        print("\n!! This will post publicly in 8 seconds. Ctrl+C to abort. !!")
        time.sleep(8)

    with sync_playwright() as pw:
        ctx = pw.chromium.launch_persistent_context(
            PROFILE, headless=False,
            args=["--disable-blink-features=AutomationControlled"],
            viewport={"width": 1280, "height": 900},
        )
        page = ctx.pages[0] if ctx.pages else ctx.new_page()
        page.add_init_script("Object.defineProperty(navigator,'webdriver',{get:()=>undefined})")

        page.goto("https://x.com/home", wait_until="domcontentloaded", timeout=30000)
        time.sleep(5)

        if "login" in page.url.lower() or "flow" in page.url.lower():
            print("NOT LOGGED IN. Log in manually. Waiting up to 5 min...")
            for i in range(60):
                time.sleep(5)
                if "home" in page.url.lower():
                    print("[info] login detected")
                    break
                if i % 6 == 0:
                    print(f"[info] waiting... ({i*5}s)")
            else:
                shot(page, "err_login")
                ctx.close()
                sys.exit(1)

        time.sleep(2)
        dismiss_modals(page)

        # open composer
        box = page.locator('[data-testid="tweetTextarea_0"]')
        if box.count() == 0:
            try:
                page.locator('[data-testid="SideNav_NewTweet_Button"]').first.click()
                time.sleep(2)
                box = page.locator('[data-testid="tweetTextarea_0"]')
            except Exception:
                pass
        if box.count() == 0:
            print("[ERROR] compose box not found")
            shot(page, "err_nocompose")
            ctx.close()
            sys.exit(1)

        # tweet 1
        box.first.click()
        time.sleep(0.5)
        page.keyboard.type(tweets[0], delay=6)
        print(f"[ok] typed tweet 1")
        time.sleep(1)

        # subsequent tweets via the native "add" button
        for i, t in enumerate(tweets[1:], start=2):
            clicked = False
            for sel in ['[data-testid="addButton"]', 'button[aria-label*="Add post"]',
                        'button[aria-label*="Add another post"]']:
                try:
                    b = page.locator(sel).first
                    if b.is_visible(timeout=2500):
                        b.click()
                        clicked = True
                        break
                except Exception:
                    continue
            if not clicked:
                print(f"[ERROR] could not find 'add post' button for tweet {i}")
                shot(page, f"err_add_{i}")
                break
            time.sleep(1)
            nb = page.locator(f'[data-testid="tweetTextarea_{i-1}"]')
            if nb.count() == 0:
                print(f"[ERROR] textarea {i-1} not found")
                shot(page, f"err_box_{i}")
                break
            nb.first.click()
            time.sleep(0.4)
            page.keyboard.type(t, delay=6)
            print(f"[ok] typed tweet {i}")
            time.sleep(0.8)

        shot(page, "01_composed")

        if not args.post:
            print("\n" + "="*60)
            print("DRY RUN COMPLETE. Thread is composed but NOT posted.")
            print(f"Review: {SHOT_DIR}/x_01_composed.png")
            print("Browser stays open 90s -- inspect, or hit 'Post all' by hand.")
            print("Re-run with --post to submit automatically.")
            print("="*60 + "\n")
            time.sleep(90)
            ctx.close()
            return

        posted = False
        for sel in ['[data-testid="tweetButtonInline"]', '[data-testid="tweetButton"]',
                    'button:has-text("Post all")', 'button:has-text("Post")']:
            try:
                b = page.locator(sel).first
                if b.is_visible(timeout=2500) and b.is_enabled():
                    b.click()
                    print(f"[ok] posted via {sel}")
                    posted = True
                    break
            except Exception:
                continue

        if not posted:
            print("[ERROR] post button not found. Submit manually in the open browser.")
            shot(page, "err_nopost")
            time.sleep(120)
            ctx.close()
            sys.exit(1)

        time.sleep(8)
        shot(page, "02_after_post")
        print(f"\n[RESULT] {page.url}\n")
        time.sleep(3)
        ctx.close()


if __name__ == "__main__":
    main()
