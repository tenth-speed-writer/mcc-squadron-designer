import typing
from typing import Optional, List
from .base import Base
from sqlalchemy import String, ForeignKey, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship


class MechModifierAssignment(Base):
    """
        Represents an instance in which a mech modifier is
        associated with a particular mech template. Also
        indicates whether it's mandatory or optional.

        NOTE: This structure presumes that a single trait
        cannot be taken more than once. Update this data
        structure if this stops being the case.
    """
    # The name of this relational table within the database.
    __tablename__ = 'mech_modifier_assignments'

    # The ID of the mech assigned with the modifier. Part of the primary key.
    mech_id: Mapped[int] = mapped_column(
        ForeignKey('mechs.id'),
        primary_key = True
    )

    # The mech to which the modifier is assigned. Navigation property.
    mech: Mapped['Mech'] = relationship(
        back_populates = 'modifiers'
    )

    # The ID of the assigned mech modifier. The other part of the primary key.
    modifier_id: Mapped[int] = mapped_column(
        ForeignKey('mech_modifiers.id'),
        primary_key = True
    )

    # The modifier assigned to the mech. Navigation property.
    modifier: Mapped['MechModifier'] = relationship(
        back_populates = 'mech_assignments'
    )

    # Whether this trait is a mandatory take for the assigned mech.
    # Defaults to false, since making one mandatory is a design decision.
    is_mandatory: Mapped[bool] = mapped_column(Boolean, default = False)
