"""Post a validation question to r/embedded on Reddit using Playwright.

If not logged in, opens browser for manual login first.
"""

import time
import sys
from playwright.sync_api import sync_playwright, TimeoutError as PwTimeout

TITLE = "How are you guys actually handling MCU migrations?"
BODY = """\
Supply chain issues are forcing us to port about 40K LOC from STM32F4 to nRF52840. Just auditing the HAL dependencies looks like it'll take a solid week\u2014manually hunting down every HAL_SPI_*, HAL_GPIO_*, and HAL_TIM_* call to figure out the nRF Connect SDK equivalent sounds brutal.

For those who've survived this recently:

1. How long did the actual port take compared to what you originally estimated?
2. What ended up being the biggest time sink? (Peripherals, clock config, linker/startup, testing?)
3. Are you using anything to automate the HAL mapping, or just brute-forcing it manually?
4. If there was a script to scan the repo, map the STM32 calls to nRF, and spit out stub drivers, would that actually save time? Or is the API mapping the easy part and the real nightmare is elsewhere?

Every migration I've been through feels like reinventing the wheel from scratch. Curious to hear how you all handle it."""

SCREENSHOT_DIR = "/tmp"
USER_DATA_DIR = "C:/Users/prana/AppData/Local/Temp/.reddit-profile"


def save_screenshot(page, name):
    path = f"{SCREENSHOT_DIR}/reddit_post_{name}.png"
    page.screenshot(path=path)
    print(f"[screenshot] Saved: {path}")


def dismiss_cookie_popup(page):
    """Try to dismiss cookie consent popups."""
    selectors = [
        'button:has-text("Accept all")',
        'button:has-text("Accept")',
        'button:has-text("I agree")',
        'button:has-text("OK")',
        'button:has-text("Got it")',
    ]
    for sel in selectors:
        try:
            btn = page.locator(sel).first
            if btn.is_visible(timeout=1500):
                btn.click()
                print(f"[info] Dismissed cookie popup via: {sel}")
                time.sleep(1)
                return True
        except Exception:
            continue
    return False


def is_logged_in(page):
    """Check if user is logged in by looking at the current URL and page content."""
    url = page.url.lower()
    if "login" in url or "register" in url:
        return False
    # Also check if there's a login button prominently displayed
    try:
        login_form = page.locator('input[name="password"]').first
        if login_form.is_visible(timeout=2000):
            return False
    except Exception:
        pass
    return True


def wait_for_login(page, context):
    """Wait for user to log in manually."""
    print("\n" + "=" * 60)
    print("NOT LOGGED IN TO REDDIT")
    print("Please log in manually in the browser window.")
    print("The script will continue automatically once logged in.")
    print("Checking every 5 seconds...")
    print("=" * 60 + "\n")

    # Navigate to login page
    page.goto("https://www.reddit.com/login", wait_until="domcontentloaded", timeout=30000)
    time.sleep(2)

    max_wait = 300  # 5 minutes
    waited = 0
    while waited < max_wait:
        time.sleep(5)
        waited += 5
        # Check if URL changed away from login
        url = page.url.lower()
        if "login" not in url and "register" not in url:
            print(f"[info] Login detected! Current URL: {page.url}")
            time.sleep(2)
            return True
        print(f"[info] Still waiting for login... ({waited}s)")

    print("[ERROR] Timed out waiting for login after 5 minutes.")
    return False


