from flask import (Flask, render_template, jsonify, request, redirect, session, flash, Markup)
from sqlalchemy import MetaData
from sqlalchemy import (Table, Column, Integer, String,  Enum, Numeric, DateTime,Date, text)
import pandas as pd
from configs import (db_connection)
from queries import (get_coins_data, get_tvl_data, get_stablecoins_data,
                     get_dex_volume_data, get_fees_data)




app = Flask(__name__)


@app.route('/', methods = ['GET', 'POST'])
def home():
    coins = get_coins_data()
    tvl = get_tvl_data()
    stables = get_stablecoins_data()
    dex_vol = get_dex_volume_data()
    fees = get_fees_data()
    return render_template('index.html', coins = coins, tvl = tvl, stables = stables,
                           dex_vol=dex_vol, fees=fees)




app.secret_key = 'sergi'

if __name__ == '__main__': app.run(debug=True)