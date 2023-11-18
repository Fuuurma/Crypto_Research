# routes/tvl_routes.py

from flask import Blueprint, render_template
from models.tvl_historic_model import Tvl_historic
from models.protocol_model import Protocol

tvl_routes = Blueprint('tvl', __name__)

@tvl_routes.route('/tvl_historic', methods = ['GET', 'POST'])
def tvl_historic():
    tvl_historic_data = Tvl_historic.query.limit(10).all()
    return render_template('tvl_historic.html', tvl_historic=tvl_historic_data)

@tvl_routes.route('/tvl', methods = ['GET', 'POST'])
def tvl():
    tvl_data = Protocol.query.limit(10).all()
    return render_template('tvl.html', tvl=tvl_data)
