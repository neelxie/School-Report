# from flask import current_app
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import text as sa_text
from sqlalchemy import Enum
# from flask_bcrypt import Bcrypt
# from flask_jwt_extended import create_access_token
from datetime import timedelta
import uuid

import enum

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class LanguageEnum(enum.Enum):
    ENGLISH = 'English'
    LUGANDA = 'Luganda'

class AgeGroupEnum(enum.Enum):
    CHILD = 'Child'  # 0-12 years old
    TEENAGER = 'Teenager'  # 13-19 years old
    YOUNG_ADULT = 'Young Adult'  # 20-29 years old
    ADULT = 'Adult'  # 30-59 years old
    SENIOR = 'Senior'  # 60 years old and above

class User(db.Model):
    """ user table definition """

    _tablename_ = "users"

    # id = db.Column(UUID(as_uuid=True), primary_key=True,
    #                server_default=sa_text("uuid_generate_v4()"))
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    lastname = db.Column(db.String(80), nullable=False)
    firstname = db.Column(db.String(80), nullable=False)
    username = db.Column(db.String(80), nullable=False)
    location = db.Column(db.String(80), nullable=False)
    age_group = db.Column(Enum(AgeGroupEnum))
    phone_number = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now())
    questions = db.relationship('Question', backref="user")

    def __repr__(self) -> str:
        return 'User>>> {self.username}'


class Question(db.Model):
    # id = db.Column(db.Integer, primary_key=True)
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    answer = db.Column(db.Text, nullable=True)
    sentence = db.Column(db.Text, nullable=False)
    language = db.Column(Enum(LanguageEnum), nullable=False)
    user_id = db.Column(UUID, db.ForeignKey('user.id'))
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, onupdate=datetime.now())


    def __repr__(self) -> str:
        return 'Question>>> {self.sentence}'