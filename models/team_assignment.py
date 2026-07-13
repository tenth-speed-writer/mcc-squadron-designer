import typing
from typing import Optional, List
from .base import Base
from sqlalchemy import String, Integer, ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship


class TeamAssignment(Base):
    """
        Represents an instance of a specific mech and pilot as
        assigned to a particular squadron team in the teams table.

        Relationally linked to teamTeamAssignmentModifiers, which indicates
        which of the mech's modifiers are currently set as active.
    """
    # The name of this table in the database
    __tablename__ = 'team_assignments'

    # The local primary key of the team_assignments table
    id: Mapped[int] = mapped_column(primary_key = True)

    # The sort order of this specific assignment in its parent team.
    # This represents the order in which the user placed this assigned
    # mech beside its peers when editing their squadron.
    position: Mapped[int] = mapped_column(Integer)

    # An optional bio for the mech in this team assignment. Can be specified
    # by the player during team design. If provided and not empty, it will be
    # displayed instead of the mech template's bio. Maximum of 1000 characters.
    custom_mech_bio: Mapped[Optional[str]] = mapped_column(String(1000))

    # Modifiers potentially held by the mech represented by this assignment,
    # and whether they're currently enabled as it appears in this team.
    # Navigation property.
    modifiers: Mapped[List['MechModifierTeamAssignment']] = relationship(
        back_populates = 'team_assignment'
    )
    
    # The ID of the team to which this assignment belongs.
    team_id: Mapped[int] = mapped_column(ForeignKey('teams.id'))

    # The team to which this assignment belongs. Navigation property.
    team: Mapped['Team'] = relationship(
        back_populates = 'assignments'
    )

    # Specify that there can only be one unique position for a given team.
    __table_args__ = (
        UniqueConstraint(
            'team_id',
            'position',
            name = 'team_assignment_unique_position_on_team'
        ),
    )