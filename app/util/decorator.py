# from functools import wraps
#
# from flask import jsonify
# from flask_jwt_extended import get_jwt_identity
# from app.models.user import User
#
#
# def role_required(role):
#     def decorator(func):
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             user_id = int(get_jwt_identity())
#             user = User.query.filter_by(id=user_id).first()
#             if user is None:
#                 return jsonify({"message": "user not exist"}), 401
#             return func(*args, **kwargs)
#         return wrapper
#     return decorator
#
