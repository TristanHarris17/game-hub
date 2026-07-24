from pydantic import BaseModel

from datetime import datetime
from decimal import Decimal

class CheapSharkDeal(BaseModel):
    steam_app_id: int | None
    cheap_shark_id: int
    title: str
    thumbnail: str | None
    steam_rating_percent: float | None
    steam_rating_text: str | None
    steam_rating_count: int | None
    release_date: datetime | None
    normal_price: Decimal
    sale_price: Decimal | None
    savings: Decimal
    is_on_sale: bool

    @classmethod
    def from_api(cls, data: dict):
        return cls(
            steam_app_id = data.get("steamAppID"),
            cheap_shark_id = data.get("gameID"),
            title = data.get("title"),
            thumbnail = data.get("thumb"),
            steam_rating_percent = data.get("steamRatingPercent"),
            steam_rating_text = data.get("steamRatingText"),
            steam_rating_count = data.get("steamRatingCount"),
            release_date = data.get("releaseDate"),
            normal_price = Decimal(data.get("normalPrice")),
            sale_price = Decimal(data.get("salePrice")),
            savings = Decimal(data.get("savings")),
            is_on_sale = data.get("isOnSale")
        )