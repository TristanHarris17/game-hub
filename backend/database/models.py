from __future__ import annotations

from typing import List
from datetime import UTC, datetime

from sqlalchemy import DateTime, ForeignKey, Integer, String, Text, Numeric, Float, Boolean, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database.database import Base


class Game(Base):
    __tablename__ = "games"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    steam_app_id: Mapped[int | None] = mapped_column(Integer, unique=True, index=True, nullable=True)
    cheap_shark_id: Mapped[int] = mapped_column(Integer, unique=True, index=True)
    title: Mapped[str] = mapped_column(Text)
    thumbnail: Mapped[str | None] = mapped_column(String(255), nullable=True, default=None)
    steam_rating_percent: Mapped[float | None] = mapped_column(Float, nullable=True)
    steam_rating_text: Mapped[str | None] = mapped_column(String(100), nullable=True)
    steam_rating_count: Mapped[int | None] = mapped_column(Integer, nullable=True)
    release_date: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    is_on_sale: Mapped[bool] = mapped_column(Boolean, default=False)

    pricing: Mapped[List[Pricing]] = relationship(back_populates="game")
    
class Pricing(Base):
    __tablename__ = "pricing"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    game_id: Mapped[int] = mapped_column(ForeignKey("games.id"), nullable=False)
    normal_price: Mapped[float] = mapped_column(Numeric(10, 2), nullable=False)
    sale_price: Mapped[float | None] = mapped_column(Numeric(10, 2), nullable=True, default=None)
    savings: Mapped[float] = mapped_column(Numeric(10, 2), nullable=False)
    timestamp: Mapped[datetime] = mapped_column(DateTime, default=lambda: datetime.now(UTC))

    __table_args__ = (UniqueConstraint("game_id", "timestamp", name="unique_game_timestamp"),)
    
    game: Mapped[Game] = relationship(back_populates="pricing")

