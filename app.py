# This is where the kivy app--that is, the GUI that
# connects all the other logic--is actually assembled.

# Import the base class for an application. We wanna extend this.
from kivy.app import App

# Import GUI elements we need to render the app itself.
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.floatlayout import FloatLayout

# Import the ability to load custom fonts.
from fonts import register_fonts

# Import our app screens from the views module.
from views.workspace_select_screen import WorkspaceSelectScreen
from views.workspace_main_menu import WorkspaceMainMenu
from views.pilot_roster import PilotRoster

# Import the database manager from the models module.
from models import DBManager

# Used to describe valid options for certain selections
from enum import Enum

# Used to explicitly describe data structures we're throwing around
from typing import NamedTuple

# Configure minimum window dimensions.
#
# Phone resolution tends to bottom out around 320px in viewport
# width and around 600px in viewport height for design purposes.
from kivy.core.window import Window
Window.minimum_width = 320
Window.minimum_height = 600

# Debugging. DELETE THIS!
# from models import \
#     DBManager, Pilot, PilotTrait, PilotTraitAssignment, PilotRank, \
#     TypeProfile, TechLevel, MechModifier, Mech, MechModifierAssignment, \
#     Team, TeamAssignment, MechModifierTeamAssignment
# from sqlalchemy.orm import Session
# import os
# try:
#     os.remove('foo.workspace.sqlite3')
# except:
#     print("DB did not need to be removed")
#dbm = DBManager(filename="sqlite:///foo.sqlite3")
# dbm = DBManager(filename="foo.workspace.sqlite3")
# with Session(dbm.engine) as session:
#     # Make bob's rank
#     shonen = PilotRank(
#         name = "Shonen Protag",
#         effect = "Bob somehow always wins",
#         cost = 1,
#         traits_added = 1
#     )
#     session.add(shonen)

#     # Make bob
#     bob = Pilot(
#         name = "Bob",
#         rank = shonen,
#         bio = "Tee hee I'm bob"
#     )
#     session.add(bob)

#     # Make being good at this
#     good_at_this = PilotTrait(
#         name = "Really Good At This",
#         effect = "Bob always pulls it off, despite seemingly being terrible."
#     )
#     session.add(good_at_this)

#     # Make bob being good at this
#     bob_being_good_at_this = PilotTraitAssignment(
#         pilot = bob,
#         trait = good_at_this
#     )
#     session.add(bob_being_good_at_this)

#     # Make a pretend mech type
#     oldie_type = TypeProfile(
#         name = 'Oldie',
#         close_range = 1,
#         medium_range = 1,
#         long_range = 1,
#         defense = 1,
#         health = 1,
#         movement = 1    
#     )
#     session.add(oldie_type)

#     # Make a tech level
#     old_tech = TechLevel(
#         level = 1,
#         stat_modifier = 0,
#         cost_modifier = 0
#     )
#     session.add(old_tech)

#     # Make a pretend mech modifier
#     rugged_ol_thing = MechModifier(
#         type = 'Defense',
#         effect = 'Adds one to defense--because it\'s made it this long right?',
#         cost_delta = 1,
#         defense_delta = 1
#     )
#     session.add(rugged_ol_thing)

#     # Make a pretend mech
#     gunmackie = Mech(
#         name = "Gunmackie",
#         is_mech = True,
#         type = oldie_type,
#         tech_level = old_tech
#     )
    
#     # Give it its modifier
#     session.add(
#         MechModifierAssignment(
#             mech = gunmackie,
#             modifier = rugged_ol_thing,
#             is_mandatory = True
#         )
#     )
#     session.commit()

#     print(f"Pilot: {bob.name}, {bob.rank.name}. ID {bob.id}.")
#     print(f"{bob.name} has trait {bob.traits[0].trait.name}.")
#     print(f"Its effect is: {bob.traits[0].trait.effect}.\n\n")

#     print(f"There exists a mech called a {gunmackie.name}. ID {gunmackie.id}")
#     print(f"It is of tech level {old_tech.level} with stat mod {old_tech.stat_modifier} and cost modifier {old_tech.cost_modifier}")
#     print(f"It is of class {gunmackie.type.name}.")
#     print(f"It possesses modifier of type {gunmackie.modifiers[0].modifier.type} with effect \"{gunmackie.modifiers[0].modifier.effect}\"")

#     # Create a team
#     bliblies = Team(
#         name = "Bob's Blathering Bliblies"
#     )
#     session.add(bliblies)

#     # Add the gunmackie, piloted by bob, to the team
#     assignment = TeamAssignment(
#         position = 0,
#         custom_mech_bio = 'Bob\'s own blibliebonker',
#         pilot = bob,
#         mech = gunmackie,
#         team = bliblies,
#     )
#     session.add(assignment)
#     session.commit()

