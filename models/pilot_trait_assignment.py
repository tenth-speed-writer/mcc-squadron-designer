from .base import Base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, MappedColumn, mapped_column, relationship

class PilotTraitAssignment(Base):
    """
        Represents an instance of a single specified pilot
        possessing a single specified pilot trait.
    """
    # The name of this relational table in the database.
    # Strictly you could call it "pilots_traits" but that's...
    # neither very descriptive nor especially easy to read.
    __tablename__ = 'pilot_trait_assignments'

    # The ID of the pilot who possesses the specified pilot trait.
    pilot_id: Mapped[int] = mapped_column(
        ForeignKey('pilots.id'),
        primary_key = True
    )

    # Navigation reference to the pilot associated with this assignment.
    pilot: Mapped["Pilot"] = relationship(
        back_populates = 'traits'
    )

    # The ID of the pilot trait possessed by the specified pilot.
    pilot_trait_id: Mapped[int] = mapped_column(
        ForeignKey('pilot_traits.id'),
        primary_key = True
    )

    # Navigation reference to the trait associated with this assignment.
    trait: Mapped["PilotTrait"] = relationship(
        back_populates = 'assignments'
    )