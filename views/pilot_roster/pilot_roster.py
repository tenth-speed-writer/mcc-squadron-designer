from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.scrollview import ScrollView
from ..outer_box_layout import OuterBoxLayout
from ..word_wrapped_ui_elements import WordWrappedLabel, WordWrappedButton


class PilotRosterButton(WordWrappedButton):
    """
        Represents one of the major buttons (new pilot,
        exit) found on the pilot roster screen.
    """
    def __init__(self, text: str, **kwargs):
        # Pass kwargs along to parent class's constructor
        super().__init__()

        self.text = text

        # Specify fond and size as 32sp Faraway Wide
        self.font_name = 'Faraway Wide'
        self.font_size = '32sp'

        # Define size hint and max size
        self.size_hint = (0.8, 0.3)
        self.size_hint_max_x = '400sp'
        self.size_hint_max_y = '45sp'

        # Center self inside of parent container
        self.pos_hint = {'center_x': 0.5}


class PilotRoster(Screen):
    """
        Represents the UI of the Pilot Roster screen, where-in the user can
        review the pilots in their roster and click through them into the
        Pilot Editor--as well as click a button to create a new one.
    """
    def __init__(self, app: App, *args, **kwargs):
        # Pass unused kwargs to parent class's constructor
        super().__init__(**kwargs)

        # Assign reference to parent app
        self.app = app
        
        # Establish an outer box with set a fixed size to manage the
        # layout and draw a background+border around the active area.
        outer = OuterBoxLayout(
            orientation = 'vertical',
            padding = '10sp',
            spacing = '10sp',
            pos_hint = { 'center_x': 0.5, 'center_y': 0.5},
            size_hint = (0.9, 0.95),
            size_hint_max_x = app.MAX_UI_SIZE[0],
            size_hint_max_y = app.MAX_UI_SIZE[1]
        )

        # Add a label for the pilot roster
        header = WordWrappedLabel(
            text = 'Pilot Roster',
            font_name = 'Faraway Large',
            bold = True,
            font_size = 32,
            pos_hint = { 'center_x': 0.5, 'center_y': 1},
            size_hint = (0.9, 0.1),
            size_hint_min_y = '80sp',
            size_hint_max_y = '100sp'
        )
        outer.add_widget(header)

        # Add the scrollable list of pilots
        pilots_list_scroll_box = ScrollView(
            pos_hint = {'center_x': 0.5},
            size_hint = (0.9, 0.4)
        )
        

        # Add the pilots list to the screen
        outer.add_widget(pilots_list_scroll_box)

        # Add a button to create a new pilot
        new_pilot_button = PilotRosterButton(
            text = 'New Pilot'
        )
        outer.add_widget(new_pilot_button)

        # Add a button to return to the workspace main menu.
        exit_button = PilotRosterButton(
            text = 'Exit'
        )
        exit_button.size_hint_max_x = '60sp'
        # Bind a method to it that moves us back to the Workspace
        # Main Menu screen when the user clicks on it.
        exit_button.bind(
            on_click = lambda instance: self.app.change_screen(
                str(self.app.ScreenNames.WorkspaceMainMenu.value)
            )
        )
        outer.add_widget(exit_button)

        # Affix the outer-most container to the root of this screen
        self.add_widget(outer)
