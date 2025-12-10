from datetime import timedelta

from flask import Blueprint, jsonify, render_template, request
from flask_jwt_extended import create_access_token

from app.extensions import db
from app.models.user import User

auth_bp = Blueprint('auth', __name__, url_prefix='/')

@auth_bp.get('/')
def home():
    return render_template('index.html')

@auth_bp.post('/signup')
def signup():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')


    if None in [username, password]:
        return jsonify({'message': 'username or password is required'}), 404
    existing_user = User.query.filter_by(username=username).first()
    if existing_user:
        return jsonify({'message': 'username already exists'}), 409

    user = User(username=username)
    user.set_password(password=password)

    db.session.add(user)
    db.session.commit()

    return jsonify({'message': 'user created'}), 201


@auth_bp.post('/login')
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if None in [username, password]:
        return jsonify({'message': 'username or password is required'}), 404

    user = User.query.filter_by(username=username).first()
    if not user:
        return jsonify({'message': 'user not found'}), 404
    if not user.check_password(password):
        return jsonify({'message': 'wrong password'}), 401

    access_token = create_access_token(identity=str(user.id))

    return jsonify({
        'access_token': access_token,
        'token_type': 'bearer',
        'user':{
            'id': user.id,
            'username': user.username
        }
    }), 200

@auth_bp.post('/logout')
def logout():
    data = request.get_json()
    current_user = User.query.filter_by(username=data['username']).first()
    access_token = create_access_token(identity=str(current_user.id), expires_delta=timedelta(seconds=1))
    return jsonify({
        'access_token': access_token,
        'token_type': 'bearer',
        'user':{
            'id': current_user.id,
            'username': current_user.username
        }
    })
