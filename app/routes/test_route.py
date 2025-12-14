import json
import random
import os

from flask import Blueprint, jsonify, request
from dotenv import load_dotenv

from app import db
from app.models import TypeTest

load_dotenv()

type_bp = Blueprint('type_bp', __name__, url_prefix='/')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, 'data.json')


@type_bp.get('/')
def home():
    return jsonify({'message': 'Welcome!'})


@type_bp.post('/test')
def test():
    data = request.get_json()

    if not data:
        return jsonify({"message": "Invalid JSON"}), 400

    # 1. Extract exactly what the frontend sends
    words_typed = data.get('words_typed')
    time_limit = data.get('time_limit', 0)
    notes = data.get('notes')

    try:
        accuracy = float(data.get('accuracy'))
        wpm = float(data.get('wpm'))
    except (TypeError, ValueError):
        return jsonify({"message": "accuracy and wpm must be numbers"}), 400

    if not words_typed:
        return jsonify({"message": "words_typed is required"}), 400

    # 2. Create the streamlined record
    test_taken = TypeTest(
        words_typed=words_typed,
        accuracy=accuracy,
        wpm=wpm,
        time_limit=time_limit,
        notes=notes
    )

    db.session.add(test_taken)
    db.session.commit()

    return jsonify({
        'message': 'Test successfully saved',
        'test': test_taken.serialize()
    }), 201


@type_bp.get('/get_text')
def get_text():
    level = request.args.get('level', type=int)

    if level is None:
        return jsonify({"message": "level query param required"}), 400

    with open(DATA_PATH, 'r') as f:
        datas = json.load(f)

    filtered = [d for d in datas if d['level'] == level]

    if not filtered:
        return jsonify({'content': datas[0]['behavior']}), 200

    selected = random.choice(filtered)
    return jsonify({'content': selected['behavior']}), 200


@type_bp.get("/results")
def results():
    _results = TypeTest.query.all()

    serialized_result = [r.serialize() for r in _results]

    sored_result = sorted(serialized_result, key=lambda x: x['wpm'], reverse=True)

    return jsonify({
        "results": sored_result
    }), 200

