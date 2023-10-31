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
import random
import os
from os.path import join, dirname, realpath


from sqlalchemy import func, or_, and_
from app.helper import admin_required

UPLOADS_PATH = join(dirname(realpath(__file__)), "static/audio_uploads")

questions = Blueprint("questions", __name__, url_prefix="/api/v1/questions")


def format_question(question, language):
	return {
		"id": question.id,
		"sentence": question.sentence,
		"language": question.language,
		"created_at": question.created_at.strftime("%Y-%m-%d %H:%M:%S"),
		"topics": question.topic,
		"sub_topic": question.sub_topic,
		"category": question.category,
		"animal_crop": question.animal_crop,
		"location": question.location,
		"question_language": language,
		"filename": question.filename,
	}

def jsonify_question(question):
	return {
		"id": question.id,
		"sentence": question.sentence,
		"language": question.language,
		"created_at": question.created_at.strftime("%Y-%m-%d %H:%M:%S"),
		"topics": question.topic,
		"sub_topic": question.sub_topic,
		"category": question.category,
		"animal_crop": question.animal_crop,
		"location": question.location,
		"filename": question.filename,
		"reviewed": question.reviewed,
		"answered": question.answered
	}

@questions.route("/", methods=["POST", "GET"])
@jwt_required()
def handle_questions():
	def process_single_question(question_data, current_user):
		sentence = question_data.get("sentence", "")
		language = question_data.get("language", "")
		topic = question_data.get("topic", "")
		sub_topic = question_data.get("sub_topics", "")
		category = question_data.get("category", "")
		animal_crop = question_data.get("sub_category", "")
		location = question_data.get("location", "")
		today = datetime.date.today()

		if language not in ["English", "Luganda", "Runyankole"]:
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
				sub_topic=sub_topic,
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
						"sub_topic": question.sub_topic,
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

		if isinstance(data, list): 
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
						"sub_topic": question.sub_topic,
						"category": question.category,
						"animal_crop": question.animal_crop,
						"location": question.location,
					}
				)

			return jsonify(returned_data), HTTP_200_OK
		else:
			return jsonify({"error": "User not found"}), HTTP_404_NOT_FOUND


@questions.route("/upload_question", methods=["POST"])
@jwt_required()
def upload_question():
	if "audio" not in request.files:
		return jsonify({"error": "No audio file provided"}), HTTP_400_BAD_REQUEST

	language = request.form.get("language")
	topic = request.form.get("topic", "")
	sub_topic = request.form.get("sub_topics", "")
	category = request.form.get("category", "")
	animal_crop = request.form.get("sub_category", "")
	location = request.form.get("location", "")

	audio = request.files["audio"]

	if audio:
		filename = os.path.join("static", "audio_uploads", audio.filename)
		if os.path.exists(filename):
			return jsonify({"Error": "File with same name already exists"})
		audio.save(filename)

	current_user = get_jwt_identity()
	question = Question(
		language=language,
		user_id=current_user,
		topic=topic,
		sub_topic=sub_topic,
		filename=filename,
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
				"sub_topic": question.sub_topic,
				"category": question.category,
				"animal_crop": question.animal_crop,
				"location": question.location,
				"filename": question.filename
			}
		)

	return {
		"num_questions": num_questions,
		"questions": todaysQuestions,
	}, HTTP_201_CREATED


