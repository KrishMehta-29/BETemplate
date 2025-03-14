from flask import render_template, redirect, request, url_for, jsonify
from . import index_bp  # Import the blueprint

from app.models.mongo_models import User

@index_bp.route('/')
def index():
    return jsonify("Hello World")

@index_bp.route('/user/<userName>')
def getUser(userName):
    u = User.objects.filter(name=userName)
    users = list(u)

    userDict = [{ "name": user.name, "age": user.age, "email": user.email } for user in users]

    return jsonify(userDict)

@index_bp.route('/user/createUser', methods=["POST"])
def createUser():
    data = request.json
    u = User(name=data["name"], age=data["age"], email=data["email"])
    u.save()

    return jsonify({"ok": True})
