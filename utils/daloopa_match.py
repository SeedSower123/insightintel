# utils/daloopa_match.py

def get_daloopa_matches():
    """
    Return mocked IPO signal data.
    Replace this later with a real data integration.
    """
    return [
        {
            "company": "Acme Corp",
            "signal_score": 87,
            "form_type": "D",
            "match_reason": "Recurring executive names + S-1 filed"
        },
        {
            "company": "BetaWorks",
            "signal_score": 92,
            "form_type": "S-1",
            "match_reason": "Known investor cluster"
        },
        {
            "company": "ZenTech Ventures",
            "signal_score": 75,
            "form_type": "D",
            "match_reason": "Same syndicate as IPO candidate"
        }
    ]