def try_fill_body_approach_a(page):
    """Click on body textbox area and type using keyboard."""
    print("[approach A] Looking for body text area (contenteditable/textbox)...")

    selectors = [
        'div[contenteditable="true"][data-placeholder]',
        'div[role="textbox"]',
        'div[data-placeholder="Body text (optional)"]',
        '[contenteditable="true"]:not([data-placeholder*="title"]):not([aria-label*="Title"])',
        'div[slot="rte"]',
        'shreddit-composer div[contenteditable="true"]',
        'p[data-placeholder]',
    ]

    for sel in selectors:
        try:
            elements = page.locator(sel)
            count = elements.count()
            print(f"[approach A] Selector {sel}: found {count} elements")
            for i in range(count):
                el = elements.nth(i)
                if el.is_visible(timeout=2000):
                    # Skip if this looks like the title field
                    placeholder = el.get_attribute("data-placeholder") or ""
                    aria = el.get_attribute("aria-label") or ""
                    if "title" in placeholder.lower() or "title" in aria.lower():
                        print(f"[approach A] Skipping title-like element: placeholder={placeholder}")
                        continue

                    print(f"[approach A] Clicking element {i}: placeholder={placeholder}, aria={aria}")
                    el.scroll_into_view_if_needed()
                    time.sleep(0.3)
                    el.click()
                    time.sleep(0.5)
                    page.keyboard.type(BODY, delay=3)
                    time.sleep(1)
                    # Verify
                    text = el.inner_text()
                    if len(text) > 50:
                        print(f"[approach A] SUCCESS - typed {len(text)} chars")
                        return True
                    else:
                        print(f"[approach A] Text not confirmed ({len(text)} chars), trying next")
        except Exception as e:
            print(f"[approach A] Selector {sel} failed: {e}")
            continue

    return False


def try_fill_body_approach_b(page):
    """Switch to markdown mode and fill textarea."""
    print("[approach B] Looking for markdown mode toggle...")

    md_selectors = [
        'button[aria-label*="arkdown"]',
        'button:has-text("Markdown")',
        'button:has-text("Md")',
        '[data-click-id="markdown"]',
        'button[slot="md"]',
        'button[name="md"]',
    ]

    for sel in md_selectors:
        try:
            btn = page.locator(sel).first
            if btn.is_visible(timeout=2000):
                print(f"[approach B] Found markdown toggle: {sel}")
                btn.click()
                time.sleep(1)
                break
        except Exception:
            continue

    textarea_selectors = [
        'textarea[placeholder*="body"]',
        'textarea[placeholder*="Body"]',
        'textarea[name="body"]',
        'textarea',
    ]

    for sel in textarea_selectors:
        try:
            ta = page.locator(sel).first
            if ta.is_visible(timeout=3000):
                print(f"[approach B] Found textarea: {sel}")
                ta.click()
                time.sleep(0.3)
                ta.fill(BODY)
                time.sleep(1)
                val = ta.input_value()
                if len(val) > 50:
                    print(f"[approach B] SUCCESS - filled {len(val)} chars")
                    return True
        except Exception as e:
            print(f"[approach B] Selector {sel} failed: {e}")
            continue

    return False


def try_fill_body_approach_c(page):
    """Tab from title field to body and type."""
    print("[approach C] Tabbing from title to body...")
    # First click back on title to ensure focus is there
    title_selectors = [
        'textarea[name="title"]',
        'textarea[placeholder*="Title"]',
        'input[name="title"]',
    ]
    for sel in title_selectors:
        try:
            el = page.locator(sel).first
            if el.is_visible(timeout=2000):
                el.click()
                time.sleep(0.3)
                break
        except Exception:
            continue

    page.keyboard.press("Tab")
    time.sleep(0.5)
    page.keyboard.type(BODY, delay=3)
    time.sleep(1)
    print("[approach C] Typed text via Tab navigation")
    return True