@questions.route("/offline_upload", methods=["POST"])
@jwt_required()
def offline_upload():
	if "file" not in request.files:
		return jsonify({"error": "No metadata file provided"}), HTTP_400_BAD_REQUEST

	if "files" not in request.files:
		return jsonify({"error": "No audio files provided"}), HTTP_400_BAD_REQUEST

	metadata_file = request.files.get("file")
	audio_files = request.files.getlist("files")

	metadata = json.loads(metadata_file.read().decode("utf-8"))

	if not audio_files:
		return jsonify({"error": "No audio files provided"}), HTTP_400_BAD_REQUEST

	if not metadata:
		return jsonify({"error": "Metadata file not provided"}), HTTP_400_BAD_REQUEST

	current_user = get_jwt_identity()

	questions = []
	dup_count = 0
	duplicates = []
	for i, audio in enumerate(audio_files):
		if audio:
			filename = os.path.join("static", "audio_uploads", audio.filename)
			if os.path.exists(filename):
				dup_count += 1
				duplicates.append({"filename": filename})
				return (
					jsonify({"error": "File with the same name already exists"}),
					HTTP_400_BAD_REQUEST,
				)
			audio.save(filename)
			# i am assuming the metadata has the audio file name for correlation
			# in my case am calling the metadata object attribute for the audio "audio_filename"
			matching_metadata = None
			for item in metadata:
				if item.get("audio_filename") == audio.filename:
					matching_metadata = item
					break

			if matching_metadata:
				question_data = {
					"language": matching_metadata.get("language"),
					"topic": matching_metadata.get("topic", ""),
					"sub_topic": matching_metadata.get("sub_topics", ""),
					"category": matching_metadata.get("category", ""),
					"animal_crop": matching_metadata.get("sub_category", ""),
					"location": matching_metadata.get("location", ""),
					"user_id": current_user,
					"filename": filename,
				}

				question = Question(**question_data)
				questions.append(question)
			else:
				# no matching metadata is found
				return (
					jsonify(
						{"error": f"No metadata found for audio file: {audio.filename}"}
					),
					HTTP_400_BAD_REQUEST,
				)

	db.session.add_all(questions)
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
			topic = obj.get("topic")
			sub_topic = obj.get("sub_topics")
			category = obj.get("category")
			animal_crop = obj.get("sub_category")
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
					sub_topic=sub_topic,
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
	questions = Question.query.filter(
		(Question.cleaned.is_(None) | (Question.cleaned != True))
	).all()

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
				"sub_topic": question.sub_topic,
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
		.filter(Question.cleaned.is_(None) | (Question.cleaned != True))
		.group_by(Question.language)
		.all()
	)

	average_daily_questions = total_questions / (
		Question.query.filter(
			(Question.cleaned.is_(None) | (Question.cleaned != True))
			& (Question.created_at >= datetime.date.today())
		).count()
		or 1
	)

	one_week_ago = datetime.date.today() - datetime.timedelta(weeks=1)
	average_weekly_questions = total_questions / (
		Question.query.filter(
			(Question.cleaned.is_(None) | (Question.cleaned != True))
			& (Question.created_at >= one_week_ago)
		).count()
		or 1
	)

	#  Calculate average questions per user
	total_users = User.query.count()
	average_questions_per_user = total_questions / (total_users or 1)

	plant_question_count = Question.query.filter(
		(Question.cleaned.is_(None) | (Question.cleaned != True))
		& (func.lower(Question.category) == "crop")
	).count()

	animal_question_count = Question.query.filter(
		(Question.cleaned.is_(None) | (Question.cleaned != True))
		& (func.lower(Question.category) == "animal")
	).count()

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
				"sub_topic": question.sub_topic,
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
			"sub_topic": random_question.sub_topic,
			"category": random_question.category,
			"animal_crop": random_question.animal_crop,
			"location": random_question.location,
		}
		return jsonify(question_data), HTTP_200_OK
	else:
		return jsonify({"message": "No questions available."}), HTTP_404_NOT_FOUND


@questions.route("/main_question_review", methods=["POST"])
@jwt_required()
def main_question_review():
	data = request.get_json()
	
	category = data.get("category", None)
	language = data.get("language", None)
	sub_category = data.get("sub_category", None)

	filters = []

	category_filter = func.lower(Question.category) == category
	reviewed_filter = Question.reviewed == False

	# filters = [Question.category == category, Question.reviewed == False]

	if language:
		languages = [lang.strip().lower() for lang in language.split(",")]
		language_filter = func.lower(Question.language).in_(languages)
		filters.append(language_filter)

	if sub_category:
		sub_categories = [sub_cat.strip() for sub_cat in sub_category.split(",")]
		sub_category_filter = Question.animal_crop.in_(sub_categories)
		filters.append(sub_category_filter)

	matching_questions = (
		Question.query.filter(category_filter, reviewed_filter, *filters)
		.order_by(func.random())
		.first()
	)

	questions_data = []

	if matching_questions is not None:
		questions_data.append(format_question(matching_questions, "Any Language"))
		return jsonify(questions_data), HTTP_200_OK
	else:
		return jsonify({"message": "No questions available."}), HTTP_404_NOT_FOUND


