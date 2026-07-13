import typing
from typing import Optional, List
from .base import Base
from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship


class TechLevel(Base):
    """
        Represents a tech level that a mech may have.
        Affects its cost and base stat modifier.
    """
    # The name of this class's table in the database
    __tablename__ = 'tech_levels'
    
    # The tech level represented by this object. Also its primary key.
    level: Mapped[int] = mapped_column(Integer, primary_key = True)

    # A bonus given to all relevant stats based on this tech level.
    stat_modifier: Mapped[int] = mapped_column(Integer)

    # An increase in mech points cost given based on this tech level.
    cost_modifier: Mapped[int] = mapped_column(Integer)

    # Mech whichs have been assigned this tech level.
    # Navigation property.
    mechs_at_tech_level: Mapped[List['Mech']] = relationship(
        back_populates = 'tech_level'
    )
