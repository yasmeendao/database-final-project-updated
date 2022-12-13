from flask import Blueprint, request, jsonify, make_response,current_app
import json
from src import db

employees = Blueprint('employees',__name__)

@employees.route('/employees')
def get_employees():
    return '<h1>List of employees</h1>'

@employees.route('/employee',methods=['POST'])
def add_employee():
    current_app.logger.info(request.form)
    cursor = db.get_db().cursor()
    name = request.form['name']
    employeeID = request.form['employeeID']
    customerID = request.form['customerID']
    deptID = request.form['deptID']
    employeeType = request.form['employeeType']
    query = f'INSERT INTO (name, employeeID, customerID, deptID, employeeType) VALUES(\"{name}\", \"{employeeID}\", \"{customerID}\",  \"{deptID}\",  \"{employeeType}\")'
    cursor.execute(query)
    db.get_db().commit()
    return "Success!"

@employees.route('/employee/<name>',methods=['GET'])
def get_employee_detail(name):
    pass

