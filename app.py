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

# Debugging. DELETE THIS!
# from models import \
#     DBManager, Pilot, PilotTrait, PilotTraitAssignment, PilotRank, \
#     TypeProfile, TechLevel, MechModifier, Mech, MechModifierAssignment
# from sqlalchemy.orm import Session
# import os
# os.remove('foo.sqlite3')
# dbm = DBManager(filename="sqlite:///foo.sqlite3")
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
#     print(f"{bob.name} has trait {bob.traits.trait.name}.")
#     print(f"Its effect is: {bob.traits.trait.effect}.\n\n")

#     print(f"There exists a mech called a {gunmackie.name}. ID {gunmackie.id}")
#     print(f"It is of tech level {old_tech.level} with stat mod {old_tech.stat_modifier} and cost modifier {old_tech.cost_modifier}")
#     print(f"It is of class {gunmackie.type.name}.")
#     print(f"It possesses modifier of type {gunmackie.modifiers[0].modifier.type} with effect \"{gunmackie.modifiers[0].modifier.effect}\"")

class SquadronDesigner(App):
    """
        The parent class representing the application.
    """
    def build(self):
        # Load and register custom fonts used by this app.
        register_fonts()
        
        # Instantiate the screen manager
        screen_manager = ScreenManager()

        # Mount each of our screens on the screen manager
        screen_manager.add_widget(
            # This one goes first so it shows at app launch
            WorkspaceSelectScreen(name="WorkspaceSelectScreen")
        )

        # Return our screen manager with its screens mounted.
        return screen_manager
    
if __name__ == "__main__":
    SquadronDesigner().run()
