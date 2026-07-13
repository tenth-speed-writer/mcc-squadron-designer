import typing
from typing import Optional, List
from .base import Base
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

class PilotTrait(Base):
    """
        Represents a trait which may be possessed by a pilot.

        Assignments of these traits to a given pilot are
        handled by the pilot_trait_assignment table and
        the PilotTraitAssignment class.
    """
    # The name for this class's corresponding table in the database.
    __tablename__ = 'pilot_traits'

    # The auto-incrementing primary key for the pilot_traits table.
    id: Mapped[int] = mapped_column(primary_key=True)

    # The human-legible name of this trait. Up to 50 characters in length.
    name: Mapped[str] = mapped_column(String(50))

    # A description of the trait's gameplay impact (up to 500 characters.)
    effect: Mapped[str] = mapped_column(String(500))

    # Instances in which this trait has been assigned
    # to various pilots. A data navigation property.
    assignments: Mapped[List['PilotTraitAssignment']] = relationship(
        'PilotTraitAssignment',
        back_populates = 'trait'
    )
