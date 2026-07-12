# This is where the kivy app--that is, the GUI that
# connects all the other logic--is actually assembled.

# Import the base class for an application. We wanna extend this.
from kivy.app import App

# Import GUI elements we need to render the app itself.
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.floatlayout import FloatLayout

# Import the ability to load custom fonts.
from fonts import register_fonts

# Import our app screens from the views module.
from views.workspace_select_screen import WorkspaceSelectScreen

# Configure minimum window dimensions.
#
# Phone resolution tends to bottom out around 320px in viewport
# width and around 600px in viewport height for design purposes.
from kivy.core.window import Window
Window.minimum_width = 320
Window.minimum_height = 600

class SquadronDesigner(App):
    """
        The parent class representing the application.
    """
    def build(self):
        # Load and register custom fonts used by this app.
        register_fonts()
        
        # Instantiate the screen manager
        screen_manager = ScreenManager(
        #     size_hint = (None, None),
        #     size_hint_min_x = Window.minimum_width,
        #     size_hint_min_y = Window.minimum_height,
        #     pos_hint = {'center_x': 0.5, 'center_y': 0.5}
        )

        # Mount each of our screens on the screen manager
        # This one goes first so it shows at app launch
        screen_manager.add_widget(
            WorkspaceSelectScreen(name="WorkspaceSelectScreen")
        )

        # foo = FloatLayout()
        # foo.add_widget(Label(text="lmao"))
        # foo.add_widget(screen_manager)

        # Return our (aligned) screen manager with its screens mounted.
        return screen_manager
    
if __name__ == "__main__":
    SquadronDesigner().run()
