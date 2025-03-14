from flask import render_template, redirect, url_for, jsonify
from . import index_bp  # Import the blueprint

@index_bp.route('/')
def index():
    return jsonify("Hello World")

@index_bp.route('/veer')
def veer():
    return jsonify("My Name Is Veer")