@questions.route("/random_question_review_crop", methods=["GET"])
@jwt_required()
def random_question_for_review_crop():
	english_filter = func.lower(Question.language) == "english"
	luganda_filter = func.lower(Question.language) == "luganda"
	runyankole_filter = func.lower(Question.language) == "runyankole"
	unreviewed_filter = Question.reviewed == False
	cleaned_filter = Question.cleaned == True
	crop_category_filter = Question.category == "Crop"

	english_random_unreviewed_question = (
		Question.query.filter(
			crop_category_filter, english_filter, unreviewed_filter, cleaned_filter
		)
		.order_by(func.random())
		.first()
	)

	luganda_random_unreviewed_question = (
		Question.query.filter(
			crop_category_filter, luganda_filter, unreviewed_filter, cleaned_filter
		)
		.order_by(func.random())
		.first()
	)

	runyankole_random_unreviewed_question = (
		Question.query.filter(
			crop_category_filter, runyankole_filter, unreviewed_filter, cleaned_filter
		)
		.order_by(func.random())
		.first()
	)

	random_unreviewed_question = (
		Question.query.filter(crop_category_filter, unreviewed_filter, cleaned_filter)
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


@questions.route("/random_question_review_animal", methods=["GET"])
@jwt_required()
def random_question_for_review_animal():
	english_filter = func.lower(Question.language) == "english"
	luganda_filter = func.lower(Question.language) == "luganda"
	runyankole_filter = func.lower(Question.language) == "runyankole"
	unreviewed_filter = Question.reviewed == False
	cleaned_filter = Question.cleaned == True
	animal_category_filter = Question.category == "Animal"

	english_random_unreviewed_question = (
		Question.query.filter(
			animal_category_filter, english_filter, unreviewed_filter, cleaned_filter
		)
		.order_by(func.random())
		.first()
	)

	luganda_random_unreviewed_question = (
		Question.query.filter(
			animal_category_filter, luganda_filter, unreviewed_filter, cleaned_filter
		)
		.order_by(func.random())
		.first()
	)

	runyankole_random_unreviewed_question = (
		Question.query.filter(
			animal_category_filter, runyankole_filter, unreviewed_filter, cleaned_filter
		)
		.order_by(func.random())
		.first()
	)

	random_unreviewed_question = (
		Question.query.filter(animal_category_filter, unreviewed_filter, cleaned_filter)
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


@jwt_required()
@questions.route("/main_question_answer", methods=["POST"])
def main_question_answer():
	data = request.get_json()

	category = (data.get("category", None)).title()
	language = data.get("language", None)
	sub_category = data.get("sub_category", None)
	filters = []
	if language:
		if ',' in language:
			languages = [lang.strip().lower() for lang in language.split(",")]
			language_filter = func.lower(Question.language).in_(languages)
		else:
			language_filter = func.lower(Question.language) == language.strip().lower()
		filters.append(language_filter)
	if sub_category:
		if ',' in sub_category:
			sub_categories = [lang.strip().lower() for lang in sub_category.split(",")]
			sub_category_filter = func.lower(Question.animal_crop).in_(sub_categories)
		else:
			sub_category_filter = func.lower(Question.animal_crop) == sub_category.strip().lower()
		filters.append(sub_category_filter)

	matching_questions = Question.query.filter(
		Question.category.ilike(category),
    	Question.answered == True,
    	# Question.answered.is_not(True),
		*filters
		).order_by(db.func.random()).first()

	if matching_questions is not None:
		return jsonify(jsonify_question(matching_questions)), HTTP_200_OK
	else:
		return jsonify({"message": "No questions available."}), HTTP_404_NOT_FOUND


@questions.post("/add_answer/<int:question_id>")
@jwt_required()
def add_answer(question_id):
	data = request.get_json()
	user_id = get_jwt_identity()
	answer_text = request.json["answer"].strip()

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
		)
		if rephrased_data:
			question.sentence = rephrased_data

		new_topic = request.json.get(
			"topic"
		)
		if question.topic:
			if new_topic:
				new_topic += (
					", " + question.topic
				)
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
			"sub_topic": random_question.sub_topic,
			# answer part
		}
		return jsonify(question_data), 200
	else:
		return jsonify({"message": "No unanswered questions available"}), 404


