from flask import Blueprint, request, jsonify
from src.models import User, db
from src.schemas import user_schema, users_schema
import datetime

users_bp = Blueprint('users_bp', __name__)

@users_bp.route('/users', methods=['GET'])
def get_users():
    all_users = User.query.all()
    result = users_schema.dump(all_users)
    return jsonify(result)

@users_bp.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)
    return user_schema.jsonify(user)

@users_bp.route('/users', methods=['POST'])
def add_user():
    last_name = request.json['last_name']
    first_name = request.json['first_name']
    date_birth = request.json['date_birth']

    date_birth_obj = datetime.datetime.strptime(date_birth, '%d/%m/%Y')
    new_user = User(last_name, first_name, date_birth_obj)

    db.session.add(new_user)
    db.session.commit()

    return user_schema.jsonify(new_user)

@users_bp.route('/users/<int:user_id>', methods=['PUT'])
def update_users(user_id):

    user = User.query.get(user_id)

    if user:
        last_name = request.json['last_name']
        first_name = request.json['first_name']
        date_birth = request.json['date_birth']

        date_birth_obj = datetime.datetime.strptime(date_birth, '%d/%m/%Y')

        user.last_name = last_name
        user.first_name = first_name
        user.date_birth = date_birth_obj

        db.session.commit()

        return user_schema.jsonify(user)
    else:
        return jsonify({"error": "Cannot find the user"})



