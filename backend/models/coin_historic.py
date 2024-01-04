from app import db
from datetime import datetime

class Coin_Historic(db.Model):
    __bind_key__ = 'coins'
    # the table will need to change simultaniously
    id = db.Column( db.String, primary_key=True )
    date = db.Column( db.DateTime )
    open = db.Column( db.Float )
    high = db.Column( db.Float )
    low = db.Column( db.Float )
    close = db.Column( db.Float )
    sma_10 = db.Column( db.Float )
    sma_25 = db.Column( db.Float )
    sma_50 = db.Column( db.Float )
    sma_100 = db.Column( db.Float )
    ema_10 = db.Column( db.Float )
    ema_25 = db.Column( db.Float )
    ema_50 = db.Column( db.Float )
    ema_100 = db.Column( db.Float )
    daily_return = db.Column( db.Float )
    log_return = db.Column( db.Float )
    volatility = db.Column( db.Float )
    rsi = db.Column( db.Float )
    ema_12 = db.Column( db.Float )
    ema_26 = db.Column( db.Float )
    macd = db.Column( db.Float )
    signal_line = db.Column( db.Float )
    updated_at = db.Column( db.DateTime, default=datetime.utcnow )

    # Define relationships if needed
    # coin = relationship('Coin', back_populates='coin_historic')

    def __repr__(self):
        return f"<Coin_Historic {self.id} - {self.date}>"

    