from flask import Blueprint, jsonify, request
import google.generativeai as gai
from dotenv import load_dotenv
import os

from app import db
from app.models import TypeTest

load_dotenv()

type_bp = Blueprint('type_bp', __name__, url_prefix='/')
@type_bp.route('/')
def home():
    return jsonify({'message': 'Welcome!'})
@type_bp.post('/test')
def test():
    """
    'prompt': self.prompt,
            'time_limit': self.time_limit,
            'words_typed': self.words_typed,
            'accuracy': self.accuracy,
            'errors': self.errors,
            'wpm': self.wpm,
            'notes': self.notes,
            'created_at': self.created_at,
            'updated_at': self.updated_at
    """
    data = request.get_json()

    word_typed = data.get('word_typed')
    accuracy = data.get('accuracy', type=float)
    errors = data.get('errors', type=float)
    wpm = data.get('wpm', type=float)
    notes = data.get('notes', type=str)
    time_limit = data.get('time_limit', 0)



    if None in [word_typed, accuracy, errors, wpm]:
        return jsonify({"message": "in valid post request"}), 400

    test_taken = TypeTest(words_typed=word_typed, accuracy=accuracy, errors=errors, wpm=wpm, notes=notes, time_limit=time_limit)
    db.session.add(test_taken)
    db.session.commit()

    return jsonify({'message': 'test successfully registered', "test":test_taken.serialize()}), 201




@type_bp.get("/get_text_ai")
def get_text_ai():
    level = request.args.get('level', type=int)
    prompt = "generate text related to animal unique behaviour with "

    gai.configure(api_key=os.getenv("GEMINI_API_KEY"))
    model = gai.GenerativeModel(os.getenv("GEMINI_MODEL"))

    match level:
        case 1:
            prompt += " 300 words"

        case 2:
            prompt += " 200 words"

        case 3:
            prompt += " 100 words"

    try:
        response = model.generate_content(prompt)

        if hasattr(response, 'text'):

            return jsonify({'content': response.text})
        else:
            return jsonify(
                {'content':
                     "Elephants are the largest land mammals, recognized for their trunks with 150,000 muscles,"
                     " ivory tusks, thick wrinkled skin, massive molars, and large ears shaped like continents. "
                     "They display intelligence, empathy, memory, complex social bonds, and eat 150kg daily."
                     " Lifespans reach 70 years, vital for ecosystems and culture."}), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 403


@type_bp.get('/get_text')
def get_text():
    level = request.args.get('level', type=int)
    datas = []

    with open()
