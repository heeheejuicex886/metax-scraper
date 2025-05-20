from input.user_input import parse_args
from browser.controller import launch_browser, stop_browser
from browser.page_loader import scroll_and_get_html  # or scroll_to_bottom

def main():
    args = parse_args()
    url = f"https://twitter.com/{args.uname}"

    try:
        playwright, browser, context, page = launch_browser(headless=not args.show_browser)
        page.goto(url, timeout=15000)
        page.wait_for_selector("article", timeout=10000)
        html = scroll_and_get_html(page, scrolls=args.scrolls)

        with open(f"{args.uname}_snapshot.html", "w", encoding="utf-8") as f:
            f.write(html)

        print(f"[+] Snapshot saved for @{args.uname}")
    finally:
        stop_browser(playwright, browser)

if __name__ == "__main__":
    main()
