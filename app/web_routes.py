from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from app.models import User, Question, db
import datetime
from flask_jwt_extended import (
    create_access_token,
)


web_bp = Blueprint("web", __name__)


@web_bp.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        error_message = None

        user = User.query.filter_by(phone_number=password).first()

        if user and user.phone_number == password:
            access_token = create_access_token(
                identity=user.id, expires_delta=datetime.timedelta(days=0)
            )
            if user.role == "admin":
                flash("Access granted.")
                session["token"] = access_token
                session["role"] = user.role
                session["username"] = user.username
                return redirect(url_for("web.admin"))
                # return render_template('admin.html', token=access_token, role=user.role, user=user.username)

            elif user.role == "expert":
                flash("Access granted.")
                session["token"] = access_token
                session["role"] = user.role
                session["username"] = user.username
                return redirect(url_for('web.choose'))
                # return render_template(
                #     "dashboard.html",
                #     token=access_token,
                #     role=user.role,
                #     user=user.username,
                # )
            else:
                pass
        if not user:
            error_message = "Wrong Credentials. You don't have access to the admin or recommender area."
            return render_template("login.html", error_message=error_message)

    return render_template("login.html")


@web_bp.route("/admin")
def admin():
    access_token = session.get("token")
    role = session.get("role")
    username = session.get("username")
    return render_template("admin.html", token=access_token, role=role, user=username)

@web_bp.route("/choose")
def choose():
    access_token = session.get("token")
    role = session.get("role")
    username = session.get("username")
    return render_template("choose.html", token=access_token, role=role, user=username)

@web_bp.route("/dash")
def dash():
    access_token = session.get("token")
    role = session.get("role")
    username = session.get("username")
    return render_template("dashboard.html", token=access_token, role=role, user=username)

@web_bp.route("/crop_expert")
def crop_expert():
    access_token = session.get("token")
    role = session.get("role")
    username = session.get("username")
    return render_template("dashboard.html", token=access_token, role=role, user=username)

@web_bp.route("/animal_expert")
def animal_expert():
    access_token = session.get("token")
    role = session.get("role")
    username = session.get("username")
    return render_template("dashboard.html", token=access_token, role=role, user=username)


@web_bp.route("/farmers")
def farmers():
    access_token = session.get("token")
    role = session.get("role")
    username = session.get("username")
    return render_template("farmers.html", token=access_token, role=role, user=username)


@web_bp.route("/questions")
def questions():
    access_token = session.get("token")
    role = session.get("role")
    username = session.get("username")
    return render_template(
        "questions.html", token=access_token, role=role, user=username
    )


@web_bp.route("/experts")
def experts():
    access_token = session.get("token")
    role = session.get("role")
    username = session.get("username")
    return render_template("experts.html", token=access_token, role=role, user=username)


@web_bp.route("/expert_dash")
def expert_dashboard():
    access_token = session.get("token")
    role = session.get("role")
    username = session.get("username")
    return render_template(
        "expertDash.html", token=access_token, role=role, user=username
    )


@web_bp.route("/english_review")
def english_review():
    access_token = session.get("token")
    role = session.get("role")
    username = session.get("username")
    return render_template(
        "englishReview.html", token=access_token, role=role, user=username
    )


@web_bp.route("/luganda_review")
def luganda_review():
    access_token = session.get("token")
    role = session.get("role")
    username = session.get("username")
    return render_template(
        "lugandaReview.html", token=access_token, role=role, user=username
    )

@web_bp.route("/runyankole_review")
def runyankole_review():
    access_token = session.get("token")
    role = session.get("role")
    username = session.get("username")
    return render_template(
        "runyankoleReview.html", token=access_token, role=role, user=username
    )

@web_bp.route("/answer")
def answer_questions():
    access_token = session.get("token")
    role = session.get("role")
    username = session.get("username")
    return render_template("answer.html", token=access_token, role=role, user=username)


@web_bp.route("/rank")
def rank_answers():
    access_token = session.get("token")
    role = session.get("role")
    username = session.get("username")
    return render_template("rank.html", token=access_token, role=role, user=username)

@web_bp.route("/english_answer")
def english_answer():
    access_token = session.get("token")
    role = session.get("role")
    username = session.get("username")
    return render_template("englishAnswer.html", token=access_token, role=role, user=username)


@web_bp.route("/english_rank")
def english_rank():
    access_token = session.get("token")
    role = session.get("role")
    username = session.get("username")
    return render_template("englishRank.html", token=access_token, role=role, user=username)

@web_bp.route("/luganda_answer")
def luganda_answer():
    access_token = session.get("token")
    role = session.get("role")
    username = session.get("username")
    return render_template("lugandaAnswer.html", token=access_token, role=role, user=username)


@web_bp.route("/luganda_rank")
def luganda_rank():
    access_token = session.get("token")
    role = session.get("role")
    username = session.get("username")
    return render_template("lugandaRank.html", token=access_token, role=role, user=username)

@web_bp.route("/runyankole_answer")
def runyankole_answer():
    access_token = session.get("token")
    role = session.get("role")
    username = session.get("username")
    return render_template("runyankoleAnswer.html", token=access_token, role=role, user=username)


@web_bp.route("/runyankole_rank")
def runyankole_rank():
    access_token = session.get("token")
    role = session.get("role")
    username = session.get("username")
    return render_template("runyankoleRank.html", token=access_token, role=role, user=username)


@web_bp.route("/luganda")
def luganda():
    access_token = session.get("token")
    role = session.get("role")
    username = session.get("username")
    return render_template("luganda.html", token=access_token, role=role, user=username)


@web_bp.route("/english")
def english():
    access_token = session.get("token")
    role = session.get("role")
    username = session.get("username")
    return render_template("english.html", token=access_token, role=role, user=username)

@web_bp.route("/runyankole")
def runyankole():
    access_token = session.get("token")
    role = session.get("role")
    username = session.get("username")
    return render_template("runyankole.html", token=access_token, role=role, user=username)


@web_bp.route("/upload_dataset")
def upload_dataset():
    access_token = session.get("token")
    role = session.get("role")
    username = session.get("username")
    return render_template("dataset.html", token=access_token, role=role, user=username)
