import time


def scroll_and_get_html(page, scrolls=5, delay=2):
    """
    Scrolls the page down multiple times and returns the final HTML.

    Args:
        page: The Playwright Page object.
        scrolls: Number of times to scroll.
        delay: Time in seconds to wait between scrolls.

    Returns:
        str: The full HTML content after scrolling.
    """
    for _ in range(scrolls):
        page.evaluate("window.scrollBy(0, document.body.scrollHeight);")
        time.sleep(delay)

    return page.content()
