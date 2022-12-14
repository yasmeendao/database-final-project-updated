import db
from flask import Blueprint, request, jsonify, make_response
import json
#from src import db

users = Blueprint('users', __name__)

def users_blueprint():
    return None