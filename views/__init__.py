"""
    Views are the high-level UI elements of our model.
    Most things rendered in the UI should be templated
    based on these UI element classes.

    This package definition script imports these elements
    and any supporting elements they have which other parts
    of the application might need to refer to and makes it
    easy to import them as a package elsewhere in the project.
"""
from .workspace_main_menu import WorkspaceMainMenu
from .workspace_select_screen import WorkspaceSelectScreen
from .pilot_roster import PilotRoster
