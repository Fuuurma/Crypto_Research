from flask import Blueprint, render_template
from models.coin_model import Coin
from models.protocol_model import Protocol
from models.tvl_historic_model import Tvl_historic
from models.fees_model import Fees
from app import db

from queries import (get_coins_data, get_tvl_data, get_stablecoins_data,
                     get_dex_volume_data, get_fees_data, get_global_tvl, 
                     get_tvl_by_categories, test_coin_data)

main_routes = Blueprint('main', __name__)

@main_routes.route('/', methods = ['GET', 'POST'])
def home():
    coins = get_coins_data()
    tvl = get_tvl_data()
    global_tvl = get_global_tvl()
    tvl_categories = get_tvl_by_categories()
    stables = get_stablecoins_data()
    dex_vol = get_dex_volume_data()
    fees = get_fees_data()
    btc = test_coin_data()
    return render_template('index.html', coins=coins, tvl=tvl, global_tvl=global_tvl,
                           tvl_categories=tvl_categories, dex_vol=dex_vol, fees=fees, stables=stables,
                           btc=btc
                           )
    
    
@main_routes.route('/login', methods = ['GET', 'POST'])
def login():
    
    return render_template('login.html')

@main_routes.route('/new_user', methods = ['GET', 'POST'])
def new_user():
    
    return render_template('new_user.html')



@main_routes.route('/test')
def test():
    # Query the first 10 items from the coins_general table
    coins = Coin.query.limit(10).all()
    protocol = Protocol.query.first()
    tvl_historic = Tvl_historic.query.first()

    return render_template('test.html', d=tvl_historic.date if tvl_historic else "No records found")


