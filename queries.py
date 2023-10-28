from configs import (db_connection)

def get_coins_data():
    with db_connection() as connection:
        # Call the stored procedure and retrieve the results
        result = connection.execute("CALL Get_coins_general_table()")  

        # Convert the result set to a list of dictionaries
        data = [dict(row) for row in result]

        return data
    
    

def get_tvl_data():
    with db_connection() as connection:
        result = connection.execute("CALL Get_tvl_general_table")
        
        data = [dict(row) for row in result]
        
        return data
    
    
    

def get_stablecoins_data():
    with db_connection() as connection:
        result = connection.execute("CALL Get_stablecoins_general_table")
        
        data = [dict(row) for row in result]
        
        return data



def get_dex_volume_data():
    with db_connection() as connection:
        result = connection.execute("CALL Get_dex_volume_general_table")
        data = [dict(row) for row in result]
        return data


def get_fees_data():
    with db_connection() as connection:
        result = connection.execute("CALL Get_fees_general_table")
        data = [dict(row) for row in result]
        return data
