"""Open a Playwright browser with persistent profile for Reddit login.

Run this first, log in manually, then close the browser.
The session cookies will be saved in the profile directory.
"""

from playwright.sync_api import sync_playwright

USER_DATA_DIR = "C:/Users/prana/AppData/Local/Temp/.reddit-profile"

def main():
    with sync_playwright() as pw:
        print(f"[info] Opening browser with profile: {USER_DATA_DIR}")
        print("[info] Please log in to Reddit in the browser window.")
        print("[info] After logging in, close the browser window to save the session.\n")

        context = pw.chromium.launch_persistent_context(
            user_data_dir=USER_DATA_DIR,
            headless=False,
            args=["--disable-blink-features=AutomationControlled"],
            viewport={"width": 1280, "height": 900},
            locale="en-US",
        )

        page = context.pages[0] if context.pages else context.new_page()
        page.add_init_script("""
            Object.defineProperty(navigator, 'webdriver', { get: () => undefined });
        """)

        page.goto("https://www.reddit.com/login", wait_until="domcontentloaded", timeout=30000)

        # Wait until user closes the browser
        try:
            page.wait_for_event("close", timeout=600000)  # 10 min
        except Exception:
            pass

        print("[info] Browser closed. Session saved.")
        try:
            context.close()
        except Exception:
            pass

if __name__ == "__main__":
    main()
