"""Models"""

from sqlalchemy import (create_engine, Column, String, Integer,
                        DateTime, ForeignKey)
from sqlalchemy.orm import (sessionmaker, relationship)
from sqlalchemy.ext.declarative import declarative_base
from config import DATABASE_URL

Base = declarative_base()
engine = create_engine(DATABASE_URL, echo=True)
Session = sessionmaker(bind=engine)


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String)
    created_by = Column(DateTime)
    comment = relationship('Comment')
    submission = relationship('Submission')


Base.metadata.create_all(engine)
