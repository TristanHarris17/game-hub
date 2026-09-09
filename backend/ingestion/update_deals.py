from database.database import Session
from database.deal_repository import DealRepository
from database.models import Game, Pricing

from api.cheapshark_api import get_deals

class UpdateDeals:
    def update_deals(self):
        session = Session()
        deal_repository = DealRepository(session)
        deals = get_deals()
        seen_games = set()

        for deal in deals:
            game = deal_repository.upsert_game(deal)
            deal_repository.insert_pricing_if_changed(game.id, deal)
            seen_games.add(game.id)

        deal_repository.update_game_sale_status(seen_games)
        deal_repository.commit()