# app.py
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_login import LoginManager

# Define multiple SQLAlchemy instances for different databases
db = SQLAlchemy()
db_protocols_tvl = SQLAlchemy()
db_protocols_historic_tvl_by_chain = SQLAlchemy()
db_protocols_historic_tvl_by_tokens = SQLAlchemy()
db_coins = SQLAlchemy()

def create_app(config_filename=None):
    app = Flask(__name__)

    # Load configuration from file or environment variables
    if config_filename:
        app.config.from_pyfile(config_filename)

    app.template_folder = '../templates'
    

    # Set up the database connections for different databases
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:240699@127.0.0.1:3306/dashboard'
    app.config['SQLALCHEMY_BINDS'] = {
        'protocols_tvl': 'mysql+pymysql://root:240699@127.0.0.1:3306/protocols_tvl',
        'protocols_historic_tvl_by_chain': 'mysql+pymysql://root:240699@127.0.0.1:3306/protocols_historic_tvl_by_chain',
        'protocols_historic_tvl_by_tokens': 'mysql+pymysql://root:240699@127.0.0.1:3306/protocols_historic_tvl_by_tokens',
        'coins': 'mysql+pymysql://root:240699@127.0.0.1:3306/coins',
        # 'stablecoins': 'mysql+pymysql://root:240699@127.0.0.1:3306/stablecoins',
    }

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    

    # login_manager = LoginManager(app)
    
    
    
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
