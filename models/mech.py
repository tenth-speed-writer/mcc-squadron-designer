import typing
from typing import Optional, List
from .base import Base
from sqlalchemy import String, ForeignKey, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Mech(Base):
    """
        Represents the rulebook template for a given mech (or non-mech
        vehicle.) Contains its type, tech level, and references to its
        associated traits (as well as whether they're mandatory).
    """
    # The name of this table within the database
    __tablename__ = 'mechs'

    # The unique database key for the mechs table
    id: Mapped[int] = mapped_column(primary_key = True)

    # The name of this mech (or non-mech vehicle)
    name: Mapped[str] = mapped_column(String(50))

    # An optional human-legible biographic of the mech represented
    # by this template. Maximum length of 1000 characters.
    bio: Mapped[Optional[str]] = mapped_column(String(1000))

    # Whether this is a mech (or just a vehicle).
    # Used by the GUI when generating text to decide what to call it.
    # NOTE: This could be replaced by a 'vehicle_type' string in the future!
    is_mech: Mapped[bool] = mapped_column(Boolean)

    # The name (primary key) of the type profile
    # which defines this mech's core stat block.
    type_name: Mapped[str] = mapped_column(ForeignKey('type_profile.name'))

    # The type of base statblock used by this mech
    # (e.g. Destroyer, Fortress, Duelist, etc.)
    # Navigation property.
    type: Mapped['TypeProfile'] = relationship(
        back_populates = 'mechs'
    )

    # The numeric value of the tech level corresponding to this mech.
    tech_level_value: Mapped[int] = mapped_column(
        ForeignKey('tech_levels.level')
    )

    # The tech level of this mech, including its cost and stat modifiers.
    tech_level: Mapped['TechLevel'] = relationship(
        back_populates = 'mechs_at_tech_level'
    )

    # The list of modifiers which apply to this mech,
    # along with whether those modifiers are mandatory.
    # Navigation property.
    modifiers: Mapped[List['MechModifierAssignment']] = relationship(
        back_populates = 'mech'
    )

    # A list of instances in which this mech template has been
    # referenced by team-level instances of mech modifiers.
    #   (Don't worry about it; it's a navigation property.
    #    If you need it, you'll know.)
    modifiers_in_team_assignments: Mapped[List['MechModifierTeamAssignment']] = \
        relationship(
            back_populates = 'mech'
        )
