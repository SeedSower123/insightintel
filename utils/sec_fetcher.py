# utils/sec_fetcher.py

import requests
from datetime import datetime, timedelta
from utils.watchlist import get_watchlist

SEC_BASE_URL = "https://data.sec.gov"
HEADERS = {"User-Agent": "YourName your@email.com"}

def fetch_sec_filings(form_type="D", days=7):
    """
    Fetch recent SEC filings of a given form type (D or S-1) from the last X days.
    """
    now = datetime.utcnow()
    start_date = (now - timedelta(days=days)).strftime("%Y-%m-%d")
    query = f"https://www.sec.gov/cgi-bin/browse-edgar?action=getcurrent&type={form_type}&owner=exclude&output=atom"

    response = requests.get(query, headers=HEADERS)
    if response.status_code != 200:
        return []

    # Atom feed is XML, but we’ll mock this part for now since full XML parsing isn’t in scope here
    # In real implementation, use feedparser or xml.etree.ElementTree

    # TEMPORARY MOCK FOR DEMO PURPOSES:
    mock_filings = [
        {"company": "Acme Corp", "form_type": form_type, "filing_date": now.strftime("%Y-%m-%d")},
        {"company": "BetaWorks", "form_type": form_type, "filing_date": now.strftime("%Y-%m-%d")},
        {"company": "OtherCo", "form_type": form_type, "filing_date": now.strftime("%Y-%m-%d")}
    ]

    watchlist = get_watchlist()

    for filing in mock_filings:
        filing["watchlist_match"] = any(
            wl.lower() in filing["company"].lower() for wl in watchlist
        )

    return mock_filings

def get_all_recent_signals():
    """
    Combine Form D and S-1 recent filings for unified signal view.
    """
    return fetch_sec_filings("D") + fetch_sec_filings("S-1")