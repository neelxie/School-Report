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
            "animal_crop": "Chicken",
            "Category": "Animal",
            "Language": "English",
            "Location": "Uganda",
            "Prompts": "If i need to feed each hen; 130g of Ugachick premixed feed per day in order to get one egg per day per hen and i have 500 hens. With each hen having a life expectancy of three years, How many eggs in total can i expect my hens to have laid over the course of three years before selling them off. Explain it to me step by step",
            "Bard Response": "A hen can lay an egg a day if she is fed 130g of Ugachick premixed feed.\nYou have 500 hens, so you need to feed them 500 * 130g = 65000g of feed per day.\nEach hen has a lifespan of 3 years, so you can expect them to lay eggs for 3 * 365 = 1095 days.\nSo, the total number of eggs you can expect your hens to lay is 1095 * 500 = 547500 eggs.",
            "Llama - 2 Response": "Sure! Here's the calculation: 1. Life expectancy: 3 years x 365 days/year = 1,095 days 2. Daily eggs per hen: 1 egg/day x 500 hens = 500 eggs/day 3. Total eggs per year: 500 eggs/day x 365 days/year = 182,500 eggs/year 4. Total eggs over 3 years: 182,500 eggs/year x 3 years = 547,500 eggs So, you can expect your hens to lay approximately 547,500 eggs over three years, assuming they each produce one egg per day.",
            "Bing response": "If you feed each of your 500 hens 130g of Ugachick premixed feed per day, you can expect each hen to lay 365 eggs per year. Over three years, you can expect a total of 912,500 eggs. This is calculated by multiplying the number of hens (500) by the number of eggs laid per year (365)",
            "GPT 3.5 response": "If each hen needs 130g of feed per day for one egg, then they will require 130g * 365 days = 47,450g (47.45kg) of feed per year. For 500 hens, the total feed required will be 47.45kg * 500 = 23,725kg per year. Over three years, the total feed required will be 23,725kg * 3 = 71,175kg.",
            "Topic": "Animal feeds and nutrition",
        },
        {
            "animal_crop": "Chicken",
            "Category": "Animal",
            "Language": "English",
            "Location": "Uganda",
            "Prompts": "Would i make enough money to break even at the end of the chicken if i start off with 50 layer chicken in a deep litter system. Factor in the price of feeding each chicken to from chicks to adulthood, price of buying a chick and selling a tray of eggs in Uganda will give me 12000 shillings per tray. Explain it to me step by step",
            "Bard Response": "To break even, you need to sell 50 * 12000 = 600000 shillings worth of eggs.\nIf each chicken lays 300 eggs per year, you need to keep the chickens for 200 years.\nThe cost of feeding each chicken is 1000 shillings per year, so the total cost of feeding the chickens is 50000 shillings.\nTherefore, you need to sell the chickens for at least 65000 shillings to break even.\nSo, the answer is yes, you would make enough money to break even at the end of the chicken if you start off with 50 layer chicken in a deep litter system.",
            "Llama - 2 Response": "Sure! Here's the calculation step-by-step: 1. Chicken starting costs: 50 chicks x $3 = $150 (assuming $3 per chick) 2. Feed costs from chicks to laying age: $150 x 6 months = $900 3. Egg sales revenue: 12000 shillings per tray x 10 trays per month = $12,000 per month 4. Break-even point: $900 + $12,000 = $13,900 So, you would reach break-even point after selling around 10 trays of eggs per month, assuming no other expenses or income sources.",
            "Bing response": "To calculate the profitability of your chicken farming venture, you need to consider various factors such as the cost of feeding each chicken from chicks to adulthood, the price of buying a chick, and the selling price of a tray of eggs. You should also factor in other costs like housing, labor, and veterinary care. Subtract the total costs from the revenue generated by selling eggs to determine if you will break even or make a profit",
            "GPT 3.5 response": "To calculate if you will break even, consider the costs of raising 50 layer chickens to adulthood, including chick prices and feed costs. Estimate the total cost and compare it to the revenue from selling eggs. Multiply the number of trays (e.g., 20 eggs per tray) sold by the selling price per tray to calculate revenue. If revenue exceeds costs, you will break even.",
            "Topic": "Animal marketing",
        },
        {
            "animal_crop": "Coffee",
            "Category": "Crop",
            "Language": "Luganda",
            "Location": "Uganda",
            "Prompts": "Abalimi mu bitundu by’olusozi Elgon bayinza batya okwewala endwadde mu kaawa",
            "Bard Response": "I'm still learning languages, so at the moment I can't help you with this request. So far I've only been trained to understand the languages listed in the Bard Help Center.",
            "Llama - 2 Response": "As an experienced farmer, I am concerned about the negative impact of climate change on our crops and livestock. We must work together to find sustainable solutions for a resilient future.",
            "Bing response": "Nkakasa, nze simanyi oba nnoonyereza ku bitundu by’olusozi Elgon. Naye nze ndiggye nti okwewala endwadde mu kaawa kwe kugamba nti abalimi mu bitundu by’olusozi Elgon bali batya okwewala endwadde mu kaawa. Nga bwekityo, nze simanyi oba bino byonna byonna byonna byonna byonna",
            "GPT 3.5 response": "Abalimi mu bitundu by’olusozi Elgon bafambisa ebirala mu kantu kamwe ku baganda n’abakyala abatya okwewala endwadde mu kaawa. Era oluvannyuma lw’ensi eno ne bwe lwakoma okutuuka okwatiddwala nga bwe lwakoma okumala.Okuyingira mu maaso n’obulwadde kuwala endwadde mu kaawa ne bwe lwakoma olina amagezi g’eby’okubaenderamu n’ebirala by’amayinja omu kaawa bwe lwakoma bw’ayita kuwanjaganya endwadde mu kaawa.Abalimi ne batendawo okubamalako mu bwangu bwaendwadde bwe kaawa baba omusomesa awabeere mu kibuga Nendogamistaali bano Bungokho Kowalalu. Omukwano gwe’ggwa ku baasoma bano nga balaba okujako banafaayo omusanyusa w’obuzibu atuli.",
            "Topic": "Crop pest and disease management",
        },
        {
            "animal_crop": "Coffee",
            "Category": "Crop",
            "Language": "English",
            "Location": "Nakasongola",
            "Prompts": "A farmers in Nakasongola district wants to grow coffee, he wants to know how it is cultivated",
            "Bard Response": "Tips for growing coffee in Iganga district:\nThe ideal temperature for coffee cultivation is 18-24 degrees Celsius.\nIganga district receives an average of 1,500-2,000 mm of rainfall per year, which is sufficient for coffee cultivation.\nThe soil in Iganga district is generally well-drained, which is ideal for coffee cultivation.\nCoffee plants are susceptible to a number of pests and diseases, so it is important to take steps to protect them.",
            "Llama - 2 Response": "To grow coffee, plant Robusta or Arabica seeds in well-draining soil with ample sunlight. Water regularly and provide shade during hot seasons. Prune trees annually for optimal yields.",
            "Bing response": "Coffee is a flowering plant cultivated for its seeds, called coffee beans. It grows best in warm areas with temperatures between 16-24ºC. Coffee plants can be grown in pots or backyards. They start producing beans 3-4 years after planting.",
            "GPT 3.5 response": "Coffee is grown by planting seedlings in well-drained, fertile soil that receives enough rainfall or irrigation. The seedlings take 3-4 years to produce berries, which are handpicked when ripe. The berries are then pulped, fermented, and washed to remove the outer layers. After drying, the coffee beans are roasted and ground to produce the final product. Regular pruning, fertilization, and pest control are crucial for a successful coffee crop.",
            "Topic": "Planting and Sowing",
        },
        {
            "animal_crop": "Sheep",
            "Category": "Animal",
            "Language": "English",
            "Location": "Nakaseke",
            "Prompts": "How can a farmer with 100 heads of sheep in Ngoma, Nakaseke district treat them from diseases",
            "Bard Response": "Here are the steps on how a farmer with 100 heads of sheep in Ngoma, Nakaseke district can treat them from diseases :\nConsult a vet.\nIsolate sick sheep.\nAdminister meds.\nProvide supportive care.",
            "Llama - 2 Response": "The farmer can treat their 100 heads of sheep in Ngoma, Nakaseke district by providing clean water and nutritious feed, vaccinating against common diseases, and monitoring for signs of illness. Regular deworming and parasite control also helps prevent disease transmission.",
            "Bing response": "Sheep can be affected by various infectious and noninfectious diseases. To treat them, consult a veterinarian for diagnosis and appropriate treatment. Regularly wash the sheep with parasites removing medicine, apply disease preventive vaccines, and feed them worm protective medicine",
            "GPT 3.5 response": "The farmer should ensure that the sheep are regularly vaccinated against common diseases. They should also be kept in a clean and hygienic environment to prevent the spread of diseases. The farmer should deworm the sheep regularly and provide them with a balanced diet to maintain their immune system. In case of any signs of illness, a veterinarian should be consulted immediately.",
            "Topic": "Animal diseases, management and prevention",
        },
        {
            "animal_crop": "Coffee",
            "Category": "Crop",
            "Language": "English",
            "Location": "Mbale",
            "Prompts": "A coffee farmer in Mbale was found spraying gramoxone (herbicide) and was told that it was banned. List down other insectcides that were banned in Uganda",
            "Bard Response": "Insecticides: Carbofuran, Dichlorvos, Fenitrothion",
            "Llama - 2 Response": "Here are some insecticides that have been banned in Uganda: * Gramoxone (herbicide) * DDT (insecticide) * Lindane (insecticide) * Chlorpyrifos (insecticide) * Mercury-based pesticides",
            "Bing response": "Four pesticides, carbofuran, dichlorvos, fenitrothion (insecticides) and gramoxone (herbicide) have been banned from use in Uganda",
            "GPT 3.5 response": "1. Aldicarb (carbamate insecticide)\n2. Carbofuran (carbamate insecticide)\n3. DDT (organochlorine insecticide)\n4. Lindane (organochlorine insecticide)\n5. Monocrotophos (organophosphate insecticide)\n6. Paraquat (herbicide)\n7. Endosulfan (organochlorine insecticide)\n8. Methamidophos (organophosphate insecticide)\n9. Methyl parathion (organophosphate insecticide)\n10. Dicofol (organochlorine insecticide)",
            "Topic": "Crop pest and disease management",
        },
        {
            "animal_crop": "Sheep",
            "Category": "Animal",
            "Language": "Luganda",
            "Location": "Uganda",
            "Prompts": "Endiga enkazi esobola okufa ng’ezaala olw’omutima okulemererwa, okulumwa, okuvaamu omusaayi. Wandiika ebintu ebirala ebiyinza okugiviirako okufa ng’ezaala.",
            "Bard Response": "As an LLM, I am trained to understand and respond only to a subset of languages at this time and can't provide assistance with that. For a current list of supported languages, please refer to the Bard Help Center.",
            "Llama - 2 Response": "Endiga enkazi esobola okufa ng'ezaala olw'omutima okulemererwa, uganda nga wangezi wanzita.",
            "Bing response": "Nkakasa, nze simanyi oba nnoonyereza ku bitundu by’olusozi Elgon. Naye nze ndiggye nti okwewala endwadde mu kaawa kwe kugamba nti abalimi mu bitundu by’olusozi Elgon bali batya okwewala endwadde mu kaawa. Nga bwekityo, nze simanyi oba bino byonna byonna byonna byonna byonna",
            "GPT 3.5 response": "Okufa ng’ezaala olw’omutima kubanga kukyawa ensi eno emirira gyayo n’ogwe ekutuyazikika okweyongera kw’okukola mu buwanguzi bwaffe. Okunyiga emiggo gyaffe okuba n’amatoro gy’enjawulo togiliba n’ogwe egenda mu namugongo abazuula, okusonko okuseburisa bulungi ne bamusenkye. Kubonereza kwo ne kwengeza kwekwevuuta ekiso era empale kuwaasseera okuwa ebintu ebigenderako nga mbeera okukolaba ebintu by’ekibiina gyatandikirwa, olw’okukoomera okukola ne kugalinnya ekibiina kya bantu. Kyali kyeeyongera n’okwefuna omusango omu. Kye akalulu ka bantu abamu be nitumikirye ne baleebere ababiri ensi eno be ntuyisa n’okusemma abantu, okuwanula obun",
            "Topic": "Animal diseases, management and prevention",
        },
        {
            "animal_crop": "Coffee",
            "Category": "Crop",
            "Language": "Luganda",
            "Location": "Uganda",
            "Prompts": "Singa emmwaanyi zange zivaamu ttani emu buli mwezi. ttani mmeka ze zinaavaamu mu mwaka katulowoozeeko mutendera ku mutendera",
            "Bard Response": "I'm still learning languages, so at the moment I can't help you with this request. So far I've only been trained to understand the languages listed in the Bard Help Center.",
            "Llama - 2 Response": "Inga emmwaanyi zange zivaamu ttani emu buli mwezi. Ttani mmeka ze zinaavaamu mu mwaka katulowoozeeko mutendera ku mutendera.",
            "Bing response": "Nkakasa, nze simanyi oba nnoonyereza ku bitundu by’olusozi Elgon. Naye nze ndiggye nti okwewala endwadde mu kaawa kwe kugamba nti abalimi mu bitundu by’olusozi Elgon bali batya okwewala endwadde mu kaawa. Nga bwekityo, nze simanyi oba bino byonna byonna byonna byonna byonna",
            "GPT 3.5 response": "Nzibe zinaavaamu ntyaamu buli mwezi mu 1 Muwaka Okumuda Mutendera ku Mutendera. nzira ndimu enzaiddeyo neemitena ku nsi yonna eli mu maanyi gaali. Nzibe zivunja mu buli mutabaala. Mbaga muwashongojoka mu bbanku ndimu ezoondokanga nava ntyaamu Ndizikyal yammwe. Nzibe ndavaavamu okulibwa ssente ensiimi naye nga nsira enkubiramu bbanku ssente. Nga addira yange ga nsi. Navaavamu okunyumiramu Nzibe zinavaamu buli mwezi ku mutendera ku mutendera. kumweleza mu nkusunguza yange ndangamu Okusoga namagombe koosimba kumweleza mu nkuzunga yange nti ono si omaze OKWangaazangoMMRH .Nzibe zinaavaamu ntyaamu nesasi n'ekibuzzi ze buli mwezi. Ok",
            "Topic": "Crop harvesting and post-harvest handling",
        },
        {
            "animal_crop": "Sheep",
            "Category": "Animal",
            "Language": "Luganda",
            "Location": "Uganda",
            "Prompts": "Omulimi afuna liita z’amata amakumi abiri okuva mu ndiiga ye buli lunaku liita z’amata mmeka ye mu myezi esatu katulowoozeeko mutendera ku mutendera.",
            "Bard Response": "I am an LLM trained to respond in a subset of languages at this time, so I can't assist you with that. Please refer to the Bard Help Center for the current list of supported languages.",
            "Llama - 2 Response": "Mumuteko yokwe mu buli lunaku, liita z'amata mmeka ye mu myezi esatu katulowoozeeko.",
            "Bing response": "Omulimi afuna liita z’amata amakumi abiri okuva mu ndiiga ye buli lunaku liita z’amata mmeka ye mu myezi esatu katulowoozeeko mutendera ku mutendera",
            "GPT 3.5 response": "Ndiri omulimi ono omuntu ajja mu bwangu lw’okujawukilaho okusula ebicumu bino ate alleen okuzaala mu diiga yange omukumi abiri ani kubanga buli lunaku ndifa ebicumu bino, naye omulimi afuna liita z’amata esatu zonna ezilowoozeeko musiime okukuluziza ku mutendera w’amaanyiriddwa ag’ebicumu byo.\nBy obsessively watering his crops twice a day, the farmer ensures that his crops receive the necessary amount of water every day.",
            "Topic": "Animal diseases, management and prevention",
        },
        {
            "animal_crop": "Coffee",
            "Category": "Crop",
            "Language": "Luganda",
            "Location": "Eastern Uganda",
            "Prompts": "Kaawa wa arabic alimibwa ku lusozi Elgon, mu buvanjuba bwa Uganda, kitundu ki ekirala eky’eggwanga ky’atera okulimibwa?",
            "Bard Response": "As an LLM, I am trained to understand and respond only to a subset of languages at this time and can't provide assistance with that. For a current list of supported languages, please refer to the Bard Help Center.",
            "Llama - 2 Response": "Kaawa wa Arabic alimibwa ku Lusozi Elgon, mu buvanjuba bwa Uganda, kitundu ki ekirala eky'eggwanga ky'atera okulimibwa.",
            "Bing response": "Kaawa wa arabic alimibwa ku lusozi Elgon, mu buvanjuba bwa Uganda. Kitundu kya ekirala eky’eggwanga ky’atera okulimibwa kya Uganda",
            "GPT 3.5 response": "Olusozzi Elgon mu Uganda ku by’ebya lwaki abantu balya okulimibwa era bikirala ebyo ebitundu by’amazzi ate olulimi luwa dda ku lusozi lutenderezeddwa ekitundu ekinene.",
            "Topic": "Planting and Sowing",
        },
        {
            "animal_crop": "Rice",
            "Category": "Crop",
            "Language": "English",
            "Location": "Central Uganda",
            "Prompts": "What rice varities can i grow in Central Uganda? Provide a brief list of 3 varieties i can grow here",
            "Bard Response": "Three rice varieties that you can grow in Central Uganda are NERICA 1, NERICA 4, and Kaiso. These varieties are all high-yielding, pest-resistant, and well-adapted to the local conditions.",
            "Llama - 2 Response": "Here are three rice varieties that can be grown in central Uganda: 1. Nerica 1: A popular variety that matures within 90 days and is resistant to blast and stem borer. 2. Nerica 5: A high-yielding variety that matures within 120 days and has good resistance to pests and diseases. 3. Swati: A local variety that is well-suited for the humid climate of central Uganda, with a maturity period of around 100 days.",
            "Bing response": "According to the Rice Cultivation Handbook by the Government of Uganda, there are several varieties of rice that can be grown in Uganda1. Some of the varieties that you could consider growing in Central Uganda include:\nNERICA 4 (Upland Rice): Matures in 110-120 days and has a yield of 4.0-5.0 t/ha1.\nNERICA 1 (Upland Rice): Matures in 105-115 days and has a yield of 3.0-4.0 t/ha. It is also aromatic1.\nK-85 (Lowland Rice): This is an older variety that was introduced many years ago from elsewhere2.\nIt’s important to note that the best variety for your land will depend on factors such as soil type, climate, and water availability. You may want to consult with local agricultural experts or other farmers in your area to determine which variety would be best for your land.",
            "GPT 3.5 response": "1. NERICA 4 - This variety of rice is a cross between African and Asian rice, making it well-suited for the growing conditions found in Central Uganda. It has a shorter growing period and higher yield compared to other varieties, making it a popular choice among farmers in the region.\n2. Basmati - This long-grain variety is well-known for its aromatic fragrance and is typically grown in the Eastern parts of Uganda. However, with proper management and ideal conditions, it can also be successfully cultivated in Central Uganda.\n3. NERICA 10 - Another popular variety in Central Uganda, NERICA 10 is a high-yielding and disease-resistant rice variety. It has a medium maturity period and is suitable for both rain-fed and irrigated farming systems. Additionally, it is rich in nutrients, making it a nutritious option for farmers and consumers alike.",
            "Topic": "Planting and Sowing",
        },
        {
            "animal_crop": "Rice",
            "Category": "Crop",
            "Language": "English",
            "Location": "Wakiso",
            "Prompts": "I am a rice farmer in Wakiso with 5 acres of land. When is the best time for me to plant my rice?is the best time for me to plant my rice?",
            "Bard Response": "The best time to plant rice in Wakiso, Uganda is March-April and August-September. Consult with your local agricultural extension officer for specific advice for your area.",
            "Llama - 2 Response": "The best time to plant rice in Wakiso, Uganda is during the rainy season (March to August). This allows for optimal growing conditions and a higher yield.",
            "Bing response": "According to my sources, the best time to plant rice in Uganda depends on the amount of rainfall and the agronomic practices you follow1. It is recommended to plant rice in lower parts of the field to reduce the drought risk and to target a higher yield1.",
            "GPT 3.5 response": "The best time to plant rice in Wakiso is between the months of March and April, as this coincides with the rainy season. This will ensure that your crops have enough water for proper growth and yield. It is important to start planting as soon as the rains begin, as rice requires a lot of water to grow. It is also recommended to choose high-yielding, disease-resistant rice varieties for maximum production. Consult with your local agricultural extension office for more specific planting recommendations for your area.",
            "Topic": "Planting and Sowing",
        },
        {
            "animal_crop": "Rice",
            "Category": "Crop",
            "Language": "English",
            "Location": "Uganda",
            "Prompts": "Bbanga ki erikubirizibwa okulekebwa wakati w'omuceere ng'ogusimba?",
            "Bard Response": "I'm still learning languages, so at the moment I can't help you with this request. So far I've only been trained to understand the languages listed in the Bard Help Center.",
            "Llama - 2 Response": "Bbanga ki Erikubirizi bwa Okulekebwa wakati w'omuceere ng'ogusimba. (Grammar and vocabulary are not correct, please provide a real sentence.)",
            "Bing response": "I'm sorry, but I couldn't find any information about the spacing between rice plants and the stem. Could you please clarify your question or provide more details so that I can better assist you?",
            "GPT 3.5 response": "Kemika ky'obugwangwa bwa muceere okuba okusiyaga olulimi era waliwo abantu abangu tewali bisaanya nti waana kaakano kikuba kiba ky'emirimu gy'okukolanga eby'omwoyo bali wansi w'omuceere gwakiwandiikira. Bbanga ki muno; ku basaba olwoolesezza okulekebwa wakati w'omuceere ng'ogusimba, kukkiriza omuceere okukalaba olulimi lwa kitalo okwekana obulungi obukozesebwa omwaka ebyobulamu obuyonjo, okusaba emirembe obilala ebigambo okusunsula omuceere okuva ebigambo bikola obukadde bwe kyokka emirembe okusaba okulongoosa olulimi lwa nyina okusinga!",
            "Topic": "Planting and Sowing",
        },
        {
            "animal_crop": "Sweet Potato",
            "Category": "Crop",
            "Language": "English",
            "Location": "Kasese",
            "Prompts": "I grow sweet potatoes on my piece of farm land in Kasese district and was wondering how long can sweet potatoes take before they go bad?",
            "Bard Response": "Sweet potatoes can last for up to a month at room temperature, or up to four months in a cool, dark place. You can also freeze them for up to six months.",
            "Llama - 2 Response": "Sweet potatoes can last for several months when stored properly. In ideal conditions, they can remain fresh for up to 6-8 months. However, if stored in warm temperatures or exposed to moisture, they may spoil faster.",
            "Bing response": "Sweet potatoes can last for one to four weeks depending on whether you leave them on the counter or store them in a cool and dark place like a pantry. Cut sweet potatoes last for 3 to 5 days, while cooked ones stay safe for 3 to 4 days only. Raw sweet potato kept on the countertop will go bad within one or two weeks. Stored correctly in the pantry, they should last for around one month.",
            "GPT 3.5 response": "Sweet potatoes can usually last for several weeks before going bad, as long as they are stored properly in a cool, dry and well-ventilated place. They can also last for several months if stored in a cool, humid and dark environment, such as a root cellar. However, the exact shelf life may vary depending on the variety, growing conditions and storage methods used. It is important to regularly check and remove any spoiled or damaged sweet potatoes to prevent them from affecting the rest.",
            "Topic": "Crop harvesting and post-harvest handling",
        },
        {
            "animal_crop": "Cattle",
            "Category": "Animal",
            "Language": "English",
            "Location": "Uganda",
            "Prompts": "My neighbor's farm has had an outbreak of anthrax and I fear it will spread to my dairy cattle especially the pregnant cows. How can I vaccinate my pregnant cows safely?",
            "Bard Response": "To safely vaccinate your pregnant cows against anthrax, consult with your veterinarian. They can advise you on the best vaccine to use and the best time to vaccinate. It is also important to note that you should take steps to biosecure your farm and prevent the spread of anthrax from your neighbor's farm. This may include restricting the movement of animals and equipment, and disinfecting any surfaces that may have been contaminated.",
            "Llama - 2 Response": "It is not recommended to vaccinate pregnant cows for anthrax, as the vaccine can cause adverse effects on the developing fetus. Instead, isolate and monitor your cows closely, provide supportive care, and consult with a veterinarian for guidance on how to protect your herd.",
            "Bing response": "Vaccination is the best way to protect your cattle from anthrax. Pregnant cows can be vaccinated against anthrax, but it is important to consult with a veterinarian before vaccinating them. The recommendations of the International Working Group on anthrax indicate that cattle grazing pastures within 6 miles (10 km) of a known previously infected area should be vaccinated as well, due to the potential for wildlife or biting flies to transmit anthrax spores to adjacent herds.",
            "GPT 3.5 response": "The best way to vaccinate your pregnant cows against anthrax is to work closely with your veterinarian. They can advise you on the appropriate timing and type of vaccine to use, as well as any potential risks associated with vaccinating pregnant animals. It is important to follow their guidance and make sure that the vaccine is administered correctly and safely to minimize any potential harm to your cows and their offspring. Additionally, implementing proper biosecurity measures, such as quarantining any new animals or regularly disinfecting equipment, can also help prevent the spread of anthrax to your herd.",
            "Topic": "Animal diseases, management and prevention",
        },
        {
            "animal_crop": "Cattle",
            "Category": "Animal",
            "Language": "English",
            "Location": "Uganda",
            "Prompts": "Last month my dairy cows produced 8 litres per cow each day but ever since i changed their feeds and started feeding them sweet potato peelings the milk produced per cow reduced to about 3 litres per cow. I want my cows to produce more than 8 litres per day for each cow. What can I do?",
            "Bard Response": "To increase your cows' milk production, feed them a complete and balanced diet, provide them with fresh water, make sure they have a comfortable environment, milk them regularly, and keep them healthy.It is also important to note that it may take some time for your cows to start producing more milk after you change their diet. It is important to be patient and consistent with their feeding and milking routine.",
            "Llama - 2 Response": "Adjust your cow's diet by adding a high-energy feed such as corn or wheat bran to increase milk production. Ensure they have access to clean water and proper shelter.",
            "Bing response": "There are several ways to increase milk production in dairy cows. Some of the ways include providing clean water and feed, avoiding stress factors, and using hormones. You can also try feeding your cows a balanced diet that includes high-quality forage and concentrates. Sweet potato peelings are not a good source of feed for dairy cows as they are low in protein and energy. It is important to consult with a veterinarian or an animal nutritionist before making any changes to your cows’ diet.",
            "GPT 3.5 response": "There could be a few reasons for the decrease in milk production. Firstly, make sure that the sweet potato peelings are not replacing the cows' regular feed completely, as they may be missing important nutrients. It is best to mix the peelings with a balanced diet. Additionally, it could be possible that the cows are not adjusting well to the new feed, so it may take some time for them to adapt. Lastly, make sure that the cows have access to clean water and a comfortable environment, as these factors play a significant role in milk production. Consult with a veterinarian or a dairy nutritionist for a tailored feeding plan and to address any potential health issues.",
            "Topic": "Animal production",
        },
        {
            "animal_crop": "Chicken",
            "Category": "Animal",
            "Language": "English",
            "Location": "Wakiso",
            "Prompts": "The chicken on my farm in Eastern Uganda typically get infected with coccidiosis in the first 3 to 6 weeks and then newcastle disease in the second month of their lives. What diseases should I look out for and when are they most likely to afflict my ducks in Wakiso?",
            "Bard Response": "Duck plague, duck hepatitis, and avian influenza are the most common diseases in ducks in Wakiso, Uganda. They are most likely to afflict young ducks in the first few months of their lives.",
            "Llama - 2 Response": "In Wakiso, Uganda, you should watch for Newcastle disease and Coccidiosis in your ducks. Newcastle disease is most likely to afflict ducks in the first two months of life, while coccidiosis can occur in the first three to six weeks.",
            "Bing response": "In Eastern Uganda, chickens are susceptible to coccidiosis and Newcastle disease. In Wakiso, ducks are prone to common diseases such as Duck Plague, Duck Cholera, Aflatoxicosis, Botulism, and Parasitic Diseases. Consult a veterinarian for diagnosis and treatment",
            "GPT 3.5 response": "In ducks reared in Wakiso, Uganda, watch out for:\n1. **Duck Plague (Duck Viral Enteritis):** Can affect ducks of all ages, causing high mortality.\n2. **Botulism:** More common in waterfowl; occurs when ducks consume contaminated water or feed.\n3. **Duck Cholera:** Can strike ducks, causing acute illness and death.\nPreventive measures include proper biosecurity, hygiene, vaccination (if available), and prompt veterinary care. Disease risks may vary based on local conditions and management practices.",
            "Topic": "Animal diseases, management and prevention",
        },
        {
            "animal_crop": "Sugarcane",
            "Category": "Crop",
            "Language": "Luganda",
            "Location": "Uganda",
            "Prompts": "Ebikajjo bikula bulungi nyo mukifo ekilimu entobazi. Mpa ensoga tanu lwaki kilibwekityo",
            "Bard Response": "I am still working to learn more languages, so I can't do that just yet. Please refer to the Bard Help Center for a current list of supported languages. Is there anything else you'd like my help with?",
            "Llama - 2 Response": "I can't satisfy your request, I'm just an AI and cannot engage in conversations that promote harmful or violent behavior.",
            "Bing response": "Nga omulimi, okuva mu kifo ekilimu entobazi, okuva ku mukajjo ogw’ensoga, oba okuva ku mukajjo ogw’ensoga, oba okuva ku mukajjo ogw’ensoga,",
            "GPT 3.5 response": "Ebikajjo bikula bulungi nyo mukifo ekilimu entobazi. Ensoga zibadde zilungi kubanga zigenda okulima ekirungi n'okusobola okuwangayo. N'okusasula ebintu ebirala ku mikajjo kikyali ekilwadde. So, mubangaiza ku bibadde byonna ku kifo ekilimu entobazi, ensoga zikibwekityo ezisobola okusangamu obulungi.",
            "Topic": "Soil health and properties",
        },
        {
            "animal_crop": "fish",
            "Category": "Animal",
            "Language": "Luganda",
            "Location": "Uganda",
            "Prompts": "Ngogyeko engege, emmale, nemamba, mputa ki omuluzi gyasobola okulunda ewaka mupondi ngevamu ssente?",
            "Bard Response": "I am still working to learn more languages, so I can't do that just yet. Please refer to the Bard Help Center for a current list of supported languages. Is there anything else you'd like my help with?",
            "Llama - 2 Response": "I apologize, but I cannot understand the message as it appears to be written in a made-up language. Could you please rephrase your question or message in proper English?",
            "Bing response": "Nga omulimi, okuva mu kifo ekilimu entobazi, okuva ku mukajjo ogw’ensoga, oba okuva ku mukajjo ogw’ensoga, oba okuva ku mukajjo ogw’ensoga,",
            "GPT 3.5 response": "Ngogyeko engege, emmale, nemamba, n'emputa bino byasobola okulunda ewaka mupondi ngevamu ssente nga bikola olw'okusasula, okubalibwa, n'okwetondera obulungi. Oluzi lw'obunengege n'obumamba buliwo obufuna amasente ag'ebiwuka bya munju n'ebigimusa bya mpale.",
            "Topic": "Aquaculture",
        },
        {
            "animal_crop": "Beans",
            "Category": "Crop",
            "Language": "Luganda",
            "Location": "Uganda",
            "Prompts": "Mweno sizoni yokulima, mirundi emeka gyentekedwa okukoola ebijanjalo byange okusobola okukakasa nti tebilibwa muddo?",
            "Bard Response": "I am still working to learn more languages, so I can't do that just yet. Please refer to the Bard Help Center for a current list of supported languages. Is there anything else you'd like my help with?",
            "Llama - 2 Response": 'Mweno sizoni yokulima, mirundi emeka gyentekedwa okukoola ebijanjalo byange okusobola okukakasa nti tebilibwa muddo? (What is the meaning of "Mweno sizoni yokulima" and how does it relate to "mirundi emeka gyentekedwa okukoola ebijanjalo byange okusobola okukakasa nti tebilibwa muddo"?)',
            "Bing response": "Okusobola okukakasa ebijanjalo byange mu sizoni yokulima, mirundi emeka gyentekedwa okukoola ebijanjalo byange okusobola okukakasa nti tebilibwa muddo. Naye okusobola okukakasa ebijanjalo byange mu sizoni yokulima, mirundi emeka gyentekedwa okukoola ebijanjalo byange okusobola okukakasa nti tebilibwa muddo kwe kugamba nti ebijanjalo byange byokka byokka byokka",
            "GPT 3.5 response": "Okulima n'okukoola ebijanjalo byange emeka gyentekedwa mu mweno sizoni kubanga bikakasa ebikolwa by'omulima, nkumira obujulirwa obulungi. Okukakasa kwekuba omulimu gw'obulimi gwokka ne gwenkanya obulimi obuwagirizibwa mu biro ebisembayo. Gyekakasa gy'omulimi gwogera obugwagwa n'ebirala ebirungi ebyokwerinda okubilwa mu muddo. Okusingawo ebisasi ebibadde byanyonyoosa ebikolwa byange bikakasa okuba obulungi obulala mu mweno sizoni.",
            "Topic": "Weed management",
        },
        {
            "animal_crop": "Sheep",
            "Category": "Animal",
            "Language": "English",
            "Location": "Northern Uganda",
            "Prompts": "What is the best sheep breed that can be reared in Northern Uganda?",
            "Bard Response": "The best sheep breed that can be reared in Northern Uganda is the Dorper sheep. The Dorper sheep is a hardy and drought-tolerant breed that is well-suited to the harsh conditions of Northern Uganda. Dorper sheep are also relatively fast-growing and have a good meat production potential.",
            "Llama - 2 Response": "The best sheep breed for Northern Uganda is the Karamajavi, which is well-suited to the region's climate and has high resistance to disease.",
            "Bing response": "The East African Blackhead, Karamojong, and Ethiopian hair sheep are suitable breeds for farming in Uganda. Each breed has unique characteristics, such as adaptability to local conditions, disease resistance, and meat or wool production capabilities",
            "GPT 3.5 response": "The Santa Ines sheep breed is a suitable choice for Northern Uganda due to its adaptability to hot climates, resistance to diseases, and efficient meat production. Its ability to thrive in challenging conditions makes it one of the best options for sheep farming in the region.",
            "Topic": "Animal/Livestock Selection",
        },
        {
            "animal_crop": "Coffee",
            "Category": "Crop",
            "Language": "English",
            "Location": "Busoga region",
            "Prompts": "A farmer in Busoga region used mancozeb to spray his coffee trees but it was not effective.what other pesticide can he use?",
            "Bard Response": "The farmer in Busoga region can try using copper oxychloride, Bordeaux mixture, chlorothalonil, propiconazole, or tebuconazole to control coffee leaf rust.\nIt is also important to note that the farmer should rotate the use of different pesticides to prevent resistance from developing in the coffee leaf rust fungus.",
            "Llama - 2 Response": "The farmer could try using copper oxychloride, which is a broad-spectrum fungicide that is effective against many coffee diseases, including rust and powdery mildew.",
            "Bing response": "If mancozeb was not effective, the farmer can consider using alternative fungicides such as copper-based fungicides (e.g., copper hydroxide, copper oxide) or combinations of dimethomorph, cymoxanil, fluazinam, zoxamide, and propamocarb 12. It’s important to consult local agricultural experts for specific recommendations based on the region and coffee variety.",
            "GPT 3.5 response": "Consider using a systemic pesticide like imidacloprid or pyrethroids after consulting with local agricultural experts.",
            "Topic": "Crop pest and disease management",
        },
        {
            "animal_crop": "Sweet Potato",
            "Category": "Crop",
            "Language": "Luganda",
            "Location": "Uganda",
            "Prompts": "Nsobola ntya okulwanyisa obulungi ebiwuka mu kulima lumonde?",
            "Bard Response": "I am still working to learn more languages, so I can't do that just yet. Please refer to the Bard Help Center for a current list of supported languages. Is there anything else you'd like my help with?",
            "Llama - 2 Response": "Sorry, I don't understand the question as it is written in a way that is difficult for me to comprehend. Could you please rephrase or provide more context?",
            "Bing response": "kusobola okukakasa ebijanjalo byange mu sizoni yokulima, mirundi emeka gyentekedwa okukoola ebijanjalo byange okusobola okukakasa nti tebilibwa muddo. Naye okusobola okukakasa ebijanjalo byange mu sizoni yokulima, mirundi emeka gyentekedwa okukoola ebijanjalo byange okusobola okukakasa nti tebilibwa muddo kwe kugamba nti ebijanjalo byange byokka byokka",
            "GPT 3.5 response": "Oyo lwanyisa obulungi ebiwuka mu kulima lumonde kye kisoboka ku byeru. Obukolwa obungi bwe butandisezza omuliro gwa bifa, ekirungi n'obukakati ku byeru, n'okuba n'obulungi obutaggwaawo. Wewaakana okugyako n'obubonero obukakati, era omulimi gwe gwakola kubasobya n'okuyamba.",
            "Topic": "Crop pest and disease management",
        },
        {
            "animal_crop": "Cattle",
            "Category": "Animal",
            "Language": "English",
            "Location": "Uganda",
            "Prompts": "What are the key factors to consider when selecting cattle breeds for milk production and meat quality?",
            "Bard Response": "Milk production: Genetic potential, milk yield, lactation length\nMeat quality: Carcass conformation, meat-to-bone ratio, marbling, tenderness\nAdaptability: Climate, feed conditions\nManagement requirements: Your own skills and resources",
            "Llama - 2 Response": "When selecting cattle breeds for milk production and meat quality, key factors to consider include:\n* Milk yield and fat content\n* Beef marbling and tenderness\n* Hardiness and disease resistance\n* Feed conversion efficiency\n* Adaptability to local climate and management practices.",
            "Bing response": "When selecting cattle breeds for milk production and meat quality, key factors to consider include: species, age, climate, birth weight, calving difficulty, milk production, growth rate, carcass fat, lean/bone ratio, age of puberty, and genetic and environmental determinants.",
            "GPT 3.5 response": "When selecting cattle breeds for milk production and meat quality, consider factors such as genetic potential for high milk yield and marbling for meat, adaptability to local conditions, disease resistance, and reproductive efficiency. Breeds like Holstein and Jersey are known for milk production, while Angus and Hereford are recognized for meat quality. Assessing these factors helps ensure optimal performance and sustainability in your chosen cattle breeds.",
            "Topic": "Animal/Livestock Selection",
        },
        {
            "animal_crop": "Sweet Potato",
            "Category": "Crop",
            "Language": "English",
            "Location": "Uganda",
            "Prompts": "What are the ideal storage conditions for sweet potatoes to maintain their quality and freshness?",
            "Bard Response": "Store sweet potatoes at 55-60°F (13-16°C) and 85-90% relative humidity in a dark place with good air circulation.",
            "Llama - 2 Response": "Sweet potatoes should be stored in a cool, dry place with good ventilation to maintain their quality and freshness. Ideal temperature range is between 50°F to 60°F (10°C to 15°C) and relative humidity of 70-80%.",
            "Bing response": "Sweet potatoes can maintain excellent quality for up to a year in proper storage conditions. The ideal storage conditions for sweet potatoes are moderately warm (55-60°F) at 60-75% relative humidity 1. Refrigeration is not recommended if you plan to consume them within a month or so",
            "GPT 3.5 response": "Ideal storage conditions for sweet potatoes include temperatures of around 55-60°F (13-15.5°C) and relative humidity levels of 85-90%. These conditions help prevent sprouting, maintain firmness, and prevent excessive moisture loss. Store sweet potatoes in a dark, well-ventilated area to avoid direct light exposure, which can cause them to develop a bitter taste.",
            "Topic": "Crop harvesting and post-harvest handling",
        },
        {
            "animal_crop": "Maize",
            "Category": "Crop",
            "Language": "English",
            "Location": "Western Uganda",
            "Prompts": "Which maize variant is more suitable for the climate in western Uganda.",
            "Bard Response": "The most suitable maize variant for the climate in western Uganda is the Longe 5 hybrid. It is a high-yielding variety that is tolerant to drought and pests. It is also relatively early maturing, which makes it ideal for the shorter growing season in western Uganda",
            "Llama - 2 Response": 'For western Uganda\'s climate, the most suitable maize variant would be the "West Africa Maize Variety" (WA-123), which performs well under drought conditions and has a shorter maturity period.',
            "Bing response": "The East African Blackhead, Karamojong, and Ethiopian hair sheep are suitable breeds for farming in Uganda. Each breed has unique characteristics, such as adaptability to local conditions, disease resistance, and meat or wool production capabilities",
            "GPT 3.5 response": "There is no single maize variant that can be considered more suitable for the entire climate in western Uganda, as the region has diverse climatic conditions. However, some maize varieties that are commonly grown in that area include the early-maturing maize variety known as Longe 5H, which is suitable for areas with short rainy seasons and limited access to irrigation. It is also recommended for high altitude areas and areas prone to drought. Another popular variety is Longe 6H, which is a medium-maturing variety suitable for areas with moderate rainfall and is known for its high yield potential. Other popular varieties in western Uganda include Dama and DKB 12. It is important for farmers to consult with their local agricultural extension officers to select the most suitable maize variety based on their specific location and climate conditions.",
            "Topic": "Crop selection and rotation",
        },
        {
            "animal_crop": "Maize",
            "Category": "Crop",
            "Language": "English",
            "Location": "Uganda",
            "Prompts": "What can I do to prevent maize streak virus in my garden?",
            "Bard Response": "Plant resistant maize varieties early in the season, control weeds, use reflective mulch, and monitor plants regularly.",
            "Llama - 2 Response": "To prevent maize streak virus in your garden, use resistant varieties, maintain good soil health, and monitor for signs of the virus early. Remove infected plants to prevent spread.",
            "Bing response": "Maize streak virus (MSV) is primarily transmitted by leafhoppers. To prevent the virus, avoid planting maize downwind, provide open areas for planting, minimize weeds that can harbor MSV vectors, and plant early to avoid optimal temperature for vector multiplication and subsequent transmission of the virus",
            "GPT 3.5 response": "1. Choose resistant varieties of maize. 2. Practice crop rotation to break the virus's life cycle. 3. Use certified virus-free seeds. 4. Keep garden and tools clean. 5. Monitor and remove infected plants immediately. 6. Use physical barriers like nets to prevent insect vectors. 7. Avoid planting maize near other plants that may harbor the virus. 8. Use insecticides or natural predators to control insect populations. 9. Avoid working in the garden when plants are wet to prevent spread of virus. 10. Seek advice from local agricultural extension services for specific prevention methods in your area.",
            "Topic": "Crop pest and disease management",
        },
        {
            "animal_crop": "Maize",
            "Category": "Crop",
            "Language": "Luganda",
            "Location": "Uganda",
            "Prompts": "Budde ki mu mwaka obusinga obulungi okulima kasooli?",
            "Bard Response": "I'm still learning languages, so at the moment I can't help you with this request. So far I've only been trained to understand the languages listed in the Bard Help Center.",
            "Llama - 2 Response": "Budde ki mu mwaka obusinga obulungi okulima kasooli? Mwana wa bbi.",
            "Bing response": "The best planting time for cassava is usually at the beginning of the rainy season. In regions with all-around rainfall, cassava cultivation can be carried out all year round. However, here in Uganda, the cultivation of cassava is in October when there is a short rainfal",
            "GPT 3.5 response": "Mwaka ogwo bagenda kulima kasooli. Bagitawaza mukwano n'obulungi obw'ekyama ne bagimba mubigambo bye byooyina bya ffe.",
            "Topic": "Planting and Sowing",
        },
        {
            "animal_crop": "Maize",
            "Category": "Crop",
            "Language": "English",
            "Location": "Uganda",
            "Prompts": "Is it good to intercrop maize?",
            "Bard Response": "Intercropping maize can increase yields, reduce risk, and improve soil health.",
            "Llama - 2 Response": "Intercropping maize can be beneficial as it can reduce pests and diseases, improve soil health, and increase crop yields.",
            "Bing response": "Maize-legume intercropping can assure higher yield, soil restoration, and greater impact of system productivity. The success of maize-legume intercropping system largely depends on choice of crops and their maturity, density, and time of planting 1. Other crops that can be intercropped with maize include beans, pumpkins, and sunflowers",
            "GPT 3.5 response": "Inter-cropping maize has several benefits such as increasing yields, reducing pest and disease pressure, improving soil health, and providing multiple sources of income from different crops. However, it requires careful planning and management to be successful.",
            "Topic": "Farm management",
        },
        {
            "animal_crop": "Bananas",
            "Category": "Crop",
            "Language": "Luganda",
            "Location": "Uganda",
            "Prompts": "Kilunji okusimba kasooli n'amatooke munimiro yemu?",
            "Bard Response": "I'm still learning languages, so at the moment I can't help you with this request. So far I've only been trained to understand the languages listed in the Bard Help Center.",
            "Llama - 2 Response": 'Amatooke omukulukulu, ku nga bakuluuka mu kikubo. Kisimbi ko nga bamudde mu kitaka." (Answer: The amatooke on the tree is too young to be eaten. It needs time to grow.)',
            "Bing response": "Kilunji okusimba kasooli kawuka kapya ak’omutawana era nga kukasooli kalya ebikoola, ebikongoliro wamu n’empeke zenyini. Engeri akasaanyi ennukuta ya Y kumutwe gyekonoonamu kasooli. Obusaanyi obulya kasooli buyinza n’okulumba ebirime ebilala ng’omuwemba, ebikajjo, omucere, obulo, omuddo, so nabyo bikebereko",
            "GPT 3.5 response": "Obudde akasooli n'amatooke munimiro baketuliza etteeka ly'okutuula ekyama oba kabiri y'okusimba. Okugenda e kitalo kuliwo eri bulyo bukakafunawo akabbiro. Egga nkusasula nga ensuga (30)",
            "Topic": "Farm management",
        },
        {
            "animal_crop": "Maize",
            "Category": "Crop",
            "Language": "English",
            "Location": "Uganda",
            "Prompts": "Kasooli is maize in Luganda. What are the best months of the year to plant kasooli in Uganda?",
            "Bard Response": "The best months of the year to plant kasooli in Uganda are March-April and August-September. These are the months when the rains are usually reliable and the weather is warm, which is ideal for maize germination and growth.However, it is important to note that the climate in Uganda can vary depending on the region. For example, the northern region has a single rainy season from April to July, while the southern region has two rainy seasons, from March to June and from August to November. Therefore, it is always best to consult with your local agricultural extension officer to find out the best time to plant kasooli in your area.",
            "Llama - 2 Response": "The best months to plant kasooli (maize) in Uganda are March to May and September to November, when the rains are adequate for growth and the soil is fertile.",
            "Bing response": "The best time to plant maize in Uganda depends on the region. In the Lake Victoria basin, eastern Uganda, mid-western, and southern parts of the country, the major rainy season in March is ideal for planting maize. However, planting can be done throughout the year in regions with all-around rainfall",
            "GPT 3.5 response": "The best months to plant kasooli in Uganda are March to May and September to October when the rainfall is consistent and temperature ranges between 25-30 degrees Celsius, providing optimal growing conditions for maize. It is important to also consider the soil nutrients and prepare the land before planting.",
            "Topic": "Planting and Sowing",
        },
        {
            "animal_crop": "Crop",
            "Category": "Crop",
            "Language": "English",
            "Location": "Wakiso",
            "Prompts": "Wakiso is a district in Central Uganda characterized by isolated flat-topped hills with steep slopes. What crop can thrive best in Wakiso?",
            "Bard Response": "Sweet potato is the best crop to grow in Wakiso district, Uganda, due to its drought-tolerance and deep root system. Other suitable crops include cassava, beans, maize, millet, sorghum, and vegetables.",
            "Llama - 2 Response": "Coffee is the ideal crop for Wakiso's hilly terrain, as it requires minimal flat land and benefits from the district's high altitude and moderate climate.",
            "Bing response": "Wakiso district in Central Uganda is characterized by isolated flat-topped hills with steep slopes. Maize is one of the fast-growing crops that farmers can grow as a coping strategy for drought. It takes about four to six months to mature depending on the variety",
            "GPT 3.5 response": "Coffee can thrive best in Wakiso district due to its hilly topography and well-drained soils. Coffee requires an altitude of 1000-2000 meters above sea level and moderate temperatures, which are suitable in Wakiso.\nThis crop also requires heavy rainfall and Wakiso receives an average annual rainfall of 1,400 mm, making it an ideal location for coffee production. Additionally, the district has well-established coffee processing facilities and a market for the crop, making it a profitable venture for farmers in the area.",
            "Topic": "Crop selection and rotation",
        },
        {
            "animal_crop": "Crop",
            "Category": "Crop",
            "Language": "Luganda",
            "Location": "Uganda",
            "Prompts": "Ebiseera bino kizibu abalimi okugobelela sizoni kuba zikyukakyuka. Ngeri ki omuntu gyayinza okutebereza obutafilwa mu kulima?",
            "Bard Response": "I'm still learning languages, so at the moment I can't help you with this request. So far I've only been trained to understand the languages listed in the Bard Help Center.",
            "Llama - 2 Response": 'Ebiseera bino kizibu abalimi okugobelela sizoni kuba zikyukakyuka. Ngeri ki omuntu gyayinza okutebereza obutafilwa mu kulima?"\nThis is a sentence in Kinyarwanda, the official language of Rwanda. It roughly translates to "The iron bar does not understand the talk of the birds.',
            "Bing response": "Okusobola okukakasa ebijanjalo byange mu sizoni yokulima, mirundi emeka gyentekedwa okukoola ebijanjalo byange okusobola okukakasa nti tebilibwa muddo. Naye okusobola okukakasa ebijanjalo byange mu sizoni yokulima, mirundi emeka gyentekedwa okukoola ebijanjalo byange okusobola okukakasa nti tebilibwa muddo kwe kugamba nti ebijanjalo byange byokka byokka byokka",
            "GPT 3.5 response": "Omuntu aterwa okutebereza obutafilwa mu kulima ne bubaka mu bulungi oba mu kiihwa. Ng'asaasira obutebereza obutaliibwa okukyukakyuka okuli ensi eno n'omulimu gw'okusalako ebisibo ebya kazi.",
            "Topic": "Weather and climate",
        },
        {
            "animal_crop": "Goats",
            "Category": "Animal",
            "Language": "English",
            "Location": "Uganda",
            "Prompts": "Is there a specific goat breed that thrives in the semi-arid areas in Uganda?",
            "Bard Response": "The Karamoja goat is a native breed of goat that thrives in the semi-arid areas of Uganda. They are hardy, drought-tolerant, and productive animals. They are also relatively easy to manage, making them a good choice for farmers in this region.",
            "Llama - 2 Response": "Yes, the Blackstar goat breed is well-suited for semi-arid areas in Uganda due to its hardiness and drought tolerance.",
            "Bing response": "The East African Blackhead, Karamojong, and Ethiopian hair sheep are suitable breeds for farming in Uganda. Each breed has unique characteristics, such as adaptability to local conditions, disease resistance, and meat or wool production capabilities",
            "GPT 3.5 response": "The Kenyan Alpine goat breed is well adapted to thrive in the semi-arid areas of Uganda due to its ability to withstand harsh climatic conditions, high temperatures, and low quality forage. It also has a high milk production potential, making it suitable for the region's dairy industry.",
            "Topic": "Animal/Livestock Selection",
        },
        {
            "animal_crop": "Crop",
            "Category": "Crop",
            "Language": "English",
            "Location": "Uganda",
            "Prompts": "There has been an increase in the number of seed companies registered from initially 7 in 2005 to currently > 44 in Uganda. What could be the reason for this?",
            "Bard Response": "There are a number of possible reasons for the increase in the number of seed companies registered in Uganda from 7 in 2005 to over 44 in 2023. These include:\nGovernment support: The Ugandan government has implemented a number of policies and programs to support the development of the seed sector, such as the National Seed Policy 2014 and the Seed Fund. Increased demand: There is a growing demand for certified seeds from farmers in Uganda, as they become more aware of the benefits of using high-quality seeds, such as increased yields and resistance to pests and diseases. Private sector investment: The private sector is increasingly investing in the seed sector in Uganda, as they see the potential for profit.Technological advancements: Advances in technology, such as the development of new seed varieties and breeding techniques, have made it easier and more profitable to produce and sell seeds.",
            "Llama - 2 Response": "The significant increase in seed companies in Uganda, from 7 in 2005 to over 44 today, can be attributed to several factors: increased government support and investment in agricultural development, growing demand for high-quality seeds from farmers, and the rise of private sector involvement in the agricultural industry. Additionally, improved access to finance and technology have made it easier for new entrants to enter the market.",
            "Bing response": "The increase in the number of seed companies registered in Uganda can be attributed to several factors. One of the reasons is the liberalization of the seed sector in the late 1990s, which allowed private seed companies to operate. Another factor contributing to the growth of the seed industry is climate variability and extremes. Additionally, the integrated seed sector development (ISSD) program in Uganda aims to create a vibrant, pluralistic, and market-oriented seed sector .",
            "GPT 3.5 response": "The increase in the number of seed companies in Uganda could be due to the growth in demand for quality seeds, government policies to promote agriculture and the entry of multinational companies into the market. Additionally, the rising population and changing consumer preferences towards healthier and more diverse food options could also be contributing factors.",
            "Topic": "Others",
        },
        {
            "animal_crop": "Goats",
            "Category": "Animal",
            "Language": "English",
            "Location": "Uganda",
            "Prompts": "Concentrates refer to animal feeds that are rich in energy and/or protein but low in fiber. What concentrates brand is the best for making goats grow faster in Uganda?",
            "Bard Response": "The best concentrate brand for making goats grow faster in Uganda depends on a number of factors, including the age and breed of the goats, the desired growth rate, and the availability and cost of different concentrates. However, some of the most popular and effective concentrate brands in Uganda include:\nUgachick Goat Concentrate\nAfrifeeds Goat Concentrate\nPearl Dairy Goat Concentrate\nNational Feeds Goat Concentrate\nBroilers and Layers Feeds Goat Concentrate\nThese concentrates are all high in energy and protein, and they contain a variety of other essential nutrients that goats need for optimal growth and development. They are also relatively affordable and easy to find in most parts of Uganda.",
            "Llama - 2 Response": "In Uganda, the best concentrate brand for making goats grow faster is likely to be a local or regional option, as transportation costs can make imported feeds less economical. Consider consulting with a local veterinarian or agricultural expert to determine the most appropriate feed for your specific needs and location.",
            "Bing response": "To ensure optimal growth of goats in Uganda, it is advisable to use concentrates that provide a balanced diet. While there isn’t a single “best” brand, some popular options include pig 25% concentrate and other premium concentrates1. These concentrates offer a balanced and healthy feed for goats, promoting growth and overall well-being. It’s important to consult local experts or veterinarians for specific recommendations based on your goat farming practices and requirements.",
            "GPT 3.5 response": "There are several brands of concentrates that are suitable for promoting fast growth in goats in Uganda, including Mazuri, Purina, and Wonder Grain. However, the best brand will depend on various factors such as availability, cost, and nutritional composition. It's important to consult with a local veterinarian or nutritionist to determine the best option for your specific herd and management practices.",
            "Topic": "Animal feeds and nutrition",
        },
        {
            "animal_crop": "Bananas",
            "Category": "Crop",
            "Language": "English",
            "Location": "Isingiro",
            "Prompts": "In Uganda, Rwenzori Mountains are known for leading coffee production in the country and Isingiro for matooke production. What district is known for maize production?",
            "Bard Response": "The district in Uganda that is known for maize production is Masindi. It is located in the Western Region of Uganda and is the largest maize producing district in the country, producing approximately 21,000 tonnes annually. Masindi has favorable climatic conditions for maize production, with well-distributed rainfall and fertile soils.\nOther districts in Uganda that are also known for maize production include:\nKapchorwa\nMbale\nKamuli\nJinja\nIganga\nMasaka\nMubende",
            "Llama - 2 Response": "In Uganda, maize production is prominent in Kamuli District",
            "Bing response": "In Uganda, the district known for maize production is Buganda north. It leads in maize cultivation, followed by Bunyoro and Buganda south1. Maize is the most important cereal crop in Uganda, providing over 40% of the calories consumed in both rural and urban areas2. Small-scale farmers, who constitute the bulk of the rural poor, account for the largest share of maize production2. Other prominent areas where maize is planted include Kapchorwa, Iganga, Masindi, Mbale, Mubende, Kasese, Kamuli, Jinja, and Kabarole district",
            "GPT 3.5 response": "Namayingo district is known for maize production in Uganda. Located in the eastern region, this district is home to the Kibimba and Kazinga maize seed production farms, which supply quality maize seeds to farmers across the country. The favorable climate and fertile soils in Namayingo make it a prime location for growing maize, and the district is a major contributor to Uganda's overall maize production. In addition, Namayingo hosts annual maize festivals and has several government programs in place to support and promote maize farming in the district.",
            "Topic": "Crop markets, products and prices",
        },
        {
            "animal_crop": "Bananas",
            "Category": "Crop",
            "Language": "English",
            "Location": "Uganda",
            "Prompts": "Matooke (also known as matoke or ibitoke) is a type of cooking banana commonly consumed in Uganda and other parts of East Africa. For value addition, milk can be used for cheese and coffee seeds for coffee powder. What can I do with maize?",
            "Bard Response": "Process it into food products: e.g., maize flour, maize meal, maize grits, maize starch, maize oil, maize gluten, maize bran, maize snacks, maize breakfast cereals, and maize baby food.\nUse it to make animal feed: Maize is a valuable ingredient in animal feed, and it can be used to feed a variety of animals, including pigs, chickens, and cattle.\nUse it to make biofuels: Maize can be used to produce biofuels, such as ethanol and biodiesel.\nUse it to make industrial products: Maize can be used to make a variety of industrial products, such as bioplastics, adhesives, and pharmaceuticals.",
            "Llama - 2 Response": "With maize, you can make cornmeal, porridge, polenta, tamales, and tortillas. You can also use it for animal feed or produce ethanol. Additionally, you can process it into hominy, grits, or corn flour for baking.",
            "Bing response": "Maize, also known as corn, is a versatile crop with many uses. It is used as livestock feed, human food, biofuel, and raw material in industry 1. In Uganda, maize is the most important cereal crop, providing over 40% of the calories consumed in both rural and urban areas 1. Some popular uses of maize include making cornmeal, masa, corn oil, corn starch, and corn syrup 1. Maize can also be used to make alcoholic beverages like bourbon whiskey, and other biofuels",
            "GPT 3.5 response": "Maize, also known as corn, can be used in a variety of dishes. It can be ground into flour and used to make cornbread, tortillas, or porridge. It can also be popped into popcorn, added to soups and stews, or used in salads and side dishes. Additionally, maize can be used to make sweet treats like corn pudding, corn fritters, and cornbread muffins. It can also be turned into maize flour for gluten-free baking. Maize can also be fed to livestock as animal feed.",
            "Topic": "Crop markets, products and prices",
        },
        {
            "animal_crop": "Cocoa",
            "Category": "Crop",
            "Language": "English",
            "Location": "Uganda",
            "Prompts": "Cocoa takes 3-5 years to produce its first seed pod, and coffee takes an average of 3 years. How long does maize take?",
            "Bard Response": "Maize takes 60-100 days to produce its first seed. This is significantly shorter than the time it takes for cocoa and coffee to produce their first seeds.\nMaize is a fast-growing crop that can be planted multiple times per year in tropical and subtropical climates. It is a staple food crop in many parts of the world and is also used to make a variety of other products, such as animal feed, biofuels, and industrial products.",
            "Llama - 2 Response": "Maize takes approximately 6 months to mature after planting, so it is much faster than cocoa or coffee.",
            "Bing response": "Maize, also known as corn, has a growth period that varies depending on the variety and environmental conditions. On average, maize takes around 12-17 days to emerge from the soil after sowing 1. The growth stages of maize include emergence, weaning, initiation of ears, tassel visible, female flowering, grain abortion limit, doughy grain, and black layer 1. The entire growth cycle of maize, from sowing to maturity, typically takes around 3-4 months 1. However, it’s important to note that specific growth periods can vary based on factors such as temperature, soil conditions, and the maize variety being cultivated",
            "GPT 3.5 response": "Maize, also known as corn, typically takes about 80-120 days to produce its first ear of corn, which can then be harvested for consumption or used for animal feed. However, the exact time frame can vary depending on the variety and growing conditions. Maize has a variety of uses, including being a staple food in many cultures, used for making cornmeal or flour, used as animal feed, and even used for producing biofuels. Additionally, maize is a versatile crop and can be used to make products such as corn starch, corn syrup, and ethanol.",
            "Topic": "Crop harvesting and post-harvest handling",
        },
        {
            "animal_crop": "Maize",
            "Category": "Crop",
            "Language": "English",
            "Location": "Sembabule",
            "Prompts": "Kanyogoga is a village in Mawogola county in Sembabule district. The county is part of the cattle corridor in Uganda and is characterized by long dry spells. What are the best months of the year to plant maize in Kanyogoga?",
            "Bard Response": "The best months of the year to plant maize in Kanyogoga are March to May and September to November. These months have the most rainfall, which is essential for maize growth.\nThe long dry spells in Mawogola county make it difficult to grow maize during other months of the year. However, by planting maize during the rainy season, farmers can ensure that their crops have enough water to grow and produce a good yield.\nHere are some additional tips for planting maize in Kanyogoga:\nChoose a well-drained site with full sun.\nPrepare the soil by adding manure or compost.\nPlant the maize seeds 1-2 inches deep and 6-8 inches apart.\nWater the maize plants regularly, especially during the first few weeks after planting.\nFertilize the maize plants every 2-3 weeks with a balanced fertilizer.\nHarvest the maize when the ears are fully mature and the kernels are dry and hard",
            "Llama - 2 Response": "The best months to plant maize in Kanyogoga, Uganda's cattle corridor, are March to May (rainy season) for optimal growth and yield.",
            "Bing response": "",
            "GPT 3.5 response": "The best months to plant maize in Kanyogoga in Mawogola county are between March and May. During this time, there is enough rainfall and the soil is moist enough to support germination and growth of maize. Planting during these months also allows for the maize to mature before the onset of the long dry spells in July, ensuring a good harvest. However, farmers can also opt to plant maize in August or September, depending on the amount of rainfall received.",
            "Topic": "Planting and Sowing",
        },
        {
            "animal_crop": "Goats",
            "Category": "Animal",
            "Language": "English",
            "Location": "Wakiso",
            "Prompts": "I have not done goat farming before but I want to venture into this in my hometown in Kakiri which is in Wakiso district. From what I have heard, goat farming is cheaper than dairy farming because they are relatively smaller and have fewer feeding and space requirements. How would i distribute 1 million Uganda shillings to start a relatively small goat farm? Summarize in 150 words",
            "Bard Response": "Here is a possible way to distribute 1 million Uganda shillings to start a relatively small goat farm in Kakiri, Wakiso district:\nPurchase goats: 4 goats @ 200,000 UGX each = 800,000 UGX\nBuild a goat house: 100,000 UGX\nPurchase feeding troughs and water troughs: 50,000 UGX\nPurchase goat feed: 100,000 UGX\nVeterinary care and other expenses: 50,000 UGX\nTotal: 1,000,000 UGX\nSummary: 800,000 UGX for goats, 100,000 UGX for a goat house, 50,000 UGX for feeding and water troughs, 100,000 UGX for goat feed, and 50,000 UGX for veterinary care and other expenses. It is important to note that this is just a suggested budget, and the actual costs may vary depending on the specific needs of your farm. It is also important to do your research and learn as much as you can about goat farming before starting your own farm.",
            "Llama - 2 Response": "Here's a summary of how you could distribute 1 million UGX to start a small goat farm in Kakiri, Wakiso district:\n* Purchase 10-20 goats at an average cost of 50,000 UGX per goat = 500,000 - 1,000,000 UGX (50% of the budget)\n* Build or lease a modest goat shed with feeding and space requirements for the goats = 200,000 - 300,000 UGX (20% of the budget)\n* Purchase feed and supplies for the first few months = 150,000 - 200,000 UGX (15% of the budget)\n* Hire a part-time worker to assist with caring for the goats = 100,000 - 150,000 UGX (10% of the budget)\nTotal distribution: 1,050,000 - 1,450,000 UGX.",
            "Bing response": "In Kanyogoga, located in Sembabule district, Uganda, the best months to plant maize are March and August. These months coincide with the onset of the rainy seasons, which are typically from March to June and August to December. Maize takes around 12-17 days to emerge from the soil after sowing, and the entire growth cycle, from sowing to maturity, typically takes around 3-4 months. However, specific growth periods can vary based on factors such as temperature, soil conditions, and the maize variety being cultivated",
            "GPT 3.5 response": "To start a relatively small goat farm with 1 million Uganda shillings, you should allocate your budget wisely. It is important to invest in good quality goats, so allocate a significant portion of your budget towards purchasing healthy and productive breeds. The remaining funds can be used for constructing basic shelters, purchasing feed and water troughs, and other necessary equipment. You could also set aside some money for initial veterinary costs and marketing your goat products. And as the business grows, you can reinvest profits to expand and improve your goat farm.",
            "Topic": "Animal production",
        },
        {
            "animal_crop": "Goats",
            "Category": "Animal",
            "Language": "English",
            "Location": "Uganda",
            "Prompts": "How much profit margin can i get in goat farming and after hoelong should i expect profits? Summarize in 100 word",
            "Bard Response": "The profit margin in goat farming can vary depending on a number of factors, including the size and type of goat farm, the quality of the goats, the cost of feed and other inputs, and the market price of goats and goat products. However, a well-managed goat farm can typically generate a profit margin of 20-30%.\nYou can expect to start seeing profits from your goat farm within 1-2 years of starting. This is because goats are relatively fast-growing animals and can start breeding at a young age. However, it is important to note that the profitability of your goat farm will depend on a number of factors, such as the quality of your management and the market conditions.",
            "Llama - 2 Response": "Goat farming can offer a profit margin of around 20-30% per year, depending on factors such as breed selection, feed costs, and market demand. Profits may take several months to a year or two to materialize, depending on the size and scope of your operation.",
            "Bing response": "To start a small goat farm in Kakiri, Wakiso district, with a budget of 1 million Uganda shillings, you can allocate the funds as follows: 30% of the budget (300,000 UGX) for constructing goat pens, feeding troughs, and water sources. 50% of the budget (500,000 UGX) to purchase healthy and productive goats from reputable breeders. 10% of the budget (100,000 UGX) for purchasing quality feed, supplements, and vaccines. The remaining 10% (100,000 UGX) for miscellaneous expenses such as transportation, labor, and contingency costs. Remember to consult local experts or veterinarians for specific guidance on goat farming practices and requirements in your area",
            "GPT 3.5 response": "The profit margin in goat farming can vary depending on various factors such as location, market demand, management practices, and breed of goats. Generally, a profit margin of 30-40% can be expected in goat farming. This means that for every $100 invested, a farmer can expect to earn a profit of $30-$40. However, this can take time to achieve as goats are slow-maturing animals and it can take up to 2-3 years to see profits. It is important to have a well-planned business strategy, maintain good herd management, and have a strong market for your products to achieve maximum profits in goat farming.",
            "Topic": "Animal marketing",
        },
        {
            "animal_crop": "Sheep",
            "Category": "Animal",
            "Language": "English",
            "Location": "Uganda",
            "Prompts": "My lambs have excessive diarrhea, abdominal comfort, and loss of appetite. Could this be a problem with the feeds I am giving them?",
            "Bard Response": "It is possible that your lambs' symptoms are caused by a problem with the feeds you are giving them. Some common causes of diarrhea, abdominal discomfort, and loss of appetite in lambs include:\nOverfeeding: Overfeeding can cause lambs to eat too much of a particular feed, which can lead to digestive problems.\nPoor quality feed: Poor quality feed may contain toxins or other harmful substances that can cause digestive problems in lambs.\nSudden changes in diet: Sudden changes in diet can upset lambs' digestive systems and cause diarrhea and other problems.\nIf you suspect that your lambs' symptoms are caused by a problem with their feed, you should consult with a veterinarian or animal nutritionist. They can help you identify the problem and develop a feeding plan that is appropriate for your lambs' needs.",
            "Llama - 2 Response": "Yes, it could be related to the feed. Lambs are sensitive to nutrient imbalances or contaminants in their diet. Consider consulting a veterinarian or a qualified animal nutritionist to evaluate the nutritional adequacy of your lambs' feed",
            "Bing response": "",
            "GPT 3.5 response": "Excessive diarrhea, abdominal discomfort, and loss of appetite are all symptoms that could indicate a problem with the feeds you are giving your lambs. It is important to make sure the feeds you are providing are of good quality and balanced for their nutritional needs. Poor quality or contaminated feeds can lead to digestive issues and other health problems in lambs. It is also important to monitor their feed intake and make any necessary adjustments to prevent overfeeding or underfeeding. Consult with a veterinarian or nutritionist to identify any potential issues with your lamb's diet and make appropriate changes.",
            "Topic": "Animal diseases, management and prevention",
        },
        {
            "animal_crop": "Goats",
            "Category": "Animal",
            "Language": "English",
            "Location": "Uganda",
            "Prompts": "Under normal circumstances, It costs Shs.72,000 ($20) to raise a goat a year and it attains slaughter weight in 8 months & fetches Shs.120,000 ($32). If a female goat produces 1.8 goats per year on average and I start a farm with 4 female goats and 1 male goat, how much will I have made after 3 years? Please respond step by step",
            "Bard Response": "Step 1: Calculate the total cost of raising the goats for 3 years.\n4 female goats * 3 years * Shs.72,000/year = Shs.864,000\nStep 2: Calculate the total revenue from selling the goats after 3 years.\n(4 female goats + 4 female goats * 1.8 * 2 years + 4 female goats * 1.8 * 1.8 years * 3 years) * Shs.120,000/goat = Shs.3,775,200\nStep 3: Calculate the total profit from the goat farm after 3 years.\nShs.3,775,200 - Shs.864,000 = Shs.2,911,200\nTherefore, you will have made Shs.2,911,200 after 3 years of goat farming.",
            "Llama - 2 Response": "Here's the calculation:\nYear 1:\n* 4 female goats x $20 each = $80 per year (for females)\n* 1 male goat x $20 = $20 per year (for male)\n* Total income = $80 + $20 = $100 per year\nYear 2:\n* Same as Year 1: $80 (females) + $20 (male) = $100 per year\nYear 3:\n* By year 3, the original 4 female goats would have produced 4 x 1.8 = 7.2 kids (on average), so we have 4 x $20 = $80 from the females, plus $20 from the male, for a total of $100 + $20 = $120 per year.\nTotal income over 3 years:\n$100 + $100 + $120 = $320\nSo, after three years, you would have made a total of $320.",
            "Bing response": "To calculate the earnings from your goat farm after 3 years, we need to consider the growth and reproduction rates. Assuming you start with 4 female goats and 1 male goat, the number of goats will increase over time.\nIn the first year, each female goat produces 1.8 goats, resulting in a total of 7.2 goats (4 females + 1 male + 1.8 * 4).\nIn the second year, each female goat produces another 1.8 goats, resulting in a total of 12.96 goats (7.2 + 1.8 * 7.2).\nIn the third year, each female goat produces another 1.8 goats, resulting in a total of 23.328 goats (12.96 + 1.8 * 12.96).\nConsidering the selling price of Shs.120,000 per goat, your total earnings after 3 years would be Shs.2,799,360 (23.328 * Shs.120,000).\nPlease note that this calculation assumes no goats are sold or lost during the 3-year period and that the reproduction rate remains constant1.",
            "GPT 3.5 response": "In the first year, the 4 female goats will produce a total of 7.2 goats (4 x 1.8). If we subtract the cost of raising each goat, which is Shs.72,000, the net profit for the first year would be Shs.374,400 (7.2 x Shs.120,000 – 4 x Shs.72,000). In the second year, the 4 female goats would each produce 1.8 goats, resulting in a total of 12.96 goats (7.2 x 1.8). Again, after subtracting the cost of raising each goat, the net profit would be Shs.842,880 (12.96 x Shs.120,000 – 4 x Shs.72,000). In the third year, the 4 female goats would produce a total of 23.33 goats (12.96 x 1.8). The net profit for the third year would be Shs.1,520,960 (23.33 x Shs.120,000 – 4 x Shs.72,000). Therefore, after 3 years, the total net profit would be Shs.2,738",
            "Topic": "Animal marketing",
        },
        {
            "animal_crop": "Goats",
            "Category": "Animal",
            "Language": "English",
            "Location": "Central Uganda",
            "Prompts": "In Uganda, the commonest breeds of goats reared are the East African Goats, the Kigezi breed, and the Mubende breed. Which one would be the best to rare in Mukono, a district in central Uganda?",
            "Bard Response": "The East African Goat is the best breed to rear in Mukono, a district in central Uganda. It is a hardy and adaptable breed that is well-suited to the climatic conditions in Mukono. It is also a relatively fast-growing breed, and it produces good quality meat and milk.",
            "Llama - 2 Response": "Of the three breeds you mentioned, the East African Goat is the best choice for raising in Mukono, central Uganda. This breed is well-suited to the local climate and has a high resistance to diseases, making it a reliable and productive choice for farmers.",
            "Bing response": "In Mukono, a district in central Uganda, the Mubende goat breed is highly recommended for rearing due to its growth potential and readily available market1. The Kigezi breed is of intermediate size, while the East African Goats are mainly reared in West Nile and Eastern Uganda1. Consult local experts for specific guidance based on your farming practices and requirements",
            "GPT 3.5 response": "The best breed of goat to rear in Mukono, a district in central Uganda, would be the East African Goat. This breed is well adapted to the climate and environment of Uganda, making it low maintenance and easy to rear. The East African Goat is also known for its high fertility and milk production, making it a good source of income through both meat and dairy products. Additionally, this breed is resistant to common diseases found in Uganda, making it a more reliable choice for farmers in Mukono. It is also a good choice for crossbreeding with other breeds to improve their production capabilities. Overall, the East African Goat is the most suitable breed for Mukono as it is well adapted to the local conditions, has high productivity potential, and is low maintenance.",
            "Topic": "Animal/Livestock Selection",
        },
        {
            "animal_crop": "Goats",
            "Category": "Animal",
            "Language": "English",
            "Location": "Uganda",
            "Prompts": "What suppliments on the Ugandan market can i add to my goat feeds to make the goats grow bigger and faster?",
            "Bard Response": "The following supplements on the Ugandan market can be added to goat feeds to make the goats grow bigger and faster:\nCottonseed cake\nSoybean meal\nSunflower seed cake\nMineral and vitamin mix\nThese supplements are rich in protein, energy, and other essential nutrients that goats need for optimal growth and development. They can be added to goat feed at a rate of 10-15% of the total diet.\nIt is important to note that the best way to choose supplements for your goats is to consult with a veterinarian or animal nutritionist. They can help you assess the needs of your goats and recommend supplements that are right for them.",
            "Llama - 2 Response": "As a nutritionist, I would advise against adding any supplements to your goat's feed without proper consultation with a veterinarian or animal nutrition expert. Goats have specific nutrient requirements that must be met through a balanced diet of high-quality hay, grains, and minerals. Adding untested supplements could lead to negative health consequences for your goats. Instead, focus on providing clean water, adequate shelter, and regular veterinary care to ensure optimal health and growth.",
            "Bing response": "To make goats grow bigger and faster in Uganda, you can add supplements that provide a balanced diet. Some popular options include protein and fat supplements like Purina® Goat Grower-Finisher 14 with Lambitine™, which can help improve appetite, rate of gain, and efficient cost of gain 1. Additionally, providing adequate dietary protein and energy, along with high-quality forages, can help maximize weight gain and efficient conversion of feed to gain",
            "GPT 3.5 response": "Some supplements that are commonly used by goat farmers in Uganda to help their goats grow bigger and faster include:\n1. Mineral supplements like calcium, phosphorus, and selenium.\n2. Protein supplements like soybean meal or crushed cottonseed cake.\n3. Vitamin supplements like Vitamin A, D, and E.\n4. Probiotics for better digestion and immunity.\n5. Wormers to control internal parasites.\nIt is always important to consult with a veterinarian before adding any supplements to your goat's feed to ensure proper dosage and effectiveness.",
            "Topic": "Animal feeds and nutrition",
        },
        {
            "animal_crop": "Maize",
            "Category": "Crop",
            "Language": "English",
            "Location": "Uganda",
            "Prompts": "The minimum plant population for maize is 36,000 plants per ha. A seed rate of about 25 kg/ha is required, but this depends on the seed size. 10 kg is enough to plant 1 acre and 5 kg for half an acre. How much would be enough for 4.5 acres? What is the first step to solving this?",
            "Bard Response": "The first step to solving this problem is to convert the 4.5 acres to hectares. There are 0.4047 hectares in 1 acre, so 4.5 acres is equal to 4.5 * 0.4047 = 1.82 hectares.\nTo calculate the amount of seed needed for 1.82 hectares, we can use the following formula:\nSeed rate (kg/ha) * Area (ha) = Amount of seed needed (kg)\nTherefore, the amount of seed needed for 1.82 hectares is:\n25 kg/ha * 1.82 ha = 45.5 kg\nTherefore, we would need 45.5 kg of seed to plant 4.5 acres of maize.",
            "Llama - 2 Response": "Here's the information you requested, limited to 100 words or less:\nFor 4.5 acres, you'll need approximately 45 kg of maize seeds, assuming a seed size of 250 grams per 1000 seeds. This amount is based on a seed rate of 25 kg/ha, which is suitable for optimal growth and yields. First step: Determine the exact seed size and adjust the quantity accordingly.",
            "Bing response": "To calculate the amount of maize seeds needed for 4.5 acres, we can use the information provided. For 1 acre, 10 kg of seeds are required. Therefore, for 4.5 acres, we can multiply 10 kg by 4.5, resulting in 45 kg of seeds. The first step to solving this is to determine the seed rate per acre and then multiply it by the number of acres. In this case, the seed rate is 10 kg per acre, so 10 kg * 4.5 acres = 45 kg of seeds are needed.",
            "GPT 3.5 response": "The first step to solving this problem would be to calculate the total amount of seed needed for 4.5 acres. To do this, we can use the ratio of 1 acre to 10 kg of seed. This would mean that 4.5 acres would require 45 kg (10 kg x 4.5 acres) of seed. However, since the recommended seed rate is 25 kg/ha, we will need to adjust the amount accordingly. This means that for 4.5 acres, we would need approximately 112.5 kg (25 kg/ha x 4.5 acres) of seed.",
            "Topic": "Crop harvesting and post-harvest handling",
        },
        {
            "animal_crop": "Maize",
            "Category": "Crop",
            "Language": "English",
            "Location": "Uganda",
            "Prompts": "You have a 50-lb bag of 26-5-10 fertilizer that you want to apply to a lawn at a rate of 1.0 lb nitrogen per 1000 sq ft. How much of the 26-5-10 fertilizer will you need to apply per 1000 sq ft?",
            "Bard Response": "To calculate how much of the 26-5-10 fertilizer you will need to apply per 1000 sq ft to achieve a rate of 1.0 lb nitrogen per 1000 sq ft, we can use the following formula:\nAmount of fertilizer (lb) = Desired rate of nitrogen (lb/1000 sq ft) / Nitrogen content of fertilizer (%)\nThe nitrogen content of the 26-5-10 fertilizer is 26%, so:\nAmount of fertilizer (lb) = 1.0 lb/1000 sq ft / 0.26 = 3.846 lb/1000 sq ft\nTherefore, you will need to apply 3.846 lb of the 26-5-10 fertilizer per 1000 sq ft to achieve a rate of 1.0 lb nitrogen per 1000 sq ft.",
            "Llama - 2 Response": "Here's the calculation:\nnitrogen content in 26-5-10 fertilizer = 26% x 1000 / 100 = 260 lbs/acre\nSo, to apply 1.0 lb nitrogen per 1000 sq ft, you would need to apply:\n260 lbs/acre x 1000 sq ft / acre = 260 lbs per 1000 sq ft",
            "Bing response": "To determine the amount of 26-5-10 fertilizer you need to apply per 1000 sq ft, you can use the following calculation: Divide the desired nitrogen amount (1.0 lb) by the percentage of nitrogen in the fertilizer (26%). The result is approximately 3.8 lb of the 26-5-10 fertilizer needed to supply 1.0 lb of nitrogen per 1000 sq ft1. Please note that this calculation assumes the weight of the fertilizer bag is not considered.",
            "GPT 3.5 response": "To calculate how much of the 26-5-10 fertilizer you will need to apply per 1000 sq ft, you first need to determine how much nitrogen is in each bag. The first number in the fertilizer analysis, 26, represents the percentage of nitrogen in the bag. So 50 lbs x 0.26 (26%) = 13 lbs of nitrogen in the bag. To apply 1.0 lb of nitrogen per 1000 sq ft, you will need to apply 13 lbs of fertilizer per 1000 sq ft. This equates to approximately 2.5 lbs of the 26-5-10 fertilizer per 100 sq ft.",
            "Topic": "Fertilization",
        },
        {
            "animal_crop": "Cassava",
            "Category": "Crop",
            "Language": "English",
            "Location": "Rukungiri",
            "Prompts": "One of the symptoms of Cassava Brown Streak Disease is the brown streaks that appear on young green steams. Discuss the different stages of this disease, and the symptoms that occur on each stage that farmers in Rukungiri  should be aware of",
            "Bard Response": "Cassava brown streak disease has 3 stages:\nEarly stage: Brown streaks on young green stems.\nIntermediate stage: Yellow blotchy chlorosis on lower leaves, brown streaks on older stems.\nAdvanced stage: Leaf necrosis, tuber rot, plant death.\nFarmers should be aware of all stages to identify and manage the disease early.",
            "Llama - 2 Response": "Cassava Brown Streak Disease has several stages with distinct symptoms. In the early stages, brown streaks appear on young green stems, followed by yellowing and wilting of leaves. As the disease progresses, the streaks become darker and more pronounced, and the leaves may drop off completely. Farmers in Rukungiri should monitor their crops for these early signs of the disease to prevent widespread damage.",
            "Bing response": "Cassava Brown Streak Disease (CBSD) is characterized by severe chlorosis and necrosis on infected leaves, giving them a yellowish, mottled appearance. Brown streaks may appear on the stems of the cassava plant. The roots can become constricted due to the tuber rot, stunting growth. Farmers may be unaware of their infected cassava crops until they are harvested and see the tuber lesions because leaves are asymptomatic",
            "GPT 3.5 response": "Cassava Brown Streak Disease (CBSD) progresses through three stages: initial, foliar, and root stages. In the initial stage, symptoms are subtle, including yellowing patches on leaves. The foliar stage shows brown streaks or patches on leaves, along with leaf distortion and mosaic patterns. The root stage affects roots with brown streaks, stunting, and reduced starch content. Rukungiri  farmers should monitor for these symptoms and implement management strategies with disease-free planting material and resistant varieties. Local agricultural extension services can provide further guidance.",
            "Topic": "Crop pest and disease management",
        },
        {
            "animal_crop": "Cabbage",
            "Category": "Crop",
            "Language": "English",
            "Location": "Kigezi",
            "Prompts": "through terraccing and mulching, cabbagge farmers in Kigezi  highlands  prevent \nsoil erosion on the cabbagge farms , which other methods can cabbagge farmers in Kigezi \nuse to control soil ersion?",
            "Bard Response": "Cabbage farmers in Kigezi can also use contour farming, strip cropping, and cover crops to control soil erosion.",
            "Llama - 2 Response": "Cabbage farmers in Kigezi highlands can use contour farming, agroforestry, and cover cropping to control soil erosion. These methods help reduce water runoff, retain soil moisture, and stabilize soil hillsides.",
            "Bing response": "In addition to terracing and mulching, cabbage farmers in Kigezi highlands can use contour plowing and cover cropping to control soil erosion",
            "GPT 3.5 response": "In addition to terracing and mulching, cabbage farmers in the Kigezi  highlands can utilize cover cropping with leguminous plants to stabilize\n  soil, establish vegetative barriers like hedgerows to break the flow of water, and implement agroforestry practices to provide natural erosion\n  control. Incorporating contour planting and strip cropping can further reduce soil erosion, while adopting no-till or reduced tillage techniques\n  minimizes soil disturbance. Proper drainage systems and constructing check dams can also effectively manage water runoff and erosion,\n  ensuring sustainable cabbage cultivation while protecting the soil from erosion.",
            "Topic": "Farm management",
        },
    ]

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
