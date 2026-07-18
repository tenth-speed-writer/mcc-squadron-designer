from models import Pilot, PilotRank
from word_wrapped_ui_elements import WordWrappedLabel

class PilotsListRow(WordWrappedLabel):
    """
        Represents a row in the PilotsList, representing a single
        pilot's name and rank in a clickable, neatly displayed way.
    """
    def __init__(self, pilot: Pilot, **kwargs):
        # Pass kwargs to parent constructor
        super().__init__(**kwargs)
        
        # Set preferred size and position
        self.size_hint = (0.1, 0.1)
        self.pos_hint = {'center_x': 0.5, 'center_y': 0.5}

        # Set size minima and maxima
        self.size_hint_min_y = '48sp'
        self.size_hint_max_y = '48sp'

        # Set font and style
        font_name = 'Faraway Mono'
        font_size = '16sp'

        # Set text based on pilot's name and rank
        self.text = f"{pilot.name} - {pilot.rank.name}"
