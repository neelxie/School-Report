# admin_decorator.py

from functools import wraps
from flask import request, jsonify, current_app
from app.models import User, db
from flask_jwt_extended import decode_token
import random

def number_class(num):
    if num == 1:
        return "Primary One"
    elif num == 2:
        return "Primary Two"
    elif num == 3:
        return "Primary Three"
    elif num == 4:
        return "Primary Four"
    elif num == 5:
        return "Primary Five"
    elif num == 6:
        return "Primary Six"
    elif num == 7:
        return "Primary Seven"
    else:
        return "Number out of range"



def clean_token(token):
    if token.startswith("Bearer "):
        token = token.split(" ")[1]
    return token

def generate_registration():
    """Generate a new student registration number."""
    return 'U002342024' + ''.join(random.choices('0123456789', k=5))


def get_authenticated_user():
    token = request.headers.get("Authorization")  # Example for token from headers

    if not token:
        return None


    cleaned_token = clean_token(token)
    decoded_token = decode_token(cleaned_token)
    user_id = decoded_token["sub"]

    # Fetch the user from the database based on the user_id in the token
    user = User.query.get(user_id)
    if user:
        return user.__dict__
    else:
        return None


def admin_required(endpoint):
    @wraps(endpoint)
    def wrapper(*args, **kwargs):
        user = get_authenticated_user()
        
        picked_role = user["role"]
        if not user:
            return jsonify({"error": "Unauthorized"}), 401

        if picked_role != "admin":
            return jsonify({"error": "Admin access required"}), 403

        return endpoint(*args, **kwargs)

    return wrapper

HTTP_200_OK = 200
HTTP_201_CREATED = 201
HTTP_202_ACCEPTED = 202
HTTP_203_NON_AUTHORITATIVE_INFORMATION = 203
HTTP_204_NO_CONTENT = 204
HTTP_205_RESET_CONTENT = 205
HTTP_206_PARTIAL_CONTENT = 206
HTTP_207_MULTI_STATUS = 207
HTTP_208_ALREADY_REPORTED = 208
HTTP_226_IM_USED = 226
HTTP_300_MULTIPLE_CHOICES = 300
HTTP_301_MOVED_PERMANENTLY = 301
HTTP_302_FOUND = 302
HTTP_303_SEE_OTHER = 303
HTTP_304_NOT_MODIFIED = 304
HTTP_305_USE_PROXY = 305
HTTP_306_RESERVED = 306
HTTP_307_TEMPORARY_REDIRECT = 307
HTTP_308_PERMANENT_REDIRECT = 308
HTTP_400_BAD_REQUEST = 400
HTTP_401_UNAUTHORIZED = 401
HTTP_402_PAYMENT_REQUIRED = 402
HTTP_403_FORBIDDEN = 403
HTTP_404_NOT_FOUND = 404
HTTP_405_METHOD_NOT_ALLOWED = 405
HTTP_406_NOT_ACCEPTABLE = 406
HTTP_407_PROXY_AUTHENTICATION_REQUIRED = 407
HTTP_408_REQUEST_TIMEOUT = 408
HTTP_409_CONFLICT = 409
HTTP_410_GONE = 410
HTTP_411_LENGTH_REQUIRED = 411
HTTP_412_PRECONDITION_FAILED = 412
HTTP_413_REQUEST_ENTITY_TOO_LARGE = 413
HTTP_414_REQUEST_URI_TOO_LONG = 414
HTTP_415_UNSUPPORTED_MEDIA_TYPE = 415
HTTP_416_REQUESTED_RANGE_NOT_SATISFIABLE = 416
HTTP_417_EXPECTATION_FAILED = 417
HTTP_422_UNPROCESSABLE_ENTITY = 422
HTTP_423_LOCKED = 423
HTTP_424_FAILED_DEPENDENCY = 424
HTTP_426_UPGRADE_REQUIRED = 426
HTTP_428_PRECONDITION_REQUIRED = 428
HTTP_429_TOO_MANY_REQUESTS = 429
HTTP_431_REQUEST_HEADER_FIELDS_TOO_LARGE = 431
HTTP_451_UNAVAILABLE_FOR_LEGAL_REASONS = 451
HTTP_500_INTERNAL_SERVER_ERROR = 500
HTTP_501_NOT_IMPLEMENTED = 501
HTTP_502_BAD_GATEWAY = 502
HTTP_503_SERVICE_UNAVAILABLE = 503
HTTP_504_GATEWAY_TIMEOUT = 504
HTTP_505_HTTP_VERSION_NOT_SUPPORTED = 505
HTTP_506_VARIANT_ALSO_NEGOTIATES = 506
HTTP_507_INSUFFICIENT_STORAGE = 507
HTTP_508_LOOP_DETECTED = 508
HTTP_509_BANDWIDTH_LIMIT_EXCEEDED = 509
HTTP_510_NOT_EXTENDED = 510
HTTP_511_NETWORK_AUTHENTICATION_REQUIRED = 511


def is_informational(status):
    # 1xx
    pass


def is_success(status):
    # 2xx
    pass


def is_redirect(status):
    # 3xx
    pass


def is_client_error():
    # 4xx
    pass


def is_server_error():
    # 5xx
    pass