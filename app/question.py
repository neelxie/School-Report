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


@questions.route("/upload_json_answers/", methods=["POST"])
@jwt_required()
def upload_json_answers():
    if request.method == "POST":
        beforeData = request.get_json()
        json_data = beforeData["file"]
        

        current_user_id = get_jwt_identity()
        dup_count = 0
        duplicates = []

        for obj in json_data:
            sentence = obj.get("Prompts")
            language = obj.get("Language")
            topic = obj.get("Topic")
            category = obj.get("Category")
            animal_crop = obj.get("animal_crop")
            location = obj.get("Location")

            # Check if the question already exists
            if Question.query.filter_by(sentence=sentence).first():
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
                    "Bing response",
                    "Bard Response",
                    "Llama -2 Response",
                    "GPT 3.5 response",
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
