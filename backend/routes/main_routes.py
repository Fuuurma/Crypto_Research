from flask import Blueprint, render_template
from models.coin_model import (Coin, get_coin_data, get_coins_data)
from models.protocol_model import Protocol # function top 100 tvl
from models.tvl_historic_model import Tvl_historic
from app import db
import request
from queries import (get_coins_data, get_tvl_data, get_stablecoins_data,
                     get_dex_volume_data, get_fees_data, get_global_tvl, 
                     get_tvl_by_categories, test_coin_data)

main_routes = Blueprint('main', __name__)

@main_routes.route('/', methods = ['GET', 'POST'])
def home(): # forget all this functions by the moment. theyre old
    coins = get_coins_data()
    tvl = get_tvl_data()
    global_tvl = get_global_tvl()
    tvl_categories = get_tvl_by_categories()
    stables = get_stablecoins_data()
    dex_vol = get_dex_volume_data()
    fees = get_fees_data()
    btc = test_coin_data()
    
    # new
    page = request.args.get('page', 1, type=int)
    coins_pagination = get_coins_data(page)
    return render_template('index.html', coins=coins, tvl=tvl, global_tvl=global_tvl,
                           tvl_categories=tvl_categories, dex_vol=dex_vol, fees=fees, stables=stables,
                           btc=btc
                           )
    

@main_routes.route('/coins/<string:coin_symbol>')
def individual_coin(coin_symbol):
    # Use coin_symbol to fetch details of the specific coin from the database
    # <a href="{{ url_for('main.coin_detail', coin_symbol=coin.symbol) }}">View Details</a>
    coin = get_coin_data(coin_symbol)
    return render_template('coin.html', coin=coin)

  
  
  
    
    
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


