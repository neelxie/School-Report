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
                session["language"] = user.language
                session["category"] = user.category
                session["sub_category"] = user.sub_category
                return redirect(url_for("web.main_review"))
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


@web_bp.route("/main_review")
def main_review():
    access_token = session.get("token")
    role = session.get("role")
    username = session.get("username")
    language = session.get("language")
    category = session.get("category")
    sub_category = session.get("sub_category")
    return render_template(
        "mainReview.html",
        token=access_token,
        role=role,
        user=username,
        language=language,
        category=category,
        sub_category=sub_category,
    )

@web_bp.route("/main_answer")
def main_answer():
    access_token = session.get("token")
    role = session.get("role")
    username = session.get("username")
    language = session.get("language")
    category = session.get("category")
    sub_category = session.get("sub_category")
    return render_template(
        "mainAnswer.html",
        token=access_token,
        role=role,
        user=username,
        language=language,
        category=category,
        sub_category=sub_category,
    )

@web_bp.route("/main_rank")
def main_rank():
    access_token = session.get("token")
    role = session.get("role")
    username = session.get("username")
    language = session.get("language")
    category = session.get("category")
    sub_category = session.get("sub_category")
    return render_template(
        "mainRank.html",
        token=access_token,
        role=role,
        user=username,
        language=language,
        category=category,
        sub_category=sub_category,
    )

@web_bp.route("/expert_english")
def expert_english():
    access_token = session.get("token")
    role = session.get("role")
    username = session.get("username")
    language = session.get("language")
    category = session.get("category")
    sub_category = session.get("sub_category")
    return render_template(
        "expertEnglish.html",
        token=access_token,
        role=role,
        user=username,
        language=language,
        category=category,
        sub_category=sub_category,
    )

@web_bp.route("/expert_luganda")
def expert_luganda():
    access_token = session.get("token")
    role = session.get("role")
    username = session.get("username")
    language = session.get("language")
    category = session.get("category")
    sub_category = session.get("sub_category")
    return render_template(
        "expertLuganda.html",
        token=access_token,
        role=role,
        user=username,
        language=language,
        category=category,
        sub_category=sub_category,
    )

@web_bp.route("/expert_runyankole")
def expert_runyankole():
    access_token = session.get("token")
    role = session.get("role")
    username = session.get("username")
    language = session.get("language")
    category = session.get("category")
    sub_category = session.get("sub_category")
    return render_template(
        "expertRunyankole.html",
        token=access_token,
        role=role,
        user=username,
        language=language,
        category=category,
        sub_category=sub_category,
    )


@web_bp.route("/answer_page.html")
def answer_page():
    access_token = session.get("token")
    role = session.get("role")
    username = session.get("username")
    language = session.get("language")
    category = session.get("category")
    sub_category = session.get("sub_category")

    return render_template(
        "answer_page.html",
                token=access_token,
        role=role,
        user=username,
        language=language,
        category=category,
        sub_category=sub_category,
    )

@web_bp.route("/expert_answers.html")
def expert_answers():
    access_token = session.get("token")
    role = session.get("role")
    username = session.get("username")
    return render_template(
        "expert_answers.html",
        token=access_token,
        role=role,
        user=username
    )


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

@web_bp.route("/download")
def download():
    access_token = session.get("token")
    role = session.get("role")
    username = session.get("username")
    return render_template(
        "download.html", token=access_token, role=role, user=username
    )


@web_bp.route("/experts")
def experts():
    access_token = session.get("token")
    role = session.get("role")
    username = session.get("username")
    return render_template("experts.html", token=access_token, role=role, user=username)


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
    return render_template(
        "runyankole.html", token=access_token, role=role, user=username
    )


@web_bp.route("/my-answers")
def my_answers():
    access_token = session.get("token")
    role = session.get("role")
    username = session.get("username")
    return render_template(
        "myanswers.html", token=access_token, role=role, user=username
    )


@web_bp.route("/dataset")
def upload_dataset():
    access_token = session.get("token")
    role = session.get("role")
    username = session.get("username")
    return render_template("dataset.html", token=access_token, role=role, user=username)
