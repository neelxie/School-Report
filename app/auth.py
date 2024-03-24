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
from app.helper import admin_required, generate_registration


auth = Blueprint("auth", __name__, url_prefix="/api/v1/auth")


def validate_student(data):
    required_fields = [
        "lastname",
        "firstname",
        "gender",
        "age",
        "nationality",
        "house"
    ]
    missing_fields = [field for field in required_fields if field not in data]

    if missing_fields:
        error_message = {"error": f'Missing fields: {", ".join(missing_fields)}'}
        return jsonify(error_message), HTTP_400_BAD_REQUEST

    return None

def validate_teacher(data):
    required_fields = [
        "lastname",
        "firstname",
        "gender",
        "phone_number"
    ]
    missing_fields = [field for field in required_fields if field not in data]

    if missing_fields:
        error_message = {"error": f'Missing fields: {", ".join(missing_fields)}'}
        return jsonify(error_message), HTTP_400_BAD_REQUEST

    return None

def validate_exam(data):
    required_fields = [
        "user_id",
        "class_id",
        "exam_type",
        "math_marks",
        "english_marks",
        "science_marks",
        "sst_marks"
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
            phone_number="0707467195",
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

    validation_result = validate_student(data)
    if validation_result:
        return validation_result
    # must add a validator function for phone number here
    registration = generate_registration()

    while User.query.filter_by(registration=registration).first():
        registration = generate_registration()


    lastname = request.json["lastname"].strip()
    firstname = request.json["firstname"].strip()
    gender = request.json["gender"]
    nationality = request.json["nationality"]
    house = request.json["house"]
    age = request.json["age"]

    # Generate username by concatenating firstname and lastname
    username = f"{firstname.lower()}{lastname.lower()}"

    user = User(
        lastname=lastname,
        firstname=firstname,
        gender=gender,
        nationality=nationality,
        house=house,
        age=age,
        registration=registration
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

    validation_result = validate_teacher(data)
    if validation_result:
        return validation_result

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
            role = user.role

            return (
                jsonify(
                    {
                        "access_token": access,
                        "role": role
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
@auth.get("/allclasses")
def get_allclasses():
    allclasses = Schoolclass.query.all()
    student_objects = []
    for student in allclasses:
        student_objects.append(
            {
                "id": student.id,
                "class": student.name
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
    social_studies_marks = data.get("sst_marks")

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
    
    exam_results = {
        "math": {"exams": [], "total": 0, "average": 0, "grade": "", "remark": ""},
        "english": {"exams": [], "total": 0, "average": 0, "grade": "", "remark": ""},
        "science": {"exams": [], "total": 0, "average": 0, "grade": "", "remark": ""},
        "social_studies": {"exams": [], "total": 0, "average": 0, "grade": "", "remark": ""}
    }

    for exam in exams:
        exam_info = {
            "exam_type": exam.exam_type,
            "math_marks": exam.math_marks,
            "english_marks": exam.english_marks,
            "science_marks": exam.science_marks,
            "social_studies_marks": exam.social_studies_marks,
            "total_marks": exam.math_marks + exam.english_marks + exam.science_marks + exam.social_studies_marks
        }
        exam_results["math"]["exams"].append(exam_info)
        exam_results["math"]["total"] += exam.math_marks
        exam_results["english"]["exams"].append(exam_info)
        exam_results["english"]["total"] += exam.english_marks
        exam_results["science"]["exams"].append(exam_info)
        exam_results["science"]["total"] += exam.science_marks
        exam_results["social_studies"]["exams"].append(exam_info)
        exam_results["social_studies"]["total"] += exam.social_studies_marks

    # Calculate average marks for each subject
    for subject, subject_data in exam_results.items():
        subject_data["average"] = round((subject_data["total"] / len(subject_data["exams"])), 1) if subject_data["exams"] else 0

    # Assign grades based on average marks
    grade_mapping = {
        "D1": (80, 100),
        "D2": (75, 79),
        "C3": (70, 74),
        "C4": (65, 69),
        "C5": (60, 64),
        "C6": (55, 59),
        "C7": (45, 54),
        "C8": (35, 44),
        "F9": (0, 34)
    }

    for subject, subject_data in exam_results.items():
        for exam in subject_data["exams"]:
            total_marks = exam["total_marks"]
            for grade, (lower_bound, upper_bound) in grade_mapping.items():
                if lower_bound <= subject_data["average"] <= upper_bound:
                    subject_data["grade"] = grade
                    break
            else:
                subject_data["grade"] = "Unknown"

            if subject_data["average"] >= 80:
                subject_data["remark"] = "This is excellent work, continue excelling."
            elif 70 <= subject_data["average"] < 80:
                subject_data["remark"] = "There is still room to improve, aim higher."
            elif 60 <= subject_data["average"] < 70:
                subject_data["remark"] = "Aim for a better grade and pay closer attention."
            else:
                subject_data["remark"] = "Very poor performance. You are encouraged to come with your parent to talk to your teacher to devise a way to improve."

    # Generate report
    report = {
        "student_id": student.id,
        "student_name": f"{student.firstname} {student.lastname}",
        "gender": student.gender,
        "registration": student.registration,
        "gender": student.gender,
        "age": student.age,
        "nationality": student.nationality,
        # "overall_remarks": overall_remarks,
        "exam_results": exam_results
    }


    return jsonify(report), HTTP_201_CREATED


@auth.get('/class_results')
def get_exams_results_by_class():
    """
    Get all students' exam results divided by class.
    """
    # Query all classes
    all_classes = Schoolclass.query.all()

    # Create a dictionary to store exam results by class
    exams_results_by_class = {}

    # Iterate through each class
    for school_class in all_classes:
        class_name = school_class.name

        # Query exam results for students in the current class
        class_exam_results = db.session.query(
            User.firstname,
            User.lastname,
            Exam.exam_type,
            Exam.math_marks,
            Exam.english_marks,
            Exam.science_marks,
            Exam.social_studies_marks
        ).join(Exam).join(Schoolclass).filter(
            Schoolclass.id == school_class.id,
            User.role == 'student'
        ).all()

        # Construct a list containing exam results for students in the current class
        class_results = []
        for result in class_exam_results:
            exam_info = {
                "student_name": f"{result.firstname} {result.lastname}",
                "exam_type": result.exam_type,
                "math_marks": result.math_marks,
                "english_marks": result.english_marks,
                "science_marks": result.science_marks,
                "social_studies_marks": result.social_studies_marks
            }
            class_results.append(exam_info)

        # Add the class results to the dictionary
        exams_results_by_class[class_name] = class_results

    # Return the exam results by class in JSON format
    return jsonify(exams_results_by_class)


