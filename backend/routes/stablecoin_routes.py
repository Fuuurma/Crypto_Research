from flask import Blueprint, render_template
from stablecoin_routes import Stablecoin

stablecoin_routes = Blueprint('stablecoins', __name__)

@stablecoin_routes.route('/stablecoins',methods = ['GET', 'POST'])
def stablecoin():
    stablecoin = Stablecoin.query.limit(10).all()
    return render_template('stablecoins.html', stablecoin = stablecoin)