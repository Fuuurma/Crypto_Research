# models/stablecoin_model.py

from app import db

class Stablecoin(db.Model):
    __tablename__ = 'stablecoins_general'
    __bind_key__ = 'dashboard'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    symbol = db.Column(db.String(10))
    gecko_id = db.Column(db.String(50))
    pegType = db.Column(db.String(50))
    priceSource = db.Column(db.String(50))
    pegMechanism = db.Column(db.String(50))
    circulating = db.Column(db.Float)
    circulatingPrevDay = db.Column(db.Float)
    circulatingPrevWeek = db.Column(db.Float)
    circulatingPrevMonth = db.Column(db.Float)
    price = db.Column(db.Float)
    delisted = db.Column(db.Boolean)

    def __repr__(self):
        return f"<Stablecoin {self.name} ({self.symbol})>"
