from sqlalchemy import create_engine
from sqlalchemy.sql import select
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import Integer, String, Column, Text

Session = scoped_session(sessionmaker(autoflush = True))

Base = declarative_base()
Base.query = Session.query_property()

engine = create_engine('mysql+mysqldb://root:root@localhost:3306/cheater', echo = True)
Session.configure(bind = engine)
session = Session()

def create_all():
  import cheater.models
  Base.metadata.create_all(bind = engine)

class TimestampMixin(object):
  pass

__all__ = sorted(name for name, obj in locals().items()
                      if not name.startswith('_'))
