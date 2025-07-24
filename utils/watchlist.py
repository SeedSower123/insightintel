# utils/watchlist.py

WATCHLIST = [
    "Acme Corp",
    "Alphabet Inc",
    "BetaWorks",
    "Jane Doe",
    "ZenTech"
]

def get_watchlist():
    return WATCHLIST

def add_to_watchlist(name):
    if name not in WATCHLIST:
        WATCHLIST.append(name)
        return True
    return False

def remove_from_watchlist(name):
    if name in WATCHLIST:
        WATCHLIST.remove(name)
        return True
    return False