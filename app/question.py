embedded_json = []
import json

from app.status import (
	HTTP_200_OK,
	HTTP_201_CREATED,
	HTTP_204_NO_CONTENT,
	HTTP_400_BAD_REQUEST,
	HTTP_404_NOT_FOUND,
	HTTP_409_CONFLICT,
)
from flask import Blueprint, request, send_file
from flask.json import jsonify
import pandas as pd
from flask_jwt_extended import get_jwt_identity, jwt_required, verify_jwt_in_request
from app.models import Question, db, User, Answer
import datetime
import random
import os
from os.path import join, dirname, realpath
from io import StringIO
from google.cloud import storage

from sqlalchemy import func, or_, and_, not_, text
from app.helper import admin_required

UPLOADS_PATH = join(dirname(realpath(__file__)), "static/audio_uploads")
DATASET_PATH = join(dirname(realpath(__file__)), "static/dataset")

questions = Blueprint("questions", __name__, url_prefix="/api/v1/questions")

def get_audio_file_content(file_path):
	# file_path = os.path.join(UPLOADS_PATH, filename)
	return send_file(file_path, as_attachment=True)



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

def file_name(file):
	name = file.filename
	file_name, file_extension = os.path.splitext(name)
	return file_name, file_extension


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

	for obj in metadata:
		audio_filename = obj['audio_filePath'].rsplit('.', 1)[0]
		
		for audio in audio_files:
			au  =  file_name(audio)[0]
			
			if audio_filename == au:
				
				filename = os.path.join("static", "audio_uploads", obj["audio_filename"])

				if os.path.exists(filename):
					dup_count += 1
					duplicates.append({"filename": filename})
					return (
						jsonify({"error": "File with the same name already exists"}),
						HTTP_400_BAD_REQUEST,
					)
				audio.save(filename) 		

				if obj:
					question_data = {
						"language": obj.get("language"),
						"topic": obj.get("topic", ""),
						"sub_topic": obj.get("sub_topics", ""),
						"category": obj.get("category", ""),
						"animal_crop": obj.get("sub_category", ""),
						"location": obj.get("location", ""),
						"user_id": current_user,
						"filename": filename,
					}

					question = Question(**question_data)
					questions.append(question)
				else:
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
@questions.get('/delete-questions')
def delete_questions():
	try:
		questions_to_delete = Question.query.filter(Question.rephrased == "actual", Question.reviewed != True).all()
		
		# for question in questions_to_delete:
		#		Answer.query.filter_by(question_id=question.id).delete()

		# num_deleted = Question.query.filter(Question.rephrased == "actual", Question.reviewed != True).delete()
		num_deleted = len(questions_to_delete)

		db.session.commit()
		return jsonify({'message': f'{num_deleted} questions and associated answers deleted successfully'})
	except Exception as e:
		db.session.rollback()
		return jsonify({'error': 'An error occurred while deleting questions and answers'})


@jwt_required()
@questions.get("/displayall")
def display_questions():
	verify_jwt_in_request()
	curre = get_jwt_identity()
	isadmin = User.query.get(curre)
	page = request.args.get('page', 1, type=int)
	per_page = request.args.get('per_page', 100, type=int)
	questions = Question.query.filter(
		(Question.user_id != isadmin.id)
	).paginate(page=page, per_page=per_page, error_out=False)

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
				"audio": question.filename,
				"user_name": user_name,
			}
		)

	return jsonify(returned_data), HTTP_200_OK


@jwt_required()
@questions.get("/all")
def get_questions():
	current_user = get_jwt_identity()
	isadmin = User.query.get(current_user)
	questions = Question.query.filter(
		(Question.user_id != isadmin.id)
	).all()

	if not questions:
		return jsonify({"message": "No questions yet."}), HTTP_204_NO_CONTENT

	returned_data = []

	for question in questions:
		user = User.query.get(question.user_id)
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
				"audio": question.filename,
				"user_name": user_name,
			}
		)

	return jsonify(returned_data), HTTP_200_OK



