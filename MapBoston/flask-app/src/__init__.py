# Some set up for the application
from multiprocessing import managers

from flask import Flask, views
from flaskext.mysql import MySQL
from users_api import users

# create a MySQL object that we will use in other parts of the API
db = MySQL()


def create_app():
    app = Flask(__name__)
    # secret key that will be used for securely signing the session
    # cookie and can be used for any other security related needs by
    # extensions or your application
    app.config['SECRET_KEY'] = 'someCrazyS3cR3T!Key.!'

    # these are for the DB object to be able to connect to MySQL.
    app.config['MYSQL_DATABASE_USER'] = 'webapp'
    app.config['MYSQL_DATABASE_PASSWORD'] = open('/secrets/db_password.txt').readline()
    app.config['MYSQL_DATABASE_HOST'] = 'db'
    app.config['MYSQL_DATABASE_PORT'] = 3306
    app.config['MYSQL_DATABASE_DB'] = 'database_project'  # Change this to your DB name

    # Initialize the database object with the settings above.
    db.init_app(app)

    # Import the various routes
    from flask.src.users_api.views import views
    from flask.src.managers_api.managers import managers
    from flask.src.users_api.users import users
    from flask.src.employees_api.employees import employees

    # Register the routes that we just imported so they can be properly handled
    app.register_blueprint(views, url_prefix='/vie')
    app.register_blueprint(managers, url_prefix='/mag')
    app.register_blueprint(users, url_prefix='/use')
    app.register_blueprint(employees, url_prefix='/emp')
    return app
