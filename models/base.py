from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    """
        Base class placeholder for classes which represent rows and tables of
        the database that describes a workspace.

        It gets to be its own empty, free-standing parent subclass because
        doing so lets us easily call this class's .metadata.create_all(engine)
        method in order to instantiate our ORM engine based on its subclasses.
    """
    pass