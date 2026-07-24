from database.database import SessionLocal
from database.deal_repository import DealRepository
from database.models import Game, Pricing

from api.cheapshark_api import get_deals

class UpdateDeals:
    def update_deals(self):
        session = SessionLocal()
        deal_repository = DealRepository(session)
        deals = get_deals()

        for deal in deals:
            game = deal_repository.insert_game(deal)
            deal_repository.insert_pricing(game.id, deal)

        deal_repository.commit()
    
    def test_update_game(self):
        session = SessionLocal()
        deal_repository = DealRepository(session)
        deals = get_deals()

        for deal in deals:
            game = deal_repository.update_game(deal)
            deal_repository.insert_pricing_if_changed(game.id, deal)

        deal_repository.commit()
        print(session.query(Game).count())
        print(session.query(Pricing).count())