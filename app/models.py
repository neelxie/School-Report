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
    location = db.Column(db.String(80), nullable=False)
    age_group = db.Column(db.String(10), nullable=False)
    role = db.Column(db.String(20), default="farmer")
    gender = db.Column(db.String(10), nullable=False)
    phone_number = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now())
    organisation = db.Column(db.String(120))
    email = db.Column(db.String(120), unique=True, nullable=True)
    questions = db.relationship(
        "Question", backref="user", foreign_keys="Question.user_id"
    )

    def __repr__(self) -> str:
        return "User>>> {self.username}"


class Question(db.Model):
    __tablename__ = "questions"
    id = db.Column(db.Integer, primary_key=True)
    sentence = db.Column(db.Text, nullable=False)
    language = db.Column(db.String(10), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user_accounts.id"), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, onupdate=datetime.now())
    topic = db.Column(db.String, nullable=True)
    reviewer_id = db.Column(
        db.Integer, db.ForeignKey("user_accounts.id"), nullable=True
    )
    rephrased = db.Column(db.Text, nullable=True)
    category = db.Column(db.Text, nullable=True)
    animal_crop = db.Column(db.Text, nullable=True)
    location = db.Column(db.String(80), nullable=True)
    reviewed = db.Column(db.Boolean, default=False)
    correct = db.Column(db.Boolean, default=False)
    answers = db.relationship("Answer", backref="question")

    def __repr__(self) -> str:
        return "Question>>> {self.sentence}"


class Answer(db.Model):
    __tablename__ = "answers"

    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey("questions.id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user_accounts.id"), nullable=False)
    answer_text = db.Column(db.String, nullable=False)
    source = db.Column(db.String(100), nullable=False)
    rank = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.now())
    fluency = db.Column(db.Integer, nullable=True, default=0)
    relevance = db.Column(db.Integer, nullable=True, default=0)
    coherence = db.Column(db.Integer, nullable=True, default=0)


    def __repr__(self) -> str:
        return f"Answer>>> {self.answer_text}"
