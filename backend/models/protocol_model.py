# models/protocol_model.py

from app import db

class Protocol(db.Model):
    __tablename__ = 'tvl_general'
    __bind_key__ = 'dashboard'
    id = db.Column(db.Integer, primary_key=True)
    index = db.Column( db.Integer, unique = True )
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
    
    @staticmethod
    def get_protocols_data():
        data = Protocol.query.limit( 100 ).all()
        return data 
    
    @staticmethod
    def get_actual_TVL():
        total_tvl = db.session.query(db.func.sum(Protocol.tvl)).scalar()
        return total_tvl
    
    @staticmethod
    def get_dominance_pct(top=5):
        # Order protocols by TVL in descending order and limit to the top N
        top_protocols = Protocol.query.order_by(Protocol.tvl.desc()).limit(top).all()

        # Calculate the total TVL of the top N protocols
        top_protocols_tvl = sum(protocol.tvl for protocol in top_protocols)

        # Calculate the dominance percentage
        total_tvl = Protocol.get_actual_TVL()
        dominance_pct = (top_protocols_tvl / total_tvl) * 100 if total_tvl else 0.0

        data = [ top_protocols_tvl, dominance_pct ]
        return data
    
    @staticmethod
    def get_number_of_protocols():
        total_number = Protocol.query.count()
        return total_number