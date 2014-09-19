from sqlalchemy import (
    Column,
    Index,
    Integer,
    Float,
    Text,
    Date
    )

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    )

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()


class Pass(Base):
    __tablename__ = 'passes'
    id = Column(Integer, primary_key=True)
    uid = Column(Integer)
    speed = Column(Float)
    line = Column(Integer)
    count = Column(Float)
    division = Column(Text)
    date = Column(Date)

    def as_dict(self):
       this_dict = {c.name: getattr(self, c.name) for c in self.__table__.columns}
       this_dict['date'] = str(this_dict['date'])
       return this_dict

class Skier(Base):
    __tablename__ = 'skiers'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    age = Column(Integer)
    division = Column(Text)

    def as_dict(self):
       this_dict = {c.name: getattr(self, c.name) for c in self.__table__.columns}
       return this_dict



Index("UID", Pass.uid)