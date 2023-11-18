# routes/fees_routes.py

from flask import Blueprint, render_template
from models.fees_model import Fees

fees_routes = Blueprint('fees', __name__)

@fees_routes.route('/fees', methods = ['GET', 'POST'])
def fees():
    fees = Fees.query.limit(10).all()
    return render_template('fees.html', fees=fees)

