from sqlalchemy import Engine, create_engine
from kivy.app import App
from pathlib import Path

# We import Base last so that all the specific subclasses will have already
# been defined, and we can immediately use Base.metadata.create_all to
# generate the database if it doesn't already exist.
from .base import Base

class DBManager:
    """
        Represents and provides ORM functionality for a SQLite
        DB representing a single Squadron Designer workspace.
    """
    # The file in the saves/ directory associated with this workspace.
    filename: str

    # The database engine which generates usable sessions. Created during init.
    engine: Engine

    # The parent app which is managing this database engine
    app: App

    # The path prefix used for creating SQLite connections
    PATH_ROOT: str = 'sqlite:///'

    def get_workspace_directory(self):
        """
            Helper function to piece together the workspace
            storage path from data held by the parent app object.
        """
        return f"{self.app.storage_path}/{self.app.workspace_subdirectory}/"

    def ensure_storage_directory_exists(self):
        """
            Checks that the workspace subdirectory
            exists, and creates it if it don't.
        """
        # Piece together the workspace directory path
        workspace_directory = self.get_workspace_directory()
        
        # Create it (and its parent directories) if it doesn't already exist
        Path(workspace_directory).mkdir(
            parents = True,
            exist_ok = True
        )

    def __init__(self, filename: str, app: App):
        # Store the provided filename and app reference
        self.filename = filename
        self.app = app

        # Ensure the workspace storage directory exists
        self.ensure_storage_directory_exists()

        # Instantiate a DB engine to generate database sessions
        print(
            f"Generating DB engine for workspace DB {
                self.PATH_ROOT + self.get_workspace_directory() + filename
            }"
        )
        self.engine = create_engine(
            self.PATH_ROOT + self.get_workspace_directory() + filename
        )

        # Create the database schema, if necessary, based on the
        # table definitions in each of the individual model classes.
        #
        # Our subclass of the DeclarativeBase class provides
        # us with a convenience function to make this simple.
        Base.metadata.create_all(self.engine)
    
