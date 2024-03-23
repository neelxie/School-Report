from os import access
from app.helper import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST,
    HTTP_401_UNAUTHORIZED,
    HTTP_409_CONFLICT,
    HTTP_404_NOT_FOUND
)
from flask import Blueprint, app, request, jsonify, g
from flask_jwt_extended import (
    jwt_required,
    create_access_token,
    create_refresh_token,
    verify_jwt_in_request,
    get_jwt_identity,
)
import datetime
from datetime import date
from app.models import User, Exam, db, Schoolclass
from app.helper import admin_required
import json
import pandas as pd
import random
from sqlalchemy import func, or_, and_, not_, text
from app.helper import admin_required


auth = Blueprint("auth", __name__, url_prefix="/api/v1/auth")


def validate_values(data):
    required_fields = [
        "lastname",
        "firstname",
        "gender",
    ]
    missing_fields = [field for field in required_fields if field not in data]

    if missing_fields:
        error_message = {"error": f'Missing fields: {", ".join(missing_fields)}'}
        return jsonify(error_message), HTTP_400_BAD_REQUEST

    return None


@auth.get("/admin")
def create_admin_user():
    admin_username = "admin"
    admin_password = "password"

    # Check if the admin user already exists in the database
    admin_user = User.query.filter_by(username=admin_username).first()

    if not admin_user:
        # If the admin user doesn't exist, create and add them to the database
        admin_user = User(
            username=admin_username,
            password=admin_password,
            phone_number="0705828612",
            lastname="Nabakooza",
            firstname="Lydia",
            role="admin",
            gender="female",
        )
        db.session.add(admin_user)
        db.session.commit()
        return jsonify({"message": "Admin Added"}), HTTP_201_CREATED
    else:
        return jsonify({"message": "Admin already here"}), HTTP_200_OK


@auth.post("/register_student")
def register():
    data = request.get_json()

    validation_result = validate_values(data)
    if validation_result:
        return validation_result
    # must add a validator function for phone number here

    lastname = request.json["lastname"].strip()
    firstname = request.json["firstname"].strip()
    gender = request.json["gender"]

    # Generate username by concatenating firstname and lastname
    username = f"{firstname.lower()}{lastname.lower()}"

    user = User(
        lastname=lastname,
        firstname=firstname,
        gender=gender,
    )
    db.session.add(user)
    db.session.commit()

    return (
        username,
        HTTP_201_CREATED,
    )


@jwt_required()
@auth.post("/register_teacher")
def register_teacher():
    data = request.get_json()

    phone_number = data["phone_number"].strip()
    lastname = data["lastname"].strip()
    firstname = data["firstname"].strip()
    gender = data["gender"]

    if User.query.filter_by(phone_number=phone_number).first():
        return jsonify({"error": "Phone number is already taken"}), HTTP_409_CONFLICT

    username = f"{firstname.lower()}{lastname.lower()}"

    password = phone_number

    teacher = User(
        username=username,
        password=password,
        phone_number=phone_number,
        lastname=lastname,
        firstname=firstname,
        gender=gender,
        role="teacher",
    )

    db.session.add(teacher)
    db.session.commit()

    return jsonify({"message": "Teacher registered successfully"}), HTTP_201_CREATED


@auth.post("/login")
def login():
    username = request.json.get("username", "")
    password = request.json.get("password", "")

    user = User.query.filter_by(phone_number=password).first()

    if user:
        is_pass_correct = user.phone_number == password

        if is_pass_correct:
            access = create_access_token(
                identity=user.id, expires_delta=datetime.timedelta(days=0)
            )

            return (
                jsonify(
                    {
                        "access_token": access,
                    }
                ),
                HTTP_200_OK,
            )

    return jsonify({"error": "Wrong credentials"}), HTTP_401_UNAUTHORIZED


@jwt_required()
@auth.get("/students")
def students():
    users = (
        User.query.filter_by(role="student")
        .all()
    )
    students = User.query.filter_by(role="student").all()
    student_objects = []
    for student in users:
        student_objects.append(
            {
                "user_id": student.id,
                "lastname": student.lastname,
                "firstname": student.firstname,
                "gender": student.gender,
            }
        )
    return (
        jsonify(student_objects),
        HTTP_200_OK,
    )


