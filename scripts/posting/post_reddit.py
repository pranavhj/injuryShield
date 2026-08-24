"""Post to Reddit via Playwright, reading content from a JSON file.

Built on the proven pattern in makingDollarsInIndia/scripts/reddit_post.py plus the
shadow-DOM findings in makingDollarsInIndia/knowledge/playbook-browser-automation.md.

SAFETY: dry-run is the DEFAULT. It fills the form and screenshots it but does NOT submit.
Pass --post to actually submit.

Usage:
    python post_reddit.py --file posts/post1.json                 # dry run, fills + screenshots
    python post_reddit.py --file posts/post1.json --post          # actually submits

JSON format:
    {"subreddit": "AdvancedRunning", "title": "...", "body": "...", "flair": "Optional flair text"}
"""

import argparse
import json
import sys
import time
from pathlib import Path

from playwright.sync_api import sync_playwright

PROFILE = "C:/Users/prana/AppData/Local/Temp/.reddit-profile"
SHOT_DIR = Path("C:/Users/prana/AppData/Local/Temp/injuryshield_posting")
SHOT_DIR.mkdir(parents=True, exist_ok=True)


def shot(page, name):
    p = SHOT_DIR / f"reddit_{name}.png"
    try:
        page.screenshot(path=str(p))
        print(f"[shot] {p}")
    except Exception as e:
        print(f"[shot] failed: {e}")


def dismiss_popups(page):
    for sel in ['button:has-text("Accept all")', 'button:has-text("Accept")',
                'button:has-text("Got it")', 'button:has-text("OK")']:
        try:
            b = page.locator(sel).first
            if b.is_visible(timeout=1200):
                b.click()
                time.sleep(0.8)
        except Exception:
            continue


def logged_in(page):
    if "login" in page.url.lower():
        return False
    try:
        if page.locator('input[name="password"]').first.is_visible(timeout=1500):
            return False
    except Exception:
        pass
    return True


def wait_for_login(page):
    print("\n" + "=" * 60)
    print("NOT LOGGED IN. Log in manually in the browser window.")
    print("=" * 60 + "\n")
    page.goto("https://www.reddit.com/login", wait_until="domcontentloaded", timeout=30000)
    for i in range(60):
        time.sleep(5)
        if "login" not in page.url.lower():
            print("[info] Login detected.")
            time.sleep(2)
            return True
        if i % 6 == 0:
            print(f"[info] waiting... ({i*5}s)")
    return False


def fill_title(page, title):
    for sel in ['textarea[name="title"]', 'textarea[placeholder*="Title"]',
                'textarea[placeholder*="title"]', 'input[name="title"]', 'textarea >> nth=0']:
        try:
            el = page.locator(sel).first
            if el.is_visible(timeout=4000):
                el.click()
                time.sleep(0.3)
                el.fill(title)
                time.sleep(0.4)
                print(f"[ok] title filled via {sel}")
                return True
        except Exception:
            continue
    return False


def fill_body(page, body):
    """Playbook: div[role=textbox][contenteditable=true], force click, keyboard type."""
    for sel in ['div[role="textbox"][contenteditable="true"]',
                'div[contenteditable="true"][data-placeholder]',
                'shreddit-composer div[contenteditable="true"]']:
        try:
            els = page.locator(sel)
            for i in range(els.count()):
                el = els.nth(i)
                ph = (el.get_attribute("data-placeholder") or "") + (el.get_attribute("aria-label") or "")
                if "title" in ph.lower():
                    continue
                if el.is_visible(timeout=2000):
                    el.scroll_into_view_if_needed()
                    el.click(force=True)
                    time.sleep(0.4)
                    page.keyboard.type(body, delay=2)
                    time.sleep(1)
                    if len(el.inner_text()) > 50:
                        print(f"[ok] body filled via {sel}")
                        return True
        except Exception:
            continue
    # fallback: markdown textarea
    try:
        for sel in ['button[aria-label*="arkdown"]', 'button:has-text("Markdown")']:
            b = page.locator(sel).first
            if b.is_visible(timeout=1500):
                b.click()
                time.sleep(1)
                break
        ta = page.locator("textarea").last
        if ta.is_visible(timeout=2000):
            ta.click()
            ta.fill(body)
            print("[ok] body filled via markdown textarea")
            return True
    except Exception:
        pass
    return False


