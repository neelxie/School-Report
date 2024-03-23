from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


db = SQLAlchemy()


class User(db.Model):
    """user table definition"""

    __tablename__ = "user_accounts"

    id = db.Column(db.Integer, primary_key=True)
    lastname = db.Column(db.String(80), nullable=False)
    firstname = db.Column(db.String(80), nullable=False)
    username = db.Column(db.String(80), nullable=True)
    role = db.Column(db.String(20), default="student")
    gender = db.Column(db.String(10), nullable=False)
    phone_number = db.Column(db.String(120), unique=True, nullable=True)
    password = db.Column(db.String(120), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, onupdate=datetime.now())
    exams = db.relationship('Exam', backref='user', lazy=True)
    

    def __repr__(self) -> str:
        return "User>>> {self.username}"


class Schoolclass(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    exams = db.relationship('Exam', backref='schoolclass', lazy=True)

class Exam(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user_accounts.id'), nullable=False)
    class_id = db.Column(db.Integer, db.ForeignKey('schoolclass.id'), nullable=False)
    exam_type = db.Column(db.String, nullable=False)
    math_marks = db.Column(db.Float)
    english_marks = db.Column(db.Float)
    science_marks = db.Column(db.Float)
    social_studies_marks = db.Column(db.Float)
