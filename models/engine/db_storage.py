#!/usr/bin/python3
"""
New engine DBStorage: (models/engine/db_storage.py)
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from os import getenv
from models.state import State
from models.city import City
from models.base_model import BaseModel, Base


class DBStorage():
    """class dbstorage"""
    __engine = None
    __session = None

    def __init__(self):
        """init for DBStorage"""
        self.__engine = create_engine(
                'mysql+mysqldb://{}:{}@{}/{}'.
                format(
                    getenv(HBNB_MYSQL_USER),
                    getenv(HBNB_MYSQL_PWD),
                    getenv(HBNB_MYSQL_HOST),
                    getenv(HBNB_MYSQL_DB)),
                pool_pre_ping=True)
        if getenv(HBNB_ENV) is 'test':
            Base.metadata.drop_all(engine)

    def all(self, cls=None):
        """
        returns the dictionary __objects
        """
        all_items = {}
        if cls is not None:
            todos = self.__session.query(cls)
        else:
            todos = self.__session.query()
        for item in todos:
            key = 'cls' + '.' + str(self.id)
            all_items.update(key = item)
        return all_items

    def new(self, obj):
        """add object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """ delete from the current database session """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """ create the current database session and create all tables """
        Base.metadata.create_all(engine)
        Session = scoped_session(sessionmaker(engine, expire_on_commit=False))
        self.__session = Session()
        