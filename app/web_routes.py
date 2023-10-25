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
    return render_template(
        "dashboard.html", token=access_token, role=role, user=username
    )


@web_bp.route("/crop_expert")
def crop_expert():
    access_token = session.get("token")
    role = session.get("role")
    username = session.get("username")
    return render_template(
        "crop_expert.html", token=access_token, role=role, user=username
    )


@web_bp.route("/animal_expert")
def animal_expert():
    access_token = session.get("token")
    role = session.get("role")
    username = session.get("username")
    return render_template(
        "animal_expert.html", token=access_token, role=role, user=username
    )


@web_bp.route("/answer_page.html")
def answer_page():
    access_token = session.get("token")
    role = session.get("role")
    username = session.get("username")

    return render_template(
        "answer_page.html",
        token=access_token,
        role=role,
        user=username,
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


@web_bp.route("/experts")
def experts():
    access_token = session.get("token")
    role = session.get("role")
    username = session.get("username")
    return render_template("experts.html", token=access_token, role=role, user=username)


@web_bp.route("/expert_dash_crop")
def expert_dashboard_crop():
    access_token = session.get("token")
    role = session.get("role")
    username = session.get("username")
    return render_template(
        "expertDashCrop.html", token=access_token, role=role, user=username
    )


@web_bp.route("/expert_dash_animal")
def expert_dashboard_animal():
    access_token = session.get("token")
    role = session.get("role")
    username = session.get("username")
    return render_template(
        "expertDashAnimal.html", token=access_token, role=role, user=username
    )


@web_bp.route("/english_review_animal")
def english_review_animal():
    access_token = session.get("token")
    role = session.get("role")
    username = session.get("username")
    return render_template(
        "englishReviewAnimal.html", token=access_token, role=role, user=username
    )


@web_bp.route("/luganda_review_animal")
def luganda_review_animal():
    access_token = session.get("token")
    role = session.get("role")
    username = session.get("username")
    return render_template(
        "lugandaReviewAnimal.html", token=access_token, role=role, user=username
    )


@web_bp.route("/runyankole_review_animal")
def runyankole_review_animal():
    access_token = session.get("token")
    role = session.get("role")
    username = session.get("username")
    return render_template(
        "runyankoleReviewAnimal.html", token=access_token, role=role, user=username
    )


@web_bp.route("/english_review_crop")
def english_review_crop():
    access_token = session.get("token")
    role = session.get("role")
    username = session.get("username")
    return render_template(
        "englishReviewCrop.html", token=access_token, role=role, user=username
    )


@web_bp.route("/luganda_review_crop")
def luganda_review_crop():
    access_token = session.get("token")
    role = session.get("role")
    username = session.get("username")
    return render_template(
        "lugandaReviewCrop.html", token=access_token, role=role, user=username
    )


@web_bp.route("/runyankole_review_crop")
def runyankole_review_crop():
    access_token = session.get("token")
    role = session.get("role")
    username = session.get("username")
    return render_template(
        "runyankoleReviewCrop.html", token=access_token, role=role, user=username
    )


@web_bp.route("/answer_animal")
def answer_questions_animal():
    access_token = session.get("token")
    role = session.get("role")
    username = session.get("username")
    return render_template(
        "answerAnimal.html", token=access_token, role=role, user=username
    )


@web_bp.route("/answer_crop")
def answer_questions_crop():
    access_token = session.get("token")
    role = session.get("role")
    username = session.get("username")
    return render_template(
        "answerCrop.html", token=access_token, role=role, user=username
    )


@web_bp.route("/rank_animal")
def rank_answers_animal():
    access_token = session.get("token")
    role = session.get("role")
    username = session.get("username")
    return render_template(
        "rankAnimal.html", token=access_token, role=role, user=username
    )


@web_bp.route("/english_answer_animal")
def english_answer_animal():
    access_token = session.get("token")
    role = session.get("role")
    username = session.get("username")
    return render_template(
        "englishAnswerAnimal.html", token=access_token, role=role, user=username
    )


@web_bp.route("/english_rank_animal")
def english_rank_animal():
    access_token = session.get("token")
    role = session.get("role")
    username = session.get("username")
    return render_template(
        "englishRankAnimal.html", token=access_token, role=role, user=username
    )


@web_bp.route("/luganda_answer_animal")
def luganda_answer_animal():
    access_token = session.get("token")
    role = session.get("role")
    username = session.get("username")
    return render_template(
        "lugandaAnswerAnimal.html", token=access_token, role=role, user=username
    )


@web_bp.route("/luganda_rank_animal")
def luganda_rank_animal():
    access_token = session.get("token")
    role = session.get("role")
    username = session.get("username")
    return render_template(
        "lugandaRankAnimal.html", token=access_token, role=role, user=username
    )


@web_bp.route("/runyankole_answer_animal")
def runyankole_answer_animal():
    access_token = session.get("token")
    role = session.get("role")
    username = session.get("username")
    return render_template(
        "runyankoleAnswerAnimal.html", token=access_token, role=role, user=username
    )


@web_bp.route("/runyankole_rank_animal")
def runyankole_rank_animal():
    access_token = session.get("token")
    role = session.get("role")
    username = session.get("username")
    return render_template(
        "runyankoleRankAnimal.html", token=access_token, role=role, user=username
    )


@web_bp.route("/rank_crop")
def rank_answers_crop():
    access_token = session.get("token")
    role = session.get("role")
    username = session.get("username")
    return render_template(
        "rankCrop.html", token=access_token, role=role, user=username
    )


@web_bp.route("/english_answer_crop")
def english_answer_crop():
    access_token = session.get("token")
    role = session.get("role")
    username = session.get("username")
    return render_template(
        "englishAnswerCrop.html", token=access_token, role=role, user=username
    )


@web_bp.route("/english_rank_crop")
def english_rank_crop():
    access_token = session.get("token")
    role = session.get("role")
    username = session.get("username")
    return render_template(
        "englishRankCrop.html", token=access_token, role=role, user=username
    )


@web_bp.route("/luganda_answer_crop")
def luganda_answer_crop():
    access_token = session.get("token")
    role = session.get("role")
    username = session.get("username")
    return render_template(
        "lugandaAnswerCrop.html", token=access_token, role=role, user=username
    )


@web_bp.route("/luganda_rank_crop")
def luganda_rank_crop():
    access_token = session.get("token")
    role = session.get("role")
    username = session.get("username")
    return render_template(
        "lugandaRankCrop.html", token=access_token, role=role, user=username
    )


@web_bp.route("/runyankole_answer_crop")
def runyankole_answer_crop():
    access_token = session.get("token")
    role = session.get("role")
    username = session.get("username")
    return render_template(
        "runyankoleAnswerCrop.html", token=access_token, role=role, user=username
    )


@web_bp.route("/runyankole_rank_crop")
def runyankole_rank_crop():
    access_token = session.get("token")
    role = session.get("role")
    username = session.get("username")
    return render_template(
        "runyankoleRankCrop.html", token=access_token, role=role, user=username
    )


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


@web_bp.route("/upload_dataset")
def upload_dataset():
    access_token = session.get("token")
    role = session.get("role")
    username = session.get("username")
    return render_template("dataset.html", token=access_token, role=role, user=username)
