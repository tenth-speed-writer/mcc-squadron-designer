import typing
from typing import Optional, List
from .base import Base
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

print("Pilot class loaded")
class Pilot(Base):
    """
        Represents a single pilot who may be assigned to
        any given mech up to one time in any given team.
    """
    # The name of the database table represented by this class.
    __tablename__ = 'pilots'

    # The primary key of the pilots table, an auto-incrementing integer.
    id: Mapped[int] = mapped_column(primary_key=True)

    # The pilot's human-legible name. Max 50 characters.
    name: Mapped[str] = mapped_column(String(50))

    # The pilot's optional bio and/or written notes about them.
    # Can be up to 1000 characters in length.
    bio: Mapped[Optional[str]] = mapped_column(String(1000))

    # Pilot-level traits possessed by this particular pilot.
    # A referential link to the PilotTraitAssignments table.
    traits: Mapped[List['PilotTraitAssignment']] = relationship(
        "PilotTraitAssignment",
        back_populates = 'pilot'
    )

    # The pilot's rank. Max 20 characters. Foreign key to the PilotLevel table.
    # One of 'Liability', 'Standard,' 'Experienced', 'Skilled', or 'Ace'. 
    rank_name: Mapped[str] = mapped_column(ForeignKey('pilot_ranks.name'))

    # Navigation property for information associated with this pilot's rank.
    rank: Mapped['PilotRank'] = relationship(
        "PilotRank",
        back_populates = 'pilots_of_rank'
    )
    
    # Team roles to which this pilot is assigned. Navigation property.
    assignments: Mapped[List['TeamAssignment']] = relationship(
        back_populates = 'pilot'
    )
