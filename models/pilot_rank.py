import typing
from typing import Optional
from .base import Base
from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

class PilotRank(Base):
    """
        Represents a tier of experience that a pilot can have. Each tier has
        a higher cost but a better effect and, in the case of Skilled or Ace
        pilots, more pilot traits.
    """
    # The name of the database table associated with this class
    __tablename__ = 'pilot_ranks'
    
    # The name of this skill level. Max 20 chars.
    name: Mapped[str] = mapped_column(String(20), primary_key = True)

    # The human-readable effect this skill level has on gameplay (<= 500 chars)
    effect: Mapped[str] = mapped_column(String(500))

    # The cost increase applied to a mech piloted by a pilot of this rank.
    cost: Mapped[int] = mapped_column(Integer)

    # The number of Pilot Trait points available to a pilot of this rank.
    traits_added: Mapped[int] = mapped_column(Integer)

    # Pilots who bear this rank. Navigation property.
    pilots_of_rank: Mapped[List['Pilot']] = relationship(
        "Pilot",
        back_populates = 'rank'
    )
