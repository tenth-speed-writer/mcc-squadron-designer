# Python variable type checking
import typing

# UI components
from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.button import Button 
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout

# Custom UI elements
from .word_wrapped_ui_elements import \
    WordWrappedButton, \
    WordWrappedLabel


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
    # The maximum width in system specific pixels beyond which the outer-most
    # container of this screen's contents won't try to stretch any wider.
    MAX_CONTENTS_WIDTH = '768sp'
    
    def __init__(self, **kwargs):
        # Pass along optional keyword arguments to parent class's constructor
        super().__init__(**kwargs)

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

        # Add the New Workspace button
        layout.add_widget(
            WorkspaceSelectScreenButton(text = 'New Squadron Workspace')
        )

        # Add the Load Workspace button
        layout.add_widget(
            WorkspaceSelectScreenButton(text = 'Load Squadron Workspace'),
        )

        # Lastly, append the layout to this screen
        self.add_widget(layout)