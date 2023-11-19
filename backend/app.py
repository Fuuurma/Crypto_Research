# app.py
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_login import LoginManager


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
    login_manager = LoginManager(app)
    
    
    
    # Register blueprints, middleware, etc.
    from routes.main_routes import main_routes
    from routes.fees_routes import fees_routes
    from routes.tvl_routes import tvl_routes
    from routes.pools_routes import pools_routes
    
    app.register_blueprint(main_routes)
    app.register_blueprint(fees_routes, url_prefix='/fees')  # You can set a prefix for the URL
    app.register_blueprint(tvl_routes, url_prefix='/tvl')
    app.register_blueprint(pools_routes, url_prefix='/pools')
    
    

    return app
