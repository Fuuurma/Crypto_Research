from configs import (db_connection)

def get_coins_data():
    with db_connection() as connection:
        # Call the stored procedure and retrieve the results
        result = connection.execute("CALL Get_coins_general_table()")  

        # Convert the result set to a list of dictionaries
        data = [dict(row) for row in result]

        return data[:100]
    

def test_coin_data():
    with db_connection() as connection:
        # Call the stored procedure and retrieve the results
        result = connection.execute("CALL Get_coins_general_table()")  

        # Convert the result set to a list of dictionaries
        data = [dict(row) for row in result]

        return data[:1]
    
    

def get_tvl_data():
    with db_connection() as connection:
        result = connection.execute("CALL Get_tvl_general_table")
        
        data = [dict(row) for row in result]
        
        return data[:100]

def get_global_tvl():
    with db_connection() as connection:
        result = connection.execute("CALL Get_total_tvl")        
        return result
    
def get_tvl_by_categories():
    with db_connection() as connection:
        result = connection.execute("CALL Get_tvl_by_category")
        
        data = [dict (row) for row in result]
        return data
        
    

def get_stablecoins_data():
    with db_connection() as connection:
        result = connection.execute("CALL Get_stablecoins_general_table")
        
        data = [dict(row) for row in result]
        
        return data[:100]



def get_dex_volume_data():
    with db_connection() as connection:
        result = connection.execute("CALL Get_dex_volume_general_table")
        data = [dict(row) for row in result]
        return data[:100]


def get_fees_data():
    with db_connection() as connection:
        result = connection.execute("CALL Get_fees_general_table")
        data = [dict(row) for row in result]
        return data[:100]
    
    
    
# Old template
# coins = get_coins_data()
#     tvl = get_tvl_data()
#     global_tvl = get_global_tvl()
#     tvl_categories = get_tvl_by_categories()
#     stables = get_stablecoins_data()
#     dex_vol = get_dex_volume_data()
#     fees = get_fees_data()
#     btc = test_coin_data()
    
#     # new
#     # page = requests.args.get('page', 1, type=int)
#     # coins_pagination = get_coins_data(page)
#     return render_template('index.html', coins=coins, tvl=tvl, global_tvl=global_tvl,
#                            tvl_categories=tvl_categories, dex_vol=dex_vol, fees=fees, stables=stables,
#                            btc=btc
#                            )
    


