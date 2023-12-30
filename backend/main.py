from app import (create_app, db)

from flask import (Flask, render_template, jsonify, request, redirect, session, flash, Markup)
from sqlalchemy import MetaData


app = create_app()

if __name__ == '__main__': 
    app.run(debug=True),
    with app.app_context():
            db.init_app(app) 
            # Initialize other SQLAlchemy instances for another databases
            # db_protocols_tvl.init_app(app)
            # db_protocols_historic_tvl_by_chain.init_app(app)
            # db_protocols_historic_tvl_by_tokens.init_app(app)
            # db_coins.init_app(app)