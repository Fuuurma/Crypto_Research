# models/stablecoin_model.py

from app import db

class Stablecoin( db.Model ):
    __tablename__ = 'stablecoins_general'
    __bind_key__ = 'dashboard'
    id = db.Column( db.Integer, primary_key=True )
    name = db.Column( db.String( 128 ) )
    symbol = db.Column( db.String( 10 ) )
    gecko_id = db.Column( db.String( 50 ) )
    pegType = db.Column( db.String( 50 ) )
    priceSource = db.Column( db.String( 50 ) )
    pegMechanism = db.Column( db.String( 50 ) )
    circulating = db.Column( db.Float )
    circulatingPrevDay = db.Column( db.Float )
    circulatingPrevWeek = db.Column( db.Float )
    circulatingPrevMonth = db.Column( db.Float )
    price = db.Column( db.Float )
    market_cap = db.Column( db.Float )
    delisted = db.Column( db.Boolean )


    def __repr__( self ):
        return f"<Stablecoin { self.name } ({ self.symbol } )>"
    
    @staticmethod
    def get_stables_data():
        stables_data = Stablecoin.query.order_by( Stablecoin.market_cap.desc() ).limit( 100 ).all()
        # stables_data = Stablecoin.query.limit(100).order_by(Stablecoin.market_cap.desc()).all()

        return stables_data
    
    @staticmethod
    def get_stablecoin_by_symbol( symbol ):
        stablecoin = Stablecoin.query.filter_by( symbol = symbol ).first()
        return stablecoin

    @staticmethod
    def get_stablecoins_above_price( price_threshold ):
        stablecoins = Stablecoin.query.filter( Stablecoin.price > price_threshold ).all()
        return stablecoins

    @staticmethod
    def get_stablecoins_below_price( price_threshold ):
        stablecoins = Stablecoin.query.filter( Stablecoin.price < price_threshold ).all()
        return stablecoins
    
    @staticmethod
    def get_stables_offpeg():
        below_peg = Stablecoin.query.filter( Stablecoin.price < 0.99 ).count()
        above_peg = Stablecoin.query.filter( Stablecoin.price > 1.01 ).count()
        return below_peg + above_peg

    @staticmethod
    def get_stablecoins_by_peg_type( peg_type ):
        stablecoins = Stablecoin.query.filter_by( pegType = peg_type ).all()
        return stablecoins

    @staticmethod
    def get_stablecoins_by_peg_mechanism( peg_mechanism ):
        stablecoins = Stablecoin.query.filter_by( pegMechanism = peg_mechanism ).all()
        return stablecoins

    @staticmethod
    def get_actual_TVL():
        total_tvl = db.session.query( db.func.sum( Stablecoin.market_cap ) ).scalar()
        return total_tvl
    
    @staticmethod
    def get_number_of_stables():
        total_number = Stablecoin.query.count()
        return total_number
    
    @staticmethod
    def get_dominance_pct( top = 5 ):
        top_stables = Stablecoin.query.order_by( Stablecoin.market_cap.desc() ).limit( top ).all()
        top_stables_tvl = sum(stable.market_cap for stable in top_stables)

        total_tvl = Stablecoin.get_actual_TVL()
        dominance_pct = (top_stables_tvl / total_tvl) * 100 if total_tvl else 0.0
        data = [ top_stables_tvl, dominance_pct ]
        return data