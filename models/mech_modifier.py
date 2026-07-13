import typing
from typing import Optional, List
from .base import Base
from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

class MechModifier(Base):
    """
        Represents a modifier that a mech may possess. Includes human-
        legible description, type, cost mod, and various stat mods.
    """
    # The database name for the table with which this class is associated
    __tablename__ = 'mech_modifiers'

    # The primary ID for the table with which this class is associated
    id: Mapped[int] = mapped_column(primary_key = True)

    # The descriptive type of this modifier (e.g. defense, ability, hybrid)
    type: Mapped[str] = mapped_column(String(20))

    # The human-legible gameplay effect of this mech modifier
    effect: Mapped[str] = mapped_column(String(500))

    # The increase or decrease in points cost for a mech with this trait
    cost_delta: Mapped[int] = mapped_column(Integer)

    # Change in close range power
    close_range_delta: Mapped[int] = mapped_column(Integer, default = 0)

    # Change in medium range power
    medium_range_delta: Mapped[int] = mapped_column(Integer, default = 0)

    # Change in long range power
    long_range_delta: Mapped[int] = mapped_column(Integer, default = 0)

    # Change in defense stat
    defense_delta: Mapped[int] = mapped_column(Integer, default = 0)

    # Change in max HP stat
    health_delta: Mapped[int] = mapped_column(Integer, default = 0)

    # Change in movement stat
    movement_delta: Mapped[int] = mapped_column(Integer, default = 0)

    # Change to action count stat
    action_delta: Mapped[int] = mapped_column(Integer, default = 0)

    # Mech/vehicle templates which use this modifier. Navigation property.
    mech_assignments: Mapped[List['MechModifierAssignment']] = relationship(
        back_populates = 'modifier'
    )

    # Instances of modifiers assigned to mechs in squadron teams
    # which refer to this particular modifier.
    # Navigation property.
    mech_team_assignments: Mapped[List['MechModifierTeamAssignment']] = \
        relationship(
            back_populates = 'modifier'
        )
