# utils/sec_fetcher.py

from utils.watchlist import get_watchlist

def fetch_recent_filings():
    """
    Simulated fetch of recent SEC filings.
    In a real app, replace this with actual SEC EDGAR API calls or scraping logic.

    Returns:
        List of filings with watchlist matching flag.
    """

    # Example dummy filings data
    filings = [
        {"company": "Acme Corp", "form_type": "D", "filing_date": "2025-07-22"},
        {"company": "BetaWorks", "form_type": "S-1", "filing_date": "2025-07-20"},
        {"company": "OtherCo", "form_type": "D", "filing_date": "2025-07-19"},
        {"company": "Alphabet Inc", "form_type": "S-1", "filing_date": "2025-07-18"},
        {"company": "ZenTech Ventures", "form_type": "D", "filing_date": "2025-07-15"},
    ]

    watchlist = get_watchlist()

    # Flag filings that match any watchlist entries (case insensitive substring match)
    for filing in filings:
        filing["watchlist_match"] = any(
            wl_name.lower() in filing["company"].lower() for wl_name in watchlist
        )

    return filings