@jwt_required()
@auth.get("/teachers")
def get_teachers():
    teachers = User.query.filter_by(role="teacher").all()
    student_objects = []
    for student in teachers:
        student_objects.append(
            {
                "user_id": student.id,
                "username": student.username,
                "phone_number": student.phone_number,
                "lastname": student.lastname,
                "firstname": student.firstname,
                "gender": student.gender,
            }
        )
    return (
        jsonify(student_objects),
        HTTP_200_OK,
    )

@jwt_required()
@auth.post("/create_class")
def create_class():
    data = request.get_json()

    class_name = data.get("class_name")

    if not class_name:
        return jsonify({"error": "Class name is required"}), HTTP_400_BAD_REQUEST

    new_class = Schoolclass(name=class_name)
    db.session.add(new_class)
    db.session.commit()

    return jsonify({"message": "Class created successfully"}), HTTP_201_CREATED

@jwt_required()
@auth.post("/create_exam")
def create_exam():
    data = request.get_json()

    student_id = data.get("student_id")
    class_id = data.get("class_id")
    exam_type = data.get("exam_type")
    math_marks = data.get("math_marks")
    english_marks = data.get("english_marks")
    science_marks = data.get("science_marks")
    social_studies_marks = data.get("social_studies_marks")

    if not all([student_id, class_id, exam_type, math_marks, english_marks, science_marks, social_studies_marks]):
        return jsonify({"error": "Incomplete data provided"}), HTTP_400_BAD_REQUEST

    exam = Exam(
        user_id=student_id,
        class_id=class_id,
        exam_type=exam_type,
        math_marks=math_marks,
        english_marks=english_marks,
        science_marks=science_marks,
        social_studies_marks=social_studies_marks,
    )
    db.session.add(exam)
    db.session.commit()

    return jsonify({"message": "Exam recorded successfully"}), HTTP_201_CREATED

@auth.get("/generate_report/<int:student_id>")
@jwt_required()
def generate_report(student_id):
    # Retrieve student
    student = User.query.get(student_id)
    if not student:
        return jsonify({"error": "Student not found"}), HTTP_404_NOT_FOUND

    # Retrieve exams for the student
    exams = Exam.query.filter_by(user_id=student_id).all()

    if not exams:
        return jsonify({"message": "No exams found for this student"}), HTTP_404_NOT_FOUND

    # Calculate total marks for each subject and overall marks
    total_marks = {"math": 0, "english": 0, "science": 0, "social_studies": 0}
    total_exams = {"beginning": 0, "mid": 0, "end": 0}

    for exam in exams:
        total_marks["math"] += exam.math_marks
        total_marks["english"] += exam.english_marks
        total_marks["science"] += exam.science_marks
        total_marks["social_studies"] += exam.social_studies_marks

        total_exams[exam.exam_type] += (
            exam.math_marks
            + exam.english_marks
            + exam.science_marks
            + exam.social_studies_marks
        )

    # Calculate total percentage for each subject
    total_percentage = {}
    for subject, marks in total_marks.items():
        total_percentage[subject] = (marks / (len(exams) * 100 * 4)) * 100

    # Calculate total marks and percentage for each exam type
    total_marks_percentage = {}
    for exam_type, marks in total_exams.items():
        total_marks_percentage[exam_type] = (marks / (len(exams) * 400)) * 100

    # Calculate overall remarks based on total marks
    total_marks_percentage["overall"] = sum(total_marks_percentage.values())
    remarks = ""

    if total_marks_percentage["overall"] >= 370:
        remarks = "This is excellent work, continue excelling."
    elif 300 <= total_marks_percentage["overall"] < 370:
        remarks = "There is still room to improve, aim higher."
    elif 200 <= total_marks_percentage["overall"] < 300:
        remarks = "Aim for a better grade and pay closer attention."
    else:
        remarks = "Very poor performance. You are encouraged to come with your parent to talk to your teacher to devise a way to improve."

    # Generate report
    report = {
        "student_id": student_id,
        "student_name": f"{student.firstname} {student.lastname}",
        "subject_breakdown": total_percentage,
        "exam_details": total_marks_percentage,
        "teacher_remarks": remarks
    }

    return jsonify(report), HTTP_201_CREATED

