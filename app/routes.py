from flask import Blueprint, request, jsonify
from bson.objectid import ObjectId
from app.models import get_user_collection

users_bp = Blueprint('users', __name__)

@users_bp.route('/users', methods=['GET'])
def get_users():
    users = get_user_collection().find()
    return jsonify([user for user in users])

@users_bp.route('/users/<id>', methods=['GET'])
def get_user(id):
    user = get_user_collection().find_one({"_id": ObjectId(id)})
    return jsonify(user) if user else jsonify({"error": "User not found"}), 404

@users_bp.route('/users', methods=['POST'])
def create_user():
    data = request.json
    user_id = get_user_collection().insert_one(data).inserted_id
    return jsonify({"_id": str(user_id)})

@users_bp.route('/users/<id>', methods=['PUT'])
def update_user(id):
    data = request.json
    get_user_collection().update_one({"_id": ObjectId(id)}, {"$set": data})
    return jsonify({"message": "User updated"})

@users_bp.route('/users/<id>', methods=['DELETE'])
def delete_user(id):
    get_user_collection().delete_one({"_id": ObjectId(id)})
    return jsonify({"message": "User deleted"})
