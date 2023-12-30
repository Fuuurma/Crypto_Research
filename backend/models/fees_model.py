# models/fees_model.py

from app import db

class Fees(db.Model):
    __tablename__ = 'fees_general'
    __bind_key__ = 'dashboard'
    defillamaId = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    disabled = db.Column(db.String(1))
    displayName = db.Column(db.String(255))
    module = db.Column(db.String(255))
    category = db.Column(db.String(255))
    logo = db.Column(db.String(255))
    change_1d = db.Column(db.Float)
    change_7d = db.Column(db.Float)
    change_1m = db.Column(db.Float)
    change_7dover7d = db.Column(db.Float)
    change_30dover30d = db.Column(db.Float)
    total24h = db.Column(db.Float)
    total48hto24h = db.Column(db.Float)
    total7d = db.Column(db.Float)
    total30d = db.Column(db.Float)
    total14dto7d = db.Column(db.Float)
    total60dto30d = db.Column(db.Float)
    totalAllTime = db.Column(db.Float)
    protocolType = db.Column(db.String(255))
    methodologyURL = db.Column(db.String(255))
    parentProtocol = db.Column(db.String(255))
    latestFetchIsOk = db.Column(db.String(1))
    versionKey = db.Column(db.String(255))
    dailyRevenue = db.Column(db.Float)
    dailyUserFees = db.Column(db.Float)
    dailyHoldersRevenue = db.Column(db.Float)
    dailyCreatorRevenue = db.Column(db.Float)
    dailySupplySideRevenue = db.Column(db.Float)
    dailyProtocolRevenue = db.Column(db.Float)
    dailyBribesRevenue = db.Column(db.Float)
    dailyFees = db.Column(db.Float)
    holdersRevenue30d = db.Column(db.Float)

    def __repr__(self):
        return f"<Fees {self.name}>"
