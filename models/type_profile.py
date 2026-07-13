import typing
from typing import Optional, List
from .base import Base
from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

class TypeProfile(Base):
    """
        Represents a type profile that a mech or vehicle may be based on,
        including the various base stats associated with that type.
    """
    # This class's associated table name in the database
    __tablename__ = 'type_profile'

    # The name of this unit type (and its primary key)
    name: Mapped[str] = mapped_column(String(20), primary_key=True)

    # Base close range power
    close_range: Mapped[int] = mapped_column(Integer)

    # Base medium range power
    medium_range: Mapped[int] = mapped_column(Integer)

    # Base long range power
    long_range: Mapped[int] = mapped_column(Integer)

    # Base defense stat
    defense: Mapped[int] = mapped_column(Integer)

    # Base max health
    health: Mapped[int] = mapped_column(Integer)

    # Base movement speed
    movement: Mapped[int] = mapped_column(Integer)

    # Mechs templates which use this type profile. Navigation property.
    mechs: Mapped[List['Mech']] = relationship(
        back_populates = 'type'
    )
