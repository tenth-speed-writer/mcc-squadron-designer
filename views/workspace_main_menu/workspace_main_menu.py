from kivy.app import App
from kivy.uix.screenmanager import Screen
from ..word_wrapped_ui_elements import WordWrappedLabel
from ..outer_box_layout import OuterBoxLayout
from .workspace_menu_button import WorkspaceMenuButton

class WorkspaceMainMenu(Screen):
    """
        Represents the main menu screen made shown to the user
        after they create a new workspace, select an existing one,
        or exit to the menu from within one of the editor screens.

        Contains such navigation buttons as the Pilot Roster,
        the Team Editor, and the Team Overview screen links,
        as well as a nice print out of the workspace name.
    """
    # The parent-level kivy app. Specifically an instance of SquadronDesigner.
    app: App

    def exit_to_workspace_select(self):
        """
            Clears the current workspace selection from the parent App object,
            then switches the ScreenManager to the Workspace Select Screen.

            NOTE: Uncommitted changes on the DB will be lost on execution.
        """
        self.app.db_manager = None
        self.app.change_screen(self.app.ScreenNames.WORKSPACE_SELECT_SCREEN)

    def __init__(self, app: App, *args, **kwargs):
        # Pass unused args and kwargs along to superclass's constructor
        super().__init__(*args, **kwargs)

        # Assign a reference to the app which is running this screen.
        self.app = app

        # Get the name of the active database instance from the App.
        # Be sure to ditch the .workspace suffix, if it's present.
        db_name = app.db_manager.filename.removesuffix('.workspace')

        # Set up a vertical box layout to hold the contents of this screen.
        layout = OuterBoxLayout(
            orientation = 'vertical',
            padding = '10sp',
            spacing = '10sp',
            pos_hint = { 'center_x': 0.5, 'center_y': 0.5},
            size_hint = (0.9, 0.95),
            size_hint_max_x = app.MAX_UI_SIZE[0],
            size_hint_max_y = app.MAX_UI_SIZE[1]
        )

        # Render a header with the name of this screen
        screen_header = WordWrappedLabel(
            text = 'Squadron Workspace',
            font_name = 'Faraway Large',
            bold = True,
            font_size = 32,
            pos_hint = { 'center_x': 0.5, 'center_y': 0},
            size_hint = (0.9, 0.2),
            size_hint_min_y = '80sp',
            size_hint_max_y = '100sp'
        )
        layout.add_widget(screen_header)

        # Render a sub-header with the name of the current workspace.
        sub_header = WordWrappedLabel(
            # Limit the name to 60 characters
            text = db_name[0:min(60, len(db_name))],
            font_name = 'Faraway Wide',
            font_size = 32,
            italic = True,
            size_hint = (0.8, 0.4),
            size_hint_min_y = '240sp',
            size_hint_max_y = '300sp',
            pos_hint = { 'center_x': 0.5, 'center_y': 0.2}
        )
        layout.add_widget(sub_header)

        # Render a button leading to the Pilot Roster screen.
        pilot_roster_button = WorkspaceMenuButton(
            text = 'Pilot Roster'
        )
        pilot_roster_button.bind(
            on_release = lambda instance: self.app.change_screen(
                self.app.ScreenNames.PILOT_ROSTER
            )
        )
        layout.add_widget(pilot_roster_button)

        # Render a button leading to the Team Editor screen.
        team_editor_button = WorkspaceMenuButton(
            text = 'Team Editor'
        )
        layout.add_widget(team_editor_button)

        # Render a button leading to the Team Overview screen.
        team_overview_button = WorkspaceMenuButton(
            text = 'Team Overview'
        )
        layout.add_widget(team_overview_button)

        # Render a button which unloads the DB and returns to workspace select.
        back_to_workspace_select_button = WorkspaceMenuButton(
            text= 'Return'
        )
        back_to_workspace_select_button.bind(
            on_release = lambda instance: self.exit_to_workspace_select()
        )
        layout.add_widget(back_to_workspace_select_button)

        # Affix the outermost layout to the root of this screen
        self.add_widget(layout)
