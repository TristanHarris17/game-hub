from sqlalchemy.orm import Session

from datetime import datetime, UTC

from database.models import Game, Pricing

from schemas.deals import CheapSharkDeal

class DealRepository:
    def __init__(self, session: SessionLocal):
        self.session = session
        
    def commit(self):
        self.session.commit()

    def insert_game(self, deal_data: CheapSharkDeal) -> Game:
        """
        Inserts a game from CheapShark API deal data.
        """
        # Insert new game
        game_kwargs = {
            "steam_app_id": deal_data.steam_app_id,
            "cheap_shark_id": deal_data.cheap_shark_id,
            "title": deal_data.title,
            "thumbnail": deal_data.thumbnail,
            "steam_rating_percent": deal_data.steam_rating_percent,
            "steam_rating_text": deal_data.steam_rating_text,
            "steam_rating_count": deal_data.steam_rating_count,
            "release_date": deal_data.release_date
        }
        game = Game(**game_kwargs)
        self.session.add(game)
        self.session.flush()  # Flush to generate the game.id
        
        return game

    def insert_pricing(self, game_id: int, deal_data: CheapSharkDeal) -> Pricing:
        """
        Inserts a pricing record linked to the game.
        """            
        pricing_kwargs = {
            "normal_price": deal_data.normal_price,
            "sale_price": deal_data.sale_price,
            "savings": deal_data.savings,
            "is_on_sale": deal_data.is_on_sale
        }
        pricing = Pricing(game_id=game_id, **pricing_kwargs)
        self.session.add(pricing)
        
        return pricing

    def get_game_by_steam_app_id(self, steam_app_id: int) -> Game:
        """
        Gets a game by its steam app id.
        """
        return self.session.query(Game).filter(Game.steam_app_id == steam_app_id).first()

    def get_latest_price(self, game_id: int) -> Pricing:
        """
        Gets the latest pricing record for a game.
        """
        return self.session.query(Pricing).filter(Pricing.game_id == game_id).order_by(Pricing.timestamp.desc()).first()

    def update_game(self, deal_data: CheapSharkDeal) -> Game:
        game = self.get_game_by_steam_app_id(deal_data.steam_app_id)
        if game is None:
            return None
        
        game.cheap_shark_id = deal_data.cheap_shark_id
        game.title = deal_data.title
        game.thumbnail = deal_data.thumbnail
        game.steam_rating_percent = deal_data.steam_rating_percent
        game.steam_rating_text = deal_data.steam_rating_text
        game.steam_rating_count = deal_data.steam_rating_count
        game.release_date = deal_data.release_date
                   
        return game

    def insert_pricing_if_changed(self, game_id: int, deal_data: CheapSharkDeal) -> None:
        latest = self.get_latest_price(game_id)

        print("Database:")
        print(latest.sale_price, latest.normal_price, latest.is_on_sale)
        print("API:")
        print(deal_data.sale_price, deal_data.normal_price, deal_data.is_on_sale)

        print(latest.sale_price == deal_data.sale_price)
        print(latest.normal_price == deal_data.normal_price)
        print(latest.is_on_sale == deal_data.is_on_sale)

        print(type(latest.sale_price))
        print(type(deal_data.sale_price))

        if latest is None or latest.sale_price != deal_data.sale_price or latest.normal_price != deal_data.normal_price or latest.is_on_sale != deal_data.is_on_sale:
            self.insert_pricing(game_id, deal_data)