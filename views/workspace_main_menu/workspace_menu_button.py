from ..word_wrapped_ui_elements import WordWrappedButton


class WorkspaceMenuButton(WordWrappedButton):
    """
        Represents one of the buttons in the workspace main menu.
        Contains pre-set size and positioning parameters.
    """
    def __init__(self, *args, **kwargs):
        # Pass args and kwargs along to parent class's constructor
        super().__init__(*args, **kwargs)

        # Specify fond and size as 32sp Faraway Wide
        self.font_name = 'Faraway Wide'
        self.font_size = '32sp'

        # Define size hint and max size
        self.size_hint = (0.8, 0.3)
        self.size_hint_max_x = '400sp'
        self.size_hint_max_y = '120sp'

        # Center self inside of parent container
        self.pos_hint = {'center_x': 0.5}
