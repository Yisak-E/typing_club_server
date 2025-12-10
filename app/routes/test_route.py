from flask import Blueprint, jsonify

type_bp = Blueprint('type_bp', __name__, url_prefix='/type')
@type_bp.route('/')
def home():
    return jsonify({'message': 'Welcome!'})
@type_bp.route('/test')
def test():
    return jsonify({'message': 'Welcome!'})