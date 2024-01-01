# app.py
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_login import LoginManager

# Define multiple SQLAlchemy instances for different databases
db = SQLAlchemy()

# Initialize LoginManager
# login_manager = LoginManager()

def create_app(config_filename=None):
    app = Flask(__name__)

    # Load configuration from file or environment variables
    if config_filename:
        app.config.from_pyfile(config_filename)

    app.template_folder = '../templates'
    app.static_folder = '../static'
    

    # Set up the database connections for different databases
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:240699@127.0.0.1:3306/dashboard'
    app.config['SQLALCHEMY_BINDS'] = {
        'dashboard': 'mysql+pymysql://root:240699@127.0.0.1:3306/dashboard',
        'protocols_tvl': 'mysql+pymysql://root:240699@127.0.0.1:3306/protocols_tvl',
        'protocols_historic_tvl_by_chain': 'mysql+pymysql://root:240699@127.0.0.1:3306/protocols_historic_tvl_by_chain',
        'protocols_historic_tvl_by_tokens': 'mysql+pymysql://root:240699@127.0.0.1:3306/protocols_historic_tvl_by_tokens',
        'coins': 'mysql+pymysql://root:240699@127.0.0.1:3306/coins',
        'users' : 'mysql+pymysql://root:240699@127.0.0.1:3306/users',
        'volume' : 'mysql+pymysql://root:240699@127.0.0.1:3306/dex_volume' 
        # 'stablecoins': 'mysql+pymysql://root:240699@127.0.0.1:3306/stablecoins',
    }

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    

    # login_manager = LoginManager(app)
    
    
    
    # Register blueprints, middleware, etc.
    from routes.main_routes import main_routes
    from routes.fees_routes import fees_routes
    from routes.tvl_routes import tvl_routes
    from routes.pools_routes import pools_routes
    from routes.stablecoin_routes import stablecoin_routes
    from routes.volume_routes import volume_routes
    # from routes.auth_routes import user_routes
    
    app.register_blueprint(main_routes)
    app.register_blueprint(fees_routes, url_prefix='/fees')  
    app.register_blueprint(tvl_routes, url_prefix='/tvl')
    app.register_blueprint(pools_routes, url_prefix='/pools')
    app.register_blueprint( stablecoin_routes, url_prefix = '/stablecoins' )
    app.register_blueprint( volume_routes, url_prefix = '/volume' )
    # app.register_blueprint(user_routes, url_prefix='/user')
    
    # Configure LoginManager
    # login_manager.init_app(app)
    # login_manager.login_view = 'user.login'  # 'user.login' is the endpoint for the login route
    

    db.init_app(app)
    return app
