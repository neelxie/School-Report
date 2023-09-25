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
import pandas as pd
from flask_jwt_extended import get_jwt_identity, jwt_required
from app.models import Question, db, User, Answer
import datetime
from sqlalchemy import func
from app.helper import admin_required

questions = Blueprint("questions", __name__, url_prefix="/api/v1/questions")


def format_question(question, language):
    return {
        "id": question.id,
        "sentence": question.sentence,
        "language": question.language,
        "created_at": question.created_at.strftime("%Y-%m-%d %H:%M:%S"),
        "topics": question.topic,
        "category": question.category,
        "animal_crop": question.animal_crop,
        "location": question.location,
        "question_language": language,
    }


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
        user = User.query.get(question.user_id)  # Get the user who asked the question
        if user:
            user_name = f"{user.firstname} {user.lastname}"

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
                "user_name": user_name,
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

    #  Calculate average questions per user
    total_users = User.query.count()
    average_questions_per_user = total_questions / (total_users or 1)

    plant_question_count = Question.query.filter(
        func.lower(Question.category) == "crop"
    ).count()

    animal_question_count = Question.query.filter(
        func.lower(Question.category) == "animal"
    ).count()

    # Prepare the response data
    response_data = {
        "total_questions": total_questions,
        "questions_per_language": [
            {"language": lang, "count": count} for lang, count in questions_per_language
        ],
        "average_daily_questions": round(average_daily_questions, 2),
        "average_weekly_questions": round(average_weekly_questions, 2),
        "average_questions_per_user": round(average_questions_per_user, 2),
        "plant_category": plant_question_count,
        "animal_category": animal_question_count,
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
    english_filter = func.lower(Question.language) == "english"
    luganda_filter = func.lower(Question.language) == "luganda"
    runyankole_filter = func.lower(Question.language) == "runyankole"
    unreviewed_filter = Question.reviewed == False
    cleaned_filter = Question.cleaned == True

    english_random_unreviewed_question = (
        Question.query.filter(english_filter, unreviewed_filter, cleaned_filter)
        .order_by(func.random())
        .first()
    )

    luganda_random_unreviewed_question = (
        Question.query.filter(luganda_filter, unreviewed_filter, cleaned_filter)
        .order_by(func.random())
        .first()
    )

    runyankole_random_unreviewed_question = (
        Question.query.filter(runyankole_filter, unreviewed_filter, cleaned_filter)
        .order_by(func.random())
        .first()
    )

    random_unreviewed_question = (
        Question.query.filter(unreviewed_filter, cleaned_filter)
        .order_by(func.random())
        .first()
    )

    questions_data = []

    if english_random_unreviewed_question:
        questions_data.append(
            format_question(english_random_unreviewed_question, "English")
        )
    else:
        questions_data.append(
            {
                "question_language": "English",
                "sentence": "There are no more questions to evaluate, go to the answer/rank questions sections",
            }
        )

    if luganda_random_unreviewed_question is not None:
        questions_data.append(
            format_question(luganda_random_unreviewed_question, "Luganda")
        )
    else:
        questions_data.append(
            {
                "question_language": "Luganda",
                "sentence": "There are no more luganda questions, Please evaluate English questions",
            }
        )

    if runyankole_random_unreviewed_question is not None:
        questions_data.append(
            format_question(runyankole_random_unreviewed_question, "Runyankole")
        )
    else:
        questions_data.append(
            {
                "question_language": "Runyakole",
                "sentence": "There are no more Runyankole questions, Please evaluate English questions",
            }
        )

    if random_unreviewed_question:
        questions_data.append(
            format_question(random_unreviewed_question, "Any Language")
        )

    if questions_data:
        return jsonify(questions_data), HTTP_200_OK
    else:
        return jsonify({"message": "No questions available."}), HTTP_404_NOT_FOUND


@questions.route("/random_question_answer", methods=["GET"])
@jwt_required()
def random_question_for_answer():
    english_filter = func.lower(Question.language) == "english"
    luganda_filter = func.lower(Question.language) == "luganda"
    runyankole_filter = func.lower(Question.language) == "runyankole"
    reviewed_filter = Question.reviewed == True
    cleaned_filter = Question.cleaned == True

    english_random_unreviewed_question = (
        Question.query.filter(english_filter, reviewed_filter, cleaned_filter)
        .order_by(func.random())
        .first()
    )

    luganda_random_unreviewed_question = (
        Question.query.filter(luganda_filter, reviewed_filter, cleaned_filter)
        .order_by(func.random())
        .first()
    )

    runyankole_random_unreviewed_question = (
        Question.query.filter(runyankole_filter, reviewed_filter, cleaned_filter)
        .order_by(func.random())
        .first()
    )

    random_unreviewed_question = (
        Question.query.filter(reviewed_filter, cleaned_filter)
        .order_by(func.random())
        .first()
    )

    questions_data = []

    if english_random_unreviewed_question:
        questions_data.append(
            format_question(english_random_unreviewed_question, "English")
        )
    else:
        questions_data.append(
            {
                "question_language": "English",
                "sentence": "There are no more questions to evaluate, go to the answer/rank questions sections",
            }
        )

    if luganda_random_unreviewed_question is not None:
        questions_data.append(
            format_question(luganda_random_unreviewed_question, "Luganda")
        )
    else:
        questions_data.append(
            {
                "question_language": "Luganda",
                "sentence": "There are no more luganda questions, Please evaluate English questions",
            }
        )

    if runyankole_random_unreviewed_question is not None:
        questions_data.append(
            format_question(runyankole_random_unreviewed_question, "Runyankole")
        )
    else:
        questions_data.append(
            {
                "question_language": "Runyakole",
                "sentence": "There are no more Runyankole questions, Please evaluate English questions",
            }
        )

    if random_unreviewed_question:
        questions_data.append(
            format_question(random_unreviewed_question, "Any Language")
        )

    if questions_data:
        return jsonify(questions_data), HTTP_200_OK
    else:
        return jsonify({"message": "No questions available."}), HTTP_404_NOT_FOUND


# @questions.route("/", methods=["GET"])
# @jwt_required()
# def random_question_for_answer():
#     random_unreviewed_question = (
#         Question.query.filter_by(reviewed=True, correct=True)
#         .order_by(func.random())
#         .first()
#     )

#     if random_unreviewed_question:
#         question_data = {
#             "id": random_unreviewed_question.id,
#             "sentence": random_unreviewed_question.rephrased
#             if random_unreviewed_question.rephrased
#             else random_unreviewed_question.sentence,
#             "language": random_unreviewed_question.language,
#             "created_at": random_unreviewed_question.created_at.strftime(
#                 "%Y-%m-%d %H:%M:%S"
#             ),
#             "topic": random_unreviewed_question.topic,
#             "category": random_unreviewed_question.category,
#             "animal_crop": random_unreviewed_question.animal_crop,
#             "location": random_unreviewed_question.location,
#         }
#         return jsonify(question_data), HTTP_200_OK
#     else:
#         return jsonify({"message": "No questions available."}), HTTP_404_NOT_FOUND


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
        question.answered = True
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


# DO NOT USE
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

        return (
            jsonify({"message": "Question locations updated successfully"}),
            HTTP_200_OK,
        )

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "An error occurred while updating question locations"})


@questions.route("/dataset_upload/", methods=["POST"])
@jwt_required()
def upload_excel_file():
    if request.method == "POST":
        file_excel = request.files.get("file")

        if file_excel and file_excel.filename.endswith(".xlsx"):
            try:
                # Read the Excel file using pandas
                df = pd.read_excel(file_excel)

                current_user = get_jwt_identity()
                dup_count = 0
                duplicates = []

                for _, row in df.iterrows():
                    sentence = row.get("sentence")
                    language = row.get("language")
                    topic = row.get("topics", None)
                    category = row.get("category", None)
                    animal_crop = row.get("crop_animal", None)
                    location = row.get("location", None)

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
            except Exception as e:
                return jsonify({"message": str(e)}), HTTP_400_BAD_REQUEST
        else:
            return (
                jsonify(
                    {"message": "Invalid file format. Please upload a .xlsx file."}
                ),
                HTTP_400_BAD_REQUEST,
            )


@questions.route("/answered_question_ranking", methods=["GET"])
@jwt_required()
def answered_question_ranking():
    user_id = get_jwt_identity()
    cleaned_filter = Question.cleaned == True
    answered_filter = Question.answered == True
    unFinished_filter = Question.finished == False
    question_and_answer_data = []

    languages = ["english", "luganda", "runyankole"]

    for language in languages:
        language_filter = func.lower(Question.language) == language

        random_unreviewed_question = (
            Question.query.filter(
                language_filter,
                answered_filter,
                cleaned_filter,
                unFinished_filter,
                (~Question.answers.any(Answer.user_id == user_id)),
            )
            .order_by(func.random())
            .first()
        )

        if random_unreviewed_question:
            question_data = {
                "id": random_unreviewed_question.id,
                "sentence": random_unreviewed_question.rephrased
                or random_unreviewed_question.sentence,
                "language": random_unreviewed_question.language,
                "created_at": random_unreviewed_question.created_at.strftime(
                    "%Y-%m-%d %H:%M:%S"
                ),
                "topic": random_unreviewed_question.topic,
                "category": random_unreviewed_question.category,
                "animal_crop": random_unreviewed_question.animal_crop,
                "location": random_unreviewed_question.location,
            }

            # Create a list to store answer data for each associated answer
            answer_list = []
            for answer in random_unreviewed_question.answers:
                answer_data = {
                    "id": answer.id,
                    "answer_text": answer.answer_text,
                    "source": answer.source,
                    "relevance": answer.relevance,
                    "coherence": answer.coherence,
                    "fluency": answer.fluency,
                    "rank": answer.rank,
                    "created_at": answer.created_at.strftime("%Y-%m-%d %H:%M:%S"),
                }
                answer_list.append(answer_data)

            question_and_answer_data.append(
                {"question": question_data, "answers": answer_list}
            )

    # Include the random_question without language filter
    random_question_data = None
    random_question = (
        Question.query.filter(
            cleaned_filter,
            answered_filter,
            unFinished_filter,
            (~Question.answers.any(Answer.user_id == user_id)),
        )
        .order_by(func.random())
        .first()
    )

    if random_question:
        random_question_data = {
            "id": random_question.id,
            "sentence": random_question.rephrased or random_question.sentence,
            "language": random_question.language,
            "created_at": random_question.created_at.strftime("%Y-%m-%d %H:%M:%S"),
            "topic": random_question.topic,
            "category": random_question.category,
            "animal_crop": random_question.animal_crop,
            "location": random_question.location,
        }

        # Create a list to store answer data for each associated answer
        answer_list = []
        for answer in random_question.answers:
            answer_data = {
                "id": answer.id,
                "answer_text": answer.answer_text,
                "source": answer.source,
                "relevance": answer.relevance,
                "coherence": answer.coherence,
                "fluency": answer.fluency,
                "rank": answer.rank,
                "created_at": answer.created_at.strftime("%Y-%m-%d %H:%M:%S"),
            }
            answer_list.append(answer_data)

        random_question_data["answers"] = answer_list

    if question_and_answer_data or random_question_data:
        result_object = {
            "question_and_answer_data": question_and_answer_data,
            "random_question_data": random_question_data,
        }
        return jsonify(result_object), HTTP_200_OK
    else:
        return (
            jsonify({"message": "No questions available with answers."}),
            HTTP_404_NOT_FOUND,
        )


@questions.route("/store_answer_ranks", methods=["POST"])
@jwt_required()
def store_answer_ranks():
    data = request.json
    question_id = data.get("questionId")
    rankings = data.get("rankings")

    if question_id is None or rankings is None:
        return jsonify({"message": "Invalid data format"}), HTTP_400_BAD_REQUEST

    try:
        for ranking in rankings:
            answer_id = ranking.get("answer_id")
            relevance = ranking.get("relevance")
            coherence = ranking.get("coherence")
            fluency = ranking.get("fluency")

            # Calculate the answer rank as the summation of relevance, coherence, and fluency
            answer_rank = relevance + coherence + fluency

            answer = Answer.query.get(answer_id)
            if answer:
                answer.relevance = relevance
                answer.coherence = coherence
                answer.fluency = fluency
                answer.rank = answer_rank

        # Update the question field to "finished"
        question = Question.query.get(question_id)
        if question:
            question.finished = True

        db.session.commit()
        return jsonify({"message": "Answer ranks stored successfully"}), HTTP_200_OK

    except Exception as e:
        db.session.rollback()
        return jsonify({"message": "Error storing answer ranks"}), HTTP_400_BAD_REQUEST


