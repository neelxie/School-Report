from os import access
from app.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_401_UNAUTHORIZED, HTTP_409_CONFLICT
from flask import Blueprint, app, request, jsonify
from werkzeug.security import check_password_hash, generate_password_hash
from flask_jwt_extended import jwt_required, create_access_token, create_refresh_token, get_jwt_identity
from app.models import User, db, AgeGroupEnum

auth = Blueprint("auth", __name__, url_prefix="/api/v1/auth")

def validate_values(data):
    required_fields = ['phone_number', 'lastname', 'firstname', 'location']
    missing_fields = [field for field in required_fields if field not in data]

    if missing_fields:
        error_message = {'error': f'Missing fields: {", ".join(missing_fields)}'}
        return jsonify(error_message), 400

    return None

@auth.post('/register')
def register():
    data = request.get_json()
    phone_number = request.json['phone_number']
    lastname = request.json['lastname']
    firstname  = request.json['firstname']
    location = request.json['location']
    # age_group = request.json['age_group']

    validation_result = validate_values(data)
    if validation_result:
        return validation_result

    # if not username.isalnum() or " " in username:
        # return jsonify({'error': "Username should be alphanumeric, also no spaces"}), HTTP_400_BAD_REQUEST

    # must add a validator function for phone number here

    if User.query.filter_by(phone_number=phone_number).first() is not None:
        return jsonify({'error': "Phone number is taken"}), HTTP_409_CONFLICT

    # Generate username by concatenating firstname and lastname
    username = f"{firstname.lower()}{lastname.lower()}"
    print(username)
    # Use phone number as the password
    password = phone_number


    user = User(username=username, password=password, phone_number=phone_number, lastname=lastname, firstname=firstname, location=location, age_group=AgeGroupEnum.ADULT)
    db.session.add(user)
    db.session.commit()

    return jsonify({
        'message': "User created",
        'user': {
            'username': username, "phone_number": phone_number
        }

    }), HTTP_201_CREATED


@auth.post('/login')
def login():
    username = request.json.get('username', '')
    password = request.json.get('password', '')

    user = User.query.filter_by(phone_number=password).first()

    if user:
        is_pass_correct = user.phone_number == password

        if is_pass_correct:
            refresh = create_refresh_token(identity=user.id)
            access = create_access_token(identity=user.id)

            return jsonify({
                'user': {
                    'refresh': refresh,
                    'access': access,
                    'username': user.username,
                    'phone_number': user.phone_number
                }

            }), HTTP_200_OK

    return jsonify({'error': 'Wrong credentials'}), HTTP_401_UNAUTHORIZED


@auth.get("/me")
@jwt_required()
def me():
    user_id = get_jwt_identity()
    user = User.query.filter_by(id=user_id).first()
    return jsonify({
        'username': user.username,
        'phone_number': user.phone_number,
        'lastname':user.lastname,
        'firstname': user.firstname,
        'location':user.location
    }), HTTP_200_OK


@auth.get('/token/refresh')
@jwt_required(refresh=True)
def refresh_users_token():
    identity = get_jwt_identity()
    access = create_access_token(identity=identity)

    return jsonify({
        'access': access
    }), HTTP_200_OK