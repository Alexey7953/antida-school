from typing import List, Dict, Tuple

from .models.base import BaseModel
from sqlalchemy.exc import *

from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.exc import ProgrammingError


class DBIntegrityException(Exception):
    pass


class DBDuplicateException(Exception):
    pass


class DBDataException(Exception):
    pass


class DBNoResultException(Exception):
    pass


class DBProgrammingException(Exception):
    pass


class DBSession(object):

    _session: Session

    def __init__(self, session: Session, *args, **kwargs):
        self._session = session

    def query(self, *entities, **kwargs):
        return self._session.query(*entities, **kwargs)

    def add_model(self, model: BaseModel, need_flush: bool = False):
        try:
            self._session.add(model)

            if need_flush:
                self._session.flush([model])
        except IntegrityError as e:
            raise DBIntegrityException(e)
        except DataError as e:
            raise DBDataException

    def expunge_model(self, model: BaseModel):
        try:
            self._session.expunge(model)
        except IntegrityError as e:
            raise DBIntegrityException(e)
        except DataError as e:
            raise DBDataException

    def add_models(self, models: List[BaseModel], need_flush: bool = False):
        if models is None:
            return
        if isinstance(models, list) and len(models) == 0:
            return

        try:
            self._session.add_all(models)

            if need_flush:
                self._session.flush(models)
        except IntegrityError as e:
            raise DBIntegrityException(e)
        except DataError as e:
            raise DBDataException

    def delete_model(self, model: BaseModel):
        if model is None:
            raise DBNoResultException

        try:
            self._session.delete(model)
        except IntegrityError as e:
            raise DBIntegrityException(e)
        except DataError as e:
            raise DBDataException

    def delete_models(self, models: List[BaseModel]):
        [self.delete_model(model) for model in models]

    def flush_session(self):
        try:
            self._session.flush()
        except IntegrityError as e:
            raise DBIntegrityException(e.args)
        except DataError as e:
            raise DBDataException(e.args)
        except ProgrammingError as e:
            raise DBProgrammingException(e.args)

    def flush_models(self, models: List[BaseModel]):
        if models is None:
            return
        if isinstance(models, list) and len(models) == 0:
            return

        try:
            self._session.flush(models)
        except IntegrityError as e:
            raise DBIntegrityException(e)
        except DataError as e:
            raise DBDataException

    def commit_session(self, need_close: bool = False):
        try:
            self._session.commit()
        except IntegrityError as e:
            raise DBIntegrityException(e.args)
        except DataError as e:
            raise DBDataException(e.args)

        if need_close:
            self.close_session()

    def close_session(self):
        try:
            self._session.close()
        except IntegrityError as e:
            raise DBDuplicateException
        except DataError as e:
            raise DBDataException

    def rollback_session(self, need_close: bool = False):
        try:
            self._session.rollback()
        except IntegrityError as e:
            raise DBDuplicateException
        except DataError as e:
            raise DBDataException

        if need_close:
            self.close_session()

    def set_autoflush(self, to: bool):
        self._session.autoflush = to
