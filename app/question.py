from app.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_204_NO_CONTENT,
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_409_CONFLICT,
)
from flask import Blueprint, request
from flask.json import jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required
from app.models import Question, db, User
import datetime
from sqlalchemy import func
from app.helper import admin_required

questions = Blueprint("questions", __name__, url_prefix="/api/v1/questions")


@questions.route("/", methods=["POST", "GET"])
@jwt_required()
def handle_questions():
    def process_single_question(question_data, current_user):
        sentence = question_data.get("sentence", "")
        language = question_data.get("language", "")

        if language not in ["English", "Luganda"]:
            return (
                jsonify({"error": "Invalid language selection"}),
                HTTP_400_BAD_REQUEST,
            )

        if not sentence or not language:
            return (
                jsonify({"error": "Both sentence and language must be provided for each question"}),
                HTTP_400_BAD_REQUEST,
            )
        # elif len(sentence) < 12:
        #     return {
        #         "error": "Enter a valid sentence for each question"
        #     }, HTTP_400_BAD_REQUEST
        elif Question.query.filter_by(sentence=sentence).first():
            return (
                jsonify({"error": "Sentence already exists for one of the questions"}),
                HTTP_409_CONFLICT,
            )
        else:
            question = Question(
                sentence=sentence, language=language, user_id=current_user
            )
            db.session.add(question)
            db.session.flush()

            num_questions = Question.query.filter_by(user_id=current_user).count()

            return {
                "num_questions": num_questions,
            }, HTTP_201_CREATED

    current_user = get_jwt_identity()

    if request.method == "POST":
        data = request.get_json()

        if not data:
            return (
                jsonify({"error": "Invalid or empty JSON data provided"}),
                HTTP_400_BAD_REQUEST,
            )

        if isinstance(data, list):  # If it's a JSON file with multiple questions
            results = []
            for question_data in data:
                result = process_single_question(question_data, current_user)
                results.append(result)
            db.session.commit()
            return jsonify(results), HTTP_201_CREATED
        else:  # If it's a single question
            result = process_single_question(data, current_user)
            db.session.commit()
            return result

    else:
        questions = Question.query.filter_by(user_id=current_user).all()

        returned_data = []

        if not questions:
            return jsonify({"error": "No data yet"}), HTTP_204_NO_CONTENT

        for question in questions:
            returned_data.append(
                {
                    "id": question.id,
                    "sentnce": question.sentence,
                    "language": question.language,
                    "created_at": question.created_at,
                }
            )

        return jsonify({"data": returned_data}), HTTP_200_OK


@questions.route("/file_upload/", methods=["POST"])
@jwt_required()
def upload_json_file():
    if request.method == "POST":
        file_json = request.files.get('file')
        json_data = json.load(file_json)

        current_user = get_jwt_identity()
        dup_count = 0

        for obj in json_data:
            sentence = obj['sentence']
            language = obj['language']

            if Question.query.filter_by(sentence=sentence).first():
                dup_count += 1
            else:
                question = Question(
                    sentence=sentence, language=language, user_id=current_user
                )
                db.session.add(question)
                db.session.commit()

        num_questions = Question.query.filter_by(user_id=current_user).count()

        return (
            jsonify(
                {
                    "duplicate_questions": dup_count,
                    "num_questions": num_questions
                }
            ),
            HTTP_200_OK,
        )


@questions.get("/<int:id>")
@jwt_required()
def get_question(id):
    current_user = get_jwt_identity()

    question = Question.query.filter_by(user_id=current_user, id=id).first()

    if not question:
        return jsonify({"message": "Question not found"}), HTTP_404_NOT_FOUND

    return (
        jsonify(
            {
                "id": question.id,
                "language": question.language,
                "sentence": question.sentence,
                "created_at": question.created_at,
            }
        ),
        HTTP_200_OK,
    )


@jwt_required()
@questions.get("/top_users")
def top_users_with_most_questions():
    # Fetch data from the database to get the top five users with the most questions
    users_with_most_questions = (
        User.query.join(Question, User.id == Question.user_id)
        .group_by(User.id)
        .order_by(db.func.count(Question.id).desc())
        .limit(5)
        .all()
    )

    # Prepare the response data with user information
    top_users_data = []
    for user in users_with_most_questions:
        top_users_data.append(
            {
                "user_id": user.id,
                "username": user.username,
                "phone_number": user.phone_number,
                "total_questions": len(user.questions),
            }
        )

    return jsonify(top_users_data), HTTP_200_OK

@jwt_required()
@questions.get("/stats")
@admin_required
def list_questions():
    #     query_result = session.query(Question).filter(Question.user_id == user_id, Question.id == question_id).limit(1).all()

    all_questions = Question.query.all()
    #     all_questions = db.sessionQuestion).all()
    print(all_questions)
    total_questions = len(all_questions)
    questions_per_language = db.session.query(Question.language, func.count(Question.id)).group_by(Question.language).all()

    #     # # Calculate average daily questions
    # average_daily_questions = total_questions / (Question.query.filter(Question.created_at >= datetime.date.today()).count() or 1)
    average_daily_questions = total_questions / (Question.query.filter(Question.created_at >= datetime.date.today()).count() or 1)


    #     # # Calculate average weekly questions
    one_week_ago = datetime.date.today() - datetime.timedelta(weeks=1)
    average_weekly_questions = total_questions / (Question.query.filter(Question.created_at >= one_week_ago).count() or 1)

    #     # # Calculate average questions per user
    total_users = User.query.count()
    average_questions_per_user = total_questions / (total_users or 1)

    #     # Prepare the response data
    response_data = {
        'total_questions': total_questions,
        'questions_per_language': [{'language': lang, 'count': count} for lang, count in questions_per_language],
        'average_daily_questions': average_daily_questions,
        'average_weekly_questions': average_weekly_questions,
        'average_questions_per_user': average_questions_per_user,
        'questions': [{'id': question.id, 'answer': question.answer, 'sentence': question.sentence, 'language': question.language,
                               'created_at': question.created_at} for question in all_questions]
    }

    return jsonify(response_data), HTTP_200_OK
