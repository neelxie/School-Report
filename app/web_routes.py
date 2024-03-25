from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from app.models import User, Exam, db, Schoolclass
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

            elif user.role == "teacher":
                flash("Access granted.")
                session["token"] = access_token
                session["role"] = user.role
                session["my_id"] = user.id
                session["username"] = user.username
                return redirect(url_for("web.teacher"))
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


@web_bp.route("/teacher")
def teacher():
    access_token = session.get("token")
    role = session.get("role")
    username = session.get("username")
    return render_template(
        "teach.html",
        token=access_token,
        role=role,
        user=username
    )

@web_bp.route("/student_results.html")
def student_results():
    
    access_token = session.get("token")
    role = session.get("role")
    username = session.get("username")
    my_id = session.get("my_id")
    return render_template(
        "student_results.html",
        token=access_token,
        role=role,
        user=username,
        my_id =my_id
    )


@web_bp.route("/download")
def download():
    access_token = session.get("token")
    role = session.get("role")
    username = session.get("username")
    return render_template(
        "download.html", token=access_token, role=role, user=username
    )
