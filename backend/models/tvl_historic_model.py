# models/tvl_historic_model.py

from app import db
from datetime import datetime

class Tvl_historic(db.Model):
    __tablename__ = 'tvl_historic'
    __bind_key__ = 'dashboard'
    date = db.Column(db.DateTime, primary_key=True)
    tvl = db.Column(db.Float)

    def __repr__(self):
        return f"<Tvl at: {self.date} is ({self.tvl})>"

