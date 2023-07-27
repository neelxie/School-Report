# from flask import current_app
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import text as sa_text
import datetime
import uuid
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class User(db.Model):
    """user table definition"""

    _tablename_ = "users"

    # id = db.Column(UUID(as_uuid=True), primary_key=True, server_default=sa_text("uuid_generate_v4()"))
    id = db.Column(db.Integer, primary_key=True)
    lastname = db.Column(db.String(80), nullable=False)
    firstname = db.Column(db.String(80), nullable=False)
    username = db.Column(db.String(80), nullable=False)
    location = db.Column(db.String(80), nullable=False)
    age_group = db.Column(db.String(10), nullable=False)
    role = db.Column(db.String(20), default="farmer")
    gender = db.Column(db.String(10), nullable=False)
    phone_number = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now())
    questions = db.relationship("Question", backref="user")

    def __repr__(self) -> str:
        return "User>>> {self.username}"


class Question(db.Model):
    __tablename__ = "questions"
    # id = db.Column(UUID(as_uuid=True), primary_key=True, server_default=sa_text("uuid_generate_v4()"))
    id = db.Column(db.Integer, primary_key=True)
    answer = db.Column(db.Text, nullable=True)
    sentence = db.Column(db.Text, nullable=False)
    language = db.Column(db.String(10), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, onupdate=datetime.now())

    def __repr__(self) -> str:
        return "Question>>> {self.sentence}"
