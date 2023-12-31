# models/protocol_model.py

from app import db

class Protocol( db.Model ):
    __tablename__ = 'tvl_general'
    __bind_key__ = 'dashboard'
    id = db.Column( db.Integer, primary_key=True )
    index = db.Column(  db.Integer, unique = True  )
    name = db.Column( db.String( 70 ) )
    address = db.Column( db.String( 255 ) )
    symbol = db.Column( db.String( 50 ) )
    url = db.Column( db.String( 255 ) )
    description = db.Column( db.Text )
    chain = db.Column( db.String( 50 ) )
    logo = db.Column( db.String( 255 ) )
    gecko_id = db.Column( db.String( 50 ) )
    category = db.Column( db.String( 50 ) )
    twitter = db.Column( db.String( 128 ) )
    mcap = db.Column( db.String( 50 ) )
    audits = db.Column( db.String( 50 ) )
    slug = db.Column( db.String( 50 ) )
    tvl = db.Column( db.Float )
    change_1h = db.Column( db.Float )
    change_1d = db.Column( db.Float )
    change_7d = db.Column( db.Float )

    def __repr__( self ):
        return f"<Protocol { self.name } ({ self.symbol })>"
    
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
    
    @staticmethod
    def get_distinct_chain_names():
        chain_names = db.session.query( Protocol.chain ).distinct().all()
        return [ name[0] for name in chain_names ]
    
    
    @staticmethod
    def get_protocols_by_chain( chain_name ):
        available_chains = Protocol.get_distinct_chain_names()
        if chain_name in available_chains:
            protocols = Protocol.query.filter_by( chain = chain_name ).all()
            return protocols
        else:
            return []
        
    @staticmethod
    def get_protocols_above_tvl( threshold_tvl ):
        protocols = Protocol.query.filter( Protocol.tvl >= threshold_tvl ).all()
        return protocols 
    
    @staticmethod
    def get_all_categories_names():
        categories_names = db.session.query(Protocol.category).distinct().all()
        return [name[0] for name in categories_names]


    
    @staticmethod
    def get_protocols_by_category( category_name ):
        if category_name in Protocol.get_all_categories_names():
            protocols = Protocol.query.filter_by( category=category_name ).all()
            return protocols
        else: return []
        
    @staticmethod
    def get_protocols_with_highest_tvl( limit=5 ):
        protocols = Protocol.query.order_by(Protocol.tvl.desc()).limit( limit ).all()
        return protocols


    @staticmethod
    def search_protocols_by_name( keyword ):
        protocols = Protocol.query.filter( Protocol.name.ilike( f"%{ keyword }%" )).all()
        return protocols


