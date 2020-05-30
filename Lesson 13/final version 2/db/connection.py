from sqlalchemy import create_engine

from .models.base import BaseModel
from .session import DBSession

from sqlalchemy.orm import sessionmaker


class DataBase:

    connection = None       # engine
    session_factory = None  # session factory
    _test_query = 'SELECT NOW();'

    def __init__(self, connection):
        """
        Attributes:
          connection: sqlalchemy engine to database
        """

        self.connection = connection
        self.session_factory = sessionmaker(bind=self.connection)

    def check_connection(self):
        self.connection.execute(self._test_query).fetchall()

    def make_session(self, model: BaseModel = None) -> DBSession:
        if model is None:
            session = self.session_factory()

            return DBSession(session)
        else:
            session = self.session_factory.object_session(model)

            if session is None:
                session = self.make_session()

            return DBSession(session)


engine = create_engine(
        f'sqlite:///db.sqlite',
        pool_pre_ping=True,
        echo=True
    )
engine.execute('pragma foreign_keys=on')
db = DataBase(engine)
