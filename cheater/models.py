from cheater.database import *
from cheater.helpers import slugify


class Cheat(Base):
    """
    Cheat
    ~~~~

    `meth`:__init__(name, cheat)
    """

    __tablename__ = 'cheats'

    id = Column(Integer, primary_key=True, autoincrement=True)
    cheat = Column(Text)
    name = Column(String(255), index=True)
    _html = Column('html', Text)
    _slug = Column('slug', String(255))

    @hybrid_property
    def html(self):
        return self._html

    @hybrid_property
    def slug(self):
        return self._slug

    @html.setter
    def set_html(self, md):
        from markdown import markdown
        self._html = markdown(md, ['codehilite'])

    @slug.setter
    def set_slug(self, name):
        self._slug = slugify(name)

    def __init__(self, name, cheat):
        self.name = name
        self.slug = name
        self.cheat = cheat
        self.html = cheat

    def __repr__(self):
        return "Cheat<%s>" % self.name


class User(Base):

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(64), index=True)
    _password = Column('password', String(64), index=True)
    role = Column(String(32), default='user')

    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def set_password(self, password):
        from hashlib import md5
        self._password = md5(password).hexdigest()

    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role

    def __repr__(self):
        return "<User(%s, %s)>" % self.username, self.role

    def validate_password(self, password):
        from hashlib import md5
        (expected, got) = (self.password, md5(password).hexdigest())
        return expected == got
