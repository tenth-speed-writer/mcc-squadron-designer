from kivy.uix.button import Button
from kivy.uix.label import Label

class WordWrappedButton(Button):
    """
        Represents a button which word-wraps its text contents.
    """
    def __init__(self, *args, **kwargs):
        # Pass along all other arguments that might be given for this button.
        super().__init__(*args, **kwargs)

        # Bind its text_size (affecting its dimensions,
        # rather than its font size) to its widget width.
        self.text_size = (None, None)
        self.bind(size = lambda instance, size: setattr(instance, 'text_size', size))

        # Set text alignment to double centered.
        # Derivative classes can override this if they like.
        self.halign = 'center'
        self.valign = 'center'
    

class WordWrappedLabel(Label):
    """
        Represents a word-wrapped label.
    """
    def __init__(self, *args, **kwargs):
        # Pass along all other arguments that might be given for this label.
        super().__init__(*args, **kwargs)

        # Bind its text_size (affecting its dimensions,
        # rather than its font size) to its widget width.
        self.text_size = (None, None)
        self.bind(size = lambda instance, size: setattr(instance, 'text_size', size))

        # Set text alignment to double centered.
        # Derivative classes can override this if they like.
        self.halign = 'center'
        self.valign = 'center'
    