@jwt_required()
@questions.get("/download")
def download_questions():
	verify_jwt_in_request()
	user_id = get_jwt_identity()
	isadmin = User.query.get(user_id)
	start_date_str = request.args.get('start_date')
	
	if start_date_str:
		try:
			start_date = datetime.datetime.strptime(start_date_str, '%Y-%m-%d')
			questions = Question.query.filter(
				(Question.user_id != isadmin.id) &
				(Question.created_at >= start_date)
			).all()
		except ValueError:
			return jsonify({"message": "Invalid start_date format. Use YYYY-MM-DD."}), HTTP_400_BAD_REQUEST
	else:
		questions = Question.query.filter(
			(Question.rephrased != "actual")
		).all()

	if not questions:
		return jsonify({"message": "No questions yet."}), HTTP_204_NO_CONTENT

	returned_data = []

	for question in questions:
		user = User.query.get(question.user_id)  # Get the user who asked the question
		user_name = None
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
				"audio": question.filename,
				"user_name": user_name,
			}
		)
	return jsonify(returned_data), HTTP_200_OK

@jwt_required()
@questions.get("/myqns")
def get_my_questions():
	questions = Question.query.filter(
		(Question.rephrased == "actual")
	).all()

	if not questions:
		return jsonify({"message": "No questions yet."}), HTTP_204_NO_CONTENT

	returned_data = []

	for question in questions:
		user = User.query.get(question.user_id)
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
				"reviewed":question.reviewed,
				"rephrased": question.rephrased
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
	verify_jwt_in_request()
	current_user = get_jwt_identity()
	isadmin = User.query.get(current_user)
	all_questions = Question.query.filter(
		(Question.user_id != isadmin.id)
	).all()
	
	#     all_questions = db.sessionQuestion).all()
	total_questions = len(all_questions)
	questions_per_language = (
		db.session.query(Question.language, func.count(Question.id))
		.filter((Question.user_id != isadmin.id))
		.group_by(Question.language)
		.all()
	)
	
	audio_questions = Question.query.filter(Question.filename.isnot(None)).all()

	average_daily_questions = total_questions / (
		Question.query.filter(
			(Question.rephrased != "actual"),
			(Question.user_id != isadmin.id)
			& (Question.created_at >= datetime.date.today())
		).count()
		or 1
	)

	one_week_ago = datetime.date.today() - datetime.timedelta(weeks=1)
	average_weekly_questions = total_questions / (
		Question.query.filter(
			(Question.rephrased != "actual"),
			(Question.user_id != isadmin.id)
			& (Question.created_at >= one_week_ago)
		).count()
		or 1
	)

	#  Calculate average questions per user
	total_users = User.query.count()
	average_questions_per_user = total_questions / (total_users or 1)
	
	plant_question_count = Question.query.filter(
		(Question.user_id != isadmin.id)
		& (func.lower(Question.category) == "crop")
	).count()

	animal_question_count = Question.query.filter(
		(Question.user_id != isadmin.id)
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
		"audios": len(audio_questions),
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

	if language:
		languages = [lang.strip().lower() for lang in language.split(",")]
		language_filter = func.lower(Question.language).in_(languages)
		filters.append(language_filter)

	if sub_category:
		sub_categories = [sc.strip().lower() for sc in sub_category.split(",")]

		vegetable_sub_categories = [
				"tomatoes", "carrots", "onions", "mushrooms", "eggplant", "beetroot",
				"doodo", "spinach", "cucumbers", "avocado", "cabbage", "nakati", "ginger",
				"green pepper", "garlic", "okra", "lettuce", "malakwang", "pepper", "sukuma wiiki",
				"kale", "hubiscus"
		]

		poultry_sub_categories = ["chicken", "ducks", "guinea fowls", "turkeys"]

		cattle_sub_categories = ["cattle", "goat", "goats"]
		cereals_sub_categories = ["maize", "sorghum", "millet", "rice", "wheat", "sim sim", "sesame"]
		fruits_sub_categories = ["watermelon", "pineapple", "mango", "sugarcane", "orange", "avocado", "passion fruit", "jack fruit", "paw paw", "guava", "lemon"]
		legumes_sub_categories = [ "soya beans", "beans", "peas", "groundnuts", "Gnuts", "ground nuts"]
		sub_category_filters = []

		for sc in sub_categories:
			if sc == "vegetables":
				sub_category_filters.append(func.lower(Question.animal_crop).in_(vegetable_sub_categories))
			elif sc == "fruits":
				sub_category_filters.append(func.lower(Question.animal_crop).in_(fruits_sub_categories))
			elif sc == "cereals":
				sub_category_filters.append(func.lower(Question.animal_crop).in_(cereals_sub_categories))
			elif sc == "legumes":
				sub_category_filters.append(func.lower(Question.animal_crop).in_(legumes_sub_categories))
			elif sc == "cattle":
				sub_category_filters.append(func.lower(Question.animal_crop).in_(cattle_sub_categories))
			elif sc == "poultry":
				sub_category_filters.append(func.lower(Question.animal_crop).in_(poultry_sub_categories))
			else:
				sub_category_filters.append(func.lower(Question.animal_crop) == sc)
		
		filters.extend(sub_category_filters)
	
	if category.lower() == "animal":
		filters.append(func.lower(Question.animal_crop).in_(["animal", "animals"]))
	elif category.lower() == "crop":
		filters.append(func.lower(Question.animal_crop).in_(["crop", "crops"]))
	
	matching_questions = (
		Question.query.filter(Question.rephrased == "actual", *filters)
		.all()
	)
	print(matching_questions)
	# questions_data = []

	if matching_questions:
		random_question = random.sample(matching_questions, 1)[0]
		questions_data = format_question(random_question, "Any Language")
		return jsonify([questions_data]), HTTP_200_OK
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
		sub_category = sub_category.lower()
		if sub_category.lower() == "vegetables":
			
	
			allowed_vegetables = [
				"tomatoes", "carrots", "onions", "mushrooms", "eggplant", 
        "beetroot", "doodoo", "spinach", "cucumbers", "avocado", 
        "cabbage", "nakati", "ginger", "green pepper", "garlic", 
        "okra", "lettuce", "malakwang", "pepper"
				]
			if ',' in sub_category:
				sub_categories = [lang.strip().lower() for lang in sub_category.split(",")]
				sub_category_filter = func.lower(Question.animal_crop).in_(sub_categories)
				sub_category_filter = and_(sub_category_filter, func.lower(Question.animal_crop).in_(allowed_vegetables))
			else:
				sub_category_filter = func.lower(Question.animal_crop).in_(allowed_vegetables)
		else:
			if ',' in sub_category:
				sub_categories = [lang.strip().lower() for lang in sub_category.split(",")]
				sub_category_filter = func.lower(Question.animal_crop).in_(sub_categories)
			else:
				sub_category_filter = func.lower(Question.animal_crop) == sub_category.strip().lower()
		filters.append(sub_category_filter)


	matching_questions = Question.query.filter(
		Question.category.ilike(category),
		Question.rephrased == "actual",
    Question.reviewed == True,
    Question.answered.is_not(True),
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
		question.answer_expert_one = user_id
		db.session.commit()

		return jsonify({"message": "Answer added successfully."}), HTTP_201_CREATED
	return jsonify({"message": "Failed to add answer."})

@questions.post("/review_and_answer/<int:question_id>")
@jwt_required()
def review_and_answer(question_id):
	user_id = get_jwt_identity()
	question = Question.query.get(question_id)

	if not question:
		return jsonify({"message": "Question not found."}), HTTP_404_NOT_FOUND

	data = request.get_json()
	answer_text = data.get("answer", "").strip()
	new_topic = data.get("topic")

	if answer_text and len(answer_text) > 7:
		new_answer = Answer(
				question_id=question_id,
				user_id=user_id,
				answer_text=answer_text,
				source="expert",
		)

		db.session.add(new_answer)
		question.answered = True
		question.answer_expert_one = user_id

		if question.topic:
			if new_topic:
				question.topic = (new_topic + ", " + question.topic)
		else:
			question.topic = new_topic

		question.reviewed = True
		question.correct = True
		question.reviewer_id = user_id

		db.session.commit()

		return jsonify({"message": "Answer added successfully and question attributes updated."}), HTTP_201_CREATED

	return jsonify({"message": "Failed to add answer or update question attributes."})

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


@questions.route("/question_review/<int:question_id>", methods=["PATCH"])
@jwt_required()
def question_review(question_id):
	user_id = get_jwt_identity()
	question = Question.query.get(question_id)
	
	if question:

		question.reviewed = True
		question.correct = True 
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
				question.topic = (
					new_topic + ", " + question.topic
				)
		else:
			question.topic = new_topic 

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
		(Question.rephrased != "actual"),
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
		(Question.rephrased != "actual"),
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
	
@questions.route("/runyankole", methods=["GET"])
@jwt_required()
def get_runyankole_questions():
	verify_jwt_in_request()
	current_user = get_jwt_identity()
	is_admin = User.query.get(current_user)

	runya_questions = (Question.query
	.filter(Question.user_id != is_admin.id)
	.filter(func.lower(Question.language) == "runyankole")
	.all())


	if runya_questions:
		questions_data = []
		for question in runya_questions:
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
		return jsonify({"message": "No Runyankole questions found"}), HTTP_404_NOT_FOUND
	
@questions.route("/audios", methods=["GET"])
@jwt_required()
def audio_questions():
	
	audio_questions = Question.query.filter(Question.filename.isnot(None)).all()
	audio_questions_list = []

	if audio_questions:
		

		for question in audio_questions:
			
			file_path = os.path.join(UPLOADS_PATH, question.filename)
			
			# if os.path.exists(file_path):
			audio_questions_list.append({
				'id': question.id,
				"language": question.language,
				"created_at": question.created_at.strftime("%Y-%m-%d %H:%M:%S"),
				"topics": question.topic,
				"sub_topic": question.sub_topic,
				"category": question.category,
				"animal_crop": question.animal_crop,
				"location": question.location,
				'filename': question.filename,
				# 'file_content': get_audio_file_content(file_path)
			})
		return jsonify(audio_questions_list)
	return jsonify({"message": "No Audio questions found"}), HTTP_404_NOT_FOUND

@questions.route("/expertluganda", methods=["GET"])
@jwt_required()
def get_expert_luganda_questions():
	luganda_questions = Question.query.filter(
		(Question.rephrased == "actual")
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
			}
			questions_data.append(question_data)

		return jsonify(questions_data), HTTP_200_OK
	else:
		return jsonify({"message": "No Luganda expert questions found"}), HTTP_404_NOT_FOUND
	
@questions.route("/expertenglish", methods=["GET"])
@jwt_required()
def get_expert_english_questions():
	luganda_questions = Question.query.filter(
		(Question.rephrased == "actual")
		& (func.lower(Question.language) == "english")
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
			}
			questions_data.append(question_data)

		return jsonify(questions_data), HTTP_200_OK
	else:
		return jsonify({"message": "No English expert questions found"}), HTTP_404_NOT_FOUND
	
@questions.route("/expertrunyankole", methods=["GET"])
@jwt_required()
def get_expert_runyankole_questions():
	luganda_questions = Question.query.filter(
		(Question.rephrased == "actual")
		& (func.lower(Question.language) == "runyankole")
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
			}
			questions_data.append(question_data)

		return jsonify(questions_data), HTTP_200_OK
	else:
		return jsonify({"message": "No Runyankole expert questions found"}), HTTP_404_NOT_FOUND

@questions.route("/evaluated", methods=["GET"])
@jwt_required()
def get_evaluated_questions():
	
	matching_questions = (
		Question.query.filter(
			Question.rephrased == "actual",
    	Question.answered == True)
		.all()
	)
	total_questions = len(matching_questions)

	if matching_questions:
		questions_data = []
		for question in matching_questions:
			question_data = {
				"id": question.id,
				"sentence": question.sentence,
				"language": question.language,
				"created_at": question.created_at.strftime("%Y-%m-%d %H:%M:%S"),
				"topic": question.topic,
				"sub_topic": question.sub_topic,
				"category": question.category,
				"animal_crop": question.animal_crop,
				"location": question.location,
				"answers": []
			}

			for answer in question.answers:
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
				question_data["answers"].append(answer_data)

			questions_data.append(question_data)

		result_object = {
				"questions": questions_data,
				"total_questions": total_questions
		}
		return jsonify(result_object), HTTP_200_OK
	else:
		return jsonify({"message": "No questions available for ranking."}), HTTP_404_NOT_FOUND

	
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
		sub_category = sub_category.lower()

		vegetable_sub_categories = [
				"tomatoes", "carrots", "onions", "mushrooms", "eggplant", "beetroot",
				"doodo", "spinach", "cucumbers", "avocado", "cabbage", "nakati", "ginger",
				"green pepper", "garlic", "okra", "lettuce", "malakwang", "pepper"
		]

		poultry_sub_categories = ["chicken", "ducks", "guinea fowls", "turkeys"]

		cattle_sub_categories = ["cattle", "goat", "goats"]
		sub_categories = []

		if sub_category == "vegetables":
			sub_categories = vegetable_sub_categories

		elif sub_category == "cattle":
			sub_categories = cattle_sub_categories

		elif sub_category == "poultry":
			sub_categories = poultry_sub_categories
		else:
			
			sub_categories = [sub_cat.strip() for sub_cat in (sub_category.split(",") if ',' in sub_category else [sub_category])]
		
		sub_category_filter = func.lower(Question.animal_crop).in_([sc.lower() for sc in sub_categories])
		
		filters.append(sub_category_filter)
	
	if category.lower() == "animal":
		animal_sub_category_filter = func.lower(Question.animal_crop) == "animal"
		animals_sub_category = func.lower(Question.animal_crop) == "animals"
		filters.append(animal_sub_category_filter)
		filters.append(animals_sub_category)
	elif category.lower() == "crop":
		crop_sub_category_filter = func.lower(Question.animal_crop) == "crop"
		crops_sub_category = func.lower(Question.animal_crop) == "crops"
		filters.append(crop_sub_category_filter)
		filters.append(crops_sub_category)

	random_question_data = None
	matching_questions = (
		Question.query.filter(
			Question.category.ilike(category),
			Question.rephrased == "actual",
    	Question.answered == True,
    	Question.finished.is_not(True),
			(~Question.answers.any(Answer.user_id == current_user)),
			(Question.rank_expert_one == None) | (Question.rank_expert_one == None),
			*filters)
		.order_by(db.func.random())
		.first()
	)
	
	if matching_questions:
		random_question_data = {
			"id": matching_questions.id,
			"sentence": matching_questions.sentence,
			"language": matching_questions.language,
			"created_at": matching_questions.created_at.strftime("%Y-%m-%d %H:%M:%S"),
			"topic": matching_questions.topic,
			"sub_topic": matching_questions.sub_topic,
			"category": matching_questions.category,
			"animal_crop": matching_questions.animal_crop,
			"location": matching_questions.location,
			"filename": matching_questions.filename,
		}

	    # Create a list to store answer data for each associated answer
		answer_list = []
		for answer in matching_questions.answers:
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

	if random_question_data:
		result_object = {"random_question_data": random_question_data}
		return jsonify(result_object), HTTP_200_OK
	else:
		return jsonify({"message": "No questions available for ranking."}), HTTP_404_NOT_FOUND
	
def upload_to_bucket(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to a GCP storage bucket."""
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(source_file_name)
    print(f"File {source_file_name} uploaded to {destination_blob_name} in bucket {bucket_name}.")

	
@questions.route("/fetch_questions", methods=["GET"])
@jwt_required()
def fetch_questions():
	page = request.args.get('page', 1, type=int)
	per_page = request.args.get('per_page', 50, type=int)

	matching_questions = (
		Question.query.filter(
			Question.rephrased == "actual",
    	Question.reviewed == False
			)
		.paginate(page=page, per_page=per_page, error_out=False)
	)
	all = []
	random_question_data = None
	if matching_questions:
		for question in matching_questions:
			answers = [{'text': answer.answer_text, 'source': answer.source} for answer in question.answers]

			random_question_data = {
				"id": question.id,
				"sentence": question.sentence,
				"language": question.language,
				"topic": question.topic,
				"sub_topic": question.sub_topic,
				"category": question.category,
				"animal_crop": question.animal_crop,
				"location": question.location,
				"answers": answers
			}
			all.append(random_question_data)

	if all:
		pagination_details = {
			'total_pages': matching_questions.pages,
			'current_page': matching_questions.page,
			'per_page': per_page,
			'total_questions': matching_questions.total
    }

		return jsonify({'questions': all, 'pagination': pagination_details}), HTTP_200_OK
	else:
		return jsonify({"message": "No questions available."}), HTTP_404_NOT_FOUND


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
				relevance = answer.relevance if answer.relevance is not None else 0
				coherence = answer.coherence if answer.coherence is not None else 0
				fluency = answer.fluency if answer.fluency is not None else 0

				relevance += ranking.get("relevance")
				coherence += ranking.get("coherence")
				fluency += ranking.get("fluency")
				# answer.context = ranking.get("context")
				if ranking.get("isFlagged"):
					answer.offensive = True

				answer.relevance = relevance
				answer.coherence = coherence
				answer.fluency = fluency
				answer.context = ranking.get("context")


		if question:
			if question.rank_expert_one is None:
				question.rank_expert_one = user_id
				question.ranking_count = 1
			else:
				question.rank_expert_two = user_id
				question.ranking_count = 2

			ranking_count += 1

		if ranking_count == 2 or question.ranking_count == 2:
			question.finished = True

		db.session.commit()
		return jsonify({"message": "Answer ranks stored successfully"}), HTTP_200_OK

	except Exception as e:
		db.session.rollback()
		return jsonify({"message": "Error storing answer ranks"}), HTTP_400_BAD_REQUEST


@questions.route("/expert-stats", methods=["GET"])
@jwt_required()
def question_stats():
	total_cleaned = Question.query.filter_by(cleaned=True, rephrased="actual").count()
	cleaned_and_reviewed = Question.query.filter_by(cleaned=True, reviewed=True, rephrased="actual").count()
	cleaned_reviewed_and_answered = Question.query.filter_by(
		cleaned=True, answered=True, rephrased="actual"
	).count()
	all_fields_true = Question.query.filter_by(cleaned=True, finished=True, rephrased="actual").count()
	experts = User.query.filter_by(role="expert").all()
	english_questions = Question.query.filter(
		Question.rephrased == "actual",
		Question.language.ilike("english")
	).count()
	luganda_questions = Question.query.filter(
		Question.rephrased == "actual",
		Question.language.ilike("luganda")
	).count()
	runyankole_questions = Question.query.filter(
		Question.rephrased == "actual",
		Question.language.ilike("runyankole")
	).count()

	expert_data = []
	for expert in experts:
		reviewed_questions_count = Question.query.filter_by(
			reviewer_id=expert.id
		).count()
		answers = Answer.query.filter_by(user_id=expert.id).count()

		ranked_answers = Question.query.filter((Question.rank_expert_one == expert.id) | (Question.rank_expert_two == expert.id)).count()

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
			"english_questions": english_questions,
			"luganda_questions": luganda_questions,
			"runyankole_questions": runyankole_questions
		}
	)


@questions.route("/user_answers", methods=["GET"])
@jwt_required()
def get_user_answers():
	user_id = get_jwt_identity()

	reviewed_questions_count = Question.query.filter_by(
		reviewer_id=user_id
	).count()

	answers = Answer.query.filter_by(user_id=user_id).count()

	ranked_answers = Question.query.filter((Question.rank_expert_one == user_id) | (Question.rank_expert_two == user_id)).count()

	user_answers = Answer.query.filter_by(user_id=user_id).all()
	answers_data = []

	for answer in user_answers:
		question = answer.question
		
		answers_data.append(
			{
				"id": answer.id,
				"answer_text": answer.answer_text,
				"created_at": answer.created_at,
				"question_id": answer.question_id,
				"sentence": question.sentence,
				"rank": question.ranking_count
			}
		)
	return jsonify({"all_answers":answers_data, "answers": answers,"reviewed_questions": reviewed_questions_count,"ranked": ranked_answers})


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
		"question_text": question.sentence,
		"language": question.language,
		"animal_crop": question.animal_crop,
		"category": question.category,
		"topic": question.topic,
		"sub_topic": question.sub_topic,
	
	}

	return jsonify(response_data), HTTP_200_OK


@questions.route("/experts/<int:user_id>", methods=["GET"])
@jwt_required()
def get_expert_stats(user_id):
	answers = Answer.query.filter_by(user_id=user_id).all()
	if not answers:
		return jsonify({"error": "Answers not found"}), HTTP_404_NOT_FOUND

	answers_data = []
	for answer in answers:
		
		question = Question.query.get(answer.question_id)
		answers_data.append(
			{
				"answer_id": answer.id,
				"answer_text": answer.answer_text,
				"date": answer.created_at,
				"question_id": question.id,
				"question_text": question.sentence,
				"language": question.language,
				"animal_crop": question.animal_crop,
				"category": question.category,
				"topic": question.topic,
				"sub_topic": question.sub_topic,
			
			}
		)

	return jsonify(answers_data), HTTP_200_OK

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


@questions.route("/upload_json_answers/", methods=["GET"])
@jwt_required()
def upload_json_answers():

	current_user_id = get_jwt_identity()
	dup_count = 0
	duplicates = []

	for obj in embedded_json:
		sentence = obj.get("Question")
		language = obj.get("Language")
		topic = obj.get("Topics")
		category = obj.get("Category")
		animal_crop = obj.get("Animal_Crop")
		location = obj.get("Location")

		# Check if the question already exists
		if Question.query.filter_by(sentence=sentence, cleaned=True, rephrased="actual").first():
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
						rephrased="actual",
						reviewed=True,
						reviewer_id=1
				)
				db.session.add(question)
				db.session.commit()
				question_id = question.id

				response_categories = [
						"Llama2",
						"Bard",
						"Bing",
						"ChatGPT 3.5",
						"GPT 4",
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
