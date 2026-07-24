import sys
from database.init_db import init_database
from ingestion.update_deals import UpdateDeals
from database.deal_repository import DealRepository

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "init":
        init_database()  # Call the function that creates tables
    elif len(sys.argv) > 1 and sys.argv[1] == "update":
        update_deals = UpdateDeals()
        update_deals.update_deals()
    elif len(sys.argv) > 1 and sys.argv[1] == "update-test":
        update_deals = UpdateDeals()
        update_deals.test_update_game()

"""
from api.cheapshark_api import get_deals

def testing_get_deals():
    deals = get_deals()
    print(f"Fetched {len(deals)} deals.")
    print(deals[0])

testing_get_deals()
"""
