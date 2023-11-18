# app.py
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

db = SQLAlchemy() 

def create_app(config_filename=None):
    app = Flask(__name__)

    # Load configuration from file or environment variables
    if config_filename:
        app.config.from_pyfile(config_filename)

    app.template_folder = '../templates'
    
    # Set up the database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:240699@127.0.0.1:3306/dashboard'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    
    
    # Register blueprints, middleware, etc.
    from routes.main_routes import main_routes  # Update this import
    app.register_blueprint(main_routes)

    return app
