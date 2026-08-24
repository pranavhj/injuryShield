"""Post first tweet on Twitter/X. If not logged in, prompt user to log in."""
import sys
from playwright.sync_api import sync_playwright

PROFILE = "C:/Users/prana/AppData/Local/Temp/.twitter-profile-pw"

TWEET = "TIL about Section 44ADA in Indian tax law -- if you're a software consultant earning foreign currency, you only pay tax on 50% of gross receipts. Effective rate: ~8-9%. Add GST LUT for 0% GST on exports. Wild how founder-friendly India's tax structure is for solo devs."


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

    print("Navigating to Twitter/X...")
    page.goto("https://x.com/home", wait_until="domcontentloaded", timeout=30000)
    page.wait_for_timeout(5000)
    print(f"URL: {page.url}")

    # Check if logged in
    if "login" in page.url.lower() or "flow" in page.url.lower():
        print("NOT LOGGED IN. Please log in manually in the browser window.")
        print("Waiting up to 5 minutes for login...")
        for i in range(60):
            page.wait_for_timeout(5000)
            if "home" in page.url.lower():
                print("Login detected!")
                break
            if i % 6 == 0:
                print(f"  Still waiting... ({i*5}s)")
        else:
            print("Login timeout. Please run this script again after logging in.")
            page.screenshot(path="C:/Users/prana/AppData/Local/Temp/twitter_login_timeout.png")
            ctx.close()
            sys.exit(1)

    page.wait_for_timeout(2000)
    page.screenshot(path="C:/Users/prana/AppData/Local/Temp/twitter_home.png")

    # Find the tweet compose box
    # Twitter uses a contenteditable div with data-testid="tweetTextarea_0"
    print("Looking for compose box...")
    compose = page.locator('[data-testid="tweetTextarea_0"]')
    if compose.count() > 0:
        compose.first.click()
        page.wait_for_timeout(500)
        page.keyboard.type(TWEET, delay=8)
        print("Tweet typed")
        page.wait_for_timeout(1500)
        page.screenshot(path="C:/Users/prana/AppData/Local/Temp/twitter_typed.png")

        # Click the Post/Tweet button
        post_btn = page.locator('[data-testid="tweetButtonInline"]')
        if post_btn.count() > 0:
            post_btn.first.click()
            print("Tweet posted!")
        else:
            print("No inline tweet button, trying other selectors...")
            # Try the generic post button
            for sel in ['[data-testid="tweetButton"]', 'button:has-text("Post")', 'button:has-text("Tweet")']:
                btn = page.locator(sel)
                if btn.count() > 0:
                    btn.first.click()
                    print(f"Tweet posted via {sel}!")
                    break
            else:
                print("Could not find post button")
                page.screenshot(path="C:/Users/prana/AppData/Local/Temp/twitter_nopost.png")
    else:
        print("No compose box found on home page")
        # Try clicking the compose tweet button first
        compose_btn = page.locator('[data-testid="SideNav_NewTweet_Button"]')
        if compose_btn.count() > 0:
            compose_btn.first.click()
            page.wait_for_timeout(2000)
            compose2 = page.locator('[data-testid="tweetTextarea_0"]')
            if compose2.count() > 0:
                compose2.first.click()
                page.wait_for_timeout(500)
                page.keyboard.type(TWEET, delay=8)
                print("Tweet typed via modal")
                page.wait_for_timeout(1500)
                post_btn = page.locator('[data-testid="tweetButton"]')
                if post_btn.count() > 0:
                    post_btn.first.click()
                    print("Tweet posted via modal!")
        else:
            print("No compose button found")
            page.screenshot(path="C:/Users/prana/AppData/Local/Temp/twitter_nocompose.png")

    page.wait_for_timeout(5000)
    page.screenshot(path="C:/Users/prana/AppData/Local/Temp/twitter_done.png")
    ctx.close()
    print("DONE")
