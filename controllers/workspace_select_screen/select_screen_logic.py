from models import DBManager
from collections.abc import Callable
from kivy.app import App
from views.text_input_popup import TextInputPopup

def load_new_workspace(app: App, workspace_name: str):
    """
        Sets the specified app's db_manager to a new instance at a filename
        decided by the provided workspace_name, then switches its active
        screen to the workspace main menu screen.

        Args:
            app (App):
                The App object running this kiva application.
            workspace_name (str): 
                The name of the workspace, used to determine filename.
    """
    # Affix .workspace to the workspace name to get the filename.
    # Note: it's still a SQLite3 file, lol.
    filename = workspace_name + '.workspace'

    # Instantiate a database manage instance corresponding to that filename.
    db_manager = DBManager(filename)

    # Replace the specified app's DB manager with the new one.
    app.db_manager = db_manager

    # Regenerate app screens to correspond to the new database.
    app.regenerate_screens()

    # Swap the app's screen manager to the workspace menu screen.
    app.screen_manager.current = str(app.ScreenNames.WORKSPACE_MAIN_MENU.value)
