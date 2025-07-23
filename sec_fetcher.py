import requests
from bs4 import BeautifulSoup
from datetime import datetime
import re

BASE_URL = "https://www.sec.gov"
HEADERS = {
    "User-Agent": "YourAppName (your@email.com)",
    "Accept-Encoding": "gzip, deflate",
    "Host": "www.sec.gov"
}

def fetch_recent_filings(form_types=["D", "S-1"], count=25):
    feed_url = "https://www.sec.gov/cgi-bin/browse-edgar?action=getcurrent"
    response = requests.get(feed_url, headers=HEADERS)

    soup = BeautifulSoup(response.content, "html.parser")
    rows = soup.find_all("tr")[1:]  # Skip table header

    results = []

    for row in rows:
        cols = row.find_all("td")
        if len(cols) < 4:
            continue

        form_type = cols[0].text.strip()
        if form_type not in form_types:
            continue

        company_name = cols[1].text.strip()
        filing_href = cols[1].find("a")["href"]
        filing_url = BASE_URL + filing_href
        filing_date = cols[3].text.strip()

        results.append({
            "form_type": form_type,
            "company": company_name,
            "date": filing_date,
            "url": filing_url
        })

        if len(results) >= count:
            break

    return results


if __name__ == "__main__":
    filings = fetch_recent_filings()
    for filing in filings:
        print(f"{filing['date']} — [{filing['form_type']}] {filing['company']}")
        print(f"URL: {filing['url']}")
        print("-" * 60)