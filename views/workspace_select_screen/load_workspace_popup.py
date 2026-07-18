from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.filechooser import FileChooserListView
from kivy.app import App
from ..word_wrapped_ui_elements import WordWrappedLabel

class LoadWorkspacePopup(Popup):
    """
        Represents the popup shown when the user clicks on the Load Workspace
        button. Presents them with kivy's system-independent file picker
        pointed directly at the game's save directory and passes the result
        into the load_new_workspace button.
    """
    # A reference to the root application running this popup
    app: App

    def __init__(self, app: App, **kwargs):
        # Pass unused kwargs up to the parent class's constructor
        super().__init__(**kwargs)

        # Define own dimensions
        self.size_hint = (0.5, 0.5)
        self.size_hint_max_x = '400sp'
        self.size_hint_min_x = '280sp'
        self.size_hint_max_y = '500sp'
        self.size_hint_min_y = '400sp'
        self.pos_hint = { 'center_x': 0.5, 'center_y': 0.5 }

        # Save a reference to the active application object
        self.app = app

        # Create an internal box container
        layout = BoxLayout(
            orientation = 'vertical',
            padding = '10sp',
            spacing = '10sp',
            size_hint = (0.95, 0.95),
            pos_hint = { 'center_x': 0.5, 'center_y': 0.5 }
        )
        self.add_widget(layout)

        # Add a label for the pop-up
        select_workspace_label = WordWrappedLabel(
            text = 'Select Workspace'
        )

        # Get save storage path and add the file chooser pointed at it
        workspace_directory = \
            f"{self.app.storage_path}/{self.app.workspace_subdirectory}/"
        chooser = FileChooserListView(
            path = workspace_directory
        )
        

        # Add a Load Workspace button and bind it

        # Add a Cancel button and bind it
