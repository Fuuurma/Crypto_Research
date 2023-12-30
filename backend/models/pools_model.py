# models/pool_model.py

from app import db

class Pool(db.Model):
    __tablename__ = 'pools_general'
    __bind_key__ = 'dashboard'
    id = db.Column(db.Integer, primary_key=True)
    chain = db.Column(db.String(50))
    project = db.Column(db.String(50))
    symbol = db.Column(db.String(10))
    tvlUsd = db.Column(db.Float)
    apyBase = db.Column(db.Float)
    apyReward = db.Column(db.Float)
    apy = db.Column(db.Float)
    pool = db.Column(db.String(50))
    apyPct1D = db.Column(db.Float)
    apyPct7D = db.Column(db.Float)
    apyPct30D = db.Column(db.Float)
    stablecoin = db.Column(db.String(10))
    ilRisk = db.Column(db.String(3))
    exposure = db.Column(db.String(10))
    poolMeta = db.Column(db.String(255))
    mu = db.Column(db.Float)
    sigma = db.Column(db.Float)
    count = db.Column(db.Integer)
    outlier = db.Column(db.Integer)
    il7d = db.Column(db.Float)
    apyBase7d = db.Column(db.Float)
    apyMean30d = db.Column(db.Float)
    volumeUsd1d = db.Column(db.Float)
    volumeUsd7d = db.Column(db.Float)
    apyBaseInception = db.Column(db.Float)

    def __repr__(self):
        return f"<Pool {self.project} ({self.symbol})>"
