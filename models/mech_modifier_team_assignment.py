from .base import Base
from sqlalchemy import ForeignKey, Boolean
from sqlalchemy.orm import Mapped, MappedColumn, mapped_column, relationship


class MechModifierTeamAssignment(Base):
    """
        Represents a single instance of a mech assigned to a team having
        a specific modifier, as well as whether that modifier is currently
        enabled or disabled.

        There should be one of these per modifier associated with the template
        from which the mech is drawn regardless of which are currently enabled.
    """
    # The name of this table in the database
    __tablename__ = 'mech_modifier_team_assignments'
    
    # The database ID of the mech-and-pilot team assignment with
    # which this particular modifier assignment is associated.
    # First part of this table's primary key.
    team_assignment_id: Mapped[int] = mapped_column(
        ForeignKey('team_assignments.id'),
        primary_key = True
    )

    # The ID of the mech whose template bears the specified modifier.
    # Second part of this table's primary key.
    mech_id: Mapped[int] = mapped_column(
        ForeignKey('mechs.id'),
        primary_key = True
    )

    # The ID of the modifier possessed by this mech on this team.
    # Third part of this table's primary key.
    modifier_id: Mapped[int] = mapped_column(
        ForeignKey('mech_modifiers.id'),
        primary_key = True
    )

    # Whether this trait is enabled or disabled for the specified mech
    # in the specified team. Must be set to True if trait is mandatory
    # for the specified mech.
    enabled: Mapped[bool] = mapped_column(Boolean)

    # The squad team assignment with which this modifier assignment
    # is associated. Relational navigation property.
    team_assignment: Mapped['TeamAssignment'] = relationship(
        back_populates = 'modifiers'
    )

    # The template of the mech which has this modifier. Navigation property.
    mech: Mapped['Mech'] = relationship(
        back_populates = 'modifiers_in_team_assignments'
    )

    # The modifier which is here instanced. Navigation property.
    modifier: Mapped['MechModifier'] = relationship(
        back_populates = 'mech_team_assignments'
    )
