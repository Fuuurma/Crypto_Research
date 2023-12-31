# models/chain_model.py

from app import db

class Chain( db.Model ):
    __tablename__ = 'chains_general'
    __bind_key__ = 'dashboard'
    gecko_id = db.Column( db.String(48), primary_key = True)
    tvl = db.Column( db.Float )
    tokenSymbol = db.Column( db.String( 24 ) )
    cmcId = db.Column( db.Integer )
    market_cap = db.Column( db.Float )
    current_price = db.Column( db.Float )
    image = db.Column( db.String( 255 ) )
    
    def __repr__( self ):
        return f"<Chain { self.gecko_id } ({ self.tokenSymbol })>"
    
    @staticmethod
    def get_chains_data():
        data = Chain.query.limit( 100 ).all()
        return data 
    
    @staticmethod
    def get_chain_data( id ):
        chain = Chain.query.filter( Chain.gecko_id == id ).all()
        return chain
    
    
    
    
    
    # gecko_id, tvl, tokenSymbol, cmcId, name_x, chainId, id, name_y, current_price, market_cap, image
# 'ethereum', '48388589785.20481', 'ETH', '1027', 'Ethereum', '1', 'ethereum', 'Ethereum', '1588.04', '190433125271', 'https://assets.coingecko.com/coins/images/279/large/ethereum.png?1595348880'
