# coding=utf-8
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Text, Boolean, String, DateTime, SmallInteger, ForeignKey, Enum, TypeDecorator
from flask.ext.login import UserMixin, LoginManager
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import ConfigParser

cf = ConfigParser.ConfigParser()
cf.read('b612.ini')
DATABASE_URI = cf.get('db', 'sql_conn')
BaseModel = declarative_base()
engine = create_engine(DATABASE_URI, pool_recycle=3600, encoding='utf-8')
DBSession = sessionmaker(engine)
login_manager = LoginManager()
login_manager.session_protection = 'strong'


class User(UserMixin, BaseModel):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(64), unique=True)
    password_hash = Column(String(128))

    @property
    def password(self):
        raise AttributeError('password 只有写权限')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return 'user', self.id, self.name


class Notes(BaseModel):
    __tablename__ = 'notes'
    id = Column(Integer, primary_key=True)
    content = Column(Text)
    status = Column(SmallInteger, index=True)
    create_time = Column(DateTime)


if __name__ == '__main__':
    BaseModel.metadata.create_all(engine)
