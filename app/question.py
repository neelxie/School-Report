from app.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND, HTTP_409_CONFLICT
from flask import Blueprint, request
from flask.json import jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required
from app.models import Question, db

questions = Blueprint("questions", __name__, url_prefix="/api/v1/questions")


@questions.route('/', methods=['POST', 'GET'])
@jwt_required()
def handle_questions():
    
    def process_single_question(question_data, current_user):
        sentence = question_data.get('sentence', '')
        language = question_data.get('language', '')

        if not sentence or not language:
            return {
                'error': 'Both sentence and language must be provided for each question'
            }, HTTP_400_BAD_REQUEST
        elif len(sentence) < 12:
            return {
                'error': 'Enter a valid sentence for each question'
            }, HTTP_400_BAD_REQUEST
        elif Question.query.filter_by(sentence=sentence).first():
            return {
                'error': 'Sentence already exists for one of the questions'
            }, HTTP_409_CONFLICT
        else:
            question = Question(sentence=sentence, language=language, user_id=current_user)
            db.session.add(question)
            db.session.flush()
            return {
                'id': question.id,
                'sentence': question.sentence,
                'language': question.language,
                'answer': question.answer,
                'created_at': question.created_at,
                'updated_at': question.updated_at,
            }, HTTP_201_CREATED
        
    current_user = get_jwt_identity()

    if request.method == 'POST':

        data = request.get_json()

        if not data:
            return jsonify({
                "error": "Invalid or empty JSON data provided"
            }), HTTP_400_BAD_REQUEST

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
            return jsonify(result), HTTP_201_CREATED

    else:

        questions = Question.query.filter_by(user_id=current_user).all()

        returned_data = []

        if not returned_data:
            return jsonify({
                "error": "No data yet"
            }), HTTP_204_NO_CONTENT


        for question in questions.items:
            returned_data.append({
            'id': question.id,
            'sentnce': question.sentence,
            'language': question.language,
            'answer': question.answer,
            'created_at': question.created_at,
            'updated_at': question.updated_at,
            })

        return jsonify({'data': returned_data}), HTTP_200_OK


@questions.get("/<string:id>")
@jwt_required()
def get_question(id):
    current_user = get_jwt_identity()

    question = Question.query.filter_by(user_id=current_user, id=id).first()

    if not question:
        return jsonify({'message': 'Item not found'}), HTTP_404_NOT_FOUND

    return jsonify({
        'id': question.id,
        'url': question.url,
        'short_url': question.short_url,
        'visit': question.visits,
        'body': question.body,
        'created_at': question.created_at,
        'updated_at': question.updated_at,
    }), HTTP_200_OK