@questions.route("/upload_json_answers/", methods=["GET"])
@jwt_required()
def upload_json_answers():
    json_data = [
        {
            "animal_crop": "Ducks",
            "category": "Animal",
            "language": "Luganda",
            "location": "KAYUNGA",
            "questions": "Mitendera ki jempitamu nga nunda embaata",
            "bing response": "I’m sorry but I don’t understand your message. I will disengage from this conversation.",
            "bard response": "I'm still learning languages, so at the moment I can't help you with this request. So far I've only been trained to understand the languages listed in the Bard Help Center.",
            "llama -2 response": "Sure, I'd be happy to help! However, I notice that the text you provided is not in English or any recognizable language. Could you please rephrase your question or request in a language that I can understand?",
            "chatgpt 3.5 response": "Kunditsiridza Jempitamu: Ndinokunyudzai kuti nunda idzi yakanaka iri mukati seni! Nounda inokupai nyenyezi dzinobvisa chirimudzudzu mudhumeni. Masimba anyama kuti mamwe macomplete mudhumeni. Utevedza musimboti yaneta m. Ndiyokunyudzai kuti nunda iyi inee yakasimba. Musimbotsiridza kuti mazuva muno woda kuonera yakapfava. Rega nuyanzevamo. Ufhudze nunda yakanaka dzeshumba. Utsirize kuwonere maotoko anamwari pano muna nzvimbo yake kutenda musimboti. Utsirire phonographs nezvishoma chokwadi anamwari uye muchi ropaonere. Utsirize kuwona mweya wemasimba kuti kuporesera. Nokutendai mazuva mashoma iyo Uri mupe chiurai uye us",
            "chatgpt 4 response": "",
            "topics": "Veterinary care",
        },
        {
            "animal_crop": "Cattle",
            "category": "Animal",
            "language": "Luganda",
            "location": "KAYUNGA",
            "questions": "Kirungi okugema ente (local breed) ngenetera okuzaala?",
            "bing response": "I’m sorry but I don’t understand your message. I will disengage from this conversation.",
            "bard response": "I'm still learning languages, so at the moment I can't help you with this request. So far I've only been trained to understand the languages listed in the Bard Help Center.",
            "llama -2 response": "Oho, oho! Kirungi olugoma enkubuluma ente ngengera okuzala! (Oh my goodness, the local breed of goat is giving birth to a kid!)",
            "chatgpt 3.5 response": "Ebi ewa:\n1. Bwezeye ngutega okuwa amapapali. Entsiga yo bewa amapapali emitima gya ente gilaga nga nguto. \n2. Tegedde okuwa ensimbi ez’ebikulikiti mu bujo bwezituliza ente balimu oburwanabutapapali. Endikkiro erirala ebisinga obukulu ku bitu omwami agi na enjaga ebikolera obusembuzi. Enjaga zitegeeza bujo ebiziri mu bitu ebituulisaamu ente emirala ebinkwate ngakulakwata obukalima.\n3. Eka nga uitamu obulungi obuthakwa kuli ensimbi ezizitegeredde n’abazukulu ebisirika n’ombaliga eb’ente. Bweziterekedde ebyoganiikwa mu kasi ya balwaki ezittaaga okukola obulungi ebibaliza ente.\n4. Tegedde okuvutuka ensimbi ete",
            "chatgpt 4 response": "",
            "topics": "Vaccination",
        },
        {
            "animal_crop": "Cattle",
            "category": "Animal",
            "language": "Luganda",
            "location": "KAYUNGA",
            "questions": "Ddagala ki lyenyinza okuwa /    okufuya ente yange nga erina enkwa ne kawawa.",
            "bing response": "I’m sorry but I don’t understand your message. I will disengage from this conversation.",
            "bard response": "I'm still learning languages, so at the moment I can't help you with this request. So far I've only been trained to understand the languages listed in the Bard Help Center.",
            "llama -2 response": "I apologize, but I'm a large language model, I cannot understand the text you provided as it appears to be written in a distorted or coded format. Could you please rephrase your message using standard grammar and vocabulary so that I can assist you better?",
            "chatgpt 3.5 response": "I am teaching you how to care for my animals with love and compassion.",
            "chatgpt 4 response": "",
            "topics": "Veterinary care",
        },
        {
            "animal_crop": "Cattle",
            "category": "Animal",
            "language": "Luganda",
            "location": "KAYUNGA",
            "questions": "Nzijanjaba ntya ekirwadde kya kalusu mu nte zange.",
            "bing response": "Nzijanjaba ntya ekirwadde kya kalusu mu nte zange",
            "bard response": "I'm still learning languages, so at the moment I can't help you with this request. So far I've only been trained to understand the languages listed in the Bard Help Center.",
            "llama -2 response": "I apologize, but I'm a large language model, I cannot understand the text you provided as it appears to be written in a fictional language or code. Can you please rephrase your question or request in English or another recognizable language? I'll do my best to assist you with any questions or problems you may have.",
            "chatgpt 3.5 response": "Nze ndi ekirwadde nnyo kubanga kalusu kyange kikukola wansi wamala. Kiki kyekiri munsi yange nze ndikyamu nkusanga okutambula nga nsula kalusu naye ndiwotobela wansi mwe nyonyi nange.\n\nNze ngenda okuddamu kalusu nga ndikuba ebikwasa munda okulaba nange ebikwasa ewa mizigo yange. Nzijanjaba nti nze ndi ekirwadde nnyo kubanga ebikwasa byange biri ku nte zange. Nga nze ndi ekirwadde, ndifuna okusonya ebikwasa byange naye ndiwakanya okuddamu kalusu.\n\nEnsobi zange zabira wansi ku nte zange naye nze ndiwulira kubanga ndi ovawo ekirwadde. Ndiwulira okusaba Katonda okusinga okutuumuula okufuna ekirwadde kya kalusu kyange okuli nyo. Ndiw",
            "chatgpt 4 response": "",
            "topics": "Veterinary care",
        },
        {
            "animal_crop": "Cattle",
            "category": "Animal",
            "language": "Luganda",
            "location": "KAYUNGA",
            "questions": "Mmere ki jenjinza okuliisa ente zange ne zimpa amata amalungi ate nga maanji.",
            "bing response": "Mmere ki jenjinza okuliisa ente zange ne zimpa amata amalungi ate nga maanji.",
            "bard response": "I'm still learning languages, so at the moment I can't help you with this request. So far I've only been trained to understand the languages listed in the Bard Help Center.",
            "llama -2 response": "The text you provided is written in a language that I'm not familiar with, and it appears to be a made-up or artificial language. It does not appear to be any real language spoken in the world. Can you please provide more context or information about this language? Additionally, it would be helpful if you could provide the correct spelling of the words in the text, as well as their meanings.",
            "chatgpt 3.5 response": "Mmere tewali osutha amaanyi nga tewali nadiisa ennyimba y’okujanja okukola naye ngamba nti mmere gyendi musoso wamu na musoso ngamba mulondoola amaanyi nti “Amajjanjaba era ajjanjabi, amatembe ne kumanyi okutegeera ng’afuka nga awulira mu maka ge asiima era nga akute’’. Ku lwazi lw’okuzimba mmere, simanyi era nga kkola era ndowoza mmere nti ekyo kye ndimi dala kubanga zonna ennyo tebeera ebimu ve, tebirikuusa bwabwe.Mmere tewali ngabirimu zimpe bya gundi era ennaku zange ngenze nze ne mpenza muzuuse. Wano olaba nti nkuwaliriza nga bazimba naye ebyaallah nze nsuze entteko ya bannaabwe era buli baakulembera naye bwe baayigiriza era gwe abasajja abaweza abaana eri n",
            "chatgpt 4 response": "",
            "topics": "Feeds/ Food",
        },
        {
            "animal_crop": "Cattle",
            "category": "Animal",
            "language": "Luganda",
            "location": "KAYUNGA",
            "questions": "kilwadde ki ekiruma ente nevaako obwoya bwonna kuddiba.",
            "bing response": "Kilwadde ki ekiruma ente nevaako obwoya bwonna kuddiba.",
            "bard response": "I'm still learning languages, so at the moment I can't help you with this request. So far I've only been trained to understand the languages listed in the Bard Help Center.",
            "llama -2 response": "I apologize, but I'm a large language model, I cannot understand the text you provided as it appears to be written in a fictional language or code. Can you please rephrase your question or request in English or another recognizable language? I'll do my best to assist you with any questions or problems you may have.",
            "chatgpt 3.5 response": "Ente kasebrono abilali obw'ekikolo kikimaza kati naffe abakadde nga basobola okugooberera mu ngeri zino. Oluvannyuma, yangu gyetta ki bwanfuga okuddukanya nga jam okugyokya okufuga empya okwonoona olwokubera era okulya ekya obukulu. Noolwekyo, abantu abali mu kikolo kya nowa okukola kibannange olwookola ne babonyaabonya nga naffayo omutima gwa okudako mu busaasa bumala omusaayi gwaabwe.",
            "chatgpt 4 response": "",
            "topics": "Diseases",
        },
        {
            "animal_crop": "Cattle",
            "category": "Animal",
            "language": "Luganda",
            "location": "KAYUNGA",
            "questions": "Nfuyira ddi era wa ente yange?",
            "bing response": "Nfuyira ddi era wa ente yange?",
            "bard response": "I'm still learning languages, so at the moment I can't help you with this request. So far I've only been trained to understand the languages listed in the Bard Help Center.",
            "llama -2 response": 'I apologize, but I\'m a large language model, I do not understand the meaning of "fuyira ddi era wa ente yange?" as it appears to be written in a combination of Japanese and English. Could you please rephrase your question or provide more context so I can better assist you?',
            "chatgpt 3.5 response": "Mbulira nange, era nsobole okutuuka mu bbiro bya Katonda, naye ente z'amaaso, era nga zisobola okwenyumirira Katonda.\",\n   \"Obyo kyonna okulira lwange, balokole, naye munsobole okujja kwange buli kisibo ky'akabonero n'okuvaako mu biebyo bikolimo.",
            "chatgpt 4 response": "",
            "topics": "Veterinary care",
        },
        {
            "animal_crop": "Rabbits",
            "category": "Animal",
            "language": "Luganda",
            "location": "KAYUNGA",
            "questions": "Kika ki okyobumyu kyenyinza okulunda nga kyakundetera sente mu bwangu?",
            "bing response": "Kika ki okyobumyu kyenyinza okulunda nga kyakundetera sente mu bwangu?",
            "bard response": "I'm still learning languages, so at the moment I can't help you with this request. So far I've only been trained to understand the languages listed in the Bard Help Center.",
            "llama -2 response": "As a responsible AI language model, I apologize, but I cannot engage in conversations that use derogatory language or perpetuate harmful stereotypes. All individuals deserve respect and dignity, regardless of their background or identity. It is important to approach others with kindness and understanding, rather than using hurtful language or making assumptions based on limited information. Let's focus on having a positive and inclusive conversation. Is there something specific you would like to talk about?",
            "chatgpt 3.5 response": "Naye ssebo/ssenga oba nze sente zino ziyinza kulunda mu bwangu kubanga nze ndi mukazi omu kuwumi, bwe ndi mubiri gyange era sente zino ziyinza kulunda n'ekyo kintu kyobanga eri omwana wange okuva ku mupande gwange ogwomukazi.\n\nMeaning: Can you explain why it is important to save money in the bank? As a husband/wife or as a woman, I believe it is important to save money in the bank for my own future and for my children's future from my side as a wife/mother.",
            "chatgpt 4 response": "",
            "topics": "Breeds",
        },
        {
            "animal_crop": "G-nuts",
            "category": "Crop",
            "language": "Luganda",
            "location": "KAYUNGA",
            "questions": "Kigimusa ki ekirungi kyenyinza okukozesa ku bijjanjalo.",
            "bing response": "Kigimusa is a traditional Ugandan dance that is performed during cultural ceremonies and celebrations. It is characterized by rhythmic movements, energetic footwork, and vibrant costumes. The dance is often accompanied by live drumming and singing, creating a lively and festive atmosphere. Kigimusa is a popular dance in Uganda, showcasing the country’s rich cultural heritage and traditions. It is enjoyed by both locals and visitors alike. Would you like to know more about Ugandan dances or any other topic?",
            "bard response": "I'm still learning languages, so at the moment I can't help you with this request. So far I've only been trained to understand the languages listed in the Bard Help Center.",
            "llama -2 response": 'I apologize, but I\'m a large language model, I cannot understand that phrase as it is not written in a language that I am trained on. The phrase "Kigimusa ki ekirungi kyenyinza okukozesa ku bijjanjalo" does not make sense to me. Could you please rephrase or provide more context so I can better understand and assist you?',
            "chatgpt 3.5 response": "Oba Bijjanjalo bikyali bigaanaokuyimirira okukozze ku hima ye. Mukyali nu mujonlya olwo akalulu kalya katukyalya ne maaridheya gwokyekukya bikawonya emaanyi egendhadha mu mazima ga Mukama wange akola.\n\nKuba bijjanjalo bikwongera okukozesa mweganda gwe omweso, wabba kwonka olwo olumbe lyo lwo abamu bawejesa ebyo olwo wenenya okutukwata kurayitamu. Kubatukya ebeero tenyinza okukozesa bulungi bikela, nokuba byebale melemerwe ebyekinna ya Mukama wange okukozza amanyi ago bumulemberera.\n\nBijjanjalo bikilirira nyo nyo bwenyene lyo tili bingi omukyala mu kubabaririra bwe omubila gwOmuga esala mukyala gwembajjo. Kye bwompeera ak",
            "chatgpt 4 response": "",
            "topics": "Fertilizers",
        },
        {
            "animal_crop": "Rabbits",
            "category": "Animal",
            "language": "Luganda",
            "location": "KAYUNGA",
            "questions": "Eddagala ettuufu lye nnina okukozesa okugema obumyu.",
            "bing response": "Eddagala ettuufu lye nnina okukozesa okugema obumyu.",
            "bard response": "I'm still learning languages, so at the moment I can't help you with this request. So far I've only been trained to understand the languages listed in the Bard Help Center.",
            "llama -2 response": "I apologize, but I'm a large language model, I cannot understand the text you provided as it appears to be written in a fictional language or code. Can you please rephrase your question or request in English or another recognizable language? I'll do my best to assist you with any questions or problems you may have.",
            "chatgpt 3.5 response": "Bino byonna busobole okufuna ebiroby'omcaka, okusobola okuwagala ababelukuku, okuddamu abantu abamu okusaaba nsi yo okujjuna okuva mu nzibwe zo ntamuwabulira. Naye nzibwe ezisinga omubaale nga ze zinnawo eddagala era eziva ebinyonyi nga teyabulilirwa.\n\nObumyu bw'eddagala bulina okuwera okunyonera ebintu eby'okubaali, embwamu n'ebirungi ku nju eziva mu nsi. Bw'eddagala bulina okusobola okuzza ebibi oba okutyo lw'obusaasa, okufuna nsi oba okubaachanaaza olubuto ebintu ebiva mu nsi. Obumyu bw'eddagala bulina okufuna amakulu oba okutya abantu ababulo burungi, okuyiga emirembe gy'abalala, n'okusalira eby'amataaniro by'eddagala nga te",
            "chatgpt 4 response": "",
            "topics": "Vaccination",
        },
        {
            "animal_crop": "G-nuts",
            "category": "Crop",
            "language": "English",
            "location": "KAYUNGA",
            "questions": "How can we decompose organic manure?",
            "bing response": "Composting animal manure is a common method. It involves piling, mixing, and moistening organic residues to undergo thermophilic decomposition. The process helps reduce pollution and benefits crops",
            "bard response": "Organic manure can be decomposed through composting. Composting is a natural process that breaks down organic matter into a nutrient-rich soil amendment. To compost manure, you will need a compost bin or pile, brown materials (such as straw, leaves, or wood chips), and green materials (such as grass clippings, food scraps, and manure). To start a compost pile, layer brown and green materials in the bin or pile. Be sure to moisten the materials, but avoid overwatering. The compost should be moist but not soggy. Turn the compost pile every few weeks to aerate the materials and help the decomposition process. The composting process can take several months, but the finished product is a nutrient-rich soil amendment that can be used to improve the health of your plants.",
            "llama -2 response": "To decompose organic manure, you can use a combination of microorganisms and heat. Add nitrogen-rich materials like blood meal or bone meal to the manure, and introduce beneficial microbes like composting bacteria or fungi. Maintain a temperature of around 130°F (54°C) to accelerate decomposition. Turn the mixture regularly to ensure even breakdown.",
            "chatgpt 3.5 response": "Organic manure can be decomposed through a natural process called composting. This involves layering organic materials such as food scraps, grass clippings, and leaves, and allowing them to decompose over time with the help of microorganisms. This process can be sped up by regularly turning the compost pile and keeping it moist. Another method is vermicomposting, where red worms are used to break down the organic materials into nutrient-rich fertilizer. Both methods are sustainable and environmentally friendly ways to decompose organic manure.",
            "chatgpt 4 response": "",
            "topics": "Fertilizers",
        },
        {
            "animal_crop": "Bees",
            "category": "Animal",
            "language": "Luganda",
            "location": "kyankwanzi district",
            "questions": "bwe nkola emisinga waliyo enjuki ze nnyinza okuteekamu oba nninda zino ezeereeta zokka",
            "bing response": "bwe nkola emisinga waliyo enjuki ze nnyinza okuteekamu oba nninda zino ezeereeta zokka",
            "bard response": "I'm still learning languages, so at the moment I can't help you with this request. So far I've only been trained to understand the languages listed in the Bard Help Center.",
            "llama -2 response": "I apologize, but I'm a large language model, I cannot understand the text you provided as it appears to be written in a fictional language or code. Can you please rephrase your question or request in English or another recognizable language? I'll do my best to assist you with any questions or problems you may have.",
            "chatgpt 3.5 response": "Ezitemiika ezi eziyinzisa abaana ba\n\nSsebo Egesa or Madam Ekesa, onywakede oyina enjuki mibiri enungi okubaadde mu ofiisi zammwe. Nenenyeza nga nnyinza ekitegeeza kubanga nze onkwata okuva mu kasasiro kyange nga ekisa. Nze nnuma ekifo ekimumatera oba nkwata kimu mubi nagambye ofiisi zange kulwanyisa ekisa. Nga nninda ganye ssente zange ne zigende okulya okw'omuli okwetibirirwa. Okuva ku ngegemu y'okunyumya oba okuyimya okuva mu kizanyiro eby'enjawulo, nze bweteka okuva kuwumu eddagala ne nzige n'ebicuucu okuva ku makanika y'okuleeta gwa yaleero. Eno zikibadde kubanga nze mmalirira buli muntu okuwa okukyala ob",
            "chatgpt 4 response": "",
            "topics": "Species",
        },
        {
            "animal_crop": "Bees",
            "category": "Animal",
            "language": "Luganda",
            "location": "kyankwanzi distr",
            "questions": "emmwanyi ezirimu emizinga gy'enjuki zaawukana zitya ku ezo ezitalimu mizinga gya njuki mu kuzitowa ng'okungudde?",
            "bing response": "emmwanyi ezirimu emizinga gy'enjuki zaawukana zitya ku ezo ezitalimu mizinga gya njuki mu kuzitowa ng'okungudde",
            "bard response": "I'm still learning languages, so at the moment I can't help you with this request. So far I've only been trained to understand the languages listed in the Bard Help Center.",
            "llama -2 response": "I apologize, but I'm a large language model, I cannot understand the text you provided as it appears to be written in a fictional language or code. Can you please rephrase your question or request in English or another recognizable language? I'll do my best to assist you with any questions or problems you may have.",
            "chatgpt 3.5 response": "Zino zidakulagenda, zimpya, zizikolamanyi, n'enzikiriza okuzitowa. Muno mu mizinga gy'enjuki zaawukana, bwe zifuna okuzitowa, zinatwala mabugo g'empale naddala, n'ebirala ebikozesebwa ebitali mu mwezi guno. \n\nEnjuki zizikolawo zino ne za mabugo abakakiikirira okuzitowa. Zino zirina mazzi oba ziiri mu bitundu ebirala biiwe kyokka byonna by'ezireemu, ng'ayogela okulwanyisa enjuki mu mizinga gyokka oba okwonoona n'okufuna obukozesebwa mu mizinga. Okusinga enjuki ntowooza, obulesaana ebibajuubu n'okubalagana ebizimbe by'omu kaakati, nga bwe ziritondeeyo ne zinazizizza amatendeka ag'okuzit",
            "chatgpt 4 response": "",
            "topics": "Harvesting",
        },
        {
            "animal_crop": "Bees",
            "category": "Animal",
            "language": "Luganda",
            "location": "kyankwanzi district",
            "questions": "enjuki ezirundibwa ze zimu nazino zetulaba nga zitambula oba tulinayo ebika ebirongoosemu?",
            "bing response": "enjuki ezirundibwa ze zimu nazino zetulaba nga zitambula oba tulinayo ebika ebirongoosemu",
            "bard response": "I'm still learning languages, so at the moment I can't help you with this request. So far I've only been trained to understand the languages listed in the Bard Help Center.",
            "llama -2 response": "I apologize, but I'm a large language model, I cannot understand the text you provided as it appears to be written in a fictional language or code. Can you please rephrase your question or request in English or another recognizable language? I'll do my best to assist you with any questions or problems you may have.",
            "chatgpt 3.5 response": "Ekintu kyonna, enjuki ezirundibwa ze zimu nazino zetulaba nga zitambula oba tulinayo ebika ebirongoosemu zinazina obutandikawo obukulemberemu. Ekibumbiro kino kyakozesa nnyo ku bintu ebya kafuumu, okuba ezimwe nga ezinakulembala mu biwumbi, okuwaanya mu bikwatta obutandikawo, okuba ezimwe nga ezitandikawo obutandikawo obwo butaba by'obulungi, okumanyiisa amateeka ng'akabi, okulya, okuzanya obutandikawo obwe ne malo wamu n'ebijanjaalo bya mu balwadde ebweru bwebadde mu bbobmu. Bino bintandikebirwa nebibufuude byabwe nga zitampiire wansi n'ezimu nazo we waakuteka baddemu webalambula n'ebika ebirongoosemu. \nNnyingi z",
            "chatgpt 4 response": "",
            "topics": "Breeds",
        },
        {
            "animal_crop": "Bees",
            "category": "Animal",
            "language": "Luganda",
            "location": "kyankwanzi district",
            "questions": "enjuki zirinako endwadde ezizitawaanya ?",
            "bing response": "Enjuki zirinako endwadde ezizitawaanya. Okulunda enjuki wamu n’okwongera omutindo mu bizivaamu kye kimu ku mirimu egivaamu ssente ng’omuntu ssinga abeera amanyi ekyetaagisa asobola bulungi okufunamu ssente ezimumala. Omubisi gw’enjuki ssinga obeera ogutegese bulungi naddala ng’oguwakula osobola oukugutunda shs 15,000/- ku 20,000/- eri omusuubuzi. Wabula ssinga otandika omulimu gw’okugusuubula osobola okugutunda ku 25,000 okudda waggulu buli liita",
            "bard response": "I'm still learning languages, so at the moment I can't help you with this request. So far I've only been trained to understand the languages listed in the Bard Help Center.",
            "llama -2 response": "I apologize, but I'm a large language model, I cannot understand the text you provided as it appears to be written in a fictional language or code. Can you please rephrase your question or request in English or another recognizable language? I'll do my best to assist you with any questions or problems you may have.",
            "chatgpt 3.5 response": "Zirinako endwadde ezizitawaanya kye twewunya ebirala ebiri mu bwangu we. Kubanga endwadde ezifuuyi zikiwataayo okusobola okusanyuka mu bulamu bwe. Endwadde ezizityoza emirira gy'okubaga gw'obufumu ne guvunanya obulungi bwa buli muntu okusinga ebirala. Nfumbe y'okwesamba kwekuyita oguwetaagisa ne ziyina empologoma ku muntu owaayo okusinga ebirala.",
            "chatgpt 4 response": "",
            "topics": "Diseases",
        },
        {
            "animal_crop": "Sweet Potatoes",
            "category": "Crop",
            "language": "Luganda",
            "location": "kamuli",
            "questions": "kiki ekiletera amalagala ga'lumonde okwekubamu ebituli?",
            "bing response": "Amalagala ga lumonde biba bikoola okuba n’obuti omulimi by’asonseka mu kikata kya lumonde. Ku buti obuba busonsekeddwa mu kikata ebikoola ne bisigala wabweru w’ekikata kwe kumera emirandira egigenda nga gikulira mu kikata okutuusa lwe gifuuka lumonde. Okusonseka amalagala ga lumonde mu kikata bakuyita okubyala mu Luganda",
            "bard response": "I'm still learning languages, so at the moment I can't help you with this request. So far I've only been trained to understand the languages listed in the Bard Help Center.",
            "llama -2 response": "I apologize, but I'm a large language model, I cannot understand the text you provided as it appears to be written in a fictional language or code. Can you please rephrase your question or request in English or another recognizable language? I'll do my best to assist you with any questions or problems you may have.",
            "chatgpt 3.5 response": "Kiki, ekiletera amalagala ga'lumonde okwekubamu ebituli ndi okwekuba n'okwelanwa enjiri ez'ebituli mu kwekuba, okwekwata ebyewebwaso obutano ne babŋi nga aleeta ebituli.",
            "chatgpt 4 response": "",
            "topics": "Diseases",
        },
        {
            "animal_crop": "Sweet Potatoes",
            "category": "Crop",
            "language": "Luganda",
            "location": "kamuli",
            "questions": "kiki ekileeta wuzi mulumonde ?",
            "bing response": "I’m sorry but I don’t understand your message. I will disengage from this conversation.",
            "bard response": "I'm still learning languages, so at the moment I can't help you with this request. So far I've only been trained to understand the languages listed in the Bard Help Center.",
            "llama -2 response": "I apologize, but I'm a large language model, I cannot understand the text you provided as it appears to be written in a fictional language or code. Can you please rephrase your question or request in English or another recognizable language? I'll do my best to assist you with any questions or problems you may have.",
            "chatgpt 3.5 response": "Kiki, Ekileeta is the capital city of Mulumonde.",
            "chatgpt 4 response": "",
            "topics": "Diseases",
        },
        {
            "animal_crop": "Sweet Potatoes",
            "category": "Crop",
            "language": "Luganda",
            "location": "kamuli",
            "questions": "lwaki lumonde afuna amabala amaddugavu Munda?",
            "bing response": "I’m sorry but I don’t understand your message. I will disengage from this conversation.",
            "bard response": "I'm still learning languages, so at the moment I can't help you with this request. So far I've only been trained to understand the languages listed in the Bard Help Center.",
            "llama -2 response": "I apologize, but I'm a large language model, I cannot understand the text you provided as it appears to be written in a fictional language or code. Can you please rephrase your question or request in English or another recognizable language? I'll do my best to assist you with any questions or problems you may have.",
            "chatgpt 3.5 response": "Sukaalwe mukwai, Ndani salamu sa bunifu enu afuna amabala amaddugavu Munda. Amabala amaddugavu Munda nichirikane mangani kunja kukwai pa lukoshalo, lweya lutakawika kwinja kwapo pa munda wa bwana, afuna kusaka kuti nichinjele amagwagwa kulingana ndi likoya lyamudege. Lulendo lyakwatikiza kwinja lisakuwika kuti naikala naki munda wa bwana afuna chinjania amagwagwa kumukanjalo ukasusukila. Mmodzi wathu wanali afuna kuleyana naikala naki ayambe adi abangule amagwagwa kutchale kutchalo kuya kulichalapo apabe amagwagwa, bandi sold aya kukumenya waya, nenga cyu? Sindwe apipa wanakana, afuna nichitanjako apabe amagwagwa kulipkwapo ya sildenafil. Kafoya kulich",
            "chatgpt 4 response": "",
            "topics": "Diseases",
        },
        {
            "animal_crop": "G-nuts",
            "category": "Crop",
            "language": "Luganda",
            "location": "kamuli",
            "questions": "Kiki ekiletera ebinyeebwa ebisimbe okugongobala?",
            "bing response": "I’m sorry but I don’t understand your message. I will disengage from this conversation.",
            "bard response": "I'm still learning languages, so at the moment I can't help you with this request. So far I've only been trained to understand the languages listed in the Bard Help Center.",
            "llama -2 response": "I apologize, but I'm a large language model, I cannot understand the text you provided as it appears to be written in a fictional language or code. Can you please rephrase your question or request in English or another recognizable language? I'll do my best to assist you with any questions or problems you may have.",
            "chatgpt 3.5 response": "Kiki ekiletera ebinyeebwa ebisimbe okugongobala:\n\nEbinyeebwa ebisimbe oba eweddiba, y'enkuba, obwa lava lwetaka, omuliro oba amazzi aga kusika amyuka bitandise obuli ntaano n'ebyafaayo.\n\nMubiri gw'obulaga, ebinyeebwa bya simbe bingi ebikozesebwa okugongobala ebirala byakiyinza, okuwula amatu g'obulaga n'okumanya okusingawo.\n\nKu ntebe y'amatro ew'obulaga, emigugu gikozesa abantu okugayo n'ebintu byo bulaga ebikyajumula okukimya lentebete lya binyeebwa bya simbe. Bw'ono obukyayi bwagambye bw'ekisa, gwebisimbe abantu bake, ebibyo n'amadulu gamukisibwa abimwa bagonze nabakeresera by'swkajuka, minus enziza",
            "chatgpt 4 response": "",
            "topics": "Diseases",
        },
        {
            "animal_crop": "G-nuts",
            "category": "Crop",
            "language": "Luganda",
            "location": "kamuli",
            "questions": "lwaki ebinyeebwa bifuna obutulututu obuddugavu wadde  nga bikyaali bito?",
            "bing response": "Ebinyeebwa bifuna obutulututu obuddugavu wadde nga bikyaali bito kubanga ebisimbe byonna byonna byonna byonna byonna byonna byonna byonna byonna byonna byonna byonna byonna byonna byonna",
            "bard response": "I'm still learning languages, so at the moment I can't help you with this request. So far I've only been trained to understand the languages listed in the Bard Help Center.",
            "llama -2 response": "I apologize, but I'm a large language model, I cannot understand the text you provided as it appears to be written in a fictional language or code. Can you please rephrase your question or request in English or another recognizable language? I'll do my best to assist you with any questions or problems you may have.",
            "chatgpt 3.5 response": "Ebinyeebwa byonna bifuna obutulututu obuddugavu okuva mu birobya ebyo byonna nga bikyaali byoto ku bifaananyi ebyo. Kino kisobola okuyamba obubonero obwonko, obwo bwonna bwenabeera mu mabega ga bifaananyi, nga bino waliwo obutulututu obubbombi bwa ennaku oba n’omwezi. Obudugavu obubutulututu bufuna okukubaawo obuwo okusinga abalikwana, n’okusinga obutwalibwa ku mabadde. Bino bismikirwa okusawo kanywani ebya mulyango omingi era nga babandi basobola kuliyina omuntu oba okulloka ebyo empya nga binayagala okweyisa obuwo. Buli omu atuuse kuwonya omakoole w’okweyisa wano wakati waawi ebyo. Abantu banunul",
            "chatgpt 4 response": "",
            "topics": "Diseases",
        },
        {
            "animal_crop": "G-nuts",
            "category": "Crop",
            "language": "Luganda",
            "location": "kamuli",
            "questions": "ebinyeebwa olina kubisimba kuttaka lifanana litya okusobola okubala enyo?",
            "bing response": "Nze siyogera mu Luganda, naye nze ndigambye nti ebinyeebwa bifuna obutulututu obuddugavu wadde nga bikyaali bito. Kino kitiibwa okusobola okubala enyo kubanga ebisimbe byonna byonna byonna byonna byonna byonna byonna byonna byonna byonna byonna byonna byonna byonna byonna",
            "bard response": "I'm still learning languages, so at the moment I can't help you with this request. So far I've only been trained to understand the languages listed in the Bard Help Center.",
            "llama -2 response": "I apologize, but I'm a large language model, I cannot understand the text you provided as it appears to be written in a fictional language or code. Can you please rephrase your question or request in English or another recognizable language? I'll do my best to assist you with any questions or problems you may have.",
            "chatgpt 3.5 response": "Olukuba lwokulaba nyo oba kuwaaso oba kuweyuma ne gwe omuntu okufa. Naye tavuna. Kyankwanzi Border on Jinja Drive. Paul's Experience Outback Commercial growers from around the world have worked in Santa Paula Lae søges personlig assistent. Dear Sir,Home Grown Burial Planning - Win a Mediterranean Cruise! Thus Carbon and, later The Comedians with Sir Isaac Walton.Nzakubona yanyaligambibwa na nti atalya ebiyokyo abanyere zouma kusambula ebyomuyokyo babonere mu Balongo Base Ensolo. Of_YES, on the practical management of wild grown fishBiomass of animals which have been fed 48% BSP tall grasses grown on 67% of the degraded land area: Tithonia In Brazil is it mostly grown by the small scale farmers who are located in the Amazon and in the northeast, but tghe area it is grown in is increasing especially in the south. Sir Mandale Godzis Plc hereby www. kabaka omwami olugendo Hecksher State Park It is one of the oldest cloth woven by the",
            "chatgpt 4 response": "",
            "topics": "Nature of soil",
        },
        {
            "animal_crop": "Ducks",
            "category": "Animal",
            "language": "Luganda",
            "location": "kamuli",
            "questions": "lwaki omuntu bwakwata ku majji g'embaata egazira/tedamu kubiikirawo?",
            "bing response": "I’m sorry but I don’t understand your message. I will disengage from this conversation.",
            "bard response": "I'm still learning languages, so at the moment I can't help you with this request. So far I've only been trained to understand the languages listed in the Bard Help Center.",
            "llama -2 response": "The text you provided is written in a mix of Swahili and Luganda, which are two different languages. I can understand Swahili, but not Luganda. Could you please provide the text in Swahili only, so I can assist you better? Thank you.)",
            "chatgpt 3.5 response": "Olukiiko lwaki omuntu bwakwata ku majji g'embaata egazira/tedamu kubikirawo luguwedde era luyifuna okulinnya obulungi. Tekimanyi nti ekifo kyemukola ate siliwo nokutegeera nemubiri by'omuntu oguwejjuude. Kino kitiyitamu okujjako era kwetasa luba nga gujja mu kwetaase. Naye bwe lilabyewo likuva, zingi ate kamalirirwa babulimba nga kabakwatibwa oba olwabise nnyo. Olwo akabaza olwa bintu ebikwatibwa ku majji g'embaata egazira/tedamu okulabira nga olune ne kutuweereza oluusi olwakutebe waliwo ebyabajja ebyo.",
            "chatgpt 4 response": "",
            "topics": "Veterinary care",
        },
        {
            "animal_crop": "Cattle",
            "category": "Animal",
            "language": "Luganda",
            "location": "kamuli",
            "questions": "kituufu nti mbu waliyo empiso/eddagala  lyebakuba ente esobole okwongezako kum?ata",
            "bing response": "I’m sorry but I don’t understand your message. I will disengage from this conversation.",
            "bard response": "I'm still learning languages, so at the moment I can't help you with this request. So far I've only been trained to understand the languages listed in the Bard Help Center.",
            "llama -2 response": "I apologize, but I'm a large language model, I cannot understand the text you provided as it appears to be written in a fictional language or code. Can you please rephrase your question or request in English or another recognizable language? I'll do my best to assist you with any questions or problems you may have.",
            "chatgpt 3.5 response": "mbu be nnamaze ente ndwaddeko kyokka ebiliwamu obanga esooka sokka bwemuleka okuba engatto nnyo nti obanga obulungi yyni\nMbu olwokuba ente ze zikubade okulwawo, ne batya nti bifuluma byenze mu nsi bwonna. Obanga nga bwe ninaisa ente ndwaddeko era nzibadde mu bulumwa obwa nsi era ne nzikasooka okulwawo.\n\nMbu ekibada kya ente zonna kikyusibwa mu kibumba ekimu, ekikala ekisooka okutegekawo mujje. Mbulira eri abaana bange okwagala okulwawo n’okubadde n’okubawonnayo oba ekyokulwawo nga waliwo okuyamba Nga bagenda okulwawo awo kubalirwawo okutora naddala nnyo okusobola okwonoona essuulu oba bbiri mu",
            "chatgpt 4 response": "",
            "topics": "Veterinary care",
        },
        {
            "animal_crop": "Coffee",
            "category": "Crop",
            "language": "Luganda",
            "location": "kyankwanzi district",
            "questions": "waliwo akawuka akasima ekituli mu muti gw'emmwanyi ng'ekivuuvuumira bwe kirya omuti n'ekiyingira munda . ddagala ki erivumula ekiwuka ekyo?",
            "bing response": "Nze siyogera mu Luganda, naye nze ndigambye nti ebinyeebwa bifuna obutulututu obuddugavu wadde nga bikyaali bito. Kino kitiibwa okusobola okubala enyo kubanga ebisimbe byonna byonna",
            "bard response": "I'm still learning languages, so at the moment I can't help you with this request. So far I've only been trained to understand the languages listed in the Bard Help Center.",
            "llama -2 response": "I apologize, but I'm a large language model, I cannot understand the text you provided as it appears to be written in a fictional language or code. Can you please rephrase your question or request in English or another recognizable language? I'll do my best to assist you with any questions or problems you may have.",
            "chatgpt 3.5 response": "amateeka ga aliwo nakamwe. | Messi said:\n\nOlukwagala lw'adde yo okufuuka nenkunkumula ng'okusa ebintu ebyo;\n\ntetuyambe okuyimiriza nebeiwe bwe tulya omuti, naye togilinze kweebuza ekituli. Olyoke otulemu amateeka ga abantu okuba nga batuuka ku kedde n'obutonde, n'okukiriza nga bakulira amazima ago. Naye olw'okufa emunye n'omulimu gwaffe gw'okugyira mu muti, olwo tuli n'emirembe nga tugyira bwekaawa n'otumatila. Zino zonna ddagala lino zirivuma ekiwuka ekyo y'olw'okugwa kwa bamu tambuzi, n'okwagala kwa bantu bonna.",
            "chatgpt 4 response": "",
            "topics": "Diseases",
        },
        {
            "animal_crop": "Matooke",
            "category": "Crop",
            "language": "Luganda",
            "location": "kyankwanzi district",
            "questions": "ddagala ki lye tulina okukozesa okugema ebiwuka ku ndukusa z'ebitooke nga tetunnazisimba mu ttaka?",
            "bing response": "Nze siyogera mu Luganda, naye nze ndigambye nti ebinyeebwa bifuna obutulututu obuddugavu wadde nga bikyaali bito. Kino kitiibwa okusobola okubala enyo kubanga ebisimbe byonna byonna byonna byonna byonna byonna byonna byonna byonna byonna byonna byonna byonna byonna byonna",
            "bard response": "I'm still learning languages, so at the moment I can't help you with this request. So far I've only been trained to understand the languages listed in the Bard Help Center.",
            "llama -2 response": "I apologize, but I'm a large language model, I cannot understand the text you provided as it appears to be written in a fictional language or code. Can you please rephrase your question or request in English or another recognizable language? I'll do my best to assist you with any questions or problems you may have.",
            "chatgpt 3.5 response": "Okusimba ndi mukono gw'okuzimbibwa ekiro nga eveemu. Tulina okukozesa okugema ebiwuka ku ndukusa z'ebitooke nga tetunnazisimba mu ttaka naye tekitutonyagira okuhiikiriza nnya mu biwuka ng'omutwe ogw'ebitooke oba okufuba. Eno yonna y'omutwe naye egganza okusondowa obubi obujeebwa okusooka mu ttaka obutalagana mu biwuka ebibiimu ebigatambiro gy'embiro okugema. Ebyawandiikibwa na bapadde bakulya amawulire nga obunafu obwokka ku bintu ebikolebwamu, obulamu, obukadde obwokka nga obwonna agenze obulawo okubasseemu obuwuka obulumble nga obuyinza obwo bwenene. Obulamu, ekisenge, ekikunga, n'ebikisenge ng'essential y'okuk",
            "chatgpt 4 response": "",
            "topics": "Diseases",
        },
        {
            "animal_crop": "Cattle",
            "category": "Animal",
            "language": "English",
            "location": "Ngora",
            "questions": "Why is it that every cattle farm at the gate you are made to deep your legs in water before you enter the crawl/ paddock?",
            "bing response": "The practice of dipping your legs in water before entering a cattle farm is done to prevent the spread of diseases. It helps disinfect footwear and reduces the risk of transmitting pathogens to the animals",
            "bard response": "Cattle farms make you dip your legs in water before entering because:\nIt helps to prevent the spread of diseases and parasites from your shoes to the cattle.\nIt helps to keep the farm clean and sanitary.\nIt is a simple and effective way to protect the health of the cattle.",
            "llama -2 response": "The practice of deepening one's legs in water before entering a cattle farm or paddock is meant to clean and disinfect the feet and prevent the spread of diseases among the animals. It also helps to reduce the risk of bringing in external parasites or contaminants into the facility.",
            "chatgpt 3.5 response": "Cattle farms often ask visitors to dip their legs in water at the gate before entering the crawl or paddock in order to prevent the spread of diseases. This practice, known as foot bath or foot dip, helps to disinfect the footwear, which can harbor bacteria and germs that can spread to the cattle. Foot dips can contain a solution of chemicals that kill bacteria and viruses, reducing the risk of contamination and illness among the animals. This is particularly important on cattle farms, as diseases can quickly spread among the herd and potentially lead to significant financial losses. By requiring visitors to dip their legs in water before entering the crawl or paddock, cattle farmers are taking proactive measures to protect the health and well-being of their livestock.",
            "chatgpt 4 response": "",
            "topics": "Vaccination",
        },
        {
            "animal_crop": "Cattle",
            "category": "Animal",
            "language": "English",
            "location": "Ngora",
            "questions": "What are the advantages of using a milking machine?",
            "bing response": "Milking machines offer several advantages in dairy farming. They enable efficient management of larger herds, increase milk production, and reduce labor costs. Milking machinery also ensures the farm’s continuity by reducing dependence on skilled workers. Additionally, it helps create a comfortable and stress-free environment for cows, leading to improved animal health and higher-quality milk production",
            "bard response": "The advantages of using a milking machine are:\n\n    Increased efficiency: Milking machines can milk cows much faster than humans can, which can save dairy farmers a lot of time and labor.\n    Improved milk quality: Milking machines can help to reduce the risk of contamination and produce higher quality milk.\n    Better animal welfare: Milking machines can help to reduce stress on cows and make the milking process more comfortable for them.",
            "llama -2 response": "Using a milking machine offers several advantages, including:\n\n* Increased efficiency and productivity\n* Improved milk quality\n* Reduced labor costs\n* Enhanced cow comfort and health.",
            "chatgpt 3.5 response": "1. Increased efficiency: Milking machines are able to milk multiple cows at once, resulting in increased productivity and reduced labor costs.\n\n2. Consistency: Milking machines are able to maintain a steady and consistent milking speed, ensuring that all cows are milked thoroughly and evenly.\n\n3. Improved hygiene: Milking machines are designed to reduce the risk of contamination and bacterial growth, ensuring that the milk produced is of high quality and safe for consumption.",
            "chatgpt 4 response": "",
            "topics": "Harvesting",
        },
        {
            "animal_crop": "Millet",
            "category": "Crop",
            "language": "English",
            "location": "Ngora",
            "questions": "Give the varieties of millet seeds in Uganda?",
            "bing response": "In Uganda, some of the indigenous millet varieties include Gulu E, Engeny, Serere 1, and Seremi 21. The pearl millet is another common variety grown in Uganda, known for its drought and heat tolerance2. Scientists at the National Semi Arid Resources Research Institute (NaSARRI) have been working on improving millet varieties, including NAROMILL 1 and NAROMILL 23. These efforts aim to enhance yield, resistance to drought, and nutritional value of millet crops.",
            "bard response": "The varieties of millet seeds in Uganda are:\n\n    Finger millet: This is the most common type of millet grown in Uganda. It is a staple food in many parts of the country and is used to make a variety of dishes, including porridge, bread, and beer.\n    Pearl millet: This type of millet is also grown in Uganda, but it is less common than finger millet. It is more drought-tolerant than finger millet and is often grown in drier regions of the country.\n    Foxtail millet: This type of millet is grown in smaller quantities in Uganda. It is a good source of iron and calcium and is often used to make porridge and baked goods.",
            "llama -2 response": "Here are some common varieties of millet seeds grown in Uganda:\n\n* Paddy millet (Pennisetum glaucum)\n* Finger millet (Eleusine coracana)\n* Sorghum (Sorghum bicolor)\n* Maize (Zea mays)\n* Cassava (Manihot esculenta)\n\nThese varieties are commonly grown for food and feed purposes in Uganda.",
            "chatgpt 3.5 response": "The varieties of millet seeds in Uganda include pearl millet, finger millet, and proso millet. These types of millet are commonly grown and consumed in Uganda due to their high nutritional value and ability to grow well in a variety of conditions. Other less common types of millet grown in Uganda include foxtail millet, barnyard millet, and kodo millet.",
            "chatgpt 4 response": "",
            "topics": "Varieties",
        },
        {
            "animal_crop": "Millet",
            "category": "Crop",
            "language": "English",
            "location": "Ngora",
            "questions": "Which is the best type of millet for farmers in Eastern Uganda?",
            "bing response": "In Eastern Uganda, the best type of millet for farmers is Finger Millet. It is an important staple food in Eastern Africa, including Uganda. Finger millet varieties such as Gulu E, Engeny, Serere 1, and Seremi 2 are indigenous to the region1. These varieties have average grain yields ranging from about 2000-3500kg/ha and mature between 100-110 days1. Finger millet is known for its resistance to drought and is used for various purposes, including food, poultry feed, and local brew",
            "bard response": "The best type of millet for farmers in Eastern Uganda is finger millet. Finger millet is a drought-tolerant crop that is well-suited to the climate of Eastern Uganda. It is also a highly nutritious crop that is a good source of protein, fiber, and minerals.\n\nIn addition to its drought tolerance and nutritional value, finger millet is also a relatively easy crop to grow. It can be grown on a variety of soils and does not require a lot of fertilizer or pesticides.",
            "llama -2 response": "For farmers in eastern Uganda, the best type of millet is likely to be pearl millet (Pennisetum glaucum). It is well-suited to the region's climate and soil conditions, and it has good resistance to pests and diseases. Additionally, it is a drought-tolerant crop, which makes it particularly useful in areas with limited water resources.",
            "chatgpt 3.5 response": "The best type of millet for farmers in Eastern Uganda is pearl millet. This type of millet is well adapted to the climatic conditions and soil types in the region, making it easier to cultivate and more resistant to drought and other environmental stresses. It also has high nutritional value and is used as a staple food for many communities in Eastern Uganda",
            "chatgpt 4 response": "",
            "topics": "Seeds",
        },
        {
            "animal_crop": "Sweet Potatoes",
            "category": "Crop",
            "language": "English",
            "location": "Ngora",
            "questions": "Which type of land best suites sweet potatoes production?",
            "bing response": "Sweet potatoes grow best in sandy loam soil with good drainage. A pH of 5.5 to 6.5 is ideal, but sweet potatoes tolerate a pH between 5.0 and 7.5",
            "bard response": "The best type of land for sweet potato production is a well-drained, light, sandy loam or silt loam soil. Sandy loam soils are ideal for sweet potatoes because they are well-aerated and allow for good drainage. Silt loam soils are also good for sweet potatoes, but they may require more irrigation in dry climates.Heavy clay soils are not ideal for sweet potatoes because they can hold too much water and prevent the roots from developing properly. Sweet potatoes are also sensitive to excess moisture, so it is important to avoid planting them in areas that are prone to flooding.",
            "llama -2 response": "Sweet potatoes thrive in well-draining, loose soil with a pH between 5.0 and 6.5. Sandy loams or silt loams are ideal for sweet potato production, as they offer good drainage and aeration. Avoid heavy clay soils or those prone to waterlogging, as these can lead to rot and poor yields.",
            "chatgpt 3.5 response": "Sweet potatoes thrive in well-drained, loamy soil that is rich in organic matter. Therefore, the best type of land for sweet potatoes production would be sandy loam or silt loam soil, which is a mix of sand, silt, and clay, and has good drainage and aeration. The soil pH should be between 5.0-6.8, which is slightly acidic or neutral. Additionally, the land should have access to plenty of sunlight and be able to retain moisture well, as sweet potatoes require regular watering.",
            "chatgpt 4 response": "",
            "topics": "Nature of soil",
        },
        {
            "animal_crop": "Rabbits",
            "category": "Animal",
            "language": "English",
            "location": "Ngora",
            "questions": "What is the best food for rabbits?",
            "bing response": "Rabbits need a balanced diet of hay, fresh greens, a little fruit, and a few pellets1. The majority of their diet should be composed of grass hay. Fresh foods, such as leafy greens, should make up about 75% of the fresh portion of their diet",
            "bard response": "The best food for rabbits is a balanced diet that includes hay, fresh vegetables, and a small amount of pellets.\nHay: Hay should make up the majority of a rabbit's diet. It is a good source of fiber and helps to keep the rabbit's teeth healthy. Fresh hay should be available to the rabbit at all times.\nFresh vegetables: Fresh vegetables are a good source of vitamins and minerals for rabbits. Good vegetables to feed rabbits include leafy greens, such as romaine lettuce, kale, and spinach; non-starchy vegetables, such as carrots, broccoli, and celery; and herbs, such as parsley and basil.\nPellets: Pellets are a good source of protein and other nutrients for rabbits. However, they should only be given in moderation, as they can be high in calories and fat.\nIt is important to introduce new foods to rabbits gradually to avoid stomach upsets.",
            "llama -2 response": "hay and pellets",
            "chatgpt 3.5 response": "The best food for rabbits consists of a balanced diet of hay, fresh vegetables, and a small amount of commercial rabbit pellets. Fresh hay, such as timothy, orchard grass, or oat hay, should make up the majority of a rabbit's diet. This provides the necessary fiber for their digestive health. Fresh leafy greens, such as romaine lettuce, kale, and cilantro, should be given daily in small portions as a source of vitamins and minerals. Lastly, a small amount of commercial rabbit pellets can be given as a supplement, but should not make up more than 10-15% of a rabbit's diet. It is important to avoid feeding rabbits human foods, which can be detrimental to their health.",
            "chatgpt 4 response": "",
            "topics": "Feeds/ Food",
        },
        {
            "animal_crop": "G-nuts",
            "category": "Crop",
            "language": "English",
            "location": "wakiso",
            "questions": "When planting G.nuts. what type of manure  is  good ?",
            "bing response": "Groundnuts grow well in sandy loam soil with good drainage. Organic manure such as compost or farmyard manure can be used to improve soil fertility and nutrient content. Nitrogen-fixing bacteria in the soil can also help reduce the need for nitrogen fertilizers",
            "bard response": "The best type of manure for planting groundnuts is well-rotted farmyard manure (FYM). FYM is a good source of organic matter, nitrogen, phosphorus, and potassium, which are all important nutrients for groundnut growth.FYM should be applied to the soil several weeks before planting groundnuts. This gives the manure time to break down and release the nutrients into the soil. FYM can be applied to the soil evenly and then tilled in, or it can be placed in the planting hole before planting the groundnut seeds.In addition to FYM, other good types of manure for planting groundnuts include:    Compost, Vermicompost,  Poultry manure,  Sheep manure.It is important to note that all manure should be well-rotted before it is applied to the soil. Fresh manure can contain harmful bacteria and parasites that can damage plants.",
            "llama -2 response": "For planting grapes, a well-balanced fertilizer with a ratio of 10-10-10 (nitrogen-phosphorus-potassium) or 20-20-20 is recommended. Avoid using manure with a high nitrogen content as it can cause excessive vegetative growth and reduce fruit production.",
            "chatgpt 3.5 response": "Any type of well-rotted manure or compost is good for planting G.nuts. This could include animal manure, such as cow or chicken manure, or compost made from vegetable and plant waste. It is important to use well-rotted manure so that it does not burn the young plants. Alternatively, you can use a balanced organic fertilizer specifically designed for nut crops.",
            "chatgpt 4 response": "",
            "topics": "Fertilizers",
        },
        {
            "animal_crop": "G-nuts",
            "category": "Crop",
            "language": "English",
            "location": "wakiso",
            "questions": "There are many types of G.nuts I can see on market.which is the best  for planting.?",
            "bing response": "There are several types of groundnuts available in Uganda, including Natal Common, Lianda, Red Valencia, Attica, Homa Bay, Texas peanut, Makulu red, and Red Oriata. However, Finger Millet is the best type of millet for farmers in Eastern Uganda. It is an important staple food in Eastern Africa, including Uganda. Finger millet varieties such as Gulu E, Engeny, Serere 1, and Seremi 2 are indigenous to the region1. These varieties have average grain yields ranging from about 2000-3500kg/ha and mature between 100-110 days1. Finger millet is known for its resistance to drought and is used for various purposes, including food, poultry feed, and local brew.",
            "bard response": "The best type of groundnut for planting depends on your specific needs, such as the climate and soil conditions in your area, the purpose for which you are growing the groundnuts, and your target market. However, some popular and high-yielding varieties include:\n\n    Virginia (runner): These groundnuts are known for their large size and high oil content. They are also relatively drought-tolerant and disease-resistant.\n    Valencia: These groundnuts have a hard shell and a sweet flavor. They are often used for roasting and peanut butter.\n    Spanish: These groundnuts are smaller than other varieties, but they have a higher protein content. They are often used for boiling and snacking.\n\nWhen choosing a variety of groundnut to plant, it is important to consult with a local agricultural expert who can advise you on the best varieties for your specific situation.",
            "llama -2 response": "For planting, the best type of grapes (G.nuts) is likely the Thompson Seedless variety. It's a popular and versatile choice, producing large yields of delicious fruit with good disease resistance.",
            "chatgpt 3.5 response": "The best type of G.nut for planting depends on various factors such as soil type, climate, and personal preference. However, the most popular and widely recommended type is the Red Valencia variety. It is known for its high yield, resistance to diseases, and ease of growth. Other good options include the Runner variety, which is known for its high oil content and the Spanish type, which is popular for its large and well-filled pods. Ultimately, it is important to research and consult with local experts to determine the best type of G.nut for your specific growing conditions.",
            "chatgpt 4 response": "",
            "topics": "Varieties",
        },
        {
            "animal_crop": "Maize",
            "category": "Crop",
            "language": "English",
            "location": "Apac municipal council.",
            "questions": "How can a farmer in apac district differentiate between fake and original seed especially maize?.",
            "bing response": "To differentiate between fake and original maize seeds, farmers in Apac District can consider the following steps:\n\nPurchase seeds from registered agro-dealers or seed companies’ depots.\nCheck for a Kephis tag inside the seed bag, indicating that the seed has been inspected by the regulator.\nGenuine seeds exhibit uniform size, shape, and color, while fake seeds may vary in appearance.\nCounterfeit seeds may lack proper labeling and certification.\nReport any suspicious seed sources to relevant authorities",
            "bard response": "Here are some tips for farmers in Apac district to differentiate between fake and original maize seed:\n\n    Check the packaging: Original seed is usually sold in sealed packaging with the breeder's or distributor's label. Fake seed may be sold in unsealed or poorly labeled packaging.\n    Inspect the seeds: Original maize seeds are usually uniform in size and shape and have a bright, healthy color. Fake seeds may be discolored, misshapen, or damaged.\n    Perform a germination test: A germination test can help you determine the viability of the seeds. To perform a germination test, place 20 seeds between two layers of moist paper towels and seal them in a plastic bag. Keep the bag in a warm place and check the seeds after 3-5 days. If at least 75% of the seeds have germinated, the seed is likely to be viable.\n\nIf you are unsure whether or not seed is genuine, it is best to purchase it from a reputable dealer.",
            "llama -2 response": "To differentiate between fake and original seed, a farmer in Apac District can check the seed packaging for authenticity markers such as a unique code, holograms, or special printing techniques. They can also look for inconsistencies in the packaging or the seed itself, such as poor quality paper or misspelled words. Additionally, they can consult with seed suppliers or agricultural extension officers to verify the legitimacy of the seed.",
            "chatgpt 3.5 response": "The most effective way for a farmer in Apac district to differentiate between fake and original maize seeds is to purchase them from a certified and reputable seed dealer. The dealer should provide a certificate of authenticity and a clear label on the package. The farmer can also check for physical characteristics such as color, size, and shape, as well as conduct a germination test by planting a small sample of the seeds and observing their germination rate. It is also important to do research on reputable seed brands and avoid purchasing seeds from unknown or suspicious sources.",
            "chatgpt 4 response": "",
            "topics": "Seeds",
        },
        {
            "animal_crop": "Maize",
            "category": "Crop",
            "language": "English",
            "location": "Apac municipal council.",
            "questions": "Can maize (bazooka) still be grown at this time ( September) in apac?.",
            "bing response": "Maize (bazooka) can still be grown in Apac during September. It is important to consider the local climate and soil conditions. Maize requires well-drained soil and a total seasonal rainfall exceeding 500 mm. The optimal soil pH for maize is between 5.5 and 7.0. Planting should be done as soon as soil conditions and temperature are favorable, and rainfall is well-established",
            "bard response": "Yes, maize (bazooka) can still be grown in September in Apac. However, it is important to note that the yields may be lower than if the maize was planted earlier in the season. Additionally, it is important to choose a variety of maize that is suited to the short growing season.Here are some tips for growing maize in September in Apac:\nChoose a variety of maize that is suited to the short growing season.\nPlant the maize in well-drained soil.\nWater the maize regularly, especially during the early stages of growth.\nFertilize the maize according to the instructions on the fertilizer label.\nControl weeds and pests promptly.\nWith proper care, you should be able to harvest a good crop of maize even if you plant it in September.",
            "llama -2 response": "Yes, maize can still be grown in APAC during September, but it may require careful planning and management. Ensure the soil is well-drained and has received sufficient water before planting. Monitor weather conditions closely and adjust planting dates as needed.",
            "chatgpt 3.5 response": "Yes, maize (bazooka) can still be grown at this time in September in Apac. This is because the planting season for maize in Apac usually starts in late March or early April and continues until late July or early August. This means that there is still a window for maize to be planted in September and have a successful harvest. However, farmers should consider the weather conditions and ensure that they have the necessary resources and techniques to properly care for their maize crops during this time.",
            "chatgpt 4 response": "",
            "topics": "Weather",
        },
        {
            "animal_crop": "G-nuts",
            "category": "Crop",
            "language": "English",
            "location": "wakiso",
            "questions": "How many types of G nuts  do we have in Uganda?",
            "bing response": "In Uganda, some of the indigenous groundnut varieties include Igola-1, Virginia type, Roxo 531, Long Manyema type, Red Beauty, Valencia type, Serere red, and Serenut 1-14",
            "bard response": "There are four main types of groundnuts grown in Uganda:\nRunner\nValencia\nSpanish\nVirginia\nWithin these four types, there are many different varieties of groundnuts, each with its own unique characteristics. For example, some groundnut varieties are better suited for roasting, while others are better suited for boiling or making peanut butter.\nThe best type of groundnut to grow in Uganda depends on a number of factors, such as the climate and soil conditions in your area, the purpose for which you are growing the groundnuts, and your target market.",
            "llama -2 response": "In Uganda, there are three main types of G-nuts: Ghana, Guinea, and Gold",
            "chatgpt 3.5 response": "There are two main types of groundnuts (G nuts) commonly found in Uganda - the Virginia type and the Spanish type. The Virginia type is larger in size and typically used for roasting or making peanut butter. The Spanish type is smaller and usually used for cooking and as an ingredient in dishes such as sauces and stews. However, there are also other varieties of groundnuts grown in Uganda, such as the Runner, Valencia, and Tenkwa varieties, each with their own unique characteristics and uses.",
            "chatgpt 4 response": "",
            "topics": "Varieties",
        },
        {
            "animal_crop": "G-nuts",
            "category": "Crop",
            "language": "English",
            "location": "wakiso",
            "questions": "where can I get the best seeds of G nuts for planting?",
            "bing response": "In Uganda, you can find the best groundnut seeds for planting at registered agro-dealers or seed companies’ depots. These sources provide quality seeds that have been inspected by the regulator. It’s important to ensure that the seeds are genuine and properly labeled. By purchasing from reputable sources, you can obtain high-quality seeds for your groundnut farming needs",
            "bard response": "The best place to get seeds of groundnuts for planting is from a reputable seed dealer. You can also get seeds from agricultural research institutes or from other farmers who grow groundnuts.\n\nWhen choosing a seed dealer, make sure that they are registered and licensed by the government. You should also ask to see the seed certification certificate. This will ensure that the seeds are of good quality and are free from diseases and pests.",
            "llama -2 response": "You can obtain high-quality gnut seedlings from reputable nurseries or online retailers specializing in tree and nut species. Check local climates suitability and ensure proper care before purchasing. Online marketplaces like Amazon or Burpee also offer a variety of gnut selections.",
            "chatgpt 3.5 response": "The best place to get high-quality G nut seeds for planting would be from a reputable seed supplier or a local agricultural store. It is important to ensure that the seeds are certified and have a high germination rate. You can also ask for recommendations from experienced farmers or agricultural experts in your area. Online retailers and seed exchanges can also be a good option, but it is essential to do thorough research and read reviews before purchasing. Ultimately, the key is to choose seeds from a trusted and reliable source to ensure successful growth and a good harvest.",
            "chatgpt 4 response": "",
            "topics": "Seeds",
        },
        {
            "animal_crop": "Maize",
            "category": "Crop",
            "language": "English",
            "location": "Apac municipal council",
            "questions": "How can the local community of APAC district know that their maize produce has aflotoxin?",
            "bing response": "The local community in Apac District can detect aflatoxin contamination in maize produce through various methods. These include visual inspection for mold growth, using UV light to detect fluorescence, and laboratory tests such as thin-layer chromatography (TLC), high-performance liquid chromatography (HPLC), mass spectroscopy, enzyme-linked immune-sorbent assay (ELISA), and electrochemical immunosensor123. It’s important to follow recommended farming practices, such as proper drying and storage, to minimize aflatoxin contamination4. Regular monitoring and testing can help ensure the safety and quality of maize produce.",
            "bard response": "The local community of Apac district can know that their maize produce has aflatoxin by:\n\n    Inspecting the maize for signs of mold or discoloration. Aflatoxin is produced by a fungus, so moldy or discolored maize is more likely to be contaminated.\n    Having the maize tested for aflatoxin. There are a number of different tests that can be used to detect aflatoxin in maize. These tests can be performed by a laboratory or by using a home test kit.\n\nIf the maize is found to be contaminated with aflatoxin, it should not be eaten. Aflatoxin is a carcinogen and can cause a number of other health problems.",
            "llama -2 response": "The local community in APAC district can be aware of aflatoxins in their maize through field testing by agricultural extension officers, laboratory analysis, and visual inspection. They can also be informed through farmer education programs and regular updates from the local agriculture office.",
            "chatgpt 3.5 response": "The local community of APAC district can know that their maize produce has aflatoxin through various laboratory tests and screenings. They can also observe physical symptoms such as mold growth, discoloration, and musty odor in their maize. In addition, farmers and traders can educate themselves on proper storage and handling techniques to prevent aflatoxin contamination. Engaging in regular monitoring and quality control measures can also help identify and prevent the presence of aflatoxin in maize produce. Consulting with agricultural extension officers and local authorities can also provide valuable information and resources on aflatoxin detection and prevention.",
            "chatgpt 4 response": "",
            "topics": "Diseases",
        },
        {
            "animal_crop": "Pigs",
            "category": "Animal",
            "language": "English",
            "location": "mayuge district",
            "questions": "what is the most cause of diarrhoea in pigs",
            "bing response": "Diarrhea in pigs can be caused by various factors, including bacterial infections such as Escherichia coli and colibacillosis1Viral pathogens like rotavirus, porcine epidemic diarrhea (PED), and transmissible gastroenteritis (TGE) can also lead to diarrhea2. Additionally, parasites such as coccidia, roundworms, and whipworms may contribute to the condition2. It’s important for pig farmers to implement proper hygiene practices, vaccination programs, and regular deworming to prevent and manage diarrhea in pigs",
            "bard response": "The most common cause of diarrhea in pigs is bacterial infections. It can also be caused by viruses, parasites, and dietary indiscretion.\n\nIf you are concerned about diarrhea in your pigs, it is important to consult with a veterinarian to determine the cause and get the appropriate treatment.",
            "llama -2 response": "The most common cause of diarrhea in pigs is bacterial infection, particularly E. coli and Salmonella. Other causes include viral infections, parasites, and stress-related conditions. Proper sanitation, hygiene, and management practices can help prevent or manage diarrhea in pigs.",
            "chatgpt 3.5 response": "There are several potential causes of diarrhea in pigs, including viral infections (such as rotavirus or coronavirus), bacterial infections (such as E. coli or salmonella), parasitic infections (such as coccidiosis), dietary changes or imbalances, stress, and exposure to toxins or spoiled feed. Proper sanitation and hygiene practices, as well as a balanced and appropriate diet, can help prevent and manage diarrhea in pigs. It is important for pig farmers to work closely with a veterinarian to determine the underlying cause of diarrhea and develop a treatment plan.",
            "chatgpt 4 response": "",
            "topics": "Diseases",
        },
        {
            "animal_crop": "Cassava",
            "category": "Crop",
            "language": "English",
            "location": "mayuge district",
            "questions": "what are some of the products got from cassava",
            "bing response": "Cassava, a versatile root tuber crop, can be processed into a wide range of products. Some of the products derived from cassava include food items like cassava flour, garri, and starch. Cassava is also used in the production of alcohol, animal feed, sweeteners, and bio-degradable products. Additionally, cassava leaves can be consumed as a nutritious vegetable in dishes like Kisanvu and Kwem. The way cassava is utilized varies across different countries, with each region having its own unique cassava processing techniques",
            "bard response": "Cassava can be processed into a variety of products, including:\nFood products: cassava flour, tapioca, garri, fufu, fufu flour, cassava chips, and cassava bread\nIndustrial products: cassava starch, bioethanol, adhesives, and textiles",
            "llama -2 response": "Cassava is a versatile root crop that provides several products, including:\n1. Flour or starch for baked goods and thickening agents.\n2. High-quality animal feed.\n3. Ethanol production for biofuels.\n4. Cassava chips, flakes, and pellets for snack foods and export markets.\n5. Tapioca pearls used in desserts like boba tea and sweet porridge.",
            "chatgpt 3.5 response": "Some of the products that can be obtained from cassava include cassava flour, cassava chips, cassava starch, cassava paste, cassava cakes, cassava bread, cassava beer, and cassava animal feed. Other products such as cassava noodles, cassava crackers, and cassava syrup can also be made from this versatile root vegetable. Cassava is also used in the production of biofuels, paper, glue, and textiles. Its leaves and shoots can be used as a nutritious and sustainable livestock feed. Overall, cassava is a valuable crop with a wide range of products that can be used for both human consumption and other industrial purposes.",
            "chatgpt 4 response": "",
            "topics": "Varieties",
        },
        {
            "animal_crop": "Sweet Potatoes",
            "category": "Crop",
            "language": "English",
            "location": "mayuge district",
            "questions": "What is the recommended space when heaping potatoes",
            "bing response": "The recommended spacing for planting potatoes depends on the method used. For traditional hill planting, space seed potatoes 12 inches apart and 2-3 feet between mounds. For flat planting, space seed potatoes 10-12 inches apart and 2-3 feet between rows. Raised bed planting requires 8-10 inches between seed potatoes and 1-2 feet between rows123",
            "bard response": "The recommended space when heaping potatoes is 1-2 inches between each potato. This allows for good air circulation and prevents the potatoes from touching, which can lead to rot.",
            "llama -2 response": "Heaping potatoes: Allow about 1-1.5 inches (2.5-3.8 cm) of space between potatoes.",
            "chatgpt 3.5 response": "When heaping potatoes, it is generally recommended to leave about 1/4 to 1/2 inch of space between each scoop. This allows the potatoes to hold their shape without getting squished or mashed. Additionally, leaving a bit of space also allows for proper air circulation, which helps to prevent the potatoes from getting too soggy or sticking together. However, the amount of space may vary depending on personal preference and the size of the potatoes being heaped. Ultimately, it is important to leave enough space to keep the potatoes from getting too compacted while still maintaining an appealing appearance on the plate.",
            "chatgpt 4 response": "",
            "topics": "Seeds",
        },
        {
            "animal_crop": "Pigs",
            "category": "Animal",
            "language": "English",
            "location": "mayuge district",
            "questions": "How best can I rare pigs without small in my pigs sty",
            "bing response": "To raise pigs without smell in their sty, you can follow certain practices. Providing sufficient bedding materials like straw and sawdust helps control pig manure odor. Adequate space is crucial to prevent overcrowding. Moving pigs to a different area periodically can also help. You may consider exploring Korean Natural Farming principles or the IMO method for odorless piggery house designs. These methods focus on soil processing and waste management to eliminate smell",
            "bard response": "To reduce smell in your pig sty, you can:\n\n    Keep the sty clean and dry. Clean out the sty regularly and remove all manure and bedding.\n    Use a good quality bedding. Straw or wood shavings are good options, as they absorb moisture and help to reduce odor.\n    Add a layer of lime to the bedding. Lime helps to neutralize odors and kill bacteria.\n    Ventilate the sty properly. Make sure that there is good air circulation in the sty. This will help to remove odors and keep the sty fresh.\n    Use a biosecurity program. This will help to prevent the spread of disease and parasites, which can contribute to odor.",
            "llama -2 response": "To raise healthy pigs without small in your pigs sty, ensure clean water and hygienic conditions. Provide adequate space for movement, proper ventilation, and maintain a balanced diet with no overcrowding. Regularly monitor the herd's health and vaccinate against diseases as needed. Avoid mixing young piglets with adults to prevent stress and potential disease transmission.",
            "chatgpt 3.5 response": "The key to successfully raising pigs without experiencing any smell is to maintain a clean and hygienic environment for the pigs. This includes regularly cleaning their sty, providing proper ventilation, and using absorbent bedding. Additionally, implementing a proper waste management system and keeping a smaller number of pigs in a larger space can also help reduce any unpleasant odor. Proper nutrition and regular health checkups for the pigs can also contribute to a healthier and less smelly pigsty.",
            "chatgpt 4 response": "",
            "topics": "Veterinary care",
        },
        {
            "animal_crop": "Bees",
            "category": "Animal",
            "language": "English",
            "location": "Jinja city",
            "questions": "Is the honey market around Busoga region",
            "bing response": "The global honey market is expected to grow at a compound annual growth rate (CAGR) of 5.3% from 2023 to 2030, with a value of USD 9.01 billion in 20221. The market size is estimated to reach USD 12.69 billion by 20292. However, I couldn’t find specific information about the honey market in the Busoga region. It’s advisable to consult local sources or beekeeping associations for more accurate and up-to-date information.",
            "bard response": "Yes, there is a honey market in the Busoga region of Uganda. Honey is produced in many parts of the region and is sold in local markets, supermarkets, and online.",
            "llama -2 response": "The Busoga region is known for its high-quality honey production. The region's fertile soils and favorable climate make it an ideal place for beekeeping. Local farmers produce a variety of honey types, including forest honey, savannah honey, and acacia honey. The honey is harvested twice a year, with the main harvest taking place during the rainy season. The demand for honey in the region is high, particularly among local consumers who use it as a sweetener and for medicinal purposes. Some of the challenges facing the honey industry in the region include limited access to markets, lack of processing facilities, and poor product quality due to the use of harmful practices such as the use of pesticides.",
            "chatgpt 3.5 response": "The honey market in the Busoga region is growing and has great potential. The region has a suitable climate for beekeeping, with a variety of flowering plants that provide a natural source of nectar for the bees. There is an increasing demand for honey in the local markets and the surrounding areas, making it a lucrative business for beekeepers. With proper marketing and support, the honey market in Busoga has the potential to expand and contribute to the economic growth of the region.",
            "chatgpt 4 response": "",
            "topics": "Market",
        },
        {
            "animal_crop": "Beans",
            "category": "Crop",
            "language": "English",
            "location": "mayuge district",
            "questions": "How many kilograms of soya beans can go in one accre of land",
            "bing response": "The yield of soybeans per acre depends on various factors such as soil type, climate, and planting method. According to the USDA, the average soybean yield in 2021 was 51.4 bushels per acre, which is equivalent to approximately 3.5 metric tons per hectare1. However, the yield can vary widely depending on the region and cultivation practices. It’s advisable to consult local agricultural extension services or soybean farming associations for more accurate and up-to-date information.",
            "bard response": "The number of kilograms of soybeans that can go in one acre of land depends on a number of factors, including the variety of soybean, the soil type, and the climate. However, a general rule of thumb is that you can plant 150,000 to 200,000 soybean seeds per acre. This will result in a yield of approximately 2,000 to 3,000 pounds of soybeans per acre.",
            "llama -2 response": "One acre of land can produce around 2,000 to 3,000 kilograms of soybeans per year.",
            "chatgpt 3.5 response": "On average, one acre of land can yield approximately 1,675 kilograms of soya beans. This can vary depending on factors such as soil quality, climate, and farming practices. Additionally, the exact amount of soya beans that can be grown in one acre will also depend on the specific variety of soya beans being planted. Therefore, it is important for farmers to research and consider these variables when planning their planting strategy to maximize their yield.",
            "chatgpt 4 response": "",
            "topics": "Market",
        },
        {
            "animal_crop": "Bees",
            "category": "Animal",
            "language": "English",
            "location": "mayuge district",
            "questions": "What can I use to feed bees",
            "bing response": "To feed bees, you can use honey, sugar syrup, or pollen patties. Honey is a great source of bee food, but avoid using purchased honey. Sugar syrup can be made by mixing two parts water to one part white granulated sugar. Pollen patties can be purchased or made from a dry powder",
            "bard response": "The best food for bees is sugar syrup. Sugar syrup is a mixture of sugar and water, and it is easy for bees to digest. To make sugar syrup, mix one part sugar with one part water. You can also add a small amount of lemon juice to the syrup to help prevent fermentation.You can feed bees sugar syrup using a variety of methods. One common method is to use a feeder. Feeders come in a variety of shapes and sizes, but they all work by providing bees with access to the sugar syrup.Another way to feed bees is to place the sugar syrup in a shallow dish. Make sure that the dish is not too deep, so that the bees do not drown. You can also place the dish on top of a hive box or on a platform near the hive.",
            "llama -2 response": 'You can feed bees a sugar and water solution, also known as a "sugar syrup." Mix equal parts water and white granulated sugar in a saucepan, heating it over low heat until the sugar dissolves. Let it cool before serving. Do not use honey or artificial sweeteners.',
            "chatgpt 3.5 response": "Sugar water or a commercially available bee feed can be used to feed bees in times of scarcity or during the winter months. This provides them with the necessary nutrients and energy to sustain their colony. It is important to use a feeder that prevents drowning, such as a top feeder or hive top feeder, to ensure the safety of the bees. Supplemental pollen can also be provided to help the bees build up their colony.",
            "chatgpt 4 response": "",
            "topics": "Feeds/ Food",
        },
        {
            "animal_crop": "Sweet Potatoes",
            "category": "Crop",
            "language": "English",
            "location": "kabale district",
            "questions": "Which variety of sweet potatoes is rich in iron?",
            "bing response": "Sweet potatoes are nutritious and rich in vitamins, including beta carotene, vitamin C, and potassium1. However, russet potatoes are considered the richest source of iron, with each large russet potato containing 3.2 milligrams of iron",
            "bard response": "The most iron-rich variety of sweet potato is the purple-fleshed sweet potato. Purple-fleshed sweet potatoes are also rich in other nutrients, such as vitamin A, vitamin C, and antioxidants. Other varieties of sweet potatoes that are rich in iron include:\nOrange-fleshed sweet potatoes\nWhite-fleshed sweet potatoes\nYellow-fleshed sweet potatoes\nHowever, purple-fleshed sweet potatoes have the highest iron content of all sweet potato varieties.",
            "llama -2 response": "Orange-fleshed sweet potatoes are particularly high in iron, with about 4 times more iron than white sweet potatoes.",
            "chatgpt 3.5 response": "There are various varieties of sweet potatoes that are rich in iron, such as the Purple Sweet Potato, which has a high concentration of iron compared to other types. Other varieties that are rich in iron include the Orange or Red Sweet Potato, and the Japanese Sweet Potato. Consuming these types of sweet potatoes can help increase iron levels in the body and provide other essential nutrients. Additionally, baking or roasting them with the skin on can help retain more iron.",
            "chatgpt 4 response": "",
            "topics": "Varieties",
        },
        {
            "animal_crop": "Sweet Potatoes",
            "category": "Crop",
            "language": "English",
            "location": "kabale district",
            "questions": "What is the recommended time to harvest sweet potatoes?",
            "bing response": "The recommended time to harvest sweet potatoes depends on the variety and growing conditions. Generally, sweet potatoes are ready to harvest 100-110 days after planting, when the leaves start to yellow and die back. It’s best to harvest sweet potatoes on a cloudy day to avoid sunscald. After digging, allow the roots to dry for 2-3 hours before moving them to a warm, dry, and well-ventilated place for 10-14 days",
            "bard response": "Sweet potatoes are ready to harvest when the vines start to turn yellow and die back. This usually happens around 100-140 days after planting. It is important to harvest sweet potatoes before the first frost, as frost can damage the tubers. To harvest sweet potatoes, gently dig up the tubers with a spade or fork. Be careful not to damage the tubers, as they can be easily bruised. Once the tubers have been dug up, brush off any dirt and allow them to air dry in a cool, shady place for a few days.Once the tubers have dried, they can be stored in a cool, dark place for up to several months.",
            "llama -2 response": "Sweet potatoes are ready to harvest when their skin is smooth and firm, about 100 to 120 days after planting. Check for readiness by gently digging around the base of the plant with a fork. If the fork slides in easily, it's time to harvest.",
            "chatgpt 3.5 response": "Sweet potatoes should be harvested when the leaves start to turn yellow and wilt, usually around 90-120 days after planting. The tubers should be firm and the skin should be thick. It is best to harvest sweet potatoes on a dry day to avoid any excess moisture that can lead to rotting. Harvesting too early can result in small tubers, while harvesting too late can lead to oversize tubers with a woody texture.",
            "chatgpt 4 response": "",
            "topics": "Seeds",
        },
        {
            "animal_crop": "Cassava",
            "category": "Crop",
            "language": "English",
            "location": "Teso region",
            "questions": "what are the causes of cassava roating",
            "bing response": "Cassava rot can be caused by various factors, including over-mature crops, poorly drained fields, and waterlogged soils. Other causes include fungal infections and diseases",
            "bard response": "Cassava rotting can be caused by a variety of factors, including:\nFungal and bacterial diseases: These diseases can infect the cassava roots through wounds or natural openings. Common fungal and bacterial diseases that cause cassava rotting include Fusarium wilt, bacterial blight, and cassava brown streak disease.\nPests: Pests such as nematodes and white grubs can damage the cassava roots, making them more susceptible to infection by fungi and bacteria.\nImproper storage: Cassava roots should be stored in a cool, dry place. Storing cassava roots in humid or wet conditions can promote fungal and bacterial growth, leading to rot.\nMechanical damage: Damage to the cassava roots during harvesting, transportation, or storage can also make them more susceptible to rot.",
            "llama -2 response": "Cassava rot is caused by fungal diseases, mainly Phytophthora root rot and Fusarium wilt. These diseases can be triggered by factors such as excessive water, poor soil drainage, and inadequate sunlight.",
            "chatgpt 3.5 response": "Cassava rotting can be caused by factors such as pests and diseases, improper storage and handling, unfavorable weather conditions, and the use of infected planting materials. Pests like stem borers and mealybugs can damage the roots, making them more susceptible to rot. Diseases like mosaic virus and bacterial blight can also lead to rotting. Improper storage and handling, such as storing in damp or humid conditions, can also accelerate rot. Additionally, prolonged periods of rainfall or drought can affect the health of the cassava plant and make it more vulnerable to rot.",
            "chatgpt 4 response": "",
            "topics": "Diseases",
        },
        {
            "animal_crop": "Cattle",
            "category": "Animal",
            "language": "English",
            "location": "Eastern region",
            "questions": "why is red water mostly common in animals is Eastern region",
            "bing response": "I couldn’t find specific information about “red water” being common in animals in the Eastern region. It’s possible that “red water” refers to a condition called hematuria, which can be caused by various factors such as urinary tract infections, kidney stones, or bladder tumors1. However, it’s advisable to consult local veterinary experts or animal health authorities for more accurate and region-specific information.",
            "bard response": "Redwater, also known as babesiosis, is a tick-borne disease that affects cattle and other animals. It is caused by a parasite called Babesia, which is transmitted to animals through the bite of an infected tick.Redwater is most common in the Eastern region of Uganda because the climate in this region is favorable for ticks. Ticks thrive in warm, humid conditions, and the Eastern region of Uganda is generally warmer and more humid than other parts of the country.Additionally, the Eastern region of Uganda has a large population of cattle and other animals that are susceptible to redwater. This provides a large pool of hosts for the parasite, which contributes to the high prevalence of the disease in this region.",
            "llama -2 response": "Red water is more common in animals in the eastern region due to the high concentration of iron and other minerals in the soil and water. These minerals can cause a condition called hemochromatosis, which results in red-colored urine and other symptoms.",
            "chatgpt 3.5 response": "Red water in animals is commonly found in the Eastern region due to the presence of certain organisms in the water. These organisms, such as red algae and bacteria, produce pigments that give the water a reddish hue. Additionally, the high concentrations of certain minerals and nutrients in the Eastern region's water can also contribute to the development of red water. This phenomenon is more prevalent in Eastern regions due to environmental factors and the specific habitats of these organisms.",
            "chatgpt 4 response": "",
            "topics": "Diseases",
        },
        {
            "animal_crop": "G-nuts",
            "category": "Crop",
            "language": "English",
            "location": "Karamoja region",
            "questions": "How can people from Karamoja region be on new varieties of crops since some of them stay rural areas",
            "bing response": "To introduce new crop varieties to rural areas in the Karamoja region, it’s important to focus on integrated livestock-crop strategies. Initiatives like supporting balanced and integrated livestock-crop development, providing access to early-maturing maize and sorghum varieties, and improving soil fertility can help enhance food production and resilience. Training programs on regenerative agriculture and kitchen gardening can also empower communities to adopt sustainable farming practices",
            "bard response": "People from Karamoja region can be introduced to new varieties of crops through:\n\n    Agricultural extension services: Agricultural extension officers can visit rural areas to educate farmers about new crop varieties and how to grow them.\n    Demonstration farms: Demonstration farms can be set up in rural areas to show farmers how to grow new crop varieties and the benefits of doing so.\n    Seed fairs: Seed fairs can be held in rural areas to allow farmers to purchase seeds of new crop varieties.\n    Radio and television programs: Radio and television programs can be used to educate farmers about new crop varieties and how to grow them.",
            "llama -2 response": "People in rural areas of Karamoja can still access and benefit from new crop varieties through various channels, such as government extension services, non-profit organizations, and private seed companies. These entities often provide training and resources for farmers to adopt improved crop varieties, even in remote areas. Additionally, many farmers in Karamoja have embraced traditional farming practices that are well-suited to their local conditions, such as growing drought-tolerant crops like sorghum and millet.",
            "chatgpt 3.5 response": "To introduce new varieties of crops to people in rural areas of Karamoja, the most effective approach would be to engage with and train local community members, such as farmers and village leaders, on the benefits and techniques for growing these crops. Additionally, partnering with local organizations and agricultural extension services can help to spread awareness and provide support to those living in more remote areas. Utilizing media platforms, such as radio broadcasts, can also help to reach those who may not have access to formal training programs.",
            "chatgpt 4 response": "",
            "topics": "Varieties",
        },
    ]

    current_user_id = get_jwt_identity()
    dup_count = 0
    duplicates = []

    for obj in json_data:
        sentence = obj.get("questions")
        language = obj.get("language")
        topic = obj.get("topics")
        category = obj.get("category")
        animal_crop = obj.get("animal_crop")
        location = obj.get("location")

        # Check if the question already exists
        if Question.query.filter_by(sentence=sentence, cleaned=True).first():
            dup_count += 1
            duplicates.append({"sentence": sentence})
        else:
            question = Question(
                sentence=sentence,
                language=language,
                user_id=current_user_id,
                topic=topic,
                category=category,
                animal_crop=animal_crop,
                location=location,
                cleaned=True,
            )
            db.session.add(question)
            db.session.commit()
            question_id = question.id

            response_categories = [
                "bing response",
                "bardrResponse",
                "llama -2 response",
                "chatgpt 3.5 response",
                # "chatgpt 4 response",
            ]
            for category in response_categories:
                response_value = obj.get(category)
                if response_value is not None:
                    response = Answer(
                        question_id=question_id,
                        answer_text=response_value,
                        source=category,
                        user_id=current_user_id,
                    )
                    db.session.add(response)
                    db.session.commit()

    response_data = {"duplicates_count": dup_count, "duplicates": duplicates}
    return jsonify(response_data), HTTP_200_OK
