from flask import Blueprint, render_template
from models.stablecoin_model import Stablecoin

stablecoin_routes = Blueprint('stablecoins', __name__)

@stablecoin_routes.route('/stablecoins',methods = ['GET', 'POST'])
def stablecoin():
    stablecoin = Stablecoin.get_stables_data()
    return render_template('stablecoins.html', stablecoin = stablecoin)