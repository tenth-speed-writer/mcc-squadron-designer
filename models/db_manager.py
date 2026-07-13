from sqlalchemy import Engine, create_engine

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

    def __init__(self, filename: str):
        # Store the provided filename
        self.filename = filename

        # Instantiate a DB engine to generate database sessions
        self.engine = create_engine(filename)

        # Create the database schema, if necessary, based on the
        # table definitions in each of the individual model classes.
        #
        # Our subclass of the DeclarativeBase class provides
        # us with a convenience function to make this simple.
        Base.metadata.create_all(self.engine)
    
