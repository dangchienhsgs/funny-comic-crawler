from sqlalchemy import String

from .extensions import db

Column = db.Column


class ImageItem(db.Model):
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