#     modifier_assignment = MechModifierTeamAssignment(
#         mech_id = gunmackie.id,
#         modifier_id = rugged_ol_thing.id,
#         team_assignment_id = assignment.id,
#         enabled = True
#     )
#     session.add(modifier_assignment)
#     session.commit()
    
#     print(f"There exist a team named \"{bliblies.name}\"")

class SquadronDesigner(App):
    """
        The parent class representing the application.
    """
    # Referenced by the Screen objects to decide how large at most to let
    # themselves be. Represents a vertical-format tablet of common size.
    MAX_UI_SIZE: Tuple[str, str] = ('756sp', '1024sp')
    
    # The currently active database manager, representing the loaded workspace.
    db_manager: DBManager

    # The object which manages and switches between the different app screens.
    screen_manager: ScreenManager

    # A list of references to the currently-instantiated screens.
    screens: List[Screen]

    # The storage path given to this app by the environment running it.
    storage_path: str

    # The name of the subdirectory under the storage path where workspaces go.
    workspace_subdirectory: str = "workspaces"

    # An enumeration of valid names for each of the screens in the app.
    class ScreenNames(Enum):
        WORKSPACE_SELECT_SCREEN = 'WorkspaceSelectScreen'
        WORKSPACE_MAIN_MENU = 'WorkspaceMainMenu'
        PILOT_ROSTER = 'PilotRoster'

    def regenerate_screens(self):
        """
            Clears each of the existing Screen objects and re-instantiates
            them based on a new workspace (assumed to be self.db_engine).

            Specifically does not reset the Workspace Select Screen.
            It's fine.
        """
        # Remove every screen except the workspace selection screen from
        # the screen manager, and then from the self.screens ref list.
        screens_to_regen = [
            screen for screen in self.screens
            if screen.name != str(
                self.ScreenNames.WORKSPACE_SELECT_SCREEN.value
            )
        ]
        for screen in screens_to_regen:
            self.screen_manager.remove_widget(screen)
            self.screens.remove(screen)

        # Iterate over each screen and re-instantiate it
        # Rebuild main menu
        workspace_main_menu = WorkspaceMainMenu(
            name = str(self.ScreenNames.WORKSPACE_MAIN_MENU.value),
            app = self
        )
        self.screen_manager.add_widget(workspace_main_menu)
        self.screens.append(workspace_main_menu)

        # Rebuild pilot roster screen
        pilot_roster_screen = PilotRoster(
            name = str(self.ScreenNames.PILOT_ROSTER.value),
            app = self
        )
        self.screen_manager.add_widget(pilot_roster_screen)
        self.screens.append(pilot_roster_screen)

    # Changes the currently active screen.
    def change_screen(self, screen_name: ScreenNames):
        """
            Changes the currently active screen.
            Args:
                screen_name (ScreenNames): 
                    A member of the ScreenNames enum, representing a valid
                    screen name to be selected from the ScreenManager.
        """
        self.screen_manager.current = str(screen_name.value)

    def build(self):
        # Announce storage path for debugging use and store it for app use
        self.storage_path = App.get_running_app().user_data_dir
        print(f"App storage path is {self.storage_path}")
        
        # Load and register custom fonts used by this app.
        register_fonts()

        # Instantiate a reference list for active screens
        self.screens = []

        # Instantiate the screen manager
        self.screen_manager = ScreenManager()

        # TODO: Create a template workspace to act as our on-instantiation volume.
        self.db_manager = DBManager("Base.workspace", app = self)

        # Mount the template of each of our screens on the screen manager
        # TODO: 
        #   Replace this with an instantiation scheme which doesn't require
        #   us to instantiate a dummy DB engine just to start up the screens.

        # Workspace select. This one goes first so it shows at app launch.
        workspace_select_screen = WorkspaceSelectScreen(
            name = str(self.ScreenNames.WORKSPACE_SELECT_SCREEN.value),
            app = self
        )
        self.screen_manager.add_widget(workspace_select_screen)
        self.screens.append(workspace_select_screen)

        # TODO: Remove calls to instantiate the various other screens using
        # the dummy database. They'll never be used, and at time of writing
        # the only reason I haven't removed them is it might break things. -L

        # The main menu shown once the user chooses a workspace.
        workspace_main_menu = WorkspaceMainMenu(
            name = str(self.ScreenNames.WORKSPACE_MAIN_MENU.value),
            app = self
        )
        self.screen_manager.add_widget(workspace_main_menu)
        self.screens.append(workspace_main_menu)

        # The pilot roster overview screen
        pilot_roster_screen = PilotRoster(
            name = str(self.ScreenNames.PILOT_ROSTER.value),
            app = self
        )
        self.screen_manager.add_widget(pilot_roster_screen)
        self.screens.append(pilot_roster_screen)

        # Return our screen manager with its screens mounted.
        return self.screen_manager
    
if __name__ == "__main__":
    SquadronDesigner().run()
