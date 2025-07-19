import argparse
from tkinter.font import names


def parse_args():
    parser = argparse.ArgumentParser(
        description="Sockpuppet Detector CLI – Extract, Archive, and Analyze Social Media Profiles"
    )

    # Required: Twitter/X username
    parser.add_argument("uname", help="Twitter/X username without @")

    # Optional: Headless mode
    parser.add_argument("--headless", action="store_true", help="Run in headless mode")

    # Optional: Show browser during automation
    parser.add_argument("--show-browser", action="store_true", help="Display browser window (overrides headless)")

    # Optional: Use managed session
    parser.add_argument("--ualias", type=str, help="Specify a managed session alias")

    # Optional: Manual login flow
    parser.add_argument("--man-login", action="store_true", help="Launch browser for manual login")

    # Optional: Number of scrolls for scraping
    parser.add_argument("--scrolls", type=int, default=5, help="Number of scrolls to load timeline")

    return parser.parse_args()
