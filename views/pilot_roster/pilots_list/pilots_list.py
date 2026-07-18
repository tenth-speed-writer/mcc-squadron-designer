from typing import List
from models import Pilot
from sqlalchemy import select
from sqlalchemy.orm import Session
from kivy.uix.boxlayout import BoxLayout
from enum import Enum, member
from outer_box_layout import OuterBoxLayout
from word_wrapped_ui_elements import WordWrappedLabel
from .pilots_list_row import PilotsListRow


class PilotsList(OuterBoxLayout):
    """
        Represents the interactable list of pilots which already exist in the
        currently active workspace. Each pilot's row shows their name, rank,
        and photo as well as a button to edit them.

        This parent level class contains the UI objects for the background and
        the border around the list; however, it also instantiates the UI
        components which live inside of it and provides references to them.
    """
    # The chosen sort order for the list. Defaults to pilot name, ascending.
    sort_order: SortOrder

    # A list (data object) of the current contents of the list (UI element).
    children: List[BoxLayout]

    class SortOrder(Enum):
        """
            An enumeration of valid options for the sort order of the list.

            The value of each member is its sort function, because Louise will
            do basically anything in her willful power to avoid a switch block.
        """
        # By name, ascending
        NAME_ASC = member(
            lambda pilots: 
                sorted(
                    pilots,
                    key = lambda pilot: pilot.name
                )
        )

        # By name, descending
        NAME_DESC = member(
            lambda pilots:
                sorted(
                    pilots,
                    key = lambda pilot: pilot.name,
                    reverse = True
                )
        )

        # By rank, then by name, ascending.
        #
        # NOTE: This and RANK_DESC may break if the ranks aren't
        # written in ascending order in the JSONs, lmao. -Louise
        RANK_ASC = member(
            lambda pilots:
                sorted(
                    pilots,
                    key = lambda pilot: (pilot.rank_id, pilot.name)
                )
        )

        # By rank, then by name, descending.
        RANK_DESC = member(
            lambda pilots:
                sorted(
                    pilots,
                    key = lambda pilot: (pilot.rank_id, pilot.name)
                )
        )

    def clear_list_contents(self):
        """
            Goes over the list (UI) contents in self.children, removes them
            from this object, and then clears out the .children list (object).
        """
        # Careful not trip over the list if it hasn't been defined yet!
        if hasattr(self, 'children') and self.children is not null:
            for child in self.children:
                self.remove_widget(child)
        self.children = []

    def get_pilots(self) -> List[Pilot]:
        """
            Fetches a list of known Pilots from this workspace's database.

        Returns:
            List[Pilot]: A list of known pilots
        """
        with Session(app.db_manager.engine) as session:
            # Select all Pilot objects and return them
            return session.scalars(select(Pilot)).all()

    def redraw_list_for_sort(self, sort_order: SortOrder):
        """
            Clears the contents of the list and
            rebuilds it in the specified sort order.

            Args:
                sort_order (SortOrder): 
                    The sort order to use, based on the SortOrder enum.
        """
        # Clear any existing list contents
        self.clear_list_contents()

        # Get known Pilot objects from the database
        pilots: List[Pilot] = self.get_pilots()

        # Sort the pilots by the specified function and draw their rows
        for pilot in SortOrder.value(pilots):
            new_row = PilotsListRow(pilot)
            self.children += new_row
            self.add_widget(new_row)

    def __init__(self, **kwargs):
        # Pass along unused kwargs to the parent class's constructor.
        super().__init__(**kwargs)

        # Set default sort order to pilot name, ascending
        self.sort_order = self.SortOrder.NAME_ASC

        # Set the .children variable to an empty list
        self.children = []

        # Get the currently loaded pilot roster from the database

        # Sort the pilots list by the appropriate sort 
