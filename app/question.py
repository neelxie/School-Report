import json

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
from app.models import Question, db, User, Answer
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
        topic = question_data.get("topics", "")
        category = question_data.get("category", "")
        animal_crop = question_data.get("crop_animal", "")
        location = question_data.get("location", "")
        today = datetime.date.today()

        if language not in ["English", "Luganda"]:
            return (
                jsonify({"error": "Invalid language selection"}),
                HTTP_400_BAD_REQUEST,
            )

        if not sentence or not language:
            return (
                jsonify(
                    {
                        "error": "Both sentence and language must be provided for each question"
                    }
                ),
                HTTP_400_BAD_REQUEST,
            )

        elif Question.query.filter_by(sentence=sentence).first():
            return (
                jsonify({"error": "This question already exists"}),
                HTTP_409_CONFLICT,
            )
        else:
            question = Question(
                sentence=sentence,
                language=language,
                user_id=current_user,
                topic=topic,
                category=category,
                animal_crop=animal_crop,
                location=location,
            )
            db.session.add(question)
            db.session.flush()

            num_questions = Question.query.filter_by(user_id=current_user).count()
            today = datetime.date.today()
            questions = (
                Question.query.filter_by(user_id=current_user)
                .filter(func.date(Question.created_at) == today)
                .all()
            )
            todaysQuestions = []
            for question in questions:
                todaysQuestions.append(
                    {
                        "id": question.id,
                        "sentence": question.sentence,
                        "language": question.language,
                        "created_at": question.created_at,
                        "topics": question.topic,
                        "category": question.category,
                        "animal_crop": question.animal_crop,
                        "location": question.location,
                    }
                )

            return {
                "num_questions": num_questions,
                "questions": todaysQuestions,
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
        user = User.query.filter_by(id=current_user).first()
        if user:
            questions = user.questions

            returned_data = []

            if not questions:
                return jsonify({"error": "No data yet"}), HTTP_204_NO_CONTENT

            for question in questions:
                returned_data.append(
                    {
                        "id": question.id,
                        "sentence": question.sentence,
                        "language": question.language,
                        "created_at": question.created_at,
                        "topics": question.topic,
                        "category": question.category,
                        "animal_crop": question.animal_crop,
                        "location": question.location,
                    }
                )

            return jsonify(returned_data), HTTP_200_OK
        else:
            return jsonify({"error": "User not found"}), HTTP_404_NOT_FOUND


@questions.route("/file_upload/", methods=["POST"])
@jwt_required()
def upload_json_file():
    if request.method == "POST":
        file_json = request.files.get("file")
        json_data = json.load(file_json)

        current_user = get_jwt_identity()
        dup_count = 0
        duplicates = []

        for obj in json_data:
            sentence = obj["sentence"]
            language = obj["language"]
            topic = obj.get("topics")
            category = obj.get("category")
            animal_crop = obj.get("crop_animal")
            location = obj.get("location")

            if Question.query.filter_by(sentence=sentence).first():
                dup_count += 1
                duplicates.append({"sentence": sentence})
            else:
                question = Question(
                    sentence=sentence,
                    language=language,
                    user_id=current_user,
                    topic=topic,
                    category=category,
                    animal_crop=animal_crop,
                    location=location,
                )
                db.session.add(question)
                db.session.commit()

        num_questions = Question.query.filter_by(user_id=current_user).count()

        return (
            jsonify(
                {
                    "num_questions": num_questions,
                    "duplicate_questions": dup_count,
                    "duplicates": duplicates,
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
                "category": question.category,
                "animal_crop": question.animal_crop,
                "location": question.location,
            }
        ),
        HTTP_200_OK,
    )


@jwt_required()
@questions.get("/all")
def get_questions():
    questions = Question.query.all()

    if not questions:
        return jsonify({"message": "No questions yet."}), HTTP_204_NO_CONTENT

    returned_data = []

    for question in questions:
        returned_data.append(
            {
                "id": question.id,
                "sentence": question.sentence,
                "language": question.language,
                "created_at": question.created_at.strftime("%Y-%m-%d %H:%M:%S"),
                "topics": question.topic,
                "category": question.category,
                "animal_crop": question.animal_crop,
                "location": question.location,
            }
        )

    return jsonify(returned_data), HTTP_200_OK


@jwt_required()
@questions.get("/top_users")
def top_users_with_most_questions():
    users_with_most_questions = (
        User.query.join(Question, User.id == Question.user_id)
        .group_by(User.id)
        .order_by(db.func.count(Question.id).desc())
        .all()
    )
    top_users_data = []
    for user in users_with_most_questions:
        top_users_data.append(
            {
                "user_id": user.id,
                "location": user.location,
                "firstname": user.firstname,
                "lastname": user.lastname,
                "username": user.username,
                "phone_number": user.phone_number,
                "total_questions": len(user.questions),
            }
        )

    return jsonify(top_users_data), HTTP_200_OK


@jwt_required()
@questions.get("/stats")
# @admin_required
def list_questions():
    #     query_result = session.query(Question).filter(Question.user_id == user_id, Question.id == question_id).limit(1).all()

    all_questions = Question.query.all()
    #     all_questions = db.sessionQuestion).all()
    total_questions = len(all_questions)
    questions_per_language = (
        db.session.query(Question.language, func.count(Question.id))
        .group_by(Question.language)
        .all()
    )

    #     # # Calculate average daily questions
    # average_daily_questions = total_questions / (Question.query.filter(Question.created_at >= datetime.date.today()).count() or 1)
    average_daily_questions = total_questions / (
        Question.query.filter(Question.created_at >= datetime.date.today()).count() or 1
    )

    #     # # Calculate average weekly questions
    one_week_ago = datetime.date.today() - datetime.timedelta(weeks=1)
    average_weekly_questions = total_questions / (
        Question.query.filter(Question.created_at >= one_week_ago).count() or 1
    )

    #     # # Calculate average questions per user
    total_users = User.query.count()
    average_questions_per_user = total_questions / (total_users or 1)

    #     # Prepare the response data
    response_data = {
        "total_questions": total_questions,
        "questions_per_language": [
            {"language": lang, "count": count} for lang, count in questions_per_language
        ],
        "average_daily_questions": round(average_daily_questions, 2),
        "average_weekly_questions": round(average_weekly_questions, 2),
        "average_questions_per_user": round(average_questions_per_user, 2),
        "questions": [
            {
                "id": question.id,
                "topics": question.topic,
                "sentence": question.sentence,
                "language": question.language,
                "created_at": question.created_at,
                "category": question.category,
                "animal_crop": question.animal_crop,
                "location": question.location,
            }
            for question in all_questions
        ],
    }

    return jsonify(response_data), HTTP_200_OK


@questions.route("/random_question", methods=["GET"])
@jwt_required()
def random_question_and_add_answer():
    user_id = get_jwt_identity()
    random_question = (
        Question.query.filter(~Question.answers.any(Answer.source == "expert"))
        .order_by(db.func.random())
        .first()
    )

    if random_question:
        question_data = {
            "id": random_question.id,
            "sentence": random_question.sentence,
            "language": random_question.language,
            "created_at": random_question.created_at.strftime("%Y-%m-%d %H:%M:%S"),
            "topics": random_question.topic,
            "category": random_question.category,
            "animal_crop": random_question.animal_crop,
            "location": random_question.location,
        }
        return jsonify(question_data), HTTP_200_OK
    else:
        return jsonify({"message": "No questions available."}), HTTP_404_NOT_FOUND


@questions.route("/random_question_review", methods=["GET"])
@jwt_required()
def random_question_for_review():
    random_unreviewed_question = (
        Question.query.filter_by(reviewed=False).order_by(func.random()).first()
    )

    if random_unreviewed_question:
        question_data = {
            "id": random_unreviewed_question.id,
            "sentence": random_unreviewed_question.sentence,
            "language": random_unreviewed_question.language,
            "created_at": random_unreviewed_question.created_at.strftime(
                "%Y-%m-%d %H:%M:%S"
            ),
            "topics": random_unreviewed_question.topic,
            "category": random_unreviewed_question.category,
            "animal_crop": random_unreviewed_question.animal_crop,
            "location": random_unreviewed_question.location,
        }
        return jsonify(question_data), HTTP_200_OK
    else:
        return jsonify({"message": "No questions available."}), HTTP_404_NOT_FOUND


@questions.route("/random_question_answer", methods=["GET"])
@jwt_required()
def random_question_for_answer():
    random_unreviewed_question = (
        Question.query.filter_by(reviewed=True, correct=True)
        .order_by(func.random())
        .first()
    )

    if random_unreviewed_question:
        question_data = {
            "id": random_unreviewed_question.id,
            "sentence": random_unreviewed_question.rephrased
            if random_unreviewed_question.rephrased
            else random_unreviewed_question.sentence,
            "language": random_unreviewed_question.language,
            "created_at": random_unreviewed_question.created_at.strftime(
                "%Y-%m-%d %H:%M:%S"
            ),
            "topic": random_unreviewed_question.topic,
            "category": random_unreviewed_question.category,
            "animal_crop": random_unreviewed_question.animal_crop,
            "location": random_unreviewed_question.location,
        }
        return jsonify(question_data), HTTP_200_OK
    else:
        return jsonify({"message": "No questions available."}), HTTP_404_NOT_FOUND


@questions.post("/add_answer/<int:question_id>")
@jwt_required()
def add_answer(question_id):
    data = request.get_json()
    user_id = get_jwt_identity()
    answer_text = request.json["answer"].strip()
    # source = request.json["source"].strip()

    question = Question.query.get(question_id)
    if not question:
        return jsonify({"message": "Question not found."}), HTTP_404_NOT_FOUND

    if answer_text and len(answer_text) > 7:
        new_answer = Answer(
            question_id=question_id,
            user_id=user_id,
            answer_text=answer_text,
            source="expert",
        )

        db.session.add(new_answer)
        db.session.commit()

        return jsonify({"message": "Answer added successfully."}), HTTP_201_CREATED
    return jsonify({"message": "Failed to add answer."})


@questions.route("/incorrect/<int:question_id>", methods=["PUT"])
@jwt_required()
def mark_question_as_reviewed(question_id):
    user_id = get_jwt_identity()
    question = Question.query.get(question_id)

    if question:
        question.reviewed = True
        question.correct = False
        question.reviewer_id = user_id

        db.session.commit()

        return jsonify({"message": "Question attributes updated"})
    else:
        return jsonify({"message": "Question not found"})


@questions.route("/question_review/<int:question_id>", methods=["PUT"])
@jwt_required()
def question_review(question_id):
    user_id = get_jwt_identity()
    question = Question.query.get(question_id)

    if question:
        question.reviewed = True
        question.correct = True  # Mark the question as correct
        question.reviewer_id = user_id

        rephrased_data = request.json.get(
            "rephrased"
        )  # Assuming rephrased data is sent in the request JSON
        if rephrased_data:
            question.rephrased = rephrased_data

        new_topic = request.json.get(
            "topic"
        )  # Assuming new topic data is sent in the request JSON
        if question.topic:
            if new_topic:
                new_topic += (
                    ", " + question.topic
                )  # Append new topic to the current topic
        else:
            question.topic = new_topic  # Set new topic if no current topic exists

        db.session.commit()

        return jsonify({"message": "Question attributes updated"})
    else:
        return jsonify({"message": "Question not found"})


@questions.route("/random_unanswered_question", methods=["GET"])
@jwt_required()
def get_random_unanswered_question(user_id):
    user_id = get_jwt_identity()

    # Get a random unanswered question for the user
    random_question = (
        Question.query.outerjoin(
            Answer, (Answer.question_id == Question.id) & (Answer.user_id == user_id)
        )
        .filter(Answer.id == None)
        .order_by(func.random())
        .first()
    )

    if random_question:
        question_data = {
            "id": random_question.id,
            "sentence": random_question.sentence,
            "language": random_question.language,
            "category": random_question.category,
            "animal_crop": random_question.animal_crop,
            "location": random_question.location,
            # answer part
        }
        return jsonify(question_data), 200
    else:
        return jsonify({"message": "No unanswered questions available"}), 404


@questions.route("/luganda", methods=["GET"])
@jwt_required()
def get_luganda_questions():
    luganda_questions = Question.query.filter(
        func.lower(Question.language) == "luganda"
    ).all()

    if luganda_questions:
        questions_data = []
        for question in luganda_questions:
            question_data = {
                "id": question.id,
                "sentence": question.sentence,
                "language": question.language,
                "created_at": question.created_at.strftime("%Y-%m-%d %H:%M:%S"),
                "topics": question.topic,
                "category": question.category,
                "animal_crop": question.animal_crop,
                "location": question.location,
            }
            questions_data.append(question_data)

        return jsonify(questions_data), HTTP_200_OK
    else:
        return jsonify({"message": "No Luganda questions found"}), HTTP_404_NOT_FOUND


@questions.route("/english", methods=["GET"])
@jwt_required()
def get_english_questions():
    english_questions = Question.query.filter(
        func.lower(Question.language) == "english"
    ).all()

    if english_questions:
        questions_data = []
        for question in english_questions:
            question_data = {
                "id": question.id,
                "sentence": question.sentence,
                "language": question.language,
                "created_at": question.created_at.strftime("%Y-%m-%d %H:%M:%S"),
                "topics": question.topic,
                "category": question.category,
                "animal_crop": question.animal_crop,
                "location": question.location,
            }
            questions_data.append(question_data)

        return jsonify(questions_data), HTTP_200_OK
    else:
        return jsonify({"message": "No Luganda questions found"}), HTTP_404_NOT_FOUND

@questions.route("/add_question_location", methods=["PUT"])
@jwt_required()
def update_question_locations():
    
    try:
        users = User.query.filter(func.lower(User.role) == "farmer").all()

        for user in users:
            user_questions = Question.query.filter_by(user_id=user.id).all()

            user_location = user.location

            for question in user_questions:
                question.location = user_location

        db.session.commit()

        return jsonify({'message': 'Question locations updated successfully'}), HTTP_200_OK

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'An error occurred while updating question locations'})
