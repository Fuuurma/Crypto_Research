from flask import (Flask, render_template, jsonify, request, redirect, session, flash, Markup)
from sqlalchemy import MetaData
from sqlalchemy import (Table, Column, Integer, String,  Enum, Numeric, DateTime,Date, text)
import pandas as pd
from configs import (db_connection)
from queries import (get_coins_data, get_tvl_data, get_stablecoins_data,
                     get_dex_volume_data, get_fees_data, get_global_tvl, 
                     get_tvl_by_categories, test_coin_data)



app = Flask(__name__)


@app.route('/', methods = ['GET', 'POST'])
def home():
    coins = get_coins_data()
    tvl = get_tvl_data()
    global_tvl = get_global_tvl()
    tvl_categories = get_tvl_by_categories()
    stables = get_stablecoins_data()
    dex_vol = get_dex_volume_data()
    fees = get_fees_data()
    btc = test_coin_data()
    return render_template('index.html', coins = coins, tvl = tvl, global_tvl = global_tvl,
                           tvl_categories = tvl_categories, dex_vol=dex_vol, fees=fees,stables = stables,
                           btc = btc
                           )
    

@app.route('/login', methods = ['GET', 'POST'])
def login():
    
    return render_template('login.html')

@app.route('/new_user', methods = ['GET', 'POST'])
def new_user():
    
    return render_template('new_user.html')


@app.route('/tvl', methods = ['GET', 'POST'])
def tvl():
    
    return render_template('tvl.html')


@app.route('/fees', methods = ['GET', 'POST'])
def fees():
    fees = get_fees_data()
    return render_template('fees.html', fees = fees)


@app.route('/stablecoins', methods = ['GET', 'POST'])
def stablecoins():
    
    return render_template('stablecoins.html')






app.secret_key = 'sergi'

if __name__ == '__main__': app.run(debug=True)