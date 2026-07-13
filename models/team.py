import typing
from typing import Optional, List
from .base import Base
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Team(Base):
    """
        Represents a cohesive MCC team as built in the MCC
        squadron editor. Includes a list of TeamAssignments,
        each of which describes a single set of mech, pilot,
        and active mech traits.

        This object includes logic (not reflected in the database)
        for such things as determining the total points cost.
    """
    # The name of the database table where teams are recorded
    __tablename__ = 'teams'

    # The primary database key for the teams table
    id: Mapped[int] = mapped_column(primary_key = True)

    # The name of this team. Max 100 characters.
    name: Mapped[str] = mapped_column(String(100))

    # The mechs, pilots, and modifier sets which constitue this team.
    assignments: Mapped[List['TeamAssignment']] = relationship(
        back_populates = 'team'
    )
