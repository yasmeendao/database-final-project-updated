from flask import Blueprint, request, jsonify, make_response
import json
from src import db


departments = Blueprint('departments', __name__)

# Get all the departments from the database
@departments.route('/departments', methods=['GET'])
def get_departments():
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # use cursor to query the database for a list of departments
    cursor.execute('ManagerId, ManagerName, employeeId, num_employees, payroll from departments')

    # grab the column headers from the returned data
    column_headers = [x[0] for x in cursor.description]

    # create an empty dictionary object to use in 
    # putting column headers together with data
    json_data = []

    # fetch all the data from the cursor
    thedata = cursor.fetchall()

    # for each of the rows, zip the data elements together with
    # the column headers. 
    for row in thedata:
        json_data.append(dict(zip(column_headers, row)))

    return jsonify(json_data)

# get the department details from the database
@departments.route('/deptdetails')
def get_department_details():
    cursor = db.get_db().cursor()
    query = '''
        SELECT ManagerId, ManagerName, employeeId, num_employees, payroll
        FROM Department 
    '''
    cursor.execute(query)
       # grab the column headers from the returned data
    column_headers = [x[0] for x in cursor.description]

    # create an empty dictionary object to use in 
    # putting column headers together with data
    json_data = []

    # fetch all the data from the cursor
    theData = cursor.fetchall()

    # for each of the rows, zip the data elements together with
    # the column headers. 
    for row in theData:
        json_data.append(dict(zip(column_headers, row)))

    return jsonify(json_data)