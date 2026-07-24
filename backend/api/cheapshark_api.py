import json
from pathlib import Path

from api.safe_request import safe_request
from schemas.deals import CheapSharkDeal

# rate limit Vars
MAX_RETRIES = 5
RETRY_DELAY = 1  # seconds
TIMEOUT = 10 # seconds
#DEBUG_DIR = Path("debug/cheapshark_api")
#DEBUG_DIR.mkdir(parents=True, exist_ok=True)

LIST_DEALS_URL = "https://www.cheapshark.com/api/1.0/deals"

params = {
    "storeID": 1,
    "pageSize": 60,
    "pageNumber": 0, 
    "onSale" : 1
}

def get_total_pages(params=params):
    """
    Fetches the total number of pages from the CheapShark API with optional parameters.
    """
    response = safe_request(LIST_DEALS_URL, params=params)
    total_pages = int(response.headers.get("x-total-page-count", 1))
    return total_pages

def get_deal_page(page, params=params):
    """
    Fetches deals from the CheapShark API with optional parameters.
    """
    params["pageNumber"] = page
    r = safe_request(LIST_DEALS_URL, params=params)

    with open(f"deals_page_{page}.json", "w", encoding="utf-8") as f:
        json.dump(r.json(), f, indent=2)
    
    return r.json()
    
def get_deals(params=params):
    """
    Fetches all deals from the CheapShark API with optional parameters.
    """
    total_pages = get_total_pages(params=params)
    pages_to_request = min(total_pages, 5) # Limit to 5 pages for testing DELETE AFTER TESTING
    total_pages = pages_to_request # DELETE THIS AFTER TESTING
    all_deals = []
    
    for page in range(total_pages):
        print(f"Fetching page {page + 1} of {total_pages}...")
        deals = get_deal_page(page, params=params)
        all_deals.extend([CheapSharkDeal.from_api(deal) for deal in deals])
    
    return all_deals
