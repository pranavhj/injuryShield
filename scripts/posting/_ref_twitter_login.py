"""Open Twitter in Playwright for manual login. Profile will be saved."""
from playwright.sync_api import sync_playwright

PROFILE = "C:/Users/prana/AppData/Local/Temp/.twitter-profile-pw"

with sync_playwright() as pw:
    ctx = pw.chromium.launch_persistent_context(
        PROFILE,
        headless=False,
        args=["--disable-blink-features=AutomationControlled"],
        viewport={"width": 1280, "height": 900},
    )
    page = ctx.pages[0] if ctx.pages else ctx.new_page()
    page.add_init_script(
        "Object.defineProperty(navigator,'webdriver',{get:()=>undefined})"
    )

    page.goto("https://x.com/login", wait_until="domcontentloaded", timeout=30000)
    print("Please log in to Twitter/X in the browser window.")
    print("Waiting for login (up to 5 minutes)...")

    for i in range(60):
        page.wait_for_timeout(5000)
        url = page.url.lower()
        if "home" in url and "login" not in url and "flow" not in url:
            print(f"Login successful! URL: {page.url}")
            break
        if i % 6 == 0 and i > 0:
            print(f"  Still waiting... ({i*5}s) URL: {page.url}")
    else:
        print("Timeout. Try again.")
        ctx.close()
        exit(1)

    page.wait_for_timeout(3000)
    page.screenshot(path="C:/Users/prana/AppData/Local/Temp/twitter_logged_in.png")
    ctx.close()
    print("Session saved! You can now run twitter_post.py")
