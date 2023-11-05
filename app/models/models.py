# SQLALCHEMY MODELS

import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Worktype_ORM(Base):
    __tablename__ = "worktypes"

    id = sa.Column(sa.Integer, primary_key=True, index=True)
    name = sa.Column(sa.Text, unique=True)

    records = relationship("Workrecord_ORM", back_populates="type")


class Workrecord_ORM(Base):
    __tablename__ = "workrecords"

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.Text, unique=True)
    type_id = sa.Column(sa.Integer, sa.ForeignKey("worktypes.id"))
    author_id = sa.Column(sa.Integer, sa.ForeignKey("users.id"))
    start = sa.Column(sa.DateTime)
    end = sa.Column(sa.DateTime)

    type = relationship("Worktype_ORM", back_populates="records")
    author = relationship("User_ORM", back_populates="records")


class User_ORM(Base):
    __tablename__ = "users"

    id = sa.Column(sa.Integer, primary_key=True, index=True)
    name = sa.Column(sa.Text, unique=True)
    email = sa.Column(sa.String, unique=True, index=True)
    password = sa.Column(sa.Text)
    
    records = relationship("Workrecord_ORM", back_populates="author")
