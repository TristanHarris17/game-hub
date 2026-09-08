from pydantic import BaseModel

from datetime import datetime
from decimal import Decimal

class GameResponseBase(BaseModel):
    id: int
    steam_app_id: int | None
    cheap_shark_id: int
    title: str
    thumbnail: str | None
    steam_rating_percent: float | None
    steam_rating_text: str | None
    steam_rating_count: int | None
    release_date: datetime | None

class GameResponse(GameResponseBase):
    is_on_sale: bool

class GameDealsResponse(GameResponseBase):
    pass