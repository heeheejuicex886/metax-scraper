import argparse



def parse_args():

    """User input argument flags"""
    parser = argparse.ArgumentParser(description="Sockpuppet Detector")

    # Required argument: Twitter /X handle
    parser.add_argument("uname", help="Twitter/X username without @")

    # Optional arguments
    parser.add_argument("--headless", action="store_true", help="Run in headless mode")

    # Username to bypass guest scripts
    parser.add_argument("--ualias", type=str, help="Specify a managed session alias")

    #Optional: Trigger manual login flow
    parser.add_argument("--man-login", action="store_true", help="Log in with managed session")

    #Optional: Set number of scrolls for timeline scraping
    parser.add_argument("--scrolls", type=int, default=5, help="Number of scrolls to perform when loading"
                                                               "timeline (default=5)")
    parser.add_argument(
        "--show-browser",
        action="store_true",
        help="Show the browser window during scraping (disables headless mode)"
    )

    return parser.parse_args()
