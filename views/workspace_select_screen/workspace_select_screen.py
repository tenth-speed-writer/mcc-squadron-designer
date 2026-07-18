# Python variable type checking
import typing

# UI components
from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.button import Button 
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout

# Custom UI elements
from ..word_wrapped_ui_elements import \
    WordWrappedButton, \
    WordWrappedLabel
from ..text_input_popup import TextInputPopup
from .load_workspace_popup import LoadWorkspacePopup

# Controller logic
from controllers.workspace_select_screen import load_new_workspace


class WorkspaceSelectScreenButton(WordWrappedButton):
    """
        Represents one of the main menu buttons for
        the app, like Load Workspace or New Workspace.

        Specify your text and actions; style specifics
        will be handled by this class's constructor.
    """
    def __init__(self, **kwargs):
        # Pass along any keyword arguments to the base Button class
        super().__init__(**kwargs)

        # Set this button's desired relative size within its parent widget.
        # It'll follow this ratio up or down to its max & min height & width.
        #
        # Should try to be 80% of the container wide and 10% tall.
        self.size_hint = (.8, .130)

        # Center-align the button in its container
        self.pos_hint = {'center_x': 0.5}

        # Specify font name and size for this type of button
        self.font_name = 'Faraway Wide'
        self.font_size = '32sp'


class WorkspaceSelectScreen(Screen):
    """
        Represents the splash screen in which the user may select
        to load an existing squadron workspace or select a new one.
    """
    # A reference to the application class which runs this screen.
    app: App

    def _on_new_workspace_ok(self, workspace_name: str):
        """
            Called when the user clicks OK in the new workspace name popup.
            Takes that name and attempts to load a workspace based on it.
        """
        print(f"Loading workspace {workspace_name}")
        load_new_workspace(self.app, workspace_name)

    def _on_release_new_workspace(self, instance):
        """
            Adds a popup to the current screen which prompts the user to
            enter a name for the workspace they would like to create.

            As its ok_ok callback, passes a method which creates/loads a
            workspace of the desired name and opens the workspace menu.
        """
        popup = TextInputPopup(
            prompt_text = 'Name your Workspace.\nAlphaNum and dashes only.',
            app = self.app,
            on_ok = self._on_new_workspace_ok
        )
        popup.open()

    def _on_release_load_workspace(self, instance):
        """
            When the user clicks on the Load Workspace button, open a copy of
            LoadWorkspacePopup and add it as a widget to this parent screen.
        """
        popup = LoadWorkspacePopup(app = self.app)
        popup.open()
    
    def __init__(self, app: App, **kwargs):
        # Pass along optional keyword arguments to parent class's constructor
        super().__init__(**kwargs)

        # Assign the app attribute
        self.app = app

        # Define the BoxLayout which arranges
        # the meaningful contents of this screen
        layout: BoxLayout = BoxLayout(
            orientation = 'vertical',
            padding = '10sp', # 10px of padding between content and edges
            spacing = '10sp', # 10px of spacing between all contents
        ) 
        
        # Add a header
        layout.add_widget(
            WordWrappedLabel(
                # The linebreak (\n) makes sure it wraps to two lines minimum
                text = "Mechanical Core\nSquadron Designer",

                # Use 64pt Faraway
                font_name = 'Faraway',
                font_size = '64sp'
            )
        )

        # Add the New Workspace button and assign its on pressed logic
        new_workspace_button = WorkspaceSelectScreenButton(
            text = 'New Squadron Workspace',
        )
        new_workspace_button.bind(
            # On click, open a text input popup
            on_release = self._on_release_new_workspace
        )
        layout.add_widget(new_workspace_button)

        # Add the Load Workspace button
        load_workspace_button = WorkspaceSelectScreenButton(
            text = 'Load Squadron Workspace'
        )
        load_workspace_button.bind(
            on_release = self._on_release_load_workspace
        )
        layout.add_widget(load_workspace_button)

        # Lastly, append the layout to this screen
        self.add_widget(layout)