@questions.route("/luganda", methods=["GET"])
@jwt_required()
def get_luganda_questions():
	luganda_questions = Question.query.filter(
		(Question.cleaned.is_(None) | (Question.cleaned != "t"))
		& (func.lower(Question.language) == "luganda")
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
				"sub_topic": question.sub_topic,
				"category": question.category,
				"animal_crop": question.animal_crop,
				"location": question.location,
				"cleaned": question.cleaned,
			}
			questions_data.append(question_data)

		return jsonify(questions_data), HTTP_200_OK
	else:
		return jsonify({"message": "No Luganda questions found"}), HTTP_404_NOT_FOUND


@questions.route("/english", methods=["GET"])
@jwt_required()
def get_english_questions():
	english_questions = Question.query.filter(
		(Question.cleaned.is_(None) | (Question.cleaned != "t"))
		& (func.lower(Question.language) == "english")
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
				"sub_topic": question.sub_topic,
				"category": question.category,
				"animal_crop": question.animal_crop,
				"location": question.location,
				"cleaned": question.cleaned,
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

@questions.route("/main_question_rank", methods=["POST"])
@jwt_required()
def main_question_rank():
	data = request.get_json()
	
	category = (data.get("category", None)).title()
	language = data.get("language", None)
	sub_category = data.get("sub_category", None)

	current_user = get_jwt_identity()

	filters = []

	if language:
		if ',' in language:
			languages = [lang.strip().lower() for lang in language.split(",")]
			language_filter = func.lower(Question.language).in_(languages)
		else:
			language_filter = func.lower(Question.language) == language.strip().lower()
		filters.append(language_filter)
	if sub_category:
		if ',' in sub_category:
			sub_categories = [lang.strip().lower() for lang in sub_category.split(",")]
			sub_category_filter = func.lower(Question.animal_crop).in_(sub_categories)
		else:
			sub_category_filter = func.lower(Question.animal_crop) == sub_category.strip().lower()
		filters.append(sub_category_filter)

	random_question_data = None
	matching_questions = (
		Question.query.filter(
			Question.category.ilike(category),
    		Question.reviewed == True,
    		Question.answered.is_not(True),
			(~Question.answers.any(Answer.user_id == current_user)),
			*filters)
		# .order_by(db.func.random())
		.all()
	)
	print(matching_questions)
	# if matching_questions:
	# 	random_question_data = {
	# 		"id": matching_questions.id,
	# 		"sentence": matching_questions.sentence,
	# 		"language": matching_questions.language,
	# 		"created_at": matching_questions.created_at.strftime("%Y-%m-%d %H:%M:%S"),
	# 		"topic": matching_questions.topic,
	# 		"sub_topic": matching_questions.sub_topic,
	# 		"category": matching_questions.category,
	# 		"animal_crop": matching_questions.animal_crop,
	# 		"location": matching_questions.location,
	# 	}

	# 	# Create a list to store answer data for each associated answer
	# 	answer_list = []
	# 	for answer in matching_questions.answers:
	# 		answer_data = {
	# 			"id": answer.id,
	# 			"answer_text": answer.answer_text,
	# 			"source": answer.source,
	# 			"relevance": answer.relevance,
	# 			"coherence": answer.coherence,
	# 			"fluency": answer.fluency,
	# 			"rank": answer.rank,
	# 			"created_at": answer.created_at.strftime("%Y-%m-%d %H:%M:%S"),
	# 		}
	# 		answer_list.append(answer_data)

	# 	random_question_data["answers"] = answer_list

	if True:
		result_object = {"random_question_data": True}
		return jsonify(result_object), HTTP_200_OK
	else:
		return jsonify({"message": "No questions available."}), HTTP_404_NOT_FOUND
	
@questions.route("/answered_question_ranking_animal", methods=["GET"])
@jwt_required()
def answered_question_ranking_animal():
	user_id = get_jwt_identity()
	cleaned_filter = Question.cleaned == True
	answered_filter = Question.answered == True
	# unFinished_filter = Question.finished == False
	question_and_answer_data = []

	languages = ["english", "luganda", "runyankole"]

	for language in languages:
		language_filter = func.lower(Question.language) == language

		random_unreviewed_question = (
			Question.query.filter(
				language_filter,
				answered_filter,
				cleaned_filter,
				# unFinished_filter,
				(func.lower(Question.category) == "animal"),
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
				"sub_topic": random_unreviewed_question.sub_topic,
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
			# unFinished_filter,
			(func.lower(Question.category) == "animal"),
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
			"sub_topic": random_question.sub_topic,
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


@questions.route("/answered_question_ranking_crop", methods=["GET"])
@jwt_required()
def answered_question_ranking_crop():
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
				(func.lower(Question.category) == "crop"),
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
				"sub_topic": random_unreviewed_question.sub_topic,
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
			(func.lower(Question.category) == "crop"),
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
			"sub_topic": random_question.sub_topic,
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
	user_id = get_jwt_identity()
	data = request.json
	question_id = data.get("questionId")
	rankings = data.get("rankings")

	if question_id is None or rankings is None:
		return jsonify({"message": "Invalid data format"}), HTTP_400_BAD_REQUEST

	question = Question.query.get(question_id)

	if question is None:
		return jsonify({"error": "Question not found"}), HTTP_404_NOT_FOUND

	ranking_count = 0
	try:
		for ranking in rankings:
			answer_id = ranking.get("answer_id")
			answer = Answer.query.get(answer_id)

			if answer:
				answer.relevance = ranking.get("relevance")
				answer.coherence = ranking.get("coherence")
				answer.fluency = ranking.get("fluency")
				answer.context = ranking.get("context")
				if ranking.get("isFlagged"):
					answer.offensive = True

		if question:
			if question.ranking_count is None:
				question.ranking_count = 1
			else:
				ranking_count = question.ranking_count
				question.ranking_count += 1

			ranking_count += 1

			question.ranked_by = user_id

		if ranking_count == 3 or question.ranking_count == 3:
			question.finished = True

		db.session.commit()
		return jsonify({"message": "Answer ranks stored successfully"}), HTTP_200_OK

	except Exception as e:
		db.session.rollback()
		print("here here")
		return jsonify({"message": "Error storing answer ranks"}), HTTP_400_BAD_REQUEST


@questions.route("/expert-stats", methods=["GET"])
@jwt_required()
def question_stats():
	total_cleaned = Question.query.filter_by(cleaned=True).count()
	cleaned_and_reviewed = Question.query.filter_by(cleaned=True, reviewed=True).count()
	cleaned_reviewed_and_answered = Question.query.filter_by(
		cleaned=True, answered=True
	).count()
	all_fields_true = Question.query.filter_by(cleaned=True, finished=True).count()
	experts = User.query.filter_by(role="expert").all()

	expert_data = []
	for expert in experts:
		# Count the number of reviewed questions for this expert
		reviewed_questions_count = Question.query.filter_by(
			reviewer_id=expert.id
		).count()

		# Get all answers provided by this expert
		answers = Answer.query.filter_by(user_id=expert.id).count()

		ranked_answers = Question.query.filter_by(ranked_by=expert.id).count()

		expert_info = {
			"id": expert.id,
			"lastname": expert.lastname,
			"firstname": expert.firstname,
			"phone_number": expert.phone_number,
			"reviewed_questions_count": reviewed_questions_count,
			"answers_count": answers,
			"ranked_answers": ranked_answers,
			"language": expert.language,
			"expertise": expert.category,
			"sub_category": expert.sub_category,
			"created_at": expert.created_at,
		}

		expert_data.append(expert_info)

	return jsonify(
		{
			"total_cleaned": total_cleaned,
			"cleaned_and_reviewed": cleaned_and_reviewed,
			"cleaned_reviewed_and_answered": cleaned_reviewed_and_answered,
			"all_fields_true": all_fields_true,
			"experts": expert_data,
		}
	)


@questions.route("/user_answers", methods=["GET"])
@jwt_required()
def get_user_answers():
	user_id = get_jwt_identity()

	user_answers = Answer.query.filter_by(user_id=user_id).all()
	answers_data = []

	for answer in user_answers:
		answers_data.append(
			{
				"id": answer.id,
				"answer_text": answer.answer_text,
				"created_at": answer.created_at,
				"question_id": answer.question_id,
			}
		)

	return jsonify(answers_data)


@questions.route("/answers/<int:answer_id>", methods=["GET"])
@jwt_required()
def get_answer(answer_id):
	user_id = get_jwt_identity()

	answer = Answer.query.get(answer_id)
	if not answer:
		return jsonify({"error": "Answer not found"}), HTTP_404_NOT_FOUND

	if answer.user_id != user_id:
		return jsonify({"error": "Unauthorized access to answer details"}), 403

	question = Question.query.get(answer.question_id)
	if not question:
		return jsonify({"error": "Question not found"}), HTTP_404_NOT_FOUND

	response_data = {
		"answer_id": answer.id,
		"answer_text": answer.answer_text,
		"question_id": question.id,
		"question_text": question.rephrased or question.sentence,
		"language": question.language,
		"animal_crop": question.animal_crop,
		"category": question.category,
		"topic": question.topic,
		"sub_topic": question.sub_topic,
	}

	return jsonify(response_data), HTTP_200_OK


@questions.route("/update_answer_text/<int:answer_id>", methods=["PUT"])
@jwt_required()
def update_answer_text(answer_id):
	answer = Answer.query.get(answer_id)
	if not answer:
		return jsonify({"message": "Answer not found"}), HTTP_404_NOT_FOUND
	new_answer_text = request.json.get("answer_text")

	if not new_answer_text:
		return jsonify({"message": "New answer_text not provided"}), HTTP_404_NOT_FOUND

	answer.answer_text = new_answer_text
	db.session.commit()

	return jsonify({"message": "Answer text updated successfully"}), HTTP_200_OK


@questions.route("/upload_json_answers/", methods=["POST"])
@jwt_required()
def upload_json_answers():
	json_data = [{}]

	current_user_id = get_jwt_identity()
	dup_count = 0
	duplicates = []

	new_category = "bard response"

	# Iterate through each object in json_data
	for obj in json_data:
		sentence = obj.get("questions")

		# Check if the question already exists and is cleaned
		existing_question = Question.query.filter_by(
			sentence=sentence, cleaned=True
		).first()

		if existing_question:
			question_id = existing_question.id
			# Add a new answer for the "new category"
			new_response_value = obj.get(new_category)

			if new_response_value is not None:
				new_response = Answer(
					question_id=question_id,
					answer_text=new_response_value,
					source=new_category,
					user_id=current_user_id,
				)

				db.session.add(new_response)
				db.session.commit()

	# Calculate duplicates and return the response_data
	response_data = {"duplicates_count": "done", "duplicates": "yes"}
	return jsonify(response_data), HTTP_200_OK

	# for obj in json_data:
	#     sentence = obj.get("Prompts")
	#     language = obj.get("Language")
	#     topic = obj.get("Topic")
	#     category = obj.get("Category")
	#     animal_crop = obj.get("animal_crop")
	#     location = obj.get("Location")

	#     # Check if the question already exists
	#     if Question.query.filter_by(sentence=sentence).first():
	#         dup_count += 1
	#         duplicates.append({"sentence": sentence})
	#     else:
	#         question = Question(
	#             sentence=sentence,
	#             language=language,
	#             user_id=current_user_id,
	#             topic=topic,
	#             category=category,
	#             animal_crop=animal_crop,
	#             location=location,
	#             cleaned=True,
	#         )
	#         db.session.add(question)
	#         db.session.commit()
	#         question_id = question.id

	#         response_categories = [
	#             "Bing response",
	#             "Bard Response",
	#             "Llama -2 Response",
	#             "GPT 3.5 response",
	#             # "chatgpt 4 response",
	#         ]
	#         for category in response_categories:
	#             response_value = obj.get(category)
	#             if response_value is not None:
	#                 response = Answer(
	#                     question_id=question_id,
	#                     answer_text=response_value,
	#                     source=category,
	#                     user_id=current_user_id,
	#                 )
	#                 db.session.add(response)
	#                 db.session.commit()

	# response_data = {"duplicates_count": dup_count, "duplicates": duplicates}
	# return jsonify(response_data), HTTP_200_OK
