#!/usr/bin/python3
"""New storage engine using DB"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from models.base_model import Base


class DBStorage:
    """
    New engine DBStorage: (models/engine/db_storage.py)
    """

    __engine = None
    __session = None

    def __init__(self):
        """
        the engine must be linked to the MySQL database and user created before (hbnb_dev and hbnb_dev_db):
        dialect: mysql
        driver: mysqldb
        """
        self.__engine = create_engine(
            "mysql+mysqldb://{}:{}@{}/{}".format(
                getenv("HBNB_MYSQL_USER"),
                getenv("HBNB_MYSQL_PWD"),
                getenv("HBNB_MYSQL_HOST", default="localhost"),
                getenv("HBNB_MYSQL_DB"),
            ),
            pool_pre_ping=True,
        )
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        query on the current database session (self.__session) all objects depending of the class name (argument cls)
        """
        from models import classes

        session = self.__session
        objects = {}
        if cls:
            query_result = session.query(classes[cls]).all()
        else:
            all_classes = list(classes.values())
            query_result = []
            for class_ in all_classes:
                query_result.extend(session.query(class_).all())

        for obj in query_result:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            objects[key] = obj
        return objects

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj:
            self.__session.delete(obj)

    def reload(self):
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session_factory)
