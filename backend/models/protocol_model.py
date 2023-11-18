# models/protocol_model.py

from app import db

class Protocol(db.Model):
    __tablename__ = 'tvl_general'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(70))
    address = db.Column(db.String(255))
    symbol = db.Column(db.String(50))
    url = db.Column(db.String(255))
    description = db.Column(db.Text)
    chain = db.Column(db.String(50))
    logo = db.Column(db.String(255))
    gecko_id = db.Column(db.String(50))
    category = db.Column(db.String(50))
    twitter = db.Column(db.String(128))
    mcap = db.Column(db.String(50))
    audits = db.Column(db.String(50))
    slug = db.Column(db.String(50))
    tvl = db.Column(db.Float)
    change_1h = db.Column(db.Float)
    change_1d = db.Column(db.Float)
    change_7d = db.Column(db.Float)

    def __repr__(self):
        return f"<Protocol {self.name} ({self.symbol})>"