def click_submit(page):
    """Post button lives inside shadow DOM (r-post-form-submit-button). Playbook section:
    'Standard document.querySelectorAll will NOT find Post or Add buttons'."""
    # 1) shadow DOM traversal
    try:
        found = page.evaluate("""() => {
            const host = document.querySelector('r-post-form-submit-button');
            if (host && host.shadowRoot) {
                const btns = host.shadowRoot.querySelectorAll('button');
                for (const b of btns) {
                    if (!b.disabled) { b.scrollIntoView(); b.click(); return 'shadow'; }
                }
            }
            return null;
        }""")
        if found:
            print("[ok] submitted via shadow DOM")
            return True
    except Exception as e:
        print(f"[warn] shadow DOM submit failed: {e}")

    # 2) normal selectors
    for sel in ['button[slot="submit-button"]', 'button:has-text("Post")',
                'button[type="submit"]:has-text("Post")']:
        try:
            b = page.locator(sel).first
            if b.is_visible(timeout=2500):
                b.click()
                print(f"[ok] submitted via {sel}")
                return True
        except Exception:
            continue
    return False


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--file", required=True, help="JSON file with subreddit/title/body")
    ap.add_argument("--post", action="store_true", help="ACTUALLY SUBMIT (default is dry run)")
    args = ap.parse_args()

    data = json.loads(Path(args.file).read_text(encoding="utf-8"))
    sub, title, body = data["subreddit"], data["title"], data["body"]

    print(f"\n{'='*60}")
    print(f"  r/{sub}")
    print(f"  {title}")
    print(f"  body: {len(body)} chars")
    print(f"  MODE: {'LIVE POST' if args.post else 'DRY RUN (will not submit)'}")
    print(f"{'='*60}\n")

    if args.post:
        print("!! This will post publicly in 8 seconds. Ctrl+C to abort. !!")
        time.sleep(8)

    with sync_playwright() as pw:
        ctx = pw.chromium.launch_persistent_context(
            PROFILE, headless=False,
            args=["--disable-blink-features=AutomationControlled", "--no-sandbox"],
            viewport={"width": 1280, "height": 900}, locale="en-US",
        )
        page = ctx.pages[0] if ctx.pages else ctx.new_page()
        page.add_init_script("Object.defineProperty(navigator,'webdriver',{get:()=>undefined})")

        page.goto(f"https://www.reddit.com/r/{sub}/submit", wait_until="domcontentloaded", timeout=30000)
        time.sleep(4)
        dismiss_popups(page)

        if not logged_in(page):
            if not wait_for_login(page):
                shot(page, "err_login")
                ctx.close()
                sys.exit(1)
            page.goto(f"https://www.reddit.com/r/{sub}/submit", wait_until="domcontentloaded", timeout=30000)
            time.sleep(4)
            dismiss_popups(page)

        shot(page, "01_ready")

        if not fill_title(page, title):
            print("[ERROR] title field not found")
            shot(page, "err_title")
            ctx.close()
            sys.exit(1)
        time.sleep(0.8)

        if not fill_body(page, body):
            print("[WARN] could not confirm body text -- CHECK THE SCREENSHOT")
        shot(page, "02_filled")

        if not args.post:
            print("\n" + "="*60)
            print("DRY RUN COMPLETE. Form is filled but NOT submitted.")
            print(f"Review: {SHOT_DIR}/reddit_02_filled.png")
            print("Browser stays open 90s so you can inspect or submit by hand.")
            print("Re-run with --post to submit automatically.")
            print("="*60 + "\n")
            time.sleep(90)
            ctx.close()
            return

        print("\n[info] If a CAPTCHA or flair prompt appears, handle it now. Waiting 30s...")
        time.sleep(30)
        shot(page, "03_before_submit")

        if not click_submit(page):
            print("[ERROR] Post button not found. Submit manually in the open browser.")
            shot(page, "err_submit")
            time.sleep(120)
            ctx.close()
            sys.exit(1)

        time.sleep(10)
        shot(page, "04_after_submit")
        print(f"\n{'='*60}\n[RESULT] {page.url}\n{'='*60}\n")
        time.sleep(3)
        ctx.close()


if __name__ == "__main__":
    main()
