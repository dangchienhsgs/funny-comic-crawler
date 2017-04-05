from sqlalchemy import create_engine, Column, String
from sqlalchemy.engine.url import URL
from sqlalchemy.ext.declarative import declarative_base

from . import settings

DeclarativeBase = declarative_base()


def db_connect():
    """
    Performs database connection using database settings from settings.py.
    Returns sqlalchemy engine instance
    """
    return create_engine(URL(**settings.DATABASE))


def create_images_table(engine):
    """"""
    DeclarativeBase.metadata.create_all(engine)


class ImageItem(DeclarativeBase):
    """Sqlalchemy deals model"""
    __tablename__ = "images"

    id = Column(String, primary_key=True)
    title = Column('title', String)
    filename = Column('filename', String, nullable=False)
    url = Column('url', String, nullable=True)

    def __init__(self, id, title, filename, url):
        self.id = id
        self.title = title
        self.filename = filename
        self.url = url
