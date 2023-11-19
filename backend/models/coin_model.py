# Example in models/coin_model.py
from app import db


class Coin(db.Model):
    __tablename__ = 'coins_general'
    id = db.Column(db.Integer, primary_key=True)
    symbol = db.Column(db.String(50))
    name = db.Column(db.String(100))
    image = db.Column(db.String(255))
    current_price = db.Column(db.Float)
    market_cap = db.Column(db.Float)
    market_cap_rank = db.Column(db.Integer)
    fully_diluted_valuation = db.Column(db.Float)
    total_volume = db.Column(db.Float)
    high_24h = db.Column(db.Float)
    low_24h = db.Column(db.Float)
    price_change_24h = db.Column(db.Float)
    price_change_percentage_24h = db.Column(db.Float)
    market_cap_change_24h = db.Column(db.Float)
    market_cap_change_percentage_24h = db.Column(db.Float)
    circulating_supply = db.Column(db.Float)
    total_supply = db.Column(db.Float)
    max_supply = db.Column(db.Float)
    ath = db.Column(db.Float)
    ath_change_percentage = db.Column(db.Float)
    ath_date = db.Column(db.String(50))
    atl = db.Column(db.Float)
    atl_change_percentage = db.Column(db.Float)
    atl_date = db.Column(db.String(50))
    last_updated = db.Column(db.String(50))
    price_change_percentage_14d_in_currency = db.Column(db.Float)
    price_change_percentage_1h_in_currency = db.Column(db.Float)
    price_change_percentage_1y_in_currency = db.Column(db.Float)
    price_change_percentage_200d_in_currency = db.Column(db.Float)
    price_change_percentage_24h_in_currency = db.Column(db.Float)
    price_change_percentage_30d_in_currency = db.Column(db.Float)
    price_change_percentage_7d_in_currency = db.Column(db.Float)

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
                                                    if top else order_column.asc())
        .limit(number_of_coins).all()
        return coins_data_ordered
    else:
        # Handle invalid category
        return []
