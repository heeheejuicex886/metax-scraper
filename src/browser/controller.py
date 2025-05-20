# src/browser/controller.py

from playwright.sync_api import sync_playwright

def launch_browser(headless=True):
    """
    Launches a Chromium browser and returns:
    (playwright, browser, context, page)
    """
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=headless)
    context = browser.new_context()
    page = context.new_page()
    return playwright, browser, context, page

def stop_browser(playwright, browser):
    """
    Ensures clean shutdown of browser and Playwright engine.
    """
    if browser:
        browser.close()
    if playwright:
        playwright.stop()