def main():
    with sync_playwright() as pw:
        print(f"[info] Launching browser with profile: {USER_DATA_DIR}")
        context = pw.chromium.launch_persistent_context(
            user_data_dir=USER_DATA_DIR,
            headless=False,
            args=[
                "--disable-blink-features=AutomationControlled",
                "--no-sandbox",
            ],
            viewport={"width": 1280, "height": 900},
            locale="en-US",
        )

        page = context.pages[0] if context.pages else context.new_page()

        # Anti-detection
        page.add_init_script("""
            Object.defineProperty(navigator, 'webdriver', { get: () => undefined });
        """)

        print("[info] Navigating to r/embedded submit page...")
        page.goto("https://www.reddit.com/r/embedded/submit", wait_until="domcontentloaded", timeout=30000)
        time.sleep(4)

        save_screenshot(page, "01_loaded")

        # Dismiss cookie popup
        dismiss_cookie_popup(page)
        time.sleep(1)

        # Check if logged in
        if not is_logged_in(page):
            if not wait_for_login(page, context):
                save_screenshot(page, "error_login_timeout")
                context.close()
                sys.exit(1)
            # Navigate back to submit page after login
            print("[info] Navigating back to submit page...")
            page.goto("https://www.reddit.com/r/embedded/submit", wait_until="domcontentloaded", timeout=30000)
            time.sleep(4)
            save_screenshot(page, "02_after_login")

        dismiss_cookie_popup(page)
        time.sleep(1)

        print("[info] Logged in. Looking for title field...")

        # Dump some debug info about the page
        print(f"[debug] URL: {page.url}")
        print(f"[debug] Title: {page.title()}")

        save_screenshot(page, "03_ready")

        # Fill title
        title_filled = False
        title_selectors = [
            'textarea[name="title"]',
            'textarea[placeholder*="Title"]',
            'textarea[placeholder*="title"]',
            'input[name="title"]',
            'div[aria-label*="Title"][contenteditable="true"]',
            'textarea >> nth=0',
        ]

        for sel in title_selectors:
            try:
                title_el = page.locator(sel).first
                if title_el.is_visible(timeout=5000):
                    print(f"[info] Found title field: {sel}")
                    title_el.click()
                    time.sleep(0.3)
                    title_el.fill("")
                    time.sleep(0.2)
                    title_el.fill(TITLE)
                    time.sleep(0.5)
                    title_filled = True
                    print(f"[info] Title filled: {TITLE}")
                    break
            except Exception as e:
                print(f"[info] Title selector {sel} failed: {e}")
                continue

        if not title_filled:
            print("[ERROR] Could not find title field!")
            save_screenshot(page, "error_no_title")
            # Dump page HTML for debugging
            html = page.content()
            with open("/tmp/reddit_page_debug.html", "w", encoding="utf-8") as f:
                f.write(html)
            print("[debug] Page HTML saved to /tmp/reddit_page_debug.html")
            context.close()
            sys.exit(1)

        save_screenshot(page, "04_title_filled")
        time.sleep(1)

        # Fill body text
        body_filled = False

        if not body_filled:
            body_filled = try_fill_body_approach_a(page)

        if not body_filled:
            body_filled = try_fill_body_approach_b(page)

        if not body_filled:
            body_filled = try_fill_body_approach_c(page)

        save_screenshot(page, "05_body_filled")

        if not body_filled:
            print("[WARN] Could not confirm body text was entered. Check screenshot.")

        # CAPTCHA wait
        print("\n" + "=" * 60)
        print("If CAPTCHA appears, please solve it. Waiting 30 seconds...")
        print("=" * 60 + "\n")
        time.sleep(30)

        save_screenshot(page, "06_before_submit")
        print("[info] Pre-submit screenshot saved. Check /tmp/reddit_post_06_before_submit.png")

        # Click Post button
        post_selectors = [
            'button:has-text("Post")',
            'button[type="submit"]:has-text("Post")',
            'button[slot="submit-button"]',
            'faceplate-tracker button:has-text("Post")',
            'shreddit-submit-button button',
        ]

        post_clicked = False
        for sel in post_selectors:
            try:
                btn = page.locator(sel).first
                if btn.is_visible(timeout=3000):
                    print(f"[info] Found Post button: {sel}")
                    btn.click()
                    post_clicked = True
                    print("[info] Clicked Post button!")
                    break
            except Exception as e:
                print(f"[info] Post button selector {sel} failed: {e}")
                continue

        if not post_clicked:
            print("[ERROR] Could not find Post button!")
            save_screenshot(page, "error_no_post_btn")
            context.close()
            sys.exit(1)

        # Wait for navigation
        print("[info] Waiting for post submission...")
        time.sleep(10)

        save_screenshot(page, "07_after_submit")

        post_url = page.url
        print(f"\n{'=' * 60}")
        print(f"[RESULT] Post URL: {post_url}")
        print(f"{'=' * 60}\n")

        time.sleep(3)
        context.close()
        print("[info] Done.")


if __name__ == "__main__":
    main()
