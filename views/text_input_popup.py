from typing import Any
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from collections.abc import Callable
from kivy.uix.button import Button
from .outer_box_layout import OuterBoxLayout
from .word_wrapped_ui_elements import WordWrappedLabel


class TextInputPopupButton(Button):
    """
        Represents one of the little buttons, like OK
        or Cancel, that appear in the text input popup.
    """
    def __init__(self, **kwargs):
        # Call parent constructor on provided kwargs (inc. button text)
        super().__init__(**kwargs)

        # Set font and size
        self.font_name = 'Faraway Wide'
        self.font_size = '16sp'


class TextInputPopup(Popup):
    """
        Represents a modal which may appear whenever the user is prompted
        to ender a single line of text (such as when creating a workspace
        or assigning a name to a pilot.)

        Accepts custom prompt text to display to the user.
    """
    # The parent app object which runs this application
    app: App

    # The BoxLayout and subordinate objects which hold this popup's contents
    outer_box: OuterBoxLayout

    # The input field into which the user enters text
    text_input: TextInput

    def execute_on_ok_and_close(self, on_ok: Callable, on_ok_input: Any):
        """
            Executes the on_ok callback and then dismisses this pop-up.
            
            In some languages a lambda (an tiny anonymous function) is allowed
            to be two lines or more, making it easy to pass teensy callback
            functions around your application.

            Python, however, is Pythonic.

            So we make silly little two-line helper methods like this. <3
        """
        on_ok(on_ok_input)
        self.dismiss()

    def __init__(
            self,
            prompt_text: str,
            app: App,
            on_ok: Callable,
            **kwargs
        ):
        """
            Creates an instance of a general-purpose text input popup.

            Args:
                prompt_text (str): 
                    The text to be displayed as a prompt to the user
                app (App): 
                    A reference to the active parent class for this app
                on_ok (Callable): 
                    The callback to be executed when the user clicks OK.
        """
        # Pass keyword arguments along to parent constructor
        super().__init__(**kwargs)

        # Save a reference to the parent app
        self.app = app

        # Set own (popup) maximum dimensions
        self.padding = '10sp'
        self.pos_hint = { 'center_x': 0.5, 'center_y': 0.5 }
        self.size_hint_max_x = '420sp'
        self.size_hint_max_y = '260sp'

        # Hide title/header
        self.title = ''
        self.separator_height = 0

        # Create a outlined box layout for this modal using the same
        # OuterBoxLayout class we use to put borders on our screens.
        self.outer_box = OuterBoxLayout(
            orientation = 'vertical',
            padding = '10sp',
            spacing = '10sp',
            pos_hint = { 'center_x': 0.5, 'center_y': 0.5 },
            size_hint = (0.95, 0.95),
            size_hint_max_x = '400sp',
            size_hint_max_y = '160sp'
        )
        self.add_widget(self.outer_box)

        # Add a label containing the prompt to the outer box.
        prompt_label = WordWrappedLabel(text = prompt_text)
        prompt_label.size_hint = (0.9, 0.4)
        prompt_label.size_hint_min_y = '40sp'
        prompt_label.pos_hint = { 'center_x': 0.5, 'center_y': 0.2 }
        prompt_label.font_name = 'Faraway Large'
        prompt_label.font_size = '16sp'
        self.outer_box.add_widget(prompt_label)

        # Add a text entry field to the outer box.
        self.text_input = TextInput(
            multiline = False,
            size_hint = (0.8, None),
            height = '33sp',
            pos_hint = { 'center_x': 0.5, 'center_y': 0.5 },
            size_hint_min_x = '180sp',
            font_name = 'Faraway Mono',
            font_size = '16sp'
        )
        self.outer_box.add_widget(self.text_input)

        # Create an inner horizontal box
        inner_box = BoxLayout(
            orientation = 'horizontal',
            padding = '10sp',
            spacing = '10sp',
            size_hint = (0.8, 0.2),
            size_hint_min_y = '40sp',
            pos_hint = { 'center_x': 0.5 }
        )
        self.outer_box.add_widget(inner_box)

        # Add an OK button to the inner box and bind its callback
        ok_button = TextInputPopupButton(
            text = 'OK',
            # pos_hint = { 'center_x': 0.1, 'center_y': 0.5 }
        )
        # Pass the contents of the text box at time of click to the callback
        ok_button.bind(
            on_release = lambda instance: self.execute_on_ok_and_close(
                on_ok = on_ok,
                on_ok_input = self.text_input.text
            )
        )
        inner_box.add_widget(ok_button)

        # Add a Cancel button to the inner box and bind its callback
        cancel_button = TextInputPopupButton(
            text = 'Cancel',
            # pos_hint = { 'center_x': 0.9, 'center_y': 0.5 },
        )
        cancel_button.bind(
            on_release = self.dismiss #lambda instance: self.dismiss()
        )
        inner_box.add_widget(cancel_button)
