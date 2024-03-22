import datetime
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class User(db.Model):
    """user table definition"""

    __tablename__ = "user_accounts"

    id = db.Column(db.Integer, primary_key=True)
    lastname = db.Column(db.String(80), nullable=False)
    firstname = db.Column(db.String(80), nullable=False)
    username = db.Column(db.String(80), nullable=False)
    role = db.Column(db.String(20), default="farmer")
    gender = db.Column(db.String(10), nullable=False)
    phone_number = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, onupdate=datetime.now())
    class_id = db.Column(db.Integer, db.ForeignKey('class.id'))
    exams = db.relationship('Exam', backref='user', lazy=True)

    def __repr__(self) -> str:
        return "User>>> {self.username}"


class Class(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    users = db.relationship('User', backref='class', lazy=True)
    exams = db.relationship('Exam', backref='class', lazy=True)

class Exam(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    class_id = db.Column(db.Integer, db.ForeignKey('class.id'), nullable=False)
    exam_type = db.Column(db.Enum('beginning', 'mid', 'end'), nullable=False)
    math_marks = db.Column(db.Float)
    english_marks = db.Column(db.Float)
    science_marks = db.Column(db.Float)
    social_studies_marks = db.Column(db.Float)
