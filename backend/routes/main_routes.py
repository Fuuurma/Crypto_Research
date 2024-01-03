from flask import Blueprint, render_template
from models.coin_model import ( Coin, get_coin_data, get_coins_data )
from models.protocol_model import (Protocol) # function top 100 tvl
from models.tvl_historic_model import Tvl_historic
from models.stablecoin_model import Stablecoin
from models.volume_historic_model import Volume_Historic
from app import db
import requests
from queries import ( get_tvl_data, get_stablecoins_data,
                     get_dex_volume_data, get_fees_data, get_global_tvl, 
                     get_tvl_by_categories, test_coin_data )

# get_coins_data
main_routes = Blueprint( 'main', __name__ )

@main_routes.route( '/', methods = [ 'GET', 'POST' ] )
def home(): # forget all this functions by the moment. theyre old
    coins = get_coins_data()
    
    tvl = Protocol.get_protocols_data() 
    global_tvl = Protocol.get_actual_TVL() 
    tvl_top5_dominance = Protocol.get_dominance_pct()
    tvl_number_of_protocols = Protocol.get_number_of_protocols()
    tvl_categories = get_tvl_by_categories()
    tvl_plot = Tvl_historic.get_tvl_line_chart()
    
    stables = Stablecoin.get_stables_data() # get_stablecoins_data()
    stables_tvl = Stablecoin.get_actual_TVL()
    number_of_stables = Stablecoin.get_number_of_stables()
    off_peg_number = Stablecoin.get_stables_offpeg()
    stables_top5_dominance = Stablecoin.get_dominance_pct( 5 )
    stables_pie_plot = Stablecoin.get_stablecoins_pie_chart()
    
    dex_vol = get_dex_volume_data()
    vol_plot = Volume_Historic.get_volume_line_chart()
    fees = get_fees_data()
    btc = test_coin_data()
    
    # new
    # page = requests.args.get('page', 1, type=int)
    # coins_pagination = get_coins_data(page)
    return render_template('index.html', coins = coins, tvl = tvl, global_tvl = global_tvl, tvl_top5_dominance = tvl_top5_dominance,
                           tvl_categories = tvl_categories, dex_vol = dex_vol, fees = fees, 
                           stables = stables, stables_tvl = stables_tvl, number_of_stables = number_of_stables, off_peg_number = off_peg_number, stables_top5_dominance = stables_top5_dominance,
                           btc = btc, tvl_number_of_protocols = tvl_number_of_protocols, tvl_plot = tvl_plot, vol_plot = vol_plot, stables_pie_plot= stables_pie_plot
                           
                           )
    

@main_routes.route('/coins/<string:coin_symbol>')
def individual_coin(coin_symbol):
    # Use coin_symbol to fetch details of the specific coin from the database
    # <a href="{{ url_for('main.coin_detail', coin_symbol=coin.symbol) }}">View Details</a>
    coin = get_coin_data(coin_symbol)
    return render_template('coin.html', coin=coin)

  
  
  
    
    
# @main_routes.route('/login', methods = ['GET', 'POST'])
# def login():
    
#     return render_template('login.html')

# @main_routes.route('/new_user', methods = ['GET', 'POST'])
# def new_user():
    
#     return render_template('new_user.html')



@main_routes.route('/test')
def test():
    # Query the first 10 items from the coins_general table
    coins = Coin.query.limit(10).all()
    protocol = Protocol.query.first()
    tvl_historic = Tvl_historic.query.first()

    return render_template('test.html', d=tvl_historic.date if tvl_historic else "No records found")


