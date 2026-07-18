from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Rectangle

class OuterBoxLayout(BoxLayout):
    """
        Represents the outer box layout of most menus and framed things.
        Contains logic to give it a nice & responsive visible border.
    """
    # How thick the margin should be inset from the edge of the box layout.
    MARGIN_WIDTH = 5 # px

    def _draw_self(self):
        """
            Draws a background & border as Rectangle objects, then
            saves them to this parent object to update as needed.
        """
        with self.canvas.before:
            # Plain white, full alpha
            Color(1, 1, 1, 1) 

            # Keep a reference to the rectangle we draw so we can update it!
            self.bg_rect = Rectangle(
                pos = self.pos,
                size = self.size
            )

        with self.canvas.before:
            # Plain black, full alpha
            Color(0, 0, 0, 1) 

            # Likewise, set a reference to the overlaid black backdrop
            self.bg_overlay_rect = Rectangle(
                # Pos equals parent position plus one margin width on both axes
                pos = (
                    self.pos[0] + self.MARGIN_WIDTH,
                    self.pos[1] + self.MARGIN_WIDTH
                ),
                
                # Size is smaller by twice the margin width on both axes
                size = (
                    self.size[0] - (2 * self.MARGIN_WIDTH),
                    self.size[1] - (2 * self.MARGIN_WIDTH)
                )
            )

    def _update_border(self, *args):
        """
            Called when the position or size of this instance of this boxlayout
            changes. Sets the border's dimensions to match the boxlayout's.
        """
        # Set size and position of the border pieces to match the parent object
        self.bg_rect.pos = self.pos
        self.bg_rect.size = self.size

        self.bg_overlay_rect.pos = (
            self.pos[0] + self.MARGIN_WIDTH,
            self.pos[1] + self.MARGIN_WIDTH
        )
        
        self.bg_overlay_rect.size = (
            self.size[0] - (2 * self.MARGIN_WIDTH),
            self.size[1] - (2 * self.MARGIN_WIDTH)
        )

    def __init__(self, *args, **kwargs):
        # Run usual constructor for a box layout with provided arguments
        super().__init__(*args, **kwargs)

        # Add a default padding of 10 viewport pixels (overridable)
        if not ('padding' in kwargs):
            self.padding = '10sp'
        
        # Draw the border for the first time save a reference it
        self._draw_self()

        # Then add a bindings to the size and position of this outline so that
        # when they're updated, the size & pos of the border can update as well
        self.bind(
            pos = self._update_border,
            size = self._update_border
        )
