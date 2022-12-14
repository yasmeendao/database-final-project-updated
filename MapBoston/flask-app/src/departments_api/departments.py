from flask import Blueprint, request, jsonify, make_response
import json

departments = Blueprint('departments', __name__)

