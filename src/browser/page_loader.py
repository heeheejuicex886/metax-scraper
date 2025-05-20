import time

def scroll_and_get_html(page, scrolls=5, delay=2):
    """
    Scrolls down the page multiple times to load more content.
    Returns the final HTML content of the timeline page.
    """
    for i in range(scrolls):
        page.evaluate("window.scrollBy(0, document.body.scrollHeight);")
        time.sleep(delay)  # Let tweets load
    return page.content()
