from os import access
from app.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST,
    HTTP_401_UNAUTHORIZED,
    HTTP_409_CONFLICT,
)
from flask import Blueprint, app, request, jsonify, g
from flask_jwt_extended import (
    jwt_required,
    create_access_token,
    create_refresh_token,
    get_jwt_identity,
)
from sqlalchemy import func
import datetime
from datetime import date
from app.models import User, Question, db
from app.helper import admin_required


auth = Blueprint("auth", __name__, url_prefix="/api/v1/auth")


def validate_values(data):
    required_fields = [
        "phone_number",
        "lastname",
        "firstname",
        "location",
        "gender",
        "age_group",
    ]
    missing_fields = [field for field in required_fields if field not in data]

    if missing_fields:
        error_message = {"error": f'Missing fields: {", ".join(missing_fields)}'}
        return jsonify(error_message), HTTP_400_BAD_REQUEST

    return None


@auth.get("/")
def create_admin_user():
    admin_username = "admin"
    admin_password = "admin_password"

    # Check if the admin user already exists in the database
    admin_user = User.query.filter_by(username=admin_username).first()

    if not admin_user:
        # If the admin user doesn't exist, create and add them to the database
        admin_user = User(
            username=admin_username,
            password=admin_password,
            phone_number="0705828612",
            lastname="Gates",
            firstname="Admin",
            location="Makerere",
            age_group="19-30",
            role="admin",
            gender="female",
        )
        db.session.add(admin_user)
        db.session.commit()
        return jsonify({"message": "Admin Added"}), HTTP_201_CREATED
    else:
        return jsonify({"message": "Admin already here"}), HTTP_200_OK


@auth.post("/register")
def register():
    data = request.get_json()

    validation_result = validate_values(data)
    if validation_result:
        return validation_result
    # must add a validator function for phone number here

    phone_number = request.json["phone_number"]
    lastname = request.json["lastname"]
    firstname = request.json["firstname"]
    location = request.json["location"]
    age_group = request.json["age_group"]
    gender = request.json["gender"]

    if User.query.filter_by(phone_number=phone_number).first() is not None:
        return jsonify({"error": "Phone number is already taken"}), HTTP_409_CONFLICT

    # Generate username by concatenating firstname and lastname
    username = f"{firstname.lower()}{lastname.lower()}"

    # Use phone number as the password
    password = phone_number

    user = User(
        username=username,
        password=password,
        phone_number=phone_number,
        lastname=lastname,
        firstname=firstname,
        location=location,
        age_group=age_group,
        gender=gender,
    )
    db.session.add(user)
    db.session.commit()

    return (
        username,
        HTTP_201_CREATED,
    )


@auth.post("/login")
def login():
    username = request.json.get("username", "")
    password = request.json.get("password", "")

    user = User.query.filter_by(phone_number=password).first()
    today = datetime.date.today()

    if user:
        is_pass_correct = user.phone_number == password

        if is_pass_correct:
            access = create_access_token(identity=user.id, expires_delta=datetime.timedelta(days=0))
            num_questions = Question.query.filter_by(user_id=user.id).count()
            questions = Question.query.filter_by(user_id=user.id).filter(func.date(Question.created_at) == today).all()
            num_questions_today = Question.query.filter_by(user_id=user.id).filter(func.date(Question.created_at) == date.today()).count()

            question_objects = []
            for question in questions:
                question_objects.append({
                    'sentence': question.sentence,
                    'date': question.created_at.strftime('%Y-%m-%d %H:%M:%S')
                })

            return (
                jsonify(
                    {
                        "access_token": access,
                        "num_questions": num_questions,
                        "todays_questions": question_objects,
                        "total_questions_today": num_questions_today
                    }
                ), HTTP_200_OK,
            )

    return jsonify({"error": "Wrong credentials"}), HTTP_401_UNAUTHORIZED


@auth.get("/me")
@jwt_required()
def me():
    user_id = get_jwt_identity()
    user = User.query.filter_by(id=user_id).first()
    return (
        jsonify(
            {
                "username": user.username,
                "phone_number": user.phone_number,
                "lastname": user.lastname,
                "firstname": user.firstname,
                "location": user.location,
                "role": user.role,
                "gender": user.gender,
            }
        ),
        HTTP_200_OK,
    )


@auth.get("/token/refresh")
@jwt_required(refresh=True)
def refresh_users_token():
    identity = get_jwt_identity()
    access = create_access_token(identity=identity)

    return jsonify({"access": access}), HTTP_200_OK


@auth.get("/user_stats")
@jwt_required()
@admin_required
def user_statistics():
    # Fetch all locations and count the total number of locations
    all_locations = User.query.with_entities(User.location).distinct().all()
    locations_data = [dict(location=row[0]) for row in all_locations]
    total_locations = len(all_locations)

    # Count the total number of male and female users
    total_male_users = User.query.filter_by(gender="male").count()
    total_female_users = User.query.filter_by(gender="female").count()

    # Count the total number of users
    total_users = User.query.count()

    # Count the number of users per location
    users_per_location = []
    for location in all_locations:
        location_name = location[0]
        user_count = User.query.filter_by(location=location_name).count()
        users_per_location.append({"location": location_name, "user_count": user_count})

    # Count the number of users per age group
    age_groups = ["0-18", "19-30", "31-50", "51-65", "65+"]
    users_per_age_group = []
    for age_group in age_groups:
        user_count = User.query.filter_by(age_group=age_group).count()
        users_per_age_group.append({"age_group": age_group, "user_count": user_count})

    # Prepare the response data
    response_data = {
        "locations": locations_data,
        "total_locations": total_locations,
        "total_male_users": total_male_users,
        "total_female_users": total_female_users,
        "total_users": total_users,
        "users_per_location": users_per_location,
        "users_per_age_group": users_per_age_group,
    }
    return jsonify({"data": response_data}), HTTP_200_OK
