from app import db_coins

class Coin(db_coins.Model):
    __tablename__ = 'coins_general'
    id = db_coins.Column(db_coins.Integer, primary_key=True)
    symbol = db_coins.Column(db_coins.String(50))
    name = db_coins.Column(db_coins.String(100))
    image = db_coins.Column(db_coins.String(255))
    current_price = db_coins.Column(db_coins.Float)
    market_cap = db_coins.Column(db_coins.Float)
    fully_diluted_valuation = db_coins.Column(db_coins.Float)
    total_volume = db_coins.Column(db_coins.Float)
    high_24h = db_coins.Column(db_coins.Float)
    low_24h = db_coins.Column(db_coins.Float)
    price_change_24h = db_coins.Column(db_coins.Float)
    price_change_percentage_24h = db_coins.Column(db_coins.Float)
    circulating_supply = db_coins.Column(db_coins.Float)
    total_supply = db_coins.Column(db_coins.Float)
    max_supply = db_coins.Column(db_coins.Float)
    ath = db_coins.Column(db_coins.Float)
    ath_change_percentage = db_coins.Column(db_coins.Float)
    ath_date = db_coins.Column(db_coins.String(50))
    atl = db_coins.Column(db_coins.Float)
    atl_change_percentage = db_coins.Column(db_coins.Float)
    atl_date = db_coins.Column(db_coins.String(50))
    last_updated = db_coins.Column(db_coins.String(50))
    price_change_1Y = db_coins.Column(db_coins.Float)
    price_change_200d = db_coins.Column(db_coins.Floaty)
    price_change_24h = db_coins.Column(db_coins.Float)
    price_change_30d = db_coins.Column(db_coins.Float)
    price_change_7d = db_coins.Column(db_coins.Float)

    def __repr__(self):
        return f"<Coin: {self.id} ({self.symbol})>"

    
    
# Helper functions
def get_coins_data(page=1, per_page=100):
    coins_data = Coin.query.paginate(page, per_page, error_out=False)
    return coins_data


def get_coin_data(coin_symbol='BTC'):
    coin_data = Coin.query.filter_by(symbol=coin_symbol).first()
    return coin_data

def get_x_coins_by_category(number_of_coins=10, category='market_cap', top=True):
    order_column = getattr(Coin, category, None)
    if order_column is not None:
        coins_data_ordered = Coin.query.order_by(order_column.desc() 
                                                    if top else order_column.asc()).limit(number_of_coins).all()
        return coins_data_ordered
    else:
        # Handle invalid category
        return []
